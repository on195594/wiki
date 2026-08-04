# Claude + Codex + Hermes Shared Wiki Index Rollout

## Goal
建立一个工具无关的共享索引，让 Claude Code、Codex 和 Hermes 在需要长期知识、既有决策或跨工具交接时，按需检索 `/home/lin/wiki`。

## Requirements
- R1：共享索引是唯一的跨工具 Wiki 路由入口，不复制 Wiki 正文。
- R2：Claude 与 Codex 的全局入口文件只增加短指针和触发条件。
- R3：Hermes 通过现有 `wiki_readonly` MCP 读取索引，并用一条短 memory 记录入口路径。
- R4：Wiki 默认只读；任何写入仍需用户明确要求，并遵守 `SCHEMA.md`、`index.md`、`log.md`。
- R5：项目事实优先读取项目内 `AGENTS.md`、`CLAUDE.md`、README、ADR 和源码，不用共享索引覆盖项目规则。

## Non-goals
- 不启用或修改 Memory Vault、Codex MCP、本地 LLM、cron、gateway、provider、profile/plugin。
- 不自动加载整个 Wiki，不新增后台同步或自动写回。
- 不移动现有 Claude/Codex/Hermes 记忆，也不复制动态任务状态。

## Targets
- `/home/lin/wiki/operations/agent-shared-wiki-index.md`
- `/home/lin/wiki/index.md`
- `/home/lin/wiki/log.md`
- `/home/lin/.claude/CLAUDE.md`
- `/home/lin/.codex/AGENTS.md`
- Hermes user-visible memory：一条共享索引路径事实。

## Acceptance
- A1：共享索引通过 Wiki health check、`git diff --check`，且至少有两个有效 wikilink。
- A2：Claude 与 Codex 入口包含完全相同的共享索引绝对路径，并明确“按需读取、不得全量预载”。
- A3：Hermes 注册的 `wiki_readonly` 工具能读取该页面并返回预期标题。
- A4：反向边界检查确认普通编码任务仍优先项目规则，不强制读取 Wiki。
- A5：未修改 Memory Vault、MCP 配置、Hermes config、cron、gateway 或本地模型。

## Rollback
- Claude/Codex：从 `/home/lin/.hermes/backups/agent-shared-wiki-index-20260804-114144/` 恢复。
- Wiki：恢复本次 diff，或删除新增页面并回退 `index.md`、`log.md`。
- Hermes memory：按完整文本移除本次新增条目。

## Stop conditions
若 Wiki 健康检查出现新 P0/P1、入口规则覆盖项目级约束、或 Hermes 注册工具无法读取索引，则停止并回滚对应变更。
