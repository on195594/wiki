---
title: Best practices – Codex
author: OpenAI Developers
source_type: article
source_url: https://developers.openai.com/codex/learn/best-practices
published_at: unknown
captured_at: 2026-04-17
status: raw
---

# Summary capture

## Core claim
这篇文章的核心观点是：Codex 的效果提升，主要不靠一次次把 prompt 写得更花，而靠把 agent 工作方式逐步工程化——先给清晰任务上下文，再把长期规则沉淀进 `AGENTS.md`，再通过配置、测试审查、MCP、skills 和 automations，把一次性协助升级成可持续复用的工程搭子。

## Key points
- prompt 的默认结构应包含四部分：`Goal`、`Context`、`Constraints`、`Done when`。
- 复杂任务先做 plan，而不是直接编码；可用 Plan mode、访谈式澄清、或 `PLANS.md` 模板。
- `AGENTS.md` 用来承载仓库级长期规则，避免把稳定指导反复塞进 prompt。
- `config.toml`、approval policy、sandbox mode、profiles 和 MCP 配置决定 Codex 跨会话的一致性。
- 不要只让 Codex 写代码；还要让它补测试、跑检查、审 diff、验证结果。
- 当所需上下文在 repo 外部、且会动态变化时，用 MCP 连接外部系统和工具。
- 重复工作先收敛成 skill，再在流程足够稳定后做 automation。
- session / thread 管理会直接影响质量；一个线程最好只承载一个连贯任务。

## Important facts
- reasoning effort 建议：
  - `Low`：小而快、边界清晰的任务
  - `Medium` / `High`：复杂改动或调试
  - `Extra High`：长链路、强推理、强 agentic 任务
- `AGENTS.md` 可按层级放置：
  - 全局：`~/.codex`
  - 仓库级
  - 子目录级
  - 就近文件优先生效
- 推荐配置位置：
  - 个人默认：`~/.codex/config.toml`
  - 仓库特化：`.codex/config.toml`
- 文章强调的常见命令/控制项包括：`/init`、`/review`、`/resume`、`/fork`、`/compact`、`/agent`。
- MCP 适合“上下文不在 repo 内、数据变化快、需要工具调用”的场景。
- 文章给出的典型重复任务包括：日志排查、发布说明、PR review、迁移规划、事故摘要、调试流程、提交总结、CI 故障检查等。

## Practical takeaway
文章真正强调的是一条分层路线：
1. prompt 定义单次任务目标
2. `AGENTS.md` 固化仓库规则
3. skill 固化某类任务的方法
4. MCP 提供 repo 外实时上下文
5. automation 调度成熟流程

也就是：不要把所有东西都堆进 prompt；要把 agent 的规则、方法、外部接口和调度层分开建模。

## Applicability
- 大型代码仓库或多人协作仓库
- 高频重复的工程任务
- 需要接入 CI、GitHub、工单、监控等外部系统的工作流
- 已经开始把 AI coding agent 当成长期工程基础设施使用的团队

## Limits
- 这是官方最佳实践文档，不是不同配置效果的量化实验。
- 文中主要讲工作流设计，对具体模型差异、成本、失败率和误操作案例展开不多。
- 更适合持续工程协作场景，对一次性脚本或极小项目可能偏重。