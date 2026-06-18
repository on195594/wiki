---
title: OKF Concepts for Hermes Wiki Governance Assessment
created: 2026-06-18
updated: 2026-06-18
type: query
tags: [hermes, knowledge-base, governance, context-engineering]
sources: [docs:https://www.marktechpost.com/2026/06/16/google-cloud-introduces-open-knowledge-format-okf-a-vendor-neutral-markdown-spec-for-giving-ai-agents-curated-context/, docs:hermes-llm-wiki, docs:hermes-skills, docs:hermes-memory]
status: stable
description: 评估 OKF/LLM-wiki 思路如何作为 Hermes wiki 的机器可读治理增强，而不是替代现有 wiki 架构。
aliases: [okf, open-knowledge-format, knowledge-object, llm-wiki]
---

# OKF Concepts for Hermes Wiki Governance Assessment

## Summary
OKF 对 Hermes wiki 有用，但只应作为机器可读治理增强参考，不应替代当前 `~/wiki` 的 LLM-wiki 三层结构。当前优先落地的是可选 `description`、保守 `aliases`、可读 `## Relations`、只读 validator 和小范围试点；不做全库迁移、不新增图数据库、不触碰 active skill/runtime/memory。

## Decision
采纳“知识对象增强”而不是“迁移到 OKF”：

- Hermes wiki 的 canonical 架构仍是 [[hermes-knowledge-architecture]] 定义的 raw / compiled wiki / schema 分层。
- OKF 只提供设计参考：Markdown 文件、YAML metadata、文件链接图谱、Agent 可消费上下文。
- 本地命名采用“知识对象增强”或“Agent-readable knowledge object convention”，不把 OKF 作为本地规范名。

## Adopt now

### Optional `description`
用于 Agent 路由和页面预览，适合新页面和高价值治理页。

边界：不能替代 `## Summary`，也不能作为事实来源。

### Conservative `aliases`
仅用于明显同义词和高频缩写，例如 `OKF` / `Open Knowledge Format`。

边界：不能替代 canonical 文件名、tag taxonomy 或 index 导航。

### `## Relations`
用于表达页面之间的语义关系：

```markdown
## Relations

- refines: [[hermes-knowledge-architecture]]
- depends_on: [[hermes-wiki-page-writing-standards]]
- conflicts_with: []
- supersedes: []
```

边界：`Relations` 是推理/维护关系；证据仍写入 `sources`。

### Read-only validation first
先扩展只读健康检查，再决定是否把新约定变成强规则。

首批检查重点：
- `Relations` 中的 wikilinks 是否可解析；
- `description` 是否短且具体；
- `aliases` 是否与 tags 或文件命名冲突；
- context pack 引用是否存在；
- `sources` 是否可复验。

## Defer or reject

### Defer `resource`
暂不默认新增 `resource` 字段。当前页面身份已经由相对路径承担，证据由 `sources` 承担。只有在 validator 和检索层证明具体价值后，再考虑兼容映射。

### Defer full `aliases` rollout
不批量补旧页面。只在新页面或高频页面使用。

### Reject full migration
不把 85+ 现有页面一次性迁移到 OKF 风格；这会制造大量无意义 diff、审计噪声和回滚压力。

### Reject external graph/runtime dependencies
不引入图数据库、外部向量库或专有 catalog。官方 LLM-wiki 文档强调 Markdown-first、无数据库、无特殊 runtime。

## Pilot scope

首批只试点 5 个治理核心页：

1. [[hermes-knowledge-architecture]]
2. [[wiki-ingestion-workflow]]
3. [[hermes-wiki-page-writing-standards]]
4. [[hermes-wiki-lint-and-health-check-standards]]
5. [[hermes-memory-skills-wiki-boundaries]]

试点只允许小步更新：补 `description` / 少量 `aliases` / `## Relations`。每次修改后运行健康检查并更新 [[log]]。

## Governance risks

### Naming drift
不要并行使用 OKF、LLM-wiki、Knowledge Object、Hermes object 多套名字。对外统一称为“知识对象增强”。

### Source vs inference mixing
`sources` 表示证据来源；`Relations` 表示页面关系。不能把推断关系当成事实来源。

### Active-layer bleed
该方案只属于 wiki/schema/validator 层。不得因此修改 memory、active skills、cron、MCP、runtime、wrapper 或 gateway。

### Migration pressure
不承诺自动补齐旧页。只有页面被真实任务触达，才增量补充可选 metadata。

## Relations

- refines: [[hermes-knowledge-architecture]]
- depends_on: [[hermes-wiki-page-writing-standards]]
- depends_on: [[hermes-wiki-lint-and-health-check-standards]]
- depends_on: [[hermes-memory-skills-wiki-boundaries]]

## Related
- [[agent-context-engineering]]
- [[progressive-knowledge-system-growth]]
- [[hermes-knowledge-architecture]]
- [[hermes-wiki-page-writing-standards]]
- [[hermes-wiki-lint-and-health-check-standards]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[index]]
- [[log]]
