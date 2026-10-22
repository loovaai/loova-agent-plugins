#!/usr/bin/env python3
"""从插件源目录构建可复现的官网分发包，不打包开发文件或凭据。"""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def encode_json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def archive(files):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(path, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    return output.getvalue()


def release_files():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    version = catalog['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Release version must be semantic version x.y.z.')
    plugin = ROOT / 'plugins/loova'
    for path in ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json']:
        if json.loads((plugin / path).read_text())['version'] != version:
            raise ValueError(f'Version mismatch: {path}')
    if json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())['plugins'][0]['version'] != version:
        raise ValueError('Marketplace version mismatch.')
    expected = {s['name'] for s in catalog['skills']}
    actual = {p.parent.name for p in (plugin / 'skills').glob('*/SKILL.md')}
    if expected != actual or len(expected) != catalog['skill_count']:
        raise ValueError('Catalog and skill directories differ.')
    files = {}
    downloads = {}
    shared = set()
    for skill in catalog['skills']:
        name = skill['name']
        if not re.fullmatch(r'loova-[a-z0-9-]+', name):
            raise ValueError('Invalid skill name.')
        entries = {}
        for relative in ['SKILL.md', 'agents/openai.yaml', 'references/execution.md']:
            data = (plugin / 'skills' / name / relative).read_bytes()
            entries[f'{name}/{relative}'] = data
            files[f'skills/{name}/{relative}'] = data
            if relative == 'SKILL.md' and f'version: "{version}"' not in data.decode():
                raise ValueError(f'Skill version mismatch: {name}')
            if relative == 'references/execution.md':
                shared.add(data)
        skill['path'] = f'skills/{name}/SKILL.md'
        skill['archive'] = f'downloads/{name}-{version}.zip'
        downloads[skill['archive']] = archive(entries)
    if len(shared) != 1:
        raise ValueError('Execution references differ; synchronize all ten copies before publishing.')
    catalog['bundle'] = f'loova-creative-skills-{version}.zip'
    files['catalog.json'] = encode_json(catalog)
    files['README.md'] = (ROOT / 'docs/downloads-README.md').read_bytes()
    files['DEPLOYMENT.md'] = (ROOT / 'docs/DEPLOYMENT.md').read_bytes()
    folder = f'loova-creative-skills-{version}'
    bundle = archive({f'{folder}/{p}': data for p, data in files.items()})
    files.update(downloads)
    files[catalog['bundle']] = bundle
    manifest = {'name': catalog['name'], 'version': version, 'language': 'en', 'files': [
        {'path': p, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
        for p, data in sorted(files.items())
    ]}
    files['manifest.json'] = encode_json(manifest)
    files['SHA256SUMS'] = ''.join(f'{hashlib.sha256(data).hexdigest()}  {p}\n'
                                  for p, data in sorted(files.items())).encode()
    return folder, files


def build(output):
    folder, files = release_files()
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / folder
    deploy = output / f'{folder}-deploy.zip'
    if destination.exists() or deploy.exists():
        raise ValueError('Release already exists. Choose another output directory; published bytes must not be overwritten.')
    destination.mkdir()
    for path, data in files.items():
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    deploy.write_bytes(archive({f'{folder}/{p}': data for p, data in files.items()}))
    return destination, deploy


def openai_package_files():
    """复用同一套 skills，生成只含一个插件根目录的 OpenAI 上传包。"""
    _, release = release_files()
    plugin = ROOT / 'plugins/loova'
    manifest = json.loads((plugin / 'plugin.json').read_text())
    overlay = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
    # 上传包使用 portable 格式，将现有 Codex 展示信息放入官方扩展位置。
    manifest.setdefault('extensions', {}).setdefault('com.openai', {})['interface'] = overlay['interface']
    files = {path: data for path, data in release.items() if path.startswith('skills/')}
    files['plugin.json'] = encode_json(manifest)
    files['mcp.json'] = (plugin / 'mcp.json').read_bytes()
    files['assets/icon.webp'] = (plugin / 'assets/icon.webp').read_bytes()
    return manifest['version'], files


def build_openai(output):
    version, files = openai_package_files()
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / f'loova-openai-{version}.zip'
    # 不覆盖已交付的上传包，修订时使用新的输出目录。
    with destination.open('xb') as handle:
        handle.write(archive(files))
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    parser.add_argument('--openai', action='store_true', help='Build the complete OpenAI plugin upload ZIP')
    args = parser.parse_args()
    try:
        if args.openai:
            bundle = build_openai(args.output)
        else:
            directory, bundle = build(args.output)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Build failed: {exc}\n')
    if not args.openai:
        print(f'Website directory: {directory}')
    print(f'Archive: {bundle}')
