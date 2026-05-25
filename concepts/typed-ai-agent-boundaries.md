---
title: Typed AI Agent Boundaries
created: 2026-05-01
updated: 2026-05-22
type: concept
tags: [agent, ai-coding, typed-boundary, structured-output, pydantic, governance]
sources: [raw/articles/machinelearningmastery-pydantic-ai-agents-2026-04-29.md, concepts/dijkstra-ai-programming-formalization.md, concepts/hermes-ai-workflow-formalization-principles.md]
status: stable
---

# Typed AI Agent Boundaries

## Summary

Pydantic AI 这篇文章的长期价值，不是“又一个 Python agent 框架教程”，而是给出了一种降低 AI 编程不确定性的工程边界：把 LLM 的自然语言输出、工具调用和外部依赖，压进 typed schema、typed function tools 和 dependency injection 里。模型仍然不确定，但系统边界变得更可验证、可测试、可替换。

这页补充 `[[dijkstra-ai-programming-formalization]]` 与 `[[hermes-ai-workflow-formalization-principles]]`：前者说明 AI 编程仍需要形式化，后者说明 Hermes 应采用“自然语言输入 + 形式化约束 + 验证闭环”；本页把这个原则落到 agent runtime 内部的三个窄接口上。

## Core pattern

### 1. Structured output turns language into objects

普通 LLM 调用返回自然语言字符串，工程系统随后需要用正则、脆弱 JSON 解析或 prompt 约定去猜格式。Pydantic AI 的 `output_type` 把期望输出定义为 Pydantic `BaseModel`：字段、类型、约束和说明都成为模型必须满足的 schema。

这降低了两类不确定性：

- 输出形状不确定：字段是否存在、类型是否正确、列表/布尔/枚举是否可用。
- 下游处理不确定：业务代码拿到的是已验证 Python 对象，而不是一段待解释文本。

重要细节：`Field(description=...)` 不只是文档，也是在给模型提供字段级约束。字段说明越明确，校验失败和自动重试越少。

### 2. Tool functions define a narrow action surface

Agent 需要调用外部世界时，最危险的不是“能不能调工具”，而是工具边界是否宽到足以被误用。Pydantic AI 用普通 Python 函数注册工具，让类型提示和 docstring 成为模型理解工具用途的主要依据。

这带来一个直接规则：暴露给 agent 的工具函数必须像 public API 一样写。

- 参数类型要精确。
- 返回值要稳定。
- docstring 要说明何时使用、输入含义、限制和失败语义。
- 工具应尽量小而窄，避免一个函数同时承担查询、修改、删除、推断多种职责。

### 3. Dependency injection removes hidden global state

生产 agent 往往需要数据库连接、API client、session 信息、租户权限或运行时配置。如果这些依赖隐藏在全局变量里，agent 行为会变得难测试、难复现，也更难做权限治理。

Pydantic AI 的 `RunContext` 模式把依赖作为运行时参数注入工具函数。它的价值不只是代码整洁，而是把外部环境显式化：

- 测试时可以替换成 mock / fake service。
- 不同用户、租户、权限上下文可以隔离。
- 工具函数不需要读取隐式全局状态。
- 失败可以被定位到模型输出、工具实现或依赖服务，而不是混在一起。

## What uncertainty this solves

它主要解决 agent 工程中的“边界不确定性”：

- 输出是否符合业务可消费结构。
- 工具是否被以正确参数调用。
- 外部依赖是否可替换、可测试、可审计。
- 验证失败时是否能重试或报错，而不是把坏数据继续传下去。

它不解决所有 AI 不确定性：

- 模型仍可能误解任务。
- 多步推理仍可能漂移。
- 工具选择策略仍可能错误。
- 自动重试会增加 token 成本和延迟。
- 权限、安全、审计、回滚仍需要平台层设计。

因此更准确的结论是：typed boundaries 不会让模型确定，但会让模型和业务系统之间的接口更确定。

## Hermes mapping

### Wiki

这类文章应进入 wiki，而不是 memory：它需要来源、结构、交叉链接和后续扩写。raw source 保留在 `raw/articles/`，可复用模式沉淀为本页概念。

### Skill

如果未来在 Hermes 中实际采用 Pydantic AI 或类似框架构建 agent，才应把具体开发流程沉淀为 skill。当前只保留为概念原则，不提前写执行 SOP。

### MCP / internal tools

对企业内网 AI 编程集成，这个模式可以翻译成：不要让 agent 直接访问数据库或业务系统；应暴露窄工具接口，并让每个工具继承原系统权限、记录审计日志、返回 typed result。

### Verification

Hermes 现有规则“写完要验证”可以进一步细化为：agent 输出进入业务系统前必须经过 schema validation；工具调用必须有类型边界；依赖必须能在测试环境替换。

## Operating rules

- 对任何进入生产链路的 LLM 输出，优先定义 schema，而不是信任自然语言格式。
- 对任何暴露给 agent 的工具，优先当成 public API 设计，而不是临时 helper。
- 对任何外部依赖，优先通过显式上下文注入，而不是全局变量。
- 对任何自动重试机制，都要设置成本、延迟和失败上限。
- 对任何 agent workflow，都要区分“模型不确定性”和“接口不确定性”：前者只能降低，后者必须工程化约束。

## What this adds to the existing wiki

- `[[dijkstra-ai-programming-formalization]]` 说明为什么 AI 编程仍需要形式化。
- `[[hermes-ai-workflow-formalization-principles]]` 说明 Hermes 应把模糊自然语言收敛成可验证结构。
- 本页补上 agent 内部的具体工程边界：structured output、function tools、dependency injection。
- `[[ai-coding-agent-workflow-types]]` 关注 agent 放在哪种执行入口中；本页关注 agent 进入工程系统时接口如何收窄。

## Relationship to document fidelity risk

`[[ai-agent-document-fidelity-risk]]` explains why wide file read/write tools are not sufficient safety controls for autonomous document work. Typed boundaries should be paired with narrow, domain-specific tools and explicit validation of content preservation.

## Applied Hermes practice

- [[how-i-should-use-hermes-for-ai-coding-with-typed-boundaries]] 将本页原则转成我使用 Hermes 做 AI 编程时的默认最佳实践：先压 contract，再选择 execution lane，再用 typed output、窄工具、显式依赖和分层验证控制不确定性。

## Related

- [[dijkstra-ai-programming-formalization]]
- [[hermes-ai-workflow-formalization-principles]]
- [[ai-coding-agent-workflow-types]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-layer-routing-decision-checklist]]
- [[how-i-should-use-hermes-for-ai-coding-with-typed-boundaries]]
- [[ai-agent-document-fidelity-risk]]
- [[constrained-toolbox-evaluator-loop]]
- [[deterministic-analytics-llm-reasoning-boundary]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
