`★ Insight ─────────────────────────────────────`
- Raw source frontmatter schema drift is a common wiki hygiene issue: when fields are inlined into the body instead of YAML, the file becomes grep-able by humans but not parseable by tools or future automation.
- The "Related section should mirror body wikilinks" convention matters because automated graph-builders often only read the declared section, not parse prose.
`─────────────────────────────────────────────────`

---

## Review Result

### Verdict: PASS_WITH_MINOR_FIXES

---

### Blocking findings

None.

---

### Important findings

**1. Raw source frontmatter schema inconsistency** (`raw/articles/towardsdatascience-most-ai-agents-built-backwards-2026-05-27.md`, lines 1–9)

Comparing with the peer TDS file `raw/articles/towardsdatascience-agent-planning-operations-research-2026-05-20.md`:

| Field | New file | Peer pattern |
|---|---|---|
| `status` | `captured` | `raw` |
| URL | `sources: [docs:https://...]` | `source_url: https://...` (dedicated field) |
| Author | absent from frontmatter | `author: Destin Gong` |
| Published date | absent from frontmatter | `published: 2026-05-20` |
| Captured date | absent from frontmatter | `captured: 2026-05-21` |
| Extraction note | inline body paragraph | `extraction:` frontmatter key |

`status: captured` is a non-standard value that won't match any tool or query that filters `status: raw`. The bundled `sources: [docs:https://...]` format is non-standard and loses the author and date as queryable fields. These are the only fields worth patching before calling ingestion complete.

---

### Minor suggestions

**1. Related section missing two cited pages** (`concepts/agentic-programming-system-engineering.md`, line 37 vs lines 107–116)

`[[production-ai-agent-evaluation-framework]]` and `[[agent-orchestration-production-tradeoffs]]` are explicitly named in the body as "connected but not replaced" pages, but neither appears in the `## Related` section. Any graph traversal reading only the declared section will miss these edges.

**2. Summary artifact path is a non-portable absolute path** (raw source, line 17)

`/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/...` is a local filesystem reference. It will be a dead pointer on any other host or after a home directory move. Either note it explicitly as "local path, not portable" or drop the line — the extraction note already records what it was used for.

**3. Extraction note is honest but vague about what's missing** (raw source, line 18)

"reader output begins mid-sentence" doesn't say which sentence or how much was lost. A reader opening this file cold can't tell if the intro paragraph or half the article is gone. A one-phrase addition like "approximately the first 1–2 paragraphs of the introduction were not captured" would make the limitation actionable.

**4. `[[production-ai-agent-evaluation-framework]]` and `[[agent-orchestration-production-tradeoffs]]` absent from concept page `tags:`**

The concept page could benefit from an `anti-pattern` tag to make the new built-backwards addition discoverable by tag queries. Currently `tags:` has no anti-pattern signal.

---

### Recommended patches

**Patch 1** — normalize raw source frontmatter to peer schema:

```yaml
---
title: Most AI Agents Fail in Production Because They're Built Backwards
author: Benjamin Nweke
source: Towards Data Science
source_url: https://towardsdatascience.com/most-ai-agents-fail-in-production-because-theyre-built-backwards/
published: 2026-05-27
captured: 2026-05-29
created: 2026-05-29
updated: 2026-05-29
type: raw-source
status: raw
tags: [agent, architecture, orchestration, observability, anti-pattern]
extraction: Jina Reader extraction; reader output begins mid-sentence (opening ~1–2 intro paragraphs not captured), but main body sections, examples, and conclusion are intact. Gemini summary run 20260529-201234 used as off-wiki grounding artifact (local path only).
---
```

Drop lines 17–18 from the body accordingly.

**Patch 2** — add missing Related entries to concept page (`concepts/agentic-programming-system-engineering.md`, after line 116):

```markdown
- [[production-ai-agent-evaluation-framework]]
- [[agent-orchestration-production-tradeoffs]]
```

---

### Layer-boundary assessment

**Clean.** The article is correctly parked at the `raw/` layer. The concept page update is appropriately scoped to an existing page — creating a new page would have duplicated the system-engineering framing already owned by `agentic-programming-system-engineering`. The built-backwards anti-pattern is genuinely new content in the wiki (confirmed: no pre-existing occurrences in `typed-ai-agent-boundaries`, `production-ai-agent-evaluation-framework`, or `agent-orchestration-production-tradeoffs`). The concept page's `Hermes layer routing` section explicitly and correctly declines all active-layer promotions (memory, skill, cron, MCP, runtime, gateway) with sound reasoning. The log entry at line 870–875 accurately records the boundary.
