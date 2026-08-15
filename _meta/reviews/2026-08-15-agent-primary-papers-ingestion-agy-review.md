# Adversarial Review: Five Primary Agent Papers Wiki Ingestion

- Candidate root: `/tmp/agentic-five-papers-wiki-ingestion/candidate`
- Target vault: `/home/lin/wiki`
- Reviewed files:
  - [`proposal.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/proposal.md)
  - [`raw/papers/arxiv-2210-03629-react.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2210-03629-react.md)
  - [`raw/papers/arxiv-2302-04761-toolformer.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2302-04761-toolformer.md)
  - [`raw/papers/arxiv-2304-03442-generative-agents.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2304-03442-generative-agents.md)
  - [`raw/papers/arxiv-2305-16291-voyager.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2305-16291-voyager.md)
  - [`raw/papers/arxiv-2308-08155-autogen.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2308-08155-autogen.md)
  - [`queries/agent-architecture-primary-paper-map.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/queries/agent-architecture-primary-paper-map.md)
  - [`concepts/agent-memory-reflection-planning-pipeline.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/concepts/agent-memory-reflection-planning-pipeline.md)
- Inspected live pages:
  - [`SCHEMA.md`](file:///home/lin/wiki/SCHEMA.md)
  - [`index.md`](file:///home/lin/wiki/index.md)
  - [`log.md`](file:///home/lin/wiki/log.md)
  - [`concepts/agentic-programming-system-engineering.md`](file:///home/lin/wiki/concepts/agentic-programming-system-engineering.md)
  - [`concepts/ai-agent-tool-selection-architecture.md`](file:///home/lin/wiki/concepts/ai-agent-tool-selection-architecture.md)
  - [`concepts/agent-self-validation-loops.md`](file:///home/lin/wiki/concepts/agent-self-validation-loops.md)
  - [`concepts/stateful-agent-environments-and-grounded-verification.md`](file:///home/lin/wiki/concepts/stateful-agent-environments-and-grounded-verification.md)
  - [`concepts/agent-orchestration-production-tradeoffs.md`](file:///home/lin/wiki/concepts/agent-orchestration-production-tradeoffs.md)
  - [`concepts/agent-context-engineering.md`](file:///home/lin/wiki/concepts/agent-context-engineering.md)
  - [`concepts/agent-experience-consolidation-loops.md`](file:///home/lin/wiki/concepts/agent-experience-consolidation-loops.md)
  - [`concepts/hermes-memory-skills-wiki-boundaries.md`](file:///home/lin/wiki/concepts/hermes-memory-skills-wiki-boundaries.md)

---

## Verdict

**`PASS_WITH_MINOR_FIXES`**

The candidate ingestion package is well-engineered, strictly respects active-layer boundaries, accurately represents primary source mechanisms and quantitative findings without overstatement, and properly separates raw source evidence from Hermes-local architectural inferences. The structure conforms to [`SCHEMA.md`](file:///home/lin/wiki/SCHEMA.md) and passes static health-check requirements.

---

## Blocking

*None.* There are no schema violations, broken links, ungrounded claims, or active-layer regressions.

---

## Important

*None.*

---

## Minor

### 1. Provenance section heading mismatch in `agentic-programming-system-engineering.md` patch
- **File / Location**: [`proposal.md:L22-28`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/proposal.md#L22-L28) patching [`concepts/agentic-programming-system-engineering.md:L41-91`](file:///home/lin/wiki/concepts/agentic-programming-system-engineering.md#L41-L91)
- **Defect Type**: Design / Editorial provenance structure.
- **Finding**: In [`concepts/agentic-programming-system-engineering.md`](file:///home/lin/wiki/concepts/agentic-programming-system-engineering.md), section line 41 is explicitly titled `## Durable units from the article` referencing the MachineLearningMastery article. Inserting `### 5. Reasoning–action–observation is a selectable control pattern` as child item #5 under that heading conflates the ReAct primary paper source with the MachineLearningMastery article units.
- **Recommendation**: Either elevate the patch to an independent H2 section (e.g. `## Control pattern: reasoning, action, and observation`) or generalize the parent H2 heading to `## Core system engineering patterns` so the source provenance remains distinct.

### 2. Language consistency in `agent-self-validation-loops.md` patch
- **File / Location**: [`proposal.md:L58-62`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/proposal.md#L58-L62) patching [`concepts/agent-self-validation-loops.md:L91`](file:///home/lin/wiki/concepts/agent-self-validation-loops.md#L91)
- **Defect Type**: Style / Vault consistency.
- **Finding**: The host page [`concepts/agent-self-validation-loops.md`](file:///home/lin/wiki/concepts/agent-self-validation-loops.md) is written predominantly in Chinese prose with English technical terms. The proposed patch text is written entirely in English.
- **Recommendation**: Provide a Chinese translation of the patch text (or a bilingual formulation) to maintain stylistic coherence across the page.

### 3. Verification of deterministic formal page count update in `index.md`
- **File / Location**: [`proposal.md:L87`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/proposal.md#L87) referencing [`index.md:L5`](file:///home/lin/wiki/index.md#L5)
- **Defect Type**: Operational verification.
- **Finding**: [`index.md`](file:///home/lin/wiki/index.md) currently records `Total pages: 110`. The landing adds 2 formal pages (`concepts/agent-memory-reflection-planning-pipeline.md` and `queries/agent-architecture-primary-paper-map.md`). The 5 `raw/papers/` files are exempt from formal page count under `is_formal_page`.
- **Recommendation**: Explicitly ensure `index.md` is updated to `Total pages: 112` upon landing.

---

## Passes

1. **Primary-source fidelity and metric precision**:
   - [`raw/papers/arxiv-2210-03629-react.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2210-03629-react.md): Accurately captures HotpotQA EM (27.4 vs CoT 29.4) and FEVER accuracy (60.9 vs CoT 56.3) from Table 1, explicitly documenting that ReAct is not universally superior to CoT on knowledge QA due to search/retrieval failures.
   - [`raw/papers/arxiv-2302-04761-toolformer.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2302-04761-toolformer.md): Accurately captures API sampling, execution, and loss-reduction filtering, downstream performance, Table 8 language perplexity preservation, and explicit limitations (no tool chaining, no interactive browsing, no cost modeling).
   - [`raw/papers/arxiv-2304-03442-generative-agents.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2304-03442-generative-agents.md): Accurately captures the memory stream, equal weighting heuristic (`recency + importance + relevance`), reflection synthesis threshold, Smallville 25-agent simulation, token credit cost, and human believability evaluation vs factual accuracy limits.
   - [`raw/papers/arxiv-2305-16291-voyager.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2305-16291-voyager.md): Accurately captures automatic curriculum, JavaScript skill library, Mineflayer execution error feedback loop, GPT-4 self-verification critic, and failure modes (impossible curriculum tasks, nonexistent APIs, critic false negatives, ~15x cost).
   - [`raw/papers/arxiv-2308-08155-autogen.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/raw/papers/arxiv-2308-08155-autogen.md): Accurately captures conversable agents, conversation programming, ALFWorld (+15% grounding agent gain), safe/unsafe coding role separation (+8% GPT-4 / +35% GPT-3.5-turbo), and early-stage experimental limitations.
2. **Fact vs local inference separation**:
   - All 5 `raw/papers/` files adhere strictly to neutral extraction, confining Hermes layer mappings and operational interpretations to `Evidence boundary` sections and downstream formal pages.
3. **No harmful duplication across concepts**:
   - [`concepts/agent-memory-reflection-planning-pipeline.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/concepts/agent-memory-reflection-planning-pipeline.md) addresses the runtime state processing pipeline (memory stream $\rightarrow$ retrieval $\rightarrow$ reflection $\rightarrow$ hierarchical planning). It does not duplicate [`concepts/agent-experience-consolidation-loops.md`](file:///home/lin/wiki/concepts/agent-experience-consolidation-loops.md) (which governs cross-session offline learning and post-hoc evolution), [`concepts/hermes-memory-skills-wiki-boundaries.md`](file:///home/lin/wiki/concepts/hermes-memory-skills-wiki-boundaries.md) (normative tier definitions), or [`concepts/agent-context-engineering.md`](file:///home/lin/wiki/concepts/agent-context-engineering.md) (JIT context assembly).
4. **Owner-level gap validity for proposed patches**:
   - Each of the 4 patches targets an explicit owner-level boundary: ReAct control pattern in [`agentic-programming-system-engineering.md`](file:///home/lin/wiki/concepts/agentic-programming-system-engineering.md); training-time vs runtime routing in [`ai-agent-tool-selection-architecture.md`](file:///home/lin/wiki/concepts/ai-agent-tool-selection-architecture.md); environment-grounded execution loops in [`agent-self-validation-loops.md`](file:///home/lin/wiki/concepts/agent-self-validation-loops.md); and conversation programming abstractions in [`agent-orchestration-production-tradeoffs.md`](file:///home/lin/wiki/concepts/agent-orchestration-production-tradeoffs.md).
5. **Quality of problem-oriented query map**:
   - [`queries/agent-architecture-primary-paper-map.md`](file:///tmp/agentic-five-papers-wiki-ingestion/candidate/queries/agent-architecture-primary-paper-map.md) explicitly avoids pretending the 5 papers form an exhaustive taxonomy, instead structuring them across concrete design problems, layer boundaries, and failure paths.
6. **Active-layer boundaries preserved**:
   - No memory mutation, no automatic skill creation, no runtime/config modifications, and explicit warnings against ReAct-by-default and multi-agent-by-default.
7. **Schema & static health-check compliance**:
   - All frontmatter fields match [`SCHEMA.md`](file:///home/lin/wiki/SCHEMA.md). All tags (`agent`, `research`, `architecture`, `decision`, `memory`) are registered in the Tag Taxonomy. All wikilinks resolve bidirectionally. Raw sources are properly referenced.

---

## Recommended patches

### Smallest Acceptable Landing Shape

Land all 8 candidate files as proposed (5 raw papers, 1 query map, 1 concept page, and the 4 concept patches), applying the two minor adjustments below:

```diff
--- a/concepts/agentic-programming-system-engineering.md
+++ b/concepts/agentic-programming-system-engineering.md
@@ -7,7 +7,7 @@
-sources: [raw/articles/machinelearningmastery-agentic-programming-roadmap-2026-05-20.md, raw/articles/towardsdatascience-most-ai-agents-built-backwards-2026-05-27.md, concepts/agent-context-engineering.md, concepts/typed-ai-agent-boundaries.md, concepts/agent-development-lifecycle.md]
+sources: [raw/articles/machinelearningmastery-agentic-programming-roadmap-2026-05-20.md, raw/articles/towardsdatascience-most-ai-agents-built-backwards-2026-05-27.md, raw/papers/arxiv-2210-03629-react.md, concepts/agent-context-engineering.md, concepts/typed-ai-agent-boundaries.md, concepts/agent-development-lifecycle.md]
-updated: 2026-05-29
+updated: 2026-08-15
@@ -91,6 +91,12 @@

+## Control pattern: reasoning, action, and observation
+
+ReAct provides primary evidence for interleaving language reasoning with task-specific actions and environment observations. Its benchmark results are mixed rather than universal: external interaction can reduce unsupported internal reasoning, but search failures, wrong subgoals and repeated steps create new error paths. Hermes should therefore treat ReAct as an optional trajectory shape for tasks that need iterative environment evidence, not as a default for deterministic, low-risk or already well-specified work. See [[agent-architecture-primary-paper-map]].
+
 ## Hermes layer routing
@@ -125,3 +131,4 @@
 - [[subagent-orchestration-patterns]]
+- [[agent-architecture-primary-paper-map]]
```

```diff
--- a/concepts/agent-self-validation-loops.md
+++ b/concepts/agent-self-validation-loops.md
@@ -7,3 +7,3 @@
-sources: [raw/articles/towardsdatascience-claude-code-self-validation-2026-05-05.md]
+sources: [raw/articles/towardsdatascience-claude-code-self-validation-2026-05-05.md, raw/papers/arxiv-2305-16291-voyager.md]
-updated: 2026-05-22
+updated: 2026-08-15
@@ -90,6 +90,12 @@

+## Environment-grounded skill admission
+
+Voyager 展示了比纯文本自我批评（prose self-critique）更强的闭环：生成可执行代码、在真实环境中运行、反馈中间状态与执行报错、校验任务完成度，仅在验证通过后才将程序沉淀至可检索的技能库。同时其自身的失败案例也表明验证器不可被盲目视为权威：课程可能生成不可能完成的任务，程序可能调用不存在的 API，自我验证 critic 亦会漏判真实成功。可迁移原则是“先有环境证据再做技能准入”；Hermes active skill 的自主修改仍被严格排除在本模式之外。参见 [[agent-architecture-primary-paper-map]] 与 [[stateful-agent-environments-and-grounded-verification]]。
+
 ## Hermes mapping
```

```diff
--- a/index.md
+++ b/index.md
@@ -5,3 +5,3 @@
-> Last updated: 2026-08-14 | Total pages: 110
+> Last updated: 2026-08-15 | Total pages: 112
@@ -20,2 +20,3 @@
 - [[agent-context-engineering]] — Agent 上下文工程：用即时装配、最小必要上下文、工具反向边界和状态裁剪，防止 context rot 与多步执行偏航
+- [[agent-memory-reflection-planning-pipeline]] — Agent 记忆–反思–规划流水线：将经历处理为事件流、多因素检索、反思推断与分层计划，区分应用事件存储与 Hermes 默认 memory
@@ -100,2 +101,3 @@
 - [[software-engineering-laws-decision-map]] — 56 条软件工程法则的全量问题导向入口：按真实工程场景检索适用法则、误用边界、跨类别张力和来源记录
+- [[agent-architecture-primary-paper-map]] — Agent 架构一手论文地图：按设计问题检索 ReAct、Toolformer、Generative Agents、Voyager 与 AutoGen 的机制、证据和外推边界
```
