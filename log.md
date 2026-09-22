# Wiki Log

> Public repository maintenance history. This log records reusable repository changes, not personal runtime state, private sessions, local backups or task transcripts.
> Format: `## [YYYY-MM-DD] action | subject`

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
