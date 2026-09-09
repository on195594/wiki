from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import wiki_reverse_lookup as reverse


class ReverseLookupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def page(self, name, sources='[docs:source]', body=''):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f'---\ntitle: Fixture\nsources: {sources}\n---\n# Fixture\n{body}\n')
        return p

    def test_source_lists_duplicates_and_formal_scope(self):
        self.page('concepts/b.md', '[docs:source, docs:source]')
        self.page('operations/a.md', '\n  - docs:other\n\n  - docs:source')
        self.page('concepts/comma-block.md', '\n  - docs:https://example.test/a,b')
        self.page('concepts/comma-inline.md', '["docs:https://example.test/a,b"]')
        for name in ('raw/a.md', '_meta/a.md', '_backups/a.md', 'index.md', 'concepts/a.bak.md.bak.x.md'):
            self.page(name)
        self.assertEqual(reverse.lookup(self.root, source='docs:source'), ['concepts/b.md', 'operations/a.md'])
        self.assertEqual(
            reverse.lookup(self.root, source='docs:https://example.test/a,b'),
            ['concepts/comma-block.md', 'concepts/comma-inline.md'],
        )
        self.assertEqual(reverse.lookup(self.root, source='docs:missing'), [])

    def test_inbound_canonical_links_and_dedup(self):
        self.page('concepts/old.md')
        self.page('concepts/new.md', body='## Relations\n- supersedes: [[old]], [[concepts/old.md#claim|label]], [[./old]]\n- conflicts_with: [[old]]\n- depends_on: [[old]]\n- related: []')
        result = reverse.lookup(self.root, page='concepts/old.md')
        self.assertEqual([r['relation'] for r in result], ['conflicts_with', 'depends_on', 'supersedes'])
        self.assertTrue(all(r['declared_by'] == 'concepts/new.md' and r['target'] == 'concepts/old.md' for r in result))
        self.assertEqual(reverse.lookup(self.root, page='concepts/new.md'), [])

    def test_ignore_code_examples(self):
        self.page('concepts/old.md')
        self.page('concepts/examples.md', body='```md\n## Relations\n- supersedes: [[missing]]\n```\n~~~md\n## Relations\n- conflicts_with: [[missing]]\n~~~\n## Relations\n`- supersedes: [[old]]`\n``- related: [[old]]``\n    - supersedes: [[missing]]\n')
        self.assertEqual(reverse.lookup(self.root, page='concepts/old.md'), [])

    def test_ambiguous_and_unresolved_links_error(self):
        self.page('concepts/old.md')
        self.page('queries/old.md')
        p = self.page('concepts/new.md', body='## Relations\n- supersedes: [[old]]')
        with self.assertRaisesRegex(ValueError, 'ambiguous'):
            reverse.lookup(self.root, page='concepts/old.md')
        p.write_text(p.read_text().replace('[[old]]', '[[missing]]'))
        with self.assertRaisesRegex(ValueError, 'unresolved'):
            reverse.lookup(self.root, page='concepts/old.md')

    def test_invalid_inputs_never_return_empty(self):
        p = self.page('concepts/a.md')
        for text in ('# no frontmatter', '---\nsources: [unterminated\n---\n# Bad\n', '---\nsources:\n  bad: mapping\n---\n# Bad\n', '---\nsources: []\nsources: []\n---\n# Bad\n', '---\nsources: [docs:a,,docs:b]\n---\n# Bad\n', '---\nsources: [\"unclosed]\n---\n# Bad\n'):
            with self.subTest(text=text):
                p.write_text(text)
                with self.assertRaises(ValueError):
                    reverse.lookup(self.root, source='docs:none')
        p.write_bytes(b'\xff')
        with self.assertRaises(ValueError):
            reverse.lookup(self.root, source='docs:none')
        for page in ('../outside.md', '/tmp/outside.md', 'absent.md'):
            with self.assertRaises(ValueError):
                reverse.lookup(self.root, page=page)
        with self.assertRaises(ValueError):
            reverse.lookup(self.root / 'missing', source='x')

    def test_directory_read_errors_are_not_empty_matches(self):
        with patch.object(reverse.os, "scandir", side_effect=PermissionError("unreadable directory")):
            with self.assertRaises(PermissionError):
                reverse.lookup(self.root, source="docs:none")

    def test_cli_errors_have_no_success_output(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = reverse.main(['--root', str(self.root), '--page', 'missing.md'])
        self.assertEqual(code, 2)
        self.assertEqual(out.getvalue(), '')
        self.assertIn('error', err.getvalue())
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            reverse.main(['--source', 'x', '--page', 'y'])


if __name__ == '__main__':
    unittest.main()
