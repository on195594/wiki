# Independent Pi review prompt

- Target commit: `7c5fc75c35308b88159777c86fc83d59703cf64c`
- Reviewer: Pi CLI
- Mode: read-only (`read,grep,find,ls`)
- Working copy: detached exact-commit worktree

# Independent Pi review: wiki ingestion commit 7c5fc75c35308b88159777c86fc83d59703cf64c

You are an independent read-only reviewer. Review the detached worktree at the exact commit above. Do not edit files and do not assess unrelated later working-tree changes.

## Scope

Commit message: `wiki: ingest multi-agent context handoff article`

Changed allowlist:
- `_meta/raw-source-hashes.json`
- `concepts/agent-context-engineering.md`
- `concepts/subagent-orchestration-patterns.md`
- `index.md`
- `log.md`
- `raw/articles/langchain-organizing-context-multi-agent-harness-2026-09-08.md`

Read all six files. Compare the two concept-page additions directly with the raw source. Check line-number evidence in the current detached worktree.

## Rubric

1. Source fidelity: every article-attributed claim must have a concrete raw-source anchor; inspect raw head and tail and test whether the declared extraction scope is accurate.
2. Smallest durable unit and ownership: raw/source vs concept vs index/log are correctly separated; no unnecessary new concept/workflow.
3. Fact vs inference: framework mapping and recommendations not stated by the article must be visibly marked `[推论]` or equivalently delimited so they cannot be read as source facts.
4. Hermes accuracy: do not accept claims about current `delegate_task`, runtime fork support, permissions, memory, or caching unless the commit itself can substantiate them; classify unsupported operational claims.
5. Wikilinks and schema/index/log: targets exist, frontmatter and source hash are consistent, index count/date and log claims are accurate.
6. Over-promotion: wiki-only material must not imply that active Skill/runtime behavior was changed.
7. Economy: prefer deletion or the smallest bounded fix; do not request a new abstraction, workflow, or active-layer change unless necessary.

## Output

Start with exactly one verdict: `APPROVE_LANDING`, `PASS_WITH_MINOR_FIXES`, or `REQUEST_CHANGES`.

Then list findings in severity order. For every finding provide:
- severity and stable ID (for example `P1-F1`)
- `文件:行号`
- impact
- exact smallest remediation

Include one short section for each rubric criterion, even if it passes. End with a one-line go/no-go conclusion. Do not modify anything.
