# Claude read-only wiki ingestion review

You are reviewing a Hermes wiki change. This is a read-only review: do not edit files, do not commit, do not run destructive commands, and do not modify active Hermes skills/runtime/memory/cron/config.

## Change under review

Commit: `26d6d4b docs: 沉淀 AI agent built backwards 反模式`

Files changed:
- `raw/articles/towardsdatascience-most-ai-agents-built-backwards-2026-05-27.md`
- `concepts/agentic-programming-system-engineering.md`
- `log.md`

## User intent

The user asked whether the Towards Data Science article "Most AI Agents Fail in Production Because They’re Built Backwards" has similar ideas in the Hermes wiki, whether it should be sedimented into the Hermes workflow, and how. The chosen implementation was minimal: preserve raw source, update the existing `agentic-programming-system-engineering` concept with a `built backwards / model-as-orchestrator` anti-pattern, update `log.md`, and avoid memory/skill/cron/runtime promotion.

## Review scope

Please inspect the changed files and nearby relevant concept pages as needed. Evaluate:

1. Layer routing:
   - Is the article correctly kept as raw source + existing concept update?
   - Is it correctly not promoted into memory, skill, cron, runtime, gateway, MCP, or Hermes core?

2. Duplication / concept fit:
   - Does updating `agentic-programming-system-engineering.md` avoid duplicating `agent-context-engineering`, `typed-ai-agent-boundaries`, `production-ai-agent-evaluation-framework`, and `agent-orchestration-production-tradeoffs`?
   - Should this have been a new concept page, or is the existing-page decision appropriate?

3. Provenance and raw source quality:
   - Does the raw source page preserve enough provenance: URL, title, source, author/date, summary artifact, extraction note/limitation?
   - Is the extraction limitation honest enough, given the reader output begins mid-sentence?

4. Wiki hygiene:
   - Are wikilinks, frontmatter, headings, related links, and log entry appropriate?
   - Did this change unnecessarily require `index.md`? If not, is leaving `index.md` unchanged correct?

5. Actionability:
   - Are there any blocking or important fixes that should be applied before considering this ingestion complete?
   - Identify minor suggestions separately.

## Output format

Return exactly these sections:

- Verdict: PASS | PASS_WITH_MINOR_FIXES | NEEDS_CHANGES
- Blocking findings:
- Important findings:
- Minor suggestions:
- Recommended patches:
- Layer-boundary assessment:

Keep it concise but specific. Cite file paths and line numbers where possible.
