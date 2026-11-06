#!/usr/bin/env python3
"""Prepare bounded evidence packets; never call a model or grade semantic truth."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

from wiki_catalog import build_catalog
from wiki_health_check import extract_frontmatter, strip_code
from wiki_reverse_lookup import sources
from wiki_root import resolve_root

BENCHMARK_PAGE = "queries/wiki-cross-source-evidence-navigation-benchmark.md"
STRATEGIES = ("keyword", "catalog", "relations")


def terms(text: str) -> set[str]:
    # Character bigrams let Chinese queries work without a tokenizer dependency.
    result = set(re.findall(r"[a-z0-9_]{2,}", text.lower()))
    for part in re.findall(r"[\u4e00-\u9fff]+", text):
        result.update(part[i:i + 2] for i in range(len(part) - 1))
    return result


def score(query: set[str], text: str, weights: dict[str, float]) -> float:
    return sum(weights.get(t, 1.0) for t in query & terms(text))


def passages(path: str, text: str) -> list[dict]:
    """Stable line spans within an input hash, with enough local context to cite."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0] == "---":
        start = next((i + 1 for i in range(1, len(lines)) if lines[i] == "---"), 0)
    result = []
    for i in range(start, len(lines), 12):
        content = "\n".join(lines[i:i + 12])
        if content.strip():
            end = min(i + 12, len(lines))
            result.append({"id": f"{path}:L{i + 1}-L{end}", "path": path, "text": content})
    return result


def ratio(found: set[str], gold: set[str]) -> dict:
    return {"precision": len(found & gold) / len(found) if found else None,
            "recall": len(found & gold) / len(gold) if gold else None}


def prepare(root: Path, cases: list[dict], strategy: str, limit: int = 4, budget: int = 9000) -> dict:
    pages = {p["path"]: p for p in build_catalog(root)["pages"] if p["path"] != BENCHMARK_PAGE}
    texts = {p: (root / p).read_text(encoding="utf-8") for p in pages}
    metadata = {p: " ".join([v["title"], v["description"], *v["aliases"], *v["tags"]]) for p, v in pages.items()}
    tokens = {p: terms(strip_code(t)) for p, t in texts.items()}
    weights = {t: math.log(1 + len(pages) / (1 + sum(t in ts for ts in tokens.values())))
               for t in set().union(*(terms(c["question"]) for c in cases))}
    by_slug = {Path(p).stem: p for p in pages}
    inputs = dict(texts)
    results = []
    for case in cases:
        q = terms(case["question"])
        base = texts if strategy == "keyword" else metadata
        ranked = sorted(pages, key=lambda p: (-score(q, base[p], weights), p))
        candidates = ranked[:limit]
        if strategy == "relations":
            # This is a hybrid: metadata seeds, typed expansion, then full-text
            # reranking. Against catalog alone it cannot isolate graph benefit.
            pool = set(ranked[:2])
            for p in ranked[:2]:
                rels = pages[p]["relations"]
                for kind in ("depends_on", "refines", "conflicts_with"):
                    pool.update(by_slug[s] for s in rels.get(kind, []) if s in by_slug)
                # Incoming replacement and conflict edges are safety candidates.
                for other, entry in pages.items():
                    if any(Path(p).stem in entry["relations"].get(k, []) for k in ("supersedes", "conflicts_with")):
                        pool.add(other)
            candidates = sorted(pool, key=lambda p: (-score(q, texts[p], weights), p))[:limit]
        evidence = []
        source_paths = set()
        for p in candidates:
            chunks = passages(p, texts[p])
            evidence.extend(sorted(chunks, key=lambda x: (-score(q, x["text"], weights), x["id"]))[:2])
            source_paths.update(s for s in sources(extract_frontmatter(texts[p]) or "") if s.startswith("raw/") and (root / s).is_file())
        raw_chunks = []
        for p in sorted(source_paths):
            inputs[p] = (root / p).read_text(encoding="utf-8")
            raw_chunks.extend(passages(p, inputs[p]))
        evidence.extend(sorted(raw_chunks, key=lambda x: (-score(q, x["text"], weights), x["id"]))[:3])
        # Same selection and byte budget for all three strategies. No mid-span truncation.
        evidence.sort(key=lambda x: (-score(q, x["text"], weights), x["id"]))
        selected, used = [], 0
        for e in evidence:
            size = len(json.dumps(e, ensure_ascii=False).encode())
            if used + size <= budget:
                selected.append(e)
                used += size
        results.append({"id": case["id"], "question": case["question"], "candidates": candidates,
                        "evidence": selected, "evidence_bytes": used,
                        "formal_retrieval": ratio(set(candidates), set(case["gold_pages"])),
                        "raw_retrieval": ratio({e["path"] for e in selected if e["path"].startswith("raw/")}, set(case["gold_raw"]))})
    # Run-level source union, not a per-case/prompt/protocol fingerprint.
    # Only each case's source_paths feeds its raw_chunks; inputs is bookkeeping.
    hashes = {p: hashlib.sha256(t.encode()).hexdigest() for p, t in sorted(inputs.items())}
    fingerprint = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    return {"strategy": strategy, "input_sha256": fingerprint, "input_hashes": hashes,
            "page_limit": limit, "evidence_byte_budget": budget, "cases": results}


def validate_answers(packet: dict, answers: list[dict]) -> dict:
    expected = {c["id"]: c for c in packet["cases"]}
    if len(answers) != len(expected) or {a["id"] for a in answers} != set(expected):
        raise ValueError("answers must cover every case exactly once")
    for answer in answers:
        allowed = {e["id"] for e in expected[answer["id"]]["evidence"]}
        if not isinstance(answer.get("answer"), str) or not answer["answer"].strip():
            raise ValueError("each answer needs nonempty answer text")
        citations = answer.get("citations")
        if not isinstance(citations, list) or any(not isinstance(c, str) or c not in allowed for c in citations):
            raise ValueError("citations must refer to evidence in this packet")
    return {"cases": len(answers), "citation_ids_valid": True, "semantic_correctness": "NOT_GRADED"}


def citation_consistency(packet: dict, first: list[dict], second: list[dict]) -> dict:
    validate_answers(packet, first)
    validate_answers(packet, second)
    other = {a["id"]: set(a["citations"]) for a in second}
    values = {}
    for a in first:
        left, right = set(a["citations"]), other[a["id"]]
        values[a["id"]] = len(left & right) / len(left | right) if left | right else None
    valid = [v for v in values.values() if v is not None]
    return {"per_case_jaccard": values, "mean_jaccard": sum(valid) / len(valid) if valid else None,
            "empty_pairs": len(values) - len(valid), "scope": "two answers to the same fixed evidence packet; not retrieval stability or correctness"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root")
    parser.add_argument("--strategy", choices=STRATEGIES, default="keyword")
    parser.add_argument("--answers", type=Path, help="Validate saved answers against a packet")
    parser.add_argument("--packet", type=Path)
    parser.add_argument("--repeat-answers", type=Path, help="Compare a second isolated answer run")
    args = parser.parse_args()
    try:
        if args.answers or args.packet or args.repeat_answers:
            if not (args.answers and args.packet):
                raise ValueError("--answers and --packet must be supplied together")
            result = validate_answers(json.loads(args.packet.read_text()), json.loads(args.answers.read_text()))
            if args.repeat_answers:
                result["citation_consistency"] = citation_consistency(json.loads(args.packet.read_text()), json.loads(args.answers.read_text()), json.loads(args.repeat_answers.read_text()))
        else:
            root = resolve_root(args.root)
            cases = json.loads((root / "_meta/retrieval-benchmark.json").read_text())["cases"]
            result = prepare(root, cases, args.strategy)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
