---
title: Hermes LifeOS Executable Architecture
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [hermes, lifeos, architecture, workflow, governance]
sources: [concepts/companyos-to-lifeos-filesystem-philosophy.md, concepts/hermes-knowledge-architecture.md, concepts/hermes-memory-skills-wiki-boundaries.md, queries/hermes-layer-routing-edge-cases.md, session:2026-04-21-hermes-lifeos-vs-profile]
status: stable
---

# Hermes LifeOS Executable Architecture

## Summary
这页把“LifeOS 在上、Hermes primitives 在下、profiles 只做少量边界隔离”的结论压成可执行架构。目标不是再谈抽象理念，而是明确每一层的职责、禁止越界的规则、落地顺序和验收标准，让 Hermes 可以作为个人 LifeOS 的执行内核持续运行。

## Goal
把 Hermes 建成一个以 `default profile` 为主脑的 LifeOS：
- 正式知识统一沉淀到 `~/wiki`
- 稳定偏好与长期事实只保留在 `memory`
- 可复用方法沉淀为 `skills`
- 周期性动作通过 `cron` 运行
- 外部系统能力通过 `MCP` 接入
- `profiles` 只在确有隔离必要时使用

## Core design decision
### 主判断
LifeOS 不是由多个 profile 拼出来的，而是由一个统一语义层 + 少量受控执行层组成。

### 默认拓扑
- `default profile`：唯一主脑，承载 LifeOS 主语义层
- `~/wiki`：正式知识与结构化页面
- `memory`：短小稳定规则、偏好、环境事实
- `skills`：重复工作的方法层
- `cron`：已稳定方法的调度层
- `MCP`：外部系统接入层
- 少量专用 `profiles`：只承担高摩擦隔离边界

## Hard boundaries

### 1. `wiki`
**职责**
- 承载长期知识资产
- 承载需要结构、小节、来源、交叉链接的内容
- 承载架构原则、领域框架、决策模型、样板案例

**允许进入**
- LifeOS 架构设计
- 家庭/教育/资产/工作等领域的长期框架
- 复盘后已经稳定的结论
- 需要持续扩写的正式页面

**禁止进入**
- 临时任务状态
- 一次性聊天结论
- 多步 SOP 本体
- 纯调度信息
- 敏感 secrets

**判定句**
如果内容回答的是“这是什么、为什么这么设计、和其他知识怎么关联”，优先放 `wiki`。

### 2. `memory`
**职责**
- 承载短小、稳定、值得默认注入上下文的事实
- 承载用户偏好、长期约束、环境 quirk

**允许进入**
- “Hermes 相关规划要优先参考官方文档”这类稳定行为规则
- 用户长期偏好
- 已反复验证的工具 quirks

**禁止进入**
- 长段说明
- 可展开成页面的方法论
- 项目进度
- 临时 workaround
- 任何需要小节、来源和案例才能说清的内容

**硬限制**
- 能压成一句话
- 脱离当前会话仍成立
- 未来多次默认注入确实有收益

**判定句**
如果内容不能被压成一句稳定事实，就不要进 `memory`。

### 3. `skill`
**职责**
- 承载可重复执行的方法
- 承载步骤、验证、坑点、边界和交接条件

**允许进入**
- 周报生成流程
- 知识入库流程
- 教育信息收集与整理流程
- 家庭决策例会 preparation/checklist

**禁止进入**
- 大段概念阐述
- 用户个人长期偏好本体
- 纯外部接入能力说明
- 只有一次性的临时解法

**判定句**
如果内容回答的是“这类事以后稳定怎么做”，优先放 `skill`。

### 4. `cron`
**职责**
- 调度已经稳定的方法在 fresh session 中自动运行

**允许进入**
- 每日晨报
- 每周教育基金回顾提醒
- 每日信息汇总
- 周期性检查和提醒

**禁止进入**
- 尚未稳定的方法
- 需要人工频繁改 prompt 才能工作的流程
- 只靠 cron prompt 临时拼出来的方法

**前置条件**
- 方法已存在于 `skill` 或足够稳定的自包含 prompt
- 输入输出已收敛
- 失败时可观察、可审计、可恢复

**判定句**
`cron` 只负责“何时跑”，不负责定义“怎么跑”。

### 5. `MCP`
**职责**
- 提供 Hermes 对外部实时系统的能力接入

**允许进入**
- 日历
- 邮件
- GitHub
- 文档系统
- 地图、行情、任务平台等外部接口

**禁止进入**
- 业务方法本体
- 周期性调度定义
- 长期知识沉淀

**判定句**
如果问题本质是“Hermes 怎么接入/操作一个外部实时系统”，优先看 `MCP`。

### 6. `profile`
**职责**
- 提供 Hermes 状态级隔离：配置、memory、sessions、skills、cron、gateway state

**允许进入**
- 工作/个人强隔离
- 面向外部的 bot 身份隔离
- 实验性模型与流程隔离
- 高风险自动化与主脑隔离

**禁止进入**
- 以领域为单位无节制拆分
- 代替统一知识层
- 承载主 LifeOS 语义

**硬规则**
- 没有明确隔离收益，不新建 profile
- 领域分层优先在 `wiki / skill / cron / MCP` 内完成
- 主 LifeOS 语义默认只维护在 `default profile`

**判定句**
`profile` 回答的是“要不要隔离运行时状态”，不是“这是不是一个新领域”。

### 7. `session`
**职责**
- 承载探索态、临时态、尚未验证的工作上下文

**升级规则**
- 稳定短规则 -> `memory`
- 稳定方法 -> `skill`
- 正式知识 -> `wiki`
- 周期性执行 -> `cron`
- 外部能力接入 -> `MCP`

**硬规则**
重要不等于可持久化；未稳定内容默认留在 `session`。

## Boundary matrix
### 一句话裁决表
- 外部能力：`MCP`
- 重复方法：`skill`
- 周期执行：`cron`
- 短小稳定事实：`memory`
- 正式知识资产：`wiki`
- 运行时隔离：`profile`
- 未稳定过程：`session`

### 反越界规则
- 不把概念页写成 skill
- 不把 skill 缩成 cron prompt
- 不把长篇知识塞进 memory
- 不把 profile 当领域目录
- 不把一次性聊天结论直接编译成 wiki

## Recommended topology for your Hermes
### 默认保持
- 主脑：`default profile`
- 正式知识库：`~/wiki`
- 对话入口：当前 Telegram gateway

### 只在满足条件时增加 profile
#### `work`
适用条件：需要与个人 LifeOS 分开维护工作记忆、工作 token、工作 cron、工作人格。

#### `public` 或 `bot`
适用条件：需要一个对外可暴露、可被多人触发、不能污染主脑记忆的入口。

#### `lab`
适用条件：需要实验新模型、新 prompt、新 skill、新接入，不希望影响主脑稳定性。

### 当前建议
在没有明确隔离痛点前，继续只保留 `default profile`。

## Execution plan

### Phase 0: Freeze the architecture contract
**Goal**
把这一页作为当前 Hermes LifeOS 的总边界文档。

**Actions**
1. 把本页作为后续新增 workflow 的判定基线
2. 新需求先回答“这是知识、方法、调度、能力、隔离，还是临时过程”
3. 任何新增长期层内容都必须能说明为什么不放到其他层

**Exit criteria**
- 后续新需求都能按层裁决
- 不再出现“重要所以先塞进去”的混放

### Phase 1: Build the LifeOS domain map in wiki
**Goal**
先建统一语义层，不急着开 profile。

**Must create as wiki pages**
- `concepts/lifeos-overview.md`
- `concepts/family-education-operating-model.md`
- `concepts/personal-finance-and-education-fund-model.md`
- `concepts/work-and-career-operating-model.md`
- `concepts/personal-growth-operating-model.md`

**Rules**
- 这些页面写“是什么/为什么/边界/关系”
- 不写成 SOP
- 每页都要能被其他页面链接

**Exit criteria**
- 主要人生域有正式知识页
- 领域之间关系能通过 wiki 链接表达

### Phase 2: Extract repeatable methods into skills
**Goal**
把高频动作从聊天技巧升级成可复用方法。

**Priority skill candidates**
- 家庭教育信息收集与周回顾
- 教育基金月度检查
- 重要决策对比分析
- 外部文章/信息入库与摘要标准化
- 家庭例会前的状态汇总

**Rules**
- skill 只写做法，不写大段背景百科
- 每个 skill 明确 trigger / do not use / workflow / pitfalls / verification

**Exit criteria**
- 主要高频动作不再依赖临场 prompt
- 同类任务输出结构明显收敛

### Phase 3: Add automation only after method stability
**Goal**
只给已经跑顺的方法加调度。

**Priority cron candidates**
- 每周教育基金与学校信息回顾
- 每日信息摄取摘要
- 每周家庭关键事项清单

**Rules**
- 没有稳定 skill，不上 cron
- cron prompt 必须自包含
- 每个 cron 都要有明确投递目标与失败可见性

**Exit criteria**
- 自动化任务稳定运行
- 失败可审计，且不会默默丢失输出

### Phase 4: Add MCP where external live systems become bottlenecks
**Goal**
只有当手工导入成为瓶颈时，才接实时系统。

**Priority MCP directions**
- Calendar
- Mail
- Docs/Sheets
- Maps
- Task system

**Rules**
- 先接能力，再定义 skill，再考虑 cron
- 不因“看起来高级”而提前引入 MCP

**Exit criteria**
- 外部实时信息能被稳定拉取
- 接入后的方法和调度边界仍然清晰

### Phase 5: Add profiles only for real isolation needs
**Goal**
把 profile 保持为稀缺资源，而不是默认分层手段。

**Create a new profile only if one of these is true**
- 需要独立 token / gateway 身份
- 需要独立 memory / cron / skill 污染隔离
- 需要实验性环境
- 需要工作与个人强隔离

**Do not create a new profile if**
- 只是一个新人生领域
- 只是一个新知识主题
- 只是一个可通过 skill 或 wiki 解决的方法问题

**Exit criteria**
- profile 数量少而清晰
- 每个 profile 都能说清楚隔离收益

## Operating policy
### Intake policy
所有新请求先过这一串判断：
1. 是外部能力问题吗？-> `MCP`
2. 是重复方法问题吗？-> `skill`
3. 是周期执行问题吗？-> `cron`
4. 是短小稳定事实吗？-> `memory`
5. 是正式知识吗？-> `wiki`
6. 是运行时隔离问题吗？-> `profile`
7. 都不是且未稳定 -> `session`

### Promotion policy
- chat 里形成的结论，先留 `session`
- 经过复用验证，再升级到长期层
- 升级时只进一个主层；必要时允许辅层配合，但角色必须不同

### Deletion policy
如果某项内容同时像两个层，先删掉“职责不对”的承载：
- 长文在 memory -> 拆去 wiki
- 方法在 wiki -> 抽成 skill
- 调度写死在 skill 里 -> 拆到 cron
- 领域拆成 profile -> 收回主脑

## Immediate next steps
按投入产出比，下一步顺序应该是：
1. 创建 `lifeos-overview` 总览页
2. 创建“家庭教育 operating model”页面
3. 创建“教育基金 operating model”页面
4. 抽一条高频方法做成 skill
5. 连续人工跑通 2-3 次后，再决定是否加 cron
6. 只有出现明确隔离痛点时，再创建新 profile

## Success criteria
如果这个架构跑对了，会看到：
- 你主要靠 `default profile + wiki + skills` 运转，而不是 profile 泛滥
- 新需求能快速落层，不再反复讨论“放哪里”
- 聊天产出更少停留在会话里，更多进入正式资产层
- 自动化数量不多，但稳定可控
- 每个 profile 都有明确隔离价值

## Failure signs
如果出现这些现象，说明架构在跑偏：
- 为每个主题新建 profile
- memory 越写越长、越来越像笔记
- cron 里堆复杂业务逻辑
- wiki 页面里塞步骤化 SOP
- skill 变成概念散文

## Related
- [[companyos-to-lifeos-filesystem-philosophy]]
- [[hermes-knowledge-architecture]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-layer-routing-edge-cases]]
- [[hermes-knowledge-base-operating-flow]]
- [[index]]
- [[log]]
