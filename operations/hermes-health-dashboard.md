---
title: Hermes Health Dashboard
created: 2026-04-22
updated: 2026-09-16
type: operation
tags: [hermes, governance, validation, cron, monitoring]
sources: [concepts/hermes-memory-governance-notes.md, skill:hermes-runtime-operations, docs:https://hermes-agent.nousresearch.com/docs/user-guide/security, docs:https://hermes-agent.nousresearch.com/docs/user-guide/configuration, filesystem:/home/lin/.hermes/config.yaml, filesystem:/home/lin/.hermes/state.db, project:/home/lin/.hermes/hermes-agent]
status: active
description: Hermes 周度治理线的当前运行基线、风险跟踪与运维检查入口。
aliases: [health-dashboard]
volatility: high
verified_at: 2026-09-16
review_by: 2026-09-23
---

# Hermes Health Dashboard

## Summary
这页记录 Hermes 周度治理线的当前运行基线。版本、服务、依赖、Cron 和数据库状态变化快；到期后或执行运维动作前，以实时命令和当前项目文件重新核验，不把本页当成执行授权。

## Current baseline

### Runtime
- Hermes：`v0.21.3 [fb56a7e0] (2026-09-16)`，检查时与上游同步。
- Python：`3.11.15`。
- Gateway：systemd user service `active/running`，`Result=success`，`NRestarts=0`。
- 平台：Telegram；6/6 Cron active。
- Terminal：`local`，默认工作目录仍在 `~/.hermes`；这是尚未处理的生产隔离风险。

### Cron
- `晨报`：`0 7 * * *`，最近一次 `ok`。
- `hermes-weekly-health-check`：`30 8 * * 1`，最近一次 `ok`；skill 为 `hermes-runtime-operations`。
- `weekly-knowledge-review`：`0 9 * * 6`，最近一次 `ok`。
- `华东医药000963低于27.8预警`：每 5 分钟，最近一次 `ok`。
- `a-stock-stage1-final-2026-09-20`：实际调度为 `2026-09-21 18:30`；名称与日期意图仍需人工核对。
- `amazon-price-watch-daily`：Playwright Chromium 1217 已补齐，本地 smoke 通过。首次手工触发的应用 run 对 10/10 商品返回 `source_status=ok`，但触发命令 owner 超时使该 execution 标为 `unknown`；随后重新完整触发，Cron execution `completed`、job `Last run: ok`，新 run 仍为 10/10 `source_status=ok` 且无重复价格提醒。下一次正常调度为 2026-09-17 09:30。

### Memory
- `MEMORY.md`：`1253/2200` chars。
- `USER.md`：从 `1350/1375` 压缩到 `843/1375` chars，约 61%；长期偏好语义保留，下一新 session 生效。

### Session store
- `state.db`：从 `1053.2 MB` 优化到 `655.9 MB`。
- 会话：从 1348 降到 835；消息：从 120715 降到 105217。
- 已在 gateway 离线并生成已校验 SQLite 快照后，删除 513 个 `session_key IS NULL`、超过 30 天的遗留 open Telegram session；未删除当前 keyed Telegram session。
- 当前 open：Telegram 5、recovered 4、cron 1；VACUUM 后 freelist 为 0。
- 恢复快照：`~/.hermes/state-snapshots/20260916_171753-legacy-open-cleanup/state.db`。

### Browser
- Playwright `chromium-1217` 与 `chromium_headless_shell-1217` 已安装到 `~/.local/share/ms-playwright/`。
- 本地 Chromium 启动、页面渲染和 DOM 读取 smoke 通过。
- Amazon 真实抓取已证明缺失浏览器这一根因已消除；登录、强反爬和其他复杂站点仍需按站点验证。

### Backup and recovery
- `updates.pre_update_backup: quick` 已恢复为官方默认保护；自定义一致性大数据库快照继续保留。
- 每日双目标加密 restic backup 保持启用。
- 新增每月 `hermes-backup-verify.timer`；2026-09-16 已对 `jedi` 和 `wiki` 两个仓库执行 `restic check` 与必需路径核验，均通过。
- 新增季度 `hermes-restore-drill.timer`；2026-09-16 已从两个仓库分别恢复约 1.029 GiB 关键状态到隔离临时目录，恢复后的 `state.db` quick check 与配置解析均通过，临时目录已清理。

## Open risks

### High priority
- 主机隔离尚未处理：Hermes 仍使用 `terminal.backend: local`，运行用户属于 `docker` 组，且永久 `command_allowlist` 包含宽泛危险类别。
- SSH 仍允许 root/password 登录；主机 INPUT policy 为 ACCEPT，多个非 Hermes Docker 端口绑定 `0.0.0.0`。公网可达性仍需从外部及云安全组核验。
- `httpx2/httpcore2==2.7.0` 的安全审计仍有 12 条记录（3 条 HIGH package/advisory records）；上游 [#108219](https://github.com/NousResearch/hermes-agent/issues/108219) 仍为 OPEN。当前 MCP 为 stdio，未配置 HTTP streamable MCP；不要做脱离上游 lockfile 的强制升级。

### Maintenance
- `agent-browser` 仍有 1 high + 1 moderate npm advisory；web workspace 有 1 high + 5 moderate，TUI 有 2 moderate。等待受审查的上游 lockfile 更新，不盲跑 `npm audit fix`。
- 上游 gateway planned-stop 问题 [#42517](https://github.com/NousResearch/hermes-agent/issues/42517) 仍为 OPEN；本机安全更新脚本已改为通过 `hermes gateway stop` 写 planned-stop marker，实际维护停机返回 `ExecMainStatus=0`。
- 仍需观察 keyed open Telegram/recovered/cron 行是否继续增长。

## Weekly governance pipeline
- Skill：`hermes-runtime-operations`。
- Cron：`hermes-weekly-health-check`。
- Schedule：`30 8 * * 1`。
- Deliver：`origin`。
- Goal：生成短、面向决策、带实时证据的运行健康报告。

## Report contract
每周报告至少回答：
1. Hermes 是否落后于上游，gateway 是否稳定？
2. Cron 是否成功、仍有业务意义，是否存在名称/调度漂移？
3. Memory 和 session store 是否接近容量或异常增长？
4. Browser、备份与恢复演练是否通过？
5. 依赖安全与主机隔离风险是否变化，下一步是什么？

## Interpretation policy
- **Healthy**：更新无明显漂移；核心 Cron 最近成功；Memory 低于 80%；备份验证和最近一次恢复演练通过。
- **Degraded**：某项集成或账本待下一次定时闭环；存在受控、已知、未扩大的依赖风险。
- **Unhealthy**：核心投递失败；恢复演练失败；数据库完整性异常；gateway 重启循环；安全边界被扩大。

## Next actions
1. 观察 2026-09-17 09:30 Amazon 正常定时执行，确认定时调度在无人介入时继续保持 `ok`。
2. 核对 `a-stock-stage1-final-2026-09-20` 的实际目标日期。
3. 单独安排主机与 Hermes 执行隔离整改：container/SSH backend、专用工作目录、收紧 allowlist、SSH 与公开端口。
4. 跟踪上游 #108219、#42517 和 npm lockfile 修复；不采用未经兼容验证的强升。
5. 下周复查剩余 open session 数量以及 backup verify/restore timers。

## Relations

- depends_on: [[hermes-memory-governance-notes]], [[hermes-retrieval-priority-and-answer-path]]
- related: [[hermes-layer-routing-decision-checklist]], [[hermes-active-surface-lifecycle-governance]]

## Related
- [[index]]
- [[log]]
