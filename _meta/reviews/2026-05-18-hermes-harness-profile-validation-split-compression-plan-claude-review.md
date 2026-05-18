`★ Insight ─────────────────────────────────────`
This plan uses a layered evidence-preservation model common in well-run knowledge systems: git history as the "cold" archive, project-local docs as the "warm" canonical record, and the wiki page as the "hot" navigation surface. The review task is essentially checking whether the compression plan respects that separation without accidentally destroying evidence at any layer.
`─────────────────────────────────────────────────`

Now writing the review with full context.

---

# Claude Review — Hermes harness validation split/compression plan

**Verdict: APPROVE_WITH_CHANGES**

The plan is well-scoped, correctly non-destructive, and respects all major boundary constraints. Three issues need patching before implementation: a frontmatter-gate ambiguity, a Gate 6 coverage gap in the proposed page shape, and a missing wiki-closeout file check in the pre-edit checklist. None are blocking on their own, but together they create enough ambiguity that a future implementer could go slightly off-track.

---

## Blocking findings

None.

All hard constraints are explicitly honored in section 2 (non-goals) and section 9 (stop conditions). No evidence deletion, no project-local modification, no Hermes core/skill/cron/memory change is authorized or implied.

---

## Important findings

**I-1. Frontmatter gate in section 8 step 3 contradicts section 2.**

Section 2 (non-goals) prohibits "changing the target page path, title, frontmatter, tags, or `type`." But section 8 step 3 says: *"Preserve frontmatter unless there is explicit approval to change `status` or `type`."* The phrase "unless there is explicit approval" leaves the door open for an implementer to decide inline during the compression commit that such approval exists — without a separate explicit decision step. This partially undermines the section 2 guarantee. The implementation step should say: *"Do not change frontmatter, `status`, or `type` in the compression commit; these require a separate, explicitly approved pass."*

**I-2. The proposed compact page shape (section 5) may produce a Gate 6 gap.**

Section 5 maps `## Promotion and stop gates` to "[Compressed gate list]." The only source for that list in the original wiki page is section 13 (lines 1152–1197), which covers Gates 1–5 only. Gate 6 (post-patch regression) is not in the wiki page at all — it exists only in `docs/gate-6-post-patch-regression-2026-04-30.md`. A future implementer who compresses only section 13 will silently omit Gate 6 from the compact page. The plan should explicitly call out that the compressed gate list must synthesize all six gates that were actually executed (the original five from section 13 plus Gate 6 from project-local evidence), with a link to the gate-6 doc.

Note: section 5's `## Evidence and canonical records` does list "Gate 6 regression evidence," but this is in a separate section from "Promotion and stop gates" — an implementer can include both sections and still present Gates 1–5 as the complete gate sequence.

**I-3. The pre-edit checklist (section 7) omits the wiki final closeout file.**

Section 7 lists four project-local evidence files to verify in step 4. The wiki final closeout (`queries/hermes-harness-profile-validation-final-closeout.md`) is referenced in sections 3 and 4 as a key durable record, and section 9 stop conditions do block on it being missing — but it is not in section 7's explicit pre-edit verification list. This creates inconsistency: a future implementer following section 7 mechanically would skip confirming the file exists before editing. It should be added as step 4e or a standalone step 5 in section 7.

---

## Minor findings

**M-1. Section 8 step 1 wording is confusing.**

"Create a rollback commit for this plan if not already committed" — "rollback commit" is not a standard git concept and could be misread. The intent appears to be: *ensure a clean commit checkpoint in the wiki repo exists before starting any edits to the target page.* Suggest: *"Confirm the wiki repo is clean and committed (so the pre-edit state is fully recoverable via `git checkout`)."*

**M-2. Line count discrepancy between plan and triage doc.**

Section 3 says the target page is "1324 lines, 31486 bytes." The triage document (`2026-05-18-long-page-triage.md`, line 31) says "1325." The difference is one line — likely a frontmatter delimiter counting difference — but it could confuse an implementer who verifies the count before editing. Minor; note in plan that counts may vary ±1 by tool.

**M-3. Section 10 open questions are already answered by the default recommendation.**

All three open questions in section 10 have a stated default answer in the same section. Since this plan will be reviewed before implementation, explicitly marking the defaults as "the answer unless overridden in review" would make the section less ambiguous for an implementer who reads it out of order.

---

## Archive policy assessment

**Acceptable.** The default policy — git history as cold archive, project-local evidence as canonical warm record, no `_meta/plans/archive/` copy unless explicitly approved — is the right choice. The project-local directory is complete and well-structured; duplicating 1324 lines of execution plan into `_meta/` would add retrieval noise without adding evidence value. The explicit opt-in path (`_meta/plans/archive/2026-04-30-hermes-harness-profile-validation-original-detailed-plan.md`) is well-named and correctly gated.

---

## Page-shape assessment

**Sufficient with one fix (I-2 above).** The proposed 120–180 line shape covers all durable lookup value: status + closure verdict, promoted changes, explicit non-authorized changes, design principles, evidence paths, original execution map in pointer form, and related links. The structure appropriately turns an implementation checklist into a navigation/decision page. The shape will preserve enough context for future readers to understand why the validation existed, what it decided, and where the full evidence lives — provided Gate 6 is included in the gate summary as noted in I-2.

---

## Pre-edit gate assessment

**Mostly sufficient; one gap (I-3 above).** The combination of section 7 (pre-edit checks) and section 9 (stop conditions) forms a reasonable safety net:

- wiki working tree clean ✓
- project-local inspect-only ✓
- read target page and final closeout ✓
- verify four project-local evidence files ✓ (but see I-3: wiki closeout not listed)
- archive decision: default no ✓
- health check + diff + stat + status ✓
- commit only compressed page + log entry ✓

The stop condition list in section 9 is comprehensive, including the closed-project boundary enforcement. Adding the wiki final closeout to section 7's explicit checklist (I-3) closes the only mechanical gap.

---

## Recommended patch list

1. **Section 8 step 3** — Replace "Preserve frontmatter unless there is explicit approval to change `status` or `type`" with: *"Do not change frontmatter, `status`, or `type` in the compression commit. Any reclassification requires a separate explicitly approved pass (see section 10 question 1)."*

2. **Section 5** — In the `## Promotion and stop gates` description, replace "[Compressed gate list.]" with: *"[Compressed list of all six gates actually executed: Gates 1–5 from section 13 of the original page, plus Gate 6 post-patch regression from `docs/gate-6-post-patch-regression-2026-04-30.md`. Link the gate-6 doc.]"*

3. **Section 7** — Add a step 4e (or standalone step 5 before the archive decision): *"Confirm wiki final closeout exists: `queries/hermes-harness-profile-validation-final-closeout.md`."*

4. **Section 8 step 1** — Replace "Create a rollback commit for this plan if not already committed" with: *"Confirm the wiki repo is in a clean, committed state so the pre-edit snapshot is recoverable via `git checkout`."*

5. **Section 10** — Mark all three default recommendations as authoritative for this review: if the reviewer approves without changes to these items, treat the defaults as the implementation decision.
