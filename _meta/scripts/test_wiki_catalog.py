from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from wiki_catalog import build_catalog, check_catalog, extract_relations, write_catalog


class WikiCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_extract_relations(self) -> None:
        body = """# Sample

Some text.

## Relations

- depends_on: [[other-page]]
- depends_on: [[second-dep]]
- conflicts_with: []
- related: [[rel1]], [[rel2]]
- related: [[rel3]]

## Related
- [[other-page]]
"""
        rels = extract_relations(body)
        self.assertEqual(rels["depends_on"], ["other-page", "second-dep"])
        self.assertEqual(rels["conflicts_with"], [])
        self.assertEqual(rels["related"], ["rel1", "rel2", "rel3"])

    def test_build_and_check_catalog(self) -> None:
        # Create minimal repo structure
        (self.root / "index.md").write_text("# Index\n- [[sample-concept]]\n", encoding="utf-8")
        concepts = self.root / "concepts"
        concepts.mkdir()
        (concepts / "sample-concept.md").write_text(
            """---
title: Sample Concept
created: 2026-09-30
updated: 2026-09-30
type: concept
tags: [agent, testing]
sources: [raw/source.md]
status: stable
description: A sample concept for testing.
aliases: [sample]
volatility: low
---

# Sample Concept

## Summary
A sample page.

## Relations

- related: [[index]]
""",
            encoding="utf-8",
        )

        catalog = build_catalog(self.root)
        self.assertEqual(catalog["total_pages"], 1)
        self.assertEqual(catalog["format"], "okf-bundle-catalog")
        page = catalog["pages"][0]
        self.assertEqual(page["path"], "concepts/sample-concept.md")
        self.assertEqual(page["title"], "Sample Concept")
        self.assertEqual(page["description"], "A sample concept for testing.")
        self.assertEqual(page["volatility"], "low")
        self.assertEqual(page["relations"]["related"], ["index"])

        # Write catalog and check
        cat_file = write_catalog(self.root)
        self.assertTrue(cat_file.exists())
        self.assertTrue(check_catalog(self.root))

        # Modify a file and check should fail
        (concepts / "sample-concept.md").write_text(
            (concepts / "sample-concept.md").read_text(encoding="utf-8").replace("low", "high"),
            encoding="utf-8",
        )
        self.assertFalse(check_catalog(self.root))


if __name__ == "__main__":
    unittest.main()
