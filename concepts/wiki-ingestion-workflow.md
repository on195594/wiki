---
title: Wiki Ingestion Workflow
created: 2026-04-16
updated: 2026-06-18
type: concept
tags: [knowledge-base, workflow, research, automation]
sources: []
status: stable
description: 定义把外部材料编译进 Hermes wiki 的标准路径：保存 raw、提炼正式页面、补链接、更新 index 和 log。
aliases: [wiki-ingestion, knowledge-ingestion]
---

# Wiki Ingestion Workflow

## Goal
把链接、文档、对话结论、视频摘要等外部信息，稳定转化为 Hermes 可复用的长期知识。

## Summary
这页定义 Hermes 把外部材料编译进 wiki 的标准入库路径：先保存 raw，再提炼主题与结论，随后更新正式页面、补充链接，并同步维护 `[[index]]` 与 `[[log]]`。

## Standard flow
1. 获取原始材料
   - URL → `raw/articles/`
   - PDF → `raw/papers/`
   - 会议/音视频整理 → `raw/transcripts/`
2. 提炼主题、实体、概念、可复用结论
3. 搜索现有 wiki，避免重复建页
4. 新建或更新正式页面：
   - `entities/`
   - `concepts/`
   - `comparisons/`
   - `queries/`
5. 为页面补充 `[[wikilinks]]`
6. 更新 `[[index]]`
7. 记录到 `[[log]]`

## Filing rules
- 值得长期复用的问答，归档到 `queries/`
- 横向分析放到 `comparisons/`
- 方法论与架构放到 `concepts/`
- 具体项目、模型、组织、产品放到 `entities/`

## Quality bar
满足以下至少一项才进入正式知识层：
- 以后高概率会再次用到
- 需要跨来源综合才能得到
- 对系统设计、配置、决策有长期价值
- 人类重新整理的成本较高

## Anti-patterns
- 把整段聊天直接复制进 wiki
- 没有来源就写死结论
- 只堆 raw，不更新正式页面
- 新建页面后不更新 `[[index]]` 与 `[[log]]`

## Relations
- refines: [[hermes-knowledge-architecture]]
- depends_on: [[hermes-wiki-page-writing-standards]]
- depends_on: [[hermes-retrieval-priority-and-answer-path]]

## Related
- [[hermes-knowledge-architecture]]
- [[hermes-knowledge-base-operating-flow]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[hermes-wiki-page-writing-standards]]
- [[index]]
- [[log]]
