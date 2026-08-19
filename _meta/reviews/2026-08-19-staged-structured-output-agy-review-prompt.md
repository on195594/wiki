# AGY read-only review: staged structured output sedimentation

Review the completed wiki ingestion and bounded active-skill patch below. This is a read-only review: do not write, patch, commit, restore, or mutate any file, skill, memory, runtime, config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency, or external service.

## Exact change under review

- Wiki commit: `2cfcfc676686700f692b8f99e508d4337277c3db` — `docs: add staged structured-output pattern`
- Raw source: `/home/lin/wiki/raw/articles/towardsdatascience-structured-output-local-llms-2026-08-09.md`
- Updated concept: `/home/lin/wiki/concepts/typed-ai-agent-boundaries.md`
- Updated index: `/home/lin/wiki/index.md`
- Updated log: `/home/lin/wiki/log.md`
- Updated raw hash manifest: `/home/lin/wiki/_meta/raw-source-hashes.json`
- Active skill: `/home/lin/.hermes/skills/software-development/grounded-structured-output-workflows/SKILL.md`
- Pre-change skill backup: `/home/lin/.hermes/backups/structured-output-two-stage-20260819-151947/SKILL.md`
- Adjacent concept to check for duplication or conflict: `/home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md`

## Intended decision

The article's durable delta is not another generic Pydantic tutorial. It demonstrates a schema-valid but semantically wrong one-shot extraction by a small local model and repairs the worked case by splitting scope selection from detailed nested extraction.

The user rejected a passive rule that would wait for a real Hermes failure before adopting a good external method. The intended corrected policy is:

- proactively absorb source-backed, reusable, low-cost, reversible, verifiable methods;
- allow a bounded optional workflow rule before a local production failure;
- let missing local evidence limit default/hard-gate promotion, not optional adoption;
- avoid creating a new concept, project, benchmark system, model runtime, dependency, or universal two-call gate.

## Review questions

1. Source fidelity: Does the raw page preserve provenance, extraction limits, the article's worked failure/repair, and the single-case evidence boundary without overstating completeness or generality?
2. Smallest durable unit: Was updating `typed-ai-agent-boundaries` better than creating a duplicate concept? Is the new subsection distinct enough from existing structured-output and production-evaluation material?
3. Active adoption: Does the skill patch proactively expose `scope → details` while keeping clear trigger/skip conditions and avoiding a mandatory two-call workflow?
4. Evidence and validation: Are semantic correctness, schema success, call count, and latency separated appropriately? Is any important counter-case or cross-stage consistency risk missing?
5. Layer routing: Did the change stay within raw/concept/index/log/hash plus one bounded active-skill rule, without leaking into runtime/provider/dependency/cron/MCP/gateway or new-project promotion?
6. Wiki integrity: Are frontmatter, sources, wikilinks, index wording, log wording, and raw-hash handling coherent?
7. Overweight/underweight risk: Is any wording too passive, too restrictive, too broad, repetitive, or likely to turn an optional pattern into ceremony?
8. Compare the active skill against its backup and review the exact wiki commit, not conversation history.

## Known deterministic evidence

Before review, Hermes verified:

- Wiki health: PASS; P0/P1/P2 = 0/0/0.
- `git diff --check`: PASS.
- Wiki worktree after commit: clean.
- Active skill is enabled and loads via `skill_view`.
- Focused assertions found both `proactively compare one-shot generation` and `Keep staging optional`.

## Required output

Use exactly these sections:

- `Verdict`: `APPROVE`, `APPROVE_WITH_NOTES`, `REQUEST_CHANGES`, or `ROLLBACK_REQUIRED`
- `Blocking`
- `Important`
- `Minor`
- `Passes`
- `Recommended patches`
- `Active-layer decision`: state whether no active change is needed, a bounded follow-up should be proposed, or rollback is required

For every finding, cite the exact file and relevant heading/text. Do not invent line-level defects you did not verify. If there are no findings in a category, write `None`.