---
title: Loop Engineering for Hermes Agent Workflows
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [agent, ai-coding, workflow, automation, subagent, orchestration, hermes]
sources: [raw/articles/addyosmani-loop-engineering-2026-06-08.md, skill:coding-agent-delegation, skill:subagent-driven-development]
status: stable
---

# Loop Engineering for Hermes Agent Workflows

## Summary

Loop engineering 是把 coding agent 从“一轮 prompt → 一轮回答”的交互，提升为可审计的工作闭环：发现任务、隔离执行、验证结果、记录状态，并决定下一步。对 Hermes 来说，它不是立即新增 cron/daemon/runtime 的理由，而是把现有 `delegate_task`、external coding-agent lanes、skills、run artifacts、project-local 工作区和父级验证组织成更稳定的执行规则。

## Durable principle

Hermes 中的 agent loop 应被设计为可审计闭环：自动或半自动发现任务，隔离执行，独立验证，外部记录状态，并在人类确认点前停止。任何 runtime、cron、MCP、gateway、wrapper 或生产侧自动改动都必须另走 active-layer 审批、备份、验证和回滚。

## Source idea

Addy Osmani 的《Loop Engineering》把 loop 拆成几个构件：

- automations：周期性发现、分发、triage 任务；
- worktrees：隔离并行 agent 的修改，避免互相覆盖；
- skills：把项目规约和经验沉淀成可复用上下文；
- plugins/connectors：连接 issue、Slack、数据库、CI 等外部系统；
- sub-agents：让不同 agent 分担执行、检查、研究等角色；
- external memory/state：把状态写到 repo、Markdown、issue tracker 或 run artifacts，而不是依赖模型上下文。

文章同时强调风险：token 成本、错误被循环放大、理解债务和“认知投降”。因此 Hermes 采用它时应偏向可审计 workflow rule，而不是自动化权限扩张。

## Hermes mapping

### 1. Concept layer

本页保存术语和架构映射，连接 [[agent-self-validation-loops]]、[[subagent-orchestration-patterns]]、[[agent-context-engineering]] 和 [[hermes-context-layer-operating-rules]]。

### 2. Direct skill/reference adoption

当文章原则已经由现有 Hermes 能力支持，且只是 prose/reference 执行规则时，可以进入已有 skill/reference，而不是停在 wiki-only：

- maker-checker separation：写入 lane 与验证 lane/父 Agent 分离；
- external state over context：长任务状态写入 project-local 文件、run artifacts、issue 或 wiki，而不是只靠上下文；
- parent verification：subagent 或外部 coding agent 的自报不是完成证据；
- isolated write lanes：并行写入必须使用 worktree、独立目录、project-local sandbox 或明确的父级串行整合。

### 3. Guarded default

以下行为适合成为 guarded default，而不是大型 pilot：

- bounded repair loop：实现 → 验证 → 修复 → 复查，默认有 2–3 轮上限；
- 失败信号保留：连续同类失败时停止，输出 failure signal 和根因假设；
- 父级验收：父 Hermes 读回 diff、artifact、测试输出或路径后才能声明完成；
- 成本控制：只有任务可独立、可验证、上下文隔离收益明确时才 fan-out。

### 4. Active proposal only

以下只属于 active proposal，不因文章本身获得授权：

- 新建长期 cron/daemon loop；
- 修改 Hermes runtime、gateway、MCP、wrapper 或 profile；
- 自动 push/PR/deploy/delete；
- 对生产、云服务、数据库或外部系统产生写副作用；
- 让 agent pool/team 常驻运行。

这些需要单独 plan、scope、备份、验证、回滚和用户确认。

## Adoption rule

面对 AI coding workflow 文章时，Hermes 应先判断：

1. 这是新概念，还是给已有实践命名？
2. Hermes 是否已有对应 primitive？
3. 是否只是 prose/reference 规则？
4. 是否会产生外部副作用或 active-layer 变化？
5. 是否需要 project-local pilot，还是可以直接进入 existing skill/reference？

如果能力已存在且规则无副作用，优先 direct skill/reference adoption；如果会消耗大量 token、可能扩 scope 或需要循环执行，作为 guarded default；如果涉及 runtime/cron/MCP/gateway/wrapper，降级为 active proposal。

## Operating rules

- 不要把所有文章启发都压成 wiki-only；这会形成沉淀但不改变日常行为的 stall pattern。
- 不要因为文章提到 automation 就直接创建自动化；先判断是否已有 Hermes primitive 可承载。
- 并行 agent 写入默认需要隔离工作区或明确的父级整合顺序。
- Maker 和 Checker 不能只靠同一个 agent 的自我声明；至少要有验证命令、独立 reviewer、父级 diff/artifact 检查中的一种。
- 长任务必须有外部状态：计划、todo、run artifact、project-local note、issue 或 wiki，而不是只有聊天上下文。
- Active-layer 改动继续按 [[hermes-layer-routing-decision-checklist]] 和 [[hermes-lifeos-layer-boundary-contract]] 审批。

## What not to promote

- 不照搬 Codex/Claude Code 的命令名、目录结构或产品模板，除非要集成对应工具。
- 不把“loop engineering 是未来”当成已证实结论；它是有用的趋势框架。
- 不把自动 loop 视为正确性证据；真实测试、diff、artifact、审查和人类验收仍是完成标准。
- 不把本页变成 runtime 改造计划；runtime/cron/MCP/gateway/wrapper 都需要单独批准。

## Related

- [[agent-self-validation-loops]]
- [[subagent-orchestration-patterns]]
- [[agent-context-engineering]]
- [[ai-coding-agent-workflow-types]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-layer-routing-decision-checklist]]
- [[hermes-lifeos-layer-boundary-contract]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
