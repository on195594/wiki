# Wiki governance cleanup closeout

Date: 2026-05-18
Scope: `/home/lin/wiki`
Status: closed / follow-up backlog remains

## Summary

This governance round moved the wiki from a growing but drifting knowledge base to a healthier governed state: schema reflects actual directories and metadata, tag taxonomy was conservatively tightened, the longest pages now have triage and the top three were handled with reviewed page-specific plans, and every mutating step has a focused git rollback point.

The round intentionally did not try to clear every undeclared tag, reclassify historical `queries/` pages, or rewrite all long pages. Those remain controlled backlog rather than hidden drift.

## Baseline and final state

### Health check

Final command:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
```

Final result:

- `pass`: true
- `formal_pages`: 80
- `index_wikilinks`: 80
- `P0`: 0
- `P1`: 0
- `P2`: 0
- working tree after final fixes: clean

### Tag audit

Before the conservative taxonomy round:

- declared tags: 45
- undeclared unique tags: 60
- undeclared tag instances: 72

After the conservative taxonomy round:

- declared tags: 51
- undeclared unique tags: 54
- undeclared tag instances: 60
- duplicate tag files: 0

Accepted residual debt:

- `gstack` remains the main high-frequency undeclared candidate.
- `dreaming`, `project-development`, and `skill-files` remain deferred until a semantic decision is made.
- Single-use tags remain intentionally unnormalized by default.

## Completed work

### 1. Schema alignment

Updated `SCHEMA.md` so documented governance matches actual corpus structure:

- recognized `operations/` as a formal directory;
- expanded `type` guidance to include `plan`, `closeout`, `validation-case`, `operation`, and `summary`;
- expanded status guidance for formal and raw pages;
- documented `_meta/plans/`, `_meta/reviews/`, and `_meta/scripts/` roles;
- documented allowed `sources` forms and the `/tmp/...` persistence risk;
- recorded that `source_policy: normative` is not yet enforced by tooling.

### 2. Conservative taxonomy round

Added stable recurring tags to `SCHEMA.md`:

- `content-engineering`
- `position-sizing`
- `closeout`
- `pydantic`
- `structured-output`
- `typed-boundary`

No page frontmatter was bulk-rewritten during this round.

### 3. Long-page triage

Created `_meta/plans/2026-05-18-long-page-triage.md`.

Initial read-only scan found 15 formal pages above the 200-line guideline and classified the first high-priority pages.

### 4. Page-specific long-page cleanup

Handled the first three long-page targets with plan/review/implementation/review loops.

#### Harness profile validation detailed plan

- Page: `queries/hermes-harness-profile-validation-detailed-plan.md`
- Before: about 1325 lines
- After: 173 lines
- Reduction: about 1152 lines / 86.9%
- Result: converted from execution-heavy detailed plan into compact navigation and decision record.

#### Hermes project dev migration engineering review

- Page: `queries/hermes-project-dev-migration-plan-eng-review.md`
- Before: about 537 lines
- After: 146 lines
- Reduction: about 391 lines / 72.8%
- Result: converted into compact historical engineering decision record.

#### Hermes LifeOS executable architecture

- Hub page: `concepts/hermes-lifeos-executable-architecture.md`
- Before: about 388 lines
- After: 254 lines
- Reduction: about 134 lines / 34.5%
- New page: `concepts/hermes-lifeos-layer-boundary-contract.md`
- Result: split a differentiated LifeOS layer-boundary contract while preserving the hub as the top-level architecture page.

## Review gates used

Independent Claude reviews were saved under `_meta/reviews/` for:

- the broad governance cleanup plan;
- the harness page-specific plan;
- the harness compression implementation;
- the project-dev migration closeout/compression plan;
- the project-dev migration compression implementation;
- the LifeOS split plan;
- the LifeOS split implementation.

Findings were either patched into the relevant plan or recorded as accepted/closed in `log.md`.

## What was deliberately not changed

This round did not modify:

- memory;
- skills;
- cron;
- runtime config;
- MCP config;
- wrappers;
- quick commands;
- `SOUL.md`;
- Hermes core;
- project-local runtime files.

It also did not create browsable full-text archives for compressed pages. Git history plus existing project-local evidence remain the rollback/evidence path unless a future task explicitly approves archive creation.

## Remaining backlog

### High priority

1. Add a compact decision card / navigation section to `concepts/public-info-monitoring-automation-methodology.md` without splitting the page yet.
2. Decide whether `gstack` should be promoted to a declared taxonomy tag, represented as an entity/project page, or treated as a historical marker.
3. Add health-check coverage for source-form validation and obvious `/tmp/...` source risks.

### Medium priority

1. Continue long-page cleanup for remaining pages above the 200-line guideline, but use page-specific plans for any split/compression.
2. Revisit historical `queries/` pages that behave like closeouts, plans, or validation cases; prefer compact status/summary cleanup before path moves.
3. Consider month-based organization for `_meta/plans/` and `_meta/reviews/` if metadata artifacts keep growing.

### Accepted risks

- `wiki_tag_audit.py` still exits non-zero because undeclared tags intentionally remain.
- `source_policy: normative` remains documented but not fully enforced.
- The health check proves structural validity, not semantic freshness or lack of duplication.

## Recommended next sequence

1. Add the public-info monitoring methodology decision card.
2. Resolve `gstack` taxonomy/entity status.
3. Enhance wiki audit scripts for sources/schema checks.
4. Re-run health/tag audit and keep focused commits for each step.
