---
title: Hermes Wiki Lint and Health Check Standards
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [hermes, knowledge-base, workflow, configuration, debugging]
sources: []
status: stable
---

# Hermes Wiki Lint and Health Check Standards

## Summary
Hermes wiki 的健康检查不是“看看文件还在不在”，而是持续验证知识库是否仍然可检索、可维护、可导航、可扩展。
lint 的目标是尽早发现知识孤岛、结构漂移、标签失控、索引失真和陈旧内容。

## Canonical goal
一次合格的 wiki lint / 健康检查，至少要回答这几个问题：
- 页面之间还能不能连起来
- 索引还能不能正确导航
- 页面结构是否仍符合规范
- 标签是否还受控
- 页面是否已经陈旧或过大
- 日志是否还能继续维护

## Lint scope
默认检查范围包括：
- `index.md`
- `log.md`
- `SCHEMA.md`
- `entities/`
- `concepts/`
- `comparisons/`
- `queries/`

通常不把 `raw/` 当作 lint 主对象，因为 raw 是来源层，不是正式知识层。

## Core checks
### 1. Broken wikilinks
检查 `[[wikilinks]]` 是否指向不存在的页面。

目标：
- 避免页面可读但不可跳转
- 防止知识网络断裂

### 2. Orphan pages
检查哪些正式页面没有任何 inbound links。

目标：
- 找出知识孤岛
- 避免页面存在但永远检索不到

说明：
- 新页面短期内可能是“暂时孤立”
- 但长期孤立页应被补链、合并或归档

### 3. Index completeness
检查所有正式页面是否都列在 `[[index]]` 中。

目标：
- 保证目录仍是有效导航入口
- 防止页面实际存在但索引缺失

### 4. Frontmatter validation
检查页面是否具备完整 frontmatter：
- `title`
- `created`
- `updated`
- `type`
- `tags`
- `sources`
- `status`

目标：
- 保持页面结构统一
- 保证后续筛选、治理和自动化处理可行

### 5. Tag audit
检查页面 tags 是否都来自 `SCHEMA.md` 的 taxonomy。

目标：
- 防止 tag 漫游
- 防止同义标签并存造成检索分裂

### 6. Page size check
检查页面是否过长，经验阈值约 200 行。

目标：
- 防止一个页面变成无法维护的大杂烩
- 发现应拆分为子页面的候选项

### 7. Staleness check
检查页面是否长时间未更新，且主题已被更晚资料覆盖。

目标：
- 发现看似存在、实则过期的知识
- 提醒进行增量维护，而不是继续引用旧结论

### 8. Contradiction check
检查相近主题页面之间是否存在互相冲突的结论。

目标：
- 防止知识库表面整齐、内部互相打架
- 要求显式记录冲突，而不是静默覆盖

### 9. Log health
检查 `[[log]]` 是否持续追加、是否过长、是否需要轮转。

目标：
- 保持维护历史可追踪
- 防止日志无限增长后失去可读性

### 10. Schema drift
检查页面实际写法是否偏离 `SCHEMA.md` 与 `[[hermes-wiki-page-writing-standards]]`。

目标：
- 防止规范写在文档里，但页面实际早已失控

## Severity levels
建议把 lint 结果按严重性分级：

### P0
必须立即修：
- broken wikilinks
- 丢失 index 主入口
- frontmatter 严重缺失

### P1
应尽快修：
- orphan pages
- tag taxonomy 失控
- 明显结构漂移
- 重要页面陈旧

### P2
常规维护：
- 页面过长
- 日志接近轮转阈值
- 页面可读性一般但仍可用

## Recommended lint workflow
1. 先读 `SCHEMA.md`
2. 读 `[[index]]`
3. 读最近的 `[[log]]`
4. 扫描所有正式知识页
5. 输出 broken links / orphan / missing index / frontmatter / tag / stale / size / contradictions
6. 按严重性排序
7. 明确给出每项对应文件路径
8. 若允许修复，再按优先级修
9. 记录 lint 结果到 `[[log]]`

## Health check frequency
建议频率：
- 日常增量维护后：轻量 lint
- 每新增一批页面后：结构 lint
- 每周或每月：全量健康检查
- 在大规模重构前后：完整 lint + 对比

## Pass criteria
一个健康的 Hermes wiki，至少应满足：
- 没有 broken wikilinks
- 没有长期 orphan pages
- 所有正式页面都进入 `[[index]]`
- frontmatter 完整
- tags 受控
- 页面可扫描
- 日志持续可追踪

## Anti-patterns
- 只看文件存在就算健康
- 只检查链接，不检查结构和标签
- lint 结果不写回 `[[log]]`
- 发现问题但长期不处理
- 每次都全量大修，缺少日常轻量维护

## Output format
一份好的 lint 报告至少包含：
- 检查范围
- 问题统计
- 按严重性分组的问题列表
- 每个问题的具体文件路径
- 建议动作
- 是否需要立即修复

## Relationship to other rules
这页定义“怎么检查 wiki 是否健康”。
- 页面怎么写，见 `[[hermes-wiki-page-writing-standards]]`
- 内容怎么入库，见 `[[wiki-ingestion-workflow]]`
- 回答时怎么检索，见 `[[hermes-retrieval-priority-and-answer-path]]`
- 整体架构，见 `[[hermes-knowledge-architecture]]`

## Related
- [[hermes-knowledge-architecture]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[hermes-wiki-page-writing-standards]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
