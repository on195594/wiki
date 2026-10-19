from __future__ import annotations

import io
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from wiki_maintain import check_all, fix_all, install_git_hook, report_freshness


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

        with patch("sys.stdout", new_callable=io.StringIO) as out:
            report_freshness(self.root, days=30, fmt="json")
        report = json.loads(out.getvalue())
        self.assertEqual(report["days"], 30)
        self.assertEqual(report["items"], items)

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

    def test_check_all_preserves_health_severity_contract(self) -> None:
        for severity in ("P0", "P1", "P2"):
            with self.subTest(severity=severity):
                issues = {key: [] for key in ("P0", "P1", "P2")}
                issues[severity] = [{"code": "test-finding", "path": "concepts/test.md", "message": "Review needed"}]
                with (
                    patch("wiki_maintain.run_unit_tests", return_value=True),
                    patch("wiki_maintain.check_catalog", return_value=True),
                    patch("wiki_maintain.build_health_report", return_value={"issues": issues, "pass": severity == "P2"}),
                    patch("wiki_maintain.build_tag_report", return_value={}),
                    patch("wiki_maintain.build_public_content_report", return_value={"candidates": [{"path": "concepts/test.md"}]}),
                    patch("wiki_maintain.check_git_diff", return_value=True),
                    patch("sys.stdout", new_callable=io.StringIO) as out,
                    patch("sys.stderr", new_callable=io.StringIO) as err,
                ):
                    self.assertEqual(check_all(self.root), severity == "P2")
                self.assertIn("test-finding", out.getvalue() + err.getvalue())
                self.assertIn("1 public-content candidates need review", out.getvalue())

    def test_freshness_includes_local_claims_without_page_deadline(self) -> None:
        path = self.root / "concepts" / "claims.md"
        path.parent.mkdir()

        def block(due: str) -> str:
            return (
                "> [!volatile]\n> verified_at: 2026-10-01\n"
                f"> review_by: {due}\n> source: docs:test\n>\n> Scoped claim.\n\n"
            )

        path.write_text(
            "---\ntitle: Claims\nvolatility: low\n---\n# Claims\n"
            + block("2026-10-18") + block("2026-10-19")
            + block("2026-11-18") + block("2026-11-19")
            + "```markdown\n" + block("2026-10-18") + "```\n",
            encoding="utf-8",
        )
        with patch("wiki_maintain.datetime") as clock, patch("sys.stdout", new_callable=io.StringIO) as out:
            clock.now.return_value = datetime(2026, 10, 19, tzinfo=timezone.utc)
            items = report_freshness(self.root, days=30, fmt="json")
        self.assertEqual([(i["block"], i["status"], i["days_left"]) for i in items], [
            (1, "expired", -1), (2, "expiring_soon", 0), (3, "expiring_soon", 30),
        ])
        self.assertEqual(json.loads(out.getvalue())["items"], items)
        self.assertTrue(all(i["source"] == "docs:test" for i in items))
        with patch("wiki_maintain.datetime") as clock, patch("sys.stdout", new_callable=io.StringIO) as out:
            clock.now.return_value = datetime(2026, 10, 19, tzinfo=timezone.utc)
            report_freshness(self.root)
        self.assertIn("concepts/claims.md (block 1)", out.getvalue())

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
