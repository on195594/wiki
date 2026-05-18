# Claude review prompt — Hermes harness validation compression implementation

You are an independent reviewer. Review the implementation only. Do not modify files.

## Context

Wiki root:

```text
/home/lin/wiki
```

Reviewed implementation commit:

```text
499f3ea docs: 压缩 harness 验证长页
```

Plan that must be followed:

```text
_meta/plans/2026-05-18-hermes-harness-profile-validation-split-compression-plan.md
```

Target page that was compressed:

```text
queries/hermes-harness-profile-validation-detailed-plan.md
```

Relevant prior review:

```text
_meta/reviews/2026-05-18-hermes-harness-profile-validation-split-compression-plan-claude-review.md
```

Relevant evidence records:

```text
queries/hermes-harness-profile-validation-final-closeout.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/README.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/STATUS.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/gate-6-post-patch-regression-2026-04-30.md
```

## Review goal

Check whether the compression implementation follows the reviewed plan and preserves the durable evidence/decision trail.

## Hard constraints

Flag as BLOCKING if the implementation did any of these:

- changed target page path, title, frontmatter, tags, `type`, or `status`;
- omitted the final closeout status or misrepresented final promoted changes;
- omitted Gate 6 post-patch regression from the gate summary;
- created or required a duplicate archive despite the plan default;
- modified project-local files under `/home/lin/.hermes/projects/hermes-harness-profile-validation/`;
- modified memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core;
- broke wiki links or health-check assumptions;
- removed all pointers to full evidence such that the original decision trail is no longer discoverable through git history/project-local records/wiki closeout.

## Checks to perform

Use read-only commands only. Suggested checks:

```bash
git show --stat --oneline 499f3ea
git show --name-only --oneline 499f3ea
git diff ff05f74..499f3ea -- queries/hermes-harness-profile-validation-detailed-plan.md log.md
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
```

Also inspect the compressed target page and compare it to the plan sections:

- status / closeout pointers;
- why this mattered;
- scope and non-scope;
- durable design principles;
- evidence and canonical records;
- original execution map;
- promotion and stop gates including Gate 6;
- rollback/safety;
- final acceptance criteria;
- reusable rule;
- related links.

## Output format

Write a concise markdown review with these sections:

```markdown
# Claude Review — Hermes harness validation compression implementation

Verdict: PASS | PASS_WITH_MINOR_FIXES | FAIL

## Blocking findings
- ...

## Important findings
- ...

## Minor findings
- ...

## Plan compliance
...

## Evidence preservation assessment
...

## Verification observed
...

## Recommended patch list
1. ...
```

Be specific: cite file paths and sections/lines when possible.
