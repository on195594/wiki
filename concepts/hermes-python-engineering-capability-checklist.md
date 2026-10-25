---
title: AI Agent Python Engineering Capability Checklist
created: 2026-06-16
updated: 2026-10-22
type: concept
tags: [agent, tool, ai-coding, workflow, governance, optimization, architecture, validation]
sources: [raw/articles/machinelearningmastery-python-concepts-ai-engineer-2026-06-12.md, raw/articles/realpython-python-performance-optimization-guide-2026-10-21.md]
aliases: [agent-python-engineering-capability-checklist]
status: stable
description: 列出 AI Agent 执行 Python 工程任务时的流式处理、资源、并发、类型边界，以及测量驱动的性能优化检查项。
volatility: medium
review_by: 2027-01-31
---

# AI Agent Python Engineering Capability Checklist

## Summary

AI Agent 的 AI 能力提升不只来自更强模型，也来自更可靠的 Python 工程边界：大输入要流式处理，资源要有生命周期管理，网络型任务要支持有界并发，工具参数要结构化校验，自定义对象要遵守 Python 协议；性能改动先测量、定位，再做最小优化并复测。

这页把 MachineLearningMastery 文章 `Python Concepts Every AI Engineer Must Master` 转换为 AI Agent 工作流检查清单，并用 Real Python 的 `Python Performance Optimization: A Practical Guide` 补充性能诊断顺序。两者都是教学来源；本页只保留可复用工程原则，不把示例性能数据当作生产基准。

## Core principle

> AI agent 的可靠性取决于工具边界、资源状态、输入规模、并发控制和验证闭环；Python 代码应把这些约束显式化，而不是依赖模型临场判断。

## Durable units from the article

### 1. Large inputs should default to streaming

适用场景：

- 网页正文提取
- 摘要工作流的长文本输入
- 日志分析
- JSONL / CSV / 数据库导出
- 批量文件处理
- 大规模 API 响应聚合

检查项：

- 输入是否可能超过几 MB？
- 是否先构造了完整 list 再处理？
- 是否可以改成 iterator / generator / chunk pipeline？
- 是否保留 source metadata 和 extraction note？
- 是否有截断、摘要化、抽取失败的质量标记？

AI Agent 映射：

- 摘要与内容提取工作流 应优先保持 source packet 可追溯；
- 大输入清洗应避免一次性粗暴拼接；
- 需要清楚区分 full source、partial source、extractor-generated digest。

### 2. Resource state needs context-managed boundaries

适用场景：

- 浏览器 / CDP session
- 临时目录和缓存
- 文件句柄
- 数据库连接
- API client session
- 锁文件
- 长任务 runner
- 模型状态或推理上下文

检查项：

- 是否有 setup / teardown？
- 异常发生时是否一定释放资源？
- 是否恢复原状态？
- 是否写入必要审计信息？
- 是否能 rollback 或安全重试？

AI Agent 映射：

- runtime 操作中，浏览器、进程、缓存、锁不应依赖人工清理；
- 工作流脚本中，临时资源应封装为 context manager 或等价的 cleanup boundary；
- 失败路径必须和成功路径一样维护 metadata。

### 3. Network-bound workflows should use bounded concurrency

适用场景：

- 多 URL 提取
- 多 API 查询
- 多 agent / subagent 执行
- 向量库查询
- LLM 批量调用
- 状态巡检

检查项：

- 瓶颈是否是网络 I/O？
- 是否存在无界并发？
- 是否设置 timeout？
- 是否设置 retry 和 backoff？
- 是否有 rate limit？
- 部分失败是否能隔离？
- 输出是否保持可复现排序？
- 是否记录每个子任务的状态和证据？

AI Agent 映射：

- subagent/workflow 并发不应只是“同时发出去”；
- 需要有并发上限、失败归并、证据 readback 和停止条件；
- 对外部 API 或付费调用，必须保留 side-effect 和成本边界。

### 4. Tool and config boundaries should be typed

适用场景：

- AI Agent tool wrapper
- CLI 参数
- YAML / JSON 配置
- LLM tool calling schema
- 项目模板
- 批处理任务参数
- Agent handoff contract

检查项：

- 参数是否仍是裸 dict？
- 是否存在静默默认值？
- 是否校验枚举、范围、路径、URL、布尔开关？
- 内部结构是否适合 dataclass？
- 边界输入是否需要 Pydantic / schema？
- 错误信息是否能指导 AI 修正调用？

AI Agent 映射：

- dataclass 适合内部状态；
- Pydantic 适合边界校验、配置解析和 tool schema；
- 不应把 Pydantic 强推到所有纯内部函数；
- 新三方依赖仍需项目级确认，已有依赖才可直接使用。

### 5. Custom abstractions should follow Python protocols

适用场景：

- task queue
- artifact collection
- dataset-like wrapper
- callable workflow object
- validation result container
- model/tool adapter

检查项：

- 对象是否应该支持 `len()`？
- 是否应该支持索引或迭代？
- 是否应该是 callable？
- 是否需要 context manager？
- 是否会被外部框架或通用工具消费？
- magic methods 是否只是提升协议兼容，而不是炫技？

AI Agent 映射：

- 适合长期复用的内部对象应优先遵守 Python 协议；
- 不要为一次性脚本过度设计 magic methods；
- 当对象进入框架、模板、队列、runner 时，再补协议边界。

### 6. Performance work should be measurement-led

来源：[[realpython-python-performance-optimization-guide-2026-10-21]]（Mostafa Ibrahim，Real Python，页面更新于 2026-10-21）。它补充的是性能诊断与优化顺序，不替代前述资源、并发和类型边界。

**原文原则：**

- **先区分定位与计时。** 不知道程序哪里慢时，用 `cProfile` 等 profiler 找热点；已怀疑某段函数时，再用 `timeit` 比较候选。微基准不能单独证明该函数是端到端瓶颈。
- **按成本逐级处理，够用就停。** 先检查算法和数据结构，再找内置函数/标准库，随后考虑重复计算缓存；内存布局、并发和 C 扩展留给简单修复不足的情况，不是必须走完的步骤。
- **数据结构看访问模式与总成本。** `list` 成员查找通常为 O(n)，`set` 平均为 O(1)，但构建集合有成本；单次查询不应假定转换一定获益。原文的构建成本估算不作为通用盈亏平衡点。
- **标准库不等于自动提速。** 原文中 CPython 的 `Counter` 可把逐项计数交给 C helper，但把循环改写为 `any()` 仍可能保留 Python 层逐项工作；替换后照样测量。
- **缓存先保正确，再看速度。** 重复参数且结果稳定时才考虑缓存；原例读取全局列表，但 key 只有 `target`，列表改变后会返回陈旧答案。`cache` 无界保留条目；有容量约束时考虑有界 `lru_cache`，不照抄示例容量。
- **冷启动与命中分开。** 原文缓存计时前已调用一次函数；测到的是热缓存命中，而非第一次计算变快。不可把两种工作量的比较描述为算法本身加速。

**[推论] 项目落地的最小检查闭环：**

1. 先定义要改善的端到端指标与可接受目标，保留正确性基线；区分 CPU、I/O、等待和内存压力。
2. 使用有代表性的输入、相同解释器/环境建立基线；记录总耗时、调用次数和单次耗时，不混淆量纲。重复测量，并分别说明数据结构构建、I/O 与缓存预热是否计入。
3. 一次只改一个已测热点，优先消除重复工作、选择现成容器或标准库；复用现有测试验证输出、异常和资源生命周期不变。
4. 如需缓存，核对参数可哈希、隐藏状态/外部数据变化、失效与容量，以及返回可变对象的共享风险；测冷缓存、热缓存和实际命中率，不只测理想命中路径。
5. 在相同条件下复测微基准与端到端指标；达标即停止。并发仍受第 3 节的超时、限流、失败隔离约束，不能为提速删除这些边界。

**适用边界：** 原文是概念性教程，不是生产基准研究；本页未运行示例或复现加速倍数。生成器主要降低峰值内存，并不保证更快；线程、进程和异步的收益受解释器构建、原生库、任务粒度及通信成本影响，不能只凭 CPU/I/O 标签定方案。这里的检查闭环是本页推导，不声称原文已证明项目收益，也不授权增加依赖、改生产代码或运行配置。

这与 [[software-engineering-laws-planning]] 中“避免过早优化”的原则一致；结果验收沿用 [[agent-self-validation-loops]]，缓存命中与端到端成本的评估范围另见 [[production-agent-evaluation-baselines]]。

## AI Agent adoption matrix

| Capability | Primary layer | Recommended artifact | Priority |
|---|---|---|---|
| Streaming large input | summary / extraction workflows | skill reference checklist | P0 |
| Typed tool/config boundary | project templates / tool wrappers | template + skill reference | P0 |
| Context-managed resources | runtime operations or Python project templates | wiki concept or template note | P1 |
| Bounded concurrency | subagent/workflow orchestration | skill reference checklist | P1 |
| Python protocol compatibility | reusable Python project code | template note | P2 |

## Non-goals

- 不把原文作为 Python 语法教程维护；
- 不把示例 benchmark 当成 AI Agent 性能基准；
- 不把 Pydantic 引入所有项目；
- 不新增 runtime dependency；
- 不改 active workflow 行为，除非后续有单独实现计划和验证。

## Promotion rules

当未来改 AI Agent workflow 或 Python 项目模板时，使用本页作为检查清单：

1. 大输入：是否流式？
2. 资源：是否有 cleanup boundary？
3. 并发：是否有 timeout/rate-limit/failure isolation？
4. 参数：是否有 typed validation？
5. 抽象：是否遵守必要 Python protocol？
6. 验证：是否有测试、readback 或 smoke evidence？
7. 性能：是否已定位热点、保留基线，并区分冷/热缓存、微基准与端到端复测？

## Relations

- related: [[hermes-ai-workflow-formalization-principles]], [[agentic-programming-system-engineering]], [[agent-context-engineering]], [[typed-ai-agent-boundaries]], [[software-engineering-laws-planning]], [[agent-self-validation-loops]], [[production-agent-evaluation-baselines]]
