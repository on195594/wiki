# AGY 独立审查报告：OpenWiki 知识新鲜度沉淀与 Wiki 改造计划

日期：2026-08-26
审查范围：
- `raw/articles/langchain-self-correcting-memory-openwiki-2026-08-26.md`
- `concepts/hermes-knowledge-freshness-and-claim-evidence.md`
- `queries/hermes-wiki-knowledge-freshness-improvement-plan.md`
- `index.md`
- `log.md`

## 总体裁决

**PASS_WITH_NOTES**

AGY 明确建议批准阶段 0–1 的 Wiki-only 试点。当前沉淀准确区分 Wiki promotion、Wiki-only 优化和 active workflow/runtime adoption，没有把 OpenWiki 的外部实践、OKF 元数据或实验指标升级为 Hermes 默认规范。

## Findings

### Blocking

无。

### Important

无。

### Minor

1. `index.md` 头部索引计数需要从 113 更新为 115，因为本次新增了一个 concept 页面和一个 query 计划页。
2. 新 raw source 需要加入 `_meta/raw-source-hashes.json`。
3. 计划页 `## Relations` 中的 `related` 不是当前 schema 的标准关系谓词，应移到 `## Related` 或改用标准谓词。

### Recommended

1. 概念页的中文 `## 关系` 建议统一为 `## Related`，与 `## Relations` 的结构化关系区分。
2. 阶段 2 应明确是 Just-in-Time / 按需触发，避免被误读为常驻 watcher 或自动化扫描。

## 试点结论

建议批准阶段 0–1：先选择 3–5 个高复用、易变化页面，在 Markdown 正文中补充断言、证据、推论和复核语义；不修改强制 schema，不引入数据库、sidecar、cron、runtime 或 active skill。阶段 2–3 继续保留真实证据和独立授权门槛。

## 审查边界与验证

审查为只读，未执行写入、删除、提交或 active Hermes surface 变更。AGY 报告：`git diff --check` 通过；Wiki health check `P0=0, P1=0, P2=1`，唯一 P2 是新 raw source 尚未加入 hash 清单。
