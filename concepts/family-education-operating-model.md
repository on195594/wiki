---
title: Family Education Operating Model
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [family, education, lifeos, operating-model]
sources: [concepts/lifeos-overview.md, concepts/hermes-lifeos-executable-architecture.md, session:2026-04-21-user-family-education-goals]
status: stable
---

# Family Education Operating Model

## Summary
这页定义家庭教育领域在 LifeOS 里的职责、目标、边界和协同关系。它不直接回答“选哪所学校”，而是定义：面对孩子成长与择校问题时，家庭教育系统应该优先优化什么、如何避免把教育问题误做成纯资源竞赛、以及 Hermes 后续该围绕哪些信息结构和决策接口提供支持。

## Core objective
家庭教育系统的核心目标不是单点名校最大化，而是：
- 让孩子在小学阶段获得稳定成长环境
- 让家庭保留足够的选择权和兜底能力
- 让教育决策与孩子个体发展相匹配，而不是只追外部标签
- 让父母的时间、财务与心理负担保持可持续

## Primary decision questions
这个领域主要回答四类问题：
1. 孩子当前最需要什么样的成长环境？
2. 家庭在资源、通勤、时间、陪伴、现金流上能稳定支撑什么？
3. 哪些学校/路径是真正适配，而不是名义上更强？
4. 如果理想方案不成立，B 方案和兜底方案是什么？

## Non-goals
以下内容不应成为家庭教育系统的主目标：
- 用学校标签替代对孩子实际需求的判断
- 用短期焦虑驱动长期承诺
- 用一次性重投入掩盖系统性支撑不足
- 为了“不能输”而损害家庭现金流和家庭关系稳定性

## Core variables
家庭教育决策至少要同时看这几组变量：
- 孩子：性格、节奏、适应性、兴趣、压力承受、基础能力
- 家庭：陪伴能力、沟通质量、作息稳定性、祖辈支持、通勤承受度
- 学校：教学风格、同伴环境、评价机制、距离、入学路径、长期连续性
- 资源：教育基金、居住成本、时间成本、机会成本
- 风险：择校失败、转学摩擦、家庭过载、教育投入失衡

## Decision principles
### 1. Child fit over label fit
优先判断“适不适合孩子”，再判断“名不名”。

### 2. Family sustainability over one-shot optimization
优先选能长期支撑的路径，而不是一次性看上去最强的路径。

### 3. Preserve fallback capacity
任何教育决策都要保留兜底能力，不能把家庭压到只剩单一路径。

### 4. Education is ecosystem design
教育不是学校单点选择，而是学校、家庭氛围、居住安排、作息结构、父母参与方式的组合系统。

## Interfaces with other domains
### 与 [[personal-finance-and-education-fund-model]] 的关系
教育路径会直接影响现金流、教育基金目标、住房与通勤成本，因此不能脱离财务模型单独决策。

### 与 [[work-and-career-operating-model]] 的关系
父母的工作强度、通勤方式、职业稳定性会影响家庭陪伴和教育执行能力。

### 与 [[personal-growth-operating-model]] 的关系
父母的表达、情绪管理、学习方式和成长观，会深刻影响教育环境质量。

## What Hermes should eventually support here
后续 Hermes 在这个领域应主要支持：
- 学校信息归档与比较
- 教育路径方案对比
- 约束条件清单化
- 家庭教育决策记录
- 周期性回顾与状态更新

这些支持未来可分化为 wiki 页面、skill 和 cron，但当前阶段先停留在正式知识层。

## Boundary
这页不包含：
- 具体学校名单与打分表
- 每周执行清单
- 自动抓取教育信息的实现细节
- 资金配置细节

这些内容后续分别进入更具体页面或方法层。

## Success criteria
家庭教育 operating model 成立时，应满足：
- 教育决策有明确目标函数，而不是随情绪漂移
- 每次讨论都能显式看到家庭约束与兜底能力
- 学校选择能落到“适配度 + 可持续性”而不是单维排名
- 家庭教育问题能与财务、职业、成长三个域联动判断

## Related
- [[lifeos-overview]]
- [[personal-finance-and-education-fund-model]]
- [[work-and-career-operating-model]]
- [[personal-growth-operating-model]]
- [[hermes-lifeos-executable-architecture]]
- [[index]]
- [[log]]
