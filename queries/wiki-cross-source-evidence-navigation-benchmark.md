---
title: Wiki 跨源证据导航离线评测方案与拓扑基线
created: 2026-11-02
updated: 2026-11-06
type: query
tags: [agent, knowledge-base, evaluation, verification, architecture, workflow]
sources: [repository:_meta/catalog.json, concepts/hermes-knowledge-freshness-and-claim-evidence.md, concepts/production-agent-evaluation-baselines.md, concepts/production-ai-agent-evaluation-framework.md, raw/articles/langchain-agent-memory-openwiki-graphs-2026-10-28.md, raw/articles/langchain-self-correcting-memory-openwiki-2026-08-26.md]
status: stable
volatility: medium
verified_at: 2026-11-06
review_by: 2027-03-02
description: 保存本仓库 8 组双入口跨源证据导航（locate → expand）离线评测方案、黄金正式页与原始证据清单、一跳双向关系可达性拓扑基线（含召回率、精确率与一跳体积代理）及 Q1–Q8 章节级证据映射表，区分静态图重合度与重复问答引用一致性。
aliases: [cross-source-evidence-benchmark, evidence-navigation-benchmark, wiki-evidence-navigation-eval]
---

# Wiki 跨源证据导航离线评测方案与拓扑基线

## Summary

本页从 [[hermes-knowledge-freshness-and-claim-evidence]] 拆出并独立维护本仓库面向 `locate` → `expand` 两步证据导航的 **8 组双入口跨源检索评测方案（Q1–Q8）** 及其一跳双向关系拓扑基线。核心边界是严格区分两类指标：

1. **静态图拓扑可达性（已按 `_meta/catalog.json` 实测基线）**：从两个不同种子入口沿 `## Relations` 一跳双向展开后，完整可达正式页集合与 `raw/` 原始证据集合的重合度（Jaccard）及对候选黄金集的召回率，用于检测断链、孤岛与候选膨胀。
2. **模型问答引用一致性（Citation Consistency，当前状态：NOT_RUN）**：对同一跨源问题重复运行端到端模型问答流程时，实际引用的支撑段落集合的平均成对 Jaccard 相似度（参考 [[langchain-agent-memory-openwiki-graphs-2026-10-28]] 与 [[langchain-self-correcting-memory-openwiki-2026-08-26]]）。当前仓库尚未提交端到端多次问答的运行记录与逐题段落引用产物，因此模型层引用一致性保持 **NOT_RUN**，不将静态图拓扑重合度冒充为模型回答稳定性。

## 1. 评测口径与证据边界

- **黄金集独立性**：固定治理前后 commit 或内容哈希清单，提交机器可读的入口、黄金正式页和黄金原始来源集合；黄金集须独立复核，不按治理后遍历结果倒推。
- **遍历约束统一**：对照无类型关系展开与类型化展开时，统一跳数、边方向、来源提取范围、停止条件和候选预算；若分别测单向与双向遍历，逐项标明。多分支与冲突不能默认为全部适用；`A supersedes B` 必须沿入边从旧页 B 指向现行页 A（见 [[hermes-retrieval-priority-and-answer-path]]）。
- **完整可达集合重合度**：对每个入口保留完整可达正式页及来源集合，不先与黄金集求交再计算 Jaccard。**跨入口可达证据重合度**是图结构指标，不是模型回答的引用一致性；两端皆空时标记 N/A，并报告空结果数，不能记为完全一致。
- **召回率与精确率成对报告**：黄金证据召回率可用可达集合与黄金集的交集计算；另报精确率（或候选池规模），防止靠扩大全库候选虚增召回。空黄金集的指标标记 N/A。
- **真实问答引用一致性（Citation Consistency）**：必须对同一问题重复运行真实回答流程，保存实际引用的段落 ID，再计算完整引用集合的平均成对 Jaccard；同时独立评估引用正确性和答案正确性（见 [[production-ai-agent-evaluation-framework]] 与 [[production-agent-evaluation-baselines]]）。
- **上下文开销口径**：上下文开销应统计实际加载的全部跳数、正式页与原始证据；仅统计一跳页面字节数时只能称为一跳体积代理，不能推导完整问答的 Token、延迟或成本节省。

## 2. 8 组双入口候选问题（Q1–Q8）

| 编号与跨源问题域 | 双入口种子页（Seed A ↔ Seed B） | 拟用黄金正式页与原始证据 |
| --- | --- | --- |
| **Q1：上下文工程 × 状态契约 × 专用模型压缩** | [[agent-context-engineering]] ↔ [[agent-context-history-state-and-bounded-processing]] | 正式页：上述两页 + [[hermes-context-engineering-design-priorities]], [[hermes-memory-skills-wiki-boundaries]]<br>原始源：[[arxiv-2608-26263-skill-state]], [[langchain-scaledown-deep-agents-2026-10-13]], [[machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28]] |
| **Q2：知识新鲜度 × 两步证据导航 × 旧计划替代** | [[hermes-knowledge-freshness-and-claim-evidence]] ↔ [[hermes-wiki-knowledge-freshness-improvement-plan]] | 正式页：上述两页 + [[hermes-knowledge-architecture]], [[hermes-wiki-page-writing-standards]], [[hermes-memory-skills-wiki-boundaries]]<br>原始源：[[langchain-agent-memory-openwiki-graphs-2026-10-28]], [[langchain-self-correcting-memory-openwiki-2026-08-26]] |
| **Q3：生产级评测 × 统计功效 × Rubric 校准 × 成本基线** | [[production-ai-agent-evaluation-framework]] ↔ [[repeated-measures-statistical-power-for-ai-evaluation]] | 正式页：上述两页 + [[agent-evaluation-rubric-calibration]], [[production-agent-evaluation-baselines]], [[agent-self-validation-loops]]<br>原始源：[[towardsdatascience-statistical-power-more-problems-2026-08-04]], [[langchain-similarweb-long-form-agent-report-evaluation-2026-07-29]], [[kdnuggets-llm-latency-inference-cost-2026-07-18]] |
| **Q4：形式化工作流 × 分层代码审查 × Python 工程清单** | [[hermes-ai-workflow-formalization-principles]] ↔ [[hermes-python-engineering-capability-checklist]] | 正式页：上述两页 + [[ai-code-review-governance-and-convergence]], [[dijkstra-ai-programming-formalization]], [[typed-ai-agent-boundaries]], [[agent-self-validation-loops]]<br>原始源：[[claude-dev-solving-code-review-at-anthropic-2026-10-15]], [[aymannadeem-plan-mode-is-dead-2026-09-24]], [[realpython-python-performance-optimization-guide-2026-10-21]] |
| **Q5：子代理编排 × 生产拓扑取舍 × 资源路由与证据门** | [[subagent-orchestration-patterns]] ↔ [[agent-orchestration-production-tradeoffs]] | 正式页：上述两页 + [[agent-resource-optimization]], [[agent-research-evidence-gate]], [[hermes-context-layer-operating-rules]]<br>原始源：[[philschmid-subagent-patterns-2026-05-05]], [[alphasignal-agent-orchestration-patterns-2026-05-05]], [[langchain-model-router-in-harness-2026-10-01]] |
| **Q6：静态工具上下文 × 工具选择架构 × 类型化边界** | [[agent-context-prompt-tools-and-examples]] ↔ [[typed-ai-agent-boundaries]] | 正式页：上述两页 + [[ai-agent-tool-selection-architecture]], [[agent-context-engineering]]<br>原始源：[[microsoft-developer-ai-coding-agents-use-technology-2026-05-27]], [[machinelearningmastery-tool-selection-ai-agents-2026-07-06]], [[langchain-paid-media-agent-2026-09-13]] |
| **Q7：经验固化闭环 × Skill 可逆状态机 × 知识演化元技能** | [[agent-experience-consolidation-loops]] ↔ [[agent-skill-governance-and-reversible-state]] | 正式页：上述两页 + [[agent-knowledge-evolution-and-meta-skills]], [[hermes-memory-skills-wiki-boundaries]]<br>原始源：[[arxiv-2608-27454-wikiskill]], [[microsoft-research-evolib-evolving-knowledge-2026-07-30]], [[xudong-han-self-evolving-agent-alloomi-2026-08-13]] |
| **Q8：文档解析结构保真 × 文档失真风险 × 确定性计算边界** | [[document-parsing-structural-fidelity]] ↔ [[ai-agent-document-fidelity-risk]] | 正式页：上述两页 + [[deterministic-analytics-llm-reasoning-boundary]], [[typed-ai-agent-boundaries]]<br>原始源：[[llamaindex-markdown-is-all-you-need-2026-10-08]], [[venturebeat-frontier-ai-document-fidelity-risk-2026-05-13]], [[motherduck-jev-for-analytics-2026-09-29]] |

## 3. 静态图谱一跳双向可达性基线（2026-11-06 实测）

基于 `repository:_meta/catalog.json` 的显式 `## Relations` 边（含出边与 `wiki_reverse_lookup` 入边），对每个入口做 1 跳展开，**包含种子自身，并从图中排除本评测页及其关联边**，得到正式页集合 $P_A, P_B$，避免评测页的回链污染候选集合。$R_A, R_B$ 是这些正式页 frontmatter `sources` 中的直接 `raw/` 路径与非代码区原始源 wikilink 的并集，不递归扩展原始源。黄金集取第 2 节表格；集合指标（含召回率 $R$、精确率 $P$ 与一跳正式页 UTF-8 字节体积代理）按此口径重算如下。

有效输入（各正式页的 Relations 与上述直接原始源集合，排除本页）规范化后的 SHA256 为 `d644e62fff8102efcbaf1ed3b9d2d00eddaf9ea858a446e6150680876f7bbbb8`。该指纹仅固定拓扑与直接原始源集合，不覆盖正文体积；新增 `size_input_sha256: a065bded1ccaccd94b466301e786fabb7af840ec740d076acfcd3fe78396a426` 单独对正式页 UTF-8 字节数映射做指纹。正文或元数据变化后须重算体积及其指纹；两者均不代表模型问答评测通过。

| 题号 | $|P_A|$ / $|P_B|$ | 正式页重合度 $J(P_A, P_B)$ | 黄金正式页召回 $R(P_A)/R(P_B)$ | 黄金正式页精确率 $P(P_A)/P(P_B)$ | $|R_A|$ / $|R_B|$ | 黄金原始源召回 $R(R_A)/R(R_B)$ | 黄金原始源精确率 $P(R_A)/P(R_B)$ | 原始源重合度 $J(R_A, R_B)$ | 一跳正式页体积代理（Seed A / B KiB） | 结构诊断结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Q1** | 26 / 8 | 0.259 | 1.00 / 1.00 | 0.15 / 0.50 | 55 / 23 | 1.00 / 1.00 | 0.05 / 0.13 | 0.322 | 252.0 / 80.3 | 双入口一跳均 100% 覆盖黄金集；Seed B（状态子页）精确率显著高于高入度枢纽 Seed A（`0.50` vs `0.15`） |
| **Q2** | 14 / 8 | 0.571 | 1.00 / 1.00 | 0.36 / 0.62 | 21 / 5 | 1.00 / 1.00 | 0.10 / 0.40 | 0.238 | 126.3 / 68.7 | 消除 `index` 同名原始源碰撞后，双入口一跳均 100% 覆盖黄金集，且历史计划入口（Seed B）原始源精确率达 `0.40` |
| **Q3** | 32 / 7 | 0.182 | 1.00 / 1.00 | 0.16 / 0.71 | 68 / 20 | 1.00 / 1.00 | 0.04 / 0.15 | 0.275 | 300.6 / 62.9 | 统计功效页（Seed B）一跳黄金正式页精确率达 `0.71`（体积仅 `62.9 KiB`），而评估总框架（Seed A）因汇聚全库评估子页使候选池达 `300.6 KiB` |
| **Q4** | 29 / 12 | 0.171 | 1.00 / 1.00 | 0.21 / 0.50 | 63 / 48 | 1.00 / 1.00 | 0.05 / 0.06 | 0.291 | 295.4 / 134.6 | Python 工程清单页（Seed B）一跳正式页精确率（`0.50`）与体积代理（`134.6 KiB`）均优于形式化总原则枢纽页（Seed A） |
| **Q5** | 31 / 20 | 0.417 | 1.00 / 1.00 | 0.16 / 0.25 | 70 / 61 | 1.00 / 1.00 | 0.04 / 0.05 | 0.560 | 306.4 / 221.4 | 双入口均为高连接度编排核心页，一跳原始源重合度最高（`0.560`），但需靠 `locate` 二次筛选裁剪候选体积 |
| **Q6** | 8 / 28 | 0.200 | 1.00 / 1.00 | 0.50 / 0.14 | 23 / 66 | 1.00 / 1.00 | 0.13 / 0.05 | 0.254 | 77.9 / 290.7 | 静态上下文子页（Seed A，`77.9 KiB`）比类型化边界枢纽页（Seed B，`290.7 KiB`）具有更高的一跳信噪比（`P(P)=0.50`） |
| **Q7** | 18 / 9 | 0.286 | 1.00 / 1.00 | 0.22 / 0.44 | 34 / 13 | 1.00 / 1.00 | 0.09 / 0.23 | 0.306 | 168.8 / 76.4 | 经验固化主干页与两个子页形成完整三角互链；从子页（Seed B）进入可将一跳体积控制在 `76.4 KiB` |
| **Q8** | 4 / 9 | 0.444 | 1.00 / 1.00 | 1.00 / 0.44 | 10 / 33 | 1.00 / 1.00 | 0.30 / 0.09 | 0.303 | 41.9 / 101.8 | 文档解析页（Seed A）一跳 4 页恰好全为黄金正式页（`P(P)=1.00`，`41.9 KiB`），全表 Q1–Q8 双入口一跳黄金召回率均为 `1.00 / 1.00` |

### 复算命令

在本仓库根目录运行；只读，不写目录或评测产物。输出依次为题号、正式页数、正式页 Jaccard、黄金正式页召回、黄金正式页精确率、原始源数、黄金原始源召回、黄金原始源精确率、原始源 Jaccard 与一跳正式页体积代理（KiB）。未来图谱变动时应重算指纹和表格；历史提交可通过 Git 回放。

```bash
python3 - <<'PY'
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path('_meta/scripts').resolve()))
from wiki_health_check import extract_frontmatter, strip_code
from wiki_reverse_lookup import markdown_pages, sources

root = Path.cwd()
benchmark = 'queries/wiki-cross-source-evidence-navigation-benchmark.md'
catalog = json.loads((root / '_meta/catalog.json').read_text())
pages = {Path(p['path']).stem: p for p in catalog['pages'] if p['path'] != benchmark}
raw = {p.stem: p.relative_to(root).as_posix() for p in markdown_pages(root)
       if p.relative_to(root).parts[0] == 'raw' and p.stem != 'index'}
graph = {slug: set() for slug in pages}
evidence, sizes, inputs = {}, {}, {}
for slug, page in pages.items():
    raw_bytes = (root / page['path']).read_bytes()
    sizes[slug] = len(raw_bytes)
    text = raw_bytes.decode('utf-8')
    refs = {s for s in sources(extract_frontmatter(text)) if s.startswith('raw/')}
    links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]', strip_code(text))
    refs.update(raw[s] for s in links if s in raw)
    evidence[slug] = refs
    inputs[slug] = {'relations': page['relations'], 'raw': sorted(refs)}
    for targets in page['relations'].values():
        for target in targets:
            if target in pages:
                graph[slug].add(target)
                graph[target].add(slug)
encoded = json.dumps(inputs, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
print('input_sha256', hashlib.sha256(encoded.encode()).hexdigest())
size_encoded = json.dumps(sizes, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
print('size_input_sha256', hashlib.sha256(size_encoded.encode()).hexdigest())

def jaccard(a, b):
    return f'{len(a & b) / len(a | b):.3f}' if a | b else 'N/A'

def recall(a, gold):
    return f'{len(a & gold) / len(gold):.2f}' if gold else 'N/A'

def precision(a, gold):
    return f'{len(a & gold) / len(a):.2f}' if a else 'N/A'

for line in (root / benchmark).read_text().splitlines():
    match = re.match(r'^\| \*\*Q([1-8])：', line)
    if not match:
        continue
    cells = line.split('|')
    a, b = re.findall(r'\[\[([^\]]+)\]\]', cells[2])
    goldlinks = re.findall(r'\[\[([^\]]+)\]\]', cells[3])
    gold = {a, b, *[s for s in goldlinks if s in pages]}
    goldraw = {raw[s] for s in goldlinks if s in raw}
    A, B = {a} | graph[a], {b} | graph[b]
    RA = set().union(*(evidence[s] for s in A))
    RB = set().union(*(evidence[s] for s in B))
    kib_a = sum(sizes[s] for s in A) / 1024.0
    kib_b = sum(sizes[s] for s in B) / 1024.0
    print('Q' + match[1], f'{len(A)}/{len(B)}', jaccard(A, B),
          f'{recall(A, gold)}/{recall(B, gold)}',
          f'{precision(A, gold)}/{precision(B, gold)}',
          f'{len(RA)}/{len(RB)}',
          f'{recall(RA, goldraw)}/{recall(RB, goldraw)}',
          f'{precision(RA, goldraw)}/{precision(RB, goldraw)}',
          jaccard(RA, RB), f'{kib_a:.1f}/{kib_b:.1f}')
PY
```

## 4. 黄金断言与章节级证据映射表（Q1–Q8 Claim-to-Section Grounding Map）

为支持后续离线或端到端模型问答评测按章节核对引用正确性（Citation Precision / Recall）与 Answer Faithfulness，下表将 Q1–Q8 的核心跨源综合断言固定映射到黄金正式页的具体章节与底层 `raw/` 证据锚点（模型层重复问答 Citation Consistency 仍保持 **NOT_RUN**）：

| 题号 | 跨源核心综合断言（Target Synthesis Claim） | 黄金正式页章节锚点（Formal Section Anchors） | 底层原始证据锚点（Primary Raw Evidence Anchors） |
| --- | --- | --- | --- |
| **Q1** | 上下文工程应优先隔离静态契约与动态观察：长程程序性状态通过确定性校验的 `SKILL.state` 投影维护，工具大输出与历史膨胀分别用转储与有界专用模型加工处理，并保留原始证据回读路径 | [[agent-context-engineering]] `## Context rot and JIT defense`；[[agent-context-history-state-and-bounded-processing]] `### SKILL.state：状态成为执行真相源，而不是历史摘要`、`## 专用模型承担有界上下文加工`；[[hermes-context-engineering-design-priorities]] `## Improvement priorities when a gap is observed`；[[hermes-memory-skills-wiki-boundaries]] `## Boundary rule` | [[arxiv-2608-26263-skill-state]], [[langchain-scaledown-deep-agents-2026-10-13]], [[machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28]] |
| **Q2** | 编译型知识库通过显式 `## Relations` 与段落级来源绑定支持 `locate` → `expand` 两步证据导航；现行规范已由 `supersedes` 替代旧改造计划，且必须区分静态图可达重合度与多次问答的段落引用一致性 | [[hermes-knowledge-freshness-and-claim-evidence]] `### 在本 Wiki 中的可迁移映射`；[[hermes-wiki-knowledge-freshness-improvement-plan]] `## Decision`；[[hermes-knowledge-architecture]] `## Architecture at a glance`；[[hermes-wiki-page-writing-standards]] `## Wikilinks and relations`；[[hermes-memory-skills-wiki-boundaries]] `## What belongs in wiki` | [[langchain-agent-memory-openwiki-graphs-2026-10-28]], [[langchain-self-correcting-memory-openwiki-2026-08-26]] |
| **Q3** | 生产级 Agent 评估须分层覆盖检索、生成、行为与成本/延迟分位数基线；少样本对照须识别同一题目重复采样的伪重复与方差结构，并用带理由的专家反馈校准开放式 Rubric | [[production-ai-agent-evaluation-framework]] `## Evaluation layers`；[[repeated-measures-statistical-power-for-ai-evaluation]] `## 核心问题：更多数据点是否真的增加证据`；[[agent-evaluation-rubric-calibration]] `## Turn expert review into reusable evaluation data`；[[production-agent-evaluation-baselines]] `## Latency and cost baseline`；[[agent-self-validation-loops]] `## Core pattern` | [[towardsdatascience-statistical-power-more-problems-2026-08-04]], [[langchain-similarweb-long-form-agent-report-evaluation-2026-07-29]], [[kdnuggets-llm-latency-inference-cost-2026-07-18]] |
| **Q4** | AI 编程不能用自然语言生成替代形式化规约：编码前先收敛可验证契约与类型边界，Python 实现遵守流式/资源/并发与测量驱动优化清单，审查阶段按风险分级收敛并验证测试断言 | [[hermes-ai-workflow-formalization-principles]] `## Principle 2.6: specification is an agreement, not an eight-field ritual`；[[hermes-python-engineering-capability-checklist]] `## Durable units from the article`；[[ai-code-review-governance-and-convergence]] `## 3. 分层防线、风险分级审批与审查收敛：以回滚率约束人类注意力`；[[dijkstra-ai-programming-formalization]] `## Core thesis`；[[typed-ai-agent-boundaries]] `## Core pattern`；[[agent-self-validation-loops]] `## Core pattern` | [[claude-dev-solving-code-review-at-anthropic-2026-10-15]], [[aymannadeem-plan-mode-is-dead-2026-09-24]], [[realpython-python-performance-optimization-guide-2026-10-21]] |
| **Q5** | 子代理编排应先验证单 Agent 基线与任务可分解性，按协调成本和错误相关性选择最小拓扑；主代理保留目标与证据门裁决，子任务通过有界上下文交接并结合任务上下文做资源/模型路由 | [[subagent-orchestration-patterns]] `## Single-agent first escalation rule`；[[agent-orchestration-production-tradeoffs]] `### Additive value must beat coordination cost`；[[agent-resource-optimization]] `## 任务上下文驱动的模型分层：Open SWE 案例`；[[agent-research-evidence-gate]] `## Gate contract`；[[hermes-context-layer-operating-rules]] `### 7. Subagent` | [[philschmid-subagent-patterns-2026-05-05]], [[alphasignal-agent-orchestration-patterns-2026-05-05]], [[langchain-model-router-in-harness-2026-10-01]] |
| **Q6** | 工具表面应保持窄接口与强类型契约：区分资源发现、工具可用性、候选集缩减与逐步选择，避免因暴露过多同名或宽泛工具导致选择准确率下降，并以行为示例引导调用 | [[agent-context-prompt-tools-and-examples]] `## Tools: narrow action surface with negative boundaries`；[[typed-ai-agent-boundaries]] `### 3. Tool functions define a narrow action surface`；[[ai-agent-tool-selection-architecture]] `## Four distinct decisions`；[[agent-context-engineering]] `## Summary` | [[microsoft-developer-ai-coding-agents-use-technology-2026-05-27]], [[machinelearningmastery-tool-selection-ai-agents-2026-07-06]], [[langchain-paid-media-agent-2026-09-13]] |
| **Q7** | 经验固化闭环必须区分不可变执行轨迹、可回滚的候选 Skill 状态机与持久编译知识：新经验经整合/加权/拒绝后按层职责路由，且指导 Target 的任务技能与指导 Builder 的元技能须分别评估 | [[agent-experience-consolidation-loops]] `## Core pattern`；[[agent-skill-governance-and-reversible-state]] `## Separate persistent knowledge from reversible Skill state`；[[agent-knowledge-evolution-and-meta-skills]] `## Evolve knowledge instead of only appending experience`、`## Distinguish task skills from support-design meta-skills`；[[hermes-memory-skills-wiki-boundaries]] `## Boundary rule` | [[arxiv-2608-27454-wikiskill]], [[microsoft-research-evolib-evolving-knowledge-2026-07-30]], [[xudong-han-self-evolving-agent-alloomi-2026-08-13]] |
| **Q8** | 文档处理与分析应将结构保真解析、概率性语义判断与确定性计算分层：Markdown/HTML/JSON 各司其职，多轮处理核对表头/单位/脚注防失真，不把 LLM 分类标签当作已验证的确定性事实 | [[document-parsing-structural-fidelity]] `## 格式按职责分工`；[[ai-agent-document-fidelity-risk]] `## Reusable pattern`；[[deterministic-analytics-llm-reasoning-boundary]] `## 自由文本的有界语义分类：概率性加工，确定性聚合`；[[typed-ai-agent-boundaries]] `### 1.1 Stage scope selection before nested extraction` | [[llamaindex-markdown-is-all-you-need-2026-10-08]], [[venturebeat-frontier-ai-document-fidelity-risk-2026-05-13]], [[motherduck-jev-for-analytics-2026-09-29]] |

## 5. 采用与晋升边界

- 上表仅证明本仓库 `## Relations` 与段落级 `[[raw-...]]` 锚定在 1–2 跳内具备确定性图可达性；**模型在真实多跳问答中的引用一致性（Citation Consistency）、精确率与成本节省仍为待执行（NOT_RUN）假设**。
- 在提交模型问答评测脚本、独立复核黄金集与多次问答轨迹产物前，不得将静态可达率宣称为端到端问答准确率或引用稳定性提升。

## Relations

- refines: [[hermes-knowledge-freshness-and-claim-evidence]], [[production-agent-evaluation-baselines]]
- depends_on: [[hermes-retrieval-priority-and-answer-path]], [[production-ai-agent-evaluation-framework]]
- related: [[agent-context-engineering]], [[agent-context-history-state-and-bounded-processing]], [[hermes-context-engineering-design-priorities]], [[hermes-memory-skills-wiki-boundaries]], [[hermes-wiki-knowledge-freshness-improvement-plan]], [[hermes-knowledge-architecture]], [[hermes-wiki-page-writing-standards]], [[repeated-measures-statistical-power-for-ai-evaluation]], [[agent-evaluation-rubric-calibration]], [[agent-self-validation-loops]], [[hermes-ai-workflow-formalization-principles]], [[hermes-python-engineering-capability-checklist]], [[ai-code-review-governance-and-convergence]], [[dijkstra-ai-programming-formalization]], [[subagent-orchestration-patterns]], [[agent-orchestration-production-tradeoffs]], [[agent-resource-optimization]], [[agent-research-evidence-gate]], [[hermes-context-layer-operating-rules]], [[agent-context-prompt-tools-and-examples]], [[typed-ai-agent-boundaries]], [[ai-agent-tool-selection-architecture]], [[agent-experience-consolidation-loops]], [[agent-skill-governance-and-reversible-state]], [[agent-knowledge-evolution-and-meta-skills]], [[document-parsing-structural-fidelity]], [[ai-agent-document-fidelity-risk]], [[deterministic-analytics-llm-reasoning-boundary]]
