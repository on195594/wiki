---
title: Hermes Wiki Knowledge Freshness Architecture v2
created: 2026-09-09
updated: 2026-09-09
type: plan
status: closed
tags: [hermes, knowledge-base, governance, verification, architecture, workflow]
sources:
  - concepts/hermes-knowledge-architecture.md
  - concepts/hermes-knowledge-freshness-and-claim-evidence.md
  - concepts/hermes-retrieval-priority-and-answer-path.md
  - concepts/hermes-wiki-page-writing-standards.md
  - concepts/wiki-ingestion-workflow.md
  - queries/hermes-wiki-knowledge-freshness-improvement-plan.md
---

# Hermes Wiki Knowledge Freshness Architecture v2

## 1. 目标

本方案面向“Wiki 主要供 AI Agent 检索和复用”的长期运行场景，解决以下问题：

1. 已经正确写入的知识随着外部世界变化而失效，但 Agent 仍继续复用。
2. `status: stable` 被误解为“当前仍然正确”。
3. `updated` 只能说明文件被编辑过，不能说明整页或具体结论已重新验证。
4. 新来源进入 `raw/` 后，系统缺少可解释的受影响页面候选发现路径。
5. `supersedes`、`conflicts_with` 等关系已存在，但尚未成为 Agent 检索阶段的硬约束。
6. 页面同时包含稳定原则和高波动事实时，整页级 `review_by` 粒度过粗。
7. 知识库能够持续增加知识，但缺少同等清晰的“失效、重审、替代、退役”路径。

本方案的核心原则：

> 知识进入 Wiki 不代表永久可信；每次被 Agent 使用时，都应重新判断它此刻是否仍有资格作为答案依据。

## 2. 非目标

本方案明确不做以下事项：

- 不引入独立数据库、Neo4j、向量数据库或新的知识图谱运行时。
- 不为每一句正文建立 claim ID。
- 不建立全库定时 LLM 重写或全自动事实证明系统。
- 不把 `status` 扩展成 `stale / verified / unverified` 等混合状态机。
- 不要求一次性迁移全部历史页面。
- 不因实现 freshness 机制而修改 Hermes memory、skills、runtime、cron、MCP 或 provider。
- 不自动覆盖存在冲突但尚未解决的旧知识。

继续保持 Markdown-first、Git-backed、raw immutable、formal-page canonical 的现有架构。

## 3. 设计原则

### 3.1 生命周期与新鲜度分离

`status` 只表达知识对象的生命周期：

- `draft`
- `stable`
- `active`
- `closed`
- `current`

它不表达“截至今天仍然真实”。

知识的新鲜度由独立字段和运行时规则判断。

### 3.2 Freshness 是检索时计算结果，不是永久标签

不新增 `fresh / stale / invalid` 到页面 status。

Agent 在检索时根据以下因素计算当前状态：

- `status`
- `volatility`
- `verified_at`
- `review_by`
- `supersedes`
- `conflicts_with`
- 来源适用范围
- 当前问题的时间/版本/环境上下文

输出为运行时状态：

- `GREEN`：可直接作为当前答案依据。
- `YELLOW`：可作为候选背景，但必须验证后才能作为当前事实。
- `RED`：不得作为当前确定性事实使用。

### 3.3 写入时正确不等于读取时仍然正确

Wiki 继续执行现有 write-time governance：来源、frontmatter、raw hash、links、tags、health check。

新增 read-time governance：Agent 每次消费高价值知识时先通过 Freshness Gate。

### 3.4 变化触发失效候选，而不是自动重写

新来源、版本变化或冲突出现时：

`source event -> exact dependents or explained candidates -> needs review -> verify -> patch`

禁止：

`source changed -> LLM automatic rewrite -> overwrite canonical knowledge`

### 3.5 稳定知识和易变知识使用不同维护成本

不应因为存在 freshness 机制，就周期性复查所有方法论、历史知识和稳定原理。

维护成本集中在高波动知识上。

## 4. Schema v2：第一阶段只新增两个可选字段

正式页面允许增加：

```yaml
volatility: low | medium | high
verified_at: YYYY-MM-DD
```

现有字段继续保留：

```yaml
review_by: YYYY-MM-DD
```

三个字段语义严格区分。

### 4.1 `volatility`

表示知识对象对应现实世界的变化速度，不表示知识质量。

#### low

典型对象：

- 数学原理
- 长期稳定的软件工程原则
- 已稳定的方法论
- 历史事实
- Hermes 自定义且未发生变更的规范性规则

默认行为：没有明确事件触发时，不因为年龄自动外部验证。

#### medium

典型对象：

- Agent 架构模式
- 工程最佳实践
- 某一生态的推荐工作流
- 项目架构说明
- 依赖外部工具但不绑定单一具体版本的方法页

默认行为：页面较久未验证且问题依赖其“当前适用性”时进入 YELLOW。

#### high

典型对象：

- 当前 API / CLI 行为
- 当前模型能力
- 当前软件配置字段
- provider/tool/runtime 当前特性
- 当前 benchmark / pricing / limits
- 当前法规、市场状态、版本行为

默认行为：若要作为当前事实，必须具备 `verified_at` + `review_by`；缺失或到期后进入 YELLOW，存在明确替代/冲突时可进入 RED。

#### 字段缺失时的默认判定

`volatility` 缺失不等于 `low`。对未迁移的历史页面按当前问题实际依赖的内容判定：

- 涉及当前/版本化外部事实，或适用性无法确认：YELLOW。
- 明确的稳定方法论、低波动原理，或处于明确时间范围内的历史知识，且无替代或未解决冲突：GREEN。

### 4.2 `verified_at`

表示最近一次对页面相关易变结论进行真实核对的日期。

规则：

- 只有实际检查过来源、运行状态、项目事实或权威文档时才能更新。
- 普通文字编辑不能刷新 `verified_at`。
- 有效的 `verified_at` 必须是合法日期且 `verified_at <= today`；未来日期不能表示已经完成的验证。
- 页面级 `verified_at` 只在页面内所有会被当作“当前事实”的易变结论都完成复核时使用。
- 只复核局部内容时，不得刷新页面级 `verified_at`；应对相关 claim 使用局部 `verified_at` 标记。
- 局部标记只赋予被标记 claim 独立的新鲜度资格，不能把整页提升为 GREEN。

### 4.3 `review_by`

表示该日期结束后，Agent 不应再无条件把相关易变知识当作当前事实。

规则：

- 到期不等于“错误”。
- 到期意味着从 GREEN 降为 YELLOW。
- 验证仍成立：刷新 `verified_at` 与 `review_by`。
- 验证已变化：修改受影响内容并保留必要的 supersession/历史说明。
- 无法验证：不得删除 `review_by` 来消除告警。

## 5. 默认字段策略

不做全库批量迁移。

### 新页面

仅当页面包含外部变化会改变 Agent 行为的知识时添加 `volatility`。

推荐：

```yaml
volatility: high
verified_at: 2026-09-09
review_by: 2026-10-09
```

### 现有页面

只在以下情况触发补充：

1. 页面本次被实际编辑。
2. 页面被 Agent 高频检索并直接驱动操作。
3. 页面包含 API、CLI、模型、provider、版本、配置等当前行为。
4. 页面因来源变化进入 review candidate。
5. 页面曾因过时信息导致错误回答或错误操作。

### 不应补字段的页面

- 纯历史记录
- 已 closed 的审查/计划
- 稳定数学/计算机科学原理
- 不依赖当前外部状态的方法论
- 仅引用某工具作为例子的抽象概念页

## 6. Freshness Gate

Agent 在 Wiki 检索完成后、生成最终事实结论前执行 Freshness Gate。

### 6.1 输入

对于每个候选页面至少读取：

- path
- title
- status
- updated
- volatility（若有）
- verified_at（若有）
- review_by（若有）
- sources
- Relations
- 与当前问题直接相关的 claim/section 及其局部 `verified_at`（若有）
- 当前用户问题中的时间、版本、产品、环境约束

### 6.2 GREEN

满足以下条件之一：

1. 稳定低波动知识，且不存在 superseded / unresolved conflict。
2. medium/high volatility 知识满足 `verified_at <= today <= review_by`，且来源和当前上下文匹配。
3. 当前问题只依赖页面中的稳定方法论，而不是易变事实。
4. 当前问题只依赖一个具备完整局部 `verified_at`、`review_by` 和来源的易变 claim，且满足 `verified_at <= today <= review_by`；此时只有该 claim 为 GREEN，页面其余内容不随之升级。

Agent 行为：

- 可直接使用。
- 仍保留正常来源边界。

### 6.3 YELLOW

任一条件成立：

- `review_by < today`
- high volatility 但缺少有效 `verified_at`、`review_by` 或可判断的局部新鲜度信息
- 页面时间很旧且当前问题明确询问“现在/当前/最新”
- 新来源可能影响该页，但尚未完成重审
- 页面包含当前版本事实，但用户环境版本未知
- 来源仍存在，但适用范围可能变化

Agent 行为：

1. Wiki 只作为候选背景和检索起点。
2. 优先检查 raw、官方文档、live tool 或当前项目事实。
3. 验证后回答。
4. 当前任务有 Wiki 写入授权时，生成最小知识补丁。
5. 没有写入授权时，只报告“该知识已到期/需要验证”，不静默修改。

### 6.4 RED

任一条件成立：

- 页面被一个对当前 scope/version 仍然生效的 `supersedes` 关系替代；替代页自身是否新鲜不影响旧页保持 RED
- 存在 unresolved `conflicts_with` 且当前上下文无法消解
- 已知来源明确撤回或否定旧结论
- 页面适用版本与当前版本不兼容
- high volatility 内容明显超出有效窗口并且无法验证
- 页面 status 已 closed 且内容本身是历史结论，不应继续当成 current rule

Agent 行为：

- 禁止把该页作为当前确定性事实。
- 可以作为历史背景引用。
- 必须寻找替代页、权威来源或 live evidence。
- 无法解决时 fail closed：明确“不足以确定”，而不是由模型自行调和。

## 7. Relations 升级为 Retrieval Hard Constraints

当前支持：

- `depends_on`
- `refines`
- `conflicts_with`
- `supersedes`
- `related`

v2 中：

### `supersedes`

不再只是图谱描述，而是检索解析规则。

当检索命中旧页 B 时，必须同时检查指向 B 的关系入边。若页面 A 声明了一个对当前 scope/version 生效的关系：

`A supersedes B`

即使语义检索没有直接命中 A，或 B 的语义相似度更高，也必须把 B 判为 RED。A 再独立通过 Freshness Gate；若 A 已到期，则 A 为 YELLOW、B 仍为 RED，并寻找 live evidence，不能恢复使用 B。

旧页 B 只作为历史理由和变更背景。

### `conflicts_with`

不允许 LLM 在没有证据的情况下自行综合成一个“看起来合理”的答案。

冲突解析顺序：

1. scope
2. applicable version
3. effective date
4. source authority
5. supersession
6. live/current evidence

仍无法解决：进入 unresolved，答案明确表达冲突。

`conflicts_with` 在语义上按双向约束处理：无论关系写在哪一页，检索任一端时都必须检查出边和入边。

凡会影响当前事实结论的 CONFLICT，必须写入 `conflicts_with`；正文说明只能补充范围和理由，不能替代机器可读关系。

### 关系发现规则

Freshness Gate 不能只读取当前候选页自己的 Relations。分类前必须：

1. 读取候选页的关系出边。
2. 在正式页面中查找指向候选页的 `supersedes`、`conflicts_with` 和 `depends_on` 入边。
3. 将发现的替代页或冲突页加入候选集，即使它们没有被语义搜索直接命中。

第一阶段可直接扫描 Markdown；Phase 3 再用同一个只读查询脚本统一来源和关系反查，不引入图数据库。

### `depends_on`

如果当前结论依赖页面已进入 RED，则当前页面不能自动保持 GREEN，应至少降级为 YELLOW，除非能证明依赖部分与问题无关。

## 8. Source / Relation Reverse Lookup

现有 `sources` 解决：

`formal page -> source`

v2 增加按需反查：

`source -> dependent formal pages`

### 8.1 目标

当已引用来源发生变化时，确定性得到直接依赖页；当新来源首次进入时，得到带匹配依据的候选页，而不是依赖 Agent 记忆或把启发式结果伪装成确定性关系。

### 8.2 实现

新增只读查询脚本候选：

```text
_meta/scripts/wiki_reverse_lookup.py
```

输入：所有正式页面 frontmatter `sources` 与 `## Relations`。

默认按需扫描并向 stdout 输出稳定排序的 JSON，不持久化派生文件。

示例：

```json
{
  "raw/articles/claude-code-2026-08.md": [
    "concepts/claude-code-practical-workflow-tips.md",
    "concepts/ai-coding-agent-workflow-types.md"
  ]
}
```

正式页面始终是 canonical truth。只有实际扫描延迟成为问题时，才另行评估持久化 generated JSON；不得预先增加缓存一致性检查。

### 8.3 Review Candidate

两类触发严格分开：

#### 已引用来源发生变化

1. 用精确 source path 查询 reverse dependency。
2. 确定性列出所有直接引用它的 formal pages。
3. 把这些页面标记为本次任务的 review candidates。

#### 新来源首次进入

新 raw 尚无反向边，不能宣称确定性定位。Agent 使用新来源中的产品名、实体名、别名和窄主题词搜索现有 formal pages，并为每个候选保留匹配依据。

结果只表示 candidate invalidation，不表示页面已失效；随后比较具体 claim，而不是整页重写。

第一阶段不要求自动建立永久 `needs-review` 字段。

## 9. Claim-level Freshness

页面级 freshness 只用于粗粒度路由。

当页面同时包含稳定知识和高波动事实时，使用最小 claim-level 标记。

### 推荐格式 A：简单 as-of

```markdown
Claude Code 当前支持 XXX。
_As of: 2026-09-09 · Source: [[raw-source]]_
```

简单 `as_of` 是信息性简写，只说明该句的核对时间和来源，不等同于机器字段 `verified_at`；没有局部 `verified_at` 与 `review_by` 时不能单独把高波动 claim 判为 GREEN。

### 推荐格式 B：高风险 volatile block

仅对真正会直接影响 Agent 操作的事实使用：

```markdown
> [!volatile]
> verified_at: 2026-09-09
> review_by: 2026-10-09
> source: docs:vendor-url
>
> 当前行为……
```

第一阶段不要求 health check 解析 volatile block；先作为写作约定试运行。局部 block 只覆盖 block 内明确的 claim，不能刷新页面级 `verified_at`。

### 禁止

- 每段都加元数据。
- 给稳定原则加人为过期时间。
- 为追求覆盖率把页面拆成大量原子 claim。

## 10. Ingestion v2

当前 ingest：

`raw -> extract -> formal -> index/log -> health check`

升级为：

```text
raw ingest
   ↓
extract product / entity / aliases / narrow topic terms
   ↓
search existing formal knowledge
   ↓
check reverse dependents
   ↓
classify:
   NEW | CONFIRM | UPDATE | CONFLICT | SUPERSEDE
   ↓
minimal knowledge patch
   ↓
Freshness metadata update where justified
   ↓
health check
```

### NEW

新知识，与已有结论无冲突。

### CONFIRM

新来源继续支持旧结论。

行为：必要时刷新 `verified_at/review_by`，不制造无意义正文 diff。

### UPDATE

旧知识仍大体成立，但局部事实发生变化。

行为：只更新相关段落。

### CONFLICT

新旧来源无法直接统一。

行为：保留双方；影响当前事实时必须增加 `conflicts_with`，正文补充冲突范围和理由，不自动选边。

### SUPERSEDE

存在明确的新规则/新版本替代旧规则。

行为：新页或当前页建立 `supersedes`；旧页保留历史，但检索默认不再使用旧结论。

## 11. Retrieval v2

现有原则：wiki first。

升级为：

> freshness-qualified wiki first

### 概念/架构问题

```text
wiki search
→ Freshness Gate
→ stable concepts
→ external only when current applicability matters
```

### 配置/排障/操作问题

```text
wiki
→ freshness + version match
→ skills/current project state
→ external/live docs when needed
```

### 当前事实 / 最新行为

```text
live/external authoritative source
→ wiki as historical/contextual knowledge
→ write-back if durable
```

### 历史问题

```text
time-scoped wiki/raw/session
→ do not prefer newest source automatically
```

## 12. Health Check v2

第一阶段只新增确定性、低误报规则。

### P1 候选

- `volatility` 非 `low|medium|high`
- `verified_at` 不是 `YYYY-MM-DD`
- `verified_at > today`（未来日期不能代表已完成验证）
- high volatility 页面存在 `review_by` 但日期格式非法

### P2 候选

- high volatility 页面有 `verified_at` 但没有 `review_by`
- `review_by` 已过期
- `verified_at > updated`（元数据逻辑异常）

Relations 目标不存在继续由现有 `broken_wikilink` P0 处理，不新增重复或降级的 P2 报告。

暂不增加：

- 根据固定天数自动判 stale
- 全库 freshness score
- LLM semantic truth check

原因：这些不能被 deterministic validator 可靠判断。

## 13. Agent 行为契约

任何消费 Wiki 的 Agent 应遵守：

1. `stable` 不等于 current truth。
2. `updated` 不等于 verified。
3. 当前问题出现“最新/当前/现在/当前版本”时，主动提高 freshness 要求。
4. high volatility 缺少有效验证信息或已经到期时，不得直接作为当前事实。
5. `supersedes` 优先于相似度排名。
6. unresolved conflict 必须 fail closed。
7. 新来源只能形成 candidate invalidation，不能直接自动覆盖 canonical knowledge。
8. 实际验证后才允许刷新 `verified_at`。
9. 修改知识时优先最小局部 patch，不整页重写。
10. 没有写入授权时，只报告 stale/conflict，不修改 Wiki。

## 14. 实施阶段

### Phase 0 — 基线确认

目标：不修改行为，只确认设计不会破坏现有 Schema。

任务：

- [x] 审查本方案。
- [x] 明确 `volatility` / `verified_at` 为 optional。
- [x] 选 5–10 个高波动页面做样本。
- [x] 记录当前 retrieval 行为作为 baseline。

验收：

- 不要求历史迁移。
- 不新增 runtime dependency。

### Phase 1 — Schema + Writing Rules

任务：

- [x] 更新 `SCHEMA.md`，增加 `volatility` 与 `verified_at` 可选字段。
- [x] 更新 `hermes-wiki-page-writing-standards.md`。
- [x] 扩大 `review_by` 的适用定义：凡外部变化可能导致 Agent 错误行动的知识均可使用。
- [x] 更新现有 `_meta/page-template.md`；不为此新增 page generator。
- [x] 增加 health-check 字段格式验证。
- [x] 增加对应 regression tests。

验收：

- 旧页面全部继续通过。
- 新字段非法值能被确定性检测。
- optional 字段缺失不会导致历史页面失败。

### Phase 2 — Retrieval Freshness Gate

任务：

- [x] 更新 `hermes-retrieval-priority-and-answer-path.md`。
- [x] 在 `operations/agent-shared-wiki-index.md` 写入必须执行 Freshness Gate 和关系入边检查的最小入口规则，并链接 canonical 检索契约。
- [x] 将 “wiki first” 明确修改为 “freshness-qualified wiki first”。
- [x] 定义 GREEN/YELLOW/RED 运行时判断。
- [x] 将 `supersedes`、`conflicts_with` 升级为 retrieval hard constraints。
- [x] 增加至少 8 个 behavior cases。

最低测试集：

- [x] stable + low volatility -> GREEN
- [x] high volatility + valid verified_at + valid review_by -> GREEN
- [x] high volatility + future review_by but no verified_at -> YELLOW
- [x] high volatility + future verified_at -> YELLOW，并触发 P1
- [x] volatile block with verified_at + valid review_by + source -> only that claim GREEN
- [x] 局部 claim 复核后，同页其他易变 claim 仍为 YELLOW
- [x] expired review_by -> YELLOW
- [x] current question + old high-volatility page -> YELLOW
- [x] legacy page without volatility + current external fact -> YELLOW
- [x] legacy page without volatility + stable method -> GREEN
- [x] 只命中旧页但存在 inbound supersedes -> RED，并发现替代页
- [x] A supersedes B 且 A 已到期 -> A YELLOW、B RED，并寻找 live evidence
- [x] conflict 只声明在另一页 -> RED/fail closed
- [x] historical question uses old time-scoped source correctly
- [x] method-only section of old page不被无意义 freshness gate 阻塞

验收：

- Agent 不再把 `status: stable` 等价为“当前已验证”。
- 最新事实问题不会仅因为 Wiki 有结果就绕过 live verification。
- 四个既有 Agent 入口仍指向共享索引；用 fresh session 执行上述代表性 probe，并保留命令/结果作为验收证据。若无法取得某一端证据，只能声明该端尚未验证，不能宣称全体生效。

### Phase 3 — On-demand Reverse Lookup

任务：

- [x] 实现 `_meta/scripts/wiki_reverse_lookup.py`，统一支持精确 source 反查和 Relations 入边反查。
- [x] 输出稳定排序 JSON，不生成持久化索引文件。
- [x] 增加 source 与 relation lookup 的最小 regression tests。
- [x] ingest workflow 接入精确 source 与 Relations 反查；新来源继续走带依据的窄词检索。

验收：

- 给定任意已被引用的 `raw/...` source，可以确定性列出所有直接引用它的 formal pages。
- 给定任意页面，可以确定性列出指向它的 `supersedes`、`conflicts_with` 和 `depends_on` 入边。

### Phase 4 — Ingestion Classification

任务：

- [x] 更新 `wiki-ingestion-workflow.md`。
- [x] ingest 时输出 `NEW/CONFIRM/UPDATE/CONFLICT/SUPERSEDE`。
- [x] CONFIRM 只刷新真实验证过的 metadata。
- [x] UPDATE 使用最小 patch。
- [x] CONFLICT 不自动统一。
- [x] SUPERSEDE 建立明确 relation。

验收：

同一主题的新材料进入后，即使它尚未出现在任何正式页的 `sources` 中，Agent 也能通过产品名、实体名、别名和窄主题词列出 review candidates，逐项记录匹配依据，并说明为什么需要/不需要修改；不得把候选集描述成确定性依赖集。

最小 fixture 固定包含：

- 一个未被任何正式页 `sources` 引用的新 raw source。
- 一个应由产品名、实体名、别名或窄主题词命中的正式页。
- 一个包含宽泛相关词但不应命中的干扰页。

测试必须记录每个命中的字段/词，排除干扰页，并把结果标记为 `heuristic candidate` 而不是 `exact dependent`。

### Phase 5 — Claim-level Pilot

仅选择 3–5 个混合型页面试点。

候选：

- Claude/Codex 当前行为
- Hermes 当前 runtime/tool 行为
- Agent provider/tool capability 页面

任务：

- [x] 使用 `_As of..._` 简单标记。
- [x] 必要时使用 `[!volatile]` block。
- [x] 观察 Agent 是否更准确定位待验证段落。
- [x] 不做全库迁移。

验收：

同一页面的稳定方法论和易变事实可以拥有不同的新鲜度判断。

## 15. 成功指标

第一阶段不建立复杂 freshness score，只观察以下实际结果：

### 正向指标

- Agent 在当前事实问题中主动验证到期知识。
- 已引用来源变化后可以确定性找到 dependent pages；新来源进入后可以找到带匹配依据的 review candidates。
- superseded 页面不再被错误优先检索。
- unresolved conflict 不再被模型静默调和。
- 真实验证后 metadata 才更新。
- Wiki 更新以局部 patch 为主。

### 失败信号

出现任一项说明方案需要回调：

- Agent 因 freshness gate 对稳定知识频繁重复联网。
- 大量页面被机械添加 `review_by`。
- 每次 ingest 都触发大规模无意义页面更新。
- `volatility` 成为主观评分游戏。
- claim-level metadata 比正文更复杂。
- 按需反查结果被误当 canonical knowledge。
- 为 freshness 建立大量新的常驻 Agent/cron/observer。

## 16. 默认决策表

| 情况 | Freshness | Agent 行为 | 是否建议写回 |
|---|---|---|---|
| 稳定原理，无冲突 | GREEN | 直接使用 | 否 |
| 高波动，verified_at 有效且 review_by 未到期 | GREEN | 使用，保留来源边界 | 仅有新证据时 |
| 高波动，review_by 未到期但缺少 verified_at | YELLOW | 先验证 | 验证后可写回 |
| review_by 到期 | YELLOW | 先验证 | 验证后可写回 |
| 当前事实但页面无 freshness metadata | YELLOW | live/官方来源验证 | 视长期价值 |
| 页面被 supersede | RED | 不用于当前事实 | 必要时补关系 |
| unresolved conflict | RED | fail closed | 只在证据足够时修正 |
| 新来源确认旧结论 | GREEN | 继续使用 | 可刷新验证日期 |
| 新来源局部改变旧结论 | YELLOW→GREEN | 最小 patch 后使用 | 是 |
| 历史问题查询旧规则 | 时间范围内 GREEN | 使用历史版本 | 否 |

## 17. 最小可行版本（MVP）

如果只做最少工作，必须完成以下五项：

1. `SCHEMA.md` 增加 optional `volatility`、`verified_at`。
2. Retrieval contract 改为 `freshness-qualified wiki first`。
3. 到期 `review_by` 在 Agent 检索中触发 verification，而不只是 health-check P2。
4. `supersedes` / unresolved `conflicts_with` 成为 retrieval hard constraints。
5. 建立按需的 `source -> dependent pages` 与关系入边反查。

在这五项完成前，不建议继续增加更复杂的 freshness 状态、confidence score 或知识图谱基础设施。

## 18. 最终架构

```text
External / Project / Live Sources
              │
              ▼
             RAW
              │
          Ingestion v2
              │
      reverse dependency
              │
              ▼
         Formal Wiki
              │
          Retrieval
              │
              ▼
       Freshness Gate
   ┌──────────┼──────────┐
   ▼          ▼          ▼
 GREEN      YELLOW       RED
   │          │          │
 answer     verify    reject current
              │          │
              └────┬─────┘
                   ▼
            Knowledge Patch
                   │
                   ▼
              Formal Wiki
```

## 19. 结论

Hermes Wiki v2 的目标不是让所有知识永远“最新”，这是不可实现也不经济的。

目标是做到：

- 稳定知识长期低维护。
- 易变知识有明确时效语义。
- Agent 在使用知识前能够判断其当前资格。
- 来源变化能够定位受影响知识。
- 旧知识能够被替代而不丢失历史。
- 冲突不能被模型静默抹平。
- 更新发生在真正需要的局部，而不是全库重写。

一句话定义：

> Hermes Wiki 从“经过治理的长期知识库”升级为“具备时效判断、失效传播和可验证更新闭环的 Agent Knowledge System”。

## Relations

- refines: [[hermes-knowledge-freshness-and-claim-evidence]]
- refines: [[hermes-retrieval-priority-and-answer-path]]
- refines: [[wiki-ingestion-workflow]]
- depends_on: [[hermes-knowledge-architecture]]
- depends_on: [[hermes-wiki-page-writing-standards]]

## Related

- [[hermes-knowledge-architecture]]
- [[hermes-knowledge-freshness-and-claim-evidence]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[hermes-wiki-page-writing-standards]]
- [[wiki-ingestion-workflow]]

## 20. 实施与验收证据（2026-09-09）

状态：已收口。实现与独立 AGY 复审完成（PASS、无实现阻断项）；用户于 2026-09-09 明确同意 Claude 行为验收不计未完成，并授权 Git 提交和推送。Claude 记为用户豁免，不宣称实测通过；其余历史证据保持原文。

### 基线与五页样本

基线 `48dc01b`，初始 `git status --short` 为空。修改前执行 `python3 -m unittest discover -s _meta/scripts -p 'test_*.py'`：13 tests OK；`python3 _meta/scripts/wiki_health_check.py --format markdown`：PASS，P0/P1/P2=0/0/0，119 正式页、163 raw、116 index links。

五页样本（均读取基线正文；后两页通过 `git show 48dc01b:<path>` 回看，不修改）：

| concepts/ 下页面 | 基线检索证据与缺口 | 本次处置 |
|---|---|---|
| claude-code-practical-workflow-tips.md | stable，review_by=2026-11-11，无 verified_at；方法与当前命令混合 | 局部目录访问 claim 试点 |
| codex-agent-workflow-layering.md | 同上；来源可命中工作流分层内容，无法区分核验范围 | 局部指令发现规则试点 |
| hermes-model-specific-harness-profiles.md | 同上；旧 default/model/Gateway 快照写成当前状态 | 历史化旧快照，局部 CLI/路径计算试点 |
| hermes-agent-workflow-layering-and-adoption-order.md | stable，无 freshness 字段；稳定分层与当前工具 owner 混合 | 保持历史页；读取时按 claim 范围判断 |
| hermes-layer-routing-decision-checklist.md | stable，无 freshness 字段；方法与外部 memory/cron/MCP 定义混合 | 保持历史页；实时行为独立核验 |

这是文件/检索契约的静态基线，不是修改前四端 fresh-session 行为实测。原契约只要求 wiki first，入口已有实时验证边界，却没有关系入边硬约束；健康检查只处理 review_by 格式与到期。不能据此声称旧 Agent 实际犯过错误。

### 实现与确定性验证

- 可选元数据、Schema、写作、健康规则和模板已同步；模板不预填 verified_at/review_by。保留任意页面 review_by 校验。修正共享 frontmatter 读取的跨行吞值与多行 sources 只读首项问题。
- 反查脚本支持互斥 source/page；精确来源返回路径数组，页面查询返回 declared_by/relation/target 数组；去重排序、不持久化索引。错误返回 stderr JSON、exit 2，无成功 stdout；代码示例（反引号、波浪围栏、行内/缩进）排除。
- 22 项 unittest 通过；其中元数据表驱动含 15 个缺省/非法/未来/边界情形，反查覆盖多引用、block list、重复边、关系类型、代码例子、无匹配、歧义、无效 UTF-8、非法 sources、不可读目录和 CLI 错误。
- 实库 source 查询 `raw/articles/openai-codex-best-practices-2026-04-17.md` 返回 codex-agent-workflow-layering、hermes-agent-workflow-layering-and-adoption-order、hermes-layer-routing-decision-checklist 三页。检索契约页面的入边查询返回知识架构、摄取流程和共享入口的声明。
- Freshness Gate 通过共享入口和 Agent 契约生效，Python 不实现语义裁决。没有新增依赖、全局配置、memory/skills/runtime/MCP 改动或批量历史页迁移。

### 可复现行为 fixture 与命令

测试为虚构 Aster CLI；today 固定 2026-09-09。临时 Vault `/tmp/wiki-freshness-v2-fixture`，正式页均在 concepts/；共同 frontmatter 为 title=文件 stem、created=2026-01-01、updated=2026-09-09、type=concept、tags=[tool]、sources=[docs:aster-v2]、status=stable。默认正文为 `Aster CLI v2 buffer limit is 16.`。下表列出差异；不把虚构来源写进真实 raw。

| fixture | 额外元数据/正文 |
|---|---|
| stable | volatility=low；正文 Method: compare output with acceptance criteria. |
| valid | high；verified_at=09-01；review_by=10-01（均 2026 年） |
| missing | high；review_by=10-01；无 verified_at |
| future | high；verified_at=09-10；review_by=10-01 |
| mixed | high；稳定 Method 同 stable；volatile block 内 verified_at=09-01、review_by=10-01、source=docs:aster-v2、v2 limit=16；block 外 Other claim: Aster CLI v2 supports teleport. |
| expired | high；verified_at=08-01；review_by=09-08 |
| old | high；verified_at=01-01；review_by=02-01；只有默认 API claim，无稳定方法段 |
| legacy | 无 freshness 元数据 |
| legacy-method | 无 freshness 元数据，正文为 stable 的 Method |
| b | high；verified_at=09-01；review_by=10-01；正文 v1 limit=8，适用至 v2 于 08-01 生效 |
| a | high；verified_at=08-01；review_by=09-08；正文 v2 limit=16，替代从 08-01 起对 v2 生效、不替代 v1 历史；Relations: supersedes 指向 b |
| conflict-target | 默认正文 |
| conflict-declarer | v2 limit=32，同 scope/date/authority，明确 unresolved；Relations: conflicts_with 指向 conflict-target |
| candidate | aliases=[Aster CLI]；sources=[docs:aster-v1]；正文仅 Aster CLI buffer-limit configuration. |
| distractor | sources=[docs:general]；正文仅 Agent AI workflow and general productivity. |
| raw/articles/new-aster.md | 产品 Aster CLI；窄词 buffer-limit；v2 buffer-limit is 16。没有正式页 sources 引用它 |

命令：`python3 -B /home/lin/wiki/_meta/scripts/wiki_reverse_lookup.py --root /tmp/wiki-freshness-v2-fixture --page concepts/b.md`（a/supersedes/b）；对 conflict-target 查询得到 conflict-declarer/conflicts_with；`--source raw/articles/new-aster.md` 输出 `[]`。`rg -n -i 'aster cli|buffer-limit' .../concepts/candidate.md .../concepts/distractor.md` 命中 candidate 的 aliases（第 9 行）和正文（第 12 行），不命中 distractor。

新材料候选判定：candidate 是 **heuristic candidate**，局部 v2 limit=16 为 **NEW**（可并入原 owner；旧正文没有数值 claim，不能仅凭 docs:aster-v1 推断 UPDATE）。distractor 缺窄词匹配而排除，不强行分入五分类。Codex 实测给出此结果；AGY 首轮误判 UPDATE，已收紧契约并重测，AGY/Codex/Hermes 均判 NEW。此 fixture 只验证 NEW 与排除，五分类规则不等于五类都已有端到端样例。

调用均在 /home/lin/wiki，未使用 resume/continue：

- Claude 2.1.259：`claude -p --no-session-persistence --permission-mode plan --tools Read,Grep,Glob,Bash --allowedTools 'Read,Grep,Glob,Bash(python3 _meta/scripts/wiki_reverse_lookup.py *)' --output-format json < /tmp/wiki-freshness-v2-probe.txt`。
- Codex 0.153.4：`codex exec --ephemeral --sandbox read-only --json - < /tmp/wiki-freshness-v2-probe.txt`。
- AGY：Python subprocess 参数列表调用 `agy --mode plan --sandbox --print-timeout 180s --log-file /tmp/wiki-freshness-agy-cli.log --output-format json -p <prompt字符串>`；AGY 的 -p 必须带参数，不能仅从 stdin 提供。
- Hermes v0.21.1：`hermes chat --query-file /tmp/wiki-freshness-v2-probe.txt --oneshot --max-turns 12 --run-budget 150 -t terminal`。

完整 probe 要求：按既有全局入口读取共享入口与 canonical 检索/摄取契约，不读取实施计划预期；用现有工具反查 fixture；依次回答下表 15 项（资格、scope、live 要求、依据），判断固定新来源/候选/干扰页，再指出三真实试点页的稳定原则、局部核验 claim 和待验证部分。固定日期 09-09，只读不联网，不修改外部状态。初轮“不能联网虚构产品”混入了无法验证条件；重测将第 8 项明确为“尚未尝试核验，且无证据表明权威来源不可取得”的初判，避免把 YELLOW 与验证失败后的 RED 混淆。

### 15 项实际行为结果

下列 Codex/AGY 初轮均实际读取共享入口、canonical 文件并运行反查。Codex fresh session 的完整响应及工具 JSONL 在本次 /tmp 证据中；AGY conversation `5ad69af8-d370-43a8-8612-fc68908b17d9` 返回完整表格。结果摘要在此长期保留，临时日志不作为唯一证据。

| # | 输入/范围 | 预期 | 首轮 Codex / AGY |
|---|---|---|---|
| 1 | stable 方法 | GREEN | GREEN / GREEN |
| 2 | valid v2 claim | GREEN，当前事实仍 live | GREEN + live / 同 |
| 3 | missing | YELLOW | YELLOW / YELLOW |
| 4 | future | YELLOW + P1 | YELLOW + future_verified_at P1 / 同 |
| 5 | mixed block | 仅该 claim GREEN | 局部 GREEN / 同 |
| 6 | mixed teleport | YELLOW | YELLOW / 同 |
| 7 | expired | YELLOW | YELLOW / 同 |
| 8 | old 当前适用性初判 | YELLOW，实际无法核验才 RED | 首轮均 RED（提示混入无法验证条件）；收紧后 AGY/Codex/Hermes 均 YELLOW |
| 9 | legacy 当前外部事实 | YELLOW | YELLOW / 同 |
| 10 | legacy-method | GREEN | GREEN / 同 |
| 11 | 只命中 b 问 v2 | RED，发现 a | RED，反查发现 a / 同 |
| 12 | a 到期 | a YELLOW、b RED，live | 符合 / 符合 |
| 13 | 只命中 conflict-target | RED/fail closed | 入边冲突 RED / 同 |
| 14 | 07-01 的 v1 历史 b | 时间范围 GREEN | GREEN / 同 |
| 15 | mixed 方法 | GREEN | GREEN；Codex 另指出 old 实际无方法段，不虚构内容 / GREEN |

### 试点核验来源与范围

- Claude：2026-09-09 实际打开官方 memory 文档，核对 additional directories 小节的 --add-dir 与指令加载开关；本机 --help 辅助确认参数存在。[官方文档](https://code.claude.com/docs/en/memory)。不验证 /teleport、浏览器、schedule 或远程能力。
- Codex：实际打开官方 AGENTS 文档（developers.openai.com 跳转至 learn.chatgpt.com），核对 global/project/discovery/merge 顺序。[官方文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。不宣称本机所有运行端已验证。
- Hermes：实际读取 `/home/lin/.hermes/hermes-agent/hermes_cli/profiles.py` 的 `_get_profiles_root` 与 `_get_default_hermes_home`，执行 `hermes --version`、`hermes profile --help`。核验仅覆盖命名 profile 路径计算与 CLI 子命令，不读取或刷新当前模型/provider/Gateway 状态。
- 三页只加局部 verified_at=2026-09-09、review_by=2026-10-09 和具体 source；保留页面 review_by=2026-11-11，不增加页面级 verified_at。Codex/AGY 初轮均正确定位局部 claim、稳定方法及仍待验证内容，未提升整页。

### 四端与复审状态

- 全局入口只读核对：Claude `~/.claude/CLAUDE.md`、Codex `~/.codex/AGENTS.md`、AGY `~/.gemini/GEMINI.md`、Hermes `~/.hermes/memories/MEMORY.md` 均包含共享入口路径；未修改。
- Claude 用户豁免（2026-09-09，不计未完成）：此前返回 `Failed to authenticate: OAuth session expired and could not be refreshed`，模型 usage 为 0。没有行为执行证据，不进行凭证变更。
- Codex 首次受只读宿主初始化限制；获准放行 CLI 初始化后，子会话仍为 read-only，完成上述 15 项、候选及三页范围判断。第 8 项收紧后重测通过，代表性行为验收通过。
- AGY 首次被 socket 沙箱限制；放行本地通信后完成初轮。第 8 项和候选 NEW 分类重测通过，代表性行为验收通过。
- Hermes 首次受会话目录只读限制；正常初始化重跑已读当前工作区契约、执行 fixture 反查，但在预算内未返回最终判断，首轮不计通过；缩为代表性案例的新会话返回完整判断，入口/缺验证/替代及局部验证全部通过（未声称 Hermes 完成全部 15 项）。
- AGY 独立实施复审首轮只有等待文字，不计通过；续审发现 log 标题插入错误，修复后复审 **PASS，Blocking None**。prompt/result 见 [[2026-09-09-knowledge-freshness-v2-agy-review-prompt]]、[[2026-09-09-knowledge-freshness-v2-agy-review]]。已记录一次 reviewer 误运行 manifest writer 的边界偏差，确认未改变任何 raw/manifest 字节；最终复审只执行只读比较。

重测命令与结果：AGY 同参数 fresh session、Codex 同参数 fresh session、Hermes `--max-turns 20 --run-budget 210`，均改读 `/tmp/wiki-freshness-v2-focused.txt`。此 prompt 明确只读且不读取计划，要求加载既有入口并实际读取 old/missing/mixed/b/a/candidate/distractor、新 raw；依次判断未尝试核验的 old、missing、block/teleport、反查 b 的 a/b 资格、精确反查为空后的 NEW/干扰页分类。三端均返回 YELLOW、YELLOW、GREEN/YELLOW、a YELLOW/b RED、heuristic candidate NEW/干扰排除，未将局部提升整页。

会话标识：Codex 初轮 `01a084fc-da5c-7281-a7f2-303ffe0e6969`，重测 `01a08500-85e1-7fa3-8d90-564f845438c7`；AGY 重测 `f308be16-f910-4fec-9746-15aa0c1cf8a0`；Hermes 重测 `20260909_151005_4dcefa`（16 tool calls，最终完整回答）。Claude 初轮 `258449eb-75e5-4f23-ab61-8c288071faf4` 只有认证失败。15 项行为已由 Codex/AGY 初轮加边界重测覆盖；Claude 后经用户明确豁免，不计未完成；不宣称四端全部实测通过。

- [x] 元数据与反查回归、检索/摄取契约、三个局部 claim 试点。
- [x] 15 项行为案例及固定新来源候选检查（初轮问题与纠正如上）。
- [x] Codex、AGY、Hermes fresh-session 代表性行为。
- [x] Claude fresh-session 验收项收口（用户豁免；认证失败记录保留，不等于实测通过）。
- [x] AGY 独立实施复审取得明确无阻断裁决（PASS）。
- [x] 整体 Phase 0–5 按用户确认的验收范围关闭。

最终验证：22 tests OK；Wiki health check P0/P1/P2=0/0/0；`git diff --check` 无输出；`git diff -- raw/ _meta/raw-source-hashes.json` 为空。共享入口 5055 bytes，未超过 8 KiB。实现范围已完成；Claude 验收由用户豁免，计划关闭，按用户授权提交并推送。
