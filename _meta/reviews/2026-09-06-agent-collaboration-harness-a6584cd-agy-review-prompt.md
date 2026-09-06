# AGY independent read-only review: agent collaboration and harness evidence

You are an independent, adversarial reviewer. Review commit `a6584cd3784a1642a450de60167978ccbdef77c4` (`wiki: capture agent collaboration and harness evidence`) in `/home/lin/wiki`.

## Read-only boundary

Do not modify files, stage changes, commit, or alter memory, skills, cron, MCP, runtime, wrappers, prompts, profiles/plugins, credentials, or Hermes core. Use only read-only inspection commands. Treat committed blobs from `git show a6584cd:<path>` and the commit diff as authoritative. The current worktree may contain later review artifacts; do not treat them as reviewed content.

## Exact commit allowlist

- `_meta/raw-source-hashes.json`
- `concepts/agent-development-lifecycle.md`
- `concepts/agent-orchestration-production-tradeoffs.md`
- `concepts/production-ai-agent-evaluation-framework.md`
- `concepts/stateful-agent-environments-and-grounded-verification.md`
- `concepts/subagent-orchestration-patterns.md`
- `index.md`
- `log.md`
- `raw/articles/nature-capable-language-models-can-outgrow-the-benefits-of-collaboration-2026.md`
- `raw/articles/stencil-the-harness-playbook-2026-09-05.md`

Adjacent concepts may be inspected read-only only to evaluate overlap and links. Public source URLs in the raw records may be checked read-only where available. Distinguish direct publisher evidence from local summary-derived claims.

## Intended boundary

This is a Wiki-only ingestion and existing-owner update. It should retain two bounded source records and add only reusable concept-level conclusions. It must not turn source-specific numerical results, architecture proposals, technology choices, or general tutorials into Hermes defaults. It must not create or imply authorization for active Skills, runtime/config, MCP, cron, gateway, provider, router, pool, team, or evaluation-platform changes.

## Review criteria

Review the exact committed bytes and cite committed `file:line` ranges.

1. **Source fidelity** — Are claims in concept/index/log updates supported by the corresponding raw record? Does each raw record accurately disclose its structured-capture limitation, provenance, source-vs-summary status, and evidence limits? Flag any externally checkable bibliographic or quantitative claim that is wrong or insufficiently anchored.
2. **Smallest durable unit** — Are two raw records plus updates to five existing owners justified, or is any concept delta duplicative, overlong, or better deleted? Do not propose new machinery where deletion or existing ownership suffices.
3. **Ownership and overlap** — Are lifecycle, orchestration, evaluation, grounded verification, and subagent guidance placed under their actual existing owners without conflicting duplicated rules?
4. **Fact vs inference** — Are Hermes mappings and recommendations explicitly marked `[推论]` or equivalently bounded? Check paragraph scope, not merely nearby headings.
5. **Wikilinks** — Do new/edited links resolve and represent justified relationships?
6. **Schema/index/log/hash** — Verify frontmatter, index/log consistency, and SHA-256 values against the exact committed raw blobs.
7. **Over-promotion and safety** — Confirm that source-specific thresholds, benchmark deltas, agent counts, harness architecture, technology choices, and control-plane proposals are not promoted to defaults or active-layer instructions.
8. **Necessity/minimality** — Name content that should be removed or shortened rather than expanded. Style preferences are not findings.

## Output contract

Return exactly these sections:

- `Verdict`: one of `APPROVE_LANDING`, `PASS_WITH_MINOR_FIXES`, `REQUEST_CHANGES`
- `Blocking`: severity-tagged findings, or `None`
- `Important`: severity-tagged findings, or `None`
- `Minor`: severity-tagged findings, or `None`
- `Passes`: criterion-by-criterion verified positives with committed `file:line` evidence
- `Recommended patches`: minimum bounded remediation for confirmed findings, or `None`

For every finding include `file:line`, impact, and recommendation. Do not claim a check passed unless you performed it. A process exit code is not review evidence.