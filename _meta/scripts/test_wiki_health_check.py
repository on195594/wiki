from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from datetime import date
from unittest.mock import patch
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
        status: str = "stable",
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
            f"---\ntitle: {name}\ncreated: 2026-01-01\nupdated: 2026-01-01\n"
            f"type: concept\ntags: [{tags}]\nsources: [docs:test]\n"
            f"status: {status}\n{review_line}---\n\n{page_body}",
            encoding="utf-8",
        )
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write(f"- [[{name}]]\n")
        return path

    def issue_codes(self, severity: str) -> set[str]:
        report = wiki_health_check.build_report(self.root)
        return {item["code"] for item in report["issues"][severity]}

    def test_optional_freshness_and_date_boundaries(self):
        p = self.add_formal("freshness")
        original = p.read_text()
        cases = [
            ("", set(), set()),
            ("volatility: high", set(), set()),
            ("volatility: invalid", {"invalid_volatility"}, set()),
            ("volatility:", {"invalid_volatility"}, set()),
            ("verified_at: 2026-02-30", {"malformed_verified_at"}, set()),
            ("verified_at: 20260909", {"malformed_verified_at"}, set()),
            ("verified_at:", {"malformed_verified_at"}, set()),
            ("review_by:", {"malformed_review_by"}, set()),
            ("verified_at: 2026-09-10", {"future_verified_at"}, {"verified_after_updated"}),
            ("verified_at: 2026-09-09", set(), {"verified_after_updated"}),
            ("volatility: high\nverified_at: 2026-01-01", set(), {"missing_review_by"}),
            ("review_by: 2026-09-09", set(), set()),
            ("review_by: 2026-09-08", set(), {"page_due_for_review"}),
            ("volatility: low\nreview_by: bad", {"malformed_review_by"}, set()),
            ("volatility: high\nverified_at: 2026-01-01\nreview_by: 2026-09-10", set(), set()),
        ]
        with patch.object(wiki_health_check, "date", wraps=date) as clock:
            clock.today.return_value = date(2026, 9, 9)
            for metadata, p1, p2 in cases:
                with self.subTest(metadata=metadata):
                    p.write_text(original.replace("status: stable\n", "status: stable\n" + metadata + "\n"))
                    self.assertEqual(self.issue_codes("P1"), p1)
                    report = wiki_health_check.build_report(self.root)
                    self.assertEqual({i["code"] for i in report["issues"]["P2"] if i["path"] == "concepts/freshness.md"}, p2)

    def test_multiline_sources_read_all_items(self):
        p = self.add_formal("block-sources")
        p.write_text(p.read_text().replace("sources: [docs:test]", "sources:\n  - docs:test\n  - /tmp/transient"))
        self.assertIn("tmp_source", self.issue_codes("P2"))

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

    def test_reports_missing_required_frontmatter_field(self) -> None:
        path = self.add_formal("missing-title")
        path.write_text(
            path.read_text(encoding="utf-8").replace("title: missing-title\n", ""),
            encoding="utf-8",
        )
        self.assertIn("missing_frontmatter_field", self.issue_codes("P1"))

    def test_reports_invalid_formal_status(self) -> None:
        self.add_formal("invalid-status", status="current-as-of-2026-01-01")
        self.assertIn("invalid_formal_status", self.issue_codes("P1"))

    def test_allows_closed_query_outside_main_index(self) -> None:
        path = self.add_formal("closed-record", status="closed")
        query = self.root / "queries" / path.name
        query.parent.mkdir()
        path.rename(query)
        index = self.root / "index.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace("- [[closed-record]]\n", ""),
            encoding="utf-8",
        )
        self.assertNotIn("unexpected_unindexed_formal_page", self.issue_codes("P1"))

    def test_reports_near_duplicate_pages(self) -> None:
        body = "# Shared subject\n\n" + "重复知识治理内容用于检测重新摄取。" * 20 + "\n"
        self.add_formal("duplicate-one", body=body)
        self.add_formal("duplicate-two", body=body)
        self.assertIn("near_duplicate_pages", self.issue_codes("P2"))

    def test_reports_illegal_review_sidecar(self) -> None:
        rev_dir = self.root / "_meta" / "reviews"
        rev_dir.mkdir(parents=True)
        (rev_dir / "sample.exit").write_text("0", encoding="utf-8")
        self.assertIn("illegal_review_sidecar", self.issue_codes("P1"))

    def test_reports_unregistered_relation_key(self) -> None:
        body = "# Relation page\n\n" + "context " * 20 + "\n\n## Relations\n\n- invalid_key: [[duplicate-one]]\n"
        self.add_formal("bad-relation", body=body)
        self.assertIn("unregistered_relation_key", self.issue_codes("P2"))

    def test_reports_invalid_relation_format(self) -> None:
        body = "# Format page\n\n" + "context " * 20 + "\n\n## Relations\n\nfree text without dash\n"
        self.add_formal("bad-format", body=body)
        self.assertIn("invalid_relation_format", self.issue_codes("P2"))

    def test_reports_nested_illegal_review_sidecar(self) -> None:
        nested_dir = self.root / "_meta" / "reviews" / "subdir" / "deep"
        nested_dir.mkdir(parents=True)
        (nested_dir / "nested.exit").write_text("0", encoding="utf-8")
        self.assertIn("illegal_review_sidecar", self.issue_codes("P1"))

    def test_reports_invalid_relation_value(self) -> None:
        body = "# Value page\n\n" + "context " * 20 + "\n\n## Relations\n\n- related: arbitrary non-link text\n"
        self.add_formal("bad-value", body=body)
        self.assertIn("invalid_relation_value", self.issue_codes("P2"))


if __name__ == "__main__":
    unittest.main()
