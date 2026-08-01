---
title: Agent Experience Consolidation Loops
created: 2026-05-11
updated: 2026-08-01
type: concept
tags: [agent, memory, skills, wiki, validation, workflow, hermes, multi-agent]
sources: [raw/articles/venturebeat-anthropic-dreaming-ai-agents-2026-05-07.md, raw/articles/microsoft-research-evolib-evolving-knowledge-2026-07-30.md]
status: draft
description: 定义把 Agent 历史经验提炼为可复用知识、持续整合重验证，并路由到 memory、skills、wiki 或评估资产的闭环。
---

# Agent Experience Consolidation Loops

## Summary
Agent experience consolidation loop 是一种让 agent 从历史任务、失败、成功路径和用户纠正中提取可复用经验，并将其路由到 memory、skills、wiki、project closeout、evaluator 或 runtime automation 的闭环。它的目标不是把更多历史塞进上下文，而是把经验转成可审计、可复用、可验证的未来任务支撑。

一句话原则：**不要把所有历史经验直接写进 memory；先复盘，再按层路由。**

## Source anchor
本页由 VentureBeat 对 Anthropic Claude Managed Agents `dreaming`、`outcomes` 与 multi-agent orchestration 的报道触发：[[venturebeat-anthropic-dreaming-ai-agents-2026-05-07]]。

文章中的 `dreaming` 不是模型权重训练，而是让 agent 回顾过去 session 和 memory，写出 plain-text notes / playbooks 供未来 session 使用。

Microsoft Research 的 [[microsoft-research-evolib-evolving-knowledge-2026-07-30]] 进一步区分了“经验归档”和“知识演化”：EvoLib 从成功尝试中提炼可复用技能、从失败中提炼反思见解，再通过 consolidation 与 dynamic weighting 持续更新知识库。

[推论] 该机制补充的是知识单元进入持久层后的演化方式，不改变本页原有的 Hermes 层间路由和审批边界。

## Core pattern

### 1. Collect historical task evidence
经验固化从证据开始，而不是从抽象反思开始。

可用证据包括：
- completed sessions and transcripts
- tool outputs and test results
- user corrections
- repeated failures
- successful work paths
- project closeouts
- evaluator / reviewer notes
- runtime incidents and recovery evidence

Hermes 对应入口：`session_search`、project closeout、wiki query pages、logs、git diffs、test artifacts。

### 2. Detect recurring failures and successful workflows
复盘的重点不是“发生了什么”，而是识别可以改变未来行为的模式。

高价值信号：
- 同类错误反复发生
- 某个验证步骤显著降低返工
- 用户多次纠正同一边界
- 某个 workflow 在多个项目中复用
- 某个工具/模型/子 agent 组合稳定有效
- 某个经验如果不沉淀，未来很容易再次踩坑

低价值信号：
- 一次性的任务进展
- 临时文件路径
- 单个 PR / issue / commit 的完成状态
- 没有复用场景的新闻事实
- 没有验证过的产品宣传

### 3. Convert lessons into reusable artifacts
经验必须转成未来 agent 能调用的形式。

常见 artifact：
- **memory**：短小、稳定、每个 session 都值得看到的事实
- **skill**：可重复执行的方法、命令、坑点和验证步骤
- **wiki concept**：跨工具、跨项目的长期知识模式
- **wiki query / closeout**：一次验证或判断的证据结论
- **project context**：某个 repo / workspace 的局部规则
- **evaluator rubric**：判断结果是否合格的标准
- **cron candidate report**：周期性提醒或只读复盘报告
- **runtime automation**：已验证、可回滚、低噪音的稳定流程

### 3a. Evolve knowledge instead of only appending experience

EvoLib 给出了一个比“保存更多历史”更严格的知识演化模型：

```text
experience → extract skill/insight → retrieve similar knowledge
→ consolidate/keep separate/supersede/reject → reweight → reuse/revalidate
```

- **Consolidation（来源机制）**：新经验产生候选知识后，检索相似条目并尝试整合成更通用的知识。[推论] 只有适用边界确实可泛化时才应合并，不能把语义相似直接当作可替代。
- **Weighting（来源机制）**：知识价值同时考虑当前任务效用和对后续知识生成的贡献。[推论] 访问次数和最近使用时间只能作为弱信号。
- **Lifecycle metadata**：`source`、适用范围、验证时间、supersession、当前状态和冲突关系是 Hermes 的本地映射，不是博客公开的 EvoLib schema，均应视为 `[推论]`。

### 4. Route by layer responsibility
经验固化的核心治理问题是路由，而不是保存。`[[agent-closed-loop-learning-from-corrections-to-rules]]` 进一步补充了纠错晋升门槛：不要把一次用户纠正直接写成全局规则，先记忆、再泛化、再验证、最后推广。

```text
lesson candidate
→ Is it always-needed stable context? → memory
→ Is it repeatable procedure? → skill
→ Is it durable concept/evidence? → wiki
→ Is it project-local? → project docs / AGENTS.md
→ Is it a quality gate? → evaluator / test / rubric
→ Is it scheduled and stable? → cron/runtime after approval
→ Otherwise → leave in session history
```

参考：[[hermes-memory-skills-wiki-boundaries]], [[hermes-context-layer-operating-rules]], [[hermes-layer-routing-decision-checklist]]。

### 5. Reuse in future tasks
固化后的经验必须能被未来任务触发。

触发方式包括：
- system prompt memory injection
- skill discovery and `skill_view`
- wiki retrieval before answering
- project context auto-load
- cron skill injection
- subagent context handoff
- evaluator rubric reuse

如果经验沉淀后无法被未来任务检索或调用，它只是归档，不是经验闭环。

### 6. Revalidate and prune stale lessons
学习系统不能只积累不遗忘。

应定期检查：
- skill 是否仍然可用
- negative claims 是否过期
- memory 是否重复或陈旧
- wiki concept 是否已有更好的验证结论
- cron 是否仍低噪音、低风险
- runtime automation 是否有 rollback path

Hermes 的 curator 已经覆盖部分 skill lifecycle；memory consolidation / Auto Dream 类型能力仍需谨慎验证。

### Evaluation boundary for evolving knowledge

[推论] 评估经验固化不能只看“是否检索到旧记录”。还要检查后续任务是否改善、Token 和测试时计算是否换来相称收益、随机混合任务顺序下是否稳定、是否产生错误泛化或陈旧规则，以及提炼、合并、评分和重验证本身的成本。

EvoLib 博客报告了数学、代码效率约束和长程环境交互三类实验，以及 Token 效率和任务顺序鲁棒性，但没有在博客中给出完整数值、超参数、并发成本或生产运行证据。它提供研究方向和评估维度，不能直接证明 Hermes 应采用该框架。

## Hermes mapping

Hermes 已具备 `session_search`、skills、memory、验证工具、`/goal`、`delegate_task` 和 cron 等底层能力，但没有在本地证实存在完整原生 Auto Dream。详细能力状态由 [[hermes-agent-experience-consolidation-capability-assessment]] 维护，本页只保留知识闭环边界：

```text
session_search / project evidence → audited review
→ wiki concept/query or project closeout
→ narrow skill patch only when a reusable procedure changed
→ memory only for compact stable facts
→ runtime/cron only after separate approval
```

- `/goal`、fresh-context reviewer 和确定性工具证据可以提供结果验证，详见 [[agent-self-validation-loops]]。
- 多 Agent 只用于适合拆分的复杂工作，不替代明确验收标准；编排边界见 [[subagent-orchestration-patterns]]。
- 定时复盘默认只生成候选报告，不自动修改 memory、skills 或 runtime。

## Anti-patterns
- 把每篇文章都变成一个 skill。
- 把未经验证的外部产品概念写进 memory。
- 把所有 session 复盘结果直接塞进 `MEMORY.md`。
- 用“Dreaming”包装不可审计的自动自改。
- 让 cron 无人确认地修改 durable knowledge layers。
- 把一次任务的进展日志当作长期经验。
- 用多 agent 取代明确验收标准。
- [推论] 把语义相似但适用边界不同的知识强行合并。
- [推论] 让同一个模型同时负责提炼、加权和验收，再把其自评分数当作有效性证明。

## Operating rules
1. 经验候选必须先问：未来会在哪类任务中复用？
2. 能写成验证步骤的，优先进入 skill 或 project gate，而不是 memory。
3. 能作为跨项目概念复用的，进入 wiki concept。
4. 一次能力判断或验证结果进入 query / closeout。
5. 只有稳定、短小、经常需要的事实进入 memory。
6. 自动化只读复盘可以先做；自动写入 durable layer 要等真实验证和单独批准。
7. 所有经验固化都要保留 provenance 和 rollback path。

## Related pages
- [[microsoft-research-evolib-evolving-knowledge-2026-07-30]]
- [[agent-self-validation-loops]]
- [[agent-closed-loop-learning-from-corrections-to-rules]]
- [[subagent-orchestration-patterns]]
- [[agent-orchestration-production-tradeoffs]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[agentic-content-pipeline-design-patterns]]
- [[progressive-knowledge-system-growth]]
