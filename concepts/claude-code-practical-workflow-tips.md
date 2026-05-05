---
title: Claude Code Practical Workflow Tips
created: 2026-04-17
updated: 2026-04-17
type: concept
tags: [claude-code, agent, workflow, automation, browser]
sources: [raw/articles/xda-claude-code-practical-tips-2026-04-13.md]
status: stable
---

# Claude Code Practical Workflow Tips

## Summary
这页提炼 XDA 对 Boris Cherny 工作方式的总结：Claude Code 的实际效率不取决于“会不会写更高级的提示词”，而取决于是否把它放进一个完整的 agent workflow 里——能侧边提问、能自己验证结果、能自动重复执行、能跨目录拿到全局上下文、还能跨设备持续操作。

## Core ideas
### 1. Side questions should not break the main task
`/btw` 的价值不是省一次新开会话，而是保留当前任务上下文，让 Claude 在不中断主流程的情况下回答一个短问题。

适合：
- 问 Claude 刚才看过哪个文件
- 追问某个中间决策
- 临时补一条不会改变主任务方向的小问题

不适合：
- 已经改变任务目标的问题
- 需要独立上下文的大分支工作

### 2. Verification beats description loops
文章最重要的点是：不要让人类持续扮演 Claude 的眼睛。

如果 Claude 只能生成代码、再由人类回报“点按钮后发生了什么”，那整个过程会退化成低效的描述循环。浏览器扩展的价值在于把 build-test-verify 闭环交还给 Claude 自己。

这对以下场景尤其关键：
- Web 页面开发
- 浏览器扩展开发
- 依赖 DOM、console、点击行为的调试

核心原则：
- 能给 Claude 真实验证环境，就不要只给文字反馈
- 能让它自己看到错误，就不要靠你转述错误

### 3. Repeated prompts should become loops or schedules
如果一个 prompt 需要反复人工重跑，它就已经接近自动化候选项了。

`/loop` 适合：
- 当前 session 内持续轮询
- 临时监控
- 需要边看边调的短周期任务

`/schedule` 适合：
- 持久运行的后台任务
- 不依赖当前 terminal 存活的自动化
- 更接近 agent dispatcher 的工作流

判断标准：
- 任务是否重复
- 输入模式是否稳定
- 结果是否主要是筛选、整理、转发、汇报

### 4. Claude needs the right filesystem scope upfront
`--add-dir` 的本质不是少点几次授权，而是让 Claude 在开始时就拿到更完整的问题边界。

适合：
- 参考旧项目实现
- 多仓库联动开发
- 拆分工程下的跨目录修改

设计启发：
- agent 的表现常常不是输在能力，而是输在视野太窄
- 工作目录权限模型，本质上也是上下文工程的一部分

### 5. Claude Code is a portable agent, not just a terminal tool
移动端、`/teleport`、`/remote-control` 和 Dispatch 共同说明：Claude Code 更像一个可跨设备延续的工作代理，而不是只能坐在桌前用的 CLI。

这意味着它更适合：
- 碎片化处理轻任务
- 远程触发或检查工作流
- 在不同设备间延续同一个任务状态

## Distilled operating rules
1. 临时追问优先用不会打断主任务的机制
2. 任何可视化产物，都优先给 Claude 验证环境
3. 重复 prompt 尽快升级成 loop 或 schedule
4. 跨项目任务一开始就给足目录访问范围
5. 把 Claude Code 当 agent workflow 使用，而不是单轮代码生成器

## What this changes in practice
对工程和 agent 使用者来说，这篇文章的真正价值在于把关注点从“prompt 技巧”转向“工作流设计”：
- 问题不是 Claude 能不能写出代码
- 问题是 Claude 能不能验证、持续执行、拿到足够上下文、并在不同设备上延续任务

如果这四件事没解决，再多 prompt 技巧也只是局部优化。

## Limits
- 这套方法更适合有持续工作流的人，不一定适合一次性小任务。
- 自动 loop / schedule / remote control 带来便利，也意味着更高的权限与误操作风险。
- 浏览器验证闭环主要对 Web 类任务收益最高，对纯后端或纯文本任务不一定同等重要。

## Related
- [[wiki-ingestion-workflow]]
- [[hermes-ai-workflow-formalization-principles]]
- [[hermes-context-engineering-design-priorities]]
- [[index]]
- [[log]]
