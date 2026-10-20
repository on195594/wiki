---
title: Inbox
created: 2026-04-16
updated: 2026-10-19
type: meta
status: current
---

# Inbox

只有已获保存授权且适合公开的待处理材料才记在这里；私有任务、会话和个人材料留在原载体。入库规则见 [[wiki-ingestion-workflow]]。

## 待入库
- [ ] 粘贴一个链接，存入 `raw/articles/`
- [ ] 上传一个 PDF，存入 `raw/papers/`
- [ ] 记录一个值得长期保存的问题，整理到 `queries/`

## 入库检查清单
- 写入授权与公开准入已确认（先于 Inbox 和 raw 保存）
- 合格原始材料已保存到 `raw/`（不覆盖已有快照），或已引用现有公开规范/来源
- 已用 `wiki_reverse_lookup.py --source` 与窄词检索现有页面，按 `NEW / CONFIRM / UPDATE / CONFLICT / SUPERSEDE` 优先并入现有 owner，避免重复建页
- 已创建或更新正式页面：含一句话 `description`，`aliases` 无自身文件名（slug）重复或已登记标签冲突，局部 `[!volatile]` block 的 `source` 已同步列入页面 `sources`
- 已补充可点击 `[[wikilinks]]`（正式页链接不用反引号包裹）与规范 `## Relations`（同类关系键单行逗号分隔、省略空 `[]` 占位、`depends_on` / `refines` 仅指向正式页）
- 已更新 `index.md`（使用标准相对 Markdown 链接、同步 `Indexed pages` 计数；`draft` 标草稿，`closed` 历史计划可退出主索引）
- 已在 `log.md` 顶部按日期倒序追加本次公共仓库的 durable delta、证据边界与验证结果
- 已按 [[wiki-health-check-runbook]] 完成适用检查与修改段落回读。需要同步时，先核对 raw 新增、删除及其授权，再执行 `python3 _meta/scripts/wiki_maintain.py --fix`；该命令会写入 `_meta/catalog.json` 与 `_meta/raw-source-hashes.json`，并移除已不存在的 raw 文件对应的清单项，不能用同步掩盖误删。回读清单差异后，单独运行 `python3 _meta/scripts/wiki_maintain.py --check`（或 `wiki_check`）；它只验证检查范围，不替代删除合理性和公开适宜性审查。
