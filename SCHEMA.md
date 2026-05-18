# Wiki Schema

## Domain
这个知识库用于沉淀与 Hermes 协作的长期知识资产，覆盖：
- AI / LLM / Agent / MCP / 自动化工作流
- DevOps / Linux / 网络 / 部署 / 故障处理
- 工具链、配置经验、最佳实践
- 值得长期保留的研究摘录、对比分析、决策记录

目标不是保存聊天原文，而是把高价值信息编译成可复用、可交叉链接、可持续维护的 Markdown 知识层。

## Conventions
- 根目录固定为 `~/wiki`
- 文件名统一使用小写英文加连字符，例如：`hermes-knowledge-architecture.md`
- 正式知识页放在 `entities/`、`concepts/`、`comparisons/`、`queries/`、`operations/`
- 原始材料只放在 `raw/`，不得直接修改原文内容
- 每个正式知识页必须包含 YAML frontmatter
- 每个正式知识页至少包含 2 个 `[[wikilinks]]` 指向其他页面或索引页
- 新建或更新页面后，必须同步更新 `index.md`
- 每次关键操作都必须追加到 `log.md`
- `memory` 只存稳定偏好与长期事实；正式知识以 wiki 为准

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | plan | closeout | validation-case | operation | summary
tags: [tag1, tag2]
sources: [raw/articles/source-name.md]
status: draft | stable | active | closed | current

# Wiki self-governance / normative pages may use:
source_policy: normative

# Raw-source files under raw/ may use:
type: raw-source
status: raw | captured
---
```

Frontmatter rules:
- `queries/` historically contains `type: query` pages that may behave like plans, closeouts, or validation cases. Schema expansion does not authorize bulk reclassification; future reclassification requires a separate approved migration plan.
- `source_policy: normative` is only for wiki rules, standards, operating policies, and self-authored governance pages. It is a documentation marker only; current health-check scripts do not enforce it.
- Deferred historical status values such as `current-as-of-<date>`, `_meta/` `complete`/`completed`, and raw `raw-source` status should be handled in a later metadata cleanup, not normalized during schema alignment.

### Sources

Allowed `sources` forms:
- `raw/...`：wiki 内保留的原始材料
- `concepts/...`、`queries/...`、`comparisons/...`、`operations/...`：wiki 内派生来源
- `project:/absolute/path`：本地项目证据
- `session:<stable-id>`：会话来源
- `skill:<skill-name>`：Hermes skill 来源
- `docs:<name-or-url>`：官方或外部文档来源
- `filesystem:<path>`：本地文件系统观察，谨慎使用

`/tmp/...` 不应作为正式页面唯一长期来源。后续清理时应替换为可持久路径、稳定 wiki/review 页面，或明确标记为历史不可复验来源。

## Tag Taxonomy

Tags are grouped by purpose. Use lowercase kebab-case. Add a new tag here before using it on pages.

**Core tags** describe broad, cross-wiki categories:

- hermes
- knowledge-base
- agent
- llm
- mcp
- automation
- workflow
- tool
- configuration
- debugging
- research
- comparison
- decision
- note

**Domain tags** name the main subject area of a page:

- devops
- linux
- networking
- product
- investment
- trading
- governance
- validation
- project
- monitoring
- memory
- skills
- cron
- browser
- context-engineering
- content-engineering
- position-sizing
- architecture
- risk-control
- deployment
- lifecycle
- optimization
- lifeos

**Facet tags** describe a cross-cutting angle, method, tool mode, or evaluation lens that can apply across multiple subject areas:

- ai-coding
- claude-code
- multi-agent
- subagent
- orchestration
- evaluation
- verification
- operating-model
- gstack
- model-profiles
- harness
- closeout
- pydantic
- structured-output
- typed-boundary

Rules:
- If a tag appears on 3+ pages, consider adding it to this taxonomy.
- If a tag appears on 1-2 pages, prefer an existing broader tag unless the narrow tag has clear future retrieval value.
- If two tags mean the same thing, keep one canonical spelling and replace the other.
- Reserved but currently unused tags are allowed when they match stable future page areas, e.g. `devops`, `linux`, `networking`, `product`.
- `gstack` is a facet tag for pages about the gstack-derived project execution/review lane in Hermes. It is not currently an entity page or a generic project tag; keep it paired with broader tags such as `workflow`, `validation`, or `project-development`.

## Page Thresholds
- 某个主题在 2 个以上来源重复出现，或在单个来源中足够核心时，创建独立页面
- 已存在页面则优先增量更新，而不是重复建页
- 只被顺手提及一次的内容，不单独建页
- 页面超过约 200 行时，拆分为子主题页并互相链接

## Directory Roles
- `raw/articles/`：网页、博客、文档摘录
- `raw/papers/`：论文、PDF 提取内容
- `raw/transcripts/`：会议记录、视频/语音转写
- `raw/assets/`：图片、截图、附件
- `entities/`：人、组织、产品、项目、模型
- `concepts/`：概念、架构、方法论、机制
- `comparisons/`：横向对比
- `queries/`：值得沉淀的问题与答案；历史上也保留部分 plan / closeout / validation case，未来新页面应优先按语义路由到更准确的位置
- `operations/`：稳定运行面板、runbook、维护契约和 recurring governance surface；不放一次性项目计划或 raw review artifact
- `_meta/`：导航与维护文档
- `_meta/plans/`：计划、整改路线图、执行前治理方案
- `_meta/reviews/`：独立审查 prompt 和审查结果
- `_meta/scripts/`：wiki 只读检查、审计和维护脚本

## Update Policy
当新信息与旧信息冲突时：
1. 优先保留带日期和来源的两种说法
2. 不静默覆盖旧结论
3. 在页面中显式标注冲突与时间
4. 必要时单独建立 comparison / query 页面

## Initial Seed Pages
初始化阶段至少保留并维护以下页面：
- `index.md`
- `log.md`
- `concepts/hermes-knowledge-architecture.md`
- `concepts/wiki-ingestion-workflow.md`

## Operating Rule
回答知识相关问题时，优先顺序为：
1. 先查 wiki
2. wiki 不足再查外部资料
3. 有长期价值的结果再回写 wiki
