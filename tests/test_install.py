"""验证安装器的覆盖保护、备份恢复路径和完整引用。"""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install_skills.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_dry_run_and_install_update(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'skills'
            installer.install(target, dry_run=True)
            self.assertFalse(target.exists())
            installer.install(target)
            self.assertEqual(len(list(target.glob('*/SKILL.md'))), 10)
            first = next(target.glob('*/SKILL.md'))
            first.write_text('user modification', encoding='utf-8')
            unrelated = target / 'unrelated.txt'
            unrelated.write_text('keep', encoding='utf-8')
            with self.assertRaises(ValueError):
                installer.install(target)
            self.assertEqual(first.read_text(), 'user modification')
            installer.install(target, update=True)
            backups = list(Path(temp).glob('loova-skills-backup-*'))
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0] / first.relative_to(target)).read_text(), 'user modification')
            self.assertEqual(unrelated.read_text(), 'keep')
            for skill in target.glob('*/SKILL.md'):
                self.assertTrue((skill.parent / 'references/execution.md').is_file())

    def test_symlink_and_source_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(installer.SOURCE, update=True)
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'skills'
            target.mkdir()
            name = next(installer.SOURCE.iterdir()).name
            (target / name).symlink_to(installer.SOURCE / name)
            with self.assertRaises(ValueError):
                installer.install(target, update=True)

    def test_manifests_and_catalog(self):
        plugin = ROOT / 'plugins/loova'
        for manifest in ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json']:
            data = json.loads((plugin / manifest).read_text())
            self.assertEqual(data['name'], 'loova')
            self.assertEqual(data['version'], '2.1.4')
        for config in ['mcp.json', '.mcp.json']:
            server = json.loads((plugin / config).read_text())['mcpServers']['loova']
            self.assertEqual(server['url'], 'https://mcp.loova.ai/mcp')
        catalog = json.loads((ROOT / 'catalog.json').read_text())
        self.assertEqual(len(catalog['skills']), 10)
        for skill in catalog['skills']:
            self.assertTrue((ROOT / skill['path']).is_file())


if __name__ == '__main__':
    unittest.main()
