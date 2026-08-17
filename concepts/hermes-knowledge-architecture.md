---
title: Hermes Knowledge Architecture
created: 2026-04-16
updated: 2026-08-17
type: concept
tags: [hermes, knowledge-base, agent, mcp, workflow, configuration]
sources: [raw/articles/towardsdatascience-persistent-knowledge-layer-2026-08-16.md]
status: stable
description: 定义 Hermes 长期知识系统的 canonical 分层，包括 memory、skills、sessions、wiki、raw 与 MCP/tools 的职责边界。
aliases: [knowledge-architecture, hermes-wiki-architecture]
---

# Hermes Knowledge Architecture

## Summary
Hermes 的知识体系不是单一“记忆库”，而是分层协作系统。
其中，`wiki` 是正式知识资产层；`memory`、`skills`、`sessions`、`tools/MCP` 分别承担不同职责，共同组成可持续积累、可检索、可回写的知识闭环。

## Architecture at a glance
可以把 Hermes 的知识体系拆成两层：

1. Hermes 运行时知识栈
2. Wiki 文件系统结构

二者关系是：Hermes 通过工具和流程读写 wiki，而不是把长期知识直接塞进 prompt memory。

## Layer 1: Hermes runtime knowledge stack
### 1. memory
- 保存短小、稳定、长期有效的用户偏好与环境事实
- 适合：沟通偏好、固定路径约定、长期工作规则
- 不适合：长文档、研究材料、一次性任务结果

### 2. skills
- 保存可复用流程与操作方法
- 适合：配置修复流程、下载流程、审计流程、调试流程
- 本质上是“程序化知识”而不是“内容知识”

### 3. sessions / session_search
- 保存历史会话与阶段性上下文
- 适合：回忆上次做过什么、查找某次排障经过
- 不应作为正式知识库替代品

### 4. wiki
- 正式知识资产层
- 保存结构化、可维护、可交叉链接的 Markdown 页面
- 是回答知识问题时的首选来源，也是长期沉淀的 canonical layer

### 5. tools / MCP
- 负责把外部系统、检索能力、写回能力暴露给 Hermes
- 当知识库继续扩展时，可把 wiki search/read/write 进一步工具化
- 这层负责“连接”，不是知识本体

## Layer 2: Wiki filesystem architecture
### 1. Navigation layer
- `[[index]]`：知识目录与入口
- `[[log]]`：知识库变更历史
- `SCHEMA.md`：结构规则、标签体系、页面规范

### 2. Raw source layer
- `raw/articles/`
- `raw/papers/`
- `raw/transcripts/`
- `raw/assets/`

这一层只保存原始材料，原则上不直接改写。

### 3. Compiled knowledge layer
- `entities/`：实体页，例如产品、组织、模型、项目
- `concepts/`：概念页，例如架构、方法论、机制
- `comparisons/`：横向比较
- `queries/`：值得长期保留的问题与答案

这一层才是知识沉淀的主战场。

## Conflict-aware knowledge primitives and temporal scoping

知识层不能只保存整理后的结论，还必须表达结论的适用边界、来源冲突和当前未知项。否则，一条写入错误的长期结论会持续污染后续检索与回答。

来源文章给出三类可复用的知识对象：

- **Decision**：保存规则或结论、适用范围、生效时间、替代关系、决策理由和原始来源。仅凭“文档更新”不能推断新规则适用于所有对象或历史时点。
- **Contradiction**：并列保存相互冲突的主张、各自来源与有效时间、责任方及未解决原因。冲突未被权威证据消解前，不按文档新旧或语义相似度自动选边。
- **Open Question**：显式记录因证据缺失、范围不清或冲突未决而无法回答的问题，以及形成结论仍需补充的证据。

由此得到的本地知识写入约束是：

- `[推论]` 最新来源不自动等于当前适用来源；必须同时检查对象范围、生效日期和替代关系。
- `[推论]` 遇到无法确定性解决的来源冲突时，知识编译应 fail closed：保留冲突并停止生成确定性结论，而不是让模型自行调和。
- `[推论]` 模型可提出知识补丁，但持久化写入仍由可验证规则和明确授权控制；文章中的 Azure、Cosmos DB、向量或图存储仅是实现示例，不构成本地技术选型。

## Canonical rule
在 Hermes 的长期知识体系里：
- `memory` 是偏好与稳定事实层
- `wiki` 是正式知识层
- `raw` 是来源层
- `sessions` 是回忆层
- `skills` 是方法层

因此：
- 长期知识以 wiki 为准
- 短期对话上下文不等于知识资产
- raw 来源不能代替整理后的知识页
- 技能不能代替概念/实体知识页

## Retrieval and write-back loop
标准闭环如下：
1. 用户提出问题、链接、文档或主题
2. Hermes 先查 `[[index]]` 与相关页面
3. 若 wiki 不足，再去读取 raw 或外部资料
4. 经过提炼后，更新正式页面或新增页面
5. 同步更新 `[[index]]` 与 `[[log]]`
6. 后续问题继续优先使用 wiki 中已编译的知识

这就是 `[[wiki-ingestion-workflow]]` 的落地方式。

## What goes where
### 应进入 memory 的内容
- 用户长期偏好
- 机器环境中的稳定事实
- 持续适用的工作规则

### 应进入 skills 的内容
- 一套稳定可复用的流程
- 明确的命令序列
- 容易遗忘、但可标准化的操作手册

### 应进入 wiki 的内容
- 概念解释
- 架构设计
- 对比分析
- 研究结论
- 值得长期复用的问题与答案

### 只应留在 sessions 的内容
- 某次会话中的临时尝试
- 中间过程
- 短期任务状态

## Design constraints
- 不把长文档直接塞进 memory
- 不把聊天记录原样当知识库
- 不只堆 raw 而不生成正式页面
- 每个正式页面都应可检索、可链接、可增量维护
- 知识问题默认先查 wiki，再外部补充，再回写 wiki

## Integration points
### Obsidian
- 作为浏览与编辑前端
- 使用 wikilinks 和 frontmatter 直接消费 wiki 目录
- 与 `OBSIDIAN_VAULT_PATH=/home/lin/wiki` 对齐

### MCP / native tools
- 当 wiki 规模扩大后，可把 search/read/write 封装成原生工具
- 让 Hermes 不是“知道 wiki 在哪里”，而是“可以直接调用 wiki 能力”

## Practical interpretation
如果把 Hermes 看成一个系统：
- memory = 用户与环境的稳定配置层
- skills = 可执行经验层
- sessions = 会话轨迹层
- wiki = 正式知识层
- MCP/tools = 外部能力接入层

如果把 wiki 看成一个系统：
- SCHEMA/index/log = 导航与治理层
- raw = 原始来源层
- entities/concepts/comparisons/queries = 编译后的知识层

这两套结构叠在一起，才构成完整的 Hermes 知识库整体架构。

## Relations
- depends_on: [[hermes-memory-skills-wiki-boundaries]]
- depends_on: [[wiki-ingestion-workflow]]
- depends_on: [[hermes-retrieval-priority-and-answer-path]]

## Related
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
