---
title: Hermes Layer Routing Decision Checklist
created: 2026-04-17
updated: 2026-05-18
type: concept
tags: [hermes, knowledge-base, workflow, configuration, decision, automation, mcp]
sources: [raw/articles/openai-codex-best-practices-2026-04-17.md, concepts/hermes-memory-skills-wiki-boundaries.md, docs:hermes-agent/user-guide/features/memory, docs:hermes-agent/user-guide/features/skills, docs:hermes-agent/user-guide/features/cron, docs:hermes-agent/user-guide/features/mcp]
status: stable
description: 提供判断内容应进入 wiki、memory、skill、cron、MCP 或 session 的路由检查清单。
aliases: [layer-routing-checklist]
---

# Hermes Layer Routing Decision Checklist

## Summary
这页把 `[[hermes-agent-workflow-layering-and-adoption-order]]` 再往前推进一层，变成可执行的路由判定清单：一个新信息、方法、能力或自动化需求出现时，应该进入 `wiki`、`memory`、`skill`、`cron` 还是 `MCP`。这页显式以 Hermes 官方文档为校准基线：`memory`、`skills`、`cron`、`MCP` 的定义与边界，优先对齐官方；`wiki` 则是当前这套 Hermes 知识库架构里的本地长期知识层，不是 Hermes 官方内置 primitive。

## Official baseline first
先明确哪些是 Hermes 官方概念，哪些是我们本地扩展层：

- `memory`：官方内置，受字符预算约束的持久记忆层，用于用户偏好、环境事实、长期约束
- `skills`：官方内置，按需加载的程序化知识与方法文档，是 agent 的 procedural memory
- `cron`：官方内置，定时运行的 fresh-session 调度层，用于稳定重复任务
- `MCP`：官方内置，连接外部工具服务器与实时能力的集成层
- `wiki`：不是 Hermes 官方原生特性；它是当前这套本地知识库架构中的正式知识资产层

这意味着：
- 讨论 `memory / skills / cron / MCP` 时，应优先遵守官方定义
- 讨论 `wiki` 时，应遵守当前本地知识库规则，不要误说成 Hermes 官方 feature

## One-screen routing rule
看到一个新东西时，按这个顺序判断：

1. 这是外部实时工具或数据接入需求吗？是 → `MCP`
2. 这是稳定重复执行的方法吗？是 → `skill`
3. 这是已经跑稳、需要按时间自动执行的方法吗？是 → `cron`
4. 这是短小、稳定、长期有效的偏好或环境事实吗？是 → `memory`
5. 这是值得长期查阅、扩展、交叉引用的正式知识吗？是 → `wiki`
6. 如果都不是，大概率只该留在当前 session / thread

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

官方对齐点：
- 官方文档把 `memory` 定义为有严格字符预算的 curated persistent memory
- 适合放 user preferences、environment facts、conventions、长期 lessons learned
- 不适合把它当无限知识库或长文档仓库

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

官方对齐点：
- 官方文档把 `skills` 定义为 on-demand knowledge documents
- 本质是 agent 的 procedural memory
- 适合沉淀复杂任务、纠错后形成的稳定工作流

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

官方对齐点：
- 官方文档明确说明 cron jobs 在 fresh agent sessions 里运行
- prompt 必须 self-contained，或配合 attached skills
- cron 负责 schedule，不负责定义方法本身

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

官方对齐点：
- 官方文档把 MCP 定义为外部 tool servers 接入层
- 支持 stdio / HTTP server
- 强调 per-server filtering 与最小暴露面

### 5. Put it in wiki when
`wiki` 是本地知识资产层，适合正式知识，不适合任务态缓存。

检查项：
- 这是概念、架构、比较、案例、长期问答或外部文章编译结果吗？
- 未来回答问题时，值得被检索、引用、扩写吗？
- 它是否需要与其他页面建立链接？
- 它是否比 session 记录更稳定、更结构化？
- 它是否已经整理成正式页面，而不是原始聊天或 raw dump？

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

## Decision order that avoids drift
为了避免层间串味，实际判断顺序建议固定成：

1. 先问：这是能力接入问题吗？是 → `MCP`
2. 再问：这是执行方法问题吗？是 → `skill`
3. 再问：这是已稳定方法的调度问题吗？是 → `cron`
4. 再问：这是短小稳定事实吗？是 → `memory`
5. 最后问：这是正式知识资产吗？是 → `wiki`

为什么把 `wiki` 放在后面：
- 很多东西看起来“值得记”，但其实是方法或偏好，不是知识页
- 很多东西看起来“需要保存”，但其实只该在 session 里短期保留

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

## Practical examples
### 例 1：用户说“以后 Hermes 相关设计要参考官方文档”
- 归类：`memory`
- 原因：这是稳定工作偏好与校准规则，短而长期有效

### 例 2：总结出“如何把外部 agent 架构文章转成 Hermes 知识资产”
- 归类：`skill` + `wiki`
- 原因：方法本身可做 skill；沉淀后的架构结论可进 wiki

### 例 3：接 GitHub issue / CI / 监控系统
- 归类：`MCP`
- 原因：这是外部实时能力接入，不是知识页，也不是记忆条目

### 例 4：每天早上自动检查失败流水线并发回摘要
- 归类：`skill` + `cron`
- 原因：先有检查方法，再用 cron 定时调度

### 例 5：把“层间路由边界”写成正式规则页
- 归类：`wiki`
- 原因：这是长期查阅与交叉引用的正式知识资产

## Minimal operating checklist
每次遇到“这个该放哪儿”时，快速过一遍：
- 外部实时工具接入？→ `MCP`
- 固定方法 / SOP？→ `skill`
- 稳定定时任务？→ `cron`
- 短小稳定偏好或事实？→ `memory`
- 正式知识资产？→ `wiki`
- 都不是？→ 留在 session

## Relations
- depends_on: [[hermes-memory-skills-wiki-boundaries]]

## Related
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-knowledge-architecture]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
