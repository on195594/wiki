# AGY read-only review prompt: WikiSkill ingestion

You are an independent read-only reviewer. Review the current uncommitted WikiSkill ingestion in `/home/lin/wiki`.

## Read-only boundary

- Do not edit, create, delete, rename, stage, or commit any file.
- Do not modify memory, Hermes skills/references, runtime/config, cron, MCP, gateway, wrapper, prompt, provider, profile/plugin, credentials, dependencies, services, or external systems.
- Use the repository and source only for inspection. Report findings; parent Hermes will verify and apply any fixes.

## Files under review

- `raw/papers/arxiv-2608-27454-wikiskill.md`
- `concepts/agent-experience-consolidation-loops.md`
- `index.md`
- `log.md`
- `_meta/raw-source-hashes.json`

Review the complete current `git diff`, including the untracked raw paper file. The source paper is:

- Abstract: https://arxiv.org/abs/2608.27454
- PDF: https://arxiv.org/pdf/2608.27454

Adjacent owners to inspect only as needed for overlap/boundary checks:

- `concepts/hermes-knowledge-architecture.md`
- `concepts/agent-self-validation-loops.md`
- `concepts/agent-closed-loop-learning-from-corrections-to-rules.md`
- Hermes skill `skill-optimization-workflows` if visible; do not modify it.

## Intended decision

The ingestion should reuse `agent-experience-consolidation-loops` rather than create a new concept or Skill. It should preserve full-paper evidence in `raw/papers`, compile only durable deltas into the existing concept, and leave rollout-actor Wiki isolation as an `OPTIONAL_REFERENCE` candidate requiring frozen local A/B evidence before default adoption. No active Skill, memory, project/pilot, runtime, cron or MCP change is authorized.

## Review questions

1. **Source fidelity:** Are architecture, role boundaries, benchmarks, reported numbers, ablation, cross-model transfer/negative transfer and limitations represented faithfully and with source-specific scope?
2. **Inference discipline:** Are paper facts, author interpretation and Hermes-local inference clearly separated? Flag claims that overstate causality, significance, universality or production readiness.
3. **Smallest durable unit:** Is updating the existing concept preferable to a new page/Skill? Is any inserted concept text redundant, misplaced or too long?
4. **Workflow adoption:** Is rollout-actor Wiki isolation correctly bounded to diagnostic skill-evolution rollouts with trigger, skip, frozen comparison and graduation conditions? Does anything silently promote it to default behavior?
5. **Lifecycle governance:** Does the change correctly preserve rejected proposals as evidence without keeping them active, and keep active promotion/rollback separately authorized?
6. **Transfer boundary:** Does it avoid treating file portability or source-model strength as behavioral portability?
7. **Wiki quality:** Check frontmatter, sources, wikilinks, index/log consistency, raw-hash manifest intent, duplicate concepts and reverse-link usefulness.
8. **Scope hygiene:** Identify any unrelated edits or missing boundary statements.

Run read-only checks if useful, but do not repair anything. Do not report the temporary existence of the review output itself as a defect.

## Required output

Use exactly these top-level headings:

- `Verdict`: `PASS`, `PASS_WITH_MINOR_FIXES`, or `FAIL`
- `Blocking`
- `Important`
- `Minor`
- `Passes`
- `Recommended patches`

For every finding include severity, exact file and line/section, evidence, why it matters, and the smallest proposed correction. If there are no findings at a severity, write `None`.
