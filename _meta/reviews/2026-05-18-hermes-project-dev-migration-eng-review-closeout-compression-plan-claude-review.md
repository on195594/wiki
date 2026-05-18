# Claude Review — Hermes project dev migration closeout/compression plan

Verdict: APPROVE_WITH_CHANGES

Reviewed: 2026-05-18
Plan: `_meta/plans/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan.md`
Target page (read-only): `queries/hermes-project-dev-migration-plan-eng-review.md`
Live-state checks performed: both project directories, `~/.hermes/scripts/`, `queries/investment-watch-final-closeout.md`, `index.md` entry.

---

## Blocking findings

None. All seven hard constraints are satisfied:

1. Target page editing during plan/review — explicitly prohibited in Section 2 Non-goals. ✓
2. Evidence deletion — Section 6 relies on git history; no archive is created by default. ✓
3. Modifying project directories — Section 2 Non-goals explicitly exclude both paths. ✓
4. Modifying memory/skills/cron/runtime/MCP/SOUL.md/Hermes core — Section 2 Non-goals and Section 9 stop condition cover all of these. ✓
5. Changing frontmatter/path/tags/type/status/index during first compression — Section 8 step 3 and Section 9 stop condition both prohibit this. ✓
6. Treating historical recommendations as current commands — Section 3 flags this explicitly and Section 5 proposes historical framing. ✓
7. Creating project-kickoff closeout inside the compression commit — Sections 4 and 10 both defer this to a separate follow-up gap. ✓

---

## Important findings

### 1. `index.md` is not in the Section 7 pre-edit checklist

Live check confirmed the target page IS indexed:

```
index.md: - [[hermes-project-dev-migration-plan-eng-review]] — Hermes 项目开发迁移计划 eng review：...
```

Section 7 pre-edit checks (items 1–7) and Section 9 stop conditions do not include reading `index.md` to verify the entry. If the implementer doesn't check this, they won't notice whether the path is correctly listed, nor have explicit confirmation that it must not be changed. A missed `index.md` edit would silently change a hard-constraint-protected entry.

**Required patch**: add to Section 7, item 2 (or as a new item 2a):
> Confirm target page path appears in `index.md`; do not update that entry in the compression commit.

And add to Section 9 stop conditions:
> implementation requires updating `index.md` for any reason — stop and get explicit approval.

### 2. Proposed page shape (Section 5) has no frontmatter stub

Section 8 step 3 says "Do not change frontmatter … in the compression commit." But Section 5's proposed markdown block starts at `# Hermes Project Development Migration Plan Eng Review` with no frontmatter. An implementer templating from Section 5 might omit the frontmatter block entirely.

**Required patch**: add a frontmatter stub at the top of the Section 5 proposed structure, explicitly marked as "preserve verbatim from original":

```
---
[preserve verbatim from original: title, created, updated, type, tags, sources, status]
---
```

### 3. Evidence pointer for `investment-watch-final-closeout.md` is conditional but the file is confirmed present

Section 5's "Current evidence and pointers" item reads "Related investment-watch closeout if relevant." The file `queries/investment-watch-final-closeout.md` is confirmed present. The pointer should be unconditional in the compressed page, not optional.

**Required patch**: Section 5 should read "investment-watch wiki closeout (confirmed present at `queries/investment-watch-final-closeout.md`)" rather than "if relevant."

---

## Minor findings

1. **Line count off by one.** The plan's preamble and Section 3 both say "536 lines." The file has 537 lines. This doesn't affect compression logic but creates a small discrepancy if the pre-edit check compares against this number.

2. **Archive filename uses page creation date, not compression date.** Section 6 proposes `_meta/plans/archive/2026-04-24-hermes-project-dev-migration-plan-eng-review-original.md`. The prefix `2026-04-24` is the target page's `created:` date. The convention should be noted explicitly so there's no ambiguity when this archive is eventually created (or not).

3. **`investment-watch` project has richer structure than Section 3 records.** Live check found: AGENTS.md, backups, data, docs (architecture, contracts, decisions, plans, retrospectives, reviews, user-manual.md), pyproject.toml, README.md, scripts, src, tests, uv.lock. Section 3 only notes that the directories "exist." The compressed page's evidence pointers could be more specific about the available docs if useful.

4. **Section 9 stop condition could add a "new fact-finding needed" trigger.** The existing condition "current project-local state contradicts the historical page so strongly that the compact page would need new fact-finding" is adequate but could be sharpened: "if writing evidence pointers requires reading more than the project README/index, stop and consult."

---

## Archive policy assessment

Acceptable. The default (git history only, no browsable archive copy) is the right call here. The full 537-line page will remain accessible via `git log -p` or `git show`. A `_meta/plans/archive/...` copy would duplicate retrieval noise rather than reduce it. The conditional path is clearly gated by explicit approval and is not invoked during the first compression. No concerns.

---

## Page-shape assessment

The proposed structure in Section 5 preserves sufficient durable lookup value:

- Historical framing in a top-level `## Status` block — prevents future misreading as an active checklist.
- Summary decision — captures the key rationale (split business projects out of `~/.hermes/scripts/`, keep Hermes as host layer).
- Scope and non-scope — the non-scope list is the single most important thing to retain; it prevents scope creep on any future revisit.
- Engineering findings — short bullets for architecture, code quality, testing, performance.
- Historical implementation map — three-phase order only, no full file trees (correctly deferred).
- Evidence pointers — project directories, office-hours review, investment-watch closeout.
- Final verdict — `DONE_WITH_CONCERNS` with the two non-negotiable concerns (cron/hardcoded paths, minimum tests).
- Related links.

Expected reduction from 537 to ~100–150 lines is realistic. The main durable lookup use case (why this migration, what was excluded, are the critical gaps acknowledged) is preserved.

One gap: the Final Verdict section lists the two concerns but does not mention the verification expectations from the original "Completion Summary" (lines 502–515). The compressed page should note that all review phases passed and the 2/2 critical gaps were explicitly called out, so a reader knows the verdict was fully informed rather than a summary short-cut.

---

## Pre-edit gate assessment

Section 7 items 1–7 are largely sufficient. Confirmed pass/fail for each against live state:

| Check | Result |
|---|---|
| Wiki repo clean | pre-edit responsibility, not checked here |
| Target page path/frontmatter | confirmed as stated in plan |
| Source page exists (`hermes-project-dev-office-hours-review.md`) | confirmed present |
| `investment-watch/` directory | confirmed, fully built out |
| `project-kickoff/` directory | confirmed, fully built out |
| `investment-watch-final-closeout.md` | confirmed present |
| project-kickoff closeout | confirmed absent — gap to note |
| browsable archive needed | default: no |

The one missing gate is the `index.md` check (see Important finding #1). Without it, the implementer has no explicit instruction to verify and leave the index entry unchanged.

Section 9 stop conditions are well-formed and comprehensive. They cover path/frontmatter drift, missing source page, compression scope creep into project-local files, and state contradiction. The sharpening in Minor finding #4 is optional.

---

## Historical/current-state handling

Correct and well-grounded. The plan's baseline (Section 3) accurately reflects what live checks confirm:

- Both project directories exist and are fully populated — investment-watch has a complete `docs/` hierarchy (architecture, contracts, decisions, plans, retrospectives, reviews, user-manual), not just a scaffold.
- The old `~/.hermes/scripts/project_kickoff.py` is confirmed absent.
- Old investment-watch scripts (`market_watch.py`, `review_trades.py`, etc.) are no longer in `~/.hermes/scripts/`.
- The target page's `Next Step` section (lines 525–532) recommending active Phase 1 execution is now historical — correctly treated as such.

The framing of the target page as a "historical engineering decision record, not an active migration checklist" is well-supported by observed state. The proposed `## Status` block in Section 5 makes this explicit for future readers.

The project-kickoff closeout gap is correctly identified (no wiki closeout page found) and correctly deferred to a separate follow-up rather than filled during compression.

---

## Recommended patch list

1. **Section 7 (Required pre-edit checks)**: Add item — confirm target page path appears in `index.md`; do not update that entry in the compression commit.

2. **Section 9 (Stop conditions)**: Add trigger — "implementation requires updating `index.md` for any reason."

3. **Section 5 (Proposed final wiki page shape)**: Add a frontmatter stub at the top of the proposed block, explicitly labeled "preserve verbatim from original."

4. **Section 5, evidence pointers**: Change "Related investment-watch closeout if relevant" to "investment-watch wiki closeout (confirmed present at `queries/investment-watch-final-closeout.md`)."

5. **Section 5, Final verdict block**: Add a note that the compressed verdict should reference the Completion Summary phase count and the 2/2 critical gaps, so future readers know the verdict was fully informed.

6. **(Optional / minor)** Section 3 line count: correct "536 lines" to "537 lines" to match the actual file.
