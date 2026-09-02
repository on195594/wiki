### 1. Verdict

`PASS_WITH_MINOR_FIXES`

---

### 2. Blocking

`none`

---

### 3. Important

`none`

---

### 4. Minor

1. **Over-broad `## Compiled concept pages` heading in raw note**:
   - **File**: [`raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md:54-58`](file:///home/lin/wiki/raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md#L54-L58)
   - **Evidence**: Lines 54–58 list `[[ai-agent-tool-selection-architecture]]`, `[[agent-context-engineering]]`, and `[[typed-ai-agent-boundaries]]` under the heading `## Compiled concept pages`. However, commit `c3e1390` only compiled this raw source into [`concepts/ai-agent-tool-selection-architecture.md`](file:///home/lin/wiki/concepts/ai-agent-tool-selection-architecture.md#L7) (as accurately recorded in [`log.md:1723`](file:///home/lin/wiki/log.md#L1723): `Updated canonical owner: concepts/ai-agent-tool-selection-architecture.md`). Neither [`concepts/agent-context-engineering.md`](file:///home/lin/wiki/concepts/agent-context-engineering.md) nor [`concepts/typed-ai-agent-boundaries.md`](file:///home/lin/wiki/concepts/typed-ai-agent-boundaries.md) cite this raw source in their frontmatter `sources:` or contain ARD content.
   - **Impact**: Minor metadata ambiguity for downstream retrieval; readers inspecting the raw note may expect all three pages to have incorporated ARD deltas.
   - **Remediation**: Annotate the list to distinguish the compiled canonical owner from adjacent boundary concepts (e.g., `Canonical owner: [[ai-agent-tool-selection-architecture]]`, `Adjacent context boundary: [[agent-context-engineering]]`, `Adjacent tool boundary: [[typed-ai-agent-boundaries]]`). *Note*: Because this file resides in `raw/`, modifying it requires updating its SHA-256 in [`_meta/raw-source-hashes.json`](file:///home/lin/wiki/_meta/raw-source-hashes.json#L118) via `_meta/scripts/wiki_raw_hashes.py`.

2. **Description alignment in concept frontmatter**:
   - **File**: [`concepts/ai-agent-tool-selection-architecture.md:9`](file:///home/lin/wiki/concepts/ai-agent-tool-selection-architecture.md#L9)
   - **Evidence**: While [`index.md:17`](file:///home/lin/wiki/index.md#L17) was updated to include resource discovery (`AI Agent 工具选择架构：分离资源发现、工具可用性、候选集缩减、具体选择和失败回退，并以本地评测决定是否需要动态路由`), the frontmatter `description` in `concepts/ai-agent-tool-selection-architecture.md:9` remains `区分工具可用性、候选集缩减、逐步选择与失败回退，并用本地评测决定是否需要动态工具路由。`.
   - **Impact**: Minor routing metadata divergence between the master index summary and the page's machine-readable preview.
   - **Remediation**: Synchronize the page frontmatter `description` with the updated 5-stage chain.

---

### 5. Passes

1. **Source fidelity**:
   - Accurately captures the substantive content of The New Stack article (Amanda Caswell, 2026-08-31) and the local Karakeep extraction artifact ([`...-summary.md`](file:///home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260902-091039-MCP-was-supposed-to-solve-the-agent-tooling-problem.-It-missed-a-step.-https-the-2046515-593366480-summary.md)).
   - Faithfully records technical details: v0.91 specification draft (Aug 26), JSON-LD and REST interface, mandatory `POST /search` endpoint, optional resource browsing endpoints, federated catalogs retaining local access policies, "agentic resources" terminology, Apache 2.0 licensing, and co-authors Junjie Bu (Google), R.V. Guha (Microsoft), and Shaun Smith (Hugging Face).
   - Accurately records industry vendor participation (Cisco, Databricks, GitHub, GoDaddy, Nvidia, Salesforce, ServiceNow, Snowflake, AWS) and unsettled governance status.

2. **Provenance and limitation disclosure**:
   - The raw note frontmatter explicitly documents capture metadata (`source_type: article`, `captured_at: 2026-09-02`, Karakeep extraction route) and discloses in `extraction_limitations` that the note is a source-backed synthesis rather than an uncleaned HTML snapshot.
   - The dedicated `## Limits` section in [`raw/...-2026-08-31.md:48-52`](file:///home/lin/wiki/raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md#L48-L52) clearly marks the material as secondary news reporting on an early proposal, not a specification or benchmark.
   - Explicitly deconstructs the "DNS for agents" metaphor: unlike DNS 1:1 name-to-address resolution, ARD returns a semantic multi-candidate set requiring caller adjudication and trust policies.

3. **Smallest durable unit & canonical-owner placement**:
   - Correctly avoided creating redundant or speculative standalone concept pages (such as `concepts/agentic-resource-discovery.md` or `entities/ard.md`) for an early external draft.
   - Placed the durable architectural delta into the authoritative owner [`concepts/ai-agent-tool-selection-architecture.md`](file:///home/lin/wiki/concepts/ai-agent-tool-selection-architecture.md#L21-L27) in a compact 3-paragraph section (`## Discovery precedes availability`).

4. **Duplication and conceptual drift avoidance**:
   - Cleanly separated capability discovery from downstream execution decisions: `Discovery` (identifying candidate capabilities in federated catalogs) precedes `Availability/Admission` (what the local runtime permits and trusts), followed by `Candidate reduction`, `Selection & execution`, and `Fallback`.
   - Maintained clean boundaries with adjacent concepts: did not duplicate discovery into [`concepts/agent-context-engineering.md`](file:///home/lin/wiki/concepts/agent-context-engineering.md) (prompt assembly and per-step visibility) or [`concepts/typed-ai-agent-boundaries.md`](file:///home/lin/wiki/concepts/typed-ai-agent-boundaries.md) (typed schemas, function tools, dependency injection).

5. **Strict avoidance of unsupported Hermes adoption claims**:
   - Explicitly stated in both the raw note and concept page that Hermes currently relies on a bounded local toolset/MCP registration model that already bounds the candidate set.
   - Qualified ARD as an architectural boundary distinction rather than a missing runtime capability.
   - Dynamic discovery adoption explicitly requires local evidence of catalog fragmentation or repeated manual registration friction, alongside separate security, evaluation, approval, and rollback work.
   - Reinforced that discovery does not bypass local credentials, permissions, schema validation, approval, or execution verification.
   - Maintained `Runtime/config/MCP/cron/memory：不推广` in the adoption boundary section.

6. **Wikilink usefulness and health verification**:
   - Bidirectional linkage resolves cleanly: `raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md` references `[[ai-agent-tool-selection-architecture]]`, and `concepts/ai-agent-tool-selection-architecture.md` lists the raw source in frontmatter `sources:`, links to it in body (`[[thenewstack-ard-agent-discovery-specification-2026-08-31]]`), and lists it in `## Related`.
   - `python3 -m unittest _meta/scripts/test_wiki_health_check.py` passed 8/8 tests.
   - Deterministic verification with `python3 _meta/scripts/wiki_health_check.py` passed cleanly (`P0: 0, P1: 0, P2: 0`).
   - `git diff --check c3e1390^!` passed with zero whitespace or formatting errors.

7. **Index and log consistency**:
   - [`index.md:17`](file:///home/lin/wiki/index.md#L17) was updated with the 5-stage distinction.
   - Header metadata in [`index.md:5`](file:///home/lin/wiki/index.md#L5) is current (`Last updated: 2026-09-02 | Indexed pages: 115`).
   - [`log.md:1721-1727`](file:///home/lin/wiki/log.md#L1721-L1727) accurately documents raw source capture, canonical owner update, durable delta, evidence boundary, and the wiki-only scope assertion.
   - The SHA-256 digest (`23e6074874337bf8284c21908b4f9d9ef74187bd1a4a164dff2926003daa0c0a`) in [`_meta/raw-source-hashes.json:118`](file:///home/lin/wiki/_meta/raw-source-hashes.json#L118) matches the file on disk exactly, with zero hash drift across all 156 raw files.

---

### 6. Recommended patches

> *Note: Recommended for review only; as this evaluation is strictly read-only, no changes have been applied.*

#### Patch 1: Align frontmatter `description` in canonical concept

```markdown
--- a/concepts/ai-agent-tool-selection-architecture.md
+++ b/concepts/ai-agent-tool-selection-architecture.md
@@ -9,1 +9,1 @@
-description: 区分工具可用性、候选集缩减、逐步选择与失败回退，并用本地评测决定是否需要动态工具路由。
+description: 区分资源发现、工具可用性、候选集缩减、逐步选择与失败回退，并用本地评测决定是否需要动态工具路由。
```

#### Patch 2 (Optional): Qualify compiled vs. adjacent concepts in raw note

*(Requires running `python3 _meta/scripts/wiki_raw_hashes.py` if applied)*

```markdown
--- a/raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md
+++ b/raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md
@@ -54,4 +54,6 @@
 ## Compiled concept pages
 
 - [[ai-agent-tool-selection-architecture]]
+
+### Adjacent boundary concepts
 - [[agent-context-engineering]]
 - [[typed-ai-agent-boundaries]]
```
