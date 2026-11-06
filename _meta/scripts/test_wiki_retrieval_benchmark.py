from __future__ import annotations

import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from wiki_retrieval_benchmark import citation_consistency, main, passages, prepare, validate_answers


class RetrievalBenchmarkTests(unittest.TestCase):
    def test_catalog_seeds_and_typed_relation_directions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "concepts").mkdir()
            nodes = {
                "seed-one": ("alpha beta gamma", "", "- depends_on: [[dependency]]\n- refines: [[refinement]]\n- conflicts_with: [[conflict]]\n- related: [[unrelated]]"),
                "seed-two": ("alpha beta", "", ""),
                "dependency": ("Dependency", "alpha beta gamma delta epsilon zeta", ""),
                "refinement": ("Refinement", "", ""),
                "conflict": ("Conflict", "", ""),
                "replacement": ("Replacement", "", "- supersedes: [[seed-one]]"),
                "incoming-conflict": ("Incoming conflict", "", "- conflicts_with: [[seed-two]]"),
                "unrelated": ("Unrelated", "alpha beta gamma delta epsilon zeta", ""),
            }
            for name, (title, body, relations) in nodes.items():
                (root / f"concepts/{name}.md").write_text(
                    f"---\ntitle: {title}\nsources: []\n---\n# {title}\n{body}\n## Relations\n{relations}\n")
            cases = [{"id": "Q1", "question": "alpha beta gamma delta epsilon zeta", "gold_pages": [], "gold_raw": []}]
            catalog = prepare(root, cases, "catalog", limit=2)["cases"][0]
            self.assertEqual(catalog["candidates"], ["concepts/seed-one.md", "concepts/seed-two.md"])
            expanded = prepare(root, cases, "relations", limit=10)["cases"][0]
            self.assertEqual(set(expanded["candidates"]), {f"concepts/{name}.md" for name in nodes if name != "unrelated"})
            # Preserve the documented hybrid protocol; this is not a graph-only ablation.
            self.assertEqual(expanded["candidates"][0], "concepts/dependency.md")

    def test_case_order_does_not_change_evidence_or_run_source_union(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "concepts").mkdir()
            (root / "raw").mkdir()
            cases = []
            for name in ("alpha", "beta"):
                (root / f"concepts/{name}.md").write_text(
                    f"---\ntitle: {name}\nsources: [raw/{name}.md]\n---\n# {name}\n{name} evidence\n")
                (root / f"raw/{name}.md").write_text(f"# {name}\n{name} source\n")
                cases.append({"id": name, "question": name, "gold_pages": [], "gold_raw": []})
            batch = prepare(root, cases, "keyword", limit=1)
            reverse = prepare(root, list(reversed(cases)), "keyword", limit=1)
            single = prepare(root, cases[:1], "keyword", limit=1)
            self.assertEqual(batch["input_sha256"], reverse["input_sha256"])
            self.assertEqual({c["id"]: c for c in batch["cases"]}, {c["id"]: c for c in reverse["cases"]})
            self.assertEqual(batch["cases"][0], single["cases"][0])
            self.assertNotIn("raw/beta.md", single["input_hashes"])
            self.assertNotEqual(batch["input_sha256"], single["input_sha256"])
            self.assertFalse(any(e["path"] == "raw/beta.md" for e in batch["cases"][0]["evidence"]))

    def test_cli_rejects_missing_packet_and_invalid_citations(self) -> None:
        with patch("sys.argv", ["benchmark", "--answers", "missing.json"]), patch("sys.stderr", new_callable=io.StringIO) as err:
            self.assertEqual(main(), 2)
            self.assertIn("must be supplied together", err.getvalue())
        with tempfile.TemporaryDirectory() as tmp:
            packet, answers = Path(tmp) / "packet.json", Path(tmp) / "answers.json"
            packet.write_text(json.dumps({"cases": [{"id": "Q1", "evidence": []}]}))
            answers.write_text(json.dumps([{"id": "Q1", "answer": "Claim", "citations": ["invented"]}]))
            with patch("sys.argv", ["benchmark", "--packet", str(packet), "--answers", str(answers)]), patch("sys.stderr", new_callable=io.StringIO) as err:
                self.assertEqual(main(), 2)
                self.assertIn("citations must refer", err.getvalue())

    def test_packet_budget_unknown_query_and_no_gold_leakage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "concepts").mkdir()
            for name in ("one", "two"):
                (root / f"concepts/{name}.md").write_text(
                    f"---\ntitle: {name}\nsources: []\n---\n# {name}\n\n证据导航 Evidence\n", encoding="utf-8")
            cases = [{"id": "Q1", "question": "未知词 zxqv 证据", "gold_pages": ["concepts/one.md"], "gold_raw": []}]
            first = prepare(root, cases, "keyword", budget=200)
            self.assertLessEqual(first["cases"][0]["evidence_bytes"], 200)
            cases[0]["gold_pages"] = ["concepts/two.md"]
            second = prepare(root, cases, "keyword", budget=200)
            self.assertEqual(first["cases"][0]["evidence"], second["cases"][0]["evidence"])
            self.assertEqual(first["input_sha256"], second["input_sha256"])

    def test_line_spans_and_answer_validation(self) -> None:
        evidence = passages("concepts/a.md", "---\ntitle: A\n---\n# A\nText\n")
        self.assertEqual(evidence[0]["id"], "concepts/a.md:L4-L5")
        packet = {"cases": [{"id": "Q1", "evidence": evidence}]}
        answer = [{"id": "Q1", "answer": "Bounded claim", "citations": [evidence[0]["id"]]}]
        self.assertTrue(validate_answers(packet, answer)["citation_ids_valid"])
        self.assertEqual(citation_consistency(packet, answer, answer)["mean_jaccard"], 1)
        answer[0]["citations"] = []
        self.assertEqual(citation_consistency(packet, answer, answer)["empty_pairs"], 1)
        self.assertIsNone(citation_consistency(packet, answer, answer)["mean_jaccard"])
        answer[0]["citations"] = ["invented"]
        with self.assertRaises(ValueError):
            validate_answers(packet, answer)
        with self.assertRaises(ValueError):
            validate_answers(packet, [])


if __name__ == "__main__":
    unittest.main()
