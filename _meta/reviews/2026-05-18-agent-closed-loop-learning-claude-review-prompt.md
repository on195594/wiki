# Claude independent review prompt

You are an independent reviewer for a Hermes wiki ingestion. Review only the ingestion plan/result and content quality. Do not edit files.

## Context
The user approved ingesting a Microsoft article about Power Apps MCP closed-loop learning into the Hermes wiki. The intended scope was:
- preserve raw source under `raw/articles/`
- create one durable concept page under `concepts/`
- update `index.md` and `log.md`
- add focused cross-links to existing related concept pages
- do not modify active memory, skills, cron, runtime, MCP, wrappers, or Hermes core

## Files to review
- `/home/lin/wiki/raw/articles/microsoft-power-apps-mcp-closed-loop-learning-2026-05-12.md`
- `/home/lin/wiki/concepts/agent-closed-loop-learning-from-corrections-to-rules.md`
- `/home/lin/wiki/index.md`
- `/home/lin/wiki/log.md`
- `/home/lin/wiki/concepts/agent-experience-consolidation-loops.md`
- `/home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md`
- `/home/lin/wiki/concepts/hermes-context-layer-operating-rules.md`
- optionally inspect `/home/lin/wiki/SCHEMA.md`

## Review questions
1. Does the ingestion match the approved scope and wiki conventions?
2. Is the raw source acceptable as preserved provenance rather than a misleading generated summary?
3. Is the concept page the right durable unit, or is it too product-news-like / too procedural / misplaced?
4. Are source facts, local Hermes implications, and recommendations clearly separated?
5. Are Microsoft numbers preserved as directional/source-specific evidence, not hard Hermes thresholds?
6. Are cross-links useful and not excessive?
7. Any broken links, frontmatter/schema issues, index/log issues, or page-size concerns?
8. Any overclaiming, unsupported claims, or missing caveats?

## Required output format

Verdict: PASS / PASS_WITH_MINOR_FIXES / NEEDS_CHANGES

Blocking:
- ...

Important:
- ...

Minor:
- ...

Recommended patches:
- For each suggested patch, name the file, current problematic text/section, and exact replacement or action.

Evidence checked:
- List files and checks you actually inspected.

Do not perform edits. If you use shell commands, use read-only commands only (`git diff`, `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json`, `grep`, etc.).