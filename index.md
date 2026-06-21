# Wiki Index

> Hermes 长期知识目录。
> 这里记录正式沉淀页面，不记录原始聊天。
> Last updated: 2026-06-21 | Total pages: 90

## Entities

## Concepts
- [[agent-development-lifecycle]] — Agent 开发生命周期：以 Build → Test → Deploy → Monitor 闭环和 Govern 横切层，把一次性 demo 推进成可验证、可部署、可监控、可治理的工程系统
- [[agent-closed-loop-learning-from-corrections-to-rules]] — Agent 闭环学习：把用户纠错先保存为结构化记忆，再经规则蒸馏、影子/离线评估和显式推广，升级为默认行为
- [[agent-context-engineering]] — Agent 上下文工程：用即时装配、最小必要上下文、工具反向边界和状态裁剪，防止 context rot 与多步执行偏航
- [[ai-assumption-challenger-before-execution]] — AI 执行前假设挑战者：在复杂创意、方案设计或 Hermes PM 编排前，用反迎合角色澄清意图、挑战假设、发现盲点，再进入执行
- [[loop-engineering-hermes-agent-workflow]] — Loop Engineering 在 Hermes 中的映射：把发现、隔离执行、验证、外部状态和下一步决策组织成可审计 agent 工作闭环，同时保留 active-layer 审批边界
- [[agentic-programming-system-engineering]] — Agentic programming 的系统工程边界：把 Agent 视为带状态、工具、记忆和目标管理的执行系统，用负向工具约束、最小上下文、行为漂移治理和分层记忆降低生产风险
- [[ai-agent-human-outcome-design-principle]] — AI Agent 项目设计的人类结果优先原则：先验证真实问题、可衡量结果和人类信任边界，再决定模型、自动化和 human-in-the-loop 范围
- [[agent-experience-consolidation-loops]] — Agent 经验固化闭环：从历史任务、失败、成功路径和用户纠正中提取可复用经验，并按 memory/skill/wiki/closeout/evaluator/cron 分层路由
- [[agent-failure-closed-loop-evaluation]] — Agent 失败闭环评估：把可复发失败从失败信号、中立证据、根因分类推进到最小修复和防回归 evaluator/case
- [[agent-orchestration-production-tradeoffs]] — Agent 编排的生产取舍：按成本/规模、延迟、平衡控制或高风险准确率选择 sequential、fan-out、supervisor-worker 或 reflexive loop
- [[agent-resource-optimization]] — Agent 资源优化：用集合覆盖、分配、背包和网络流视角建模多 Agent 的能力覆盖、预算选择、任务分派与路由成本
- [[agent-research-evidence-gate]] — 研究型 Agent 的证据质量闸门：Manager 编排、工具取证、Judge 评分和缺口补证，达标后 Analyst 才生成报告
- [[agent-self-validation-loops]] — Agent 自我验证闭环：用 baseline、测试、浏览器/MCP 反馈和停止条件，把 coding agent 任务变成可验证迭代回路
- [[agent-skill-provider-governance-boundary]] — Agent Skill Provider 治理边界：把文件、类和内联技能统一到 provider 抽象下，同时用分层来源、过滤、去重、审批和沙箱控制 active skill 风险
- [[constrained-toolbox-evaluator-loop]] — 受限工具箱评估闭环：把创造型 Agent 拆成候选生成、可执行转换、客观 evaluator 和反馈迭代，降低幻觉并保留审计边界
- [[deterministic-analytics-llm-reasoning-boundary]] — 确定性分析与 LLM 推理边界：让 LLM 生成结构化分析规约和解释结果，让确定性执行器负责过滤、聚合、计算和事实生成
- [[ai-agent-document-fidelity-risk]] — AI Agent 文档保真风险：多轮委托式工作流中模型可能悄悄重写、扭曲或幻觉原文，需用短步骤、diff、可逆验证、受限工具和中间态审计控制风险
- [[production-ai-agent-evaluation-framework]] — 生产级 AI Agent 评估框架：用检索、生成、Agent 行为和生产运营四层指标评估可靠性，阈值只保留为数量级参考
- [[ai-coding-agent-workflow-types]] — AI coding agent 的四类工作流：IDE、Terminal、PR、Cloud，按交互模式而不是品牌选择执行入口
- [[ai-coding-assistant-context-budget-management]] — AI coding assistant 的上下文预算管理：限制历史、文件、工具输出、日志和全局指令进入模型，降低 token 成本和上下文漂移
- [[repository-level-code-intelligence-layer]] — 仓库级代码智能层：用索引、依赖图、中心性排序、Git 共变、死代码候选和架构决策记录，为 AI coding agent 生成低噪音项目上下文
- [[agentic-content-pipeline-design-patterns]] — Agentic 内容生产 pipeline 的设计模式：专家流程、skill files、MCP 数据源、中间产物、人工审核与可调试迭代
- [[claude-code-practical-workflow-tips]] — Claude Code 的实用工作流要点：侧边提问、浏览器验证、自动循环、多目录访问与跨设备延续
- [[codex-agent-workflow-layering]] — Codex 的分层 agent 工作流：prompt、planning、AGENTS.md、skill、MCP 与 automation 各司其职
- [[companyos-to-lifeos-filesystem-philosophy]] — 将公司和人生建模为文件系统：统一命名空间、文件即状态、权限即治理、读写即操作
- [[dijkstra-ai-programming-formalization]] — Dijkstra 对自然语言编程的批判在 AI 编程时代的再验证：形式化约束仍是核心
- [[family-education-operating-model]] — 家庭教育域的 operating model：以孩子适配、家庭可持续和教育兜底能力为核心，而不是单点名校最优化
- [[google-sre-gemini-cli-incident-response]] — Google SRE 如何把 Gemini CLI 接入事故响应：标准 playbook、受控执行、人机协作止血
- [[hermes-agent-workflow-layering-and-adoption-order]] — 把 Codex 的分层工作流翻译成 Hermes 现有架构：指令层、知识层、skills、MCP、验证与 cron 的落地顺序
- [[hermes-ai-workflow-formalization-principles]] — 将 Dijkstra 的形式化原则落实到 Hermes 工作流：自然语言输入、形式化产物、验证闭环
- [[hermes-context-engineering-design-priorities]] — 面向 Hermes 的 context engineering 设计优先级：先做 budget、ranking、compression，再做 history decay
- [[hermes-context-layer-operating-rules]] — Hermes 上下文分层操作规则：session、memory、skill、wiki、project state、cron/log 与 subagent 的职责边界和升级路径
- [[hermes-knowledge-architecture]] — Hermes 知识库整体架构：运行时知识栈、wiki 文件结构、检索与回写闭环
- [[hermes-knowledge-base-operating-flow]] — 当前知识库的端到端操作流：输入、分类、raw、编译、检索、维护
- [[hermes-python-engineering-capability-checklist]] — Hermes Python 工程能力检查清单：流式输入、资源生命周期、有界并发、类型化工具边界与验证闭环
- [[hermes-skill-refactoring-methodology]] — Hermes active skill 重构方法论：以窄职责、前置安全边界、reference 分层、父验证和独立审查闭环优化 `test-driven-development`
- [[hermes-lifeos-executable-architecture]] — Hermes 版 LifeOS 的可执行架构：default profile 为主脑，wiki/memory/skills/cron/MCP/profiles 严格分层并按边界推进
- [[hermes-lifeos-layer-boundary-contract]] — Hermes LifeOS 的层边界契约：以 default profile 为主脑，明确 wiki、memory、skill、cron、MCP、profile 与 session 的职责和越界规则
- [[hermes-layer-routing-decision-checklist]] — Hermes 的层间路由判定清单：什么进 wiki、memory、skill、cron、MCP，按官方定义和本地知识层分开判断
- [[hermes-memory-governance-notes]] — 一次实际 memory 减脂后沉淀出的治理规则：什么该继续留在 memory，什么该迁移到 wiki、skill 或 session
- [[hermes-model-specific-harness-profiles]] — Hermes 的 model-specific harness profile 原则：把 Codex、Claude、Gemini 的模型差异转成 skill / wrapper / project context / verification overlay，而不是贸然扩张 runtime profile
- [[hermes-memory-skills-wiki-boundaries]] — Hermes memory / skills / wiki 的边界规范与归类准则
- [[hermes-retrieval-priority-and-answer-path]] — Hermes 检索优先级与回答路径：先查 wiki，再按 memory/skills/sessions/external 补全
- [[hermes-wiki-lint-and-health-check-standards]] — Hermes wiki lint / 健康检查规范：链接、索引、frontmatter、标签、陈旧性与结构健康
- [[hermes-wiki-page-writing-standards]] — Hermes wiki 页面写作规范：命名、frontmatter、结构、wikilinks 与质量检查
- [[lifeos-overview]] — LifeOS 总览页：定义人生操作系统的一级领域、系统层次和 Hermes 在其中的执行内核角色
- [[llm-context-engineering-layer]] — Context engineering 作为 RAG 与 prompt 之间的中间层：管理 memory、compression、re-ranking 与 token budget
- [[llm-engineering-knowledge-map]] — LLM 工程知识地图：从文本表示、Transformer、训练对齐、推理优化、RAG、Prompt 到评估监控的系统分层导航
- [[llm-summary-identification-step]] — LLM 摘要的识别步骤：先判断来源能否支撑 claim，再生成带证据类型的摘要，并让审查阶段只能削弱或留白
- [[leontraveller-trading-and-investment-system]] — Leontraveller 的交易系统观：不抄底、不和市场争辩，转向顺势、止损、控回撤与简单可执行规则
- [[money-as-tool-and-investment-vs-consumption-framework]] — 财富决策框架：把钱当作工具，区分资产投资、自我投资与纯消费
- [[ordinary-investor-investment-system]] — 普通人投资方法论：先搭建长期系统，再谈标的、仓位与执行
- [[personal-finance-and-education-fund-model]] — 财务与教育基金 operating model：把家庭安全层、配置层和目标层分开，让教育基金按目标导向独立建模
- [[personal-growth-operating-model]] — 个人成长域的 operating model：把成长作为职业升级、家庭沟通与判断质量的底层引擎
- [[progressive-knowledge-system-growth]] — 知识系统的渐进式生长原则：先用真实问题产生内容，再让结构、链接和自动化从反复出现的摩擦中生长
- [[public-info-monitoring-automation-methodology]] — 公开信息监控自动化方法论：从信息源建模、结构化快照、变化判断、低噪音通知到健康检查和 Hermes cron 运行
- [[system-governance-operating-model]] — 系统治理域的 operating model：管理 Hermes LifeOS 的分层边界、沉淀路径、扩张节奏与结构健康
- [[subagent-orchestration-patterns]] — Subagent 编排模式：按生命周期复杂度选择 inline tool、fan-out、agent pool 或 team，避免多智能体过度设计
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
- [[hermes-wiki-knowledge-object-governance-closeout]] — Hermes wiki knowledge-object metadata 治理复盘：记录从 OKF 评估、试点、真实查询验证到全 wiki 推广和反保守规则修正
- [[okf-for-hermes-wiki-governance-assessment]] — OKF/LLM-wiki 思路在 Hermes wiki 中的采纳边界：只作为机器可读知识对象增强，不替代现有 Markdown wiki 架构
- [[investment-watch-final-closeout]] — Investment Watch 项目知识收束页：本地验证 typed、contract-backed、read-only 投资观察系统，runtime、cron、skill、memory 推广均延后等待单独批准
- [[gsearch-knowledge-validation-closeout]] — GSearch 验证项目的知识沉淀闭环：确认 project-local evidence lane 有效，inline 默认、fan-out 限定场景，并暂不推广 live Telegram `/gsearch`
- [[hermes-agent-experience-consolidation-capability-assessment]] — Hermes 对 Anthropic Dreaming/Outcomes/多 agent 能力的本地能力映射：当前具备 primitives，可组合实现经验固化闭环，但完整 Auto Dream/`/dreaming` 仍未证实为本机原生能力
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
