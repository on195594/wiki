---
title: Hermes Wiki Page Writing Standards
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [hermes, knowledge-base, workflow, configuration, note]
sources: []
status: stable
---

# Hermes Wiki Page Writing Standards

## Summary
Hermes wiki 页面不是随手笔记，而是正式知识资产。
写作规范的目标是让页面可读、可链接、可维护、可增量更新，并能被后续回答直接复用。

## Canonical principle
一篇合格页面至少要满足：
- 主题明确
- 结构统一
- frontmatter 完整
- 至少有 2 个有效 wikilinks
- 能持续更新
- 不等于原始资料，也不等于聊天记录

## File naming
- 文件名使用小写英文加连字符
- 不用空格，不用中文文件名
- 文件名应直接表达主题

示例：
- `hermes-knowledge-architecture.md`
- `hermes-memory-skills-wiki-boundaries.md`
- `hermes-retrieval-priority-and-answer-path.md`

## Required frontmatter
每个正式页面必须包含：
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [tag1, tag2]
sources: []
status: draft | stable
---
```

字段要求：
- `title`：人类可读标题
- `created`：首次创建日期
- `updated`：最近更新时间
- `type`：必须匹配目录职责
- `tags`：只能使用 `SCHEMA.md` 中已定义的标签
- `sources`：来源路径；无来源时可先留空数组
- `status`：草稿或稳定态

## Recommended structure
推荐默认结构：
1. `## Summary`
2. 主体内容（按层次分节）
3. `## Practical checklist` 或 `## Decision rules`（如适用）
4. `## Anti-patterns`（如适用）
5. `## Related`

最少也要有：摘要、主体结构、关联链接。

## Writing style
- 先给结论：开头先写 Summary，第一屏就回答“这页在讲什么”
- 结构先于堆料：先分层，再展开；优先使用小节和列表
- 可扫描：段落短、标题清晰、30 秒内能抓到重点
- 面向复用：页面服务未来回答与维护，而不是只记录一次

## Wikilinks rules
每个正式页面至少应包含 2 个 `[[wikilinks]]`。
推荐最低配置：
- 1 个指向主题相关页面
- 1 个指向导航页，如 `[[index]]` 或 `[[log]]`

适合链接到：
- 上位概念
- 相邻概念
- 被引用的方法页
- 导航页

避免：
- 孤立页面没有关联
- 链接堆砌但没有语义关系

## Directory-specific rules
### `concepts/`
适合：架构、方法论、原理说明、边界规范

写法重点：先定义，再拆结构，再给规则。

### `entities/`
适合：产品、项目、组织、模型、人物

写法重点：它是什么、关键事实、与其他实体/概念的关系。

### `comparisons/`
适合：横向比较、方案对比、决策分析

写法重点：比较对象、比较维度、结论与取舍。

### `queries/`
适合：值得长期保存的问题与答案

写法重点：问题本身、结构化回答、为什么值得保存。

## What NOT to write
以下内容不应直接成为正式 wiki 页面：
- 原样复制聊天记录
- 没有整理的 raw 资料
- 一次性临时状态
- 没有长期价值的碎片信息
- 只有命令没有上下文的执行日志

## Update rules
更新页面时遵循：
- 保留原主题，不要越改越漂移
- `updated` 日期必须刷新
- 新增信息优先并入现有结构
- 页面超过约 200 行时考虑拆页
- 主题已经分叉时建立新页面并互链

## Quality checklist
落库前至少检查：
- 文件名规范
- frontmatter 完整
- tags 来自 `SCHEMA.md`
- 页面有 Summary
- 至少有 2 个 wikilinks
- 页面可在 30 秒内扫描理解
- 内容确实有长期复用价值

## Anti-patterns
- 把 wiki 写成日记
- 把 wiki 写成 raw 仓库镜像
- 只写标题，不写摘要
- 没有 Related，导致知识孤岛
- 一个页面塞成超长杂烩
- 用临时会话结论直接覆盖长期知识

## Minimal template
最小模板只需保留：frontmatter、`# 标题`、`## Summary`、主体内容、`## Related`。

## Relationship to other rules
这页定义“怎么写页面”，不是“信息该放哪里”。
- 内容归类边界见 `[[hermes-memory-skills-wiki-boundaries]]`
- 检索与回答顺序见 `[[hermes-retrieval-priority-and-answer-path]]`
- 入库流程见 `[[wiki-ingestion-workflow]]`
- 整体架构见 `[[hermes-knowledge-architecture]]`
- 健康检查规范见 `[[hermes-wiki-lint-and-health-check-standards]]`

## Related
- [[hermes-knowledge-architecture]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[hermes-wiki-lint-and-health-check-standards]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
