# Wiki Log

> Chronological record of wiki actions.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-04-16] create | Wiki initialized
- Path: `/home/lin/wiki`
- Created core structure: `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `_meta/`
- Created: `SCHEMA.md`, `index.md`, `log.md`
- Seeded: `concepts/hermes-knowledge-architecture.md`, `concepts/wiki-ingestion-workflow.md`

## [2026-04-16] update | Hermes knowledge architecture
- Updated: `concepts/hermes-knowledge-architecture.md`
- Updated: `index.md`
- Captured the overall Hermes knowledge-base architecture, including runtime layers, wiki filesystem layers, and write-back loop.

## [2026-04-16] create | Hermes memory skills wiki boundaries
- Created: `concepts/hermes-memory-skills-wiki-boundaries.md`
- Updated: `concepts/hermes-knowledge-architecture.md`
- Updated: `index.md`
- Defined the routing rules and decision checklist for what belongs in memory, skills, wiki, or only sessions.

## [2026-04-16] create | Hermes retrieval priority and answer path
- Created: `concepts/hermes-retrieval-priority-and-answer-path.md`
- Updated: `concepts/hermes-knowledge-architecture.md`
- Updated: `concepts/wiki-ingestion-workflow.md`
- Updated: `index.md`
- Documented the default retrieval order and answer path: wiki first, then memory, skills, sessions, raw/external, and finally write-back.

## [2026-04-16] create | Hermes wiki page writing standards
- Created: `concepts/hermes-wiki-page-writing-standards.md`
- Updated: `concepts/wiki-ingestion-workflow.md`
- Updated: `index.md`
- Defined page-level writing rules for filename, frontmatter, structure, wikilinks, update policy, and quality checks.

## [2026-04-16] create | Hermes wiki lint and health check standards
- Created: `concepts/hermes-wiki-lint-and-health-check-standards.md`
- Updated: `concepts/hermes-wiki-page-writing-standards.md`
- Updated: `concepts/hermes-retrieval-priority-and-answer-path.md`
- Updated: `index.md`
- Defined health-check scope, core lint checks, severity levels, pass criteria, and report format for the wiki.

## [2026-04-16] lint | Hermes wiki health check
- Scope: `index.md`, `log.md`, `SCHEMA.md`, `entities/`, `concepts/`, `comparisons/`, `queries/`
- Result: P0=0, P1=1, P2=1, total actionable issues=2
- P1: `concepts/wiki-ingestion-workflow.md` is missing a `## Summary` section
- P2: `concepts/hermes-wiki-page-writing-standards.md` exceeds the 200-line guideline at 228 lines
- No broken wikilinks, no orphan pages, no missing index entries, no frontmatter issues, and no tag taxonomy violations

## [2026-04-16] update | Hermes wiki lint fixes
- Backups: `wiki-ingestion-workflow.md.bak.20260416_085140`, `hermes-wiki-page-writing-standards.md.bak.20260416_085140`
- Updated: `concepts/wiki-ingestion-workflow.md`
- Updated: `concepts/hermes-wiki-page-writing-standards.md`
- Fixed the missing `## Summary` section in `wiki-ingestion-workflow.md`
- Compressed `hermes-wiki-page-writing-standards.md` from 228 lines to 164 lines

## [2026-04-16] lint | Hermes wiki health check (post-fix)
- Result: P0=0, P1=0, P2=0, total actionable issues=0
- Pass: true
- No broken wikilinks, no orphan pages, no missing index entries, no frontmatter issues, no tag violations, no page-size violations, and no schema-drift findings

## [2026-04-16] ingest | AriXZone on Dijkstra and AI programming
- Captured raw source: `raw/articles/arixzone-dijkstra-ai-programming-2026-03-31.md`
- Created: `concepts/dijkstra-ai-programming-formalization.md`
- Updated: `index.md`
- Extracted the public X post and compiled its argument into a reusable concept page about formalization, natural language limits, and AI coding workflow.

## [2026-04-16] ingest | Dijkstra EWD667 dual-source comparison
- Captured raw source: `raw/articles/dijkstra-ewd667-natural-language-programming-1978.md`
- Created: `comparisons/dijkstra-ewd667-vs-ai-programming-article.md`
- Created: `concepts/hermes-ai-workflow-formalization-principles.md`
- Updated: `concepts/dijkstra-ai-programming-formalization.md`
- Updated: `index.md`
- Compared EWD667 with the 2026 AriXZone article, then translated the shared conclusions into concrete Hermes workflow principles.

## [2026-04-16] update | Hermes knowledge base operating flow
- Created: `concepts/hermes-knowledge-base-operating-flow.md`
- Updated: `concepts/hermes-ai-workflow-formalization-principles.md`
- Updated: `concepts/wiki-ingestion-workflow.md`
- Updated: `index.md`
- Compressed the current knowledge-base process into one end-to-end flow: intake, classify, capture, compile, retrieve, maintain.

## [2026-04-16] query | Hermes optimization sample case
- Captured raw source: `raw/transcripts/hermes-optimization-sample-case-2026-04.md`
- Created: `queries/hermes-optimization-sample-case.md`
- Updated: `concepts/hermes-knowledge-base-operating-flow.md`
- Updated: `index.md`
- Re-ran the recent Hermes optimization journey through the operating flow and turned it into a reusable sample case.

## [2026-04-16] ingest | yibie on CompanyOS and LifeOS
- Captured raw source: `raw/articles/yibie-companyos-lifeos-filesystem-philosophy-2026-02-12.md`
- Created: `concepts/companyos-to-lifeos-filesystem-philosophy.md`
- Updated: `index.md`
- Extracted the X longform article and compiled it into a reusable concept page about filesystem-as-state, shared namespace, governance-by-permissions, and LifeOS.

## [2026-04-16] ingest | DtDt666 on ordinary investor investing system
- Captured raw source: `raw/articles/dtdt666-ordinary-investor-how-to-invest-2026-03-10.md`
- Created: `concepts/ordinary-investor-investment-system.md`
- Updated: `index.md`
- Compiled the X image-based longform article into a reusable concept page about investing systems, behavior, asset allocation, rebalancing, and avoiding buy-high-sell-low patterns.

## [2026-04-16] ingest | Google SRE on Gemini CLI incident response
- Captured raw source: `raw/articles/google-sre-gemini-cli-outages-2026-01-22.md`
- Created: `concepts/google-sre-gemini-cli-incident-response.md`
- Updated: `index.md`
- Compiled the Google Cloud blog article into a reusable concept page about mitigate-first incident response, constrained tool execution, MCP-based integration, and AI as a production copilot.

## [2026-04-16] comparison | Hermes vs Google SRE agentic incident response
- Created: `comparisons/hermes-vs-google-sre-agentic-incident-response.md`
- Updated: `index.md`
- Compared Google’s incident-focused Gemini CLI workflow with Hermes’s current general-purpose agent substrate, highlighting shared architecture, safety differences, and the missing incident-specific packaging layer.

## [2026-04-16] ingest | TDS on context engineering beyond RAG
- Captured raw source: `raw/articles/tds-rag-isnt-enough-context-engineering-2026-04-14.md`
- Created: `concepts/llm-context-engineering-layer.md`
- Backups: `index.md.bak.20260416_162455`, `log.md.bak.20260416_162455`
- Updated: `index.md`
- Compiled the article into a reusable concept page on context engineering as the layer that manages memory, compression, re-ranking, and token budget between retrieval and prompt assembly.

## [2026-04-16] concept | Hermes context engineering design priorities
- Created: `concepts/hermes-context-engineering-design-priorities.md`
- Backups: `index.md.bak.20260416_163018`, `log.md.bak.20260416_163018`
- Updated: `index.md`
- Converted the external context-engineering article into Hermes-specific design priorities, with a concrete implementation order: budget control, ranking, compression, then history decay.

## [2026-04-17] ingest | XDA on Claude Code practical workflow tips
- Captured raw source: `raw/articles/xda-claude-code-practical-tips-2026-04-13.md`
- Created: `concepts/claude-code-practical-workflow-tips.md`
- Backups: `index.md.bak.20260417_104004`, `log.md.bak.20260417_104004`
- Updated: `index.md`
- Compiled the article into a reusable concept page about side-question workflows, browser verification loops, task automation, multi-directory scope, and cross-device Claude Code usage.

## [2026-04-17] ingest | GVM on money as tool and investment-vs-consumption
- Captured raw source: `raw/articles/gvm-money-work-for-you-1-percent-investor-wisdom-2026-04-14.md`
- Created: `concepts/money-as-tool-and-investment-vs-consumption-framework.md`
- Backups: `index.md.bak.20260417_120501`, `log.md.bak.20260417_120501`
- Updated: `index.md`
- Compiled the article into a reusable concept page about using money as a freedom tool, distinguishing good leverage from speculative leverage, and separating investment from pure consumption.

## [2026-04-17] ingest | OpenAI Codex best practices
- Captured raw source: `raw/articles/openai-codex-best-practices-2026-04-17.md`
- Created: `concepts/codex-agent-workflow-layering.md`
- Backups: `index.md.bak.20260417_161100`, `log.md.bak.20260417_161100`
- Updated: `index.md`
- Compiled the article into a reusable concept page on agent workflow layering: prompt and planning for the current task, `AGENTS.md` for durable repo rules, skills for repeatable methods, MCP for external live context, and automation for scheduling stable workflows.

## [2026-04-17] interpret | Codex workflow layering for Hermes
- Created: `concepts/hermes-agent-workflow-layering-and-adoption-order.md`
- Backups: `index.md.bak.20260417_161543`, `log.md.bak.20260417_161543`, `concepts/codex-agent-workflow-layering.md.bak.20260417_161543`
- Updated: `concepts/codex-agent-workflow-layering.md`
- Updated: `index.md`
- Translated the neutral Codex workflow article into Hermes-native layer mapping: instruction layer, task framing, durable knowledge, skills, MCP/tools, verification, and cron-based scheduling.

## [2026-04-17] create | Hermes layer routing decision checklist
- Created: `concepts/hermes-layer-routing-decision-checklist.md`
- Backups: `index.md.bak.20260417_162351`, `log.md.bak.20260417_162351`
- Updated: `index.md`
- Wrote an executable routing checklist for deciding what belongs in wiki, memory, skill, cron, or MCP, explicitly calibrated against Hermes official docs for memory, skills, cron, and MCP while treating wiki as a local knowledge-layer convention.

## [2026-04-17] create | Hermes layer routing sample cases
- Created: `queries/hermes-layer-routing-sample-cases.md`
- Backups: `index.md.bak.20260417_165402`, `log.md.bak.20260417_165402`
- Updated: `index.md`
- Added 15 concrete routing examples showing when real Hermes inputs belong in wiki, memory, skill, cron, MCP, or only the current session, using Hermes official docs as the calibration baseline.

## [2026-04-17] create | Hermes layer routing edge cases
- Created: `queries/hermes-layer-routing-edge-cases.md`
- Backups: `index.md.bak.20260417_170159`, `log.md.bak.20260417_170159`
- Updated: `index.md`
- Added edge-case arbitration examples for `skill + cron`, `memory vs wiki`, `MCP vs skill`, `session vs long-term layers`, and other ambiguous routing cases, still calibrated against Hermes official docs.

## [2026-04-17] ingest | Leontraveller investment notes
- Captured raw sources: `raw/articles/leontraveller-investment-notes-1-2026-04-17.md`, `raw/articles/leontraveller-investment-notes-2-2026-04-17.md`
- Created: `concepts/leontraveller-trading-and-investment-system.md`
- Backups: `index.md.bak.20260417_193314`, `log.md.bak.20260417_193314`
- Updated: `index.md`
- Compiled the two-part article into a reusable concept page about trend following, risk control, anti-average-down discipline, and avoiding complex yield or leverage traps.

## [2026-04-17] create | Personal investment operating rules
- Created: `concepts/personal-investment-operating-rules.md`
- Created: `comparisons/leontraveller-vs-ordinary-investor-investment-system.md`
- Backups: `index.md.bak.20260417_193739`, `log.md.bak.20260417_193739`
- Updated: `index.md`
- Combined the long-term ordinary-investor framework with Leontraveller’s active-trading discipline into one practical operating-rules page and one comparison page.

## [2026-04-17] create | How I should use these two investment frameworks
- Created: `queries/how-i-should-use-these-two-investment-frameworks.md`
- Backups: `index.md.bak.20260417_194153`, `log.md.bak.20260417_194153`
- Updated: `index.md`
- Added a decision-card style query page showing how to separate long-term allocation logic from active-trading logic in daily use.

## [2026-04-17] create | My investment pre-trade checklist
- Created: `queries/my-investment-pre-trade-checklist.md`
- Backups: `index.md.bak.20260417_195031`, `log.md.bak.20260417_195031`
- Updated: `index.md`
- Added a pre-trade checklist page focused on capital-layer classification, action classification, exit planning, and emotional red flags before placing any order.

## [2026-04-17] create | When I should not trade
- Created: `queries/when-i-should-not-trade.md`
- Backups: `index.md.bak.20260417_195452`, `log.md.bak.20260417_195452`
- Updated: `index.md`
- Added a stop-trading query page covering average-down temptation, missing exit plans, wrong-capital usage, emotional activation, vague actions, and complex products without clear thesis.

## [2026-04-17] create | How I should review a losing position
- Created: `queries/how-i-should-review-a-losing-position.md`
- Backups: `index.md.bak.20260417_202104`, `log.md.bak.20260417_202104`
- Updated: `index.md`
- Added a losing-position review page focused on separating normal losses from broken thesis, and separating true rebalancing from emotional averaging down.

## [2026-04-17] create | How I should scale into and out of a position
- Created: `queries/how-i-should-scale-into-and-out-of-a-position.md`
- Backups: `index.md.bak.20260417_202813`, `log.md.bak.20260417_202813`
- Updated: `index.md`
- Added a position-scaling page focused on distinguishing valid staged execution from disguised averaging down, hesitation, or anxiety-driven trimming.

## [2026-04-17] create | How I should size a position
- Created: `queries/how-i-should-size-a-position.md`
- Backups: `index.md.bak.20260417_204320`, `log.md.bak.20260417_204320`
- Updated: `index.md`
- Added a position-sizing page focused on risk budget, over-sizing signals, conviction discipline, concentration risk, and when to deliberately size smaller.

## [2026-04-17] create | How I should handle a winning position
- Created: `queries/how-i-should-handle-a-winning-position.md`
- Backups: `index.md.bak.20260417_204957`, `log.md.bak.20260417_204957`
- Updated: `index.md`
- Added a winning-position management page focused on separating true risk management from profit anxiety, and balancing let-profit-run discipline with planned exits.

## [2026-04-17] create | How I should decide between doing nothing and taking action
- Created: `queries/how-i-should-decide-between-doing-nothing-and-taking-action.md`
- Backups: `index.md.bak.20260417_205225`, `log.md.bak.20260417_205225`
- Updated: `index.md`
- Added a waiting-discipline page focused on distinguishing rule-based patience from hesitation, fear of missing out, and action-for-relief behavior.

## [2026-04-17] create | How I should build a post-trade review loop
- Created: `queries/how-i-should-build-a-post-trade-review-loop.md`
- Backups: `index.md.bak.20260417_205734`, `log.md.bak.20260417_205734`
- Updated: `index.md`
- Added a post-trade review page focused on process-vs-outcome review, identifying the main error type, and converting review into one concrete rule adjustment for the next cycle.

## [2026-04-17] create | How I should detect repeat mistakes in my trading
- Created: `queries/how-i-should-detect-repeat-mistakes-in-my-trading.md`
- Backups: `index.md.bak.20260417_210104`, `log.md.bak.20260417_210104`
- Updated: `index.md`
- Added a repeat-mistake detection page focused on distinguishing isolated events from recurring behavior patterns, separating process bugs from system bugs, and only promoting actionable repeated errors into hard rules.

## [2026-04-17] create | How I should convert trading lessons into hard rules
- Created: `queries/how-i-should-convert-trading-lessons-into-hard-rules.md`
- Backups: `index.md.bak.20260417_210325`, `log.md.bak.20260417_210325`
- Updated: `index.md`
- Added a hard-rule conversion page focused on deciding which lessons deserve rule status, how concrete rules should be written, and how to avoid bloated, non-executable rule sets.

## [2026-04-17] create | How I should keep my trading system small and executable
- Created: `queries/how-i-should-keep-my-trading-system-small-and-executable.md`
- Backups: `index.md.bak.20260417_221854`, `log.md.bak.20260417_221854`
- Updated: `index.md`
- Added a rule-governance page focused on keeping the trading system small, separating core rules from supporting notes, and pruning or compressing rules that no longer improve execution.

## [2026-04-21] concept | Hermes LifeOS executable architecture
- Backups: `index.md.bak.20260421_184215`, `log.md.bak.20260421_184215`
- Created: `concepts/hermes-lifeos-executable-architecture.md`
- Updated: `index.md`
- Updated: `log.md`
- Converted the LifeOS-vs-profile conclusion into a strict Hermes layering contract, rollout plan, profile policy, and boundary matrix for executable adoption.

## [2026-04-21] concept | LifeOS Phase 1 domain map
- Backups: `index.md.bak.20260421_184650`, `log.md.bak.20260421_184650`
- Created: `concepts/lifeos-overview.md`
- Created: `concepts/family-education-operating-model.md`
- Created: `concepts/personal-finance-and-education-fund-model.md`
- Created: `concepts/work-and-career-operating-model.md`
- Created: `concepts/personal-growth-operating-model.md`
- Updated: `index.md`
- Updated: `log.md`
- Built the first LifeOS domain map so family education, finance/education fund, work/career, and personal growth now exist as formal wiki domains under one overview page.

## [2026-04-21] concept | LifeOS domain map closes the governance layer
- Backups: `lifeos-overview.md.bak.20260421_194012`, `index.md.bak.20260421_194012`, `log.md.bak.20260421_194012`
- Created: `concepts/system-governance-operating-model.md`
- Updated: `concepts/lifeos-overview.md`
- Updated: `index.md`
- Updated: `log.md`
- Added the missing system-governance domain so the LifeOS top-level map now covers family, finance, work, growth, and Hermes self-governance as a complete first-class domain set.

## [2026-04-21] create | LifeOS decision interface pages
- Backups: `index.md.bak.20260421_194554`, `log.md.bak.20260421_194554`
- Created: `queries/family-education-decision-interfaces.md`
- Created: `queries/personal-finance-and-education-fund-decision-interfaces.md`
- Created: `queries/work-and-career-decision-interfaces.md`
- Created: `queries/personal-growth-decision-interfaces.md`
- Created: `queries/system-governance-decision-interfaces.md`
- Updated: `index.md`
- Updated: `log.md`
- Turned the five first-class LifeOS domains into reusable decision-interface pages so later skills can be extracted from stable question structures instead of ad hoc chat prompts.

## [2026-04-21] create | Hermes LifeOS profile topology
- Backups: `index.md.bak.20260421_200908`, `log.md.bak.20260421_200908`
- Runtime: created profile `lab` via `hermes profile create lab --clone`
- Created: `concepts/hermes-lifeos-profile-topology.md`
- Updated: `index.md`
- Updated: `log.md`
- Formalized the current profile topology as `default` for the main brain and `lab` for experimental isolation, while explicitly deferring `work/public` until real separation needs appear.

## [2026-04-21] rollback | Light revert to mainline LifeOS
- Backups: `index.md.bak.20260421_211958`, `log.md.bak.20260421_211958`, `concepts/hermes-lifeos-profile-topology.md.bak.20260421_211958`, `queries/*.bak.20260421_211958`
- Deleted profile: `lab`
- Deleted: `concepts/hermes-lifeos-profile-topology.md`
- Deleted: `queries/family-education-decision-interfaces.md`
- Deleted: `queries/personal-finance-and-education-fund-decision-interfaces.md`
- Deleted: `queries/work-and-career-decision-interfaces.md`
- Deleted: `queries/personal-growth-decision-interfaces.md`
- Deleted: `queries/system-governance-decision-interfaces.md`
- Updated: `index.md`
- Updated: `log.md`
- Kept the executable architecture page and LifeOS domain map, while removing the experimental profile layer and the early decision-interface layer.

## [2026-04-22] create | Hermes memory governance notes
- Backups: `index.md.bak.20260422_193622`, `log.md.bak.20260422_193622`
- Created: `concepts/hermes-memory-governance-notes.md`
- Updated: `index.md`
- Updated: `log.md`
- Promoted the reusable governance rules discovered during USER.md and MEMORY.md cleanup into a formal wiki page so the long-form reasoning lives in wiki instead of staying compressed into memory.

## [2026-04-22] create | Hermes health dashboard
- Backups: `index.md.bak.20260422_195608`, `log.md.bak.20260422_195608`
- Created: `operations/hermes-health-dashboard.md`
- Updated: `index.md`
- Updated: `log.md`
- Added the ops page for the weekly governance pipeline and recorded the baseline runtime status plus the new weekly health cron job.

## [2026-04-22] update | Browser login fallback documented
- Backups: `hermes-health-dashboard.md.bak.20260422_203914`, `log.md.bak.20260422_203914`
- Updated: `operations/hermes-health-dashboard.md`
- Linked the new `browser-login-form-fallback` skill pattern from the ops page so browser login/session work has a documented low-risk fallback path when refs are unstable.

## [2026-04-23] create | Gstack project execution lane
- Backups: `index.md.bak.20260423_185423`, `log.md.bak.20260423_185423`
- Created: `concepts/gstack-project-execution-lane.md`
- Updated: `index.md`
- Updated: `log.md`
- Added a Hermes-native gstack execution lane page that turns the five most practical gstack skills into one default project progression path from idea framing through plan review, implementation review, and QA.

## [2026-04-23] create | Gstack project execution lane validation case
- Backups: `index.md.bak.20260423_193820`, `log.md.bak.20260423_193820`
- Created: `queries/gstack-project-execution-lane-validation-case.md`
- Updated: `index.md`
- Updated: `log.md`
- Recorded a full closed-loop validation of the gstack 5-skill lane using a real Hermes kickoff project, capturing what each stage contributed and where the current intake tool still has boundaries.

## [2026-04-29] create | Hermes context layer operating rules
- Backups: `index.md.bak.20260429_140339`, `log.md.bak.20260429_140339`
- Created: `concepts/hermes-context-layer-operating-rules.md`
- Updated: `index.md`
- Updated: `log.md`
- Converted the context-engineering article's Hermes-specific implications into an executable layer contract covering session, memory, skill, wiki, project state, cron/log, MCP, and subagent boundaries.

## [2026-04-30] ingest | Machine Learning Mastery on context engineering for AI agents
- Captured raw source: `raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md`
- Backups: `concepts/hermes-context-layer-operating-rules.md.bak.20260430_092935`, `log.md.bak.20260430_092935`
- Updated: `concepts/hermes-context-layer-operating-rules.md`
- Added the source-backed principles from Machine Learning Mastery to the existing Hermes context layer operating rules page instead of creating a near-duplicate concept page.

## [2026-04-30] update | Integrate Machine Learning Mastery context engineering source
- Backups: `concepts/hermes-context-layer-operating-rules.md.bak.20260430_093348`, `raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md.bak.20260430_093348`, `log.md.bak.20260430_093348`
- Updated: `concepts/hermes-context-layer-operating-rules.md`
- Updated: `raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md`
- Folded the article-specific principles into the existing Summary, Goal, and Core principles sections, then added a backlink from the raw source to the compiled concept page.

## [2026-04-30] ingest | Ahrefs content engineering with Claude Code
- Captured raw source: `raw/articles/ahrefs-content-engineering-claude-code-2026-04-28.md`
- Created: `concepts/agentic-content-pipeline-design-patterns.md`
- Backups: `index.md.bak.20260430_125203`, `log.md.bak.20260430_125203`
- Updated: `index.md`
- Compiled Ryan Law's Ahrefs article into a reusable design-pattern page for agentic content pipelines: expert workflow decomposition, skill-file chains, MCP/data sources, intermediate artifacts, human review, and automation boundaries.

## [2026-04-30] ingest | LangChain model-specific harness profiles for Deep Agents
- Captured raw source: `raw/articles/langchain-tuning-deep-agents-different-models-2026-04-29.md`
- Created: `concepts/hermes-model-specific-harness-profiles.md`
- Created: `queries/hermes-system-model-specific-harness-optimization-plan.md`
- Backups: `index.md.bak.20260430_210714`, `log.md.bak.20260430_210714`
- Updated: `index.md`
- Compiled the LangChain Deep Agents article into a Hermes-native model-specific harness principle, then drafted a conservative Hermes optimization plan: keep default stable, build overlay registry, validate with small evals, patch narrow skills before considering runtime profiles or cron.

## [2026-04-30] plan | Hermes harness profile validation detailed plan
- Created: `queries/hermes-harness-profile-validation-detailed-plan.md`
- Backups: `index.md.bak.20260430_213142`, `log.md.bak.20260430_213142`
- Updated: `index.md`
- Expanded the earlier model-specific harness optimization note into a full implementation-grade validation plan covering project bootstrap, overlay registry, prompts, fixtures, scoring rubric, experiment records, promotion gates, and rollback rules.

## [2026-04-30] closeout | Hermes harness profile validation final conclusion
- Created: `queries/hermes-harness-profile-validation-final-closeout.md`
- Backups: `concepts/hermes-model-specific-harness-profiles.md.bak.20260430_224728`, `index.md.bak.20260430_224728`, `log.md.bak.20260430_224728`
- Updated: `concepts/hermes-model-specific-harness-profiles.md`
- Updated: `index.md`
- Recorded the final project conclusion: promote only the narrow `writing-plans` and `requesting-code-review` skill patches; do not promote article summary, coding/config, runtime profile, Hermes core, SOUL, cron, or memory changes from this validation project.

## [2026-04-30] ingest | Real Python on AI coding agent workflow types
- Captured raw source: `raw/articles/realpython-ai-coding-agents-four-workflow-types-2026-04-29.md`
- Created: `concepts/ai-coding-agent-workflow-types.md`
- Backups: `index.md.bak.20260430_234650`, `log.md.bak.20260430_234650`
- Updated: `index.md`
- Compiled Real Python’s four-mode taxonomy into a reusable concept page for choosing between IDE, terminal, PR, and cloud-style coding-agent workflows.

## [2026-05-01] ingest | Pydantic AI typed agent boundaries
- Backups: `index.md.bak.20260501_085531`, `log.md.bak.20260501_085531`
- Captured raw source: `raw/articles/machinelearningmastery-pydantic-ai-agents-2026-04-29.md`
- Created: `concepts/typed-ai-agent-boundaries.md`
- Updated: `index.md`
- Compiled the Pydantic AI article into a reusable concept about reducing AI programming uncertainty through structured outputs, typed tool boundaries, and dependency injection.

## [2026-05-01] create | Hermes AI coding typed-boundary best practice
- Backups: `index.md.bak.20260501_090053`, `log.md.bak.20260501_090053`, `typed-ai-agent-boundaries.md.bak.20260501_090053`
- Created: `queries/how-i-should-use-hermes-for-ai-coding-with-typed-boundaries.md`
- Updated: `concepts/typed-ai-agent-boundaries.md`
- Updated: `index.md`
- Converted the Pydantic AI typed-boundary concept into a Hermes-native AI coding best-practice page: contract first, execution-lane selection, typed outputs, narrow tools, explicit dependency context, and layered verification.

## [2026-05-06] ingest | Agent self-validation loops
- Captured raw source: `raw/articles/towardsdatascience-claude-code-self-validation-2026-05-05.md`
- Created: `concepts/agent-self-validation-loops.md`
- Updated: `concepts/claude-code-practical-workflow-tips.md`
- Updated: `index.md`
- Converted the Towards Data Science Claude Code self-validation article into a reusable agent engineering pattern: baseline/fixture targets, tool feedback channels, iterative validation loops, equivalence rules, and stop conditions.

## [2026-05-07] ingest | Subagent orchestration patterns
- Captured raw source: `raw/articles/philschmid-subagent-patterns-2026-05-05.md`
- Created: `concepts/subagent-orchestration-patterns.md`
- Updated: `concepts/hermes-context-layer-operating-rules.md`
- Updated: `concepts/ai-coding-agent-workflow-types.md`
- Updated: `index.md`
- Ingested Phil Schmid's four subagent lifecycle patterns and translated them into a conservative Hermes adoption rule: default to inline `delegate_task`, use fan-out for genuinely independent work, and keep agent pools/teams behind validation gates.

## [2026-05-07] organize | Public info monitoring automation methodology
- Moved root-level draft `公开信息监控自动化方法论.md` into `concepts/public-info-monitoring-automation-methodology.md`
- Updated: `index.md`
- Preserved the Amazon Price Watch case as the validated sample and normalized the page as a formal concept with frontmatter and related links.

## [2026-05-07] closeout | GSearch knowledge validation
- Backups: `index.md.bak.20260507_160902`, `log.md.bak.20260507_160902`, `concepts/subagent-orchestration-patterns.md.bak.20260507_160902`
- Created: `queries/gsearch-knowledge-validation-closeout.md`
- Updated: `concepts/subagent-orchestration-patterns.md`
- Updated: `index.md`
- Captured the GSearch validation project as a completed knowledge-validation loop: project-local evidence lane succeeded, inline subagent review remains default, fan-out is reserved for promotion/source-risk cases, and live Telegram `/gsearch` remains unpromoted pending separate approval.

## [2026-05-07] ingest | AlphaSignal agent orchestration production tradeoffs
- Backups: `index.md.bak.20260507_174532`, `log.md.bak.20260507_174532`, `concepts/subagent-orchestration-patterns.md.bak.20260507_174532`
- Captured raw source: `raw/articles/alphasignal-agent-orchestration-patterns-2026-05-05.md`
- Created: `concepts/agent-orchestration-production-tradeoffs.md`
- Updated: `concepts/subagent-orchestration-patterns.md`
- Updated: `index.md`
- Compiled AlphaSignal's four production orchestration patterns into a reusable decision framework: sequential for cost/scale, fan-out for latency, supervisor-worker for balanced production control, and reflexive loops only for low-volume high-stakes accuracy.

## [2026-05-08] closeout | Investment Watch final project knowledge
- Backups: `_backups/investment-watch-final-closeout-20260508_204319/`
- Created: `queries/investment-watch-final-closeout.md`
- Updated: `index.md`
- Captured the Investment Watch project as a locally validated typed, contract-backed, read-only investment observation system; runtime, cron, skill, memory, strategy, and data-repair promotion remain deferred pending separate approval.

## [2026-05-08] validation | Investment Watch public monitoring methodology outcome
- Backups: `_backups/investment-watch-concept-validation-20260508_204715/`
- Updated: `concepts/public-info-monitoring-automation-methodology.md`
- Added a short validation outcome linking [[investment-watch-final-closeout]] to the public-info monitoring methodology: higher-risk personal decision-support monitors need project-local boundaries, typed contracts, read-only/warning-only outputs, phase closeouts, and explicit non-promotion gates.


## [2026-05-09] ingest | Analytics Vidhya on Claude Code token saving
- Captured raw source: `raw/articles/analyticsvidhya-claude-code-token-saving-2026-05-08.md`
- Created: `concepts/ai-coding-assistant-context-budget-management.md`
- Updated: `concepts/claude-code-practical-workflow-tips.md`
- Backups: `index.md.bak.20260509_124115`, `log.md.bak.20260509_124115`, `claude-code-practical-workflow-tips.md.bak.20260509_124115`
- Compiled the article into a reusable concept about context-budget management for AI coding assistants: session boundaries, layered instructions, capped tool output, explicit file scope, subagent isolation, and version-gated tool settings.

## [2026-05-11] ingest | Progressive knowledge system growth
- Backups: `index.md.bak.20260511_160407`, `log.md.bak.20260511_160407`
- Captured raw source: `raw/articles/makeuseof-obsidian-perfect-vault-one-thing-2026-05-08.md`
- Created: `concepts/progressive-knowledge-system-growth.md`
- Updated: `index.md`
- Compiled the MakeUseOf Obsidian article into a reusable knowledge-system principle: use real problems to produce content first, then let structure, links, plugins, and automation grow from repeated friction.

## [2026-05-11] ingest | Anthropic Dreaming and agent experience consolidation
- Backups: `_backups/anthropic-dreaming-ingestion-20260511_175218/`
- Captured raw source: `raw/articles/venturebeat-anthropic-dreaming-ai-agents-2026-05-07.md`
- Created: `concepts/agent-experience-consolidation-loops.md`
- Created: `queries/hermes-agent-experience-consolidation-capability-assessment.md`
- Updated: `index.md`
- Compiled the VentureBeat/Anthropic Dreaming article into a reusable concept about agent experience consolidation loops, and recorded a Hermes capability assessment: current Hermes has memory, skills, session search, curator, cron, delegation, and goal/judge primitives, but full Auto Dream or `/dreaming` is not verified as native in the local v0.13.0 checkout.

## [2026-05-11] audit | Draft query inventory
- Created: `_meta/draft-query-inventory.md`
- Reviewed the eight unindexed `queries/` draft pages left out of `index.md`.
- Decision: no index promotion. Keep `project-kickoff-education-fund-weekly-page-v2.md` as the education-fund weekly-page resumption candidate; treat the older education-fund drafts, skill-install review drafts, and weekly-health enhancement drafts as superseded/generated kickoff drafts.
- No draft query pages were deleted or edited.

## [2026-05-11] tooling | Wiki health check automation
- Created: `_meta/wiki-health-check-automation-plan.md`
- Created: `_meta/scripts/wiki_health_check.py`
- Created: `_meta/wiki-health-check-runbook.md`
- Third-party review: Gemini CLI `gemini-2.5-flash` in read-only plan mode; no blocking findings. Accepted review fixes added exit-code semantics, detailed git status, notes semantics, and formal-page H1 exclusions.
- Verification: script JSON output passed with P0=0, P1=0, P2=8 known draft query pages; Markdown output path tested; no active Hermes runtime, memory, skill, cron, MCP, or gateway changes.

## [2026-05-11] ingest | InfoWorld on AI coding upstream skills
- Captured raw source: `raw/articles/infoworld-ai-coding-three-skills-2026-04-16.md`
- Updated: `concepts/dijkstra-ai-programming-formalization.md`
- Kept this as a source-backed supplement rather than a new concept page, because the article reinforces existing AI programming formalization principles: prompt/context quality, AI output verification, and preserving independent technical judgment.

## [2026-05-11] ingest | LangChain agent development lifecycle
- Captured raw source: `raw/articles/langchain-agent-development-lifecycle-2026-05-09.md`
- Created: `concepts/agent-development-lifecycle.md`
- Updated: `index.md`
- Compiled LangChain's lifecycle model into a Hermes-native concept: Build → Test → Deploy → Monitor, with Govern as a cross-cutting layer for cost, tool permissions, context/assets, traceability, and controlled promotion. No memory, skill, cron, runtime, or gateway changes were made.

## [2026-05-11] validate | Agent development lifecycle project mapping
- Updated: `concepts/agent-development-lifecycle.md`
- Evidence project: `/home/lin/.hermes/projects/amazon-price-watch`
- Evidence record: `docs/reviews/2026-05-11-agent-development-lifecycle-checklist.md`
- Recorded the first project-level validation outcome for the lifecycle concept: a low-risk live worker maps cleanly to Build → Test → Deploy → Monitor with Govern as the cross-cutting boundary. This does not authorize runtime, cron, skill, memory, or methodology promotion.

## [2026-05-13] ingest | TDS on spec-driven development
- Captured raw source: `raw/articles/towardsdatascience-vibe-coding-spec-driven-development-2026-05-12.md`
- Updated: `concepts/dijkstra-ai-programming-formalization.md`
- Updated: `concepts/hermes-ai-workflow-formalization-principles.md`
- Patched skill: `subagent-driven-development`
- Compiled the TDS article into the existing AI workflow formalization thread: for durable multi-session, multi-agent, or collaborative work, repo-local specs and validation records should be the source of truth rather than chat history. No memory, new skill, cron, runtime, MCP, wrapper, or Hermes core changes were made.

## [2026-05-13] governance | Wiki tag taxonomy
- Added reproducible audit script: `_meta/scripts/wiki_tag_audit.py`
- Updated: `SCHEMA.md` tag taxonomy into Core / Domain / Facet groups.
- Normalized first-pass formal-page aliases: `ai-agent` → `agent` in `concepts/typed-ai-agent-boundaries.md`; `benchmark` → `evaluation` in `concepts/agent-orchestration-production-tradeoffs.md`.
- Audit before: declared=18, undeclared_unique=96, undeclared_instances=246.
- Audit after schema update: declared=37, undeclared_unique=77, undeclared_instances=128.
- Audit after alias normalization: declared=37, undeclared_unique=77, undeclared_instances=126, duplicate_tag_files=0.
- Validation: wiki health pass=true, P0=0, P1=0, P2=8 known draft query pages; `git diff --check` passed.

## [2026-05-13] governance | Wiki tag taxonomy round 2
- Updated `SCHEMA.md` with stable recurring tags: `architecture`, `risk-control`, `deployment`, `lifecycle`, `optimization`, `model-profiles`.
- Normalized conservative aliases in frontmatter only: `ai-agent` → `agent`; `coding-agent` / `agent-workflow` → `ai-coding` or `agent` + `workflow`; `review` → `validation`; `process` / `execution` / `plan` → `workflow`; `rules` → `governance`; `benchmark` → `evaluation`.
- Left ambiguous tags such as `lifeos`, `kickoff`, `gstack`, `harness`, `pydantic`, `structured-output`, and `typed-boundary` unchanged.
- Audit before round 2: declared=37, undeclared_unique=77, undeclared_instances=126.
- Audit after round 2: declared=43, undeclared_unique=61, undeclared_instances=91, duplicate_tag_files=0.
- Validation: wiki health pass=true, P0=0, P1=0, P2=8 known draft query pages; `git diff --check` passed.

## [2026-05-13] governance | Wiki tag taxonomy round 3 decisions
- Updated `SCHEMA.md` with semantic decision tags: `lifeos` under Domain tags and `harness` under Facet tags.
- Decision: `lifeos` is a stable cross-domain LifeOS subject with a central overview page, so it belongs in taxonomy.
- Decision: `harness` is a stable Hermes/agent execution-environment facet and should stay distinct from `model-profiles`.
- Deferred: `gstack` remains unchanged because the main concept page is still `status: draft`; `kickoff` remains unchanged because it marks generated draft query pages. If a later draft-query cleanup handles `kickoff`, also handle `project-kickoff`.
- Audit before round 3: declared=43, undeclared_unique=61, undeclared_instances=91.
- Audit after round 3: declared=45, undeclared_unique=59, undeclared_instances=78, duplicate_tag_files=0.
- Validation: wiki health pass=true, P0=0, P1=0, P2=8 known draft query pages; `git diff --check` and `git diff --stat` passed.

## [2026-05-15] ingest | TDS on production AI Agent evaluation framework
- Captured raw source: `raw/articles/towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13.md`
- Created: `concepts/production-ai-agent-evaluation-framework.md`
- Updated: `index.md`
- Compiled the article into a reusable concept page about evaluating production AI Agents across retrieval, generation, agent behavior, and production operations. Preserved source thresholds only as directional benchmarks, not mandatory standards. No memory, skill, cron, runtime, MCP, wrapper, or Hermes core changes were made.

## [2026-05-15] governance | Draft query cleanup
- Deleted eight unindexed `queries/` draft pages previously reported as `known_unindexed_draft_query`.
- Updated: `_meta/draft-query-inventory.md`
- Decision: user requested full cleanup with no retained draft query pages; deleted drafts were not promoted to `index.md` and were not archived.
- Validation target: wiki health check should report P0=0, P1=0, P2=0 after cleanup.

## [2026-05-15] concept | Hermes skill refactoring methodology
- Created: `concepts/hermes-skill-refactoring-methodology.md`
- Updated: `index.md`
- Compiled the `test-driven-development` skill optimization into a reusable Hermes active-skill refactoring methodology: narrow default entry, front-loaded safety boundaries, reference routing with trigger terms, parent verification for delegated work, and independent review closeout.

## [2026-05-16] ingest | TDS on LLM summary identification step
- Captured raw source: `raw/articles/towardsdatascience-llm-summarizers-identification-step-2026-05-10.md`
- Created: `concepts/llm-summary-identification-step.md`
- Updated: `index.md`
- Cross-linked: `concepts/production-ai-agent-evaluation-framework.md`, `concepts/hermes-ai-workflow-formalization-principles.md`
- Compiled the article into a reusable concept page about treating summaries as evidence-backed claim objects: identify source support before generation, require support categories and evidence pointers, and constrain review stages to weakening/deletion/insufficient-evidence operations. Source fixture numbers were preserved only as directional observations, not mandatory thresholds.
- Follow-up patch after Claude review: documented raw-source frontmatter in `SCHEMA.md`, normalized the Gemini output path to `~/.hermes/...`, removed duplicate source URL and obvious DOM sharing/footer noise from the raw article, and unwrapped Summary wikilinks in the concept page.


## [2026-05-17] ingest | TDS on LLM engineering knowledge map
- Captured raw source: `raw/articles/towardsdatascience-must-know-topics-llm-engineer-2026-05-09.md`
- Created: `concepts/llm-engineering-knowledge-map.md`
- Updated: `index.md`
- Cross-linked: `concepts/llm-context-engineering-layer.md`, `concepts/production-ai-agent-evaluation-framework.md`, `concepts/llm-summary-identification-step.md`
- Backups: `index.md.bak.20260517_162624`, `log.md.bak.20260517_162624`, `llm-context-engineering-layer.md.bak.20260517_162624`, `production-ai-agent-evaluation-framework.md.bak.20260517_162624`, `llm-summary-identification-step.md.bak.20260517_162624`
- Compiled the article into a reusable LLM engineering map: representation, architecture, training/alignment, inference optimization, grounding/context, prompt interface, and evaluation/monitoring. The page is a concept/navigation layer, not an active skill, runtime change, or full LLM encyclopedia.


## [2026-05-17] ingest | MarkTechPost on repository-level code intelligence
- Captured raw source: `raw/articles/marktechpost-repowise-repository-code-intelligence-2026-05-15.md`
- Created: `concepts/repository-level-code-intelligence-layer.md`
- Updated: `index.md`
- Cross-linked: `concepts/ai-coding-assistant-context-budget-management.md`, `concepts/codex-agent-workflow-layering.md`, `concepts/claude-code-practical-workflow-tips.md`
- Backups: `index.md.bak.20260517_173555`, `log.md.bak.20260517_173555`, `ai-coding-assistant-context-budget-management.md.bak.20260517_173555`, `codex-agent-workflow-layering.md.bak.20260517_173555`, `claude-code-practical-workflow-tips.md.bak.20260517_173555`
- Compiled the article into a reusable repository intelligence concept: index the repo, build dependency graphs, rank core files, detect communities, use Git co-change signals, treat dead-code results as candidates, keep architecture decisions near source, and generate short AI context files. No Repowise default-tool, active skill, cron, runtime, MCP, or Hermes core change was made.
- Follow-up patch after Claude review: corrected the raw-source nested Jina provenance note, marked the concept as `draft` until local validation, unwrapped Summary wikilinks, and added the new page to related-page navigation lists.

## [2026-05-17] ingest | VentureBeat on frontier AI document fidelity risk
- Captured raw source: `raw/articles/venturebeat-frontier-ai-document-fidelity-risk-2026-05-13.md`
- Created: `concepts/ai-agent-document-fidelity-risk.md`
- Updated: `index.md`
- Cross-linked: `concepts/production-ai-agent-evaluation-framework.md`, `concepts/agent-self-validation-loops.md`, `concepts/typed-ai-agent-boundaries.md`
- Compiled the article into a reusable concept about multi-step AI Agent document-fidelity risk: frontier models may silently rewrite or distort content, generic tools can worsen degradation, and long workflows need short steps, diff/read-back evidence, reversible tests, narrow tools, and intermediate audit gates. DELEGATE-52 figures were preserved as source-specific directional benchmarks, not mandatory Hermes thresholds.
- Claude review: `_meta/reviews/2026-05-17-ai-agent-document-fidelity-risk-claude-review.md`; accepted minor patches removed duplicate raw metadata and added the `research` tag. A model-name anomaly in the raw source was verified against live VentureBeat HTML and preserved only as source text, not as a durable concept claim.

## [2026-05-18] ingest | Microsoft on Power Apps MCP closed-loop learning
- Captured raw source: `raw/articles/microsoft-power-apps-mcp-closed-loop-learning-2026-05-12.md`
- Created: `concepts/agent-closed-loop-learning-from-corrections-to-rules.md`
- Updated: `index.md`
- Cross-linked: `concepts/agent-experience-consolidation-loops.md`, `concepts/production-ai-agent-evaluation-framework.md`, `concepts/hermes-context-layer-operating-rules.md`
- Compiled the article into a reusable concept about Agent closed-loop learning: capture user corrections as structured memory, distill repeated corrections into candidate rules, validate through offline or shadow evaluation, and only then promote default behavior. Microsoft’s Power Apps MCP results were preserved as source-specific directional observations, not Hermes thresholds. No active skill, memory, cron, runtime, MCP, or wrapper change was made.
- Claude review: `_meta/reviews/2026-05-18-agent-closed-loop-learning-claude-review.md`; verdict `PASS_WITH_MINOR_FIXES`. Accepted the minor dedup patch that replaced the local routing decision tree with a link to `hermes-context-layer-operating-rules`. Rejected the reported stale index counter after `wiki_health_check` confirmed `formal_pages=79` and `index_wikilinks=79`; deferred optional SCHEMA raw-source provenance-field documentation as broader schema governance.

## [2026-05-18] governance | Wiki cleanup plan and schema alignment
- Created plan: `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`
- Created Claude review prompt/result: `_meta/reviews/2026-05-18-wiki-governance-cleanup-plan-claude-review-prompt.md`, `_meta/reviews/2026-05-18-wiki-governance-cleanup-plan-claude-review.md`
- Patched the plan for Claude findings: deferred status values, no bulk `queries/` type reclassification, `source_policy: normative` tooling gap, `_meta/` subdirectory roles, duplicate-tag verifier wording, copy-paste-safe commands, and sharper `operations/` stop condition.
- Updated `SCHEMA.md` for Lane A schema alignment: added `operations/` as a formal directory, expanded type/status guidance, documented source forms, added `source_policy: normative`, and clarified `_meta/plans/`, `_meta/reviews/`, `_meta/scripts/` roles.
- No content pages, page moves, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.

## [2026-05-18] governance | Wiki taxonomy round
- Updated `SCHEMA.md` taxonomy only; no page frontmatter or content pages were changed.
- Added stable recurring tags: `content-engineering`, `position-sizing`, `closeout`, `pydantic`, `structured-output`, `typed-boundary`.
- Deferred ambiguous/project-specific tags including `gstack`, `dreaming`, `project-development`, and `skill-files`.
- Audit before: declared=45, undeclared_unique=60, undeclared_instances=72.
- Expected audit after: declared=51, undeclared_unique=54, undeclared_instances=60; final validation recorded in the execution report.

## [2026-05-18] governance | Wiki long-page triage
- Created triage record: `_meta/plans/2026-05-18-long-page-triage.md`
- Scanned formal pages above the 200-line guideline and classified the first five high-priority pages.
- Recommended first future target: `queries/hermes-harness-profile-validation-detailed-plan.md` as `move execution detail`.
- No long page content, page metadata, page paths, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.

## [2026-05-18] governance | Hermes harness validation page split/compression plan
- Created page-specific plan: `_meta/plans/2026-05-18-hermes-harness-profile-validation-split-compression-plan.md`
- Target page: `queries/hermes-harness-profile-validation-detailed-plan.md`
- Decision baseline: keep the target path by default; compress it later into a compact navigation/decision page; route workstream templates, scripts, fixtures, and task bodies to existing project-local evidence instead of keeping them inline in the query page.
- Archive default: use git history and existing project-local closeout/evidence; do not create a duplicate `_meta/` full-text archive unless explicitly approved.
- Claude review prompt/result: `_meta/reviews/2026-05-18-hermes-harness-profile-validation-split-compression-plan-claude-review-prompt.md`, `_meta/reviews/2026-05-18-hermes-harness-profile-validation-split-compression-plan-claude-review.md`.
- Claude verdict: `APPROVE_WITH_CHANGES`; no blocking findings. Accepted patches clarified frontmatter freeze, Gate 6 inclusion, wiki final closeout pre-check, clean committed pre-edit snapshot wording, line-count discrepancy, and authoritative defaults.
- No target page content, page metadata, page paths, project-local files, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.

## [2026-05-18] governance | Hermes harness validation long-page compression
- Compressed target page: `queries/hermes-harness-profile-validation-detailed-plan.md`
- Followed reviewed plan: `_meta/plans/2026-05-18-hermes-harness-profile-validation-split-compression-plan.md`
- Replaced inline project skeletons, templates, prompt bodies, fixtures, scripts, and workstream task bodies with a compact navigation/decision page and pointers to project-local evidence.
- Preserved target path, title, frontmatter, tags, `type`, and `status`; no index update was required.
- Included Gate 6 post-patch regression in the gate summary and linked the wiki final closeout.
- No browsable full-text archive was created; git history plus project-local evidence remain the archive.
- No project-local files, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.
- Claude implementation review prompt/result: `_meta/reviews/2026-05-18-hermes-harness-profile-validation-compression-implementation-claude-review-prompt.md`, `_meta/reviews/2026-05-18-hermes-harness-profile-validation-compression-implementation-claude-review.md`.
- Claude verdict: `PASS`; no blocking or important findings, no required patches.

## [2026-05-18] governance | Hermes project dev migration closeout/compression plan
- Created page-specific plan: `_meta/plans/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan.md`
- Target page: `queries/hermes-project-dev-migration-plan-eng-review.md`
- Triage class: `Closeout compress`.
- Decision baseline: keep the target path/frontmatter unchanged later; compress into a historical engineering decision record; replace detailed layouts, diagrams, and phase checklists with pointers to current project-local evidence and related wiki pages.
- Archive default: use git history; do not create a duplicate `_meta/` archive unless explicitly approved.
- Claude review prompt/result: `_meta/reviews/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan-claude-review-prompt.md`, `_meta/reviews/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan-claude-review.md`.
- Claude verdict: `APPROVE_WITH_CHANGES`; no blocking findings. Accepted patches added the index pre-check/stop condition, preserve-verbatim frontmatter stub, unconditional investment-watch closeout pointer, and final-verdict completion-summary guidance.
- No target page content, page metadata, page paths, project-local files, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.

## [2026-05-18] governance | Hermes project dev migration long-page compression
- Compressed target page: `queries/hermes-project-dev-migration-plan-eng-review.md`
- Followed reviewed plan: `_meta/plans/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan.md`
- Replaced detailed layouts, diagrams, phase checklists, and execution-heavy migration steps with a compact historical engineering decision record.
- Preserved target path, title, frontmatter, tags, `type`, and `status`; no `index.md` update was required.
- Evidence pointers retained: `queries/hermes-project-dev-office-hours-review.md`, `queries/investment-watch-final-closeout.md`, `/home/lin/.hermes/projects/investment-watch/`, and `/home/lin/.hermes/projects/project-kickoff/`.
- Recorded that no `project-kickoff` wiki closeout/status page was found; this remains a follow-up gap, not part of the compression commit.
- No browsable full-text archive was created; git history remains the archive.
- No project-local files, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.
- Claude implementation review prompt/result: `_meta/reviews/2026-05-18-hermes-project-dev-migration-compression-implementation-claude-review-prompt.md`, `_meta/reviews/2026-05-18-hermes-project-dev-migration-compression-implementation-claude-review.md`.
- Claude verdict: `PASS`; no blocking or important findings, no required patches.

## [2026-05-18] governance | Hermes LifeOS executable architecture split plan
- Created page-specific split concept plan: `_meta/plans/2026-05-18-hermes-lifeos-executable-architecture-split-plan.md`
- Target page: `concepts/hermes-lifeos-executable-architecture.md`
- Triage class: `Split concept`.
- Decision baseline: keep the target as the stable architecture hub; do not edit the target page in this step; if implemented later, split only the layer-boundary contract first unless separately approved.
- Candidate future split pages: `concepts/hermes-lifeos-layer-boundary-contract.md`, `concepts/hermes-lifeos-topology-and-profile-policy.md`, and `concepts/hermes-lifeos-promotion-operating-policy.md`.
- Archive default: use git history; do not create a duplicate `_meta/` archive unless explicitly approved.
- Claude review prompt/result: `_meta/reviews/2026-05-18-hermes-lifeos-executable-architecture-split-plan-claude-review-prompt.md`, `_meta/reviews/2026-05-18-hermes-lifeos-executable-architecture-split-plan-claude-review.md`.
- Claude verdict: `PASS_WITH_MINOR_FIXES`; no blocking or important findings. Accepted minor patches clarified the boundary-contract differentiation gate, the no-archive log wording, and the default answer to the first split question.
- No target page content, page metadata, page paths, index entries, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Hermes LifeOS layer boundary contract split
- Executed reviewed split plan: `_meta/plans/2026-05-18-hermes-lifeos-executable-architecture-split-plan.md`
- Created concept page: `concepts/hermes-lifeos-layer-boundary-contract.md`
- Updated hub page: `concepts/hermes-lifeos-executable-architecture.md`
- Updated `index.md` with exactly one new Concepts entry and incremented total pages from 79 to 80.
- Split scope: extracted/restated the hard layer-boundary contract while keeping the hub as the stable LifeOS architecture page.
- Differentiation gate honored: the new page emphasizes LifeOS topology and `profile` as runtime-state isolation, rather than duplicating the generic context-layer routing map.
- Archive default followed: no `_meta/` archive was created; git history remains the rollback source.
- Claude implementation review prompt/result: `_meta/reviews/2026-05-18-hermes-lifeos-layer-boundary-contract-split-implementation-claude-review-prompt.md`, `_meta/reviews/2026-05-18-hermes-lifeos-layer-boundary-contract-split-implementation-claude-review.md`.
- Claude verdict: `PASS`; no blocking or important findings. Minor note about the hub `updated` field was recorded and later addressed in the follow-up fix below.
- No memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Hermes LifeOS split review minor fix
- Applied Claude minor finding from `_meta/reviews/2026-05-18-hermes-lifeos-layer-boundary-contract-split-implementation-claude-review.md`.
- Updated hub frontmatter only: `concepts/hermes-lifeos-executable-architecture.md` `updated: 2026-04-21` -> `updated: 2026-05-18`.
- No page body, links, index entries, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Wiki governance cleanup closeout
- Created closeout report: `_meta/reviews/2026-05-18-wiki-governance-cleanup-closeout.md`.
- Recorded final health, tag audit deltas, completed schema/taxonomy/long-page work, accepted risks, and remaining backlog.
- No content pages, index entries, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Public info monitoring methodology navigation
- Updated: `concepts/public-info-monitoring-automation-methodology.md`.
- Added a compact decision card and navigation section at the top, following the long-page triage recommendation to add summary/navigation rather than split the page.
- Updated only the page `updated` date and top navigation content; no index entries, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Gstack taxonomy decision
- Promoted `gstack` to a declared facet tag in `SCHEMA.md`.
- Updated `concepts/gstack-project-execution-lane.md` with the decision: `gstack` is a gstack-derived review/execution lens tag, not a new entity/project page by default.
- No index entries, memory, skills, cron, runtime, MCP, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Wiki audit source/schema checks
- Enhanced `_meta/scripts/wiki_health_check.py` to emit P2 warnings for missing `sources`, unexpected source forms, and non-durable `/tmp/...` source paths.
- Fixed `_meta/scripts/wiki_tag_audit.py` so declared tag parsing stops before the `Rules:` prose block and does not count rule examples as declared tags.
- Updated `SCHEMA.md` to record that source-form validation is now health-check coverage, while `source_policy: normative` itself remains a documentation marker.
- Validation after the script change: health `pass=true`, `P0=0`, `P1=0`, `P2=20` newly surfaced source-maintenance warnings; tag audit has no high-frequency undeclared candidates.

## [2026-05-18] governance | Gstack wiki cleanup
- User requested direct removal of the `gstack` tag and related wiki pages.
- Deleted pages: `concepts/gstack-project-execution-lane.md`, `queries/gstack-project-execution-lane-validation-case.md`, `queries/hermes-project-dev-office-hours-review.md`, `queries/hermes-project-dev-migration-plan-eng-review.md`.
- Removed `gstack` from `SCHEMA.md`, removed deleted pages from `index.md`, and removed active wikilinks from remaining formal pages.
- Updated `index.md` total pages from 80 to 76.
- No memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-18] governance | Source P2 cleanup
- Normalized Hermes official docs sources from local absolute paths to `docs:hermes-agent/...` references in the layer-routing pages.
- Replaced non-durable `/tmp/...` skill-refactor sources with `session:2026-05-15-...` evidence handles in `concepts/hermes-skill-refactoring-methodology.md`.
- Target: return wiki health check to `P0=0`, `P1=0`, `P2=0` without changing page bodies or active Hermes runtime layers.

## [2026-05-20] ingest | MachineLearningMastery on prompt engineering for agentic AI
- Captured raw source: `raw/articles/machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19.md`
- Created concept page: `concepts/agent-context-engineering.md`
- Updated `index.md` total pages from 76 to 77.
- Followed Gemini independent review: emphasized Just-in-time context assembly and Context Rot defense, linked tool-boundary details to `typed-ai-agent-boundaries` instead of duplicating them.
- Boundary: no memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-20] fix | Agent context engineering Claude review follow-up
- Applied accepted Claude review findings for `concepts/agent-context-engineering.md`.
- Clarified the boundary with `concepts/hermes-context-layer-operating-rules.md` in the relationship section and state-mapping paragraph.
- Added a reverse related link from `concepts/hermes-context-layer-operating-rules.md` to `concepts/agent-context-engineering.md` and updated its `updated` date.
- Fixed the raw-source wikilink in the new concept page summary by removing code formatting around `[[machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19]]`.
- Boundary: no memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-20] concept | Agent failure closed-loop evaluation
- Created concept page: `concepts/agent-failure-closed-loop-evaluation.md`.
- Updated `index.md` total pages from 77 to 78.
- Captured the Hermes-level method: failure signal → neutral evidence → root cause class → minimal fix → regression evaluator/case → human approval before active-layer mutation.
- Boundary: no memory, cron, MCP config, profile, runtime config, wrappers, quick commands, `SOUL.md`, or Hermes core files were changed.

## [2026-05-21] ingest | MachineLearningMastery on agentic programming as system engineering
- Captured raw source: `raw/articles/machinelearningmastery-agentic-programming-roadmap-2026-05-20.md`.
- Created concept page: `concepts/agentic-programming-system-engineering.md`.
- Updated `index.md` total pages from 78 to 79.
- Preserved the source limitation: direct publisher fetch returned Cloudflare 403, so the raw capture uses Jina Reader text while preserving the original Source URL.
- Durable unit: Agentic programming as software/system engineering, with negative tool constraints, behavioral drift, minimal shared context, and layered memory routing.
- Boundary: no memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.

## [2026-05-21] review-fix | Agentic programming wiki Claude review follow-up
- Applied accepted Claude review findings for `concepts/agentic-programming-system-engineering.md` and `raw/articles/machinelearningmastery-agentic-programming-roadmap-2026-05-20.md`.
- Added inline canonical links for negative tool constraints and minimal shared context to reduce overlap with `agent-context-engineering` and `typed-ai-agent-boundaries`.
- Removed system/navigation links from the concept `Related` section and normalized the raw source `summary_path` to `~/.hermes/...`.
- Boundary: no memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files were changed.
## [2026-05-21] ingest | TDS on agent planning with operations research
- Captured raw source: `raw/articles/towardsdatascience-agent-planning-operations-research-2026-05-20.md`
- Created: `concepts/agent-resource-optimization.md`
- Updated: `concepts/agent-orchestration-production-tradeoffs.md`
- Updated: `index.md`
- Compiled the article into a reusable concept page about modeling multi-agent capability coverage, budget selection, task assignment, and routing cost as explicit optimization problems.
- Active-layer boundary: no memory, skill, cron, MCP, profile, or runtime change was promoted; numeric examples remain illustrative synthetic data.
## [2026-05-21] review | Claude review of agent resource optimization ingestion
- Reviewer: Claude Code read-only review.
- Verdict: PASS_WITH_MINOR_FIXES.
- Accepted fixes: added `created`/`updated` to the raw source frontmatter, replaced the off-wiki summary output path with a run-level note, and removed `[[index]]`/`[[log]]` navigation links from the new concept `Related` section.
- Rejected/escalated findings: none; no blocking findings were reported.

## [2026-05-22] ingest | MachineLearningMastery multi-agent research assistant
- Captured raw source: `raw/articles/machinelearningmastery-multi-agent-research-assistant-2026-05-21.md`
- Created: `concepts/agent-research-evidence-gate.md`
- Updated: `concepts/production-ai-agent-evaluation-framework.md`
- Updated: `concepts/agent-orchestration-production-tradeoffs.md`
- Updated: `index.md`
- Compiled the article into a reusable concept about research-agent evidence gates: Manager orchestrates, tools gather source-backed evidence, Judge scores sufficiency and missing information, and Analyst writes only after the gate passes. Active-layer promotion remains deferred pending separate project-local validation and approval.

## [2026-05-22] review | Agent research evidence gate AGY independent review
- Review prompt: `_meta/reviews/2026-05-22-agent-research-evidence-gate-agy-review-prompt.md`
- Review result: `_meta/reviews/2026-05-22-agent-research-evidence-gate-agy-review.md`
- Verdict: PASS_WITH_MINOR_FIXES
- Patched accepted findings: updated frontmatter dates on two touched concept pages and normalized mixed-language `targeted补证` wording.
- Rejected finding: manual index count mismatch, because deterministic health check reported `Formal pages: 81` and `Index wikilinks: 81`.

## [2026-05-22] ingest | NVIDIA multi-agent financial signal discovery
- Captured raw source: `raw/articles/nvidia-financial-signal-discovery-multi-agent-2026-05-21.md`
- Created: `concepts/constrained-toolbox-evaluator-loop.md`
- Updated: `concepts/typed-ai-agent-boundaries.md`
- Updated: `concepts/production-ai-agent-evaluation-framework.md`
- Updated: `concepts/agent-orchestration-production-tradeoffs.md`
- Updated: `index.md` total pages from 81 to 82.
- Durable unit: constrained toolbox + structured blueprint + executable artifact + objective evaluator feedback loop.
- Boundary: Rank IC thresholds, NVIDIA NIM/NeMo/Nemotron, and article-specific financial formulas remain source-specific; no memory, skill, cron, MCP, profile, runtime, wrapper, or Hermes core change was promoted.

## [2026-05-22] review | Constrained toolbox evaluator loop AGY independent review
- Review prompt: `_meta/reviews/2026-05-22-constrained-toolbox-evaluator-loop-agy-review-prompt.md`
- Review result: `_meta/reviews/2026-05-22-constrained-toolbox-evaluator-loop-agy-review.md`
- Verdict: PASS_WITH_MINOR_FIXES
- Patched accepted findings: normalized raw source `type` to `raw-source`, added reverse links from related concept pages, and cleaned vertically split formula fallback text in the raw capture.
- Blocking/important findings: none.

## [2026-05-25] ingest | TDS hybrid AI deterministic analytics
- Captured raw source: `raw/articles/towardsdatascience-hybrid-ai-deterministic-analytics-2026-05-22.md`
- Created: `concepts/deterministic-analytics-llm-reasoning-boundary.md`
- Updated: `index.md` total pages from 82 to 83.
- Durable unit: separate LLM planning/explanation from deterministic data filtering, aggregation, calculation, and fact generation.
- Boundary: Copilot Studio, the article's manufacturing assessment schema, numeric examples, and supported analysis types remain source-specific; no memory, skill, cron, MCP, profile, runtime, wrapper, or Hermes core change was promoted.

## [2026-05-25] review | Deterministic analytics boundary AGY independent review
- Review prompt: `_meta/reviews/2026-05-25-deterministic-analytics-llm-boundary-agy-review-prompt.md`
- Review result: `_meta/reviews/2026-05-25-deterministic-analytics-llm-boundary-agy-review.md`
- Verdict: PASS_WITH_MINOR_FIXES
- Patched accepted findings: added reverse links from `typed-ai-agent-boundaries`, `constrained-toolbox-evaluator-loop`, `hermes-ai-workflow-formalization-principles`, and `production-ai-agent-evaluation-framework` to `deterministic-analytics-llm-reasoning-boundary`.
- Blocking/important findings: none.

## [2026-05-25] ingest | Microsoft Agent Skills provider governance boundary
- Captured raw source: `raw/articles/microsoft-devblogs-agent-skills-python-provider-2026-05-24.md`
- Created: `concepts/agent-skill-provider-governance-boundary.md`
- Updated: `index.md` total pages from 83 to 84.
- Durable unit: multi-form skill sources can share a provider abstraction, but active exposure requires explicit source layering, filtering, conflict handling, script approval, sandboxing, and audit boundaries.
- Boundary: Microsoft Agent Framework API names, decorator details, Foundry/Azure client choices, and `require_script_approval` remain source-specific examples; no memory, skill, cron, MCP, profile, runtime, wrapper, or Hermes core change was promoted.
