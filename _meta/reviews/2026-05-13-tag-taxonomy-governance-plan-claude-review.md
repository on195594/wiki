I now have everything needed for the review.

---

## Review: Wiki Tag Taxonomy Governance Plan

**Date reviewed:** 2026-05-13
**Verdict: PASS_WITH_NOTES**

---

### Verdict summary

The plan is safe, appropriately scoped, and follows wiki conventions. It is conservative where it should be: Step 3 replacement set is small, ambiguous tags are deferred, and the validation gates are sound. No blocking issues prevent execution. The notes below should be addressed before or during Step 3 to avoid introducing tag corruption.

---

### Blocking findings

None.

---

### Important findings

**I-1 — `ai-agent` → `agent` has a silent duplicate-tag bug**

`raw/articles/venturebeat-anthropic-dreaming-ai-agents-2026-05-07.md` already carries both `agent` AND `ai-agent`. A mechanical substitution of `ai-agent` → `agent` on this file produces a duplicate entry in the list. The `wiki_tag_audit.py` proposed in Step 1 must deduplicate after replacement, or Step 3 must explicitly filter out files where both tags already coexist. This is easy to miss during manual editing.

**I-2 — `concepts/typed-ai-agent-boundaries.md` carries `ai-agent` without `agent`**

That page uses `ai-agent` + `ai-coding` + `pydantic`. The tag `ai-agent` here explicitly signals typed structured-boundary design patterns, distinct from general workflow agent pages. Replacing it with `agent` is semantically lossy unless `ai-coding` is retained (it is). Before applying the replacement to this file, confirm `ai-coding` stays. If the plan adds `ai-coding` to the schema as a facet tag (which it does), then `agent` + `ai-coding` is a workable substitute. Just requires manual confirmation, not a bulk replace.

**I-3 — Declared-but-unused tags have no explicit disposition**

`SCHEMA.md` currently declares `devops`, `linux`, `networking`, `product` — none of which appear on any page. The plan says "keep existing legitimate tags unless clearly obsolete" but doesn't decide these four cases. Leaving them in the taxonomy makes the schema look wider than the actual corpus. The plan should assign a one-line decision per tag: retain as reserved (with a note), mark deprecated, or remove. Even "retain, reserved for future infrastructure pages" is a valid answer, but it should be stated.

**I-4 — No clean-tree gate before Step 3**

The validation checklist in §8 runs `git diff --check` but does not require the working tree to be clean *before* Step 3 begins. If the repo has uncommitted changes when tag edits are applied, a rollback requires `git diff` archaeology rather than a simple `git checkout .`. The plan should add: "Ensure `git status` is clean before Step 3."

---

### Minor findings

**m-1 — `wiki_tag_audit.py` exit code convention is underspecified**

The plan says "exit 0 for audit-only mode" but `wiki_health_check.py` uses `0 = pass`, `1 = issues found`, `2 = CLI/runtime error`. The audit script should follow the same convention, otherwise callers can't distinguish "ran cleanly, zero issues" from "ran cleanly, issues reported." Suggest: `0 = audit complete, no undeclared tags found`, `1 = audit complete, undeclared tags exist`, `2 = runtime error`.

**m-2 — Domain vs. Facet distinction is not given a written criterion**

The plan proposes adding both Domain and Facet classes to `SCHEMA.md` but doesn't define the rule separating them. From reading the candidates: Domain = subject matter (`investment`, `monitoring`, `governance`); Facet = cross-cutting AI-workflow lens (`multi-agent`, `orchestration`, `evaluation`). This distinction should be written as one sentence in the `SCHEMA.md` update so future tag authors know which class to pick.

**m-3 — Raw article tags are implicitly in scope but not named**

Step 3 says "only replace when the file context confirms the meaning" without specifying whether raw articles are included. `raw/` files have frontmatter tags too (10 files scanned). Since `wiki_health_check.py` excludes `raw/` from formal-page checks, tag normalization in raw articles is lower priority — but if the audit script counts undeclared tags, raw articles will contribute to the count. The plan should state explicitly: "raw/ tags are included in the audit count but are lower priority for Step 3 replacements."

**m-4 — Existing SCHEMA.md rule text needs updating**

`SCHEMA.md` currently ends its tag section with: "规则：新增 tag 前先更新本节，再在页面里使用。" The plan adds a new quantitative threshold rule ("3+ pages = candidate for taxonomy"). These two rules need to be written together in one coherent block so the SCHEMA.md update doesn't leave a dangling legacy sentence next to new 3-class structure.

---

### Recommended plan edits

| Section | Edit |
|---|---|
| §6 Step 3 preamble | Add: "Before beginning, confirm `git status` shows a clean working tree." |
| §6 Step 3, `ai-agent` entry | Add note: "Skip files where `agent` is already present (to avoid duplicates). For `typed-ai-agent-boundaries.md`, confirm `ai-coding` is retained before removing `ai-agent`." |
| §6 Step 1 (audit script) | Add exit code spec: 0 = no issues, 1 = issues found, 2 = runtime error. Align with `wiki_health_check.py`. |
| §3 Non-goals or §4 | Add one sentence: "Raw article tags are included in audit counts but excluded from Step 3 first-pass replacements." |
| §4 or §2 | Add one sentence disposition for each of `devops`, `linux`, `networking`, `product` (retain-reserved or remove). |
| §6 Step 2 | Note that the existing rule line in SCHEMA.md tag section will be merged into the updated governance rule. |
| §4 model | Add one sentence defining Domain vs. Facet boundary criterion for future authors. |
