from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("wiki_health_check.py")
SPEC = importlib.util.spec_from_file_location("wiki_health_check", MODULE_PATH)
assert SPEC and SPEC.loader
wiki_health_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wiki_health_check)


class WikiHealthCheckRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "_meta").mkdir()
        (self.root / "SCHEMA.md").write_text(
            "# Wiki Schema\n\n## Tag Taxonomy\n\n- known-tag\n\n"
            "## Page Thresholds\n\nRegistered tags are enforced for formal pages.\n",
            encoding="utf-8",
        )
        (self.root / "index.md").write_text(
            "# Wiki Index\n\nThis fixture index is intentionally long enough to avoid "
            "unrelated tiny-file findings during focused regression checks.\n",
            encoding="utf-8",
        )
        (self.root / "log.md").write_text(
            "# Wiki Log\n\nThis fixture log is intentionally long enough to avoid "
            "unrelated tiny-file findings during focused regression checks.\n",
            encoding="utf-8",
        )
        (self.root / "_meta" / "raw-source-hashes.json").write_text(
            "{}\n", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def add_formal(
        self,
        name: str,
        *,
        tags: str = "known-tag",
        review_by: str | None = None,
        body: str | None = None,
    ) -> Path:
        path = self.root / "concepts" / f"{name}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        review_line = f"review_by: {review_by}\n" if review_by else ""
        page_body = body or (
            f"# {name}\n\nThis formal fixture contains enough stable explanatory text "
            "to avoid unrelated tiny-file findings while exercising one health rule only.\n"
        )
        path.write_text(
            f"---\ntitle: {name}\ntags: [{tags}]\nsources: [docs:test]\n"
            f"status: stable\n{review_line}---\n\n{page_body}",
            encoding="utf-8",
        )
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write(f"- [[{name}]]\n")
        return path

    def issue_codes(self, severity: str) -> set[str]:
        report = wiki_health_check.build_report(self.root)
        return {item["code"] for item in report["issues"][severity]}

    def test_reports_broken_wikilink(self) -> None:
        self.add_formal("broken-link", body="# Broken link\n\n" + "context " * 20 + "[[missing-page]]\n")
        self.assertIn("broken_wikilink", self.issue_codes("P0"))

    def test_reports_unregistered_tag(self) -> None:
        self.add_formal("unknown-tag", tags="not-registered")
        self.assertIn("unregistered_tag", self.issue_codes("P1"))

    def test_reports_raw_source_drift(self) -> None:
        raw = self.root / "raw" / "articles" / "source.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("captured source text\n", encoding="utf-8")
        (self.root / "log.md").write_text(
            (self.root / "log.md").read_text(encoding="utf-8")
            + "\nReferenced source: raw/articles/source.md\n",
            encoding="utf-8",
        )
        manifest = {"raw/articles/source.md": hashlib.sha256(b"different\n").hexdigest()}
        (self.root / "_meta" / "raw-source-hashes.json").write_text(
            json.dumps(manifest), encoding="utf-8"
        )
        self.assertIn("raw_source_drift", self.issue_codes("P1"))

    def test_reports_malformed_review_by(self) -> None:
        self.add_formal("bad-review-date", review_by="soon")
        self.assertIn("malformed_review_by", self.issue_codes("P1"))

    def test_reports_near_duplicate_pages(self) -> None:
        body = "# Shared subject\n\n" + "重复知识治理内容用于检测重新摄取。" * 20 + "\n"
        self.add_formal("duplicate-one", body=body)
        self.add_formal("duplicate-two", body=body)
        self.assertIn("near_duplicate_pages", self.issue_codes("P2"))


if __name__ == "__main__":
    unittest.main()
