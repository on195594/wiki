# Claude read-only wiki ingestion review prompt

You are reviewing a completed Hermes wiki ingestion. Respond in Chinese.

## Scope

Review commit `2d59611 docs: 入库 Agent Skill Provider 治理边界` in `/home/lin/wiki`.

Changed files:
- `raw/articles/microsoft-devblogs-agent-skills-python-provider-2026-05-24.md`
- `concepts/agent-skill-provider-governance-boundary.md`
- `index.md`
- `log.md`

Source article:
- https://devblogs.microsoft.com/agent-framework/agent-skills-for-python-file-code-and-class-composed-in-one-provider/
- Saved summary path: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260524-175728-Agent-Skills-for-Python-File-Code-and-Class-Composed-in-One-Provider-4185108-177666200-summary.md`

## Review goals

Check whether this wiki ingestion is valid and minimal:
1. Raw source provenance: Is the raw page source-backed, with URL, extraction note, summary path, and no misleading claims?
2. Concept quality: Is `agent-skill-provider-governance-boundary.md` a reusable durable concept rather than an article dump?
3. Duplication: Does it duplicate nearby pages such as `hermes-context-layer-operating-rules`, `hermes-memory-skills-wiki-boundaries`, `hermes-skill-refactoring-methodology`, or `typed-ai-agent-boundaries`? If yes, recommend specific de-dup patches.
4. Layer routing: Did the ingestion correctly stay in wiki only, without implying active skill/runtime/MCP/cron/memory promotion?
5. Index/log: Are `index.md` and `log.md` updated consistently?
6. Wiki schema/health: Check frontmatter, wikilinks, sources, line-prefix cleanliness, and whether deterministic health evidence should be trusted or repeated.
7. Source-specific boundaries: Are Microsoft Agent Framework API details, Azure/Foundry choices, decorator details, and `require_script_approval` correctly kept as source-specific examples?

## Constraints

- Read-only review only. Do not edit files.
- Do not promote memory, skills, cron, MCP, runtime, wrappers, SOUL, or Hermes core.
- If you run commands, use only read-only commands such as `git show`, `git status`, `git diff --check`, `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki`, and file reads.

## Output format

Return exactly these sections:

- Verdict: `PASS`, `PASS_WITH_MINOR_FIXES`, or `NEEDS_CHANGES`
- Blocking findings: bullet list or `none`
- Important findings: bullet list or `none`
- Minor findings: bullet list or `none`
- Recommended patches: concrete file/path/section changes; say `none` if no patch needed
- Evidence checked: commands/files inspected
- Boundary assessment: one short paragraph on whether active-layer boundaries were preserved
