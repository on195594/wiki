---
title: AGY review prompt — Context Development Lifecycle ingestion
created: 2026-09-01
updated: 2026-09-01
type: review-prompt
status: active
---

# AGY Independent Read-only Review

You are the independent reviewer. Review commit `c09006d94fb62593510c16a09029c33db5a70ff9` (`wiki: add context development lifecycle source`) in `/home/lin/wiki`.

## Boundary

- Read-only review only. Do not modify files, commit, stage, run destructive commands, or change memory, skills, cron, MCP, runtime, wrappers, profiles/plugins, prompts, Hermes core, credentials, dependencies, or external services.
- Treat the article as a sponsored experience-based source, not independent empirical proof.
- Deterministic Wiki health and hash checks remain authoritative for structural validity; assess knowledge quality, source fidelity, overlap, routing and evidence boundaries.

## Exact files under review

- `raw/articles/thenewstack-agent-context-development-lifecycle-2026-08-31.md`
- `concepts/agent-development-lifecycle.md`
- `index.md`
- `log.md`
- `_meta/raw-source-hashes.json`

## Adjacent owners to inspect only as needed

- `concepts/hermes-active-surface-lifecycle-governance.md`
- `concepts/agent-experience-consolidation-loops.md`
- `concepts/agent-failure-closed-loop-evaluation.md`
- `concepts/hermes-context-layer-operating-rules.md`

## Review questions

1. Is updating the existing `agent-development-lifecycle` concept the smallest durable unit, rather than creating a new CDLC concept or skill?
2. Does the raw capture preserve the article's substantive main body and clearly disclose sponsorship, extraction route and evidence limits?
3. Is `Generate → Evaluate → Distribute → Observe` mapped faithfully onto `Build → Test → Deploy → Monitor` without pretending the frameworks are identical?
4. Are the context-specific checks, `human touch`, `reuse multiplier`, domain-owner/platform-governance split and observability feedback loop accurately attributed?
5. Are source claims, local Hermes inferences and non-promotions clearly separated?
6. Does the update avoid duplicating adjacent concepts and avoid silently promoting a registry, dashboard, observer, KPI, active skill or runtime behavior?
7. Are the index description, backlinks and log entry useful and proportionate?
8. Identify any concrete source-fidelity error, missing limitation, misleading mapping, broken relationship or needless durable text. Prefer deletion or one narrow correction over expansion.

## Required output

Use exactly these headings:

Verdict: PASS / PASS_WITH_MINOR_FIXES / FAIL

Blocking:
- findings or `None`

Important:
- findings or `None`

Minor:
- findings or `None`

Passes:
- concise verified strengths

Recommended patches:
- exact file and smallest replacement, or `None`

For every finding, cite the file and line/section plus the failure mechanism. Do not propose optional feature expansion.
