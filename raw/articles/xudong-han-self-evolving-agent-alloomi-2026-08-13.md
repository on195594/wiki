---
title: Xudong Han on Self-Evolving Agent and Alloomi
published: 2026-08-13
captured: 2026-08-14
type: raw-source
source: X / Xudong Han
source_url: https://x.com/Xudong07452910/status/2087856761755549920
status: captured
extraction: Public X post text extracted from gallery-dl metadata; the linked technical report was inspected separately at https://alloomi.ai/reports/sea.pdf. Local Gemini summary: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260814-202327-{-487945-310446880-summary.md
---

# Xudong Han on Self-Evolving Agent and Alloomi

## Source metadata

- Author: Xudong Han (`@Xudong07452910`)
- Published: 2026-08-13 11:00:17
- Original post: https://x.com/Xudong07452910/status/2087856761755549920
- Technical report: https://alloomi.ai/reports/sea.pdf
- OpenContext repository: https://github.com/melandlabs/opencontext
- Source quality: complete public post text; first-party commentary on Alloomi's work
- Limitation: the performance claims are reported by the project authors and are not independent replication evidence. The technical report reports its main empirical results with three seeds and lists longer-horizon and stronger-ablation experiments as deferred work.

## Original post

我最近分享了很多 Agent 自进化相关的工作，有一个问题一直觉得很关键：

Agent 在真实任务里产生了大量轨迹和反馈，最后到底该学什么？

现在很多 Agent 已经能跑很长的任务，也有 memory、skills、harness 去保存经验。但很多时候，这些经验依然停留在模型外面：存进向量库、写进 skill、塞回 context。

Agent 能「记住过去」，和真正「从过去学会东西」，中间其实还有很长一段距离。

最近看了下 @AlloomiAI 在做的 Self-Evolving Agent，我觉得有意思的也是这里。

他们把真实工作里的上下文、专家修改、任务结果和反馈组织成完整轨迹，再经过质量筛选、专家锚定和后训练，让这些经验逐渐进入模型能力。

整个闭环大概是：

工作轨迹 → 筛选经验 → 专家锚定 → 后训练 → 评测准入 → 出问题可以回滚。

在 CL-Bench 上，同一个 backbone 经过这套方法后，成绩从 24.5% 提升到了 47.6%。

我比较关注的其实是它背后的方向：

未来 Agent 的自进化，需要解决怎么获得真正有价值的经验，以及怎么安全地把这些经验变成下一次任务可以复用的能力。

Alloomi 还把其中的上下文运行时 OpenContext 开源了，可以直接接进自己的 Agent。

现在我再去看很多的 Agent，比起单次任务做得更强，我现在更关注它们能不能在长期使用中持续变得更熟练。

技术报告：
https://alloomi.ai/reports/sea.pdf

OpenContext：
https://github.com/melandlabs/opencontext
