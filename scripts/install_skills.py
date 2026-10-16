#!/usr/bin/env python3
"""将自包含 Skills 安装到用户明确指定的目录，不修改 MCP 或登录配置。"""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile

SOURCE = Path(__file__).resolve().parents[1] / 'plugins' / 'loova' / 'skills'


def install(target, update=False, dry_run=False):
    target = Path(target).expanduser().resolve()
    if target == SOURCE or SOURCE in target.parents or target in SOURCE.parents:
        raise ValueError('Target must not overlap the source repository.')
    skills = sorted(p for p in SOURCE.iterdir() if (p / 'SKILL.md').is_file())
    if not skills:
        raise ValueError('No skills found in the repository.')
    # 在写入前检查所有冲突，默认不覆盖已有安装。
    for skill in skills:
        dest = target / skill.name
        if dest.is_symlink():
            raise ValueError(f'Refusing symlink destination: {dest}')
        if dest.exists() and not update:
            raise ValueError(f'Already exists: {dest}. Use --update to back it up and replace it.')
    if dry_run:
        for skill in skills:
            print(f'Would install: {target / skill.name}')
        return
    target.mkdir(parents=True, exist_ok=True)
    backup = None
    for skill in skills:
        dest = target / skill.name
        with tempfile.TemporaryDirectory(prefix='.loova-stage-', dir=target) as temp:
            staged = Path(temp) / skill.name
            shutil.copytree(skill, staged)
            old = None
            if dest.exists():
                if backup is None:
                    # 备份放在 Skills 目录外，避免被客户端重复发现。
                    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
                    backup = Path(tempfile.mkdtemp(prefix=f'loova-skills-backup-{stamp}-', dir=target.parent))
                old = backup / skill.name
                dest.rename(old)
            try:
                staged.rename(dest)
            except OSError:
                if old is not None:
                    old.rename(dest)
                raise
        print(f'Installed: {dest}')
    if backup:
        print(f'Previous skills preserved at: {backup}')
    print('Skills installed. Connect and authorize Loova MCP separately; restart your agent session.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, help='The skill directory supported by your agent')
    parser.add_argument('--update', action='store_true', help='Back up existing Loova skills before replacement')
    parser.add_argument('--dry-run', action='store_true', help='Check and print destinations without writing')
    args = parser.parse_args()
    try:
        install(args.target, args.update, args.dry_run)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Installation failed: {exc}\n')


if __name__ == '__main__':
    main()
