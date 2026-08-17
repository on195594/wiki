# AGY focused adjudication snapshot — persistent knowledge layer

Review this bounded snapshot only. No tools, file reads, writes, commands or external research are needed.

## Prior result

You previously returned `PASS` for a Wiki ingestion. Parent verification found three possible false negatives. Reassess them using the exact excerpts below.

## Source excerpts

### Layer purpose and routing

- Evidence: answers what source material is relevant now; optimized for recall, exact wording, citation and freshness.
- Knowledge: answers what the system has already worked out and currently believes; optimized for continuity, relationships, synthesis and reuse.
- Orchestrator: decides which layer is needed to answer safely; optimized for routing, risk and temporal scope.
- Exact policy wording should route to evidence; “why was this decided?” should route to knowledge.
- Not every question needs both layers; sending everything to both is expensive and slow.
- Temporal checks should constrain candidates before similarity ranking.
- Contradiction checks are an output gate regardless of route.

### Terminology drift

The source says the same concept can appear under several terms. Without entity resolution the Wiki grows separate pages that disagree by omission; with it, one canonical page carries several aliases and any alias retrieves the same object.

### Multi-hop relationships

The source gives a four-hop explanation chain across claim notes, a guideline, a concept and a policy clause. It says top-k similarity ranks but does not traverse; typed relationships traverse.

## Current concept addition

```text
Decision: saves rule/conclusion, scope, effective date, supersession, rationale and source.
Contradiction: saves conflicting claims, sources/dates, owner and unresolved reason; unresolved conflicts do not auto-resolve.
Open Question: saves unanswered issues and missing evidence.
[推论] Latest source is not automatically applicable; check scope/date/supersession.
[推论] Unresolved conflicts fail closed.
[推论] Model may propose patches; durable writes require validation and authorization; Azure/storage choices are examples only.
```

## Existing local text

### Knowledge architecture

- `entities/`: entity pages such as products, organizations, models and projects.
- `raw`: source layer; `concepts/entities/comparisons/queries`: compiled layer.
- Default retrieval loop: check Wiki; if insufficient, read raw/external; compile durable results back into Wiki.

### Retrieval priority page

- Default order: Wiki → memory → skills → sessions → raw → external.
- Raw is consulted when Wiki lacks content.
- Query types distinguish concept, execution, historical and current-fact questions.
- It does not state a choice among evidence/raw, compiled knowledge or both based on exact wording/citation, synthesis, temporal scope, contradiction or risk.

### Schema

- Optional page metadata: `aliases` for obvious synonyms.
- Optional Relations: `refines`, `depends_on`, `conflicts_with`, `supersedes`.
- Relations are semantic links; sources remain evidence.

### Parent bounded search

A search across `wiki/concepts/*.md` found no direct treatment of terminology drift, entity alignment, exact wording/citation routing, or evidence-vs-knowledge-vs-both routing.

## Required adjudication

For each point choose one:

- `ALREADY_COVERED`: cite exact local text that states the same durable rule, not merely a primitive from which it could be inferred.
- `RAW_ONLY_CORRECTLY`: explain why it is not durable architecture knowledge.
- `MISSING_DURABLE_DELTA`: give the smallest addition and one existing owner page.

Review:

1. Terminology drift / canonical entity alignment.
2. Evidence vs compiled knowledge vs both routing.
3. Typed multi-hop traversal.

Do not propose a new page, schema migration, entity service, graph database, skill, runtime gate or automation. At most recommend one compact patch to `hermes-knowledge-architecture.md`.

## Output

### Verdict
`PASS`, `PASS_WITH_NOTES`, or `REQUEST_CHANGES`

### Adjudication
- Terminology/entity alignment
- Evidence/knowledge/both routing
- Typed multi-hop relationships

### Confirmed patch
Exact bounded wording and insertion point, or `None`.

### Duplication risk

### Recommended next step
Exactly one action.
