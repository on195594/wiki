# Claude review prompt: Hermes LifeOS layer boundary contract split implementation

You are performing a read-only independent review of a committed wiki split implementation.

Repository: `/home/lin/wiki`

Implementation commit:

```text
974c441 docs: 拆分 LifeOS 层边界契约
```

Reviewed plan:

```text
_meta/plans/2026-05-18-hermes-lifeos-executable-architecture-split-plan.md
```

Target hub page:

```text
concepts/hermes-lifeos-executable-architecture.md
```

New split page:

```text
concepts/hermes-lifeos-layer-boundary-contract.md
```

Related pages:

```text
concepts/hermes-context-layer-operating-rules.md
concepts/hermes-layer-routing-decision-checklist.md
concepts/hermes-memory-skills-wiki-boundaries.md
concepts/hermes-knowledge-architecture.md
concepts/hermes-knowledge-base-operating-flow.md
index.md
log.md
```

Review scope:

1. Compare the implementation commit against the reviewed and patched plan.
2. Confirm only the first split was implemented: `concepts/hermes-lifeos-layer-boundary-contract.md`; no topology/profile or promotion-policy split pages were created.
3. Confirm the hub page remains the stable architecture hub:
   - path unchanged;
   - title/frontmatter/tags/type/status preserved exactly;
   - top-level LifeOS/default-profile architecture decision retained;
   - hub now summarizes layer boundaries and links to the new split page;
   - hub did not degrade into only a link list.
4. Confirm the new page is differentiated from `hermes-context-layer-operating-rules.md`:
   - emphasizes LifeOS topology and `default profile` as main semantic brain;
   - treats `profile` as runtime-state isolation;
   - does not merely duplicate the generic context-layer routing map.
5. Confirm `index.md` was updated safely:
   - total page count 79 -> 80;
   - exactly one new Concepts entry for `[[hermes-lifeos-layer-boundary-contract]]`;
   - existing `[[hermes-lifeos-executable-architecture]]` entry preserved.
6. Confirm reciprocal discoverability:
   - hub links to new page;
   - new page links to hub and related routing/boundary pages.
7. Confirm no `_meta/` full-text archive was created.
8. Confirm no memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were modified.
9. Confirm verification evidence is credible:
   - `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json` passed with P0/P1/P2 all zero;
   - `git diff --check` passed;
   - implementation diff scope was four files: hub, new page, index, log;
   - hub line count changed 387 -> 254;
   - new page line count is 190.

Use only read-only commands. Do not edit files.

Return this exact structure:

```markdown
# Review: Hermes LifeOS layer boundary contract split implementation

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
