---
title: "5 Jev use cases for analytics, with real queries and datasets"
author: Mehdi Ouazza
publisher: MotherDuck
type: raw-source
source_type: article
source_url: https://motherduck.com/blog/jev-analytics-use-cases/
published_at: 2026-10-06
captured_at: 2026-10-10
status: raw
capture_scope: selected-paraphrased-source-note
sources: [https://motherduck.com/blog/jev-analytics-use-cases/, https://motherduck.com/docs/sql-reference/motherduck-sql-reference/ai-functions/prompt-jev/]
---

# 5 Jev use cases for analytics, with real queries and datasets

## Provenance and capture scope

- 原文：Mehdi Ouazza，MotherDuck，2026-10-06，页面显示预计阅读时间 15 分钟。
- 本页基于原站完整可读正文、静态表格与 SQL 示例整理，是选取并转述的来源笔记，不是全文镜像，也不是独立实验报告。
- 来源质量：厂商发布的第一方产品实践文章。Agent 案例按作者描述来自生产流程，销售案例明确为虚构示例；其余数据分析与性能数字均为作者报告，未独立复现。
- 未执行 SQL、接入公开数据 share、验证交互式 Dive 或检查图片像素；图片中的信息仅采用正文和图注明确说明的部分。
- 下文区分文章内容、补充官方文档与编译推论。官方文档无可见发布日期，产品边界仅代表 2026-10-10 查阅状态，采用前须重新核验。

## Article notes — Agent trace evaluation

文章描述 MotherDuck 试用 Agent 的 OpenTelemetry spans 落入数据库，再通过每日 Flight 使用 `prompt_jev()` 评分：

- 每轮评估是否完成请求；对未达案例阈值的轮次分类失败模式。
- 对每个失败工具调用判断原因，例如模型生成无效 SQL/Python、猜错数据、平台问题或工具缺陷。
- 对有工具调用的轮次评估不必要调用数量；只对效率低于案例阈值的轮次追问主要浪费来源。
- 完成度与效率均采用三个有序等级；文章示例中的后续分流阈值分别为 `1.5` 和 `1.2`，不应视为通用评分门槛。

效率判断读取用户请求、按顺序排列的文本与调用轨迹、最终答案开头。SQL 示例分别截取请求前 1,500 字符、轨迹前 8,000 字符和答案前 1,200 字符；截断是该案例的输入选择，不证明被省略内容不影响判断。

文章为效率 Rubric 明列例外：首次使用工具前各读一次指南、保存 Dive 后立即查看、每次运行 Flight 后等待一次，不计浪费；失败调用后一次纠正重试也不计浪费。这些是其产品契约，不是所有 Agent 的免罚清单。

两个可迁移设计：低成本评分覆盖各轮，原因判断仅在低分轮次触发；重复调用与额外等待的精确计数由 SQL 从 spans 产生，模型只负责需要语义判断的问题。原文短引：

> “Facts and judgments never mix”

作者同时展示效率分数提示少量浪费、主要浪费标签却为无的例子，将这种不一致作为回查信号。同一 judge 也用于离线 eval；文中每模型只有 12 个案例，作者明确提示在切换模型前做更大评测。其模型表不是独立排名或充分选型证据。

## Article notes — Text classification patterns

### Social listening

作者先用正则查找 AI 公司或产品名称，再按公司与季度分层抽样并加权。文章报告候选提及 488,483 条、实际样本 65,635 条；统计百分比为加权结果。

模型结合日期与命名产品，区分同名实体、是否真正讨论目标产品、负面态度和主题。它将“名称匹配”“讨论相关性”“负面情绪”拆成不同问题，避免将顺带提及或其他 Gemini/Claude 实体算作产品意见。文章使用的多个置信阈值属于案例配置；HN 是偏开发者的人群，不能解释为总体市场份额。

### Sales calls

销售 SQL 使用虚构的通话与账户表，模型只回答明确产品需求是否出现，账户规模与职位沿用 CRM 的结构化字段。高分仅用于形成供人工检查的候选名单，不等于优质线索；文章建议按已标注通话验证阈值。

### Job postings and cloud platforms

输入使用职位名称与提及云的句子，而不是完整描述。候选类别除实际云厂商外，还包括“多云、无明确主平台”和“云仅被顺带提及”，防止强行选择厂商。地图另排除云厂商自己的招聘，仅保留单一云提及、真实云类别和达到案例置信阈值的记录。

文章报告的数据过滤和地域结果只是相应招聘样本与过滤条件下的代理观察，不证明企业真实部署或云市场份额。未先翻译的多语言示例也不证明中文质量。

### Remote / hybrid / on-site

作者以写明定义的远程、混合、现场、未说明四类，替代不断补丁的语义正则。对相同的 2,000 条招聘文本，作者报告正则 `0.2 秒`、普通 `prompt()` ENUM 输出 `37.0 秒`、Jev `1.7 秒`；正文未同时提供这组方法的人工金标准准确率，不能仅按速度认定质量等价或模型优于规则。

结尾建议：格式明确的 ID、邮件、URL、日期等仍用规则；语义问题才评估模型，也可先用便宜的规则筛选再作语义分类。先标注小样本、检查确定与不确定结果、验证阈值，成立后保存分类结果，避免仪表盘重复付费分类。有界模型不能写摘要或创造新类别。

## Supplemental official documentation — dated product boundaries

参考：[PROMPT_JEV 官方文档](https://motherduck.com/docs/sql-reference/motherduck-sql-reference/ai-functions/prompt-jev/)，2026-10-10 查阅。

- 功能仍为 Preview，名称、参数与返回类型可能改变；各云区域请求均在 TypeSafe 美国服务器处理，文档建议 Preview 阶段避免受监管或敏感数据。
- 输入、指令与类别会发送给 TypeSafe。`prompt_jev()` 使用 `jev-latest` 别名，没有 model 参数；不能把分类结果中的处理时间当作已固定底层模型版本。
- 输出是概率、固定候选选择或有序评分，不返回自由文本；有序评分范围由类别数量决定。
- 官方称概率经过校准，但有效响应仍可能决策错误；本次未验证目标数据上的校准或准确性。不得与上一篇文章的分数集中度解释拼成已证实的统一概率保证。
- 输入为空、重试后失败或超时等可导致行结果为 `NULL`；缺失判断不能静默视为否定或普通类别。

## Compilation implications — not measured outcomes

- 分阶段评分与低分归因可补充 [[production-ai-agent-evaluation-framework]]；它提供一种减少重复诊断的设计，不证明任意工作流的成本收益或全量故障检出率。
- 效率 Rubric 必须说明必要前置与验证动作，详见 [[agent-evaluation-rubric-calibration]]；不能为了少调用而奖励跳过合同要求的证据。
- 保留“不明确／不适用”类别、区分候选召回与语义判断，可补充 [[deterministic-analytics-llm-reasoning-boundary]]。类别出口不替代阈值验证、失败分流与高置信抽查。
- 不从本文推导默认采用 MotherDuck/Jev、模型切换、全局阈值、持续任务或任何 active runtime 改动。
