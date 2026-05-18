# Claude review prompt: Hermes project dev migration compression implementation

You are performing a read-only independent review of a committed wiki long-page compression implementation.

Repository: `/home/lin/wiki`

Implementation commit:

```text
6e292a6 docs: 压缩项目迁移审查长页
```

Reviewed plan:

```text
_meta/plans/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan.md
```

Target page:

```text
queries/hermes-project-dev-migration-plan-eng-review.md
```

Related evidence:

```text
queries/hermes-project-dev-office-hours-review.md
queries/investment-watch-final-closeout.md
index.md
log.md
/home/lin/.hermes/projects/investment-watch/
/home/lin/.hermes/projects/project-kickoff/
```

Review scope:

1. Compare the implementation commit against the reviewed plan.
2. Confirm the target page was compressed into a compact historical engineering decision record, not an active migration checklist.
3. Confirm target page path, title, frontmatter, tags, `type`, and `status` were preserved exactly.
4. Confirm `index.md` was not modified and the target page remains indexed.
5. Confirm key durable content remains discoverable:
   - migration rationale;
   - scope / non-scope;
   - architecture / code quality / test / performance findings;
   - three-phase migration order;
   - `DONE_WITH_CONCERNS`;
   - the two non-negotiable concerns: cron/internal hardcoded paths and minimum tests;
   - completion-summary signal and 2/2 critical gaps;
   - prior office-hours page;
   - investment-watch final closeout;
   - project-local evidence pointers;
   - missing project-kickoff wiki closeout/status page recorded as a follow-up gap, not invented.
6. Confirm the implementation did not create a browsable full-text archive.
7. Confirm only the target page and `log.md` were modified in the implementation commit.
8. Confirm no project-local files, memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core were modified.
9. Confirm the verification evidence is credible:
   - `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json` passed with P0/P1/P2 all zero;
   - `git diff --check` passed;
   - `git diff --stat` showed the intended narrow scope;
   - target page went from 536 lines to 146 lines.

Use only read-only commands. Do not edit files.

Return this exact structure:

```markdown
# Review: Hermes project dev migration compression implementation

Verdict: PASS | PASS_WITH_MINOR_FIXES | APPROVE_WITH_CHANGES | BLOCK

## Blocking findings
- ... or None

## Important findings
- ... or None

## Minor findings
- ... or None

## Verification notes
- ...
```
