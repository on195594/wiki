# Read-only independent review prompt

You are AGY doing a read-only independent review of a Hermes wiki ingestion.

Scope: review only the following local wiki files under `/home/lin/wiki`:
- `raw/articles/machinelearningmastery-multi-agent-research-assistant-2026-05-21.md`
- `concepts/agent-research-evidence-gate.md`
- `concepts/production-ai-agent-evaluation-framework.md`
- `concepts/agent-orchestration-production-tradeoffs.md`
- `index.md`
- `log.md`

Do not edit files. Do not suggest active Hermes runtime/skill/memory/cron/MCP changes unless you classify them as out-of-scope future work.

Review criteria:
1. Provenance: raw source preserves source URL, publisher/date, extraction note, summary path, and does not treat generated summary as the only source.
2. Durable unit: concept page should capture a reusable pattern, not a vendor/tool tutorial.
3. Layer boundaries: concept must not imply permission to change Hermes memory, skills, cron, MCP, runtime, wrappers, or profiles.
4. Cross-links: concept should link to relevant existing pages and index/log should be consistent.
5. Claim discipline: article-specific threshold/model/vendor claims should be labeled as examples, not Hermes standards.
6. Schema/hygiene: frontmatter, tags, wikilinks, and index/log consistency should match the existing wiki style.

Output format:
- Verdict: PASS / PASS_WITH_MINOR_FIXES / NEEDS_CHANGES
- Blocking findings: bullets, or `None`
- Important findings: bullets, or `None`
- Optional findings: bullets, or `None`
- Evidence checked: list exact files/sections you inspected
