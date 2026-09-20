from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import wiki_public_content_check as public_check


class PublicContentCheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def write(self, relative: str, content: str | bytes) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")

    def test_reports_violations_without_echoing_values_or_exempting_directories(self) -> None:
        sensitive_value = "super-" + "secret-value-123"
        author_path = "/home/" + "lin/wiki"
        self.write("raw/private.md", f"---\nsources: [session:private-record]\n---\n```text\n{author_path}\n```\n")
        self.write("_meta/config.md", "pass" + f'word = "{sensitive_value}"\n')
        self.write("scripts/key.txt", "-----BEGIN OPENSSH " + "PRIVATE KEY-----\n")
        self.write("notes/endpoint.md", "deliver: telegram:" + "123456789\n")

        report = public_check.build_report(self.root)
        rendered = json.dumps(report)
        rules = {(item["path"], item["rule"]) for item in report["violations"]}

        self.assertIn(("raw/private.md", "author-home-path"), rules)
        self.assertIn(("raw/private.md", "private-provenance"), rules)
        self.assertIn(("_meta/config.md", "literal-secret-assignment"), rules)
        self.assertIn(("scripts/key.txt", "private-key-material"), rules)
        self.assertIn(("notes/endpoint.md", "personal-endpoint-identifier"), rules)
        self.assertNotIn(sensitive_value, rendered)
        self.assertFalse(report["pass"])

    def test_safe_examples_do_not_trigger_violations(self) -> None:
        self.write(
            "concepts/example.md",
            "---\nsources: [docs:https://example.com/public]\n---\n"
            "WIKI_ROOT=/path/to/wiki\n"
            "Product paths may use ~/.hermes or /home/user/project.\n"
            'api_key = "YOUR_API_KEY"\n'
            "api_key=OLOSTEP_API_KEY\n"
            'api_key=os.environ["OPENAI_API_KEY"]\n'
            "api_key=credential\n"
            "The words session_search and project:relative-example are explanatory text.\n",
        )
        report = public_check.build_report(self.root)
        self.assertEqual(report["violations"], [])
        self.assertEqual(report["candidates"], [])
        self.assertTrue(report["pass"])

    def test_catches_common_private_provenance_and_unquoted_secret_forms(self) -> None:
        sensitive_value = "live-" + "secret-value-123"
        self.write("raw/quoted.md", '---\nsources: ["session:private"]\n---\n')
        self.write("raw/singular.md", "---\nsource: session:private\n---\n")
        self.write("raw/artifact.md", "Summary session run " + "20260102-030405 was off-wiki.\n")
        self.write("scripts/env.sh", f"export API_KEY={sensitive_value}\n")

        report = public_check.build_report(self.root)
        rendered = json.dumps(report)
        rules = {(item["path"], item["rule"]) for item in report["violations"]}

        self.assertIn(("raw/quoted.md", "private-provenance"), rules)
        self.assertIn(("raw/singular.md", "private-provenance"), rules)
        self.assertIn(("raw/artifact.md", "private-session-artifact"), rules)
        self.assertIn(("scripts/env.sh", "literal-secret-assignment"), rules)
        self.assertNotIn(sensitive_value, rendered)
        self.assertFalse(report["pass"])

    def test_explicit_synthetic_line_marker_avoids_candidate_noise(self) -> None:
        self.write("examples/synthetic.md", "host: 192.168.1.20  # public-check: synthetic\n")
        author_path = "/home/" + "lin/wiki"
        self.write("examples/not-exempt.md", f"{author_path}  # public-check: synthetic\n")
        report = public_check.build_report(self.root)
        self.assertEqual(report["candidates"], [])
        self.assertIn(
            {"path": "examples/not-exempt.md", "rule": "author-home-path"},
            report["violations"],
        )
        self.assertFalse(report["pass"])

    def test_candidates_are_non_failing_and_cover_unreviewed_files(self) -> None:
        self.write("notes/state.md", "当前运行基线：最近一次 `ok`。金额基线：合成值。\n")  # public-check: synthetic
        self.write("notes/network.md", "host: 192.168.1.20; owner: person@corp.test\n")  # public-check: synthetic
        self.write("assets/blob.bin", b"\xff\xfe")

        report = public_check.build_report(self.root)
        rules = {(item["path"], item["rule"]) for item in report["candidates"]}
        self.assertIn(("notes/state.md", "personal-instance-state"), rules)
        self.assertIn(("notes/state.md", "personal-financial-record"), rules)
        self.assertIn(("notes/network.md", "private-network-address"), rules)
        self.assertIn(("notes/network.md", "personal-email-address"), rules)
        self.assertIn(("assets/blob.bin", "unreviewed-binary-or-non-utf8"), rules)
        self.assertTrue(report["pass"])


if __name__ == "__main__":
    unittest.main()
