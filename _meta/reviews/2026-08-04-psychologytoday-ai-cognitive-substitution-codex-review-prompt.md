# Codex read-only review prompt: Psychology Today AI cognitive substitution ingestion

You are an independent read-only reviewer. Review the current uncommitted Wiki ingestion in `/home/lin/wiki`.

## Scope

Primary new files:
- `raw/articles/psychologytoday-ai-cognitive-substitution-skill-formation-2026-08-03.md`
- `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md`

Adjacent updates:
- `concepts/ai-assumption-challenger-before-execution.md`
- `concepts/ai-agent-human-outcome-design-principle.md`
- `concepts/dijkstra-ai-programming-formalization.md`
- `index.md`
- `log.md`

Governance references:
- `SCHEMA.md`
- `concepts/wiki-ingestion-workflow.md`

## Review goals

Check the exact files and current git diff. Do not edit any file, run network calls, commit, or mutate external/active Hermes surfaces.

Assess:
1. Raw-source fidelity and provenance: title, author/date, extraction route, captured body, local-summary path, and limitations. Flag unsupported “full/substantially complete” claims or copied wrapper metadata.
2. Claim calibration: separate what the Psychology Today article says, what its cited evidence supports, and local inference. Flag causal overclaims, especially around learning, deskilling, radiologist accuracy, critical thinking, neuroscience, and cross-domain transfer.
3. Durable-unit quality: whether compensation/scaffolding/substitution/augmentation plus withdrawal/contribution tests justify a new concept rather than duplicating adjacent concepts.
4. Overlap and ownership: confirm the new concept does not duplicate the detailed owner roles of `ai-assumption-challenger-before-execution`, `ai-agent-human-outcome-design-principle`, `dijkstra-ai-programming-formalization`, or `production-ai-agent-evaluation-framework`.
5. Wiki schema and graph quality: frontmatter, declared tags, sources, index count, wikilinks, reciprocal links, dates, page length, and log accuracy.
6. Layer boundary: no promotion into memory, active skills/references, prompt, wrapper, runtime/config, cron, MCP, gateway, provider, profile/plugin, credentials, deployment, dependencies, or external services.
7. Smallest safe fixes: propose only concrete bounded changes supported by the inspected files. Do not recommend a new pilot, evaluator, monitor, or active workflow unless a real blocker requires it.

## Existing deterministic evidence

Before review, parent Hermes ran:
- `python3 _meta/scripts/wiki_health_check.py --format json` → pass=true, formal_pages=101, index_wikilinks=101, P0/P1/P2 all empty.
- `git diff --check` → exit 0.
- line-prefix check on both new pages → no accidental leading `|` prefixes.
- new concept length: 123 lines; raw source: 120 lines.

Treat this as context but independently inspect the files and diff.

## Required output

Return in Chinese using this exact structure:

- `Verdict: PASS | PASS_WITH_MINOR_FIXES | REQUEST_BOUNDED_FIXES | REJECT`
- `Blocking findings:` numbered list or `None`
- `Important findings:` numbered list or `None`
- `Minor findings:` numbered list or `None`
- `Accepted strengths:` concise bullets
- `Exact bounded fixes:` for every finding, include target path, exact section/line context, and replacement intent; otherwise `None`
- `Layer-boundary check:` explicit pass/fail
- `Landing recommendation:` one paragraph

Do not claim a file was inspected unless you actually read it. Do not modify the worktree.
