---
title: RAG Isn’t Enough — I Built the Missing Context Layer That Makes LLM Systems Work
author: Towards Data Science
source_type: article
source_url: https://share.google/Dci3x1RofvgbGpYqZ
published_at: 2026-04-14
captured_at: 2026-04-16
status: raw
---

# Summary capture

## Core claim
这篇文章的核心观点是：传统 RAG 只能解决“找到相关文档”，但真实可用的 LLM 系统还需要一层独立的 context engineering，用来显式管理进入上下文窗口的信息、顺序、压缩方式和 token 预算。

## Key points
- 真正的问题不是 retrieval 本身，而是“最终什么进入 context window”。
- Prompt engineering 解决“怎么问”，RAG 解决“找什么”，context engineering 解决“最后放什么进去”。
- 当对话轮次增加、知识库变大、历史变长后，普通 RAG 很快会遇到：
  - 相关文档被无关历史挤掉
  - prompt 超出 token 限制
  - 重复文档浪费窗口
  - 旧上下文持续污染新回答
- 作者提出的完整流水线包括：
  1. Retriever
  2. Re-ranker
  3. Memory with exponential decay
  4. Context compression
  5. Token budget enforcement
- Retriever 支持 keyword、TF-IDF、hybrid；作者偏向 hybrid，因为它兼顾关键词匹配与语义相似度。
- Re-ranker 在检索分数之外，再按标签/领域相关性调整优先级。
- Memory 层不是机械保留全部对话，而是让重要信息保留、旧信息衰减。
- Compression 层在 token 不够时压缩内容，而不是粗暴截断。
- Token budget enforcement 会明确分配 system prompt、history、retrieval 各自的预算。

## Practical takeaway
作者的判断是：LLM 系统从 demo 走向 production，关键不再只是“继续加检索”，而是把记忆、压缩、重排、预算控制做成一层正式架构。没有这层，RAG 系统一复杂就会失效。

## Good fit
- 多轮聊天机器人
- 大知识库 RAG 系统
- 需要长期记忆的 AI copilot / agent
- 上下文复杂、需要持续交互的生产型系统

## Not worth it for
- 单轮问答
- 小知识库简单检索
- 强低延迟场景
- 高确定性、强审计、以关键词检索为主的工作流
