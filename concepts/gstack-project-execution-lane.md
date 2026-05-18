---
title: Gstack Project Execution Lane
created: 2026-04-23
updated: 2026-05-18
type: concept
tags: [gstack, project-execution, workflow, hermes, lifeos]
sources: [local-gstack-skills, session:gstack-office-hours]
status: draft
---

# Gstack Project Execution Lane

## Summary

gstack 对我最有价值的，不是一组零散 skill，而是一条从“想法澄清”到“计划收敛”再到“实现审查与验证”的项目推进链。

把最实用的 5 个 gstack skill 写入 wiki 的意义，在于把它们从“我装过的一组工具”变成“我默认怎么推进一个项目”的执行通道。这样做可以减少临时 prompt、降低上下文切换成本，并补上当前 Hermes / LifeOS 知识库里偏强于架构、偏弱于执行编排的缺口。

我当前最值得固化的 5 个 skill 是：

- `gstack-office-hours`
- `gstack-plan-ceo-review`
- `gstack-plan-eng-review`
- `gstack-review`
- `gstack-qa`

## Taxonomy decision

`gstack` 保留为 wiki taxonomy 里的 facet tag，而不是新建 entity/project 页。

理由：当前 4 个使用 `gstack` 的页面都不是在介绍一个独立外部实体，而是在描述一条被 Hermes 吸收的项目推进/审查方法：执行 lane、验证案例、office-hours 审查、eng-review 迁移计划。它的长期检索价值是“这页使用了 gstack-derived review/execution lens”，不是“这页属于某个项目”。

使用规则：

- 可用于 gstack-derived office-hours、plan review、eng review、review、QA、validation lane 页面。
- 不用作泛化的 `project` 或 `project-development` 替代品。
- 如果未来需要记录 gstack 本身的来源、版本、安装方式或外部上下文，再单独创建 entity/source 页面；当前不需要。

## Why This Matters

我现在的 Hermes / wiki 已经比较强在以下方面：

- 架构分层
- wiki / memory / skills / cron 的边界
- LifeOS 各领域 operating model
- Hermes 治理、健康检查与知识沉淀

但还缺少一条足够稳定的“项目从模糊到落地”的默认执行链。

如果没有这条链，常见问题会反复出现：

- 知道有哪些 skill，但不知道当前阶段该先用哪个
- 容易从架构讨论直接跳进实现
- 长任务中间容易漂移
- 做完以后不容易判断到底是没想清楚、没设计好，还是没测到位

gstack 的价值正好在这里：它提供了一条更接近团队化、分阶段、可复盘的推进方式。

## The 5-Skill Lane

### 1. gstack-office-hours

#### Trigger
当我遇到以下情况时先用它：

- 我有一个新想法，但还不确定值不值得做
- 我知道问题大致方向，但切口不清楚
- 我担心自己在做一个“看起来重要、其实不痛”的东西
- 我需要先把问题空间压缩到一个最小可执行切口

#### Input
- 一个模糊想法、项目方向或改进提议
- 当前背景、已有方案、限制条件
- 我直觉上觉得重要但还没被验证的判断

#### Output
- 更清楚的问题定义
- 更窄的切入点
- 什么值得做、什么先不要做
- 下一步该进入哪类计划评审

#### Value To Me
它帮助我避免过早进入实现，先判断：
- 这件事有没有真实价值
- 真正痛点是什么
- 第一刀应该切在哪

这是把“想法”变成“可计划对象”的入口。

### 2. gstack-plan-ceo-review

#### Trigger
当方向已经初步成立，但我需要从更高层判断时使用：

- 这个项目是否值得投入
- 它是否切中了真正重要的问题
- 当前方案是不是太宽、太重、太分散
- 是否存在更强的切入口或更合理的优先级

#### Input
- office-hours 后的方向定义
- 项目的目标、对象、边界、假设
- 当前拟定方案或计划草图

#### Output
- 从价值、范围、优先级角度校准后的方案
- 更清晰的主线与非主线
- 应该保留什么、删掉什么、延后什么

#### Value To Me
它的作用不是替代工程设计，而是防止我在方向层面一开始就跑偏。
它帮助我在“要不要做、先做哪块、什么先不做”上更果断。

### 3. gstack-plan-eng-review

#### Trigger
当方向已经成立，需要把它翻译成可执行工程计划时使用：

- 我已经知道要做什么，但还没拆成工程步骤
- 我需要识别依赖、风险、验证点、交付顺序
- 我不想让计划停留在“方向正确但无法执行”

#### Input
- office-hours / ceo-review 后收敛出的项目方向
- 约束条件
- 当前已有实现或空白起点
- 成功标准

#### Output
- 工程上可落地的执行计划
- 分阶段任务
- 风险点与验证方式
- 更清晰的实现顺序

#### Value To Me
它是把“值得做”转成“做得出来”的关键一步。
对我这种偏系统、偏长期架构的人来说，它能有效防止计划停留在概念层。

### 4. gstack-review

#### Trigger
当我已经做出某部分实现，准备继续推进或接近提交时使用：

- 我想检查当前方案有没有结构性问题
- 我想知道有没有遗漏明显风险
- 我不希望“看起来能跑”就等于“质量过关”

#### Input
- 当前实现结果
- 代码、配置、文档或计划产物
- 目标与验收标准

#### Output
- 结构性缺陷
- 风险点
- 应修正项
- 是否适合继续推进

#### Value To Me
它的价值在于把“自我感觉良好”换成“受审视后的继续推进”。
这一步特别适合防止我因为熟悉上下文而忽略明显问题。

### 5. gstack-qa

#### Trigger
当某个功能、流程或页面已经做出来，需要系统验证时使用：

- 我不想只凭肉眼确认
- 我需要更完整的场景验证
- 我需要知道它在真实使用路径下是否成立

#### Input
- 已实现的功能或流程
- 核心用户路径
- 预期行为和边界条件

#### Output
- 测试结果
- 缺陷列表
- 覆盖不足的路径
- 是否达到可用标准

#### Value To Me
它帮助我把“做出来了”与“真的可用”分开。
这一步是执行链里的最后一道现实检查。

## Recommended Sequence

默认顺序：

1. `gstack-office-hours`
2. `gstack-plan-ceo-review`
3. `gstack-plan-eng-review`
4. 实施
5. `gstack-review`
6. `gstack-qa`

这个顺序对应的是：

- 先判断问题值不值得做
- 再判断方向和切口是否合理
- 再把方向压成工程计划
- 然后实现
- 实现后先做结构审查
- 最后做系统验证

## Common Failure Modes

### 1. 跳过 office-hours，直接做
后果：
- 做了很多，但不一定打中真问题
- 切口过大，项目一开始就变重

### 2. 跳过 ceo-review，直接工程化
后果：
- 计划很完整，但方向不一定对
- 容易把非关键问题做得过深

### 3. 跳过 eng-review，直接实现
后果：
- 方向是对的，但任务拆分和风险控制不足
- 做着做着漂移

### 4. 跳过 review / qa
后果：
- 只验证“能不能跑”，不验证“是否可靠”
- 容易把半成品错当完成品

## How This Fits Hermes

这条 gstack lane 在 Hermes / LifeOS 里的位置，不是替代现有分层，而是补上“执行编排层”。

边界建议：

- `wiki`
  - 放长期可复用的方法页、流程页、模式页
  - 记录这条 lane 的定义、顺序、触发条件和误用方式

- `skills`
  - 放具体可调用能力
  - gstack skill 本身仍然是执行工具，不是知识目录

- `memory`
  - 不记录这些流程细节
  - 只保留稳定偏好，例如我偏好系统化推进、先 formalize 再实现

- `session`
  - 保留每次实际项目是如何使用这条 lane 的具体过程

- `cron`
  - 不适合承载这条 lane 本身
  - 但未来可以用于提醒做项目复盘或治理检查

## Practical Benefit For Me

把这 5 个 gstack skill 写进 wiki 后，最直接的收益有五个：

- 我更容易知道当前阶段该调用哪个 skill
- 我可以用统一方式推进不同类型项目
- 我能把“想到一个东西”更稳定地转成“可执行计划”
- 我能更容易复盘自己是卡在方向、计划、实现还是验证
- 我可以逐步把这条 lane 变成 Hermes / LifeOS 的默认项目推进路径

## Next Step

最合理的下一步不是继续收集更多 gstack skill，
而是先把这条 5-skill lane 固化为：

- 1 篇总页：定义顺序、触发条件、输入输出、误用方式
- 之后视需要再拆成 5 篇子页

## Related

- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-layer-routing-decision-checklist]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-lifeos-executable-architecture]]
