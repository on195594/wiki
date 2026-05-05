---
title: Hermes optimization sample case (April 2026)
source_type: transcript_summary
captured_at: 2026-04-16
status: raw
---

# Source summary

这份 raw 材料用于把“最近优化 Hermes 的过程”编译成一个可复用样板案例。
材料来源包括：
- 近期会话总结
- 当前已验证存在的 Hermes 配置与产物
- 当前知识库内已沉淀的流程页面

## 主要过程

### 1. 修复并收敛晨报 quick command
- 已验证存在脚本：`/home/lin/.hermes/scripts/utils/wd.py`
- 已验证 config 中的 quick command：
  - `wd:`
  - `command: python3 ~/.hermes/scripts/utils/wd.py`
- 这一步的核心优化是：
  - 找到 `{args}` 残留导致的调用链问题
  - 把脚本输出格式收敛成可直接使用的晨报文本
  - 让 quick command 与脚本行为重新对齐

### 2. 修复晨报定时任务投递路径
- 当前 cron job：`晨报`
- job_id：`664f52b09c76`
- schedule：`0 7 * * *`
- deliver：`telegram:6346028803`
- last_status：`ok`
- last_delivery_error：`null`
- 这一步的核心优化是：
  - 发现任务实际执行成功，但只投递到 `local`
  - 把 deliver 更新到 Telegram 私聊
  - 手动触发并验证执行成功

### 3. 初始化 Hermes 知识库基础设施
- 已创建知识库根目录：`/home/lin/wiki`
- 已对齐：`skills.config.wiki.path: ~/wiki`
- 已对齐：`OBSIDIAN_VAULT_PATH=/home/lin/wiki`
- 已创建：
  - `SCHEMA.md`
  - `index.md`
  - `log.md`
  - `raw/`
  - `entities/`
  - `concepts/`
  - `comparisons/`
  - `queries/`
- 这一步的核心优化是：
  - 把知识沉淀从纯对话切换到文件化长期层

### 4. 建立知识库规范层
近期已沉淀多篇正式页面，覆盖：
- 知识库整体架构
- memory / skills / wiki 边界
- 检索优先级与回答路径
- 页面写作规范
- lint / 健康检查规范
- 端到端操作流
- Dijkstra 与 AI 编程对照
- Hermes AI workflow formalization principles

### 5. 把方法论提升为技能
已创建 skill：`hermes-formalized-ai-workflow`
作用：
- 把模糊任务尽快转成 memory / skill / wiki / todo 等正确 artifact
- 强制验证
- 持续压缩上下文，而不是无限扩展聊天

## 可复用产物
- Quick command 脚本：`wd.py`
- 定时任务：晨报 cron job
- 本地 wiki：`~/wiki`
- formalized workflow skill：`hermes-formalized-ai-workflow`

## 核心模式
这轮 Hermes 优化不是单点修补，而是同一模式的重复应用：
- 先发现漂移或歧义
- 再收窄接口
- 然后把结果落成可验证 artifact
- 最后通过 wiki / skill / config / cron 留下长期资产
