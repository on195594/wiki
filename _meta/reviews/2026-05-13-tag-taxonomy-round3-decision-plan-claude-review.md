数据核实完成。现在撰写完整的审阅报告。

`★ Insight ─────────────────────────────────────`
审计脚本将 undeclared instance count 定义为所有未声明 tag 的总出现次数，而非唯一 tag 数。所以 `lifeos`（9 页）+ `harness`（4 页）= 13 次 instance 减少，从 91 降到 78，与计划预期吻合。
`─────────────────────────────────────────────────`

---

## Review: Wiki Tag Taxonomy Round 3 Decision Plan

**Verdict: PASS_WITH_NOTES**

计划整体判断正确、执行范围足够窄、无阻塞问题。以下细分发现。

---

### 阻塞问题

无。

---

### 重要发现

**F1 — `gstack` 主概念页仍是 draft，计划未明确引用此事实作为延迟理由**

`concepts/gstack-project-execution-lane.md` 的 `status: draft`。这是比"可能只是 project-specific marker"更硬的延迟理由：核心概念页尚未稳定，向 taxonomy 提升前应先等概念页 stable。计划的措辞（"may be a local identifier"）描述的是不确定性，但 draft 状态是可直接观察到的事实。建议在 Decision C 的 Reason 里补一句。

**F2 — `project-kickoff` 是另一个未声明 tag，计划未提及**

`queries/gstack-project-execution-lane-validation-case.md` 的 tags 包含 `project-kickoff`（复合词，与 `kickoff` 不同）。该 tag 在所有页面中只出现 1 次，不满足 3+ 阈值，无需本轮处理——但如果后续单独清理 `kickoff`，这个复合 tag 应一并处理。计划的 kickoff 分析部分未提到它存在，是一个遗漏。建议在 Decision D 里加一行 note。

---

### 次要发现

**F3 — `harness` 查询页中 2/3 是 draft**

`hermes-harness-profile-validation-detailed-plan.md` 和 `hermes-system-model-specific-harness-optimization-plan.md` 是 `status: draft`；只有 `final-closeout` 是 stable。概念页本身是 stable，且 4 页的 tag 使用是真实的（非生成草稿），taxonomy 决策不受影响，但计划描述 harness 时没有区分这一点，精确性稍欠。

**F4 — 验证命令 `git diff --check` 检查的是空格错误，而非内容变更**

计划 § 4 步骤 5 里的 `git diff --check` 不会显示 SCHEMA.md 的内容 diff。如果验证目标是确认只改了 SCHEMA.md 和 log.md，更准确的命令是 `git diff --stat` 或 `git diff SCHEMA.md`。这不影响功能，但 `--check` 的意图可能被误解。

**F5 — `lifeos` 加入 taxonomy 后，`gstack-project-execution-lane.md` 的 undeclared tag 计数会变化**

该页同时有 `gstack` 和 `lifeos` 两个当前未声明 tag。执行后 `lifeos` 变为已声明，`gstack` 仍未声明。这在预期 delta 计算里已正确隐含（9 lifeos 实例全部计入），无需修改计划，只是提醒执行时不会引发意外。

---

### 各 tag 判断验证

| Tag | 计划判断 | 实际核实 | 一致？ |
|-----|---------|---------|--------|
| `lifeos` | stable domain，9 页，中央概览页存在 | 全部 9 页确认，`lifeos-overview.md` status: stable，type: concept | ✓ |
| `kickoff` | generated draft，不加 taxonomy | 全部 8 页 status: draft，sources 均为虚构 `generated-from-project-intake` | ✓ |
| `gstack` | project-specific uncertain，延迟 | 4 页确认，主概念页 status: draft（比计划措辞更强的延迟依据） | ✓，但理由不完整 |
| `harness` | stable agent/runtime facet，4 页 | 4 页确认，概念页 stable，closeout 页 stable | ✓ |

---

### 执行范围评估

计划只改 `SCHEMA.md`（新增 2 行）和 `log.md`，不触碰任何页面 frontmatter。范围足够窄，符合"语义决策轮"的定位。预期 delta（undeclared unique 61→59，instances 91→78）计算无误。

---

### 建议计划修订

1. **Decision C Reason 中补充**：`concepts/gstack-project-execution-lane.md` 当前 `status: draft`，概念页未稳定前不宜提升为 taxonomy tag。
2. **Decision D 末尾补一行 note**：`queries/gstack-project-execution-lane-validation-case.md` 同时携带 `project-kickoff` 复合 tag（count=1），不满足阈值，但若日后清理 kickoff，需一并处理。
3. **验证命令 `git diff --check` 改为 `git diff --stat`**（可选，不阻塞执行）。
