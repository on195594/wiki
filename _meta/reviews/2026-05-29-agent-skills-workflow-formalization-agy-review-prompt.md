# AGY read-only review prompt: Agent Skills workflow formalization wiki update

You are AGY acting as an independent read-only reviewer for a Hermes wiki update.

## Boundary

Read-only review only. Do not write files, commit, edit active Hermes skills, update memory, cron, MCP, runtime config, wrappers, prompts, or Hermes core. Treat the current working tree as the change under review.

## Files under review

- Raw source: `raw/articles/addyosmani-agent-skills-2026-05-03.md`
- Concept update: `concepts/hermes-ai-workflow-formalization-principles.md`
- Log update: `log.md`

## Context

The user asked to ingest lessons from Addy Osmani's article `Agent Skills` after a `/gsummary` summary and Claude review. The intended decision was:

1. Search existing Hermes wiki first.
2. If an existing page covers agent workflow / skill governance, update it instead of creating a near-duplicate page.
3. If no page exists, create a minimal concept page.
4. Check 2-3 existing Hermes skills read-only for trigger/workflow/checkpoint/exit-condition/anti-rationalization coverage.
5. Do not directly modify active skills; the article only provides candidate principles unless local evidence and explicit approval justify promotion.

The implementation chose to update `concepts/hermes-ai-workflow-formalization-principles.md` rather than creating a new page. It added a principle that skills should be executable workflows rather than explanatory prose, highlighted anti-rationalization tables as agent shortcut interceptors, recorded a read-only comparison against `test-driven-development`, `gsummary`, and `gemini-summary`, and added a promotion boundary. It also captured a raw source from the canonical Addy Osmani page because the O'Reilly URL returned 403.

Deterministic checks already run by the main agent:

- `git diff --check` passed.
- `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format markdown` returned PASS with P0=0, P1=0, P2=0.

## Review questions

Please inspect the listed files and adjacent wiki context if needed. Evaluate:

1. Smallest durable unit: Is updating `hermes-ai-workflow-formalization-principles.md` the right layer, or should this have been a new page / update to another existing page?
2. Source fidelity: Does the raw source and concept update accurately preserve provenance and avoid overclaiming from the article?
3. Layer routing: Does the update correctly avoid direct active skill / memory / cron / runtime promotion?
4. Engineering usefulness: Are `executable workflow over explanatory prose` and `anti-rationalization tables as shortcut interceptors` captured in a way that is useful for future Hermes skill governance?
5. Read-only skill check: Are the conclusions about `test-driven-development`, `gsummary`, and `gemini-summary` appropriately bounded, or do they overstate evidence?
6. Wiki quality: Are headings, wikilinks, source references, log entry, and duplication boundaries acceptable?

## Output shape

Return Chinese output with exactly these sections:

- `Verdict`: PASS / PASS_WITH_MINOR_FIXES / NEEDS_CHANGES
- `Blocking`: bullets, or `None`
- `Important`: bullets, or `None`
- `Minor`: bullets, or `None`
- `Passes`: bullets naming what is good
- `Recommended patches`: concrete file/section-level patches to apply, or `None`

Be critical but practical. Do not recommend active skill changes unless you clearly mark them as future candidates requiring separate approval and local evidence.
