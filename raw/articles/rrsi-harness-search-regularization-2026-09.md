---
title: "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses（项目主页结构化摘录）"
author: "Peng Xia 等"
source_type: project-homepage
source_url: https://regularized-rsi.com/
paper_url: https://arxiv.org/abs/2609.24972v2
published_at: "项目主页未注明；预印本 v1 于 2026-09-21 提交，v2 于 2026-09-23 修订"
captured_at: 2026-09-29
type: raw-source
status: raw
---

# RRSI 项目主页：结构化来源记录

## Provenance and capture quality

来源为 [项目主页](https://regularized-rsi.com/)，作者署名 Peng Xia、Rujun Han 等，链接到 [arXiv:2609.24972v2](https://arxiv.org/abs/2609.24972v2) 和公开代码仓库。2026-09-29 读取主页正文；静态文本抽取遗漏部分交互图表，以下数据另对照当日已有的完整网页内容抓取。本文是中文结构化摘录，不是主页或论文的全文复制，也不是独立复现。预印本仅核对了 arXiv 摘要与版本信息，未把论文 PDF 当作已逐节审阅的证据。

## Problem and mechanism reported by authors

作者认为，自动修改 Agent harness（提示词、工具、控制流、记忆和上下文）容易在被优化的基准任务上取得收益，却不能迁移到未见任务。RRSI 不冻结特定组件，而是约束搜索与候选采纳：

- 提案侧：随轮次收缩一次候选可打包的编辑数；记录每次假设、差异、得分和成本；停滞时探索尚未修改的组件。
- 筛选侧：评分前用 critic 排除任务名称、答案和基准特化逻辑；按未修改 harness 的方差校准收益门槛；新增推理 token 必须以实测增益偿付；不再有边际价值的组件可被剪枝。
- 主页概览将噪声门槛简写为增益必须越过方差；演化探索器末尾明确写道：“inside the noise band a candidate is admitted only for a token saving or a new structural component.” 这里的“新增结构组件”是**采纳例外**；提案侧另有“停滞时转向未探索组件”的搜索策略，两者不能混为一谈。

## Reported results and scope

- 主页称在三个领域、八个 benchmark 上评估；主页顶部写三项演化基准平均 +4.0 分，六项未用于优化的评估平均 +3.4 分、六项均改善。这是作者报告的分布外结果，不等于任意新任务或其他底座模型均有保证。
- Harvey LAB 表中的 agentic-workspace OOD 平均分：未演化 H0 为 39.7，RRSI 为 43.6；不能把这组数字写成所有 OOD 任务的统一平均。
- 主页称最终 harness 每次试验的 policy token 较未正则化演化少 36%；Terminal-Bench 2.1 追踪中首个获采纳候选本身的 token 增量为 +67.8%。两者分母与比较对象不同，不矛盾，也不能概括为每处修改都降低 token。
- Terminal-Bench 2.1 展示 89 个任务、每项两次试验、20 轮和 40 个候选；其中 5 个获采纳，24 个未过噪声门槛、8 个未过成本规则、1 个被防泄漏审查拒绝、2 个未过冒烟筛查。首个获采纳候选结合完成前一次有界真实验收与长耗时工作轮询规范；得分变化 +3.93 分，页面给出的噪声带为 3.41 分。这些阈值只属于该实验设置。
- 主页说明主要比较保持策略模型 Claude Opus 4.8、工具、judge、试验次数和窗口一致。主页存在“Unseen backbone”等可切换图表；本摘录没有把交互页的所有切片或跨模型性能当作已核验结果。

## Version mismatch and limits

arXiv v2 摘要写的是“五个”分布外 benchmark、相对未正则化演化“少 30%”policy token，而 2026-09-29 的项目主页顶部写“六个”和“少 36%”。两者当前表述不一致；这里保留各自来源与比较口径，不合并成一个更强结论。没有在本次摘录中核对论文正文、代码运行或独立复现实验。搜索期间的提案与重复评分成本，不等于最终 harness 的单次推理成本。
