### Verdict
`PASS_WITH_NOTES`

---

### Adjudication

- **Terminology / entity alignment**: `MISSING_DURABLE_DELTA`  
  *Justification*: Existing local text only provides the metadata primitive `aliases` for obvious synonyms in the schema. It does not state the durable architectural rule: terminology drift must resolve to a single canonical entity page holding aliases to prevent fragmented pages that diverge by omission.  
  *Owner page*: `hermes-knowledge-architecture.md`

- **Evidence vs compiled knowledge vs both routing**: `MISSING_DURABLE_DELTA`  
  *Justification*: Existing local text specifies a static sequential fallback order (Wiki → raw) when content is missing, but does not capture the intent-based routing principles: exact wording, citations, and freshness route to the evidence layer; synthesis, rationale, and continuity route to the compiled knowledge layer; redundant dual-layer querying should be avoided; temporal constraints precede similarity ranking; and contradiction checks serve as an output gate.  
  *Owner page*: `hermes-knowledge-architecture.md`

- **Typed multi-hop relationships**: `MISSING_DURABLE_DELTA`  
  *Justification*: Existing local schema lists relation primitives (`refines`, `depends_on`, `conflicts_with`, `supersedes`) as "semantic links", but does not capture the architectural rule explaining why they exist: flat top-k vector similarity ranks candidate text but cannot navigate explanation chains; multi-hop reasoning requires traversing typed relationships.  
  *Owner page*: `hermes-knowledge-architecture.md`

---

### Confirmed patch

**Target File**: `hermes-knowledge-architecture.md`  
**Insertion Point**: Append as a subsection under the layer retrieval / query architecture section.

```markdown
### Retrieval Routing & Structural Principles

- **Layer Routing**: Route exact policy wording, literal citation, and freshness queries to the raw evidence layer. Route rationale ("why"), synthesis, and continuity queries to the compiled knowledge layer. Avoid querying both layers by default to prevent latency and cost overhead.
- **Temporal & Contradiction Gates**: Apply temporal constraints before similarity ranking. Contradiction checks must gate outputs across all retrieval routes.
- **Canonical Entity Alignment**: Resolve terminology drift by maintaining a single canonical entity page with `aliases`, preventing split pages that disagree by omission.
- **Multi-Hop Traversal**: Use typed semantic relations (`refines`, `depends_on`, `conflicts_with`, `supersedes`) to traverse multi-hop explanation chains where top-k similarity ranking fails to connect sequential dependencies.
```

---

### Duplication risk
Low. The patch does not redefine existing schema keys or replace the global retrieval priority chain. It strictly supplies the missing architectural rationales and query-routing logic that govern how the existing primitives (`aliases`, `relations`, `raw` vs compiled wiki) are utilized.

---

### Recommended next step
Apply the confirmed 4-bullet patch directly to `hermes-knowledge-architecture.md`.
