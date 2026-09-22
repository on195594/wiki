---
title: Hermes Layer Routing Decision Checklist
created: 2026-04-17
updated: 2026-09-22
type: concept
tags: [hermes, knowledge-base, workflow, configuration, decision, automation, mcp]
sources: [raw/articles/openai-codex-best-practices-2026-04-17.md, concepts/hermes-memory-skills-wiki-boundaries.md, docs:hermes-agent/user-guide/features/memory, docs:hermes-agent/user-guide/features/skills, docs:hermes-agent/user-guide/features/cron, docs:hermes-agent/user-guide/features/mcp]
status: stable
description: 以内容归属、执行方法、触发方式、外部能力和运行状态五个可组合维度判断 Hermes 层间路由。
aliases: [layer-routing-checklist]
---

# Hermes Layer Routing Decision Checklist

## Summary
这页把 `[[hermes-agent-workflow-layering-and-adoption-order]]` 再往前推进一层，变成可执行的路由判定清单。它不是要求在 `wiki`、`memory`、`skill`、`cron` 与 `MCP` 中五选一，而是把需求拆成五个可组合维度：内容归属、执行方法、触发方式、外部能力和运行状态。`memory`、`skills`、`cron`、`MCP` 的角色以目标 Hermes 版本的官方文档和实际工具列表为准；`wiki` 是这套知识库架构里的本地长期知识层，不是 Hermes 官方内置 primitive。

## Official baseline first
本页引用的 Hermes 文档把这些角色区分为：

- `memory`：受预算约束的持久记忆层，用于短小偏好、环境事实和长期约束
- `skills`：按需加载的程序化知识与方法文档
- `cron`：为稳定重复任务提供定时触发
- `MCP`：连接外部工具服务器与动态能力
- `wiki`：不是 Hermes 官方原生特性；它是当前这套本地知识库架构中的正式知识资产层

这些是路由角色，不证明目标部署当前已启用、支持或授权对应能力。执行前应核对目标版本的官方文档与实际工具列表；讨论 `wiki` 时则遵守本仓库规则。

## One-screen routing rule
对同一需求分别回答五个问题，不在第一个“是”处停止：

1. **内容归属**：公开且长期可复用的正式知识进 `wiki`；短小稳定且适合默认保留的事实进 `memory`；项目局部内容进项目文档或状态；临时、私有或一次性内容留在 session、项目记录或 Git 历史。
2. **执行方法**：重复、已验证的方法可形成 `skill`；一次性操作不必为了留痕而 skill 化。
3. **触发方式**：默认人工或按需触发；只有方法稳定、失败边界清楚且目标部署确认支持并授权时，才考虑 `cron`。
4. **外部能力**：需要动态外部数据或操作时，先确认已有且获准的连接方式；只有目标部署实际支持且适配时才选择 `MCP`。
5. **运行状态**：当前结果、队列、故障和执行进度从 live system、project state 或 logs 读取，不写成 Wiki 当前事实。

一个场景可以同时得到 `wiki + skill + cron + MCP`，但每层只承载自己的部分；组合不等于复制同一内容。

## Layer-by-layer checklist
### 1. Put it in memory when
只有同时满足“短、小、稳、长期有用”时，才进 `memory`。

检查项：
- 这是用户偏好、沟通方式或长期工作习惯吗？
- 这是环境里的稳定事实或长期约束吗？
- 这条信息能压缩成一句高密度结论吗？
- 它值得在未来很多任务里默认可见吗？
- 它不是长文档、原始资料、一次性任务状态吗？

适合：
- 用户偏好默认用中文
- 某 canonical path 或环境约束
- 稳定工具 quirks
- 长期 workflow 规则

不适合：
- 长摘要
- 临时排障过程
- 一次性任务结果
- 大段原始资料

来源边界：
- 本页引用的文档把 `memory` 描述为有字符预算的 curated persistent memory
- 其中列举 user preferences、environment facts、conventions 和长期 lessons learned
- 具体预算与当前行为需按目标版本复核；无论版本如何，都不把它当无限知识库或长文档仓库

### 2. Put it in a skill when
只要核心问题变成“以后要按这套方法做”，优先考虑 `skill`。

检查项：
- 这是一个多步、可复用、可验证的方法吗？
- 这个方法已经出现重复 prompt 或重复纠错了吗？
- 是否需要明确触发条件、步骤、坑点、验证方式？
- 这更像 SOP，而不是概念介绍吗？
- 这不是单纯的定时需求吗？

适合：
- 标准调试流
- 安全修改配置
- 固定的 PR review / 发布说明 / 巡检方法
- 某类工具的标准操作手册

不适合：
- 单纯概念说明
- 只出现一次的临时过程
- 只是“每天跑一次”的调度需求

来源边界：
- 本页引用的文档把 `skills` 描述为 on-demand knowledge documents 和 procedural memory
- 这里据此承载复杂任务与纠错后形成的稳定工作流
- 目标版本是否支持相同加载与管理行为，执行前另行复核

### 3. Put it in cron when
`cron` 不是方法层，而是调度层。只有方法先稳定，才值得升级到 `cron`。

检查项：
- 这件事是否已经人工跑顺很多次？
- 输入模式是否稳定？
- 输出目标是否清晰？
- 是否能接受 fresh session 运行，不依赖当前聊天上下文？
- 是否已经有自包含 prompt，或有合适 skill 可加载？
- 失败代价是否可控？

适合：
- 定期总结 commits
- 定期检查 CI 失败
- 定时巡检服务状态
- 定时生成简报或摘要

不适合：
- 还要人工频繁纠偏的流程
- 只是在脑中有概念、方法还没收敛的事情
- 严重依赖当前线程隐含上下文的任务

来源边界：
- 本页引用的文档将 cron 描述为在 fresh agent sessions 中运行，prompt 自包含或配合 attached skills
- 这里据此只把 cron 当触发方式，不把它当方法或内容归属层
- 目标版本的会话、附加 skill 与调度行为必须在实际启用前复核

### 4. Put it in MCP when
`MCP` 解决的是“能力接入”，不是知识沉淀，也不是方法沉淀。

检查项：
- 需要的信息是否在 Hermes 现有上下文之外？
- 数据是否会动态变化？
- 是否需要直接操作外部工具，而不是只读本地知识？
- 这个接入是否真的能减少复制粘贴和手工往返？
- 是否能控制暴露面，只开放需要的工具？

适合：
- GitHub / CI / 监控 / 数据库 / 内部 API / 文件系统等外部工具接入
- 会变化的实时状态查询
- 需要 agent 直接调用的外部系统

不适合：
- 长期知识存储
- 稳定流程说明
- 调度逻辑

来源边界：
- 本页引用的文档把 MCP 描述为外部 tool servers 接入层，并提到 stdio / HTTP 与 per-server filtering
- 这里据此把 MCP 视为外部能力维度，而不是知识或方法载体
- 可用传输、过滤和权限以目标版本与部署配置为准

### 5. Put it in wiki when
`wiki` 是本地知识资产层，适合正式知识，不适合任务态缓存。

检查项：
- 这是概念、架构、比较、案例、长期问答或外部文章编译结果吗？
- 未来回答问题时，值得被检索、引用、扩写吗？
- 它是否需要与其他页面建立链接？
- 它是否适合公开，且脱离作者私有环境仍可理解？
- 它是否已经整理成正式页面，而不是私有会话、一次性 closeout、执行记录或 raw dump？

适合：
- 架构分层规则
- 知识边界说明
- 外部文章编译后的长期结论
- 比较分析与设计判断

不适合：
- 原样聊天记录
- 一次性任务进度
- 原始日志和未整理资料

本地架构对齐点：
- `wiki` 是当前知识库设计里的正式知识层
- 它服务于长期检索、交叉链接、后续增量维护
- 它不是 Hermes 官方替代 memory 的 built-in store

## Five independent decisions

| 维度 | 要回答的问题 | 可能结果 |
|---|---|---|
| 内容归属 | 哪些内容值得持久化，公开边界允许放在哪里？ | `wiki`、`memory`、项目文档/状态、session/history |
| 执行方法 | 是否已有可重复、可验证的做法？ | `skill` 或当前任务内指令 |
| 触发方式 | 谁在何时启动？ | 人工、按需，或经核验与授权的 `cron` |
| 外部能力 | 是否需要动态外部数据或动作？ | 已有获准工具、经核验的 `MCP`，或不接入 |
| 运行状态 | 当前发生了什么，真相源在哪里？ | live system、project state、logs；不是 Wiki 推断 |

判断可以有多个结果，也可以某些维度为空。先拆职责，再检查组合是否必要；不要因为需要调度就自动创建 skill，也不要因为使用 MCP 就把外部状态写进 Wiki。

## Anti-confusion rules
### memory vs wiki
- 短小稳定事实 → `memory`
- 长期查阅知识 → `wiki`
- 如果需要多段结构、来源、链接、持续扩写，通常就不该进 `memory`

### skill vs wiki
- 回答“怎么做” → `skill`
- 回答“这是什么 / 为什么这样分层” → `wiki`

### skill vs cron
- 定义方法 → `skill`
- 定义什么时候自动跑 → `cron`

### MCP vs wiki
- 外部实时能力 → `MCP`
- 整理后的稳定知识 → `wiki`

### MCP vs skill
- 接工具能力 → `MCP`
- 用这能力怎么稳定做一类事 → `skill`

## Synthetic examples
以下只演示职责组合，不表示某个连接器、任务或调度已经部署或获批。

### 例 1：周期性检查外部 CI 并形成摘要
- **内容归属**：通用且适合公开的判定原则可进 `wiki`；目标仓库配置和收件人留在项目或私有配置
- **执行方法**：重复且验证过的检查步骤可进 `skill`
- **触发方式**：先人工或按需运行；目标版本支持、风险可控且另有授权时才使用 `cron`
- **外部能力**：按实际部署选择已获准的工具；需要且已核验时才可能是 `MCP`
- **运行状态**：每次 CI 结果留在 CI、project state 或运行日志，不写成 Wiki 当前事实

### 例 2：一次私有故障暴露出通用恢复原则
- **内容归属**：私有日志、会话和 closeout 留在原载体；只有去标识化、适合公开且长期可复用的原则才编译进对应 Wiki 正式页
- **执行方法**：若恢复步骤重复验证后稳定，可另行形成 `skill`
- **触发与外部能力**：没有独立需求就保持为空，不为凑齐层次而增加 `cron` 或 `MCP`
- **运行状态**：故障是否仍存在必须实时核验

### 例 3：整理一篇公开 agent 架构文章
- **内容归属**：有长期价值的来源与综合结论可进入 `wiki`
- **执行方法**：只有文章整理流程确实重复且已验证时才需要 `skill`
- **其余维度**：没有定时、外部动态操作或运行状态需求时，不需要 `cron`、`MCP` 或状态页

## Minimal operating checklist
每次遇到“这个该放哪儿”时，分别记录：
- 内容归属：`wiki`、`memory`、项目载体还是 session/history？
- 执行方法：需要 `skill`，还是一次性指令已足够？
- 触发方式：人工、按需，还是经核验与授权的 `cron`？
- 外部能力：已有工具是否足够；是否确实需要且支持 `MCP`？
- 运行状态：应从哪个 live source、project state 或 log 读取？

没有需求的维度留空；多个维度命中时按职责组合，不做互斥单选。

## Relations
- depends_on: [[hermes-memory-skills-wiki-boundaries]]

## Related
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-knowledge-architecture]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
