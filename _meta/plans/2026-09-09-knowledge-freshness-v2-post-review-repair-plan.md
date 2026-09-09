---
title: Knowledge Freshness v2 Post-Review Repair Plan
created: 2026-09-09
updated: 2026-09-09
type: plan
tags: [hermes, knowledge-base, governance, verification, workflow]
sources:
  - _meta/plans/2026-09-09-knowledge-freshness-architecture-v2.md
  - concepts/hermes-retrieval-priority-and-answer-path.md
  - concepts/wiki-ingestion-workflow.md
  - concepts/hermes-wiki-page-writing-standards.md
  - concepts/hermes-wiki-lint-and-health-check-standards.md
status: closed
---

# Knowledge Freshness v2 Post-Review Repair Plan

## 1. Summary

本计划用于修复 Knowledge Freshness v2 落地复审后确认的两个契约缺口。

本次不是 v3 架构升级，也不重新设计 Freshness Gate。目标是在不增加新的数据库、状态机、常驻服务、自动重写 Agent 或复杂 claim parser 的前提下，把现有 v2 中两个可能导致长期漂移的问题收口：

1. **局部 `[!volatile]` claim 的 `source:` 与页面级 `sources` 之间缺少明确一致性约束。**
   - 当前 reverse dependency 只以页面级 `sources` 为 canonical provenance。
   - 如果未来局部 claim 引用了一个未同步写入页面级 `sources` 的新来源，`wiki_reverse_lookup.py --source` 可能返回空结果，从而漏掉真实依赖页。
   - 当前三个试点页没有触发该问题，但规范没有阻止未来出现。

2. **`review_by` 校验范围存在文档与实现不一致。**
   - `SCHEMA.md`、页面写作规范与 lint/health 规范当前写成“任意页面非法 `review_by` 为 P1”。
   - 实际 `wiki_health_check.py` 只在 formal page 范围内执行 freshness metadata 校验。
   - runbook 的描述反而与代码一致，写的是 formal page。
   - 这属于 contract drift：人和 Agent 可能根据不同文件得到不同规则。

本计划的原则是：**只修复已经确认的契约缺口，不扩展 freshness 架构。**

---

## 2. 为什么现在要修

Knowledge Freshness v2 已经建立了下面这条主链路：

```text
source/raw
    ↓
formal wiki
    ↓
retrieval
    ↓
Freshness Gate
    ↓
GREEN / YELLOW / RED
    ↓
verify / use / reject
```

当前系统已经可以：

- 区分 `status` 与 freshness；
- 使用 `volatility`、`verified_at`、`review_by`；
- 检查 `supersedes` / `conflicts_with`；
- 用 `wiki_reverse_lookup.py` 做 source → dependent pages 与关系入边反查；
- 对 mixed page 使用局部 `[!volatile]` claim；
- 保持 Markdown canonical，不建立第二套持久化索引。

因此现在的主要风险已经不是“缺少 freshness 机制”，而是**现有机制之间是否保持同一个契约**。

### 2.1 来源漏挂导致失效传播中断

假设页面：

```yaml
sources:
  - docs:old-source
```

正文后来增加：

```markdown
> [!volatile]
> verified_at: 2026-09-09
> review_by: 2026-10-09
> source: docs:new-source
>
> 当前行为……
```

如果 `docs:new-source` 没有同步进入页面级 `sources`：

```bash
python3 _meta/scripts/wiki_reverse_lookup.py \
  --root /home/lin/wiki \
  --source docs:new-source
```

可能返回：

```json
[]
```

但页面实际上依赖这个来源。

这会直接破坏 Knowledge Freshness v2 中最重要的能力之一：

> 来源变化后，可以确定性找到受影响知识。

因此必须明确：

> **页面级 `sources` 是 reverse dependency 的 canonical provenance；局部 block 的 `source:` 只是 claim attribution，不能成为唯一来源记录。**

### 2.2 规则表述漂移导致 Agent 误判治理范围

如果一个 Agent 读 `SCHEMA.md`，会得到：

> 任意页面非法 `review_by` 为 P1。

如果另一个 Agent 根据 health check/runbook 执行，会得到：

> 只检查 formal page。

长期下去会产生两类不必要行为：

- Agent 误以为 `_meta/`、raw 或其他非 formal 页面也必须遵守同一 freshness metadata 规则；
- 后续维护者可能为了“修复”不存在的问题而扩大 validator 范围，制造新的治理负担。

因此需要把规则统一到当前真正的设计边界：

> **Freshness metadata 是 formal knowledge object 的规则；raw、_meta 和 core files 不默认承担同一 freshness 生命周期。**

---

## 3. 问题边界

### 3.1 本次必须修复

#### P1 — Claim source provenance invariant

必须明确并落实：

```text
volatile block source
        ⊆
page-level sources
```

含义：

- 每个 `[!volatile]` block 中的 `source:` 必须同时出现在所属页面 frontmatter 的 `sources`；
- 页面级 `sources` 继续承担：
  - canonical provenance；
  - source reverse lookup；
  - source → dependent page invalidation；
- block `source:` 只承担：
  - claim 级来源定位；
  - 说明该局部核验对应哪条证据。

如果 block source 已存在于页面级 `sources`，不重复写入。

#### P2 — review_by scope contract alignment

必须统一：

```text
“任意页面”
```

为：

```text
“正式知识页 / formal page”
```

以当前实现为准，不扩大 validator。

---

## 4. 明确不修的内容

以下内容不是本次缺陷，禁止顺手扩张。

### 4.1 不实现 Python Freshness Engine

Freshness Gate 继续是 Agent semantic contract。

不新增：

```text
freshness_engine.py
freshness_score
confidence_score
authority_score
```

原因：

- scope；
- version；
- effective date；
- source authority；
- historical applicability；
- live evidence；

这些属于语义裁决，不适合在当前阶段硬编码成规则引擎。

### 4.2 不让 reverse lookup 解析 claim block

`wiki_reverse_lookup.py --source` 继续只读取页面级 `sources`。

原因：

- 页面级 `sources` 已经是 canonical provenance；
- reverse lookup 保持简单、确定性、低维护；
- 如果 claim source 同步进入页面级 `sources`，无需产生第二套来源语义。

### 4.3 暂不增加 `[!volatile]` 静态 parser

第一阶段不让 health check 解析 `[!volatile]` block 中的日期和 source。

原因：

- 当前 claim-level block 数量仍少；
- 当前主要目标是建立正确写入契约；
- 过早解析 block 会增加 Markdown parser 复杂度；
- 真实发生漏判或 block 数量明显增加后，再考虑静态检查。

升级触发条件：

```text
volatile blocks >= 10
OR
出现一次真实漏判 / reverse dependency false negative
```

满足任一条件，再单独评估 claim-level validator。

### 4.4 不新增持久化 reverse index

继续保持：

```text
Markdown = canonical
reverse lookup = on-demand derived result
```

不新增：

```text
_meta/reverse-index.json
SQLite
vector DB
graph DB
```

### 4.5 不做全库 freshness 迁移

不批量添加：

```yaml
volatility:
verified_at:
review_by:
```

只处理实际 touched page。

---

## 5. 实施计划

## Phase 0 — Baseline

### 任务

执行前记录当前基线：

```bash
cd /home/lin/wiki

git status --short
git rev-parse HEAD

python3 -m unittest discover \
  -s _meta/scripts \
  -p 'test_*.py'

python3 _meta/scripts/wiki_health_check.py \
  --format markdown

git diff --check

git diff -- raw/ _meta/raw-source-hashes.json
```

同时枚举当前所有 claim-level source：

```bash
rg -n '^[[:space:]]*>[[:space:]]*source:' \
  concepts operations queries comparisons
```

搜索结果需区分真实 claim 与 fenced template；写作规范中的示例不作为 reverse dependency 验收对象。

### 验收

- worktree 状态被记录；
- 当前 tests 通过；
- health P0/P1/P2 基线被记录；
- raw 与 hash manifest 无非预期 diff；
- 当前 `[!volatile]` source 清单明确。

---

## Phase 1 — 建立 Claim Source Provenance Invariant

### 修改文件

至少修改：

```text
SCHEMA.md
concepts/hermes-wiki-page-writing-standards.md
concepts/wiki-ingestion-workflow.md
```

必要时同步：

```text
_meta/plans/2026-09-09-knowledge-freshness-architecture-v2.md
```

仅用于记录 closeout / follow-up，不重写原方案。

### 1.1 SCHEMA.md

在 claim-level freshness 规则中增加：

> 局部 `[!volatile]` block 的 `source:` 必须同时存在于该页面 frontmatter 的 `sources` 中。页面级 `sources` 是 canonical provenance，也是 source reverse lookup 和依赖失效传播的唯一确定性入口；block `source:` 仅用于标识该局部 claim 的具体证据，不得成为页面唯一来源记录。

同时明确：

```text
block source ⊆ page sources
```

### 1.2 hermes-wiki-page-writing-standards.md

在 `[!volatile]` 写作规范后增加：

1. 添加 block 前先检查页面级 `sources`；
2. block 使用的新来源若不在 `sources` 中，必须同步加入；
3. 不重复添加已有来源；
4. 一个 source 是否支撑整个页面仍由正文范围决定，加入页面级 `sources` 只表示该页面包含依赖于此 source 的 claim；
5. 不因一个局部 source 进入页面级 `sources` 就刷新整页 `verified_at`。

### 1.3 wiki-ingestion-workflow.md

在 NEW / CONFIRM / UPDATE 流程中增加写入规则：

当某个局部 claim 使用：

```markdown
> source: X
```

时：

```text
X ∈ page.frontmatter.sources
```

否则该次 ingest 不算闭环。

### 1.4 当前试点页检查

至少检查：

```text
concepts/claude-code-practical-workflow-tips.md
concepts/codex-agent-workflow-layering.md
concepts/hermes-model-specific-harness-profiles.md
```

对每个 `[!volatile]` block：

- 提取 `source:`；
- 确认同一个 source 已出现在 frontmatter `sources`；
- 已符合则不制造正文 diff。

### 验收

对每个当前 volatile block source `S`、所属页面 `P`：

```bash
python3 /home/lin/wiki/_meta/scripts/wiki_reverse_lookup.py \
  --root /home/lin/wiki \
  --source "$S"
```

输出必须包含：

```text
P
```

如果不包含，必须修正页面级 `sources`。

### 本阶段禁止

- 修改 `wiki_reverse_lookup.py`；
- 新增 claim block parser；
- 新增持久化索引；
- 修改 Freshness Gate GREEN/YELLOW/RED 语义。

---

## Phase 2 — 统一 review_by 校验范围

### 目标

让以下五处表达一致：

```text
SCHEMA.md
hermes-wiki-page-writing-standards.md
hermes-wiki-lint-and-health-check-standards.md
wiki_health_check.py
_meta/wiki-health-check-runbook.md
```

当前代码和 runbook 的真实边界是：

```text
formal page
```

因此文档向实现对齐，而不是扩大实现。

### 2.1 SCHEMA.md

将：

> 任意页面非法 `review_by` 为 P1

修改为：

> 正式知识页中出现的非法 `review_by` 为 P1。

同时建议使用英文/机器术语明确：

```text
formal page
```

避免“页面”被误解为 raw / _meta / core file。

### 2.2 hermes-wiki-page-writing-standards.md

做同样修改。

### 2.3 hermes-wiki-lint-and-health-check-standards.md

做同样修改。此规范页在原计划中漏列，但它属于同一份 freshness validator 契约，若不修正会保留规范漂移。

### 2.4 _meta/wiki-health-check-runbook.md

runbook 当前已经使用 formal page 口径。

只复核，不为形式制造 diff。

### 2.5 wiki_health_check.py

**默认不改代码。**

只有发现代码实际范围与 `is_formal_page()` 不一致时才修改。

当前已知设计就是：

```python
if is_formal_page(root, p):
```

所以本阶段应优先是 documentation alignment。

### 验收

全库搜索：

```bash
rg -n '任意页面.*review_by|any page.*review_by' \
  SCHEMA.md concepts _meta
```

不得再存在与 formal-page validator 冲突的规范性表述。

---

## Phase 3 — Deterministic Validation

执行：

```bash
cd /home/lin/wiki

python3 -m unittest discover \
  -s _meta/scripts \
  -p 'test_*.py'

python3 _meta/scripts/wiki_health_check.py \
  --format markdown

git diff --check

git diff -- raw/ _meta/raw-source-hashes.json
```

### Reverse dependency spot checks

至少验证三个当前 volatile source。

示例：

```bash
python3 /home/lin/wiki/_meta/scripts/wiki_reverse_lookup.py \
  --root /home/lin/wiki \
  --source docs:https://code.claude.com/docs/en/memory
```

预期包含：

```text
concepts/claude-code-practical-workflow-tips.md
```

```bash
python3 /home/lin/wiki/_meta/scripts/wiki_reverse_lookup.py \
  --root /home/lin/wiki \
  --source docs:https://learn.chatgpt.com/docs/agent-configuration/agents-md
```

预期包含：

```text
concepts/codex-agent-workflow-layering.md
```

Hermes 本地 source 同理验证。

### 验收

必须同时满足：

```text
unittest = PASS
health P0 = 0
health P1 = 0
git diff --check = clean
raw diff = empty
raw hash manifest diff = empty
```

P2：

- 不得由本次修改引入新的 P2；
- 原有时间驱动 P2 若未来出现，单独解释，不通过删除 `review_by` 消除。

---

## Phase 4 — Independent Read-Only Review

因为本次修改涉及：

```text
SCHEMA.md
governance contract
ingestion contract
```

符合现有 Wiki 的独立审查触发条件。

### 审查范围

只审查本次 diff，重点回答：

1. 是否正确建立：
   ```text
   volatile block source ⊆ page-level sources
   ```
2. 是否明确 page-level `sources` 是 reverse dependency canonical provenance；
3. 是否避免让 block source 变成第二套依赖系统；
4. 是否把 `review_by` 校验范围统一到 formal page；
5. 是否误扩大了 health check、Freshness Gate、runtime 或 active layers；
6. 是否修改了 raw；
7. 是否出现无意义历史页批量迁移。

### 禁止

Reviewer 必须只读：

- 不运行 `wiki_raw_hashes.py`；
- 不写 raw；
- 不修改 manifest；
- 不修改 global config / memory / skills / runtime / MCP / cron。

### 通过标准

Verdict：

```text
PASS
```

或至少：

```text
APPROVE_LANDING
```

且无 blocking findings。

---

## Phase 5 — Closeout

### 更新 log.md

仅记录 durable delta：

- 建立 claim source → page source provenance invariant；
- 统一 `review_by` formal-page scope；
- tests / health / reverse lookup 验证结果；
- 独立 review 结论；
- 明确没有新增 parser、数据库、runtime 或全库迁移。

### Plan status

全部验收完成后：

```yaml
status: closed
```

否则保持：

```yaml
status: draft
```

---

## 6. 验收清单

### P1 — Claim provenance

- [x] 每个真实 `[!volatile]` block 的 `source:` 都出现在所属页面 frontmatter `sources`。
- [x] `SCHEMA.md` 明确 page-level `sources` 是 canonical provenance。
- [x] 写作规范明确 block source 不能成为唯一 source。
- [x] ingestion workflow 明确新增 block source 时同步 page sources。
- [x] 当前三个试点页全部符合。
- [x] 每个当前真实 block source 用 `wiki_reverse_lookup.py --source` 都能找到所属页。

### P2 — review_by contract

- [x] `SCHEMA.md` 使用 formal page 口径。
- [x] `hermes-wiki-page-writing-standards.md` 使用 formal page 口径。
- [x] `hermes-wiki-lint-and-health-check-standards.md` 使用 formal page 口径。
- [x] runbook 与 code 口径一致。
- [x] 不扩大 validator 到 raw / _meta / core files。

### Regression

- [x] unittest 全通过。
- [x] health P0 = 0。
- [x] health P1 = 0。
- [x] 未新增意外 P2。
- [x] `git diff --check` clean。
- [x] raw 无 diff。
- [x] `_meta/raw-source-hashes.json` 无 diff。
- [x] 独立 read-only review `APPROVE_LANDING`，无 blocking findings。

---

## 7. 成功标准

本计划完成后必须能保证：

### 7.1 Source invalidation 不漏页

只要一个 claim 正式依赖来源 `S`：

```text
S
↓
page-level sources
↓
wiki_reverse_lookup
↓
dependent page
```

不会因为证据只写在 `[!volatile]` block 中而丢失 reverse dependency。

### 7.2 Freshness metadata scope 单一

所有规范性文档对 `review_by` 的校验范围都只有一个答案：

```text
formal knowledge page
```

### 7.3 不增加治理复杂度

完成修复后：

- 没有新增数据库；
- 没有新增 freshness service；
- 没有新增常驻 watcher；
- 没有新增 claim ID；
- 没有新增自动 rewrite；
- 没有全库 metadata 迁移；
- 没有把 semantic Freshness Gate 硬编码成 Python state machine。

---

## 8. 何时才进入下一阶段

本次修复后停止继续扩建。

只有出现下面任一真实信号，才开启新的 freshness 改造：

1. `[!volatile]` block 数量达到约 10 个以上；
2. 出现一次 claim source 没进入 page-level sources 导致 reverse lookup false negative；
3. Agent 实际漏掉过期 claim；
4. Agent 因 Freshness Gate 对稳定知识频繁重复验证；
5. 模型或共享入口升级后，GREEN/YELLOW/RED 行为出现明显漂移；
6. source reverse lookup 的全库扫描开始成为真实性能瓶颈。

在这些事件发生前：

> **优先使用现有系统，不继续建设新系统。**

---

## 9. Rollback

本次修改只应涉及规范文档、必要的 formal-page provenance 和 log。

如果独立 review 发现设计错误：

```bash
git revert <repair-commit>
```

即可完整回退。

不得通过：

- 删除 raw；
- 重写历史来源；
- 重建 hash manifest；
- 批量清除 freshness 字段；

来完成回滚。

---

## 10. 最终决策

本次修复的本质不是增加更多 freshness 功能，而是保证现有 v2 的两个关键不变量成立：

```text
Claim provenance 不得绕过 page-level canonical sources
```

以及：

```text
Freshness metadata validator 的治理范围必须只有一个定义
```

修完这两项以后，Knowledge Freshness v2 应进入真实使用期。

后续优化优先由真实失败驱动，而不是由架构完整性焦虑驱动。
