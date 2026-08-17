### Verdict
`PASS`

The ingestion commit `04a38e15bff913c4b5db936b2e8235d97999cb53` successfully captures the reusable, vendor-neutral core of the persistent knowledge layer article into [concepts/hermes-knowledge-architecture.md](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md) while strictly isolating synthetic demo fixtures, Azure cloud artifacts, and empirical cost figures to [raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md](file:///home/lin/wiki/raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md).

---

### Blocking findings
None.

---

### Important findings
None.

---

### Minor findings
None.

---

### Coverage matrix

| Durable Source Idea | Classification | Justification & Location |
|---|---|---|
| **Evidence / Knowledge / Orchestrator separation** | `ALREADY_OWNED_ELSEWHERE` | Already established in [concepts/hermes-knowledge-architecture.md](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L20-L73) (Runtime Stack vs Filesystem Layers) and [concepts/hermes-context-layer-operating-rules.md](file:///home/lin/wiki/concepts/hermes-context-layer-operating-rules.md#L26-L42). Recreating a third parallel layer taxonomy would create redundant conceptual clutter. |
| **Decision primitive** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L81](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L81) with rule/conclusion, scope, effective date, supersession relation, rationale, and source provenance. |
| **Contradiction primitive** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L82](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L82) with side-by-side conflicting claims, respective sources, effective dates, accountable owner, and `why_not_resolved`. |
| **Open Question primitive** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L83](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L83) with explicit tracking of blocked questions, evidence gaps, and required resolution criteria. |
| **Scoped supersession** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L81](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L81) and [hermes-knowledge-architecture.md:L87](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L87) (`[推论]` specifying scope, date, and supersession validation before assuming applicability). |
| **Effective dates / temporal scoping** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L75-L89](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L75-L89), highlighting that recency does not imply applicability and historical/as-of dates govern validity. |
| **Rationale retention ("Why dies first")** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L81](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L81) by requiring decision rationale and its original evidence source to be durably retained. |
| **Terminology drift / Entity alignment** | `ALREADY_OWNED_ELSEWHERE` | Handled structurally by [SCHEMA.md](file:///home/lin/wiki/SCHEMA.md) (`aliases: []` frontmatter convention) and existing `entities/` compiled layer in [hermes-knowledge-architecture.md:L68](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L68). Source-specific alias resolution code correctly stays in raw. |
| **Multi-hop typed relationships** | `ALREADY_OWNED_ELSEWHERE` | Managed via standard Wikilinks, comparisons, and frontmatter relations (`depends_on`, `refines`, `related`) in [concepts/hermes-knowledge-architecture.md](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L171-L182) and [concepts/progressive-knowledge-system-growth.md](file:///home/lin/wiki/concepts/progressive-knowledge-system-growth.md#L42-L46). |
| **Write-risk governance (Patch vs Write)** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L89](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L89) (`[推论]` model proposes patches, persistent writes require deterministic validation and explicit authorization). Complements [concepts/hermes-knowledge-base-operating-flow.md](file:///home/lin/wiki/concepts/hermes-knowledge-base-operating-flow.md#L20-L28). |
| **Query routing & Contradiction gate** | `CAPTURED_IN_CONCEPT` | Captured in [hermes-knowledge-architecture.md:L88](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L88) (fail-closed behavior when encountering unresolved contradictions) and supported by [concepts/hermes-context-layer-operating-rules.md](file:///home/lin/wiki/concepts/hermes-context-layer-operating-rules.md#L177-L186). |
| **When not to build (Workload boundary)** | `ALREADY_OWNED_ELSEWHERE` | Owned by [concepts/progressive-knowledge-system-growth.md](file:///home/lin/wiki/concepts/progressive-knowledge-system-growth.md#L17-L41) (friction before automation, avoiding premature complexity) and [concepts/hermes-context-layer-operating-rules.md](file:///home/lin/wiki/concepts/hermes-context-layer-operating-rules.md#L238-L245). |
| **Azure implementation (Cosmos, AI Search, etc.)** | `RAW_ONLY_CORRECTLY` | Maintained in [raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md](file:///home/lin/wiki/raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md#L353-L585) as reference implementation examples. |
| **Cost / benchmark figures (Break-even tokens)** | `RAW_ONLY_CORRECTLY` | Retained in [raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md](file:///home/lin/wiki/raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md#L765-L815) with caveats noted in raw metadata and capture notes. |

---

### Duplication assessment

- **Real duplication:** None. No redundant concept pages were created, and no blocks of text from adjacent concepts were duplicated.
- **Acceptable overlap:**
  - [concepts/hermes-memory-skills-wiki-boundaries.md#L131-L135](file:///home/lin/wiki/concepts/hermes-memory-skills-wiki-boundaries.md#L131-L135) notes that historical events do not automatically become current facts and conflicting versions cannot coexist unmarked. [concepts/hermes-knowledge-architecture.md#L86-L89](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L86-L89) refines this into concrete compiled knowledge primitives (Decision, Contradiction, Open Question) and fail-closed compilation rules.
  - [concepts/hermes-context-layer-operating-rules.md#L26-L42](file:///home/lin/wiki/concepts/hermes-context-layer-operating-rules.md#L26-L42) governs context window allocation and dynamic retrieval, whereas [concepts/hermes-knowledge-architecture.md](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md) governs durable filesystem storage and knowledge compilation.

---

### Passes

1. **Compact, appropriate landing:** Ingested as a focused 20-line section ([`## Conflict-aware knowledge primitives and temporal scoping`](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L75-L90)) within the existing owner concept rather than creating a superfluous new concept page.
2. **Clear epistemic boundaries:** Explicitly prefixed local adaptations with `[推论]` ([hermes-knowledge-architecture.md:L86-L89](file:///home/lin/wiki/concepts/hermes-knowledge-architecture.md#L86-L89)) and separated source claims from local operational rules.
3. **Rigorous provenance and limitation tracking:** [raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md](file:///home/lin/wiki/raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md#L15-L21) documents capture methodology, synthetic insurance corpus limitations, vendor-specific implementation boundaries, and source hash integrity in `_meta/raw-source-hashes.json`.
4. **Proportionate index and log maintenance:** [index.md](file:///home/lin/wiki/index.md#L60) and [log.md](file:///home/lin/wiki/log.md#L6-L13) were accurately updated with balanced summaries without bloating the index.

---

### Recommended patches
None.

---

### Recommended next step
Retain commit `04a38e15bff913c4b5db936b2e8235d97999cb53` as the canonical Wiki state without further modification.
