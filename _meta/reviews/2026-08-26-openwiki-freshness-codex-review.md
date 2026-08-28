# Codex 可实施性与目标一致性审查

日期：2026-08-26
审查对象：`queries/hermes-wiki-knowledge-freshness-improvement-plan.md` 及相关 Wiki 页面
审查模式：只读

## Verdict

**BLOCK**

计划方向正确，已明确排除 claims sidecar、状态机、watcher、全库迁移和独立试点。但当前不宜直接作为“立即生效”的写作约定，因为相关页面和日志尚未完全收敛到同一规则。

## 最强反对意见

计划声称立即生效，但最终规则只存在于 query 计划页；概念页、索引、历史日志和 canonical 写作规范仍有旧的 stale/verified/试点表述。不同 Agent 可能据不同入口执行相反规则。另一个实质问题是“发现过时即修正”可能被误读为写入授权，且没有明确复用既有 Wiki 写入闭环。

## Blocking findings

### B1：规则面存在互相冲突的旧内容

- 涉及：计划页、`concepts/hermes-knowledge-freshness-and-claim-evidence.md`、`index.md`、`log.md`、`concepts/hermes-wiki-page-writing-standards.md`。
- 失败机制：计划页拒绝新状态机，但概念页仍介绍 `verified/stale/unverified/inferred`；索引仍突出 stale；日志同时保留旧试点和新直接采用记录；canonical 写作规范尚未承载最终规则。
- 最小修正：将最终采用的简短规则写入现有 `hermes-wiki-page-writing-standards.md`；概念页明确四态是 OpenWiki 原机制而非 Hermes 采用，或删除本地采用建议；同步索引描述；历史日志不重写，只追加 supersede 说明；计划完成后可改为 `closed` 决策记录。

### B2：维护责任可能越过默认只读边界

- 涉及：计划页“发现内容可能过时时”“维护责任”。
- 失败机制：Agent 可能把“直接修改/删除/修正文段”理解为已有 Wiki 写入授权，或只改正文而漏掉 index、log、health check、diff 等现有收口步骤。
- 最小修正：加入明确规则：只有当前任务明确授权 Wiki 写入时才修正；否则只报告页面、段落和证据。所有写入继续遵守 index/log/health-check/diff 闭环；独立审查仍按既有高风险条件触发。

## Important findings

1. “重要结论”“尽量具体来源”等表述仍偏模糊。无需新语法，但应明确：数字、当前外部行为、规范性规则、争议结论和多来源综合，必须在同段或相邻句放具体 Wiki/raw 链接。
2. `updated` 只代表文件最近编辑时间，不能暗示整页已复核。局部修正应保留依据、截至日期和复核范围。
3. `review_by` 应严格复用 SCHEMA 现有适用条件：外部厂商控制的产品行为、接口或命令集；不要扩展到仅提及工具的方法论页。
4. 当前 raw 文件是结构化摘要而非完整文章快照，`Source quality: full` 可能过度表述，应改为结构化摘要或补充真正完整的不可变快照。

## Minor finding

计划页缺少 `## Summary`，应补充以符合页面写作规范。

## 是否会重新变成验证项目

Codex 明确认为不需要重新建立试点或独立验证项目。完成上述两处文档一致性修正后即可直接采用。

## 只读证据

Codex 检查了共享 Wiki 入口、计划、概念页、raw、SCHEMA、写作规范、知识对象治理收束页和 health check。health check 为 `P0=0, P1=0, P2=0`，`git diff --check` 通过；但这些检查不能发现语义冲突、Summary 缺失或写入授权歧义。
