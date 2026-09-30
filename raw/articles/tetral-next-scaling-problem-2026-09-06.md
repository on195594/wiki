---
title: The Next Scaling Problem
author: Yang Li
source_type: article
source_url: https://tetral.ai/blog/the-next-scaling-problem/
published_at: 2026-09-06
captured_at: 2026-09-29
type: raw-source
status: captured
---

# The Next Scaling Problem — source capture

## Source boundary

Tetral 创始人 Yang Li 对其云端 Agent 架构的第一手技术叙述。直接从原文页面提取了从正文首节到结语的完整文字；导航和页脚已剔除，交互图只保留文本说明，未核验图像细节。以下为结构化摘录与释义，**不是逐字全文**；实现、性能与恢复保证均为作者对个人 k3s 集群 Alpha 的陈述，未独立复现。原文以 `source_url` 为准。

## 原文结构与可回查要点

- **从沙箱捆绑转向分离**：Anoma 最初把 Agent 循环放在 E2B 沙箱内，扩容单位遂成为沙箱。Tetral 改为让运行时提供持续的 Agent 计算，让沙箱作为独立、按需分配的执行资源；原文强调计算机应被 Agent 调用，而非成为 Agent 的居所。
- **运行时边界**：Gateway 管模型格式、连接和凭据；PostgreSQL 保存会话事实，Bridge 校验归属、顺序与状态转移；Queue 管租约、重试、取消、死信和投递；Sandbox Service 管计算机激活、物化及执行。Public API 接受输入，Event Stream 公开有序记录，二者均不执行 Agent。运行时通过无数据库/网络 I/O 的 reducer 推导每个 thread 下一步，进程本身不持有持久会话状态。
- **先提交再执行**：可推进线程或产生外部义务的声明必须先经 Bridge 以稳定身份提交并获得回执，再调度模型或工具。事件日志 `session_events`、上下文投影 `session_messages` 和幂等回执 `session_bridge_operations` 分工；压缩只影响未来模型加载的上下文，不删除旧执行记录。模型流在 Pod 丢失后不续接，而标记失败并从已提交边界恢复。作者明确指出：该协议不能使任意外部系统事务化，模糊结果不得静默推进。
- **可靠投递与隔离**：输入、Inbox 项与 Queue 作业在同一 PostgreSQL 事务登记；`pg_notify` 只作唤醒提示，轮询兜底。运行时接受输入与线程实际处理分开记录，绑定 generation 和 Pod UID 防止超时后仍活跃的旧运行时被误判为失效。Gateway 在运行时/沙箱之外注入提供方凭据；已选凭据缺失、撤销、归档或无法解密时拒绝，不静默回退；未选择凭据的会话可使用平台密钥池。
- **两种并行与授权**：同一 session 内的 child thread 拥有独立有序上下文；多个 session 可选用同一 workspace 的资源但不共享执行历史。凭据隔离不等于授权。`approve_for_me` 先把操作作为提议评估，提交审查决定后再由 Tool Gate 决定是否接受为可调度工具调用；审查失败不能自行变成许可。
- **产物与瓶颈**：作者主张其他 Agent 对候选产物和证据提出对抗性质疑，再由人决定是否并入共享 workspace；这是一项产品设想，不是已证实的协作增益。增长压力还会转向编译/验证、沙箱激活、存储、Git 托管及模型调用周边。作者举例称其开发机某条集成路径耗时约 7–8 分钟、完整验证约半小时；这不是跨环境基准。

## 成熟度与适用限制

作者明确称 Tetral 仍是个人 k3s 集群上的 Alpha：运行时放置尚不感知容量，准入—队列压力—扩容反压未打通，持续多节点恢复未被证明，滚动发布缺乏优雅排空并会中断进行中的轮次。本文可用于识别云端长程 Agent 的边界与失败窗口，不能作为生产可靠性证明，也不要求一般单机 Agent 复制整套服务拓扑。
