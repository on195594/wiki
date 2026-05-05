# Wiki Index

> Hermes 长期知识目录。
> 这里记录正式沉淀页面，不记录原始聊天。
> Last updated: 2026-05-05 | Total pages: 61

## Entities

## Concepts
- [[ai-coding-agent-workflow-types]] — AI coding agent 的四类工作流：IDE、Terminal、PR、Cloud，按交互模式而不是品牌选择执行入口
- [[agentic-content-pipeline-design-patterns]] — Agentic 内容生产 pipeline 的设计模式：专家流程、skill files、MCP 数据源、中间产物、人工审核与可调试迭代
- [[claude-code-practical-workflow-tips]] — Claude Code 的实用工作流要点：侧边提问、浏览器验证、自动循环、多目录访问与跨设备延续
- [[codex-agent-workflow-layering]] — Codex 的分层 agent 工作流：prompt、planning、AGENTS.md、skill、MCP 与 automation 各司其职
- [[companyos-to-lifeos-filesystem-philosophy]] — 将公司和人生建模为文件系统：统一命名空间、文件即状态、权限即治理、读写即操作
- [[dijkstra-ai-programming-formalization]] — Dijkstra 对自然语言编程的批判在 AI 编程时代的再验证：形式化约束仍是核心
- [[family-education-operating-model]] — 家庭教育域的 operating model：以孩子适配、家庭可持续和教育兜底能力为核心，而不是单点名校最优化
- [[google-sre-gemini-cli-incident-response]] — Google SRE 如何把 Gemini CLI 接入事故响应：标准 playbook、受控执行、人机协作止血
- [[gstack-project-execution-lane]] — 把 5 个最实用的 gstack skill 串成默认项目推进链：从 office-hours、计划评审到 review 和 QA 的执行编排层
- [[hermes-agent-workflow-layering-and-adoption-order]] — 把 Codex 的分层工作流翻译成 Hermes 现有架构：指令层、知识层、skills、MCP、验证与 cron 的落地顺序
- [[hermes-ai-workflow-formalization-principles]] — 将 Dijkstra 的形式化原则落实到 Hermes 工作流：自然语言输入、形式化产物、验证闭环
- [[hermes-context-engineering-design-priorities]] — 面向 Hermes 的 context engineering 设计优先级：先做 budget、ranking、compression，再做 history decay
- [[hermes-context-layer-operating-rules]] — Hermes 上下文分层操作规则：session、memory、skill、wiki、project state、cron/log 与 subagent 的职责边界和升级路径
- [[hermes-knowledge-architecture]] — Hermes 知识库整体架构：运行时知识栈、wiki 文件结构、检索与回写闭环
- [[hermes-knowledge-base-operating-flow]] — 当前知识库的端到端操作流：输入、分类、raw、编译、检索、维护
- [[hermes-lifeos-executable-architecture]] — Hermes 版 LifeOS 的可执行架构：default profile 为主脑，wiki/memory/skills/cron/MCP/profiles 严格分层并按边界推进
- [[hermes-layer-routing-decision-checklist]] — Hermes 的层间路由判定清单：什么进 wiki、memory、skill、cron、MCP，按官方定义和本地知识层分开判断
- [[hermes-memory-governance-notes]] — 一次实际 memory 减脂后沉淀出的治理规则：什么该继续留在 memory，什么该迁移到 wiki、skill 或 session
- [[hermes-model-specific-harness-profiles]] — Hermes 的 model-specific harness profile 原则：把 Codex、Claude、Gemini 的模型差异转成 skill / wrapper / project context / verification overlay，而不是贸然扩张 runtime profile
- [[hermes-memory-skills-wiki-boundaries]] — Hermes memory / skills / wiki 的边界规范与归类准则
- [[hermes-retrieval-priority-and-answer-path]] — Hermes 检索优先级与回答路径：先查 wiki，再按 memory/skills/sessions/external 补全
- [[hermes-wiki-lint-and-health-check-standards]] — Hermes wiki lint / 健康检查规范：链接、索引、frontmatter、标签、陈旧性与结构健康
- [[hermes-wiki-page-writing-standards]] — Hermes wiki 页面写作规范：命名、frontmatter、结构、wikilinks 与质量检查
- [[lifeos-overview]] — LifeOS 总览页：定义人生操作系统的一级领域、系统层次和 Hermes 在其中的执行内核角色
- [[llm-context-engineering-layer]] — Context engineering 作为 RAG 与 prompt 之间的中间层：管理 memory、compression、re-ranking 与 token budget
- [[leontraveller-trading-and-investment-system]] — Leontraveller 的交易系统观：不抄底、不和市场争辩，转向顺势、止损、控回撤与简单可执行规则
- [[money-as-tool-and-investment-vs-consumption-framework]] — 财富决策框架：把钱当作工具，区分资产投资、自我投资与纯消费
- [[ordinary-investor-investment-system]] — 普通人投资方法论：先搭建长期系统，再谈标的、仓位与执行
- [[personal-finance-and-education-fund-model]] — 财务与教育基金 operating model：把家庭安全层、配置层和目标层分开，让教育基金按目标导向独立建模
- [[personal-growth-operating-model]] — 个人成长域的 operating model：把成长作为职业升级、家庭沟通与判断质量的底层引擎
- [[system-governance-operating-model]] — 系统治理域的 operating model：管理 Hermes LifeOS 的分层边界、沉淀路径、扩张节奏与结构健康
- [[typed-ai-agent-boundaries]] — 用 Pydantic AI 的 structured output、typed tools 与 dependency injection 把 LLM 不确定性收进可验证的工程边界
- [[personal-investment-operating-rules]] — 个人投资操作守则：核心仓做配置，进攻仓做趋势，先保护本金再争取收益
- [[wiki-ingestion-workflow]] — 把外部信息编译进知识库的标准入库流程
- [[work-and-career-operating-model]] — 工作与职业域的 operating model：兼顾现金流、能力复利、时间预算与家庭兼容性

## Operations
- [[hermes-health-dashboard]] — Hermes 周度治理线的运行面板：版本、cron、memory、browser 状态与每周健康报告契约

## Comparisons
- [[dijkstra-ewd667-vs-ai-programming-article]] — 对照 EWD667 原文与 2026 AI 编程文章：哪些原则不变，哪些是 AI 时代的新变量
- [[hermes-vs-google-sre-agentic-incident-response]] — 对照 Google 的 incident copilot 与 Hermes 当前底座：相同架构方向、不同产品收敛层
- [[leontraveller-vs-ordinary-investor-investment-system]] — 对照两套投资框架：长期配置制度 vs 主动交易纪律

## Queries
- [[gstack-project-execution-lane-validation-case]] — 用真实小项目验证 gstack 5-skill lane 的闭环价值：从 intake、review 到 QA，确认它能把模糊想法压成可推进的 kickoff artifact
- [[hermes-project-dev-office-hours-review]] — Hermes 项目开发环境的 office-hours 审查：识别 `~/.hermes` 中项目代码、状态、脚本、cron 与文档混杂的问题
- [[hermes-project-dev-migration-plan-eng-review]] — Hermes 项目开发迁移计划 eng review：将具备独立边界的内容迁移到项目目录，恢复项目级执行单元
- [[hermes-layer-routing-edge-cases]] — Hermes 层间路由的边界误判案例：当两个层都像能放时，如何按职责而不是重要性裁决
- [[hermes-layer-routing-sample-cases]] — Hermes 层间路由的样板案例：用真实场景判断什么该进 wiki、memory、skill、cron、MCP 或 session
- [[hermes-optimization-sample-case]] — 用当前知识库操作流回放最近优化 Hermes 的全过程，展示如何把对话收敛成长期资产
- [[how-i-should-use-hermes-for-ai-coding-with-typed-boundaries]] — 用 typed output、窄工具、显式依赖和验证 gate，把 Pydantic AI 的边界原则转成我使用 Hermes 做 AI 编程的默认最佳实践
- [[hermes-system-model-specific-harness-optimization-plan]] — 基于 Deep Agents harness profiles 原则制定 Hermes 系统优化计划：稳定 default 主脑，先做 overlay registry、小 eval，再决定 skill/profile/cron 推广
- [[hermes-harness-profile-validation-detailed-plan]] — Hermes harness profile 验证项目详细计划书：项目结构、prompt overlay、eval rubric、实验记录、promotion gates 与 rollback/safety 边界
- [[hermes-harness-profile-validation-final-closeout]] — Hermes harness profile 验证项目最终结论：只推广 planning/code-review 两个窄 skill patch，不推广 summary、coding/config、runtime profile、core、SOUL、cron 或 memory
- [[how-i-should-use-these-two-investment-frameworks]] — 如何在日常决策中分层使用两套投资框架：长期制度管底盘，主动纪律管进攻
- [[my-investment-pre-trade-checklist]] — 下单前检查清单：先分清资金层、动作类型、退出计划，再决定是否出手
- [[when-i-should-not-trade]] — 不该出手的场景清单：补亏损、情绪单、越权单、无退出计划时默认停手
- [[how-i-should-review-a-losing-position]] — 亏损仓位复盘：先分清仓位层次，再判断是正常回撤、该认错，还是被包装成再平衡的情绪补仓
- [[how-i-should-scale-into-and-out-of-a-position]] — 仓位分批进出规则：对了再加、错了不补、减仓先服务于风险管理
- [[how-i-should-size-a-position]] — 仓位大小规则：先看错了能亏多少，再决定能下多大，不让 conviction 取代风险预算
- [[how-i-should-handle-a-winning-position]] — 盈利仓处理规则：强时拿住，减仓先看是否真在做风险管理而不是利润焦虑
- [[how-i-should-decide-between-doing-nothing-and-taking-action]] — 等待与出手的裁决规则：当动作只是缓解不舒服时，默认继续等
- [[how-i-should-build-a-post-trade-review-loop]] — 交易后复盘闭环：先看过程是否合格，再把复盘压成下一轮可执行的规则修正
- [[how-i-should-detect-repeat-mistakes-in-my-trading]] — 识别重复错误：只有可命名、可复现、可归因的问题，才值得升级成硬规则
- [[how-i-should-convert-trading-lessons-into-hard-rules]] — 教训到硬规则的转化：只有反复出现、代价够大、且能压成明确动作的，才值得制度化
- [[how-i-should-keep-my-trading-system-small-and-executable]] — 交易系统做减法：保留少数高阻断力规则，删除不能被快速调用的说明书式规则
