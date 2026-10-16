---
title: Inbox
created: 2026-04-16
updated: 2026-10-17
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
- 合格原始材料已保存到 `raw/`，或已引用现有规范/来源
- 已检索现有页面，避免重复建页
- 已创建或更新正式页面
- 已补充 wikilinks
- 已更新 `index.md`
- 已追加 `log.md`
- 已按 [[wiki-health-check-runbook]] 完成适用检查与修改段落回读。需要同步时，先核对 raw 新增、删除及其授权，再执行 `python3 _meta/scripts/wiki_maintain.py --fix`；该命令会写入 catalog 与 raw 哈希清单，并移除已不存在的 raw 文件对应的清单项，不能用同步掩盖误删。回读清单差异后，单独运行 `python3 _meta/scripts/wiki_maintain.py --check`；它只验证检查范围，不替代删除合理性和公开适宜性审查。
