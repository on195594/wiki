---
title: Wiki Ingestion Workflow
created: 2026-04-16
updated: 2026-08-18
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
   - 重要结论、数字、当前外部行为和规范性规则尽量在同段或相邻句放具体来源；本地推导使用 `[推论]`
   - 外部厂商控制的产品行为、接口或命令集按需要使用 `review_by`
5. 为页面补充 `[[wikilinks]]`
6. 更新 `[[index]]`；已关闭的历史 plan/audit 不必进入主索引
7. 在 `[[log]]` 只记录 durable delta、证据边界和验证结果
8. 运行 Wiki health check 与 `git diff --check`

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
- 普通低风险摄取也默认生成独立 AI review、exit/stderr 和前后 hash sidecar

## Review trigger

独立 AI 审查不是普通摄取的默认步骤。只在 Schema/治理规则变更、跨层推广、高风险事实、多来源冲突或确定性检查不足时触发；其他情况由现有 health check、Git diff 和父级事实核验收口。

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
