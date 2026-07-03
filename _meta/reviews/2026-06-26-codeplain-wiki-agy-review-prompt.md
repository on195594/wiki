# AGY Wiki Review Prompt

你是 AGY，执行严格只读审查。不要修改任何文件，不要创建文件，不要调用会写入外部状态的命令。只基于下面提供的 diff 和文件内容评估。

任务：审查 Hermes wiki 对 The New Stack / Codeplain spec-driven regenerative code 文章的沉淀是否合适。用户要求按 Hermes 分析建议落地，并交给 AGY 审查。

审查重点：
- 是否符合 wiki-only 落地边界：raw source + codex-agent-workflow-layering + agent-context-engineering + log。
- 是否避免把 Codeplain/Plain/plain-forge 直接推广成 active skill/runtime/MCP/cron/memory。
- 概念是否准确：spec layer / generation layer 分离、provenance debt、行为变更先回写 spec。
- 是否存在过度主张、来源缺失、断链、错误落点、需要最小修正的问题。

请用中文输出：
1. Verdict: PASS / PASS_WITH_NOTES / REQUEST_CHANGES
2. Blocking findings: 无则写无；有则列文件/证据/最小修正
3. Important notes: 非阻塞建议
4. Safety boundary assessment: 是否触碰 memory、active skill、runtime、cron、MCP、gateway、profile/plugin
5. Recommended next step: 只给一个下一步

## Pre-run hashes
ece826b9e264b404a7c1189831d2e364d1561ec2fade7630fa606d8381c4b7d2  concepts/codex-agent-workflow-layering.md
ede0ab63757b89878c37536abe6ea5523daf2c8b85de873221cc2d5352548121  concepts/agent-context-engineering.md
28e70408510a5d20c500efeea3661803d6e2dc493082ae4baaefc485331d37c1  log.md
9fcde519f98d1f79ed84045bab86901f61fe0b7716409ff1cb886fa346989d68  raw/articles/thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26.md

## Git status
 M concepts/agent-context-engineering.md
 M concepts/codex-agent-workflow-layering.md
 M log.md
?? _meta/reviews/2026-06-26-codeplain-wiki-agy-review-prompt.md
?? raw/articles/thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26.md

## Tracked diff
diff --git a/concepts/agent-context-engineering.md b/concepts/agent-context-engineering.md
index 8a5200b..5053837 100644
--- a/concepts/agent-context-engineering.md
+++ b/concepts/agent-context-engineering.md
@@ -1,10 +1,10 @@
 ---
 title: Agent Context Engineering
 created: 2026-05-20
-updated: 2026-06-21
+updated: 2026-06-26
 type: concept
 tags: [agent, llm, context-engineering, hermes, workflow]
-sources: [raw/articles/machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19.md, raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md, raw/articles/microsoft-developer-ai-coding-agents-use-technology-2026-05-27.md, concepts/llm-context-engineering-layer.md, concepts/hermes-context-engineering-design-priorities.md]
+sources: [raw/articles/machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19.md, raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md, raw/articles/microsoft-developer-ai-coding-agents-use-technology-2026-05-27.md, raw/articles/thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26.md, concepts/llm-context-engineering-layer.md, concepts/hermes-context-engineering-design-priorities.md]
 status: stable
 description: 定义 Agent 执行过程中的上下文装配原则，用于控制工具、示例、状态和历史可见性。
 aliases: [agent-context-engineering, context-engineering-for-agents]
@@ -111,6 +111,16 @@ Hermes 的防腐原则：
    - 对复杂任务，应能回答为什么选了某段上下文、为什么丢弃某段上下文。
    - 这与 `[[hermes-context-engineering-design-priorities]]` 的 budget、ranking、compression 顺序一致。

+## Provenance debt in generated code
+
+The New Stack 对 Codeplain 的报道给这页补充了一个上下文工程视角：AI 生成代码被手工连续补丁后，容易产生 **provenance debt（出处债务）**。问题不只是代码变复杂，而是代码与它背后的需求、约束、spec、prompt、推理记录和验收证据之间的来源关系断开；后续 agent 再看到这段代码时，只能从实现反推意图，容易把临时修补当成设计事实。
+
+Hermes 的对应规则：
+- 对 AI 生成或 agent 修改的代码，优先保留“为什么改”的来源：spec、acceptance criteria、ADR、project doc、测试或审查记录。
+- 行为逻辑变更应先回写 spec / contract，再派生代码修改；不要让代码 diff 成为唯一事实源。
+- 当只剩实现代码而没有来源上下文时，后续 agent 应把意图判断标为推论，并用测试、文档或用户确认补齐事实源。
+- 不把外部文章中的全量 regenerate-code 主张直接推广为 Hermes 默认。出处债务用于提醒上下文保真，不等于允许 agent 无边界重写实现。
+
 ## Relationship to existing wiki

 - `[[llm-context-engineering-layer]]`：讲 context engineering 作为 RAG 与 prompt 之间的系统层；本页讲 Agent 多步执行中各类上下文面的即时装配。
@@ -120,6 +130,7 @@ Hermes 的防腐原则：
 - `[[ai-coding-assistant-context-budget-management]]`：讲工具输出、日志、文件和历史如何占用上下文预算；本页补充工具是否能被发现和正确选择的 upstream 级联。
 - `[[agent-development-lifecycle]]`：把 context、tool、prompt、monitor 放进 Build/Test/Deploy/Monitor/Govern 生命周期；本页提供 Build/Test 阶段的上下文装配原则。
 - `[[subagent-orchestration-patterns]]`：讲 subagent 生命周期选择；本页补充子 Agent 应接收最小共享上下文，避免跨任务污染。
+- `[[codex-agent-workflow-layering]]`：讲 prompt、AGENTS、skill、MCP、automation 以及 spec/generation layer 的职责分离；本页补充 provenance debt 如何导致 agent 上下文保真下降。

 ## What not to promote blindly

@@ -147,11 +158,13 @@ Hermes 的防腐原则：
 - [[machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19]]
 - [[machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28]]
 - [[microsoft-developer-ai-coding-agents-use-technology-2026-05-27]]
+- [[thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26]]
 - [[llm-context-engineering-layer]]
 - [[hermes-context-engineering-design-priorities]]
 - [[typed-ai-agent-boundaries]]
 - [[agent-development-lifecycle]]
 - [[subagent-orchestration-patterns]]
+- [[codex-agent-workflow-layering]]
 - [[hermes-context-layer-operating-rules]]
 - [[ai-assumption-challenger-before-execution]]
 - [[wiki-ingestion-workflow]]
diff --git a/concepts/codex-agent-workflow-layering.md b/concepts/codex-agent-workflow-layering.md
index c9e3f82..29be953 100644
--- a/concepts/codex-agent-workflow-layering.md
+++ b/concepts/codex-agent-workflow-layering.md
@@ -1,10 +1,10 @@
 ---
 title: Codex Agent Workflow Layering
 created: 2026-04-17
-updated: 2026-05-17
+updated: 2026-06-26
 type: concept
 tags: [agent, llm, mcp, automation, workflow, configuration, tool]
-sources: [raw/articles/openai-codex-best-practices-2026-04-17.md]
+sources: [raw/articles/openai-codex-best-practices-2026-04-17.md, raw/articles/thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26.md]
 status: stable
 description: 说明 Codex agent 工作流中 prompt、计划、AGENTS、skills、MCP 和自动化的分层职责。
 aliases: [codex-workflow-layering]
@@ -129,9 +129,20 @@ automation 不负责设计方法，只负责按时间和环境调度已经成熟

 这条顺序的本质是先固化规则，再固化方法，再接入外部能力，最后才做调度放大。

+## Spec layer before generation layer
+
+The New Stack 对 Codeplain 的报道补充了一个 AI coding 分层原则：当 AI 让代码生成变得便宜时，真正应该长期维护的可能不是生成出的实现代码，而是表达业务意图、约束和验收边界的 spec。实现代码更接近派生产物；spec、测试、接口契约和审查记录才是跨 agent、跨会话保留上下文的事实源。
+
+Hermes 对这篇文章的采纳边界：
+- 对中等以上 AI 编程任务，先让需求收敛到 `[[spec-driven-development]]` 的 contract，再派生 plan、tests、subagent/coding-agent 任务和 code review。
+- 当逻辑或行为需要变更时，优先修改 spec / acceptance criteria / project doc，再让 agent 生成或修改实现；不要把连续手工补丁当成最终来源。
+- “代码可再生”不是默认行为。数据库迁移、生产配置、凭证、安全策略、不可逆操作和性能敏感边界仍需要显式审查、测试和回滚。
+- Codeplain / Plain / plain-forge 是行业案例，不是 Hermes active skill、runtime、MCP 或 cron 的直接推广授权。
+
 ## Common mistakes
 - 把长期规则继续塞在 prompt 里，而不是迁移到 `AGENTS.md`
 - 在多步复杂任务上跳过 planning
+- 让 AI 在模糊需求上连续补丁实现代码，而没有回写 spec、验收标准或设计意图
 - 还没稳定就急着自动化
 - 一开始把所有外部工具都接入，导致复杂度失控
 - 只让 agent 生成代码，不要求验证和审查
@@ -146,6 +157,7 @@ automation 不负责设计方法，只负责按时间和环境调度已经成熟
 - [[claude-code-practical-workflow-tips]]
 - [[repository-level-code-intelligence-layer]]
 - [[hermes-ai-workflow-formalization-principles]]
+- [[thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26]]
 - [[wiki-ingestion-workflow]]
 - [[index]]
 - [[log]]
diff --git a/log.md b/log.md
index 34b6c82..4dbf33c 100644
--- a/log.md
+++ b/log.md
@@ -3,6 +3,12 @@
 > Chronological record of wiki actions.
 > Format: `## [YYYY-MM-DD] action | subject`

+## [2026-06-26] ingest | Codeplain spec-driven regenerative code
+- Captured raw source: `raw/articles/thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26.md`
+- Updated: `concepts/codex-agent-workflow-layering.md`, `concepts/agent-context-engineering.md`
+- Added the spec layer / generation layer separation as an AI coding workflow principle and captured `provenance debt` as a context-engineering risk for hand-patched AI-generated code.
+- Active-layer boundary: no memory, skill default gate, cron, MCP, runtime, wrapper, or gateway behavior was promoted.
+
 ## [2026-06-21] review-fix | AI assumption challenger AGY review
 - Review prompt: `_meta/reviews/2026-06-21-ai-assumption-challenger-agy-review-prompt.md`
 - Review result: `_meta/reviews/2026-06-21-ai-assumption-challenger-agy-review.md`

## New raw source file
---
title: '"Code should be regenerated, not maintained": Codeplain makes the case for spec-driven development'
author: unknown
source_type: article
source_url: https://thenewstack.io/codeplain-spec-driven-regenerative-code/
published_at: unknown
captured_at: 2026-06-26
status: raw
tags: [ai-coding, spec-driven-development, agent, context-engineering, hermes]
extraction_limitations: HTML article body was extracted from The New Stack page container by the `/gsummary` workflow; this raw page stores the generated summary and source metadata rather than the full original article body.
---

# Codeplain spec-driven regenerative code

## Source
- URL: https://thenewstack.io/codeplain-spec-driven-regenerative-code/
- Title: `"Code should be regenerated, not maintained": Codeplain makes the case for spec-driven development`
- Source: The New Stack
- Captured: 2026-06-26
- Local summary artifact: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260626-155503-Code-3183861-356495120-summary.md`
- Extraction note: HTML article body extracted from `#tns-post-body-content` / `#tns-post-body` with bounded substring fallback; scripts/navigation/forms removed; duplicate blocks removed.

## Compiled concept pages
- [[codex-agent-workflow-layering]]
- [[agent-context-engineering]]

## Core claim
Codeplain argues that in AI-era software development, teams should maintain structured, human-readable specifications as the durable source of truth and regenerate implementation code from those specs, rather than treating generated code as the primary artifact to hand-maintain.

## Key points
- AI makes code generation cheap, but code review and long-term maintenance remain expensive.
- Codeplain's Plain specification language aims to make product intent, constraints, and system behavior the reviewable artifact.
- `plain-forge` lets agents such as Claude Code incrementally draft and update specs through conversation, reducing the burden of writing a complete spec upfront.
- Manual patches to generated code create provenance debt: the code changes, but the reason, constraint, and generation context behind the change may no longer be recoverable.
- The article cites an Incode integration-maintenance case and claims spec generation can use 5–10x fewer tokens than direct code generation.

## Hermes interpretation
- The article supports the existing Hermes principle that medium or risky AI coding work should first converge into a structured spec before planning, test writing, or agent execution.
- The reusable concept is not "adopt Codeplain" or "fully regenerate all code". It is the layer separation: maintain intent/spec/contracts; generate or patch implementation from that controlled source.
- In Hermes, this should first remain wiki knowledge and optional `spec-driven-development` reference material. It should not automatically promote active skill behavior, runtime config, MCP, cron, or memory changes.

## Limits
- The article describes an early company and product direction, not a mature cross-industry standard.
- Full code regeneration is risky for database migrations, production configuration, credentials, security policy, and other irreversible or high-risk surfaces.
- Poor specs can systematize errors; regeneration only helps when specs, tests, interface contracts, and review gates are strong.
