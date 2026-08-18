# AGY read-only review: AI Agent pre-deploy regression-test sedimentation

You are AGY acting as an independent reviewer. Review the current **uncommitted** wiki ingestion in `/home/lin/wiki` strictly read-only.

## Hard boundary

- Do not modify, create, delete, stage, commit, format, or regenerate any file.
- Do not alter memory, Hermes skills, runtime/config, cron, MCP/tools, gateway, wrapper, provider, profile/plugin, credentials, dependencies, or external systems.
- Do not run commands that write caches or generated artifacts. Reading files and `git diff` is allowed.
- Treat the article as a practitioner source, not an authoritative empirical study.

## Exact files under review

1. `raw/articles/machinelearningmastery-agent-regression-tests-2026-08-17.md`
2. `concepts/production-ai-agent-evaluation-framework.md`
3. `concepts/agent-development-lifecycle.md`
4. `index.md`
5. `log.md`
6. `_meta/raw-source-hashes.json`

## Source and intent

Source URL: https://machinelearningmastery.com/7-regression-tests-every-ai-agent-should-pass-before-deploy/

Intended landing:
- preserve the full article body and provenance as raw evidence;
- update the existing `production-ai-agent-evaluation-framework` rather than create a duplicate concept;
- express the seven tests as a capability-triggered matrix with skip conditions, not a universal hard gate;
- link it from the `agent-development-lifecycle` Test → Deploy boundary;
- route only real locally observed failures to `agent-failure-closed-loop-evaluation` as a fixture/evaluator/smoke;
- make no active skill/runtime/project promotion.

## Adjacent pages to consult only as needed

- `concepts/agent-failure-closed-loop-evaluation.md`
- `concepts/typed-ai-agent-boundaries.md`
- `concepts/production-agent-evaluation-baselines.md`
- `SCHEMA.md`

## Review questions

1. Is `production-ai-agent-evaluation-framework` the smallest correct durable owner, or does this duplicate/misplace existing knowledge?
2. Does the seven-probe matrix faithfully preserve the source while correctly narrowing applicability through trigger and skip conditions?
3. Are source claims, Hermes-local inferences, evidence limitations, and non-promotion boundaries clearly separated?
4. Does the lifecycle cross-link improve Test → Deploy retrieval without duplicating the matrix?
5. Are any material source details omitted or distorted, especially stochastic test handling, retrieval-vs-summary separation, trace/side-effect assertions, structured-output semantics, bounded orchestration, bidirectional RAG risk, and state-rehydration/idempotency coupling?
6. Are raw provenance, frontmatter, wikilinks, index/log updates, and hash-manifest handling coherent with `SCHEMA.md`?
7. Did the change introduce unnecessary ceremony, a hidden default gate, or an active-layer implication contrary to the stated boundary?

## Required output

Return exactly these sections:

- `Verdict`: `PASS`, `PASS_WITH_NOTES`, or `REQUEST_CHANGES`
- `Blocking findings`: each with file/section evidence, impact, and minimal fix; write `None` if empty
- `Important notes`: non-blocking but material issues; write `None` if empty
- `Minor findings`: optional wording/link/maintenance issues; write `None` if empty
- `Passes`: concise list of what is correct
- `Safety boundary assessment`: whether any active/runtime/external side effect or unsafe shortcut was introduced
- `Recommended patches`: exact bounded edits only, or `None`
- `Recommended next step`: exactly one action

Do not propose a new skill, evaluator project, cron, runtime change, or broader wiki refactor unless you identify a concrete blocking gap that cannot be fixed in the listed files.
