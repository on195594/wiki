---
title: Gstack Project Execution Lane Validation Case
created: 2026-04-23
updated: 2026-04-23
type: query
tags: [gstack, hermes, workflow, validation, project-kickoff]
sources: [session:gstack-project-execution-lane-validation]
status: stable
---

# Gstack Project Execution Lane Validation Case

## Summary
这页记录了一次用真实小项目验证 `[[gstack-project-execution-lane]]` 的闭环案例。验证目标不是证明某个脚本“能跑”，而是检验 office-hours、CEO review、Eng review、review、QA 这条推进链，是否真的能把一个模糊想法压成更稳的可执行入口。结果证明：这条 lane 对 Hermes 小项目启动是有价值的，尤其能帮助收窄范围、避免过早做宽，并把“聊天里的想法”变成可继续推进的 kickoff artifact。

## Validation Question
把 5 个最实用的 gstack skill 写进 wiki，到底只是多一份文档，还是能真实改善 Hermes / LifeOS 里的项目推进？

## Test Project
本次选择的验证项目是：
- 输入一句项目想法
- 生成一页固定结构的 wiki kickoff 草稿
- 落到 `~/wiki/queries/`

项目名称可以概括为：
- Hermes 小项目 intake -> wiki kickoff 页面生成器

选择它的原因是：
- 足够小，1 到 2 天能闭环
- 最终产物直接进入现有 wiki 体系
- 每一步都能留下清楚中间产物
- 很适合暴露“会不会做宽”“artifact 是否真能支持下一步推进”这类问题

## Step 1: office-hours
这一步的核心收敛，不是“做一个生成页面的工具”，而是先识别真正问题：
- Hermes 当前缺少一个稳定的小项目启动入口
- 从一句模糊想法到正式 kickoff 页的转换不稳定
- 如果没有稳定入口，后面的 plan、implementation、review 都容易漂移

收敛后的最小切口是：
- 只做一句项目想法 -> 一页固定结构 kickoff 草稿
- 只写到 `~/wiki/queries/`
- 不碰自动分类、自动索引、自动日志、自动规划

这一轮的价值最大的一点是：
- 它先把“是不是要做一个更大的项目系统”这个冲动压掉了

## Step 2: CEO review
CEO review 的作用，是继续砍范围，而不是补功能。

这一轮明确了：
- 第一用户不是“所有 Hermes 用户”，而是当前已经有 wiki 体系、会频繁启动小项目的自己
- 第一版的最小价值不是“智能生成”，而是“稳定 kickoff 起点”
- 这次实验要验证的是流程价值，不是模型即兴发挥

明确推迟的内容包括：
- 自动分类到 concepts / queries / operations
- 自动更新 `index.md` / `log.md`
- 多模板
- 自动研究扩写
- 自动生成计划
- skill 化 / cron 化

这一轮最重要的价值是：
- 把一个容易膨胀成小系统的平台型想法，重新拉回到最小验证器

## Step 3: Eng review
Eng review 把方向压成工程上可执行的版本：
- 脚本路径：`/home/lin/.hermes/scripts/project_kickoff.py`
- 输入：`--idea`、`--slug`、可选 `--title`
- 输出：`~/wiki/queries/<slug>.md`
- 默认拒绝覆盖
- 用固定 frontmatter 和固定 section 骨架输出 markdown

这一轮的价值是：
- 把“值得做”变成“做得出来”
- 让验证目标落到可以直接执行和验证的文件、参数、路径上

## Step 4: implement
最小实现阶段实际产出了：
- 脚本：`/home/lin/.hermes/scripts/project_kickoff.py`
- 早期样例页面：`project-kickoff-hermes-weekly-health-enhancement.md`
- 修正版样例页面：`project-kickoff-education-fund-weekly-page.md`

第一版脚本能力是：
- 读取项目想法
- 生成固定结构 kickoff 草稿
- 拒绝覆盖已有页面

这一步证明了：
- 一句项目想法 -> 一页 kickoff artifact 在工程上是稳定可行的

但它还没有证明：
- 这个 artifact 足够支撑后续推进

## Step 5: review
review 阶段抓到了关键问题，而这些问题如果只看“能跑”，很容易被忽略：

### 发现的问题
1. frontmatter 脆弱
   - `title` 直接写入 YAML，遇到冒号、特殊字符、换行有风险
2. `idea` 没有清洗
   - 多行输入可能污染页面结构和内容质量
3. `slug` 校验过松
   - 会导致文件命名不稳
4. 正文内容过于通用
   - `Problem`、`Scope`、`Immediate Next Step` 太像统一话术

### 对应修正
- 加入 YAML 安全 title quoting
- 压平多行 idea 输入
- 把 slug 收紧为小写字母、数字、连字符
- 对 `Problem` / `Who This Helps` / `Scope` / `Immediate Next Step` 做轻量 idea-aware 分支

这一轮直接证明了 review 的价值：
- 它抓到的不是“脚本跑不起来”这种显性错误，而是“现在还不足以进入下一步价值验证”的结构问题

## Step 6: QA
QA 用 3 个真实样例验证了这个 intake 路径：
- `做一个 Hermes 每周健康检查增强版`
- `做一个教育基金周报页面`
- `做一个 skill 安装审查流程页`

### QA 结果
#### 结构稳定性
- 3 个页面都包含完整的 10 个固定 section
- 页面结构完全一致
- 都能稳定写到 `~/wiki/queries/`

#### 内容贴合度
- 健康检查类：可用
- 周报页面类：可用，而且效果最好
- skill 安装审查流程页：勉强可用，但“流程页”的意图被“审查类”分支抢先命中，说明规则优先级还有边界问题

#### 最终判定
- `DONE_WITH_CONCERNS`
- 这条 intake 路径值得保留
- 但规则分支优先级还可以再微调，尤其是流程类与审查类关键词冲突时

## What the Validation Proved
这次验证真正证明了 4 件事：

1. 把 gstack 的 5-skill lane 写进 wiki，不是纯文档工作
   - 它确实能改变项目推进过程

2. 这条 lane 最有价值的环节，是连续收窄
   - office-hours 收窄问题
   - CEO review 收窄范围
   - Eng review 收窄实现边界

3. review 和 QA 不是装饰步骤
   - review 抓到了“能跑但还不够用”的问题
   - QA 抓到了真实分类边界问题

4. 对 Hermes 来说，这条 lane 很适合“小项目启动”场景
   - 先把模糊想法变成 kickoff artifact
   - 再决定是否进入更深的计划、实现或自动化

## Which Steps Mattered Most
这次案例里，边际价值最高的步骤是：
- `gstack-office-hours`
- `gstack-plan-eng-review`
- `gstack-review`

原因：
- office-hours 负责砍掉过宽问题定义
- eng-review 负责把想法压成脚本、路径和参数
- review 负责阻止“能跑即成功”的误判

相对来说：
- `gstack-plan-ceo-review` 仍然有价值，但在这种很小的项目里，主要作用是进一步收窄，而不是改写方向
- `gstack-qa` 的价值在于发现分类边界，而不是发现低级 bug

## Current Boundary of the Kickoff Tool
当前 `project_kickoff.py` 的合理定位是：
- Hermes 小项目启动入口
- 一句想法 -> 一页 kickoff 草稿
- 让后续 plan / implementation / review 有统一输入

它目前不应该承担：
- 自动分类
- 自动索引
- 自动日志
- 自动计划生成
- 自动外部研究
- 完整项目编排

## Reusable Takeaway
这次验证最重要的复用结论是：
- 对 Hermes 这类已经有 wiki / skill / cron / memory 分层的系统来说，真正欠缺的往往不是更多能力，而是一个更稳定的项目启动入口
- gstack 的 5-skill lane 很适合被用来验证这种入口是否真的有价值
- 如果一个想法不能经过 office-hours、review、QA 后仍然站得住，那它就不应该太早被制度化

## Next Step
基于这次验证，更合理的下一步是二选一：
1. 保持 `project_kickoff.py` 为最小入口工具，只做一两处小修正
2. 在确认高频复用后，再考虑把它包装成 skill 或 quick command

不合理的下一步是：
- 立即把它扩成模板系统
- 立即接索引/日志/分类自动化
- 立即把 kickoff -> plan -> cron 整条链一口气做完

## Related
- [[gstack-project-execution-lane]]
- [[hermes-knowledge-base-operating-flow]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-optimization-sample-case]]
