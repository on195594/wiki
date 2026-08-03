---
title: Review prompt - Wonder Tools writer toolkit wiki ingestion
created: 2026-08-03
updated: 2026-08-03
type: review
status: active
---

# Independent read-only review prompt

Review commit `2532cffaef88348ce510ba69e20c9d934f0bc441` (`docs: ingest writer toolkit workflow principle`) in `/home/lin/wiki`.

## Scope

Changed files:

- `raw/articles/wondertools-writers-toolkit-2026-08-01.md`
- `concepts/ai-assumption-challenger-before-execution.md`
- `index.md`
- `log.md`

Adjacent concepts to inspect for overlap and ownership:

- `concepts/agent-research-evidence-gate.md`
- `concepts/llm-summary-identification-step.md`
- `concepts/agent-context-engineering.md`
- `concepts/hermes-context-layer-operating-rules.md`

## Review questions

1. Does the raw capture preserve source fidelity, authorship, dates, extraction limits, and time-sensitive product claims without overstating completeness?
2. Is updating `ai-assumption-challenger-before-execution` the smallest durable unit, or does the new section drift into another concept’s ownership?
3. Are source facts, existing concept synthesis, and Hermes-local inference clearly distinguished?
4. Are wikilinks useful and sufficient in both directions without creating duplicate rules?
5. Does the concept overgeneralize a practitioner interview into a default workflow or active Hermes rule?
6. Are `index.md` and `log.md` accurate and consistent with the actual commit?
7. Are there line-level wording, metadata, schema, or retrieval problems that should be fixed?

## Boundaries

Read-only review only. Do not modify files, run formatters, commit, or change memory, active skills/references, prompts, wrappers, runtime/config, cron, MCP, gateway, providers, profiles/plugins, credentials, dependencies, or external services.

## Output contract

Return these sections exactly:

- `Verdict`: `APPROVE_LANDING` or `REQUEST_BOUNDED_FIXES` or `BLOCKED_NEEDS_USER_DECISION`
- `Blocking`: each item with severity and `file:line` evidence
- `Important`: each item with severity and `file:line` evidence
- `Minor`: each item with severity and `file:line` evidence
- `Passes`: confirmed strengths
- `Recommended patches`: smallest bounded edits only

Do not treat the reviewer’s own temporary or review-output file as part of the reviewed commit.
