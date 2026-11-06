---
title: Wiki health check runbook
created: 2026-05-11
updated: 2026-11-06
type: meta
status: current
---

# Wiki Health Check Runbook

## Summary

Use the repository-local scripts for deterministic structure, tag, catalog, public-boundary, provenance and raw-integrity checks. The scripts do not modify Agent runtime layers. Check-mode commands (`wiki_maintain.py --check`, `wiki_health_check.py`, `wiki_catalog.py --check`, `wiki_tag_audit.py`, `wiki_public_content_check.py` and `wiki_reverse_lookup.py`) are read-only; write modes (`wiki_maintain.py --fix`, `wiki_catalog.py`, `wiki_raw_hashes.py` and `wiki_maintain.py --install-hooks`) update only `_meta/catalog.json`, `_meta/raw-source-hashes.json` or the local Git pre-commit hook.

## Root resolution

All maintenance scripts resolve the repository root in this order:

1. explicit `--root`;
2. existing `OBSIDIAN_VAULT_PATH`;
3. the repository containing the script.

The fallback is independent of the caller's working directory and does not depend on a username. For isolation-sensitive work, pass `--root` explicitly and set `OBSIDIAN_VAULT_PATH` to the same clone.

## Core commands

### Safe metadata synchronization

Before any `wiki_maintain.py --fix` run:

1. Compare the current raw paths with `_meta/raw-source-hashes.json` and the pre-change working tree. Review additions and deletions against the authorized change; stop and investigate unexplained missing sources rather than treating them as cleanup.
2. Explain existing raw hash changes under `SCHEMA.md` before updating the manifest. `--fix` rejects changed existing hashes, but it removes manifest entries for raw files that no longer exist; it does not determine whether a deletion was authorized.
3. Run `--fix` only after that review, then read back the catalog and manifest diff against the pre-sync baseline. Confirm every added or removed entry is intended; this also applies when the working tree already contains uncommitted ingestion changes.
4. Run `--check` separately. A pass does not validate deletion intent or make lost source material recoverable; unresolved deletions must be resolved before accepting the maintenance result.

Use these same pre-write and diff-review conditions for direct catalog/raw-manifest writers below. Do not regenerate a baseline to silence an unexplained deletion or content drift.

### Commands

From the repository root:

```bash
WIKI_ROOT=/path/to/wiki

# 一键自动化质量门禁（单测、catalog.json、健康检查、标签审计、公开边界、git diff）：
python3 _meta/scripts/wiki_maintain.py --root "$WIKI_ROOT" --check

# 先完成上面的 raw 新增/删除授权审查；同步后回读清单差异，再单独 --check：
python3 _meta/scripts/wiki_maintain.py --root "$WIKI_ROOT" --fix

# 页面与局部断言的到期预警扫描（默认未来 30 天）：
python3 _meta/scripts/wiki_maintain.py --root "$WIKI_ROOT" --freshness --days 30

# 安装本地 Git pre-commit 钩子：
python3 _meta/scripts/wiki_maintain.py --root "$WIKI_ROOT" --install-hooks

# 单独调用细分工具：
python3 _meta/scripts/wiki_health_check.py --root "$WIKI_ROOT"
python3 _meta/scripts/wiki_health_check.py --root "$WIKI_ROOT" --format markdown
python3 _meta/scripts/wiki_catalog.py --root "$WIKI_ROOT" --check
python3 _meta/scripts/wiki_tag_audit.py --root "$WIKI_ROOT"
python3 _meta/scripts/wiki_public_content_check.py --root "$WIKI_ROOT"
python3 -m unittest discover -s _meta/scripts -p 'test_*.py' -v
git diff --check
```

`wiki_health_check.py` and `wiki_tag_audit.py` are read-only. `wiki_public_content_check.py` scans every repository file outside `.git` and `__pycache__`; it does not exempt code blocks, `raw/` or `_meta/`. Local `git diff --check` covers uncommitted changes; CI separately checks the event commit range so a clean checkout cannot hide whitespace errors already committed.

`wiki_maintain.py --check` preserves the health check's severity contract: P0/P1 fail, while P2 findings remain visible warnings. Public-content candidates are also reported for review without failing the check by themselves. A passing command establishes only the checks' coverage, not factual accuracy or completion of candidate review.

`--freshness` scans both page-level `review_by` and supported local `[!volatile]` deadlines, including claims on pages without a page-level deadline. Local results add `block` (one-based callout number, excluding code examples) and `source` in JSON; text output shows the block number. Page-level result fields remain unchanged. The due date is valid through that UTC day. The scan reports deadlines only; use `--check` for malformed metadata and review sources to establish factual currency.

## Local `[!volatile]` result contract

For each supported local block, `wiki_health_check.py` validates real `YYYY-MM-DD` values, `verified_at <= review_by`, non-future verification, expiry, and exact membership of the local `source` in page frontmatter `sources`. Unless a date is injected by the Python API for testing, date comparisons use the UTC calendar date.

- P1: malformed/unsupported block, malformed date, `verified_at` later than the UTC date, invalid date order, or undeclared local source.
- P2: `review_by` is earlier than the injected/current UTC date. The due date itself remains valid; expiry begins the next day.
- Multiple blocks are independent. Fenced, inline and indented code examples are ignored.
- A passing block validates only that claim scope. It does not set or refresh page-level `verified_at` and does not imply that the whole page is current.
- The block and page-level freshness fields remain optional. Existing pages are not required to add or refresh them.

Unsupported block syntax is reported rather than treated as success. The supported syntax is defined in `SCHEMA.md`.

## Freshness ownership and disposition

The repository maintainer owns the weekly review of the existing CI freshness summary; no new scheduler, notification recipient or per-page owner registry is required. A deployment with multiple maintainers must name its responsible reviewer in its own workflow. Agent authors do not automatically become accountable human reviewers.

Use `python3 _meta/scripts/wiki_maintain.py --root "$WIKI_ROOT" --freshness --days 30 --format markdown` for the same table locally. CI writes this table into the workflow summary. JSON adds `summary` counts for expired scopes, high-volatility expired scopes, expired local claims regardless of page volatility, approaching deadlines and missing high-volatility deadlines; page and local-claim scopes count separately. `volatility` describes the parent page, including on local-claim rows. A local block does not automatically mean `high`; the overlapping `expired_local_claims` count ensures expired local scopes remain visible on low/medium pages. High volatility is a triage signal, not a measure of business impact. The command stays advisory and does not turn every expired page into a blocking error.

Review high-impact operational claims first, then frequently reused methods. Resolve each reported scope in its existing page:

- **Verified:** check the relevant evidence, record who/what verified which scope and source version, then set a justified next deadline. A formatting edit cannot renew a deadline.
- **Pending:** preserve the deadline and explain the unresolved claim next to it. Under the retrieval Freshness Gate it cannot silently regain current-fact eligibility.
- **Retired:** correct the current entry point and explain the replacement or historical scope; `closed` alone does not prove that a replacement exists.

The two initial scoped-note examples are the [OKF assessment](../queries/okf-for-hermes-wiki-governance-assessment.md#scoped-verification-note) and [Flutter dependency transition](../concepts/flutter-version-evolution-and-platform-boundaries.md#scoped-verification-note). The latter confirms a published plan, retains the 2026-12-02 local deadline, and requires checking the actual transition; it is intentionally still visible in the approaching-deadline report. No human sign-off or SDK migration is inferred from these AI checks. Record reusable corrections in the normal log, not a separate personal task ledger.

## Bounded retrieval benchmark

`_meta/retrieval-benchmark.json` fixes Q1–Q8 questions and candidate gold sets before running any strategy. `wiki_retrieval_benchmark.py` compares full-text keyword matching, catalog metadata matching and bounded typed-relation candidates with the same page and evidence-byte limits. The relation strategy combines metadata seeds with typed expansion and full-text reranking; comparing it with metadata-only ranking does not isolate the benefit of relations. It does not invoke a model, authorize API spend, or install an Agent runtime. Procedures, baseline interpretation and limitations live in [the benchmark page](../queries/wiki-cross-source-evidence-navigation-benchmark.md).

```bash
# Write evaluation artifacts outside the public Wiki; replace this output directory as needed.
mkdir -p /tmp/wiki-retrieval-eval
python3 _meta/scripts/wiki_retrieval_benchmark.py --root "$WIKI_ROOT" --strategy keyword > /tmp/wiki-retrieval-eval/keyword.json
```

Repeat for `catalog` and `relations`. Each packet’s `input_sha256` identifies its run-level source-content union, not a per-case or full-protocol snapshot. Reordering cases does not change that union; running a subset may. Preserve packets, answers and the runner externally if retaining historical results; a fresh checkout cannot reconstruct a historical source snapshot from hashes alone. Never replace an old answer’s fingerprint with a new retrieval run’s fingerprint. Give an isolated answering session only each case's `id`, `question` and `evidence`, never gold sets, retrieval metrics or another run's answers. Save a JSON array of `{id, answer, citations}`; citations use the exact evidence IDs. Repeat with a fresh answering context, then validate:

```bash
python3 _meta/scripts/wiki_retrieval_benchmark.py --packet /tmp/wiki-retrieval-eval/keyword.json --answers /tmp/wiki-retrieval-eval/keyword-answers.json --repeat-answers /tmp/wiki-retrieval-eval/keyword-repeat-answers.json
```

This verifies citation identity and computes two-run fixed-packet citation Jaccard, with both-empty pairs reported as N/A. It does not grade factual support or answer completeness. Read the cited spans separately; record missing answer requirements and unsupported claims even when every ID is valid. The byte count covers the serialized evidence records, not prompt framing, model tokens or network cost. The candidate graph is an experimental retrieval strategy, not an implementation of the full production Freshness Gate.

## Public-content result contract

- **Violation**: deterministic public-boundary failure; the command exits `1`.
- **Candidate**: possible personal instance record that needs content review; candidates do not fail the command by themselves.
- **PASS**: no blocking rule matched. It does not mean candidates were adjudicated, attachments were reviewed, or the repository is absolutely safe.
- Reports contain only repository-relative paths and rule names, never matched values.
- Files containing NUL bytes and files that do not decode as UTF-8 are candidates marked `unreviewed-binary-or-non-utf8`; they cannot be counted as reviewed until inspected with an appropriate tool.
- Generic product paths, configurable examples and obvious credential placeholders are allowed. A synthetic example does not prove deployment or authorization.
- **Baseline candidate adjudication (2026-11-06)**: The local scan returned 14 non-blocking candidates across 12 files: 11 tracked Markdown pages plus the ignored `.lycheecache`. Content review found public bibliography URL paths in `concepts/entropy-and-entropy-increase.md` and `.lycheecache` (2 candidates); public-boundary exclusions in `SCHEMA.md`, `concepts/agent-experience-consolidation-loops.md`, `concepts/household-fund-layering-model.md`, `concepts/investment-risk-control-framework.md`, `concepts/wiki-ingestion-workflow.md` and `operations/agent-shared-wiki-index.md` (8); and reusable investment examples or self-checks in `concepts/leontraveller-trading-and-investment-system.md` and the three query pages `losing-position-review-method`, `position-sizing-method` and `pre-trade-risk-checklist` (4). These reviewed matches contain no personal instance records; disclaimers alone are not evidence of safety. This is a local scan snapshot, not a portable tracked-file baseline: ignored cache contents can differ between checkouts. Keep the conservative scanner unchanged without path allowlists; re-adjudicate when matched content changes, even if the candidate count and paths remain unchanged.

## Reverse lookup

```bash
WIKI_ROOT=/path/to/wiki
python3 _meta/scripts/wiki_reverse_lookup.py --root "$WIKI_ROOT" --source raw/articles/example.md
python3 _meta/scripts/wiki_reverse_lookup.py --root "$WIKI_ROOT" --page concepts/example.md
```

Modes are mutually exclusive. Source mode returns direct formal-page paths; page mode returns sorted `declared_by`, `relation`, `target` records. Empty matches return `[]`; unreadable or malformed input exits `2` with an error on stderr and no success result on stdout.

## Raw hash manifest

`_meta/scripts/wiki_raw_hashes.py` writes `_meta/raw-source-hashes.json`. Run it after adding an approved public raw source. A changed existing hash is a finding to explain, not noise to regenerate away.

A public-boundary remediation may remove private metadata from raw or delete an ineligible raw file. Record a non-personal reason in `log.md`, verify that the manifest diff is limited to the declared files, then commit content and manifest together.

```bash
python3 _meta/scripts/wiki_raw_hashes.py --root "$WIKI_ROOT"
```

## External-link check

`_meta/scripts/wiki_link_check.sh` uses `lychee` and the repository's `_meta/lychee.toml`. It needs network access and is separate from deterministic health checks. The weekly scheduled CI workflow also runs it as a separate `external-links` job (lychee pinned in `.github/workflows/wiki-checks.yml`); inspect failed requests to distinguish dead links from network restrictions, rate limits or temporary service failures. The current configuration accepts HTTP 429 to avoid blocking on rate limits, so a passing run does not establish every URL's liveness. Install a supported `lychee` version through the operator's package or release-verification process; the repository does not claim a machine-local installation.

Both entrypoints cover `entities/`, `concepts/`, `queries/`, `comparisons/` and `operations/`.

```bash
_meta/scripts/wiki_link_check.sh --root "$WIKI_ROOT"
```

Extra arguments are passed through to `lychee`.

## Minimal CI

`.github/workflows/wiki-checks.yml` runs on pull requests and pushes to `main` with read-only repository permission. It uses only repository scripts and the Python standard library:

1. unit tests;
2. Wiki health check;
3. catalog synchronization check (`wiki_catalog.py --check`);
4. tag audit;
5. public-content check;
6. `git diff --check` over the pull-request merge base or pushed commit range.

The deterministic job does not use secrets, `pull_request_target`, write permissions, metadata/raw-hash writers, network link checks or AI review. The whitespace step runs only for push and pull_request events because it needs a commit range. External-link liveness is network-dependent, so it runs in a separate `external-links` job on the weekly schedule or manual dispatch only, and as the operator command above.

## Exit codes

For the Python checks:

- `0`: check completed and no blocking finding exists;
- `1`: check completed and found a blocking violation;
- `2`: CLI or runtime error.

## Health-check scope

The structural health check covers core files, frontmatter, type/status/tag enums, wikilinks, relative Markdown links, index coverage, semantic inbound links, log order, raw references, raw hashes, duplicate-page signals, freshness metadata and Relations syntax. It does not replace content review for public suitability, source quality, contradictions or current product behavior.

Index coverage recognizes both wikilinks and standard relative Markdown links in `index.md` and its explicitly linked `_meta/topic-index.md`; an unlinked topic directory does not establish coverage. Administrative navigation links do not count as semantic inbound links from another formal page. Catalog relations still come only from explicit `## Relations`; ordinary navigation links are not inferred as typed relations.

## Content-change readback

After changing governance content, read the changed passages and their direct quick paths, templates and examples. A disclaimer at the top does not repair a contradictory instruction below. In particular:

- Keep template dates as placeholders; edit actual page metadata only in its opening frontmatter, without changing fenced examples or historical verification dates.
- Check the log header and format example separately from real dated entries; confirm index descriptions match the revised pages.
- Check evidence scope, public intake and optional capabilities in both full rules and abbreviated routes.
- Report deterministic checks, semantic review and independent-review coverage separately. A focused re-review only clears its named findings.

Before an authorized commit or publish, inspect effective Git hooks and invoked scripts for cross-repository writes, pushes or deployment triggers. Wiki editing permission alone does not authorize those effects; establish the exact authorized scope before running the trigger.

## Related

- [[hermes-wiki-lint-and-health-check-standards]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
