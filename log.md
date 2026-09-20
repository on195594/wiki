# Wiki Log

> Chronological record of wiki actions.
> Format: `## [YYYY-MM-DD] action | subject`

> Historical entries before 2026-09-01: [_meta/log-archive/2026.md](_meta/log-archive/2026.md)

## [2026-09-20] governance | Wiki audit remediation
- Reordered all 253 log entries into descending date order without changing entry content, then moved 224 entries before 2026-09-01 to `_meta/log-archive/2026.md` while retaining them verbatim.
- Added `## Summary` to the eight formal pages identified by the governance audit, refreshed `updated` metadata on all touched formal pages, and linked `concepts/local-first-sync-confirmed-mirror-outbox-conflict-policy.md` from its lifecycle owner.
- Hardened `wiki_health_check.py` to detect missing Summary sections, semantic orphan/index-only formal pages, out-of-order log dates, and symlinked roots; added regression coverage.
- Applied the independent AGY findings by excluding administrative log/index links from semantic inbound analysis, resolving programmatic roots canonically, registering the log archive role in `SCHEMA.md`, and adding archive navigation back to `log.md`.
- Updated `index.md`'s maintenance date and aligned the lint standard and health-check runbook with the new checks.
- Validation: 29 unit tests passed; Wiki health P0/P1/P2=0/0/0; tag audit passed; `git diff --check` passed.
- Boundary: Wiki governance and validation tooling only; raw sources, runtime layers, active skills, memory, cron, MCP and external services were unchanged.

## [2026-09-16] runtime remediation + dashboard refresh | Hermes health baseline
- Replaced the stale v0.10 baseline with live `v0.21.3 [fb56a7e0]` evidence covering gateway, six Cron jobs, Memory, browser, session store, backup/restore and remaining host/dependency risks.
- Installed Playwright Chromium/headless-shell 1217 and passed a local browser smoke. The first real Amazon run returned `source_status=ok` for 10/10 products but its trigger owner timed out before durable completion; a second complete trigger then recorded Cron `completed`, job `Last run: ok`, and 10/10 successful product observations with no repeated price alert.
- Compressed `USER.md` from 1350 to 843 chars; offline-deleted 513 unrouted stale open Telegram sessions after a verified SQLite snapshot, then optimized `state.db` from 1053.2 MB to 655.9 MB with integrity checks and a clean gateway restart.
- Restored `updates.pre_update_backup: quick`; added monthly dual-repository restic verification and quarterly isolated restore-drill timers. Both services were run immediately and passed for `jedi` and `wiki`, including restored SQLite quick checks.
- Updated the local safe-update script to stop the gateway through `hermes gateway stop`, preserving the planned-stop marker; upstream #108219 and #42517 remain open, and no forced dependency upgrade was applied.
- Boundary: host SSH/firewall/public-port hardening and terminal/backend isolation remain unresolved; the dashboard records them but this Wiki write does not authorize or implement those changes.

## [2026-09-15] independent Pi review repair | Organizing Context in a Multi-Agent Harness
- Pi reviewed exact commit `7c5fc75c35308b88159777c86fc83d59703cf64c` read-only and returned `REQUEST_CHANGES` with `P1-F1` and `P2-F2`; prompt, raw output and matching before/after hashes are stored under `_meta/reviews/2026-09-15-organizing-context-7c5fc75-pi-review*`.
- Removed unsupported assertions about current `delegate_task` context/fork semantics and stated the bounded-handoff guidance without assuming a literal Hermes fork.
- Corrected extraction provenance to distinguish omitted image contents from the two retained empty-alt image links; refreshed the raw-source hash manifest.

## [2026-09-15] ingest + existing-owner update | Organizing Context in a Multi-Agent Harness
- Captured `raw/articles/langchain-organizing-context-multi-agent-harness-2026-09-08.md` with authors/date, the full substantive public article body, extraction provenance, local summary pointer and vendor-evidence limitations.
- Updated existing owners `concepts/agent-context-engineering.md` and `concepts/subagent-orchestration-patterns.md`; no duplicate concept page or new workflow was created.
- Preserved the role-aware handoff rule: continuation workers receive bounded verified evidence, while independent reviewers and self-contained researchers receive clean task contracts without the parent's conclusion. This Wiki change added no fork behavior and did not verify `delegate_task` runtime context semantics.
- Boundary: Wiki-only ingestion. Prompt-cache savings remain source-specific; no Memory, active Skill/reference, runtime/config, Cron, MCP, gateway, wrapper, provider, profile/plugin or permission policy changed.

## [2026-09-15] ingest + existing-owner update | LangChain Paid Media Agent
- Captured `raw/articles/langchain-paid-media-agent-2026-09-13.md` as a structured record of the complete public article, including its reported performance figures, metric-level authority rules, progressive tool discovery, shared-state failures, approval/readback path and vendor-evidence limitations.
- Updated existing owners `concepts/agent-context-engineering.md` and `concepts/subagent-orchestration-patterns.md`; no duplicate concept page was created.
- Preserved the reusable deltas: deterministic computation before model judgment, authority by metric, progressive tool disclosure, and isolation of each subagent's writable paths, lifecycle state and mechanical completion condition.
- Boundary: Wiki-only ingestion. The article's business and efficiency figures remain self-reported; no Memory, active Skill, runtime/config, sandbox provider, MCP, Cron, gateway, campaign integration or production write path changed.

## [2026-09-09] governance repair | Knowledge freshness v2 post-review contracts
- Established `block source ⊆ page sources`: page-level `sources` remains canonical provenance and the sole deterministic entry for source reverse lookup/invalidation; a local `[!volatile]` source is claim attribution and cannot be the page's only source record.
- Aligned `review_by` validation language across Schema, page-writing standards, lint/health standards, runbook, and existing `is_formal_page()` behavior; no validator or reverse-lookup code changed.
- Validation: 23 unittests passed; Wiki health P0/P1/P2=0/0/0; all three real volatile sources reverse-resolved to their owner pages; `git diff --check` passed; raw and hash manifest were unchanged. Independent read-only review returned `APPROVE_LANDING` with no blocking findings.
- Boundary: no claim parser, persistent index, database, Freshness Engine, runtime/active-layer change, or historical metadata migration was added.

## [2026-09-09] fix | Knowledge freshness review findings
- Made reverse-lookup commands independent of the caller's working directory across the shared entry, retrieval and ingestion contracts, and runbook.
- Preserved commas in block-list and quoted inline source values so exact dependency lookup cannot silently split a source identifier.
- Kept visible nested-list wikilinks in health checks while continuing to ignore actual indented code; 23 regression tests pass and Wiki health remains P0/P1/P2=0/0/0.

## [2026-09-09] implement | Knowledge freshness architecture v2
- Added optional volatility/verified_at validation and deterministic source/relation reverse lookup; synchronized Schema, template, writing/health standards, shared entry, retrieval and ingestion contracts. Freshness is evaluated per scope, with incoming supersession/conflict checks and live-evidence priority.
- Piloted local claim verification on Claude/Codex workflow and Hermes harness pages; only actually checked claims received dates. Preserved historical runtime context and all raw sources.
- Regression: 22 unittest tests pass; Wiki health P0/P1/P2=0/0/0. Codex/AGY completed the 15-case set with a focused retest clarifying unattempted versus failed verification; Hermes representative fresh-session probes passed. Claude could not run due to expired authentication; the user waived this acceptance item on 2026-09-09. It is not recorded as a successful probe; no credentials or global configuration changed.
- Evidence and remaining acceptance are recorded in `_meta/plans/2026-09-09-knowledge-freshness-architecture-v2.md`; independent AGY re-review returned PASS with no blockers after fixing the log header insertion. The user authorized closing the plan with the Claude waiver, committing and pushing the changes.

## [2026-09-06] ingest + existing-owner update | Solving the right problem before agentic implementation
- Captured Mike Huls's Towards Data Science article in `raw/articles/towardsdatascience-right-problem-agentic-ai-2026-09-03.md` with author/date, full Karakeep body, local summary path, and explicit practitioner-evidence limitations.
- Updated the existing owner `concepts/hermes-ai-workflow-formalization-principles.md`: allocate preflight validation effort by decision reversal cost; prefer evidence, user confirmation, real samples, or a minimal Spike over six mandatory documents.
- Preserved the small-task Direct path and rejected a new Skill, project pilot, fixed six-document workflow, default multi-Agent review, hard gate, Memory entry, runtime/config, Cron, MCP, Gateway, wrapper, provider, or plugin change.

## [2026-09-06] review | Reverse Engineering Linear's Sync Engine (`6ea1d94`)
- Pi `0.84.4` independently reviewed commit `6ea1d9488b2ef6d51bc5b0afd364679da781a049` using read-only file tools and returned `APPROVE_LANDING` with no findings.
- Parent verification accepted the declared eight-line callout omission and one trailing-space cleanup as bounded provenance exceptions; no content repair was warranted.
- Preserved the exact prompt, reviewer result, target hashes, reviewer limitation, and parent disposition under `_meta/reviews/`.

## [2026-09-06] ingest + concept | Reverse Engineering Linear's Sync Engine
- Preserved a substantially complete browser-rendered README text capture in `raw/articles/reverse-linear-sync-engine-2026-09-06.md`, with provenance, CC BY 4.0 attribution, omitted-image/link and 8-line callout limitations, one documented whitespace normalization, reverse-engineering limits, implementation-drift warning, and an explicit no-active-layer boundary.
- Added `concepts/local-first-sync-confirmed-mirror-outbox-conflict-policy.md`: distilled confirmed mirror + durable outbox + optimistic view, cursor advancement, replay/idempotency, explicit conflict policy, lazy hydration, and transactional undo/redo.
- Mapped the pattern to existing chat/session routing and future Desktop or recoverable-agent specs without changing Memory, active Skills, runtime/config, Cron, MCP, Gateway, plugins, or production behavior.

## [2026-09-06] independent review | commit a6584cd agent collaboration and harness evidence
- AGY `1.1.27` with `Gemini 3.1 Pro (High)` returned `APPROVE_LANDING` with no content findings for exact commit `a6584cd3784a1642a450de60167978ccbdef77c4`.
- Parent verification confirmed both raw-source hashes, inference markers, Wiki health, whitespace checks, source-link targets, and no active-layer changes. Favorable reviewer overclaims were narrowed in the preserved report.
- The reviewer violated the read-only instruction by creating eight untracked temporary patch files. Parent removed only those files; exact target hashes remained unchanged. No source patch was warranted.

## [2026-09-06] update | The New Stack on evidence for trustworthy agentic RAG
- Captured raw source: `raw/articles/thenewstack-building-trust-agentic-rag-2026-09-05.md` (Jeremy Daly, 2026-09-05); the page explicitly identifies Oracle as sponsor.
- Updated canonical owner: `concepts/llm-context-engineering-layer.md`; updated its existing `index.md` entry instead of creating a near-duplicate concept page.
- Durable delta: retain replayable retrieval decisions, enforce identity/scope/currency before similarity ranking, map claims to supporting excerpts, and treat retrieved content as untrusted data rather than policy.
- Evidence boundary: the source provides no public benchmark, production incident record, or independent comparison; Oracle AI Vector Search remains a vendor example, not a Hermes selection decision.
- Boundary: wiki-only update; no memory, active skill/reference, project, config, cron, MCP, runtime, wrapper, gateway, profile/plugin, credential, or Hermes core change was made.

## [2026-09-06] review + fix | AGY review of agentic RAG trust-boundary ingestion
- Reviewed commit: `ef4c25a` (`wiki: capture agentic RAG trust boundaries`). Prompt: `_meta/reviews/2026-09-06-agentic-rag-trust-boundary-agy-review-prompt.md`; result: `_meta/reviews/2026-09-06-agentic-rag-trust-boundary-agy-review.md`; AGY `1.1.27`; model `Gemini 3.1 Pro (High)`; exit `0`.
- AGY verdict: `APPROVE_LANDING`; no blocking, important, or minor findings. Parent verification accepted the source, hash, links, schema/index/log, minimality, and active-layer boundary passes.
- Parent calibration found one P3 evidence-label gap not caught by AGY: locally reusable design rules and the Hermes owner mapping were not explicitly marked `[推论]`. Added two group-level labels without changing behavior or source claims.
- Scope integrity: exact pre/post commit-blob and prompt SHA-256 manifests match (`NO_DRIFT`). Final parent verdict: `PASS_WITH_MINOR_FIXES`.
- Boundary: review and fix are wiki-only; no memory or active Hermes surface changed.
## [2026-09-05] ingest + existing-owner update | The Harness Playbook
- Captured `raw/articles/stencil-the-harness-playbook-2026-09-05.md` with URL, capture date, structured-capture limitation, local summary path, source claims, Hermes inferences, and non-adoption boundaries; publisher author, date, title, and section structure were independently checked on 2026-09-06.
- Updated existing owners `concepts/agent-development-lifecycle.md` and `concepts/stateful-agent-environments-and-grounded-verification.md`; added the harness as a stateful execution boundary, authoritative-state/readback rules, control-plane versus execution-plane separation, bounded job lifecycle requirements, and explicit evidence limits.
- Kept the article out of Memory, active Skills, runtime/config, MCP, Cron, gateway, provider, and new projects. No new workflow was created.

## [2026-09-04] ingest + minimal existing-owner update | Nature multi-agent collaboration study
- Captured `raw/articles/nature-capable-language-models-can-outgrow-the-benefits-of-collaboration-2026.md` as a structured evidence record; verified publisher metadata and retained links to the paper, preprint, code, archive, and local summary.
- Updated existing owners `concepts/subagent-orchestration-patterns.md`, `concepts/agent-orchestration-production-tradeoffs.md`, and `concepts/production-ai-agent-evaluation-framework.md`.
- Landed the slimming rule: establish a single-agent baseline and genuine task decomposability before adding multi-agent coordination; measure coordination cost and correlated errors; do not promote source-specific thresholds to Hermes defaults.
- No new Skill, memory, runtime route, MCP, Cron, router, pool, team, or evaluation platform was created.

## [2026-09-03] governance | Phase 3 P2 long-term architectural optimization
- Converged 55 legacy Reconciliation Tags: across 35 formal pages, mapped all single-use and non-curated tags into the canonical 51-tag taxonomy (14 Core + 23 Domain + 14 Facet); reduced distinct tags from 101 to 47 and single-use tags from 50 to 3.
- Retired Reconciliation Tags section in `SCHEMA.md`: formally closed the temporary reconciliation tag registry from 2026-08-11; all formal pages now strictly adhere to curated Core/Domain/Facet taxonomy.
- Topology weaving for 15 isolated formal pages: connected all 15 zero-in-degree pages (`agent-shared-wiki-index`, `multiagent-systemic-failure-modes`, `hermes-active-surface-lifecycle-governance`, etc.) into their respective concept hubs and query records; zero-in-degree pages reduced from 15 to 0.
- Verification: `wiki_health_check.py` passed (P0=0, P1=0, P2=0); `wiki_tag_audit.py` passed (47 unique tags, 0 undeclared); `test_wiki_health_check.py` passed (13/13); `git diff --check` passed.

## [2026-09-03] governance | Phase 2 P1 semantic rules and health check hardening
- Hardened `_meta/scripts/wiki_health_check.py`: added P1 check for non-markdown review sidecar files in `_meta/reviews/`; added P2 check for `## Relations` syntax format and key whitelist (`ALLOWED_RELATION_KEYS = {"depends_on", "refines", "conflicts_with", "supersedes", "related"}`).
- Updated `SCHEMA.md` and `_meta/wiki-health-check-runbook.md`: formally included `related` in the Relations specification; documented the new review sidecar (P1) and Relations (P2) validation rules in severity policy.
- Normalized formal page Relations: cleaned non-standard keys (`indexed_by`, `category`, `source*`, `extends`, `related_to`, `informs`, `evidence`) across 14 pages (including the software-engineering-laws suite), achieving 100% compliance across all 68 pages with Relations (229 valid relation lines).
- Fixed `operations/hermes-health-dashboard.md`: updated `type` from `concept` to `operation`, populated valid `sources`, and updated freshness timestamp.
- Expanded regression tests: added 5 new unit tests in `_meta/scripts/test_wiki_health_check.py` covering illegal sidecar (recursive), unregistered relation key, invalid relation format, and invalid relation value; all 13 tests pass.
- Verification: `wiki_health_check.py` passed (P0=0, P1=0, P2=0); `test_wiki_health_check.py` passed (13/13); `wiki_tag_audit.py` passed (0 undeclared); `wiki_link_check.sh` passed (0 dead links); `git diff --check` passed.

## [2026-09-03] governance | Phase 1 P0 tool and environment remediation
- Fixed `_meta/scripts/wiki_tag_audit.py`: added formal page filtering to exempt `raw/`, `_meta/` and root core files per SCHEMA.md line 98; audit exit code returned from 1 to 0 (0 undeclared tags on formal pages).
- Cleaned `_meta/reviews/`: removed 46 illegal non-markdown sidecar files (.exit, .stderr, .sha256, .txt) violating SCHEMA.md line 249; git-staged deletions.
- Restored external link check dependency: verified and installed prebuilt `lychee` v0.24.2 (archive SHA-256 `5d0b0e3aeab240f41920c633a6eaf97599be6eedda034b36e858ede7dba5e535`, binary SHA-256 `29bc0ac5c5ac3cfe9c312a5783a94f8fca33118d1a7bb687323eab0b52735f79`) to `~/.local/bin/lychee` per runbook; added PATH prepend in `_meta/scripts/wiki_link_check.sh`.
- Full verification: `wiki_health_check.py` passed (P0=0, P1=0, P2=0); `wiki_tag_audit.py` passed (0 undeclared); `test_wiki_health_check.py` passed (8/8); `wiki_link_check.sh` passed (99 checked, 0 errors).
- Boundary: Tooling and environment remediation only. No formal page content or runtime/active layer modified.

## [2026-09-03] ingest + minimal executable landing | GitHub Copilot task-level efficiency
- Captured the official GitHub Blog article at `raw/articles/github-copilot-cost-efficient-coding-2026-09-02.md`, preserving authors, publication date, full extracted body, source URL, extraction route and the vendor/workload-specific evidence limitation.
- Updated existing owners `concepts/loop-engineering-hermes-agent-workflow.md` and `concepts/hermes-context-engineering-design-priorities.md`; no duplicate concept, Skill, runtime or telemetry service was created.
- Added the reusable rule to optimize completed-task cost rather than isolated tool-call tokens; preserve source-like output, use lossless search reshaping, treat recovery/retry signals as compression evidence, test Prompt behavior, and avoid background-result retrieval detours.
- Minimal executable landing reused the existing read-only `scripts/gsummary-status.py` and recorded the 2026-09-03 baseline: 901 total records, 867 summary records, 835 real-summary successes; summary status 840 ok / 21 timeout / 6 error. This is not yet task-level cost telemetry.
- Boundary: Wiki and read-only project observation only. No memory, active Skill/reference, project implementation, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin or external service changed.

## [2026-09-02] ingest | Warp file-based self-improving Agent Skills loop
- Captured Michael Segner's Anthropic/Warp customer case at `raw/articles/claude-warp-self-improving-agent-skills-2026-08-26.md` as a clearly labeled structured capture, preserving every substantive section and finite list, author/date, public-page and Karakeep cross-check, six Skill-writing recommendations, issue-triage example and evidence limitations.
- Updated the existing owner `concepts/agent-experience-consolidation-loops.md` rather than creating a duplicate concept: added the Base Skill → in-workflow human feedback → Improver Skill → reviewed PR implementation pattern.
- Preserved the corrected knowledge-evolution boundary: self-improvement may add, delete, replace, merge, move, split, retire or keep; the article does not authorize append-only rule growth, unattended Skill mutation or scheduled Active publication.
- Evidence boundary: Warp and usage figures are company/vendor-reported, and the article provides no controlled accuracy gain, bad-edit rate, review-cost measurement or long-term regression evidence.
- Boundary: Wiki-only ingestion. No memory, active Skill/reference, project/pilot, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency or external service changed.

## [2026-09-02] review | AGY review of SKILL.state Wiki and active workflow
- AGY `1.1.23` using `Gemini 3.1 Pro (High)` returned `PASS`; blocking findings: none; stderr empty; exit code `0`.
- Review evidence: `project:/home/lin/.hermes/projects/skill-governance-evidence/docs/reviews/2026-09-02-skill-state-agy/` preserves the exact prompt, JSON response, stderr, exit status and before/after hashes.
- Parent hash guard confirmed `NO_DRIFT` across all 10 reviewed Wiki, active Skill/reference/index and integrity-manifest targets. The review remained read-only.
- AGY accepted source-claim boundaries, existing-owner placement, explicit trigger/skip conditions, append-only audit evidence, permission/rollback/exact-target-readback gates, and the explicit denial of cross-turn `execute_code` durability.
- Accepted fixes: `0`; no new Skill, validation project, runtime/config, persistence service, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency or external service was added.

## [2026-09-02] ingest + active workflow | SKILL.state explicit long-horizon execution state
- Captured a full-paper evidence packet at `raw/papers/arxiv-2608-26263-skill-state.md`, preserving the runtime equations, schema/patch ownership, SkillExecBench and public-benchmark results, open-weight failure taxonomy, sufficient-statistic assumption and explicit non-applicability boundaries.
- Updated the existing owners `concepts/agent-context-engineering.md` and `concepts/hermes-context-layer-operating-rules.md` rather than creating a duplicate formal concept: long-horizon model input is now framed as immutable contract + validated current state + latest observation, while evidence and trajectory remain external audit/recovery assets.
- Updated active `skill:autonomous-ai-agents/dynamic-workflow` with one trigger-bounded reference, `references/explicit-state-long-horizon-execution.md`; deterministic code owns patch validation, merge, rollback, permission gates and side-effect readback. Short calls, dynamic schemas, delayed-relevance tasks, trajectory-defined outputs and unresolved concurrent writes explicitly skip or hybridize the pattern.
- No validation project was created. This is a bounded L1 active-workflow change; it does not add a persistence service, change Hermes runtime/config, make `execute_code` durable, or relax any approval boundary.
- Backups: `/home/lin/wiki-backups/20260902-080644-skill-state/` and `/home/lin/.hermes/backups/skills/20260902-080644-skill-state/`; rollback removes the active reference/pointer and restores the backed-up owner files and integrity manifest.
- Verification: raw hash manifest added exactly one source with no existing drift; Wiki health passed with P0/P1/P2 all zero; 8/8 health-check tests, `git diff --check`, targeted explicit-state smoke and all 128 governed active-skill contract checks passed. Pre-existing validator warnings outside this change remain unchanged.

## [2026-09-02] ingest | Agentic Resource Discovery (ARD) discovery layer
- Captured raw source: `raw/articles/thenewstack-ard-agent-discovery-specification-2026-08-31.md` from The New Stack (Amanda Caswell, 2026-08-31); it records a secondary-source summary and extraction limits.
- Updated canonical owner: `concepts/ai-agent-tool-selection-architecture.md`.
- Durable delta: distinguish federated capability discovery from local availability/admission, then retain candidate reduction, selection, execution, and fallback as separate downstream decisions.
- Evidence boundary: ARD is an early draft described by secondary reporting; no claim of Hermes need, interoperability, security, or performance was made.
- Boundary: wiki-only ingestion; no memory, skill/reference, project pilot, config, cron, MCP, runtime, wrapper, gateway, profile/plugin, credential, or core change was made.

## [2026-09-02] review + fix | AGY review of ARD wiki ingestion
- Review prompt: `_meta/reviews/2026-09-02-ard-wiki-ingestion-agy-review-prompt.md`; result: `_meta/reviews/2026-09-02-ard-wiki-ingestion-agy-review.md`; exit: `0`; verdict: `PASS_WITH_MINOR_FIXES`.
- Independent review reported no blocking or important findings. Parent verification confirmed both cited minor issues.
- Accepted fixes (2): aligned the canonical page `description` with the discovery layer, and relabeled raw-note links so the canonical owner is distinct from adjacent concepts.
- Boundary: review and fixes remain wiki-only; no active layer changed.

## [2026-09-01] review | AGY review of WikiSkill ingestion
- Review prompt: `_meta/reviews/2026-09-01-wikiskill-ingestion-agy-review-prompt.md`; result: `_meta/reviews/2026-09-01-wikiskill-ingestion-agy-review.md`; AGY `1.1.23` verdict: `PASS`.
- Blocking: `0`; Important: `0`; Minor: `0`; recommended patches: none. Parent independently checked the paper's main-result, transfer and ablation evidence and accepted fixes: `0`.
- Reviewer remained read-only. Final Wiki health, regression tests, diff check and Git commit are owned by parent Hermes.
- Boundary: review records and `log.md` only; no active Skill/reference, memory, project/pilot, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency or external service was changed.

## [2026-09-01] ingest | WikiSkill persistent knowledge and reversible Skill evolution
- Captured the full-paper evidence packet at `raw/papers/arxiv-2608-27454-wikiskill.md`, preserving architecture, role boundaries, five-benchmark/five-model results, persistent-Wiki ablation, cross-model positive/negative transfer and source limitations.
- Updated the existing owner `concepts/agent-experience-consolidation-loops.md` rather than creating a duplicate concept or Skill: separated immutable evidence, persistent compiled knowledge and reversible Skill state, and retained rejected proposals as evidence rather than active instructions.
- Added one `OPTIONAL_REFERENCE` candidate only: for diagnostic Skill-evolution rollouts, compare Skill-only versus Skill+Wiki actor access under a frozen local A/B before considering default guidance; ordinary production knowledge retrieval is explicitly out of scope.
- Refreshed the existing `index.md` description. Backups: `/home/lin/wiki-backups/20260901-224450-wikiskill/`.
- Verification: raw hash manifest added exactly one source with no drift in existing raw files; Wiki health passed with no P0/P1/P2 findings; 8/8 health-check unit tests and `git diff --check` passed.
- Boundary: Wiki knowledge only. No active Skill/reference, memory, project/pilot, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency or external service was changed.

## [2026-09-01] ingest + optional workflow adoption | Context engineering for data-science agents
- Captured Piero Paialunga's Towards Data Science article at `raw/articles/towardsdatascience-context-engineering-data-scientists-2026-08-30.md`, preserving the full substantive body, author/date, Karakeep extraction provenance and practitioner-evidence limitations.
- Updated `concepts/agent-context-engineering.md` with project-mode declarations, bounded on-demand Skill decomposition, explicit context artifacts and supervised low-risk context maintenance; replaced the prior blanket project-validation deferral with the current risk-tiered optional-reference path.
- Adopted one bounded optional pattern in `skill:hermes-knowledge-and-workflow-governance/references/explicit-local-context-files-for-agent-memory.md`; reused the existing `skill-slimming-refactor-governance` owner instead of duplicating its Skill-decomposition rules.
- Active-reference backup: `/home/lin/.hermes/backups/skills/20260901-103419-hermes-context-files/explicit-local-context-files-for-agent-memory.md`. `skill_manage` was blocked by an unrelated pre-existing scanner finding elsewhere in the Skill, so the exact authorized reference was patched through the active-layer fallback; the canonical validator and targeted trigger/skip/boundary assertions passed.
- Boundary: no new concept, Skill, project, dependency, memory, cron, MCP, runtime, gateway, wrapper, provider, profile/plugin, credential or external service was created or enabled.

## [2026-09-01] review-fix | AGY review of Context Development Lifecycle ingestion
- Review prompt: `_meta/reviews/2026-09-01-context-development-lifecycle-agy-review-prompt.md`; result: `_meta/reviews/2026-09-01-context-development-lifecycle-agy-review.md`; AGY `1.1.22` verdict: `PASS_WITH_MINOR_FIXES`.
- Accepted one Minor fix after parent readback confirmed it: updated the existing `index.md` header date from `2026-08-30` to `2026-09-01`; indexed-page count remains `115` because no new formal page was created.
- Blocking: `0`; Important: `0`; rejected findings: `0`. Reviewer remained read-only; no source, concept, active layer or runtime behavior was changed by AGY.
- Boundary: wiki-only review and metadata correction. No memory, active skill/reference, project, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency or external service changed.

## [2026-09-01] ingest | Context Development Lifecycle for agent context assets
- Captured Ankit Jain and Patrick Dubois's sponsored The New Stack article at `raw/articles/thenewstack-agent-context-development-lifecycle-2026-08-31.md`, preserving the full main body, provenance, Karakeep/public-page cross-check and evidence limitations.
- Updated the existing owner `concepts/agent-development-lifecycle.md` rather than creating a duplicate CDLC concept or skill: mapped Generate → Evaluate → Distribute → Observe onto Build → Test → Deploy → Monitor for skill, prompt, configuration and rule assets.
- Added context-specific evaluation checks, bounded `human touch` / `reuse multiplier` signals, domain-owner versus platform-governance responsibility, and explicit rejection of automatic KPI, registry, dashboard or observer promotion.
- Boundary: wiki-only ingestion. No memory, active skill/reference, project, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency or external service changed.
