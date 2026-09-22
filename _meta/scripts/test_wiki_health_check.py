from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from datetime import date, timezone
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
            f"# {name}\n\n## Summary\n\nThis formal fixture contains enough stable explanatory text "
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
        with (self.root / "log.md").open("a", encoding="utf-8") as log:
            log.write(f"\n[[{name}]]\n")
        return path

    def issue_codes(self, severity: str) -> set[str]:
        report = wiki_health_check.build_report(self.root)
        return {item["code"] for item in report["issues"][severity]}

    @staticmethod
    def volatile_block(
        *,
        verified_at: str = "2026-09-09",
        review_by: str = "2026-09-10",
        source: str = "docs:test",
        claim: str = "This claim is verified only for the stated local scope.",
    ) -> str:
        return (
            "> [!volatile]\n"
            f"> verified_at: {verified_at}\n"
            f"> review_by: {review_by}\n"
            f"> source: {source}\n"
            ">\n"
            f"> {claim}\n"
        )

    def test_optional_freshness_and_date_boundaries(self):
        p = self.add_formal("freshness")
        self.add_formal("freshness-owner", body="# Freshness owner\n\n" + "context " * 20 + "[[freshness]]\n")
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
        for metadata, p1, p2 in cases:
            with self.subTest(metadata=metadata):
                p.write_text(original.replace("status: stable\n", "status: stable\n" + metadata + "\n"))
                report = wiki_health_check.build_report(self.root, today=date(2026, 9, 9))
                self.assertEqual({i["code"] for i in report["issues"]["P1"]}, p1)
                self.assertEqual({i["code"] for i in report["issues"]["P2"] if i["path"] == "concepts/freshness.md"}, p2)

    def test_default_today_uses_utc(self) -> None:
        with patch.object(wiki_health_check, "datetime") as clock:
            clock.now.return_value.date.return_value = date(2026, 9, 9)
            wiki_health_check.build_report(self.root)
        clock.now.assert_called_once_with(timezone.utc)

    def test_local_volatile_dates_and_injected_today(self) -> None:
        path = self.add_formal("local-freshness")
        self.add_formal("local-freshness-owner", body="# Owner\n\n" + "context " * 20 + "[[local-freshness]]\n")
        original = path.read_text(encoding="utf-8")
        cases = [
            ("2026-09-09", "2026-09-10", date(2026, 9, 9), set(), set()),
            ("2026-02-30", "2026-09-10", date(2026, 9, 9), {"malformed_volatile_verified_at"}, set()),
            ("2026-09-09", "20260910", date(2026, 9, 9), {"malformed_volatile_review_by"}, set()),
            ("2026-09-10", "2026-09-11", date(2026, 9, 9), {"future_volatile_verified_at"}, set()),
            ("2026-09-09", "2026-09-08", date(2026, 9, 9), {"invalid_volatile_date_range"}, {"volatile_block_due_for_review"}),
            ("2026-09-01", "2026-09-09", date(2026, 9, 9), set(), set()),
            ("2026-09-01", "2026-09-09", date(2026, 9, 10), set(), {"volatile_block_due_for_review"}),
        ]
        for verified_at, review_by, today, expected_p1, expected_p2 in cases:
            with self.subTest(verified_at=verified_at, review_by=review_by, today=today):
                path.write_text(original + "\n" + self.volatile_block(verified_at=verified_at, review_by=review_by), encoding="utf-8")
                report = wiki_health_check.build_report(self.root, today=today)
                self.assertEqual(
                    {item["code"] for item in report["issues"]["P1"] if item["path"] == "concepts/local-freshness.md"},
                    expected_p1,
                )
                self.assertEqual(
                    {item["code"] for item in report["issues"]["P2"] if item["path"] == "concepts/local-freshness.md"},
                    expected_p2,
                )

    def test_local_volatile_source_must_be_declared(self) -> None:
        body = "# Local source\n\n## Summary\n\n" + "context " * 20 + "\n\n" + self.volatile_block(source="docs:missing")
        self.add_formal("local-source", body=body)
        report = wiki_health_check.build_report(self.root, today=date(2026, 9, 9))
        issues = [item for item in report["issues"]["P1"] if item["path"] == "concepts/local-source.md"]
        self.assertEqual([item["code"] for item in issues], ["volatile_source_not_declared"])
        self.assertEqual(issues[0]["block"], 1)

    def test_multiple_volatile_blocks_are_independent_and_code_examples_are_ignored(self) -> None:
        code_example = (
            "```markdown\n"
            "> [!volatile]\n"
            "> verified_at: not-a-date\n"
            "> review_by: also-not-a-date\n"
            "> source: docs:missing\n"
            ">\n"
            "> This is only a template.\n"
            "```\n"
        )
        body = (
            "# Multiple local claims\n\n## Summary\n\n"
            + "context " * 20
            + "\n\n"
            + self.volatile_block()
            + "\n"
            + self.volatile_block(verified_at="2026-09-01", review_by="2026-09-08", source="docs:missing")
            + "\n"
            + code_example
        )
        self.add_formal("multiple-local-claims", body=body)
        self.add_formal("multiple-local-claims-owner", body="# Owner\n\n" + "context " * 20 + "[[multiple-local-claims]]\n")
        report = wiki_health_check.build_report(self.root, today=date(2026, 9, 9))
        p1 = [item for item in report["issues"]["P1"] if item["path"] == "concepts/multiple-local-claims.md"]
        p2 = [item for item in report["issues"]["P2"] if item["path"] == "concepts/multiple-local-claims.md"]
        self.assertEqual([(item["code"], item["block"]) for item in p1], [("volatile_source_not_declared", 2)])
        self.assertEqual([(item["code"], item["block"]) for item in p2], [("volatile_block_due_for_review", 2)])

    def test_quoted_volatile_text_is_not_treated_as_a_callout(self) -> None:
        body = (
            "# Quoted prose\n\n## Summary\n\n"
            + "context " * 20
            + "\n\n> This quote discusses [!volatile] syntax but is not a callout.\n"
        )
        self.add_formal("quoted-volatile-prose", body=body)
        report = wiki_health_check.build_report(self.root, today=date(2026, 9, 9))
        self.assertNotIn(
            "unsupported_volatile_block",
            {item["code"] for item in report["issues"]["P1"]},
        )

    def test_unsupported_volatile_block_format_is_reported(self) -> None:
        body = (
            "# Unsupported local claim\n\n## Summary\n\n"
            + "context " * 20
            + "\n\n> [!volatile] custom title\n"
            + "> verified_at: 2026-09-09\n"
            + "> review_by: 2026-09-10\n"
            + "> unsupported: value\n"
            + "> Claim without the required separator.\n"
        )
        self.add_formal("unsupported-local-claim", body=body)
        report = wiki_health_check.build_report(self.root, today=date(2026, 9, 9))
        issues = [item for item in report["issues"]["P1"] if item["path"] == "concepts/unsupported-local-claim.md"]
        self.assertEqual([item["code"] for item in issues], ["unsupported_volatile_block"])
        self.assertEqual(issues[0]["block"], 1)

    def test_multiline_sources_read_all_items(self):
        p = self.add_formal("block-sources")
        p.write_text(p.read_text().replace("sources: [docs:test]", "sources:\n  - docs:test\n  - /tmp/transient"))
        self.assertIn("tmp_source", self.issue_codes("P2"))

    def test_reports_broken_wikilink(self) -> None:
        self.add_formal("broken-link", body="# Broken link\n\n" + "context " * 20 + "[[missing-page]]\n")
        self.assertIn("broken_wikilink", self.issue_codes("P0"))

    def test_reports_missing_summary(self) -> None:
        self.add_formal("missing-summary", body="# Missing summary\n\n" + "context " * 20 + "\n")
        self.assertIn("missing_summary", self.issue_codes("P2"))

    def test_reports_broken_relative_markdown_link(self) -> None:
        self.add_formal("broken-markdown", body="# Broken markdown\n\n" + "context " * 20 + "[missing](missing.md)\n")
        self.assertIn("broken_markdown_link", self.issue_codes("P1"))

    def test_reports_index_only_inbound(self) -> None:
        self.add_formal("index-only")
        log = self.root / "log.md"
        log.write_text(log.read_text(encoding="utf-8").replace("\n[[index-only]]\n", "\n"), encoding="utf-8")
        self.assertIn("index_only_inbound", self.issue_codes("P2"))

    def test_reports_orphan_formal_page(self) -> None:
        self.add_formal("orphan")
        (self.root / "index.md").write_text(
            (self.root / "index.md").read_text(encoding="utf-8").replace("- [[orphan]]\n", ""),
            encoding="utf-8",
        )
        (self.root / "log.md").write_text(
            (self.root / "log.md").read_text(encoding="utf-8").replace("\n[[orphan]]\n", "\n"),
            encoding="utf-8",
        )
        self.assertIn("orphan_formal_page", self.issue_codes("P2"))

    def test_resolves_symlinked_root(self) -> None:
        self.add_formal("symlink-root")
        with tempfile.TemporaryDirectory() as alias_dir:
            alias = Path(alias_dir) / "wiki"
            alias.symlink_to(self.root, target_is_directory=True)
            report = wiki_health_check.build_report(alias)
        self.assertNotIn("orphan_formal_page", {item["code"] for item in report["issues"]["P2"]})
        self.assertTrue(report["pass"])

    def test_reports_log_out_of_order(self) -> None:
        log = self.root / "log.md"
        log.write_text(
            log.read_text(encoding="utf-8")
            + "\n## [2026-01-02] newer\n\n## [2026-01-03] older\n",
            encoding="utf-8",
        )
        self.assertIn("log_out_of_order", self.issue_codes("P1"))

    def test_checks_nested_list_links_but_ignores_indented_code(self) -> None:
        self.add_formal(
            "nested-link",
            body="# Nested link\n\n" + "context " * 20 + "\n\n- parent\n    - [[missing-nested-page]]\n",
        )
        self.add_formal(
            "code-example",
            body="# Code example\n\n" + "context " * 20 + "\n\n    [[missing-code-example]]\n",
        )
        report = wiki_health_check.build_report(self.root)
        targets = {item.get("target") for item in report["issues"]["P0"]}
        self.assertIn("missing-nested-page", targets)
        self.assertNotIn("missing-code-example", targets)

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

    def test_reports_binary_raw_source_drift(self) -> None:
        raw = self.root / "raw" / "attachments" / "source.bin"
        raw.parent.mkdir(parents=True)
        raw.write_bytes(b"current bytes\x00")
        manifest = {"raw/attachments/source.bin": hashlib.sha256(b"different bytes\x00").hexdigest()}
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

    def test_reports_non_public_review_artifact(self) -> None:
        rev_dir = self.root / "_meta" / "reviews"
        rev_dir.mkdir(parents=True)
        (rev_dir / "sample.exit").write_text("0", encoding="utf-8")
        self.assertIn("non_public_task_artifact", self.issue_codes("P1"))

    def test_reports_unregistered_relation_key(self) -> None:
        body = "# Relation page\n\n" + "context " * 20 + "\n\n## Relations\n\n- invalid_key: [[duplicate-one]]\n"
        self.add_formal("bad-relation", body=body)
        self.assertIn("unregistered_relation_key", self.issue_codes("P2"))

    def test_reports_invalid_relation_format(self) -> None:
        body = "# Format page\n\n" + "context " * 20 + "\n\n## Relations\n\nfree text without dash\n"
        self.add_formal("bad-format", body=body)
        self.assertIn("invalid_relation_format", self.issue_codes("P2"))

    def test_reports_nested_non_public_review_artifact(self) -> None:
        nested_dir = self.root / "_meta" / "reviews" / "subdir" / "deep"
        nested_dir.mkdir(parents=True)
        (nested_dir / "nested.md").write_text("review transcript", encoding="utf-8")
        self.assertIn("non_public_task_artifact", self.issue_codes("P1"))

    def test_reports_invalid_relation_value(self) -> None:
        body = "# Value page\n\n" + "context " * 20 + "\n\n## Relations\n\n- related: arbitrary non-link text\n"
        self.add_formal("bad-value", body=body)
        self.assertIn("invalid_relation_value", self.issue_codes("P2"))


if __name__ == "__main__":
    unittest.main()
