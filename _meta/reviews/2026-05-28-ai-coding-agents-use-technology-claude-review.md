`★ Insight ─────────────────────────────────────`
The `docs:` prefix in `sources:` for raw articles turns out to be a consistent two-article pattern (used also in `towardsdatascience-hybrid-ai-...`), and local absolute paths in body text are used by 5+ prior raw articles. Both look like deviations but are actually established conventions in this wiki.
`─────────────────────────────────────────────────`

以下是按要求格式输出的审查结果：

---

## 审查结果

### 1. 裁定

**PASS_WITH_MINOR_FIXES**

---

### 2. 阻断性发现

无。

---

### 3. 重要发现

无。

---

### 4. 次要发现

- **英文 section header 与页面语言不一致**
  `concepts/agent-context-engineering.md` 新增节标题 `#### AX cascade addendum: visible is not usable` 使用英文，而该页所有其他节标题（`### 1.`, `### 2.` 等内正文）均为中文。建议改为 `#### AX 级联补充：已安装 ≠ 可用` 或同等中文标题，保持风格统一。

- **raw article 缺少 `source_type:` 字段**
  新 raw 文件使用 `type: raw-source` + `sources: [docs:https://...]` 而未设 `source_type:`（如 `article`）。该字段在多篇旧 raw 文章中出现（`analyticsvidhya`、`ahrefs` 等）。健康检查不强制此字段，但偏离多数 raw article schema。次要，可选补充。

- **关系文章中 `[[agent-context-engineering]]` wikilink 是新加，而 `[[ai-coding-assistant-context-budget-management]]` 的 Related 里回链是在本次提交中添加的，两者正确互指——无遗漏**（此条为确认，非问题）。

---

### 5. 最小持久单元是否被保留

**是。** 本次变更严格围绕用户确认的持久单元：「工具安装/注册不等于 AI coding agent 能使用它，实际可用性取决于 harness 上下文装配、语义工具选择、过时高置信模型回退风险、低噪声工具返回、以及 CLI/LSP/test 反馈自修复」。

- 未新建独立概念页（避免过度提升）；
- 三个概念页各自只增加了一段（12行、2行、2行）聚焦补充，没有复制原文段落；
- raw 文章完整保留原文供追溯，不混入演绎推论；
- 没有把「AX 信息级联」独立提升为新 concept 页，选择在已有最近页上附加，符合"更新现有页优于新建"的原则。

---

### 6. 活跃层边界检查

**通过。** 本次提交内容：

| 检查项 | 结论 |
|--------|------|
| memory 推广 | ✗ 无 |
| skill / cron 推广 | ✗ 无 |
| MCP / runtime 配置变更 | ✗ 无 |
| wrapper / gateway 变更 | ✗ 无 |
| Hermes 核心逻辑变更 | ✗ 无 |

所有变更均止步于 wiki concept page 层，Hermes 映射说明（"评估 skill/tool/MCP 不应只看…"）是认知层原则描述，不触发任何配置或运行时改动。

---

### 7. 具体补丁建议

仅针对次要发现 #1（英文 section header）：

**文件：** `concepts/agent-context-engineering.md`

**当前：**
```
#### AX cascade addendum: visible is not usable
```

**建议改为：**
```
#### AX 级联补充：可见不等于可用
```

其余次要发现（`source_type:` 缺失）无需改动，健康检查已通过，字段非强制。

---

### 附：本地验证证据

- `wiki_health_check.py` 在提交态（不含提交后新增的两个 untracked review 文件）返回 P0=0, P1=0, P2=0；当前工作区 P1 仅为 `_meta/reviews/2026-05-28-ai-coding-agents-use-technology-claude-review.md` 空文件（系本次 review 流程的产物，不属提交 80a1079 范围）。
- `git diff --check 80a1079^ 80a1079`：无输出，whitespace 检查通过。
