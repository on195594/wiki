---
title: Claude Code's creator keeps sharing tips, and they all made my experience better
author: XDA
source_type: article
source_url: https://share.google/eo3foT11UHbV9SLim
published_at: 2026-04-13
captured_at: 2026-04-17
status: raw
---

# Summary capture

## Core claim
这篇文章的核心观点是：Claude Code 的体验提升，主要不来自更花哨的 prompt，而来自一组更接近 agent workflow 的使用方式——让它在不中断任务的前提下回答临时问题、具备浏览器验证能力、自动循环执行任务、跨目录工作，以及在手机与不同设备之间持续操作。

## Key points
- `/btw` 允许在 Claude 正在执行任务时插入一个临时问题，不打断主任务，并继承当前会话上下文。
- Claude in Chrome 扩展解决了“Claude 看不到自己构建结果”的问题，让它可以直接在浏览器中检查、交互和验证输出。
- `/loop` 和 `/schedule` 用来把重复 prompt 转成自动化工作流：
  - `/loop` 只在当前 session 存活时运行
  - `/schedule` 可做更持久的桌面或云端任务
- `--add-dir` 允许 Claude Code 一开始就访问多个目录，减少跨项目工作时反复授权。
- Claude Code 并不局限于 terminal，还支持移动端、跨设备会话迁移、远程控制和 Dispatch。

## Important facts
- `/btw` 在 2026 年 3 月引入。
- Claude in Chrome 扩展目前为 beta，面向 Claude 付费用户开放。
- `/schedule` 分为：
  - Desktop tasks：应用开着时在本机运行
  - Cloud tasks：设备关闭时仍可在 Anthropic 服务器上运行
- 文中给出的多目录访问示例：
  - `claude --add-dir ~/Projects/old-extension`
- Boris Cherny 建议把重复工作流逐步转成 skills 和 loops。

## Practical takeaway
文章真正想强调的不是“记住几个命令”，而是把 Claude Code 从单次问答工具，升级成一个可验证、可自动重跑、可跨目录、可跨设备的持续工作代理。对工程场景来说，最重要的动作是给它验证闭环和自动化执行能力，而不是只优化 prompt 写法。

## Applicability
- 前端或 Web 工程：需要浏览器验证闭环
- 重复性巡检或消息整理：适合 `/loop` / `/schedule`
- 多仓库/多目录协作开发：适合 `--add-dir`
- 远程处理轻量工作流：适合 mobile app、`/teleport`、`/remote-control`、Dispatch

## Limits
- 这是一篇体验型文章，不是严格 benchmark 或官方文档。
- 结论高度依赖作者个人使用场景，偏向正面推荐。
- 文中没有系统讨论 token 成本、失败模式、权限边界和自动化误操作风险。