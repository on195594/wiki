# AGY 对抗审查报告：Hermes Wiki 知识新鲜度改造计划

日期：2026-08-26
模式：只读对抗审查

## 总体裁决

**BLOCK**

AGY 的最强反对意见是：当前计划将缺少自动化支持的 `claim–evidence–status` 手工结构引入日常 Markdown，可能产生伪精确、格式分裂和维护负担；Just-in-Time 复核也可能留下未被读取的陈旧知识。

## 主要发现

### Blocking

1. **影子 Schema 与行为义务**
   - 位置：计划页“决策”“直接执行的改造”“维护责任”。
   - 失败机制：`## Evidence`、`## Verification`、四态状态和“必须标记”的表述可能被执行者理解为新 Schema 或默认门禁，但当前 health check 无法验证。
   - 建议：如果保留，必须明确它们是可选的轻量写作约定，不得把 `verified` 当作机器证明；不应把新状态当作页面权威度字段。

2. **四态状态缺少生命周期**
   - 位置：概念页“可迁移原则”、计划页 Evidence 示例和 stale 处理。
   - 失败机制：`verified/stale/unverified/inferred` 没有清除条件、负责人或状态转移规则，可能与 `status`、`review_by` 和 `[推论]` 产生双轨语义。
   - 建议：将状态缩减为自然语言说明；`[推论]` 继续沿用现有约定；易变性优先使用 `review_by`。

3. **Just-in-Time 复核可能遗漏冷门但关键页面**
   - 位置：计划页阶段 2。
   - 失败机制：未被读取的页面不会被发现陈旧，读取者可能先采信旧内容。
   - 建议：在高风险、易变页面使用已有 `review_by`，不要声称 JIT 提供全局新鲜度保证。

### Important

1. “按编辑机会渐进更新”没有收敛度量，可能造成长期格式不一致。
2. 概念页使用 `status: stable` 可能让读者误以为 Hermes 已验证并采纳了完整 OpenWiki 方法。

### Recommended

- 保留 raw 来源和文章限制。
- 将 OpenWiki 作为设计参考，不直接把其 vendor 实验结果变成 Hermes 规范。
- 最小替代方案：继续使用 `sources`、`review_by`、正文 `[推论]` 和普通 Markdown；不新增四态状态机或 Evidence 树。

## AGY 明确结论

当前计划不应按原文直接落地。若采用最小替代方案，则可继续 Wiki 日常维护，不需要另建验证项目：动态页面使用 `review_by`，推论使用 `[推论]`，来源使用现有 `sources`，发生变化时直接更新正文并刷新 `updated`。

## 父级复核说明

AGY 的真实有效风险是“可选约定被误读为强制 Schema”和“stale 状态未定义生命周期”。但 AGY 将“立即采用”本身等同于绕过治理、将所有 Wiki-only 规则都视为 active gate，属于范围夸大；审查结果需要结合 Wiki promotion 与 active adoption 的边界解释。
