目录权限受限，直接写入文件。

```markdown
# Claude Review — Wiki governance cleanup plan

## Verdict

APPROVE_WITH_CHANGES

## Inspected files and commands

Files read (read-only, no shell commands executed):

- `/home/lin/wiki/_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`
- `/home/lin/wiki/SCHEMA.md`
- `/home/lin/wiki/index.md`
- `/home/lin/wiki/_meta/scripts/wiki_health_check.py`
- `/home/lin/wiki/_meta/scripts/wiki_tag_audit.py`
- `/home/lin/wiki/operations/hermes-health-dashboard.md` (operations/ directory representative)
- `/home/lin/wiki/queries/hermes-harness-profile-validation-detailed-plan.md` (Lane C top candidate, first 40 lines)
- `/home/lin/wiki/queries/hermes-harness-profile-validation-final-closeout.md` (related closeout, first 15 lines)
- `/home/lin/wiki/concepts/hermes-lifeos-executable-architecture.md` (Lane C candidate, first 20 lines)
- `/home/lin/wiki/concepts/hermes-skill-refactoring-methodology.md` (first 15 lines — /tmp source verification)

Grep patterns used (read-only):

- `^status:` across all `.md` — to enumerate all non-schema status values in use
- `^type:` in `queries/` — to verify type mixing claim
- `^sources: \[\/tmp` — to locate /tmp source instances
- `^source_policy:` across all `.md` — to confirm no existing uses

No shell commands were executed.

---

## Blocking findings

None.

---

## Important findings

### IMP-1

**Severity:** important

**Evidence:** `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md` § 5 (Lane A), "Proposed schema decisions to review" item 3; corpus grep on `status:`.

**Problem:** The proposed `status` expansion (`draft | stable | active | closed | current` + `raw | captured`) is incomplete. Five additional non-schema status values are currently in live use and are not addressed:

| Value | File(s) | Directory |
|---|---|---|
| `current-as-of-2026-05-11` | `queries/hermes-agent-experience-consolidation-capability-assessment.md` | queries/ (formal) |
| `complete` | `_meta/reviews/2026-05-17-ai-agent-document-fidelity-risk-claude-review.md` | _meta/ |
| `completed` | `_meta/wiki-health-check-automation-plan.md` | _meta/ |
| `raw-source` | `raw/articles/makeuseof-obsidian-perfect-vault-one-thing-2026-05-08.md` | raw/ |
| `current` | `_meta/wiki-health-check-runbook.md`, `_meta/draft-query-inventory.md` | _meta/ |

Of these, `current-as-of-2026-05-11` is a formal `queries/` page with a date-embedded status value that doesn't fit any proposed slot. If Lane A only normalizes the listed values, the audit command `grep -r "^status:" wiki/` will still surface unlisted values on first run. The plan would benefit from either explicitly accepting these as "out-of-scope for Lane A" or adding a deferred table.

**Recommended patch:** In § 5, after the suggested status value table, add a paragraph:

> **Unaddressed values (deferred to a later pass):** `current-as-of-<date>` (treat as `draft` + a dated note, or accept as informal historical status), `complete`/`completed` (`_meta/` only — defer or map to `closed`), `raw-source` (alias to `raw`). Do not change these pages in Lane A; record them here for the next schema round.

---

### IMP-2

**Severity:** important

**Evidence:** `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md` § 5, "Proposed schema decisions to review" item 2 (queries/ compatibility policy); corpus grep on `^type:` in `queries/`.

**Problem:** All 25 `queries/` pages currently use `type: query`. The plan correctly recommends the compatibility policy ("retain historical pages, discourage future mixing"). However, the implementation instruction reads "Decide allowed `type` values and directory semantics." Without a clear prohibition, a future executor could interpret Lane A as authorizing a bulk reclassification of existing `queries/` pages from `type: query` to `type: plan`, `type: closeout`, etc. This would contradict both the "avoid mass migration now" principle and the "Minimum landing change" constraint (schema doc only).

The stop condition "Stop if plan proposes mass migration without separate approval" applies here, but it's placed in the issue matrix (§ 4), not in the Lane A execution section (§ 5). A reader following only the lane section could miss it.

**Recommended patch:** In § 5, "Minimum landing change" block, append:

> Lane A does **not** authorize changing the `type` field of existing `queries/` pages. The `type` enum expansion is a schema-documentation change only. Re-classifying existing pages requires a separate approved migration plan.

---

### IMP-3

**Severity:** important

**Evidence:** `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md` § 5 item 5 (`source_policy: normative`); `_meta/scripts/wiki_health_check.py` (full); `_meta/scripts/wiki_tag_audit.py` (full).

**Problem:** The plan proposes adding `source_policy: normative` as a new frontmatter field. Neither `wiki_health_check.py` nor `wiki_tag_audit.py` validates this field. Once added to `SCHEMA.md`, there is no automated enforcement: pages could silently use `source_policy: normative` incorrectly (e.g., a non-governance page claiming normativity to dodge the sources-policy lint), and there is no command in the Lane A verification block that would catch this.

This is not blocking because the plan is documentation-only and the field is voluntary. But the plan should acknowledge the gap so future tooling work knows to add a lint rule.

**Recommended patch:** In § 5, after item 5 (`source_policy: normative`), add a note:

> Note: `source_policy: normative` has no automated enforcement in the current scripts. A future lint rule should flag any page with `source_policy: normative` that is not under `_meta/`, `SCHEMA.md`, `index.md`, or `log.md`. Do not rely on this field for security gating without that lint.

---

## Minor findings

### MIN-1

**Severity:** minor

**Evidence:** `SCHEMA.md` § "Directory Roles"; `_meta/plans/` and `_meta/reviews/` directories referenced throughout the plan.

**Problem:** `SCHEMA.md`'s Directory Roles section lists only `_meta/` as a single entry ("导航与维护文档"). In practice the wiki now uses `_meta/plans/`, `_meta/reviews/`, and `_meta/scripts/` as distinct subdirectories with distinct purposes. The plan proposes adding `operations/` but does not note these three `_meta/` subdirectories. If Lane A updates Directory Roles, this omission leaves the schema still partially incomplete.

**Recommended patch:** In § 5 "Expected files" (Lane A), add a note: "Optionally document `_meta/plans/`, `_meta/reviews/`, and `_meta/scripts/` as recognized subdirectories in SCHEMA.md Directory Roles at the same time."

---

### MIN-2

**Severity:** minor

**Evidence:** `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md` § 6, Lane B verification block.

**Problem:** The verification note says "duplicate tag files remain zero **if a duplicate detector is available**." The detector already exists: `wiki_tag_audit.py` outputs a `duplicate_tag_files` array in JSON mode. The conditional phrasing implies it might not be present and could lead a future implementer to skip the check.

**Recommended patch:** Replace "if a duplicate detector is available" with "confirmed via `wiki_tag_audit.py --format json` `.duplicate_tag_files[]`".

---

### MIN-3

**Severity:** minor

**Evidence:** `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md` § 8, bash command block.

**Problem:** The `git diff --check` and `git diff --stat` lines in the verification block inside Section 8 have a leading space, making them not copy-paste safe as a single shell script.

**Recommended patch:** Remove the leading space from ` git diff --check` and ` git diff --stat` in the Section 8 code block.

---

### MIN-4

**Severity:** minor

**Evidence:** `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md` § 4, issue matrix, row 1 ("SCHEMA.md omits operations/"), stop condition column.

**Problem:** "Stop if defining `operations/` requires moving pages" is slightly misleading: adding `operations/` to SCHEMA.md does not require moving any pages — the directory and its one page already exist. The stop condition should be framed as "Stop if the `operations/` definition triggers a recommendation to re-home existing pages."

**Recommended patch:** Change stop condition text to: "Stop if adding `operations/` to SCHEMA.md leads to a proposal to move or rename existing pages in the same pass."

---

## Non-promotion statement

The reviewed plan **does not** authorize changes to any active Hermes layer. Section 3 ("Non-goals and forbidden actions") explicitly prohibits updating: Hermes memory, active skills, cron jobs, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, and Hermes core. Section 10 ("Rollback and stop conditions") repeats: "Stop immediately if any active Hermes layer would be touched without explicit dated approval." These protections are clear, explicit, and correctly scoped to all relevant layer types listed in the review prompt.

---

## Overall recommendation

The three-lane structure is sound and correctly sequenced. The plan is conservative and the stop conditions are generally sufficient. **Apply IMP-1, IMP-2, IMP-3 patches before starting Lane A execution** — they close a status-completeness gap, prevent a potential bulk-reclassification misread, and document a tool-enforcement gap for `source_policy: normative`. The minor findings can be patched in the same pass or deferred. No blocking issues were found.
```

---

以上是完整审查报告。主要结论：

**APPROVE_WITH_CHANGES** — 无阻断性问题，三个重要发现需在 Lane A 执行前修补：

1. **IMP-1**：`status` 枚举扩展遗漏了 5 个已在用值（`current-as-of-<date>`、`complete`、`completed`、`raw-source`、`current`），建议在 § 5 补充"延期表"
2. **IMP-2**：Lane A 的兼容政策措辞没有明确禁止批量修改现有 `queries/` 页面的 `type` 字段，需在"Minimum landing change"段落补一句禁止语
3. **IMP-3**：`source_policy: normative` 字段没有任何自动化验证，应在方案中注明这个执行缺口
