---
title: How Google SREs Use Gemini CLI to Solve Real-World Outages
author: Riccardo Carlesso, Ramón Medrano Llamas
source_type: blog
source_url: https://cloud.google.com/blog/topics/developers-practitioners/how-google-sres-use-gemini-cli-to-solve-real-world-outages
published_at: 2026-01-22
captured_at: 2026-04-16
status: raw
---

# 原始材料说明

来源为 Google Cloud Blog，主题是 Google SRE 如何在真实风格的故障处理中使用 Gemini CLI。
本页保留的是结构化原始摘录，重点覆盖文章里的事故流程、工具设计、安全机制与 postmortem 自动化。

# 原始摘录

## 文章主问题
- Google SRE 如何把 Gemini CLI 用进真实故障处理流程，而不是只把它当问答机器人？

## 文章核心主张
- Gemini CLI 的价值不在于回答“应该怎么做”，而在于把事故响应中的调查、分析、缓解、修复和复盘流程串起来。
- AI 在生产环境中应充当 copilot，而不是 autopilot。
- 事故处理中最关键的指标之一是尽快止血，缩短 MTTM（Mean Time to Mitigation），而不是先追求彻底修好。

## 关键背景
- Google SRE 的核心文化之一是 Eliminate Toil
- 事故影响通常表现为 Bad Customer Minutes 与 Error Budget 消耗
- SRE 经常需要在很短时间内确认告警并开始缓解
- 标准事故流包括：Paging -> Mitigation -> Root Cause -> Postmortem

## 文章结构化要点

### 1. 先止血，再修根因
文章强调：
- 故障发生后，第一优先级是 mitigation
- 修根因和写代码不是第一页要做的事
- 事故处理的关键不只是 MTTR，还包括 MTTM，即尽快停止用户痛感

### 2. 通过工具链自动收集上下文
Gemini CLI 通过 ProdAgent 内部函数 `fetch_playbook` 串起多类分析工具，包括：
- `get_incident_details`
- `causal_analysis`
- `timeseries_correlation`
- `log_analysis`

这些工具帮助它：
- 读取告警上下文
- 找异常时间序列
- 找相关指标
- 做日志模式分析
- 选择最合适的缓解 playbook

### 3. 使用有限、标准化的通用缓解动作
文章引用 Generic Mitigations 的思路，把缓解动作压缩为有限集合，例如：
- drain traffic
- rollback
- restart
- add capacity

这样 AI 做的不是自由发挥，而是在已知、安全边界更清楚的动作集合里做选择。

### 4. 案例中的推荐动作：restart
在模拟事故里，Gemini CLI 根据上下文推荐 `borg_task_restart` 作为缓解动作。
文章将其类比为类似 Kubernetes pod restart 的操作。
工程师在审查后给出批准：
- “SGTM, execute the restart.”

### 5. 生产安全的多层保护
文章强调 Gemini CLI 不是直接放权给模型，而是通过多层安全机制约束：
- 使用确定性工具调用，而不是让模型任意生成 shell 脚本
- 给工具标记风险级别，例如 safe / reversible / destructive
- 允许策略系统按上下文阻止危险动作
- 保留 human-in-the-loop，由人做最终批准
- 所有提议和执行保留审计轨迹

### 6. AI 是副驾，不是自动驾驶
文章专门解释为什么生产自治不能简单放开：
- 某个动作在一个系统状态下安全，在另一个状态下可能危险
- 例如 rollback 平时可能安全，但在配置推送期间可能不安全

所以重点不是“让 AI 自己做完”，而是让它更快地提出合格方案，并让人更快审批。

### 7. 止血之后继续推进工程闭环
Gemini CLI 不只参与止血，还可以继续支持：
- 代码修复
- 创建 CL
- 生成 postmortem
- 追踪后续 action items

文章把 postmortem 定义为无责复盘文档，目的是学习与改进，而不是追责。

### 8. 面向外部的能力扩展
文章还强调 Gemini CLI 已向外部开放，并可通过 MCP Servers 接入团队自己的工具，例如：
- Grafana
- Prometheus
- PagerDuty
- Kubernetes

还可以通过 Custom Commands 固化团队自己的流程，比如 postmortem 生成命令。

## 压缩结论
- 这篇文章不是在说“AI 能自动运维”，而是在说“AI 可以把高摩擦的事故流程做成人机协作系统”。
- SRE 真正得到的收益是减少 toil、提升缓解速度、降低认知切换成本。
- 文章最核心的设计原则是：标准化动作集合 + 受控工具调用 + 人类审批 + 审计留痕。
