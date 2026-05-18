---
title: Hermes Skill 重构方法论
author: Hermes Agent
created: 2026-05-15
updated: 2026-05-18
type: concept
tags: [hermes, skills, workflow, governance, verification, ai-coding, subagent]
sources: [session:2026-05-15-test-driven-development-skill-refactor-plan, session:2026-05-15-test-driven-development-phase4-closeout, session:2026-05-15-gemini-review-tdd-phase4-output]
status: stable
---

# Hermes Skill 重构方法论

## Summary

`test-driven-development` 的优化说明：skill 重构不应从“大重写”开始，而应先把职责边界、硬安全线、合法例外、reference 分层和独立审查闭环做清楚。主 `SKILL.md` 只保留执行时必须看到的规则；长案例、领域清单、项目经验下沉到 `references/`；最后用本地静态检查和独立模型审查关闭。

这套方法适用于 Hermes active skill 的治理型改造，尤其是一个 skill 已经混入过多项目特例、执行入口过重、或与其他 skill 职责边界变模糊时。它连接 [[hermes-context-layer-operating-rules]]、[[hermes-knowledge-architecture]]、[[agent-self-validation-loops]] 和 [[subagent-orchestration-patterns]]。

## Case: test-driven-development

改造目标：把 `test-driven-development` 从“强硬 TDD 教条 + 大量项目特例合集”收敛成“窄而清晰的 TDD 执行纪律 skill”。

最终定位：

- 不是 Telegram 编程任务总入口。
- 是 `coding-agent-workflow` 在新功能、bugfix、行为变更、风险 refactor、review finding 回归测试时触发的专用执行 skill。
- 核心仍是 RED → GREEN → REFACTOR：先写测试、确认失败、最小实现、确认通过、再重构。
- 合法例外必须显式命名，尤其是 coverage-only hardening。

## 原始问题

1. 主文档过长：decision-support、cash-state、CLI runner、risk guardrail 等历史项目特例占比过高。
2. 合法例外太靠后：coverage-only 允许测试立即通过，但位置靠后，容易和前文绝对语气冲突。
3. 安全边界不集中：生产 DB、live API、支付、通知、真实状态文件等测试边界需要前置。
4. skill 边界不清：root cause、planning、subagent 编排、TDD 执行纪律混在一起。
5. closeout 证据不硬：缺少 RED / GREEN / Regression 三类证据的固定报告格式。

## 分阶段改造模式

### Phase 0: 只读基线

先读主文档和 references，统计领域特例位置，不修改 active skill。

产出：当前结构、风险清单、待迁移段落、目标 reference 判断。

### Phase 1: 主文档结构补丁

只改主 `SKILL.md` 的结构和前置边界，不移动 reference 文件。

关键动作：

- 前置 `When to Use / When Not to Use`。
- 前置 `Hard limits`。
- 提前 coverage-only hardening。
- 增加 closeout 模板。
- 保留 TDD 核心语义，不软化原则。

验收点：skill 可加载；前 80 行能看到适用范围、例外、安全边界；RED / GREEN / REFACTOR / failing test first 仍存在。

### Phase 2: 领域特例引用化

把主路径中的长领域段落替换为 reference routing 索引。

关键动作：

- 保留所有 reference 内容，不删除知识。
- 主文档只保留触发词和加载路径。
- 每个 reference 索引条目必须有 agent 能从任务描述识别的触发关键词，不能只是文件名。
- 安全边界、授权边界、RED/GREEN 证据要求仍留在主文档。

核心判断：这一步不是“压缩字数”，而是把运行时必须常驻的规则和场景特例分层。

### Phase 3: delegate_task 和父验证强化

防止 subagent self-report 直接变成完成结论。

关键动作：

- delegate goal 要求返回 changed files、RED command、GREEN command、Regression command、exit code、summary。
- coverage-only 模式要返回 false-negative check 结果，或说明为什么只能算 provisional coverage。
- 父 agent 必须验证关键声明：重新运行测试、读回变更，或检查父 agent 可直接控制的 session 输出。
- 重复非收敛失败时停止，报告证据和下一步诊断，不盲修。

### Phase 4: 独立审查与收敛

对 Phase 1-3 修改后的实际 skill 和 references 做只读审查。

审查维度：职责边界、过度瘦身、安全边界、reference 可发现性、TDD 原则、coverage-only 自洽性、delegate_task 证据要求、父 agent 验证规则。

收敛规则：只接受 blocking / important findings；minor suggestions 不阻塞关闭；没有 blocking / important findings 时冻结，不继续打磨。

## 关键设计原则

### 默认入口要轻

一个 skill 的主文档不是知识仓库。主文档应回答：什么时候用、什么时候不用、执行纪律是什么、有什么硬边界、如何验证完成。长案例和领域经验应进入 `references/`。

### 专用流程要窄

`test-driven-development` 只负责 TDD 执行纪律。根因分析归 debugging workflow，多步计划归 planning workflow，subagent 编排归 orchestration workflow。

### 安全边界全局可见

测试安全线必须在主文档早期出现：不削弱测试、不碰生产 DB/live API/支付/通知/真实状态文件、不未经批准新增依赖、不用手动验证替代回归测试、不信 subagent self-report。

这些边界不应只存在于 references，因为主 skill 被加载时才是最低保证。

### 合法例外要命名并同步

coverage-only 是 TDD 中容易被误判的合法例外：新测试可能立即通过，但这不等于测试无效。

必须同步更新：

- 适用范围：前置 coverage-only。
- Verify RED：测试立即通过时做 false-negative check，而不是改测试。
- Red Flags：避免把“test passes immediately”绝对化。
- Checklist / Completion Report：记录 false-negative check 或 provisional coverage。

例外一旦出现，就要同步所有快速扫描位置，否则 skill 内部会自相矛盾。

### Reference routing 要有触发词

只列 `references/foo.md` 不够。每条 routing 都要写出触发条件，例如：

- run ID collisions / atomic report writes / run locks → CLI reliability reference。
- placeholder URLs / domain-only source normalization / final output deduplication → search runner postprocessing reference。
- missing implementation contracts / subprocess CLI behavior / temp run directories → contract-first runner tests reference。

触发词决定 agent 能不能在任务描述中识别该加载哪个 reference。

### 审查结果必须再验证

独立审查不是终点。findings 要分级，修完后重新做静态检查、skill 加载验证，必要时二次独立复审。这对应 [[agent-self-validation-loops]] 的验证闭环，而不是“让另一个模型说好就结束”。

## 可复用检查清单

改造任意 active skill 前，先问：

- 这个 skill 的单一职责是什么？
- 它是否承担了本该由其他 skill 处理的入口职责？
- 主文档前 80 行是否包含适用范围、合法例外和硬安全边界？
- 哪些内容是执行时必须常驻的规则？哪些应迁到 references？
- references 是否有可识别触发词？
- completion report 是否要求可验证证据？
- subagent 输出是否需要父 agent 验证？
- 有无覆盖合法例外的同步点，例如 Verify / Red Flags / Checklist / Closeout？
- 是否有独立审查、accepted finding patch、最终加载验证？

## 反模式

- 把一次成功经验直接膨胀成主 skill 大段规则。
- 用“更完整”为理由把领域特例堆进主文档。
- 把安全边界迁到 reference，导致默认加载时不可见。
- 只让 Claude/Gemini 审查计划，不审查最终 active 文件。
- 把 minor suggestion 当成继续打磨的理由，导致计划—审查—再计划循环。
- 忘记同步合法例外，导致 Verify RED、Red Flags、Checklist 互相冲突。
- 相信 subagent 自述，没有父 agent 复核命令、输出或文件。

## 最终结果

本次 `test-driven-development` 改造最终关闭条件：

- skill 版本：`1.2.1`。
- 主文档可加载。
- 全部 references 存在并在主文档中有触发词。
- Gemini Phase 4 独立审查结果：`approve`。
- blocking findings：None。
- important findings：None。
- Phase 4 closeout：ready。

最终经验：skill 优化不是把规则写得更多，而是让默认路径更短、边界更硬、例外更明确、证据更可验证。
