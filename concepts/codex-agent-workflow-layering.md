---
title: Codex Agent Workflow Layering
created: 2026-04-17
updated: 2026-05-17
type: concept
tags: [agent, llm, mcp, automation, workflow, configuration, tool]
sources: [raw/articles/openai-codex-best-practices-2026-04-17.md]
status: stable
description: 说明 Codex agent 工作流中 prompt、计划、AGENTS、skills、MCP 和自动化的分层职责。
aliases: [codex-workflow-layering]
---

# Codex Agent Workflow Layering

## Summary
这页提炼 OpenAI 的 Codex best practices：高质量 agent 工作流不是靠一次性 prompt magic，而是靠分层设计。单次任务目标放在 prompt，长期仓库规则放进 `AGENTS.md`，某类任务的方法沉淀成 skill，repo 外的实时上下文通过 MCP 接入，成熟后的稳定流程再交给 automation 调度。这样才能把“会写代码的助手”变成“可持续复用的工程代理”。

## Layer model
### 1. Prompt defines the current task
prompt 的职责是把这一次要做什么说清楚。

推荐最小结构：
- Goal
- Context
- Constraints
- Done when

它解决的是当前任务的边界，而不是长期规则或团队规范。

### 2. Planning reduces ambiguity before execution
复杂、多步、需求还没讲清的任务，不应该直接进入编码。

先 plan 的价值在于：
- 先补上下文
- 先暴露歧义
- 先收敛完成标准
- 降低返工率

如果任务还处在“方向模糊、约束不清、步骤未拆开”的阶段，就应优先走 plan，而不是继续堆 prompt。

### 3. AGENTS.md stores durable repo rules
`AGENTS.md` 负责承载仓库级长期规则，例如：
- 目录结构
- build / test / lint 命令
- 工程约定
- 禁止事项
- done 定义与验证要求

它本质上是 repo 级 agent README，不适合塞入频繁变化的数据、一次性需求或过长的任务说明。

核心原则：
- 短而准，比长而空更有用
- 同类错误重复出现时再补规则
- 规则离当前目录越近，优先级越高

### 4. Config makes behavior consistent
很多“模型表现不好”的问题，其实是配置问题，例如：
- 工作目录不对
- 权限不够
- sandbox 太松或太紧
- 默认模型或 reasoning effort 不合适
- 缺少外部连接器

因此，`config.toml`、approval policy、sandbox mode、profiles、MCP setup 不是附属品，而是一致性层。

### 5. Verification is part of the workflow
Codex 不应该只生成代码，还应被明确要求去：
- 写或更新测试
- 跑相关检查
- 验证行为是否符合预期
- 审查 diff 中的 bug、回归与风险模式

如果没有把验证要求写进 prompt 或 `AGENTS.md`，agent 往往只完成“生成”，而不是完成“交付”。

### 6. MCP connects external live context
当关键上下文不在 repo 里，或数据是动态变化的，就不应靠人工复制粘贴。

MCP 更适合：
- GitHub / CI / 工单 / 监控 / 文档平台
- 会变化的环境状态
- 需要直接调用工具而不是只读静态说明的场景

MCP 的职责是提供外部实时能力，不负责定义规则、方法或调度。

### 7. Skills package repeatable methods
当某类任务反复出现，而且你总在重复同一套 prompt、步骤或纠错逻辑时，它就应该升级成 skill。

skill 适合承载：
- 明确输入/输出
- 固定执行步骤
- 配套脚本、模板、检查单
- 某一类工作的 SOP

也就是：`AGENTS.md` 写“平时怎么做事”，skill 写“这类事具体怎么做”。

### 8. Automations schedule stable workflows
automation 不负责设计方法，只负责按时间和环境调度已经成熟的方法。

适合自动化的前提是：
- 输入模式稳定
- 输出预期稳定
- 人工纠偏需求低
- 已经人工跑顺多次

因此更合理的顺序是：
- 先手动跑通
- 再做 skill
- 最后再做 automation

## Decision rules
### When to use AGENTS.md
如果问题是“这个仓库里 agent 平时该遵守什么规则”，放 `AGENTS.md`。

### When to use a skill
如果问题是“这类任务以后都按这套方法做”，做成 skill。

### When to use MCP
如果问题是“agent 需要连接 repo 外部系统，读取实时数据或执行工具动作”，用 MCP。

### When to use automation
如果问题是“这件事已经稳定了，希望定时自动跑”，用 automation。

## Practical operating order
更稳的落地顺序通常是：
1. 写最小可用的 `AGENTS.md`
2. 为一个高频任务建立 skill
3. 只接入 1 到 2 个最有价值的 MCP
4. 等流程稳定后再做 automation

这条顺序的本质是先固化规则，再固化方法，再接入外部能力，最后才做调度放大。

## Common mistakes
- 把长期规则继续塞在 prompt 里，而不是迁移到 `AGENTS.md`
- 在多步复杂任务上跳过 planning
- 还没稳定就急着自动化
- 一开始把所有外部工具都接入，导致复杂度失控
- 只让 agent 生成代码，不要求验证和审查
- 一个线程长期混装多个任务，导致上下文膨胀

## Relationship to repository intelligence

`[[repository-level-code-intelligence-layer]]` adds a repo-analysis layer beneath `AGENTS.md`: durable repo rules and context files should be informed by indexed structure, dependency graph signals, Git history, and verified architecture decisions rather than hand-written summaries alone.

## Related
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[claude-code-practical-workflow-tips]]
- [[repository-level-code-intelligence-layer]]
- [[hermes-ai-workflow-formalization-principles]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
