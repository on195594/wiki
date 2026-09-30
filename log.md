# Wiki Log

> Public repository maintenance history. This log records reusable repository changes, not personal runtime state, private sessions, local backups or task transcripts.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-09-30] ingest | AI Engineer Notebooks practice entry points
- Captured the complete README and LICENSE at commit `50bbea81c369a22242e901f90b5848078842c34d` in `raw/articles/github-calmrocks-ai-engineer-notebooks-readme-2026-09-30.md`; resolved relative Markdown links to the captured revision and retained original external links. Updated [[llm-engineering-knowledge-map]] and its [[index]] description without creating a duplicate concept page.
- Added problem-oriented practice entry points for evaluation, RAG, tool loops, pipeline-versus-agent comparison and scoped delivery. Kept course descriptions, free API availability, T4 verification and production-case claims separate from independent evidence; no Notebook or benchmark was executed.
- No installation, active Skill, model routing, scheduler or runtime change is implied.
- Validation: all 54 existing tests and six maintenance gates passed; health issues, undeclared tags and blocking public-content violations were zero. README-linked repository paths were checked at the captured revision, source reverse lookup resolves to the existing knowledge map, and the raw manifest adds one source without changing existing source hashes. These checks validate the documentation capture and structure, not Notebook execution or course effectiveness.

## [2026-09-30] ingest | Bounded semantic classification before deterministic analytics
- Captured Mehdi Ouazza's MotherDuck article (2026-09-29) at `raw/articles/motherduck-jev-for-analytics-2026-09-29.md`; retained main prose, static tables, source links and SQL, with explicit exclusions for interactive diagrams. Updated [[deterministic-analytics-llm-reasoning-boundary]] and its [[index]] entry rather than creating a product concept.
- Distinguished format-based extraction from probabilistic semantic classification, reusable persisted labels from validated facts, and deterministic aggregation from input correctness. Preserved benchmark scopes and the selected-subset nature of model agreement; labeled human-ground-truth checks, high-confidence sampling, result lineage and end-to-end costing as engineering inferences.
- No product installation, active Skill change, model routing, scheduler, runtime or external publishing is implied.
- Validation: all 54 existing tests and six maintenance gates passed; health issues, undeclared tags and blocking public-content violations were zero. Source reverse lookup resolves to the existing analysis-boundary page; the raw manifest added one entry without changing or removing existing hashes, and the catalog diff is limited to this page. These checks do not validate model quality or reproduce the external benchmarks.

## [2026-09-30] ingest | One-bug agentic delivery loop
- Added the original body-text snapshot `raw/articles/builderio-agentic-software-factory-one-bug-2026-09-29.md`, with Alice Moore / Builder.io provenance, verified publication date, capture limitations and key source links; extended [[loop-engineering-hermes-agent-workflow]] rather than creating a new concept, and refreshed its [[index]] description.
- Preserved full user-behavior verification, repeatable test environments, PR follow-up and human rescue burden. Distinguished an imagined card-order example from empirical evidence; marked worktree/shared-resource isolation as an engineering inference. The live page's feedback-image alt text explains both intake and historical lookback, correcting the earlier text-only capture's apparent gap.
- No tool installation, active Skill change, scheduler, runtime or external publishing is implied.
- Validation: all 54 existing tests and six maintenance gates passed; health issues, undeclared tags and public-content violations were zero, catalog synchronization and `git diff --check` passed. Reverse lookup resolves the new source to the existing loop page; the raw manifest added one entry without changes to existing source hashes. These checks do not establish workflow effectiveness or independent product validation.

## [2026-09-30] ingest | LLM SPOC extraction as candidate knowledge
- Captured MachineLearningMastery's 2026-09-29 tutorial at `raw/articles/machinelearningmastery-llm-spoc-extraction-2026-09-29.md`; added its source and a bounded extraction-entry section to [[hermes-knowledge-architecture]], with an updated [[index]] description rather than a new concept page.
- Distinguished parseable structure, identifiable source and validated knowledge; kept controller-provided Context separate from claim-level evidence, and extraction failures separate from successful empty results. Source mechanisms and local inferences are labeled separately.
- The article's roughly 11 records and list-based storage are an author-reported teaching example, not accuracy or hallucination-reduction evidence. Raw capture retains code text but not executable indentation; no model execution, graph runtime or automatic Wiki writing is implied.
- Validation: all 54 existing tests and six maintenance gates passed; health issues, undeclared tags and public-content violations were zero, catalog synchronization and `git diff --check` passed. The raw manifest added one source with no existing hash changes; reverse lookup resolves it to the existing architecture page. The 17 pre-existing public-content review candidates remain outside this ingestion's scope.

## [2026-09-30] automation | End-to-end automated maintenance and quality gates
- Tooling: Implemented `_meta/scripts/wiki_maintain.py` providing unified one-stop verification (`--check`), auto-syncing of catalog and raw hashes (`--fix`), proactive freshness horizon scanning (`--freshness`), and local pre-commit hook installation (`--install-hooks`). Added unit tests in `_meta/scripts/test_wiki_maintain.py` (total 54 tests across suite).
- Local Gate: Installed `.git/hooks/pre-commit` to prevent committing invalid links, out-of-sync catalogs, unhashed raw captures, or privacy violations.
- Remote CI: Enhanced `.github/workflows/wiki-checks.yml` with weekly scheduled cron (`0 0 * * 1`) for proactive freshness monitoring, alongside catalog synchronization validation on push and pull requests.
- Documentation: Updated `_meta/wiki-health-check-runbook.md` with the new automated commands.
- Validation: `wiki_maintain.py --check` passed across all 6 gates; 54 unit tests passed; health P0/P1/P2=`0/0/0`; public content check passed with 0 violations (17 pre-existing candidates); `git diff --check` passed.

## [2026-09-30] governance | P2-P3 OKF catalog generation, attestation schema and topic domains
- Schema & Provenance (P2): Documented optional OKF v0.2 `attestation` metadata (`generated_by`, `verified_by`) in `SCHEMA.md` for verifiable agent authorship and review tracking without forcing retroactive migrations.
- Tooling (P2): Implemented `_meta/scripts/wiki_catalog.py` and unit tests in `_meta/scripts/test_wiki_catalog.py`; generated `_meta/catalog.json` for single-read agent context budgeting across all 114 formal pages.
- Navigation & Lineage (P3): Structured `index.md` concept navigation into five logical virtual topic domains (Agent Architecture, Workflows & Coding, Evaluation & Governance, LifeOS & Systems, Software Engineering Laws); refined granular raw source mapping in `concepts/software-engineering-laws/` to achieve 100% (167/167) raw file referencing in formal pages.
- Validation: Wiki health check passed with P0/P1/P2=`0/0/0`; `wiki_catalog.py --check` passed; tag audit undeclared tags=`0`; public content check passed with 0 violations (17 pre-existing candidates); 49 unit tests passed; `git diff --check` passed.

## [2026-09-30] governance | P1 wiki graph relations and freshness backfill
- Backfilled standard `## Relations` blocks across 30 formal pages previously lacking relations, bringing canonical relations coverage from 68 to 98/114 (86.0%). Refined relation semantics following Codex review to ensure external research concepts use `related` instead of artificial `depends_on` prerequisites.
- Added `volatility: medium` and quarterly `review_by: 2026-12-31` freshness gates to 14 high/medium-churn tooling and AI agent workflow concepts.
- Cleaned up retired empty directories (`docs/records`, `docs`, `_meta/reviews`).
- Validation: Wiki health check passed with P0/P1/P2=`0/0/0`; canonical relations coverage 98/114 (86.0%); tag audit undeclared tags=`0`; public content check passed with 0 violations (17 pre-existing candidates); all 47 unit tests passed; `git diff --check` passed. Codex review passed with actionable findings resolved.

## [2026-09-29] ingest | Tetral cloud-agent runtime boundaries
- Captured Yang Li's Tetral article as a bounded public source note at `raw/articles/tetral-next-scaling-problem-2026-09-06.md`; added its runtime/sandbox split, write-before-execute recovery, delivery, authorization and maturity limits to [[agent-development-lifecycle]] rather than making a near-duplicate concept. Refreshed its [[index]] entry.
- The source is a first-hand description of a personal-cluster Alpha, not independent production validation. Diagram details were not visually verified. The raw capture distinguishes a rejected invalid selected credential from a session with no selection that may use the platform key pool; no active Agent workflow, configuration or runtime behavior was changed.
- Validation: raw hash manifest added one entry with no existing hash changes; Wiki health P0/P1/P2=`0/0/0`, undeclared tags=`0`, public-content violations=`0`, and `git diff --check` passed. The 17 pre-existing public-content review candidates are outside this source's scope.

## [2026-09-29] ingest | Nimbus documentation framework
- Added [[nimbus-docs]] as a product page grounded in four first-party Markdown pages, added its index entry, and linked it from [[agentic-content-pipeline-design-patterns]]. The page separates product claims, public-content boundaries and selection inferences; it is a partial documentation review, not an installation or independent evaluation.
- Used the live official URLs as provenance rather than mirroring a changing documentation site into raw. No active Agent workflow, runtime, configuration or external publishing was changed.
- Validation: Wiki health P0/P1/P2=`0/0/0`, undeclared tags=`0`, public-content violations=`0`, and `git diff --check` passed. The existing 17 public-content candidates remain outside this page's review scope.

## [2026-09-29] governance | Clarify Schema authority and evidence scope
- Clarified current project authority, single-owner rule maintenance, evidence/time boundaries, partial or failed verification, and the distinction between lifecycle closure and demonstrated effectiveness.
- Replaced automatic page-creation and historical cleanup instructions with need-based maintenance. Clarified retirement/link preservation, public Git provenance, current-rule correction and the boundary between Wiki editing and operational authorization.
- Added a human-facing Schema navigation entry. These are Wiki normative choices; no private project material, deployment claim, new metadata, validator change or bulk migration was introduced.
- Validation: health P0/P1/P2=`0/0/0`, undeclared tags=`0`, public-content violations=`0` and `git diff --check` passed. The same 17 public-content candidates remain; no whole-Wiki privacy or product-fact audit is claimed.
- Independent Pi read-only review returned PASS for the Schema diff, related Wiki rules and validator-contract consistency; it did not rerun checks or inspect external project material.

## [2026-09-29] governance | Align content rules and quick reading paths
- Replaced fixed dates in the actual page template with placeholders; aligned Inbox intake with authorization and public suitability before raw capture.
- Aligned routing examples and quick rules with optional external access, reusable SOPs and public operations guides. Environment memory no longer substitutes for current-system verification; private execution history does not become eligible raw through context compression.
- Moved freshness checks before knowledge reuse, aligned abbreviated write-back paths with public/authorization boundaries, and marked the closed freshness plan as historical with current-rule links. Updated index descriptions without renaming historical paths.
- Added focused template/log/example readback and review-scope guidance to the existing health runbook, including checking hook-triggered effects before an authorized commit or publication. No new policy artifact, script, raw source or runtime change.
- Validation: Wiki health P0/P1/P2=`0/0/0`, undeclared tags=`0`, public-content violations=`0`, all 47 existing tests and `git diff --check` passed. Template placeholders, log header and unchanged raw/manifest were checked directly. The same 17 public-content candidates remain unadjudicated; no whole-Wiki privacy or current-product audit is claimed.
- Independent Pi review covered this change set and relevant owner pages; it found remaining method-to-Skill shortcuts and missing validation reporting. Corrected those shortcuts and recorded the actual validation scope. Pi follow-up returned PASS for those two findings and the related passages; it did not independently rerun deterministic checks or audit the entire Wiki.

## [2026-09-29] update | Shared human and AI Agent knowledge
- Generalized reusable Hermes-oriented concepts and their dependent pages into capability-based AI Agent knowledge. Updated titles, descriptions, tags, aliases and index display names; retained historical paths to preserve existing links and immutable raw snapshots.
- Made human and AI Agent readership explicit in `SCHEMA.md`, added task navigation to [[index]], and aligned [[agent-shared-wiki-index]], writing, retrieval and ingestion rules around shared content, evidence and authorized contribution. Public runbooks remain valid Wiki content; optional runtime capabilities are not assumed to exist.
- Removed unsupported private validation/promotion claims and private Skill dependencies from general guidance. Kept source attribution and closed historical records; scoped the Hermes/SRE comparison as a dated qualitative discussion rather than a current product ranking.
- Validation: Wiki health P0/P1/P2=`0/0/0`, undeclared tags=`0`, public-content violations=`0`, all 47 existing tests passed, and `git diff --check` passed. All 166 raw Markdown snapshots and their hash manifest were unchanged. Public scanning retained 17 pre-existing review candidates; this change does not claim a full manual privacy or current-product fact audit.
- Independent read-only review identified four groups of semantic issues; the affected passages were corrected and the focused re-review passed. No runtime, global configuration, external publishing or new infrastructure was introduced.
- A separate Pi review found a malformed log header, a fixed date in the writing template, residual private reference/promotion claims, and unsupported product comparisons. Restored the log/template structure, made first-edit adoption a project-owned candidate, and replaced Hermes capability/ranking assertions with sourced case facts and explicit design inferences. Health, tags, public-content and whitespace checks passed after repair. Pi independently re-read the four repaired areas and returned PASS; the follow-up was limited to those findings and their necessary sources.

## [2026-09-29] ingest | RRSI harness search regularization
- Added structured project-homepage capture `raw/articles/rrsi-harness-search-regularization-2026-09.md` and [[agent-harness-search-regularization]]; linked the new concept from [[production-ai-agent-evaluation-framework]] and the index.
- Kept homepage results and arXiv v2 abstract separately attributed where their OOD counts and token savings differ; clarified the noise-band exception and distinct per-edit/final-harness token comparisons. External benchmark findings are not active Agent rules or universal thresholds.
- Validation: raw hash manifest added one entry without changing existing hashes; Wiki health P0/P1/P2=`0/0/0`, tag audit undeclared=`0`, public-content violations=`0`, and `git diff --check` passed. Existing unrelated worktree changes were preserved.
- Independent AGY read-only review flagged the “new structural component” noise-band exception as a likely proposer/selector conflation. Direct readback of the project's evolution-explorer footer explicitly states it as a candidate-admission exception, so the proposed removal was rejected; the raw capture now quotes that passage and the concept distinguishes it from proposer-side exploration.

## [2026-09-28] update | ScientistTwo as a bounded scientific-discovery case
- Updated [[human-machine-scientific-discovery-verification-scarcity]] with a source-linked ScientistTwo preprint case: hypothesis screening, full experiments, ablation and simulated review/rebuttal, plus the authors' bounded task outcomes, human-review evidence and per-task cost.
- Kept AI-review acceptance distinct from real conference acceptance and author-reported results distinct from independent reproduction. Refreshed the existing index entry; no new concept or raw copy of the 71-page PDF, and no active workflow or runtime change.

## [2026-09-27] update | Planning as a process, not a mandatory artifact
- Added a structured source capture at `raw/articles/aymannadeem-plan-mode-is-dead-2026-09-24.md` (without reproducing the full article) and Ayman Nadeem's first-hand Nuanced retrospective (2026-09-24) to `[[hermes-ai-workflow-formalization-principles]]` as a bounded counterexample to mandatory long AI-generated plans; recorded provenance, retrieval quality, limitations, and the unchanged high-risk approval boundary.
- Narrowed three blanket artifact/todo statements to cross-session or verifiable-need triggers and refreshed the existing index description. Pi read-only review found and prompted removal of a private-Skill behavior claim from public provenance; no new concept, active skill, or runtime change.
- Validation after repair: Wiki health P0/P1/P2=`0/0/0`; `git diff --check` passed; tag audit undeclared count=`0`; public-content check violations=`0` (17 pre-existing review candidates).

## [2026-09-25] update | Task-specific interfaces over repeated agent-mediated operations
- Added a bounded interface-selection note to `[[hermes-ai-workflow-formalization-principles]]`, citing Burke Holland's GitHub Blog article “When chat is the wrong UI” (2026-09-24).
- Kept the product example and unmeasured token-savings claim separate from the reusable principle; the screenshot's AI praise is not independent workflow evidence. Updated the existing index entry; no new concept page, raw copy of the copyrighted article, or active workflow change.
- Validation: Wiki health P0/P1/P2=`0/0/0`; `git diff --check` passed.

## [2026-09-22] review-fix | Routing references and deterministic freshness dates
- Redirected stale consumers of `[[hermes-context-layer-operating-rules]]` to the content-ownership or composable-routing owners, while retaining that page only for context assembly, history compression and long-task state.
- Restricted local `[!volatile]` marker detection to the start of a blockquote so ordinary quoted prose can mention the syntax without becoming an unsupported block.
- Standardized page-level and claim-level freshness comparisons on the UTC calendar date and documented that contract in Schema, the runbook and the writing/lint standards.
- Added regression coverage for quoted marker prose and UTC default-date selection. No index membership, raw source, historical verification date or runtime configuration changed.
- Validation: 47 unit tests passed; Wiki health P0/P1/P2=`0/0/0`; tag audit undeclared count=`0`; public-content violations=`0`; `git diff --check` passed.

## [2026-09-22] governance | Claim-scoped freshness checks and minimal CI
- Extended the read-only health check to validate each supported local `[!volatile]` block independently: required block fields and format, real dates, `verified_at <= review_by`, future verification dates, claim-scoped expiry and `block source ⊆ page sources`.
- Kept local blocks and page-level freshness metadata optional. Malformed/unsupported blocks, invalid/future dates and undeclared local sources are P1; expiry begins the day after `review_by` and remains a non-blocking P2 reminder for that claim only.
- Added synthetic temporary-fixture coverage with an injected date for valid/invalid/future dates, due-date boundary, source omission, multiple blocks, unsupported syntax and ignored code examples.
- Added a read-only GitHub Actions workflow for unit, health, tag, public-content and commit-range whitespace checks. Network link checking remains separate; CI does not use secrets, write permissions, `pull_request_target`, raw-hash writers or AI review.
- Aligned Schema, runbook, writing/lint standards and index descriptions; no raw source, raw hash, historical freshness date, similarity threshold or Hermes runtime configuration changed.
- Validation: baseline and candidate Wiki health P0/P1/P2=`0/0/0`; unit tests increased from 41 to 45 and passed; tag audit undeclared count=`0`; public-content violations=`0` with the same 16 non-blocking candidates; external links reported 0 errors with 21 configured exclusions; `git diff --check` passed.

## [2026-09-22] refactor | Knowledge-layer rule maintenance boundaries
- Kept the existing five-dimension composable routing model and consolidated only full-rule duplication: architecture now provides navigation, content ownership remains in `[[hermes-memory-skills-wiki-boundaries]]`, quick composition and synthetic cases remain in `[[hermes-layer-routing-decision-checklist]]`, and context assembly plus long-task state remain in `[[hermes-context-layer-operating-rules]]`.
- Left the canonical Freshness Gate in `[[hermes-retrieval-priority-and-answer-path]]` unchanged; retained short local safety and time-sensitive boundaries where removing them would increase lookup cost.
- Removed duplicate layer-by-layer checklists and promotion rules while preserving unique source-scoped cron/MCP constraints, content examples, project-state structure and provenance.
- Updated the four affected index descriptions; no Schema, raw source, `verified_at`, similarity threshold, runtime layer or Hermes configuration changed.
- Validation: the four required reading paths passed semantic checks; baseline and candidate Wiki health P0/P1/P2=`0/0/0`; tag audit undeclared count=`0`; public-content violations=`0` with the same 16 non-blocking candidates; 41 unit tests passed; external links reported 0 errors with 21 configured exclusions; `git diff --check` passed.

## [2026-09-22] review-fix | Experience consolidation and layer-routing semantics
- Clarified that private state, session/execution evidence and one-off closeouts remain in their original private or project carriers; only public, durable findings and reusable public historical decisions enter the corresponding formal Wiki owner.
- Scoped the Hermes capability assessment title, section headings and action wording to its 2026-05-11 / v0.13.0 evidence window without rewriting that historical snapshot as current behavior.
- Recast layer routing as five composable dimensions—content ownership, execution method, trigger, external capability and runtime state—and replaced exclusive examples with bounded synthetic combinations.
- Updated the three index descriptions; no raw source, `verified_at`, runtime layer or Hermes configuration changed.
- Validation: baseline and candidate Wiki health P0/P1/P2=`0/0/0`; tag audit undeclared count=`0`; public-content violations=`0`; 41 unit tests passed; external links reported 0 errors with 21 configured exclusions; `git diff --check` passed. The candidate retained the baseline 15 review candidates and added one touched-page phrase candidate, manually adjudicated as a public-boundary warning rather than an instance record.

## [2026-09-21] review-fix | Flutter source attribution and platform scope
- Applied a read-only Pi review of `[[flutter]]`: distinguished native Dart VM development from Web `dartdevc`, removed an under-sourced Web characterization, and corrected the `flutter create` citation.
- Marked project-fit, plugin-validation and minimum-adoption guidance as `[推论]`, and narrowed the accessibility wording to the support described by the official architecture and accessibility pages.
- Validation: citation-ledger strict verification passed at 73% sentence coverage (40/55); Wiki health P0/P1/P2=`0/0/0`; tag audit undeclared count=`0`; public-content violations=`0`; `git diff --check` passed.

## [2026-09-21] ingest | Flutter open-source UI framework
- Added `[[flutter]]` as the canonical product page for Flutter's positioning, Dart/framework/engine/embedder layers, declarative Widget model, platform interoperability, application architecture, testing, accessibility and adoption boundaries.
- Grounded the synthesis in 12 first-party Flutter documentation pages that reflected Flutter 3.47.2 at verification time; marked the page high-volatility with a 2026-12-20 review date and separated local adoption deductions with `[推论]`.
- Added the canonical index entry and a bounded backlink from `[[software-engineering-laws-architecture]]`; retained official live URLs as canonical provenance instead of creating a raw documentation mirror.
- Validation: citation-ledger strict verification passed at 77% sentence coverage (40/52); Wiki health P0/P1/P2=`0/0/0`; tag audit undeclared count=`0`; public-content violations=`0`; `git diff --check` passed.

## [2026-09-21] ingest | Entropy and entropy increase
- Added `[[entropy-and-entropy-increase]]` to distinguish thermodynamic, statistical and Shannon entropy; documented the isolated/open-system boundary and the limits of “disorder” shorthand.
- Grounded the page in MIT OpenCourseWare, OpenStax, Shannon's 1948 paper and a narrow NIST nonequilibrium caveat; connected the existing software-entropy metaphor without treating it as a physical law.
- Tightened source boundaries by limiting `k_B` to the cited Boltzmann/Gibbs formulas, using Shannon's sourced “natural unit” wording, and marking management/software transfer as synthesis.
- Added the canonical index entry and a backlink from `[[software-engineering-laws-quality]]`; no raw source or active runtime layer changed.
- Validation: citation ledger strict verification passed at 66% sentence coverage (27/41); Wiki health P0/P1/P2=`0/0/0`; tag audit undeclared count=`0`; public-content violations=`0`; the public Harvard-hosted source URL candidate was reviewed as provenance, not a private path; `git diff --check` passed.

## [2026-09-20] governance | Public knowledge boundary remediation
- Applied the public boundary to formal pages, raw sources, `_meta`, operations, scripts and repository logs before content is admitted.
- Removed personal instance-state dashboards, private session/task artifacts and local-only provenance pointers; generalized mixed pages without promoting private observations to public facts.
- Made maintenance-script root resolution portable and added deterministic public-content violations plus non-blocking review candidates with synthetic regression tests.
- Updated indexes, relations, source rules and the raw-source hash manifest for the resulting public set.
- Classified all 447 baseline tracked files: 170 retained unchanged, 120 generalized and 157 removed; reviewed four new maintenance/test files. All files were readable UTF-8 text, so no attachment remained unreviewed.
- Validation: 35 unit tests passed; Wiki health P0/P1/P2=`0/0/0`; tag audit found no undeclared tags; public-content violations=`0`; all 65 changed raw sources passed reverse lookup with 88 formal references; `git diff --check` passed.
- Boundary: this is a local isolated-branch change. It does not publish the branch, change repository visibility, clean Git history, or authorize any Hermes runtime/configuration action.
