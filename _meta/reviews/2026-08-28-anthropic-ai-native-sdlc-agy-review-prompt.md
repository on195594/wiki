# AGY read-only review: Anthropic AI-native SDLC wiki ingestion

## Role and boundary

Act as an independent read-only reviewer of a pre-commit Hermes Wiki ingestion. Do not edit, create, delete, stage, commit, or format any file. Do not change memory, skills, runtime/config, cron, MCP/tools, gateway, wrapper, provider, profile/plugin, credentials, dependencies, services, or external systems.

The repository already contains unrelated dirty changes. Review only the allowlisted paths and the exact ingestion delta described below. Do not treat unrelated worktree changes as part of this review.

## Review target

There is no target commit yet; this is a pre-commit landing review.

Allowlisted paths:

- `raw/articles/anthropic-ai-native-sdlc-playbook-2026-08-21.md` — newly captured source
- `concepts/agent-development-lifecycle.md` — existing concept update
- `index.md` — only the 2026-08-28 header date and `agent-development-lifecycle` description
- `log.md` — only the new top entry `2026-08-28 ingest | Anthropic AI-native SDLC playbook`
- `_meta/raw-source-hashes.json` — only the new raw-source hash entry

Source packet used for capture:

- `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/inputs/20260828-173515-The-AI-Native-SDLC-playbook-Claude-by-Anthropic-3422299-304062680-summary.md`
- Local summary: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260828-173515-The-AI-Native-SDLC-playbook-Claude-by-Anthropic-3422299-304062680-summary.md`
- Official URL: https://claude.com/blog/the-ai-native-sdlc-playbook

Adjacent concepts to compare for duplication and ownership:

- `concepts/agent-development-lifecycle.md`
- `concepts/hermes-agent-workflow-layering-and-adoption-order.md`
- `concepts/hermes-ai-workflow-formalization-principles.md`
- `concepts/agent-self-validation-loops.md`
- `concepts/agent-failure-closed-loop-evaluation.md`

## Intended durable delta

The ingestion should update the existing lifecycle owner rather than create a new workflow. It preserves four transferable ideas:

1. committed artifacts connect stages (`intent → spec → plan → code/tests → PR/review → incident record → new intent`);
2. faster code generation moves bottlenecks toward planning, verification, approval, and production feedback;
3. advisory controls (`CLAUDE.md`, Skills, prompts) remain distinct from deterministic controls (tests, Hooks, CI, sandbox, permissions, human approval);
4. deterministic production signals may generate a reviewable next-cycle artifact, but must not authorize direct online rule mutation.

Anthropic-specific products, fixed filenames, 20–50-task guidance, sigma tiers, one-page documentation heuristics, productivity claims, and other source-specific values must not become Hermes defaults.

## Deterministic evidence already observed

- Raw hash manifest: 146 files, exactly one raw source added.
- Wiki health: `pass: true`, `P0=0`, `P1=0`, `P2=0`.
- `git diff --check`: passed.
- Formal indexed page count remains unchanged because this is an existing-concept update.

## Review questions

Review the current allowlisted files directly and check:

1. Source fidelity: Does the raw capture preserve title, author, publication date, extraction limits, vendor bias, and the main article body without overstating cleanliness or completeness?
2. Smallest durable unit: Is updating `agent-development-lifecycle` better than creating a duplicate concept or workflow?
3. Fact/inference boundary: Are Hermes-local mappings clearly marked `[推论]`, while source-derived claims remain attributable?
4. Ownership and overlap: Does the update avoid stealing procedure ownership from `spec-driven-development`, `writing-plans`, `coding-agent-workflow`, or active-layer/runtime owners?
5. Threshold discipline: Are source-specific numbers, heuristics, tools, and product choices prevented from becoming Hermes defaults?
6. Schema/index/log/hash consistency: Are frontmatter, wikilinks, index description, log wording, raw-source hash entry, and unchanged index count consistent?
7. Extraction quality: Compare the saved raw source mechanically with the source packet after the documented bounded cleanup. Flag any material omission, injected content, malformed code fencing, or interface noise that contradicts the stated limitations.
8. Over-promotion risk: Confirm that no active workflow, skill, memory, runtime, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency, service, or external side effect is claimed or authorized.

## Required output

Use exactly these top-level sections:

- `Verdict`: `PASS`, `PASS_WITH_NOTES`, or `REQUEST_CHANGES`
- `Blocking findings`
- `Important findings`
- `Minor findings`
- `Passes`
- `Recommended patches`
- `Safety boundary assessment`
- `Recommended next step`

For every finding, cite `file:line`, explain impact, and give the smallest concrete fix. If there are no findings in a severity, write `None`. Recommend exactly one next action. Do not write files.