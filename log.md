# Wiki Log

> Public repository maintenance history. This log records reusable repository changes, not personal runtime state, private sessions, local backups or task transcripts.
> Format: `## [YYYY-MM-DD] action | subject`

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
