"""验证发布包的内容一致性、可复现性与校验清单。"""

import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('builder', ROOT / 'scripts/build_release.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class ReleaseTests(unittest.TestCase):
    def test_archives_match_source_and_checksums(self):
        folder, files = builder.release_files()
        self.assertEqual(builder.release_files(), (folder, files))
        catalog = json.loads(files['catalog.json'])
        full = zipfile.ZipFile(io.BytesIO(files[catalog['bundle']]))
        self.assertEqual(len(catalog['skills']), 10)
        for skill in catalog['skills']:
            single = zipfile.ZipFile(io.BytesIO(files[skill['archive']]))
            for relative in ['SKILL.md', 'agents/openai.yaml', 'references/execution.md']:
                name = skill['name']
                expected = (ROOT / 'plugins/loova/skills' / name / relative).read_bytes()
                self.assertEqual(single.read(f'{name}/{relative}'), expected)
                self.assertEqual(full.read(f'{folder}/skills/{name}/{relative}'), expected)
            self.assertIn(skill['path'], files)
        for line in files['SHA256SUMS'].decode().splitlines():
            checksum, path = line.split('  ', 1)
            self.assertEqual(hashlib.sha256(files[path]).hexdigest(), checksum)
        for entry in json.loads(files['manifest.json'])['files']:
            self.assertEqual(len(files[entry['path']]), entry['bytes'])
            self.assertEqual(hashlib.sha256(files[entry['path']]).hexdigest(), entry['sha256'])

    def test_build_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            directory, deploy = builder.build(temp)
            original = deploy.read_bytes()
            with self.assertRaises(ValueError):
                builder.build(temp)
            self.assertEqual(deploy.read_bytes(), original)
            with zipfile.ZipFile(deploy) as z:
                self.assertIsNone(z.testzip())
                self.assertIn(directory.name + '/manifest.json', z.namelist())
