你是独立 Wiki 摄取审查员。请只读审查 `/home/lin/wiki` 当前工作树；它已验证为干净，并对应提交 `6ea1d9488b2ef6d51bc5b0afd364679da781a049`（`wiki: ingest local-first sync architecture study`）。不要修改、创建、删除、暂存或提交任何文件，不要访问网络。

审查范围仅限：
- `/home/lin/wiki/_meta/raw-source-hashes.json`
- `/home/lin/wiki/concepts/local-first-sync-confirmed-mirror-outbox-conflict-policy.md`
- `/home/lin/wiki/index.md`
- `/home/lin/wiki/log.md`
- `/home/lin/wiki/raw/articles/reverse-linear-sync-engine-2026-09-06.md`
- 用于核对原文的冻结本地捕获：`/home/lin/.hermes/cache/browser-use/workspace/20260906_065300_2bedd7a1/reverse-linear-sync-engine-readme.txt`
- 如需规则，可只读 `/home/lin/wiki/SCHEMA.md`。

目标：独立判断该沉淀是否准确、克制、可检索、可复用，是否错误提升为 Hermes 默认规则。

必须逐项审查：
1. 来源保真与 provenance：raw 页面声明为 substantially complete；明确源文本 89,897 字符/1,449 行、保存正文 89,620 字符/1,441 行；省略 8 行 `Important / Check out the SUMMARY` callout；清理一个尾随空格；图片和链接目标未嵌入。请核对这些声明与冻结捕获及正文是否一致。
2. 概念页中的来源事实是否能由 raw 正文支持。
3. 来源事实、作者推导、可迁移 `[推论]`、Hermes `[建议]` 与不采用边界是否明确分离。
4. 是否误把 LWW、不需要 CRDT、全局游标、Linear 内部类名/字段/端点/阈值升级为通用规范。
5. durable unit、所有权、frontmatter、Relations、wikilinks、index、log、raw hash manifest 是否一致。
6. 是否引入 active Skill、Memory、runtime/config、Cron、MCP、Gateway、插件或生产行为的推广。
7. 安全边界：不得保留 API keys、tokens、passwords、secrets、credentials 或 connection strings；如出现应为 `[REDACTED]`。

只报告能够以当前文件精确行号证明的问题。不要把风格偏好当缺陷；不要要求新框架、新 Skill 或运行时改动。严重性限定为 `BLOCKER`、`MAJOR`、`MINOR`。若没有需要修复的问题，findings 必须为空。

严格输出 JSON，不要 Markdown 围栏：
{
  "verdict": "APPROVE_LANDING | PASS_WITH_MINOR_FIXES | REQUEST_CHANGES",
  "reviewed_commit": "6ea1d9488b2ef6d51bc5b0afd364679da781a049",
  "findings": [
    {
      "severity": "BLOCKER | MAJOR | MINOR",
      "criterion": "...",
      "location": "文件:行号",
      "finding": "...",
      "evidence": "...",
      "minimal_remediation": "..."
    }
  ],
  "passes": [
    {"criterion": "...", "evidence": "文件:行号"}
  ],
  "summary": "..."
}

完成充分取证后立即返回，不要继续扩展范围。