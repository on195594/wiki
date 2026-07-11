# AGY read-only review: AI Agent memory-strategy decision-tree wiki update

## Role and boundary

You are an independent reviewer. Review the listed files under `/home/lin/wiki` in read-only mode.

Do not edit, create, delete, rename, or commit files. Do not change Hermes memory, skills, config, cron, MCP, runtime, wrappers, gateway, profiles/plugins, prompts, or core code. Recommendations must remain wiki-only and advisory.

## Files under review

Primary:

- `raw/articles/machinelearningmastery-ai-agent-memory-strategy-decision-tree-2026-07-11.md`
- `concepts/hermes-memory-skills-wiki-boundaries.md`
- `concepts/hermes-context-layer-operating-rules.md`
- `concepts/agent-context-engineering.md`
- `concepts/hermes-memory-governance-notes.md`
- `index.md`
- `log.md`

Adjacent concepts for overlap and ownership checks:

- `concepts/hermes-layer-routing-decision-checklist.md`
- `concepts/hermes-context-engineering-design-priorities.md`
- `concepts/hermes-knowledge-architecture.md`

## Source and intended decision

Source article:
`https://machinelearningmastery.com/choosing-the-right-ai-agent-memory-strategy-a-decision-tree-approach/`

Intended landing:

- raw source plus updates to existing canonical concepts;
- no new formal concept page;
- no Hermes `memory` write;
- no active skill/reference patch;
- no Zep, Mem0, Memory Bank, database, MCP, runtime, config, cron, or project pilot adoption.

The durable unit is a mapping from working/semantic/episodic/procedural memory to distinct Hermes layers, plus five routing questions based on persistence, session lifetime, fact-vs-event semantics, retrieval scale, and maturity as a reusable procedure.

## Parent deterministic validation before review

- Wiki health check: PASS
- Formal pages: 95
- Raw pages: 55
- Index wikilinks: 95
- P0/P1/P2: 0/0/0
- `git diff --check`: PASS

## Review questions

1. Is updating existing pages preferable to creating a new concept, or has the update overloaded `hermes-memory-skills-wiki-boundaries`?
2. Does the raw note preserve provenance and clearly separate source text from local synthesis?
3. Is the mapping from cognitive-memory labels to Hermes layers accurate, especially:
   - working memory → session/project state;
   - semantic memory → bounded facts or source-backed wiki knowledge;
   - episodic memory → session/project/log/raw evidence;
   - procedural memory → validated skills/references?
4. Does any wording incorrectly imply that all semantic knowledge belongs in Hermes `memory`, or that historical events become current facts?
5. Are source claims, product examples, Hermes-local implications, and unverified automation assumptions separated clearly?
6. Do cross-page additions duplicate too much content or blur canonical ownership?
7. Is the no-active-promotion boundary explicit and consistent?
8. Identify broken links, metadata drift, contradictory wording, unsupported claims, or missing high-value caveats.

## Required output

Use exactly these headings:

- `Verdict`: PASS / PASS_WITH_MINOR_FIXES / REQUEST_CHANGES
- `Blocking`
- `Important`
- `Minor`
- `Passes`
- `Recommended patches`

For each finding, cite the file and exact heading or quoted text. Keep fixes minimal and wiki-only. If a category has no findings, write `None`.
