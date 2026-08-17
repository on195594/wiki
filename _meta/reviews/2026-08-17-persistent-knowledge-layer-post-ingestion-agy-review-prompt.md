# AGY post-ingestion review — persistent knowledge layer

You are AGY acting as an independent, read-only Wiki knowledge reviewer.

## Scope

Review exact Wiki commit:

- Commit: `04a38e15bff913c4b5db936b2e8235d97999cb53`
- Subject: `docs: add conflict-aware knowledge primitives`

Primary files:

- `raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md`
- `concepts/hermes-knowledge-architecture.md`
- `index.md`
- `log.md`

Adjacent concepts to inspect for overlap:

- `concepts/hermes-context-layer-operating-rules.md`
- `concepts/hermes-memory-skills-wiki-boundaries.md`
- `concepts/hermes-knowledge-base-operating-flow.md`
- `concepts/progressive-knowledge-system-growth.md`

You may read only these files and the exact commit diff. Do not modify files, create scratch files, run tests, update indexes, commit, or touch memory, skills, cron, MCP, runtime, wrapper, gateway, provider, profile/plugin, credentials or external systems.

## Review goal

Focus on two questions:

1. **Source essence coverage:** Compare the full raw article against the compact addition to `hermes-knowledge-architecture.md`. Determine whether the durable Wiki update captured all *high-value, reusable, vendor-neutral* ideas that are genuinely missing from the existing Wiki. Do not demand that a concept page restate the whole article. Distinguish:
   - source details correctly left in raw;
   - ideas already owned by adjacent concepts;
   - genuinely missing durable ideas that should be added to an existing formal page.
2. **Duplication:** Identify wording or rules in the new concept section that materially duplicate existing pages. Do not flag necessary one-sentence context or source-backed specialization as duplication. Recommend deletion or narrowing only when another page already owns the same durable unit.

## Source boundaries

- Azure services and deployment choices are implementation examples, not Hermes requirements.
- The property-insurance corpus and entities are synthetic.
- Cost figures and token break-even estimates are source-specific.
- Active workflow adoption is out of scope; this is Wiki knowledge quality only.
- The intended landing is raw source plus a compact update to an existing concept, not a new concept page unless the evidence strongly requires one.

## Specific checks

- Did the update preserve the source's key distinction between evidence and compiled knowledge without redundantly recreating the existing Hermes layer map?
- Are Decision, Contradiction and Open Question represented accurately and with the important fields/boundaries?
- Are scoped supersession, effective-date scoping, rationale retention, terminology drift/entity alignment and multi-hop typed relationships either captured, already covered elsewhere, or unjustifiably omitted?
- Is “latest source is not automatically applicable source” stated clearly?
- Is fail-closed unresolved-conflict behavior grounded and not overstated?
- Does the concept correctly separate source claims from local `[推论]`?
- Did the ingestion preserve provenance and source limitations?
- Is the updated index description accurate and proportionate?
- Are extra reverse links or a new formal page actually needed, or would they add ceremony?

## Required output

Use exactly these sections:

### Verdict
`PASS`, `PASS_WITH_NOTES`, or `REQUEST_CHANGES`

### Blocking findings
For each: exact file/section evidence, why it blocks, minimal fix. Write `None` if none.

### Important findings
For each: source evidence, existing-Wiki comparison, and smallest recommended change. Write `None` if none.

### Minor findings
Only concrete, low-cost quality issues. Write `None` if none.

### Coverage matrix
For each durable source idea, classify as one of:
- `CAPTURED_IN_CONCEPT`
- `ALREADY_OWNED_ELSEWHERE`
- `RAW_ONLY_CORRECTLY`
- `MISSING_DURABLE_DELTA`

At minimum cover: evidence/knowledge/orchestrator separation; Decision; Contradiction; Open Question; scoped supersession; effective dates; rationale retention; terminology/entity alignment; multi-hop relationships; write-risk governance; query routing; when not to build; Azure implementation; cost/benchmark claims.

### Duplication assessment
List real duplication and acceptable overlap separately.

### Passes
What the ingestion got right.

### Recommended patches
Give exact bounded patch intent only for confirmed important/blocking findings. Do not propose general expansion. Write `None` if none.

### Recommended next step
Exactly one action.

Treat the review as advisory. Hermes will independently verify every finding against the exact raw and concept files before applying anything.
