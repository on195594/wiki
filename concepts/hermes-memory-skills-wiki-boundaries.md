---
title: Hermes Memory Skills Wiki Boundaries
created: 2026-04-16
updated: 2026-06-18
type: concept
tags: [hermes, knowledge-base, workflow, configuration]
sources: []
status: stable
description: 定义 Hermes memory、skills、wiki 和 sessions 的归类边界，避免把偏好、流程、正式知识和临时上下文混放。
aliases: [layer-boundaries, memory-skill-wiki-boundaries]
---

# Hermes Memory Skills Wiki Boundaries

## Summary
`memory`、`skills`、`wiki` 都是 Hermes 的长期能力组成部分，但三者职责完全不同。
判断边界的核心原则不是“这个信息重不重要”，而是“它属于偏好与事实、可复用流程，还是正式知识资产”。

## One-line definitions
- `memory`：短小、稳定、长期有效的偏好与事实
- `skills`：可复用的操作流程与方法手册
- `wiki`：结构化、可检索、可链接、可持续维护的正式知识资产

## Boundary rule
可以用一句话判断：
- 如果是“以后我需要记住这个人/环境/偏好”，进 `memory`
- 如果是“以后我还会照着这套方法执行”，进 `skills`
- 如果是“以后我还会查阅、扩展、交叉引用这份知识”，进 `wiki`

## What belongs in memory
### 适合进入 memory
- 用户长期偏好
- 机器环境中的稳定事实
- 长期工作规则
- 未来多次任务中都需要快速调用的简短结论

### memory 的特征
- 短
- 稳定
- 高复用
- 不是长文档
- 不是过程记录

### memory 例子
- 用户偏好默认用中文回复
- 下载文件保存到 `~/download`
- 某个固定路径是系统 canonical path
- 用户不希望视频下载通过 xitter，而要走 video-downloader

## What belongs in skills
### 适合进入 skills
- 一套多步、可重复执行的流程
- 某种工具的标准操作方式
- 容易忘，但适合沉淀为“步骤说明书”的方法
- 多次验证过、值得标准化复用的做法

### skills 的特征
- 面向执行
- 强调步骤和验证
- 通常包含触发条件、命令、注意事项、验收方式
- 本质是程序化经验，而不是主题知识

### skills 例子
- 如何安全修改 Hermes 配置
- 如何下载视频并生成短文件名
- 如何测试 fallback model
- 如何做系统化调试

## What belongs in wiki
### 适合进入 wiki
- 概念说明
- 架构设计
- 研究结论
- 横向比较
- 值得长期沉淀的问题与答案
- 需要交叉链接、持续更新、长期查阅的内容

### wiki 的特征
- 面向知识消费与复盘
- 可与其他页面建立 wikilinks
- 能被后续问题复用
- 可以不断增量更新
- 是正式知识层，而不是临时缓存

### wiki 例子
- `[[hermes-knowledge-architecture]]`
- Hermes 的检索优先级与回写闭环
- 某类工具的架构比较
- 经过多轮沉淀后形成的方法论总结

## What does NOT belong
### 不该进 memory 的内容
- 长篇摘要
- 原始文档
- 一次性任务结果
- 临时错误日志
- 会话里的中间推理

### 不该进 skills 的内容
- 纯概念介绍
- 仅在一个任务中出现一次的临时步骤
- 缺少稳定触发条件的偶发经验

### 不该进 wiki 的内容
- 原样复制整段聊天记录
- 没有长期价值的临时问题
- 完全没有结构整理的原始资料

## Relationship between the three
三者不是替代关系，而是分工关系：
- `memory` 让 Hermes 更懂用户和环境
- `skills` 让 Hermes 更会做事
- `wiki` 让 Hermes 更会积累知识

因此，一个主题可能同时触发三层：
- 用户提出长期偏好 → 写入 `memory`
- 形成稳定工作流 → 写入 `skills`
- 沉淀成架构/方法论/对比分析 → 写入 `wiki`

## Decision checklist
遇到一个新信息时，依次问：
1. 这是不是用户偏好或稳定事实？是 → `memory`
2. 这是不是一套可重复执行的方法？是 → `skills`
3. 这是不是值得长期查阅和扩写的知识？是 → `wiki`
4. 如果三者都不是，大概率只该留在 `sessions`

## Operational policy
实际工作中默认遵循：
- 偏好和长期规则，优先压缩成一句写入 `memory`
- 可复用流程，优先沉淀为 `skills`
- 正式知识，优先沉淀为 `wiki`
- 临时进度、一次性排障过程、短期状态，不进入这三者

## Anti-patterns
- 把 memory 当 changelog
- 把 skills 写成百科
- 把 wiki 写成聊天记录仓库
- 同一内容同时塞进 memory、skills、wiki，导致边界混乱

## Practical examples
### 例 1：用户说“以后默认用中文回复”
- 归类：`memory`
- 原因：这是稳定偏好，不是流程，也不是知识页

### 例 2：完成了一套“安全修改 Hermes 配置”的固定流程
- 归类：`skills`
- 原因：这是可重复执行的方法

### 例 3：总结出“Hermes 知识库整体架构”
- 归类：`wiki`
- 原因：这是正式知识资产，适合长期查阅和扩展

## Relations
- refines: [[hermes-knowledge-architecture]]
- depends_on: [[wiki-ingestion-workflow]]
- depends_on: [[hermes-wiki-page-writing-standards]]

## Related
- [[hermes-knowledge-architecture]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
