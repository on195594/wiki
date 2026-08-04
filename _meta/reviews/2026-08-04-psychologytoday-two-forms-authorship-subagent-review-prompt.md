---
title: Review prompt — AI and the Two Forms of Authorship wiki ingestion
created: 2026-08-04
type: review-prompt
status: active
sources: [raw/articles/psychologytoday-ai-two-forms-authorship-2026-07-30.md, concepts/ai-assistance-cognitive-substitution-and-skill-formation.md]
---

# Review prompt — AI and the Two Forms of Authorship wiki ingestion

Perform an independent, read-only review of the current uncommitted Wiki changes under `/home/lin/wiki`.

## Files in scope

- `raw/articles/psychologytoday-ai-two-forms-authorship-2026-07-30.md`
- `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md`
- `log.md` — only the newest `Linguistic versus cognitive authorship` entry

## Adjacent owner page to compare

- `concepts/ai-assumption-challenger-before-execution.md`

## Review questions

1. Does the raw capture preserve provenance, source text and extraction limits without overstating completeness or evidence strength?
2. Is updating the existing cognitive-substitution concept the smallest durable unit, or does the new section create ownership drift or duplication?
3. Are source claims, local synthesis and philosophical assumptions separated clearly enough?
4. Are the Contribution test extension and reader-trust framing useful without being misrepresented as AI-text detection?
5. Are active-layer boundaries explicit, with no accidental promotion to memory, skills, prompts, runtime, cron, MCP, wrapper, gateway or automation?
6. Is skipping a new concept page and index entry justified?
7. Do schema, wikilinks and log wording remain consistent with nearby Wiki pages?

## Required output

Return one verdict: `APPROVE`, `PASS_WITH_MINOR_FIXES`, or `REQUEST_BOUNDED_FIXES`.

For every finding provide:

- severity: blocking / important / minor;
- exact file and section;
- evidence;
- smallest safe fix;
- whether the finding must be fixed before landing.

Do not modify files, run destructive commands, commit, or propose active Hermes changes. Keep the review inside the Wiki ingestion scope.
