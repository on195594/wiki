---
title: Agent Experience Consolidation Loops
created: 2026-05-11
updated: 2026-05-18
type: concept
tags: [agent, memory, skills, wiki, validation, workflow, hermes, multi-agent]
sources: [raw/articles/venturebeat-anthropic-dreaming-ai-agents-2026-05-07.md]
status: draft
description: 定义把 Agent 历史经验和用户纠正路由到 memory、skills、wiki 或评估资产的闭环。
---

# Agent Experience Consolidation Loops

## Summary
Agent experience consolidation loop 是一种让 agent 从历史任务、失败、成功路径和用户纠正中提取可复用经验，并将其路由到 memory、skills、wiki、project closeout、evaluator 或 runtime automation 的闭环。它的目标不是把更多历史塞进上下文，而是把经验转成可审计、可复用、可验证的未来任务支撑。

一句话原则：**不要把所有历史经验直接写进 memory；先复盘，再按层路由。**

## Source anchor
本页由 VentureBeat 对 Anthropic Claude Managed Agents `dreaming`、`outcomes` 与 multi-agent orchestration 的报道触发：[[venturebeat-anthropic-dreaming-ai-agents-2026-05-07]]。

文章中的 `dreaming` 不是模型权重训练，而是让 agent 回顾过去 session 和 memory，写出 plain-text notes / playbooks 供未来 session 使用。

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

## Hermes mapping

### Dreaming-like review
Hermes 当前可组合实现：

```text
session_search / project evidence
→ post-session knowledge review
→ wiki closeout or concept update
→ narrow skill patch if a reusable procedure changed
→ no memory write unless the fact is stable and always-needed
```

这是一种人工可审计版 Dreaming。

### Outcomes-like grading
Hermes 当前可组合实现：
- `/goal` 设置目标并由 judge model 检查是否完成
- `delegate_task` 派 fresh-context reviewer / verifier
- tests, lint, type checks, browser verification, artifact contracts 提供真实反馈
- skill 中写入 `Verification` section

这对应 [[agent-self-validation-loops]] 中的目标-反馈-迭代结构。

### Multi-agent orchestration
Hermes 原生支持：
- `delegate_task` 单 subagent 或 batch 并行
- fresh child context and separate terminal session
- bounded nested orchestration via `role="orchestrator"` and `delegation.max_spawn_depth`
- durable long-running work改用 `cronjob` 或 background terminal

参考：[[subagent-orchestration-patterns]], [[agent-orchestration-production-tradeoffs]]。

### Scheduled consolidation
Hermes 原生支持 cron，但自动经验固化不应直接写 durable layer。

推荐安全路线：
```text
scheduled read-only review
→ candidate lessons report
→ Telegram / wiki draft
→ human approval
→ wiki/skill/memory patch
→ verification
→ commit
```

不推荐初期让 cron 直接修改 memory、skills 或 runtime 配置。

## Anti-patterns
- 把每篇文章都变成一个 skill。
- 把未经验证的外部产品概念写进 memory。
- 把所有 session 复盘结果直接塞进 `MEMORY.md`。
- 用“Dreaming”包装不可审计的自动自改。
- 让 cron 无人确认地修改 durable knowledge layers。
- 把一次任务的进展日志当作长期经验。
- 用多 agent 取代明确验收标准。

## Operating rules
1. 经验候选必须先问：未来会在哪类任务中复用？
2. 能写成验证步骤的，优先进入 skill 或 project gate，而不是 memory。
3. 能作为跨项目概念复用的，进入 wiki concept。
4. 一次能力判断或验证结果进入 query / closeout。
5. 只有稳定、短小、经常需要的事实进入 memory。
6. 自动化只读复盘可以先做；自动写入 durable layer 要等真实验证和单独批准。
7. 所有经验固化都要保留 provenance 和 rollback path。

## Local validation status
当前 Hermes 已有构建该闭环的 primitives，但没有在本地 v0.13.0 证实存在完整原生 Auto Dream 或 `/dreaming` 产品入口。详见 [[hermes-agent-experience-consolidation-capability-assessment]]。

因此，本地实践应采用：

```text
project evidence / session_search
→ audited closeout
→ wiki concept/query update
→ class-level skill patch only when workflow changed
→ memory only for compact stable facts
→ runtime/cron promotion only after separate approval
```

## Related pages
- [[agent-self-validation-loops]]
- [[agent-closed-loop-learning-from-corrections-to-rules]]
- [[subagent-orchestration-patterns]]
- [[agent-orchestration-production-tradeoffs]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[agentic-content-pipeline-design-patterns]]
- [[progressive-knowledge-system-growth]]
