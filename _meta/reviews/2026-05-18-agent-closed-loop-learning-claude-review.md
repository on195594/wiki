# Claude independent review — Agent closed-loop learning wiki ingestion

Date: 2026-05-18
Reviewer: Claude Code 2.1.143
Mode: read-only review requested via `claude -p --permission-mode plan`
Prompt: [[2026-05-18-agent-closed-loop-learning-claude-review-prompt]]

## Review output

`★ Insight ─────────────────────────────────────`
This wiki uses a layered provenance model: raw sources preserve original prose (with an extraction trail), concept pages abstract into durable mechanisms, and cross-links flow bidirectionally. The review checks all three layers for consistency — a pattern worth reusing when auditing any wiki ingestion.
`─────────────────────────────────────────────────`

---

## Review Result

**Verdict: PASS_WITH_MINOR_FIXES**

---

### Blocking

None.

---

### Important

None.

---

### Minor

1. **Concept page is 222 lines** — SCHEMA threshold is ~200. Only 10% over, so no immediate split required. The `## Local operating rule` decision tree (lines 202–211) duplicates the routing checklist already in `hermes-context-layer-operating-rules.md` and is the easiest place to trim.

2. **`index.md` total-page counter is stale** — Header says `Total pages: 79`, but the index lists ~85+ entries. The current ingestion did not worsen this but also did not correct it.

3. **Extra raw-source frontmatter fields are undocumented in SCHEMA.md** — `author`, `source_url`, `original_url`, `published`, `captured`, `extraction_note` are reasonable provenance fields but aren't listed in the schema. Low priority; affects future ingesters more than this ingestion.

---

### Recommended patches

**Patch 1 — condense the duplicated routing table** (`concepts/agent-closed-loop-learning-from-corrections-to-rules.md`, lines 200–211)

Replace the inline decision tree with a pointer:

```markdown
## Local operating rule

在 Hermes 中处理用户纠正时，按 [[hermes-context-layer-operating-rules]] 的
One-screen routing checklist 裁决层级，再参考本页 "When to promote a correction"
判断是否满足晋升条件。
```

Saves ~8 lines, eliminates duplication, brings the page under 215 lines.

**Patch 2 — update index total-page counter** (`index.md`, line 5)

Run `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json` to get the authoritative page count, then update the header.

**Patch 3 — document raw-source optional fields in SCHEMA.md** (optional, low priority)

Under the `## Frontmatter` raw-source note, add a line listing accepted provenance fields so future ingesters follow the same convention.

---

### Review question answers

| # | Question | Assessment |
|---|----------|------------|
| 1 | Scope match | ✓ Raw under `raw/articles/`, one concept under `concepts/`, `index.md`+`log.md` updated, back-links added to the three specified pages, no runtime/memory/skill/cron/MCP changes |
| 2 | Raw source as provenance | ✓ Reads as authentic article prose; `extraction_note` explains the DOM extraction route; two URLs + author + dates preserved |
| 3 | Concept as right unit | ✓ Abstracts product article into a durable mechanism; not product-news-like, not misplaced |
| 4 | Separation of layers | ✓ Three distinct sections: "Directional evidence from the source", "Hermes mapping", "Limitations" |
| 5 | MS numbers as directional only | ✓ Line 104 explicit: "应视为数量级参考，不应硬编码为 Hermes 标准"; no numbers appear as Hermes thresholds |
| 6 | Cross-links | ✓ 9 outbound wikilinks (all thematically appropriate); 3 targeted back-links on approved pages |
| 7 | Structural/schema | Minor: page length 222 lines, stale index counter; all frontmatter valid, all tags in taxonomy |
| 8 | Overclaiming | ✓ Consistently conservative; "文章只能支持建立概念和晋升门槛，不能直接支持自动自改" |

---

### Evidence checked

- `raw/articles/microsoft-power-apps-mcp-closed-loop-learning-2026-05-12.md` — frontmatter, prose vs. summary, URL provenance, extraction note
- `concepts/agent-closed-loop-learning-from-corrections-to-rules.md` — structure, wikilinks, number caveats, Hermes mapping quality, page length, routing-table duplication
- `index.md` — new entry presence, description accuracy, page counter
- `log.md` — entry format, scope description
- `concepts/agent-experience-consolidation-loops.md` — back-link at lines 72, 198
- `concepts/production-ai-agent-evaluation-framework.md` — back-link + "Relationship to closed-loop learning" section (lines 168–171)
- `concepts/hermes-context-layer-operating-rules.md` — back-link in promotion rules (line 197)
- `SCHEMA.md` — frontmatter spec, tag taxonomy, page-length threshold, directory roles
