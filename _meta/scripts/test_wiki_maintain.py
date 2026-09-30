from __future__ import annotations

import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from wiki_maintain import fix_all, install_git_hook, report_freshness


class WikiMaintainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_install_git_hook(self) -> None:
        hooks_dir = self.root / ".git" / "hooks"
        hooks_dir.mkdir(parents=True)
        with patch("sys.stdout", new_callable=io.StringIO):
            hook_path = install_git_hook(self.root)
        self.assertTrue(hook_path.exists())
        self.assertTrue(hook_path.stat().st_mode & 0o111)
        content = hook_path.read_text(encoding="utf-8")
        self.assertIn("wiki_maintain.py", content)
        self.assertIn("--staged", content)

        # Existing hook collision test
        foreign_hook = hooks_dir / "pre-commit"
        foreign_hook.write_text("#!/bin/sh\necho custom hook\n", encoding="utf-8")
        with patch("sys.stdout", new_callable=io.StringIO):
            with self.assertRaises(RuntimeError):
                install_git_hook(self.root, force=False)

        # Overwrite with force
        with patch("sys.stdout", new_callable=io.StringIO):
            installed = install_git_hook(self.root, force=True)
        self.assertIn("wiki_maintain.py", installed.read_text(encoding="utf-8"))

    def test_report_freshness(self) -> None:
        concepts = self.root / "concepts"
        concepts.mkdir(parents=True)

        (concepts / "expired-page.md").write_text(
            """---
title: Expired
created: 2026-01-01
updated: 2026-01-01
type: concept
tags: [agent]
sources: [raw/s.md]
status: stable
volatility: high
review_by: 2026-01-02
---
# Expired
## Summary
Text
""",
            encoding="utf-8",
        )

        with patch("sys.stdout", new_callable=io.StringIO):
            items = report_freshness(self.root, days=30)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["status"], "expired")
        self.assertEqual(items[0]["path"], "concepts/expired-page.md")

    def test_fix_all_drift_protection(self) -> None:
        raw_dir = self.root / "raw"
        raw_dir.mkdir(parents=True)
        sample_raw = raw_dir / "sample.md"
        sample_raw.write_text("initial content", encoding="utf-8")

        meta_dir = self.root / "_meta"
        meta_dir.mkdir(parents=True)
        manifest = meta_dir / "raw-source-hashes.json"
        valid_64_hash = "a" * 64
        manifest.write_text(json.dumps({"raw/sample.md": valid_64_hash}), encoding="utf-8")

        # Modifying existing hash should be rejected as drift
        with patch("sys.stdout", new_callable=io.StringIO), patch("sys.stderr", new_callable=io.StringIO):
            success = fix_all(self.root)
        self.assertFalse(success)

    def test_fix_all_structural_invalid_manifest_rejected(self) -> None:
        raw_dir = self.root / "raw"
        raw_dir.mkdir(parents=True)
        (raw_dir / "sample.md").write_text("initial content", encoding="utf-8")

        meta_dir = self.root / "_meta"
        meta_dir.mkdir(parents=True)
        manifest = meta_dir / "raw-source-hashes.json"

        # Test non-dict manifest
        manifest.write_text(json.dumps(["not", "a", "dict"]), encoding="utf-8")
        with patch("sys.stdout", new_callable=io.StringIO), patch("sys.stderr", new_callable=io.StringIO):
            self.assertFalse(fix_all(self.root))

        # Test invalid hash length
        manifest.write_text(json.dumps({"raw/sample.md": "too-short"}), encoding="utf-8")
        with patch("sys.stdout", new_callable=io.StringIO), patch("sys.stderr", new_callable=io.StringIO):
            self.assertFalse(fix_all(self.root))

    def test_fix_all_corrupt_manifest_rejected(self) -> None:
        raw_dir = self.root / "raw"
        raw_dir.mkdir(parents=True)
        (raw_dir / "sample.md").write_text("initial content", encoding="utf-8")

        meta_dir = self.root / "_meta"
        meta_dir.mkdir(parents=True)
        manifest = meta_dir / "raw-source-hashes.json"
        manifest.write_text("NOT_VALID_JSON{", encoding="utf-8")

        with patch("sys.stdout", new_callable=io.StringIO), patch("sys.stderr", new_callable=io.StringIO):
            success = fix_all(self.root)
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()
