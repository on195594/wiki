---
title: Wiki Topic Index
created: 2026-11-06
updated: 2026-11-14
type: meta
status: current
---

# Wiki Topic Index

[返回任务导航](../index.md)。本页集中维护正式知识页的分类清单与摘要；具体结论、适用范围和证据以正文为准。

> Last updated: 2026-11-14 | Indexed pages: 126

## Entities
- [Flutter Open-Source UI Framework](../entities/flutter.md) — 跨平台 UI 开发选型：问题导向决策入口、真实纵切验收、Impeller 默认与回退矩阵、Apple 最低版本与 `UIScene` 边界；独立设计包、SwiftPM、Wasm、FFI、实验多窗口与可选 AI 生态的版本边界见子页
- [Nimbus 文档站点框架](../entities/nimbus-docs.md) — 基于 Astro 7 的文档站点方案：仓库可编辑文件、Agent 可读端点、`nimbus-docs check --fix/--json` 校验、多平台服务器适配器、公开边界及采用限制

## Concepts

### 1. 智能体架构、边界与运行时 (Agent Architecture, Boundaries & Runtime)
- [Agent Development Lifecycle](../concepts/agent-development-lifecycle.md) — Agent 开发生命周期：Build → Test → Deploy → Monitor 与横切治理；软件交付的阶段契约与知识效果评估，生产级 Harness、薄宿主与云端运行时边界见子页
- [Agent 生产级 Harness 与云端运行时边界](../concepts/agent-production-harness-and-cloud-runtime-boundaries.md) — 生产级 Agent Harness 边界：单一权威状态、控制面与执行面分离、共享定义与薄宿主分层、云端长程运行时跨进程恢复的五个核对窗口与 Saga 补偿/枢轴/幂等事务边界，以及 Agent-as-Code 的 PR 控制面
- [Agent Harness 搜索正则化](../concepts/agent-harness-search-regularization.md) — Agent harness 搜索正则化：约束候选提案与采纳，并用未见任务、噪声和成本检验改动是否可迁移；RRSI 数值只限其评测条件
- [Agent Resource Optimization](../concepts/agent-resource-optimization.md) — Agent 资源优化：结合集合覆盖/背包整数规划（ILP）、FrugalGPT 级联停止与 RouteLLM 偏好阈值路由建模资源约束，含 `C_cov / R_route / P_tool / M_margin` 参数化裁决矩阵与 Open SWE 线上案例证据边界
- [Agentic Programming as System Engineering](../concepts/agentic-programming-system-engineering.md) — Agentic programming 的系统工程边界：把 Agent 视为带状态、工具、记忆和目标管理的执行系统，明确多步串联成功率的条件概率前提与检查点恢复边界，用负向工具约束、最小上下文、行为漂移治理和分层记忆降低生产风险
- [AI Agent Human Outcome Design Principle](../concepts/ai-agent-human-outcome-design-principle.md) — AI Agent 项目设计的人类结果优先原则：结合 Lee & See 自动化适度依赖三维信任模型（Purpose / Process / Performance）先验证真实问题、可衡量结果和人类信任边界，含 `I_iso / M_ctx / T_tax / G_human` 参数化委派与流水线裁决矩阵
- [AI Agent Tool Selection Architecture](../concepts/ai-agent-tool-selection-architecture.md) — AI Agent 工具选择架构：分离资源发现、工具可用性、候选集缩减、具体选择和失败回退，形式化四阶条件概率漏斗、Top-K 召回—精度损益不等式与分数间隔（Score Margin）回退判据
- [AI Assistance, Cognitive Substitution, and Skill Formation](../concepts/ai-assistance-cognitive-substitution-and-skill-formation.md) — AI 辅助与能力形成：结合 Bainbridge 自动化讽刺论断与 Parasuraman–Riley 误用/弃用分类，区分即时表现增益（$\Delta P_{\text{assist}}$）、撤除后技能保持（$\Delta S_{\text{retain}}$）与持续委派中的理解所有权
- [AI Assumption Challenger Before Execution](../concepts/ai-assumption-challenger-before-execution.md) — AI 执行前假设挑战者：结合 RLHF 语言模型迎合偏差实证（Sharma et al. ICLR 2024）与事前验尸反方角色锚定，在复杂创意、写作或方案编排前先澄清意图、挑战假设并区分受限知识源与开放网络核验边界
- [Constrained Toolbox Evaluator Loop](../concepts/constrained-toolbox-evaluator-loop.md) — 受限工具箱评估闭环：结合语法制导综合（SyGuS）与反例制导归纳综合（CEGIS）把创造型 Agent 拆成合法算子空间生成、可执行转换、客观 evaluator 与多重检验样本外防过拟合闭环
- [Deterministic Analytics and LLM Reasoning Boundary](../concepts/deterministic-analytics-llm-reasoning-boundary.md) — 确定性分析与语义推理边界：分开候选筛选、概率性分类与可复现计算；规范多受众配置驱动语义层、含可加性前提的度量与比率重聚纪律及输入缺口披露，不把类型、模型共识、落表标签或透明融合当作真实性证明
- [Dijkstra on AI Programming Formalization](../concepts/dijkstra-ai-programming-formalization.md) — Dijkstra 对自然语言编程的批判与 AI 编程：区分 EWD667 窄接口定性论证、本页成本类比、最弱前置条件、有限测试与形式化证明
- [Entropy and Entropy Increase](../concepts/entropy-and-entropy-increase.md) — 区分热力学熵、统计熵与信息熵，说明熵增的系统边界、开放系统例外和软件类比边界
- [AI Agent Layer Routing Decision Checklist](../concepts/hermes-layer-routing-decision-checklist.md) — AI Agent 快速组合路由：按五种正交职责分量（$\mathbf{R}(x)$）与晋升门禁（`B_act / P_skill / G_promo`）拆分需求，外部接入优先复用授权工具，MCP 可选
- [AI Agent Model-Specific Harness Profiles](../concepts/hermes-model-specific-harness-profiles.md) — AI Agent 的 model/role-specific harness 原则：对照 LangChain DeepAgents `HarnessProfile` / `ProviderProfile` 与 Hermes Agent 配置边界，把模型差异和 AGY Custom Agent 角色边界转成 skill、project context、窄工具面与 verification overlay，而不是盲目扩张 runtime profile
- [Human-Machine Scientific Discovery and Verification Scarcity](../concepts/human-machine-scientific-discovery-verification-scarcity.md) — 人机科学发现中的验证稀缺：区分 de Bruijn 准则与 LCF 架构、形式推导与领域规约，以分层验证、范围化负面结果和专家评审约束知识准入
- [LLM Engineering Knowledge Map](../concepts/llm-engineering-knowledge-map.md) — LLM 工程知识地图：系统分层导航及 AI Engineer Notebooks 的评测、RAG、工具循环、架构对照与交付练习入口；教程描述不等于实验验证
- [Local-First 同步中的确认镜像、Outbox 与冲突政策](../concepts/local-first-sync-confirmed-mirror-outbox-conflict-policy.md) — Local-First 同步中的确认镜像、Outbox 与冲突政策：结合 Xerox PARC Bayou 的 Committed/Tentative 折叠投影方程（$\text{FoldL}(\text{Apply}, S_{\text{committed}}, O)$）与 CRDT 半格边界组织游标、幂等与显式冲突政策；仅在真实离线和恢复需求下采用
- [Public Info Monitoring Automation Methodology](../concepts/public-info-monitoring-automation-methodology.md) — 只读公共信息监控：逐对象维护可空 LKG 基线，按事件选择去重/迟滞，校准 CUSUM 与告警 PPV，区分当前成功观测和尾部连续失败的健康检查
- [Stateful Agent Environments and Grounded Verification](../concepts/stateful-agent-environments-and-grounded-verification.md) — 有状态 Agent 评测单元：结合环境、任务与验证器，融汇 $\tau$-bench 数据库终态比对与多轮次连续可靠率（$\text{pass}^k$），从权威 session/run/job 状态核验恢复、取消、清理和外部副作用
- [Typed AI Agent Boundaries](../concepts/typed-ai-agent-boundaries.md) — 用 FSM 语法约束解码（Outlines / Guided Generation）、分阶段语义分解、固定候选空间、typed tools、dependency injection 与属性测试不变量检验把 LLM 不确定性收进可验证的工程边界

### 2. 上下文工程、记忆与技能演化 (Context Engineering, Memory & Skill Evolution)
- [Agent 闭环学习：从用户纠错到规则升级](../concepts/agent-closed-loop-learning-from-corrections-to-rules.md) — Agent 闭环学习：结合 DSPy/GEPA 反思式候选优化与影子实验，区分来源机制和项目自定的配对统计、回归与成本晋升门禁；来源人工修正口径待核实
- [Agent Context Engineering](../concepts/agent-context-engineering.md) — Agent 上下文工程总原则：用最小必要上下文防止偏航；结合长上下文 U 型位置退化（Lost in the Middle）与带边信息瓶颈（Information Bottleneck）解释即时加载、首尾锚定、上下文与记忆边界及出处债务；静态上下文面与历史/状态加工分别见两个子页
- [Agent Context: System Prompt, Tools and Examples](../concepts/agent-context-prompt-tools-and-examples.md) — 上下文静态面：system prompt 作操作简报（受静态配额 $B_{\text{sys}}$ 约束）、窄工具面与四阶选择概率漏斗、可见不等于可用、以行为为主的示例
- [Agent Context: History, State and Bounded Processing](../concepts/agent-context-history-state-and-bounded-processing.md) — 上下文动态面：结合 MemGPT 虚拟上下文分页区分输入转储、历史摘要与 `SKILL.state` 确定性状态折叠（受 $R_{\text{probe}}$ 与 $C_{\text{total}}$ 约束）、子代理交接及专用模型有界加工
- [Agent Experience Consolidation Loops](../concepts/agent-experience-consolidation-loops.md) — Agent 经验固化闭环：结合互补学习系统（CLS）、Sleep-Time Compute 离线重组织、记忆再巩固的工程类比（Reconsolidation）、CL-Bench 1.0 跨模型记忆行为对比与断链修复案例，含 `B_act / P_skill / G_promo / I_rev` 参数化治理矩阵；Skill 治理与知识演化/元技能见子页；研究增益不当作默认执行授权
- [Agent Skill Governance and Reversible Skill State](../concepts/agent-skill-governance-and-reversible-state.md) — Skill 治理：结合 ACT-R 知识编译（陈述性向产生式转化）与扇出效应（Fan Effect，$-\ln \text{fan}_j$）形式化使用漏斗与归因、生命周期状态机、可回滚 Skill 与持久知识分离及演化知识评估边界
- [Agent Knowledge Evolution and Meta-Skills](../concepts/agent-knowledge-evolution-and-meta-skills.md) — 知识演化与元技能：结合稳定性—可塑性困境、灾难性遗忘、弹性权重巩固（EWC Fisher 矩阵二次惩罚）与再巩固的局部修订类比区分外部知识复用 vs 权重学习，以及任务技能 vs 支持设计元技能
- [AI Agent Document Fidelity Risk](../concepts/ai-agent-document-fidelity-risk.md) — 多轮委托文档的保真风险：以 Lens 往返定律作类比，区分尝试恢复与真逆函数、汇总退化数据与示意模型，采用小步编辑、结构检查与中间态审计
- [Audience-Situation Content Briefs](../concepts/audience-situation-content-briefs.md) — 受众情境内容简报：结合 Ehrenberg-Bass 心智可得性理论（Romaniuk & Sharp，心智渗透率 $\text{MP}$ / 网络规模 $\text{NS}$ / 心智份额 $\text{SoM}$）、CEP 与 7W 框架从真实决策场景出发，消除边际关键词搜索量混杂
- [From Coping Skill Acquisition to Real-World Application](../concepts/coping-skill-application-and-imaginal-exposure.md) — 应对技能从习得到现实应用：结合抑制性学习（Craske 等）与压力接种三阶段模型（Meichenbaum），识别伪应对并以有界想象暴露检验技能是否减少回避，区分日常迁移与临床延长暴露边界
- [文档解析的结构保真与中间表示](../concepts/document-parsing-structural-fidelity.md) — 检查内容与表头、单位、脚注的绑定：结合关系元组投影、TEDS 与 DPP 0.1 工作草案，区分局部结构评分、受限格式归一化和完整语义/合规验证
- [AI Agent Context Engineering Design Priorities](../concepts/hermes-context-engineering-design-priorities.md) — 面向 AI Agent 的 context engineering 设计优先级：先做 budget、ranking、compression，再做 history decay；含 `B_ctx / U_blk / C_total / R_probe` 参数化上下文预算与端到端总成本评估模型
- [Wiki 知识新鲜度与断言证据绑定](../concepts/hermes-knowledge-freshness-and-claim-evidence.md) — 知识新鲜度、断言级来源绑定与 `locate` → `expand` 两步证据导航：区分 FActScore、ALCE 支持度与 Jaccard 稳定性，明确空集合和来源真实性边界
- [AI Agent Memory Skills Wiki Boundaries](../concepts/hermes-memory-skills-wiki-boundaries.md) — AI Agent 内容归属主规则：结合 Tulving 情景/语义记忆、Squire 陈述/程序记忆分类学与 Bjork 存储/检索强度双维解耦，区分广义 agent memory 与默认 memory 载体，用正反例与去情境化晋升门禁路由 skills、wiki、sessions/project state 与历史证据
- [AI Agent Skill Refactoring Methodology](../concepts/hermes-skill-refactoring-methodology.md) — AI Agent Skill 重构方法论：结合 Parnas 信息隐藏、Nielsen 渐进式披露与 Agent Skills 三层加载、SKILL.state 程序/状态分离（$\mathcal{O}(T)$ vs $\mathcal{O}(T^2)$）及 Warp/WikiSkill 双环演化机制，收敛默认路径与跨模型复验边界
- [LLM Context Engineering Layer](../concepts/llm-context-engineering-layer.md) — Context engineering 管理 memory、compression、re-ranking 与 token budget：结合检索召回与阅读器饱和脱节（Lost in the Middle）及信息瓶颈原理；涵盖 Agentic RAG 的证据信任边界与语义漂移/未知候选概念参考
- [LLM Summary Identification Step](../concepts/llm-summary-identification-step.md) — 来源约束摘要的识别与诚实留白：以部分识别和选择性预测作类比，按类别核验原文事实、显式推断与建议，不把建议作为事实的自动降级出口
- [Repository-Level Code Intelligence Layer](../concepts/repository-level-code-intelligence-layer.md) — 仓库级代码智能层：结合 Tree-sitter AST 符号引用图与 PageRank 预算映射（RepoMap）及三级层级化定位（Agentless），把目标代码、可达接口签名、项目约束与显式未知项装配成低噪音 Agent 上下文

### 3. 工作流编排与代码工程 (Workflows, Orchestration & Coding)
- [Agent Autonomy Ladder for AI Agent Workflows](../concepts/agent-autonomy-ladder-for-hermes-workflows.md) — AI Agent 工作流中的 Agent 自主度阶梯：结合 Parasuraman–Sheridan–Wickens 四阶段十级自动化模型（LOA），按确定性 workflow、编排 workflow、受限 reactive loop 和 bounded multi-agent 实施阶段非对称授权与语义验收
- [Agent Memory–Reflection–Planning Pipeline](../concepts/agent-memory-reflection-planning-pipeline.md) — Agent 记忆–反思–规划流水线：将经历处理为事件流、三因子归一化检索（$\gamma^{\Delta t}$ 新近度、重要性、余弦相关性）、累积重要性阈值反思推断与分层计划，对比单次间隔指数衰减与 ACT-R 全历史幂律激活的适用边界，区分应用事件存储与 AI Agent 默认 memory
- [Agent Orchestration Production Tradeoffs](../concepts/agent-orchestration-production-tradeoffs.md) — Agent 编排的生产取舍：以单 Agent 基线、任务可分解性、协调成本和错误相关性选择最小拓扑，含 `pass^k / c_err / T_pivot / C_coord` 参数化编排与状态恢复裁决矩阵
- [Agentic Content Pipeline Design Patterns](../concepts/agentic-content-pipeline-design-patterns.md) — Agentic 内容生产模式：专家判断、窄职责技能链（含 `skill-creator` 有/无引导消融裁剪 $\Delta Q$）、真实数据源、低成本中间产物与前置人类方向；视觉设计案例补充条件性门禁和模型升级后的规则复查
- [AI Coding Agent Workflow Types](../concepts/ai-coding-agent-workflow-types.md) — AI coding agent 的协作与入口选择：先定义目标、上下文、约束、验收和验证，再按 IDE、Terminal、PR、Cloud 交互模式执行并保留人工审查
- [AI Coding Assistant Context Budget Management](../concepts/ai-coding-assistant-context-budget-management.md) — AI coding assistant 的上下文预算管理：结合 AST 符号签名图（RepoMap）与三级层级化定位（Agentless），限制历史、全量文件、工具输出、日志和全局指令进入模型，降低 token 成本和上下文漂移
- [AI Task Delegation Patterns from Local-Cloud Hybrid LLMs](../concepts/ai-task-delegation-patterns-from-local-cloud-hybrid-llms.md) — 从端云混合 LLM 三维坐标（Direction / Trigger / Purpose）抽象出的 AI Agent 调度模式：含脱敏—求解—还原闭环、化名化与重识别风险、小模型结构化输出“约束税”（Constraint Tax）、Schema/业务双重校验及五种模式证据分级
- [Claude Code Practical Workflow Tips](../concepts/claude-code-practical-workflow-tips.md) — Claude Code 的实用工作流要点：侧问（`/btw`）、目标循环（`/goal`）、浏览器与指令审计（`/chrome`、`/doctor prompt-audit`、`/autofix-pr`）、会话内循环调度（`/loop` / `/proactive`）与 Cloud/Desktop 持久任务区分、多目录与规则加载边界（`--add-dir`、`claudeMdExcludes`）及跨设备/后台并行接续（`/teleport`、`/remote-control`、`/background`、`/batch`）
- [Codex Agent Workflow Layering](../concepts/codex-agent-workflow-layering.md) — Codex 的分层 agent 工作流：prompt、planning、`AGENTS.md`（含 `## Code Review Rules`）、`config.toml` / `requirements.toml`、skill（`agents/openai.yaml` 与非破坏性启停）、MCP 与 automation 各司其职
- [First-edit Economy for Coding Agents](../concepts/first-edit-economy-for-coding-agents.md) — Coding agent 的首次编辑经济性：结合样本信息期望价值（EVSI）最优停止判据与 Delta Debugging（`ddmin`）1-最小差分原则，在有明确锚点和便宜验证时减少宽泛探索、小步编辑并立即验证
- [Flutter 版本演进、平台编译与可选 AI 生态边界](../concepts/flutter-version-evolution-and-platform-boundaries.md) — Flutter 版本演进子页：独立设计包（`material_ui` / `cupertino_ui`）、SwiftPM 默认集成与 CocoaPods 2026-12-02 只读期限（含 Flutter 3.47.8 eMudhra CA 密钥拦截公告）、Wasm 编译与 `wasmAllowList` 浏览器门控（含 Flutter 3.50 文档更新）、原生 FFI 绑定、实验桌面多窗口及 GenUI/Genkit Dart 边界
- [Google SRE Gemini CLI Incident Response Pattern](../concepts/google-sre-gemini-cli-incident-response.md) — Google SRE 如何把 Gemini CLI 接入事故响应：结合 $\text{MTTM} = T_{\text{detect}} + T_{\text{triage}} + T_{\text{approve}} + T_{\text{exec}}$ 延迟分解与错误预算消耗保护，用闭集 playbook 与受控审批实现人机协作止血
- [AI Agent Workflow Layering and Adoption Order](../concepts/hermes-agent-workflow-layering-and-adoption-order.md) — AI Agent 分层工作流：指令、知识、skills、MCP/tools、Code Mode 程序化执行、验证与 cron 的职责和落地顺序
- [AI Agent Workflow Formalization Principles](../concepts/hermes-ai-workflow-formalization-principles.md) — AI Agent 的规格与规划按风险留痕；将自然语言意图收敛为可验证结构、窄接口、可执行技能与确定性路由，含 `C_spec / D_fsm / A_add / P_prop` 参数化类型契约与验证裁决模型，代码审查分层与收敛治理见子页
- [AI Code Review Governance, Traceability, and Convergence](../concepts/ai-code-review-governance-and-convergence.md) — AI 生成代码的审查治理：保留决策理解与责任，结合双向追溯、断言验证、风险分级、三轮收敛条件及排队论（Little 定律与 Kingman 拥塞公式 $W_q \propto \frac{\rho}{1-\rho}$）约束生成吞吐与人类审查产能
- [AI Agent Python Engineering Capability Checklist](../concepts/hermes-python-engineering-capability-checklist.md) — AI Agent Python 工程检查清单：流式输入、资源生命周期、有界并发、类型边界、测量驱动的性能优化，以及按真实变更压力选择七类最小设计边界与失效检查
- [Loop Engineering for AI Agent Workflows](../concepts/loop-engineering-hermes-agent-workflow.md) — Loop Engineering 在 AI Agent 中的映射：以类型化信号、确定性 dispatcher、离散控制 Lyapunov 变体函数（$\Delta V_t < 0$ 与不动点熔断）及 `L_auto / E_first / V_loop / ρ_rev` 参数化裁决矩阵组织工作闭环；保留 active-layer 审批边界
- [多智能体系统性失效模式](../concepts/multiagent-systemic-failure-modes.md) — 多智能体系统性失效模式：结合孔多塞陪审团定理相关投票退化公式与 MAST 14 类失效分类学（FC1 系统设计 / FC2 协同失调 / FC3 验证缺陷），区分行为低方差、认识论失调、资源共谋与目标冲突升级，并把 Agent 数量和有效独立证据分开
- [Subagent Orchestration Patterns](../concepts/subagent-orchestration-patterns.md) — Subagent 编排模式：结合 Nature Machine Intelligence 260 配置协作边界、角色优先的上下文交接权衡（延续任务传有界证据包，独立审查隔离父级结论以降低锚定风险）与 Bernstein 并发读写不交条件（$\mathcal{W}_i \cap \mathcal{W}_j = \emptyset$），按单 Agent 基线之后依次评估 inline tool、fan-out、pool 或 team
- [Chat to Agent Session Routing](../concepts/chat-to-agent-session-routing.md) — 聊天平台到有状态 AI Agent 运行时的会话路由：容器键映射、回复目标不可变闭包与企业集成幂等接收器（Idempotent Receiver）去重边界

### 4. 评测、验证与知识治理 (Evaluation, Verification & Governance)
- [ACA 源码：有效参数与评估预算](../concepts/fixed-budget-optimizer-selection-aca-case.md) — 仅依据固定 GitHub 提交解析参数校验、调用预算与移动算子，区分请求参数、生效种群和实际评估次数
- [Agent Evaluation Rubric Calibration](../concepts/agent-evaluation-rubric-calibration.md) — Agent 评测 Rubric 校准：分数只作诊断指针；结合 MT-Bench 三大裁判偏差（位置/冗长/自我偏好）、Rogan–Gladen 灵敏度/特异度校准（$\hat{\theta}_{\text{RG}}$ / Youden's $J$）与预测驱动推断（PPI），用相关会话、工具证据和专家评分理由校准评测器并沉淀回归案例
- [Agent 失败闭环评估](../concepts/agent-failure-closed-loop-evaluation.md) — Agent 失败闭环评估：结合 SWT-Bench `Fail-to-Pass` 复现判据与 TestPrism 单参考盲区拆解（覆盖缺口/过弱断言/执行错误），将可复发失败按三路根因分流并编译为成对差分回归工件（含 `S_f2p / F_ext / G_shadow / B_retry` 参数化裁决矩阵）
- [Agent Research Evidence Gate](../concepts/agent-research-evidence-gate.md) — 以 CRAG / Self-RAG 为参照，区分来源机制与工程推论：综合前核验支持度、按轮次/预算补证或明确弃答，并说明 `I_ident / G_evid / F_rt / V_cov` 的适用边界
- [Agent Self-Validation Loops](../concepts/agent-self-validation-loops.md) — Agent 自我验证闭环：区分提示驱动修正的局限、SCoRe 专门训练与工具/环境反馈，按证据可靠性、确定性或容差等价和项目重试预算组织迭代
- [Agent Skill Provider Governance Boundary](../concepts/agent-skill-provider-governance-boundary.md) — Agent Skill Provider 治理边界：形式化多源组合算子（`Aggregate / Deduplicate / Filter`）与命名空间遮蔽防御，结合 Saltzer–Schroeder 最小权限/完全中介原则与 Confused Deputy（ScopeGate 逐次参数值授权）分离静态暴露门控与动态执行授权
- [AI Agent Active-Surface Lifecycle Governance](../concepts/hermes-active-surface-lifecycle-governance.md) — AI Agent 活跃面的生命周期治理：结合上下文房租（Context Rent）、CL-Bench 预设规则负增益实证（`-0.234`）与模型代际补丁衰减公式（$\Delta U(r_j \mid M_{t+1})$），从基线、校准、晋升推进到事件触发的重基线与退役，含 `Q_amort / ρ_comp / E_res / ΔU_reb` 诊断矩阵，不把体积比或效用示意式作为自动退役授权
- [AI Agent Context Layer Operating Rules](../concepts/hermes-context-layer-operating-rules.md) — AI Agent 上下文装配规则：结合 MemGPT 主存/外存分页模型与 `B_ctx / U_blk / R_probe` 参数契约，管理小型默认注入层、按需检索、历史压缩、长任务 project state 和隔离 handoff
- [Human and AI Agent Shared Knowledge Architecture](../concepts/hermes-knowledge-architecture.md) — 人类与 AI Agent 共享知识架构与导航：结合 Sleep-Time Compute 离线重组织、编译摊销盈亏平衡方程（$Q^*$）、“博尔赫斯地图陷阱”压缩率边界（$\rho_{\text{comp}} < 1$）、纯检索六类结构失效与冲突感知对象组织运行时知识栈与 Wiki 文件层
- [Shared Wiki Operating Flow](../concepts/hermes-knowledge-base-operating-flow.md) — 共享知识库端到端操作流：公开准入、读写提案与提交门禁分离（Proposal vs. Commit）、离线二阶段断链/偏差对账、检索门禁与授权回写
- [AI Agent Memory Governance Notes](../concepts/hermes-memory-governance-notes.md) — Memory 减脂与跨层路由规则：结合 ACT-R 基础水平激活幂律衰减（$B_i = \ln \sum t_j^{-d}$）与借鉴 Bjork 存储/检索强度区分的工程路由矩阵界定什么适合留在 memory，什么应进入 wiki、skill、项目状态或 session
- [AI Agent Retrieval Priority and Answer Path](../concepts/hermes-retrieval-priority-and-answer-path.md) — 人类与 Agent 检索路径：区分单源查找与跨源推理，结合排序前时间窗过滤（Pre-Ranking $t_{\text{as\_of}}$ Filter）、词法—语义倒数排名融合（RRF）与证据导航图按 `locate` → `expand` 及 Freshness Gate 核验出入边与来源证据
- [Wiki Lint and Health Check Standards](../concepts/hermes-wiki-lint-and-health-check-standards.md) — 共享 Wiki lint / 健康检查规范：链接、索引、frontmatter、标签、页面及局部 claim 新鲜度与结构健康
- [Wiki Page Writing Standards](../concepts/hermes-wiki-page-writing-standards.md) — 人类与 AI Agent 共用的 Wiki 页面写作规范：命名、frontmatter、日期模板、结构、wikilinks、可选 Relations、局部 `[!volatile]` claim 与质量检查
- [Production Agent Evaluation Baselines](../concepts/production-agent-evaluation-baselines.md) — 生产 Agent 评估基线：拆分延迟、Token、调用、缓存、工具耗时、单次正确回答摊销成本（$C_{\text{amort}}$）与跨源证据导航待执行评测；结合 TOST 双单侧非劣效检验与右偏重尾分布均值—中位数公式，区分非显著与等价、中位成本与整体预算，并限制外部阈值的适用范围
- [Production AI Agent Evaluation Framework](../concepts/production-ai-agent-evaluation-framework.md) — 生产级 AI Agent 评估框架：分层评估检索（含跨运行引用一致性）、生成、行为和运营，含 `N_eff / J_judge / Δ_NI / C_amort` 参数化评估与门禁裁决矩阵；工具轨迹六步调试、部署前七类结构回归探针与 RAG 决策敏感性见子页
- [Agent 部署前结构回归与工具轨迹调试](../concepts/agent-pre-deploy-regression-and-trace-debugging.md) — 生产评估子页：工具调用六步可归因调试证据链、部署前七类结构回归探针矩阵，以及 RAG 决策输出变化与有真实值支持的质量增益边界
- [Progressive Knowledge System Growth](../concepts/progressive-knowledge-system-growth.md) — 知识系统的渐进式生长原则：结合 Gall 定律、Luhmann 卡片盒自底向上涌现与容器维护税实证（413 文件失速 vs 10 文件高显著性结构），先用真实问题产生内容，再让结构、链接和自动化从反复摩擦中生长
- [少样本 AI 评测中的重复任务、伪重复与统计功效](../concepts/repeated-measures-statistical-power-for-ai-evaluation.md) — 少样本 AI 评测的重复测量与统计功效：结合 Hurlbert 伪重复、Kish 设计效应（$\text{DEFF} = 1 + (m-1)\rho$ 与有效样本量上限 $N/\rho$）、Clark 语言固定效应谬误（$\min F'$）及 Miller 聚类标准误与配对差值方差分解，区分主体、任务和有效独立证据
- [System Governance Operating Model](../concepts/system-governance-operating-model.md) — 系统治理域的 operating model：管理 AI Agent LifeOS 的分层边界、沉淀路径、扩张节奏与结构健康
- [Wiki Ingestion Workflow](../concepts/wiki-ingestion-workflow.md) — 把外部信息编译进知识库的标准入库流程：借记录链接与信念修正作概念类比，区分精确来源依赖、名称候选、范围复核与五类编辑动作（`NEW / CONFIRM / UPDATE / CONFLICT / SUPERSEDE`），不宣称实现概率匹配或次协调逻辑，先过公开边界再固化 raw、反查依赖、更新 Relations 并验证

### 5. 个人操作系统与投资决策 (LifeOS, Systems & Investment)
- [CompanyOS to LifeOS Filesystem Philosophy](../concepts/companyos-to-lifeos-filesystem-philosophy.md) — 将公司和人生建模为文件系统：结合 Unix 文件与进程机制的四项归纳（基于 Ritchie & Thompson）、Plan 9 进程级定制命名空间与 9P 协议（Pike 等）、Simon 状态—过程转译理论及最小权威原则（PoLA），界定文件即状态与权限治理的适用边界
- [Family Education Operating Model](../concepts/family-education-operating-model.md) — 家庭教育域的 operating model：以孩子适配、SDT 基本心理需要（自主/胜任/归属）、发展性工作记忆边界和家庭可持续为核心，含 `M / T_c / F_e / K` 可选推论参数
- [AI Agent LifeOS Executable Architecture](../concepts/hermes-lifeos-executable-architecture.md) — AI Agent 版 LifeOS 的可执行参考架构：结合 Simon 近可分解系统（快慢时间尺度解耦）与 Hora/Tempus 稳定中间形态寓言，按 Phase 0–5 渐进组织协调上下文与 `wiki / memory / skills / cron / MCP / profiles`
- [AI Agent LifeOS Layer Boundary Contract](../concepts/hermes-lifeos-layer-boundary-contract.md) — AI Agent LifeOS 的层边界契约：结合 Lampson 保护域与访问控制矩阵（$\mathbf{A}[d,o]$）及 Plan 9 命名空间视图，区分领域分类（`wiki / skill`）与需独立验证的运行时状态和权限隔离（`profile`），含七层准入与越界裁决矩阵
- [Trend-Following Trading System (Summary of Leontraveller Public Notes)](../concepts/leontraveller-trading-and-investment-system.md) — Leontraveller 公开笔记中的交易系统观：不抄底、不和市场争辩，结合 52 周高点锚定动量（George & Hwang）、未实现资本利得悬顶（Grinblatt & Han $g_t$）与每日重平衡杠杆方差损耗转向顺势、止损、控回撤与简单可执行规则
- [LifeOS Overview](../concepts/lifeos-overview.md) — LifeOS 可配置总览模板：定义可选领域、系统层次、四大对象域参数耦合矩阵、公开/私有边界和 AI Agent 的可选执行角色
- [Money as Tool and Investment-vs-Consumption Framework](../concepts/money-as-tool-and-investment-vs-consumption-framework.md) — 财富决策框架：区分投资与消费，以现金缓冲保留选择权，并检查自我投资的回报路径与失败承受能力
- [Ordinary Investor Investment System](../concepts/ordinary-investor-investment-system.md) — 普通人投资方法论：先搭建长期系统，再结合日历与阈值混合再平衡、新增现金流低摩擦调仓与行为控制执行
- [Household Fund Layering Model](../concepts/household-fund-layering-model.md) — 财务与教育基金 operating model：把家庭安全层、配置层和目标层分开，结合三桶期限匹配（Bucket Strategy）让教育基金按目标期限与回撤约束独立建模
- [Personal Growth Operating Model](../concepts/personal-growth-operating-model.md) — 个人成长域的 operating model：结合刻意练习反馈边界（Ericsson / Macnamara）、认知负荷理论（Sweller）与单双环复盘（Argyris & Schön），含 `R / P / V` 可选推论参数
- [Investment Risk Control Framework](../concepts/investment-risk-control-framework.md) — 投资风险控制框架：核心仓按配置与再平衡带宽，进攻仓按趋势、禁止摊平和止损；含分散化与共同变动原理、共同经营驱动及压力检查推论（1952 原论文全文待补核）、计划止损/组合波动/最大回撤的区别，以及回撤恢复双曲方程（$G = D/(1-D)$）、杠杆 ETF 二次方方差拖累（$-\frac{1}{2}k^2\sigma^2$）与参数化风控变量（r / R_open / D_max / δ）
- [Work and Career Operating Model](../concepts/work-and-career-operating-model.md) — 工作与职业域的 operating model：结合人力资本分层（Becker 通用/企业特定与 Gibbons & Waldman 任务特定）及探索—利用权衡（March），兼顾 `B / E / C / S` 可选推论参数与家庭兼容性
- [周期利润正常化与低市盈率陷阱](../concepts/company-analysis/cyclical-earnings-normalization.md) — 公司分析方法卡：周期或商品类公司低市盈率时，用绝对利润、利润率或行业平均做正常化，并区分正常化商品价格与期货远期价格
- [增长、再投资与资本回报](../concepts/company-analysis/growth-reinvestment-and-return-on-capital.md) — 公司分析方法卡：增长率 = 再投资率 × 资本回报，ROIC 的定义、会计失真与边际回报，以及没有超额回报的增长不创造价值
- [价格隐含预期分析（反向估值）](../concepts/company-analysis/price-implied-expectations-analysis.md) — 公司分析方法卡：从股价反推隐含的销售增长、利润率与投资要求（反向估值），再判断预期修正的方向
- [自由现金流与估值口径](../concepts/company-analysis/free-cash-flow-and-valuation-basis.md) — draft：CFO 减资本开支、FCFF、FCFE 与 owner earnings 的口径，现金流与折现率匹配、再投资和终值；原信与准则正文待补核
- [盈利质量与现金转化](../concepts/company-analysis/earnings-quality-and-cash-conversion.md) — draft：同期间、同范围解释利润与经营现金流差异；区分正常投入、收付时点和待核查异常；Dechow–Dichev 含未来现金流，不作当期信号

### 6. 软件工程基础法则 (Software Engineering Laws)
- [Software Engineering Laws — Architecture](../concepts/software-engineering-laws/software-engineering-laws-architecture.md) — 软件工程 Architecture 法则地图：分布式取舍（CAP 与 PACELC）、隐式接口蒸发（Hyrum's Law）、抽象泄漏、复杂度分配与系统演化风险
- [Software Engineering Laws — Decisions](../concepts/software-engineering-laws/software-engineering-laws-decisions.md) — 软件工程 Decisions 法则地图：认知偏差（Wason 证伪实验与达克效应统计边界）、Lindy 帕累托失效率、奥卡姆剃刀与资源分配
- [Software Engineering Laws — Design](../concepts/software-engineering-laws/software-engineering-laws-design.md) — 软件工程 Design 法则地图：知识唯一表示（DRY vs AHA）、Law of Demeter 五类调用边界、LSP 强行为子类型与 YAGNI 持续重构前提
- [Software Engineering Laws — Planning](../concepts/software-engineering-laws/software-engineering-laws-planning.md) — 软件工程 Planning 法则地图：度量与代理指标失真（Gilb / Goodhart）、估算、期限、收尾成本与优化时机
- [Software Engineering Laws — Quality](../concepts/software-engineering-laws/software-engineering-laws-quality.md) — 软件工程 Quality 法则地图：渐进维护、测试策略、协议主动维护（Postel's Law 与 RFC 9413 边界）、技术债与长期演化
- [Software Engineering Laws — Scale](../concepts/software-engineering-laws/software-engineering-laws-scale.md) — 软件工程 Scale 法则地图：固定工作负载与规模化加速公式（Amdahl / Gustafson）、串行瓶颈与网络效应
- [Software Engineering Laws — Teams](../concepts/software-engineering-laws/software-engineering-laws-teams.md) — 软件工程 Teams 法则地图：团队规模、两两沟通通道二次方增长（Brooks's Law）、知识集中、组织结构与协作成本

## Operations
- [Agent Shared Wiki Index](../operations/agent-shared-wiki-index.md) — Agent 共享 Wiki 的产品无关接入模板：根目录可配置、按需检索、项目规则优先且默认只读；获准维护时保留 raw 增删审查与清单差异回读

## Comparisons
- [Dijkstra EWD667 vs 2026 AI Programming Article](../comparisons/dijkstra-ewd667-vs-ai-programming-article.md) — 对照 EWD667 原文与 2026 AI 编程文章：比较自然语言模糊性、窄接口、形式化契约、出处债务与认知风险，并区分原文论证和现代工程推论
- [Agent 事故响应接入：职责与安全边界](../comparisons/hermes-vs-google-sre-agentic-incident-response.md) — 按目标、工具、有限动作、审批和复盘职责评估任意 Agent 的接入；来源案例不作为当前产品能力或排名证据
- [Leontraveller vs Ordinary Investor Investment System](../comparisons/leontraveller-vs-ordinary-investor-investment-system.md) — 对照两套投资框架：结合行为投资组合理论（BPT-MA）区分核心安全底盘（`T / H / L / D / δ`）与主动趋势进攻（`1R / r / R_open / D_max`）的分工和冲突边界

## Queries
- [Agent Architecture Primary-Paper Map](../queries/agent-architecture-primary-paper-map.md) — Agent 架构一手论文地图：按设计问题检索 ReAct、Toolformer、Generative Agents、Voyager 与 AutoGen 的机制和定量边界，区分内生自修正、训练条件与反馈可靠性
- [Software Engineering Laws Decision Map](../queries/software-engineering-laws-decision-map.md) — 56 条软件工程法则的全量问题导向入口：按真实工程场景与 AI Agent 五维系统工程映射检索适用法则、形式化模型边界（Amdahl / Gustafson / PACELC / RFC 9413 / Brooks / LoD / LSP / Lindy）、跨类别张力和来源记录
- [OKF Concepts for AI Agent Wiki Governance Assessment](../queries/okf-for-hermes-wiki-governance-assessment.md) — OKF/LLM-wiki 的采纳边界、已完成的核心页试点、本地 catalog 与 OKF 字段对照，以及企业 Catalog 规模化实现的触发条件；不替代现有 Markdown wiki 架构
- [Wiki 跨源证据导航离线评测方案与拓扑基线](../queries/wiki-cross-source-evidence-navigation-benchmark.md) — Q1–Q8 检索基线、Q5/Q8 公开证据与评分纠正；区分覆盖、引用支持与事实核验，自由检索端到端效果仍未验证
- [AI Agent Layer Routing Edge Cases](../queries/hermes-layer-routing-edge-cases.md) — AI Agent 路由边界案例：结合正交职责分量与 `B_act / P_skill / G_promo` 门禁裁决 10 类易混淆场景，区分可选接入、执行契约与公开操作指南
- [AI Agent Layer Routing Sample Cases](../queries/hermes-layer-routing-sample-cases.md) — AI Agent 路由样例：按职责和授权选择载体，环境记忆不替代当前核验
- [Using AI Agent for AI Coding with Typed Boundaries](../queries/how-i-should-use-hermes-for-ai-coding-with-typed-boundaries.md) — AI Agent 编程中的 typed output、FSM 约束解码、窄工具、显式依赖、属性测试和验证 gate；示例不表示已经部署
- [Combining Two Investment Frameworks](../queries/combining-two-investment-frameworks.md) — 分层组合两套教育性投资框架：基于 BPT 心理账户防火墙与参数化门禁（`L / δ` vs `1R / R_open / D_max`），长期制度管底盘，主动纪律管进攻
- [Investment Pre-Trade Risk Checklist](../queries/pre-trade-risk-checklist.md) — 通用交易前风险清单：先分清资金层、动作类型、退出计划与参数化风险门禁（1R / R_open / D_max / δ），再决定是否出手
- [When Not to Trade](../queries/when-not-to-trade.md) — 停手条件：结合 Barber & Odean 过度交易换手损耗实证与四条硬熔断门禁（`D_max / R_open / δ / 1R`），拦截进攻仓摊平亏损、情绪补仓、越权单或无退出计划交易
- [Reviewing a Losing Position](../queries/losing-position-review-method.md) — 亏损仓复盘方法：结合前景理论的参考点价值函数、处置效应与回本效应（Break-Even Effect），区分正常回撤、失效判断和伪装成再平衡的情绪补仓
- [Scaling Into and Out of a Position](../queries/position-scaling-method.md) — 分批进出方法：核心仓按既定配置分阶段投入或再平衡；进攻仓防御赌场钱效应（House-Money Effect），可采用非递增顺势分层并按当前净值核算合并风险，不把浮盈或保本止损当作免费风险资本
- [Position Sizing by Risk Budget](../queries/position-sizing-method.md) — 参数化仓位预算：基于 1R 单位风险、固定比例仓位公式、R 倍数与分数凯利边界计算规模，防范超仓与跳空风险
- [Managing a Winning Position](../queries/winning-position-risk-management.md) — 盈利仓风险管理：克服前景理论与赌场钱效应提供的行为偏差视角，用结构移动止损与固定 1R 分母平衡利润保护与趋势延续
- [Deciding Between Inaction and Action](../queries/inaction-vs-action-decision-framework.md) — 不行动与行动的裁决框架：结合行动偏误（Action Bias）与交易摩擦损耗，区分进攻仓条件化等待与止损/再平衡刚性执行
- [Building a Post-Trade Review Loop](../queries/post-trade-review-loop.md) — 交易后复盘闭环：结合过程合规性与含零收益交易的 R 倍数样本分布，区分执行偏差与风险模型缺口，避免事后归因
- [Detecting Repeat Trading Mistakes](../queries/repeat-mistake-detection-in-trading.md) — 重复错误识别：区分过程违背（Process Bug）与合规尾部亏损，按频次、触发情境与累计 R 拖累过滤小样本假阳性过拟合
- [Converting Trading Lessons into Hard Rules](../queries/trading-lessons-to-hard-rules.md) — 教训到硬规则的转化：结合 Gollwitzer 执行意图（Implementation Intentions）将高频高代价教训编译为可验证的 `IF-THEN` 参数化动作约束
- [Keeping a Trading System Small and Executable](../queries/minimal-executable-trading-system.md) — 交易系统做减法：结合快省启发式（Fast-and-Frugal Heuristics）的偏差—方差权衡与样本外参数估计误差边界，保留少数高阻断力规则，删除不可快速调用的说明书式规则
- [Wiki 知识新鲜度改造：通用原则与历史决策（已关闭记录）](../queries/hermes-wiki-knowledge-freshness-improvement-plan.md) — 提炼证据绑定、时间区分和局部复查的跨系统原则；旧改造约定与现行 Schema、Freshness Gate 明确分开
- [Agent 经验固化能力评估：通用框架与历史案例（已关闭记录）](../queries/hermes-agent-experience-consolidation-capability-assessment.md) — 按证据、提炼、分层保存、效果验证、生命周期与权限核查任意 Agent，区分提供方式与验证程度；产品能力仅作版本历史案例
