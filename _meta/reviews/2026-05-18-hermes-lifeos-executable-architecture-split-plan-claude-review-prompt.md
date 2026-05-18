# Claude review prompt: Hermes LifeOS executable architecture split plan

You are performing a read-only independent review of a page-specific wiki split plan.

Repository: `/home/lin/wiki`

Plan commit:

```text
65f6726 docs: 规划 LifeOS 架构页拆分
```

Plan file:

```text
_meta/plans/2026-05-18-hermes-lifeos-executable-architecture-split-plan.md
```

Target page, not edited by the plan:

```text
concepts/hermes-lifeos-executable-architecture.md
```

Related pages to consider for duplication/contradiction risk:

```text
concepts/hermes-memory-skills-wiki-boundaries.md
concepts/hermes-layer-routing-decision-checklist.md
concepts/hermes-context-layer-operating-rules.md
concepts/hermes-knowledge-architecture.md
concepts/hermes-knowledge-base-operating-flow.md
index.md
log.md
_meta/plans/2026-05-18-long-page-triage.md
```

Review scope:

1. Confirm the plan is plan-only and did not modify the target page or `index.md`.
2. Confirm it preserves the target page as a stable architecture hub and does not treat it like a query-page compression.
3. Confirm the candidate split pages are coherent, stable, and not obviously duplicative of existing pages:
   - `concepts/hermes-lifeos-layer-boundary-contract.md`
   - `concepts/hermes-lifeos-topology-and-profile-policy.md`
   - `concepts/hermes-lifeos-promotion-operating-policy.md`
4. Confirm the recommended first implementation is conservative: at most the layer-boundary contract first, not all three pages at once.
5. Confirm metadata/index/archive policies are safe:
   - preserve hub path/frontmatter/status;
   - update `index.md` only when a new page is created in a future implementation;
   - no `_meta/` archive by default;
   - git history remains rollback source.
6. Confirm stop conditions cover duplication, scope creep, active-layer changes, and hub degradation.
7. Confirm no memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.
8. Identify any missing pre-edit checks or plan patches needed before implementation.

Use only read-only commands. Do not edit files.

Return this exact structure:

```markdown
# Review: Hermes LifeOS executable architecture split plan

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
