---
title: How Agents Manage Other Agents: Four Subagents Patterns in 2026
created: 2026-05-07
type: raw-source
tags: [agent, subagent, multi-agent, orchestration, hermes, workflow]
source_url: https://www.philschmid.de/subagent-patterns-2026
original_url: https://share.google/zcM4oRhk5H7Z5Qj0L
author: Phil Schmid
published: 2026-05-05
extracted: 2026-05-07
extraction_method: share.google exact-title resolution plus Jina Reader canonical article capture
status: captured
---

# How Agents Manage Other Agents: Four Subagents Patterns in 2026

## Provenance
- Source URL: https://www.philschmid.de/subagent-patterns-2026
- Original share link: https://share.google/zcM4oRhk5H7Z5Qj0L
- Author: Phil Schmid
- Published: 2026-05-05
- Captured: 2026-05-07
- Extraction method: `share.google` link resolved by exact-title search; canonical article fetched through Jina Reader.
- Gemini summary output: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260507-094718-How-Agents-Manage-Other-Agents-Four-Subagents-Patterns-in-2026-—-https-www.phils-160538-490197803-summary.md`
- Limitations: Jina Reader output was used as the full-text capture and may include minor site navigation/Markdown conversion artifacts.

## Why this source matters
This article is useful for Hermes because it gives a lifecycle-control ladder for subagent orchestration: one-shot calls, fan-out/fan-in, persistent agent pools, and direct agent teams. It helps decide when `delegate_task`-style isolation is enough and when a more complex orchestration model would be over-designed.

## Gemini summary

标题：How Agents Manage Other Agents: Four Subagents Patterns in 2026

一句话结论：
随着大模型规划和工具使用能力的提升，主代理管理子代理的架构演进出四种模式（内联工具、扇出、代理池、团队），主代理对子代理生命周期的控制力逐级减弱，但对模型推理能力的要求逐级增高。

核心观点与论证：
- 观点：内联工具（Inline Tool）是最简单且最常用的模式，适用于独立自包含的任务。
  依据/论证：主代理将调用子代理视为调用 read_file 等普通函数。通过 call_agent 工具同步阻塞获取结果，或异步获取代理 ID 后等待通知注入。主代理不管理子代理生命周期，该模式支持能力较弱的模型，但缺点是无法中途干预、追问或检查进度。
- 观点：扇出模式（Fan-Out）通过分离生成与等待步骤，实现了多任务并发执行与主代理的穿插工作。
  依据/论证：提供 spawn_agent（立即返回 ID）和 wait_agent（阻塞并批量收集结果）两个工具。主代理可并行下发多个任务并穿插执行自身逻辑后再统一等待，适用于多项独立任务，但仍属“阅后即焚”模式，模型必须具备判断“何时等待”的推理能力。
- 观点：代理池模式（Agent Pool）通过长生命周期的状态保持和消息传递，支持多步协作工作流。
  依据/论证：引入 spawn、send、wait、list、kill 等丰富工具面，子代理具备对话记忆。主代理扮演协调者，可多次向同一子代理发指令并在不同专家间路由信息。要求大模型具备跨回合追踪多代理状态的能力，小模型容易混淆上下文或忘记销毁代理。
- 观点：团队模式（Teams）允许代理间直接通信，适用于协调逻辑超出单代理管理上限的超大任务。
  依据/论证：子代理自身拥有 send_message 工具和跨代理寻址能力。主代理仅负责设定角色、组建团队并退居幕后监控。该模式要求所有参与节点都是前沿大模型，且面临循环死锁（A等B，B等A）、文件编辑冲突及调试困难等严重的基础设施挑战。

关键细节：
- 模式1（内联工具）应用案例：主代理调用 security-reviewer 审查 PR #42，工具直接返回了2个具体的安全漏洞（如登录处理程序缺少 HttpOnly 标志、/api/users 未校验 Token）。
- 模式2（扇出）应用案例：主代理并发拉起 backend-engineer（重构 JWT）和 test-writer（更新测试），在调用 wait_agent 等待结果之前，主代理还能自主调用 read_file 阅读 docs/auth-spec.md。
- 模式3（代理池）应用案例：撰写 WebAssembly 性能博客时，主代理先让 researcher 找数据，再发给 writer 起草，最后把草稿发回给一直在线并保留了初期参考来源的 researcher 进行 1.5x 性能数据的事实核查。
- 模式4（团队）的通信基建细节：子代理之间通过层级路径（如 /root/planner 发给 /root/implementer）、基于文件的邮箱或 IPC 协议相互寻址，主代理通过带有 timeout 的 wait_agent 或 list_agents 轮询状态。
- 原文包含明确的来源链接：Source URL: https://www.philschmid.de/subagent-patterns-2026 以及 Original share.google URL: https://share.google/zcM4oRhk5H7Z5Qj0L，这些来源标识了作者 2026-05-05 发布的这篇文章的原始出处。

可信度与局限：
- 较强证据：文章对各模式下大模型 JSON 工具调用格式（如 tool_calls 中的具体参数和返回体结构设计）的拆解、同步/异步流程的对比，以及 spawn 与 wait 的解耦逻辑，具备极强的工程落地可行性。
- 推演与主观解读：关于“前沿模型勉强能处理 2-4 个交互代理（okayish）”以及“今天需要 4 个代理协同的任务，明天可能只需 1 个更强的单体模型解决”的论断，属于基于技术演进直觉的经验性预判，缺乏严谨的数据论证。

对我的启发：
- 多智能体架构设计不应盲目追求复杂的去中心化直接通信。绝大多数需求应退回到最基础的“函数调用（Inline Tool）”，只有在明确出现并发提效需求或跨步骤状态强依赖时，才按需向上升级模式，这能大幅降低系统故障率和模型上下文开销。

可执行建议：
- 审查现有的 Agent 调度代码，如果任务没有状态依赖，强制移除驻留内存的长期子代理，重构为每次重新初始化的 call_agent 调用（即退回模式1）。
- 若必须采用代理池模式（模式3），需在框架层面白盒实现子代理的垃圾回收（GC）机制或设置最大存活回合数，不要完全依赖大模型主动调用 kill_agent，以防资源泄露。
- 暂缓在核心生产链路部署团队模式（模式4），除非底层路由网关已经实现了可靠的环路检测（cycle detection）和基于超时的死锁熔断机制。

## Extracted source text

Title: How Agents Manage Other Agents: Four Subagents Patterns in 2026

URL Source: http://www.philschmid.de/subagent-patterns-2026

Published Time: 2026-05-05

Markdown Content:
# How Agents Manage Other Agents: Four Subagents Patterns in 2026

[![Image 1: logo](http://www.philschmid.de/_next/image?url=%2Fstatic%2Flogo.png&w=48&q=75)Philschmid](http://www.philschmid.de/)

Search⌘k

[Blog](http://www.philschmid.de/)[Projects](http://www.philschmid.de/projects)[Newsletter](http://www.philschmid.de/cloud-attention)[About Me](http://www.philschmid.de/philipp-schmid)Toggle Menu

# How Agents Manage Other Agents: Four Subagents Patterns in 2026

May 5, 2026 11 minute read

[Last year I wrote about the rise of subagents](https://www.philschmid.de/the-rise-of-subagents) and why isolating tasks into focused agents with their own context, tools, and instructions improves reliability. That post covered _what_ subagents are and _why_ you want them. Since then, models have gotten better at planning, tool use, and multi-step instructions. That opens up patterns that were previously too fragile: agents managing pools of persistent workers, or agents messaging each other directly.

Here are four patterns, ordered by the level of control the main agent has over the subagent lifecycle.

## [](http://www.philschmid.de/subagent-patterns-2026#1-inline-tool-subagent-as-a-function-call)1. Inline Tool: Subagent as a Function Call

The simplest pattern. The main agent calls a tool that spawns a subagent and returns the result as the tool response. From the main agent's perspective, calling a subagent is identical to calling `read_file` or `run_command`.

![Image 2: Pattern 1 diagram](http://www.philschmid.de/static/blog/subagent-patterns-2026/pattern%201.png)

The main agent has a tool, e.g. `call_agent`. It sends a task, gets a result. The subagent runs in its own context with its own tools and instructions. The main agent never manages the subagent's lifecycle directly.

```
[
  { "role": "user", "content": "Review PR #42 for security issues" },
  { "role": "assistant", "tool_calls": [
    { "name": "call_agent", "arguments": { "task": "Review PR #42 for security issues. Focus on auth changes.", "agent": "security-reviewer", "tools": ["read_file", "search_code"] } }
  ]},
  { "role": "tool", "name": "call_agent", "content": "Found 2 issues: 1) Auth token not validated in /api/users endpoint. 2) Session cookie missing HttpOnly flag in login handler." },
  { "role": "assistant", "content": "The review found 2 security issues..." }
]
```

This pattern has a sync/async distinction at the tool level, because the tool itself can either block or return immediately:

**Sync (above):** The tool call blocks. The main agent's turn is paused until the subagent finishes. The result arrives as a normal tool response.

**Async:** The tool returns immediately with an agent ID. The subagent's result is injected into the conversation as a notification message when it finishes. The main agent can do other tool calls before the result arrives.

```
[
  { "role": "user", "content": "Review PR #42 and also check the CI logs" },
  { "role": "assistant", "tool_calls": [
    { "name": "call_agent", "arguments": { "task": "Review PR #42 for security issues", "agent": "security-reviewer", "background": true } },
    { "name": "read_file", "arguments": { "path": "ci/logs/latest.txt" } }
  ]},
  { "role": "tool", "name": "call_agent", "content": "agent_id: agent-x1. Running in background." },
  { "role": "tool", "name": "read_file", "content": "Build passed. 142 tests green." },
  { "role": "assistant", "content": "CI looks clean. Waiting for the security review..." },
  { "role": "user", "content": "<notification agent_id='agent-x1' status='completed'>Found 2 issues: ...</notification>" },
  { "role": "assistant", "content": "The security review found 2 issues..." }
]
```

In sync, the tool response contains the result. In async, the tool response contains an ID, and the result arrives later as an injected user message.

**When to use this:** Self-contained work. Research lookups, code reviews, file analysis, test generation. Most subagent use cases start and stay here.

**Limitations:** Works with any model that supports tool use, including smaller and cheaper ones. Results arrive as a single tool response (sync) or as an injected notification message (async). No way to send follow-up instructions, check progress, or cancel early. If the subagent misunderstands the task, you find out when the result comes back.

## [](http://www.philschmid.de/subagent-patterns-2026#2-fan-out-spawn-agents-and-wait-for-results)2. Fan-Out: Spawn Agents and Wait for Results

The main agent spawns subagents and collects results using a `wait_agent` tool. Unlike the inline tool, spawning and collecting are separate steps. `spawn_agent` always returns immediately. The model decides what to do next: call `wait_agent` right away, do its own work first, or spawn more agents before waiting.

![Image 3: Pattern 2 diagram](http://www.philschmid.de/static/blog/subagent-patterns-2026/pattern%202.png)

Two tools: `spawn_agent` dispatches work and returns immediately with an ID. `wait_agent` blocks until one or more agents finish.

The model controls sequencing. It can spawn agents and call `wait_agent` immediately (effectively synchronous), or interleave its own work first:

```
[
  { "role": "user", "content": "Refactor the auth module and update all related tests" },
  { "role": "assistant", "tool_calls": [
    { "name": "spawn_agent", "arguments": { "task": "Refactor the auth module to use JWT tokens", "agent": "backend-engineer" } },
    { "name": "spawn_agent", "arguments": { "task": "Update all auth-related tests for the new JWT flow", "agent": "test-writer" } },
    { "name": "read_file", "arguments": { "path": "docs/auth-spec.md" } }
  ]},
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-a (backend-engineer). Running." },
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-b (test-writer). Running." },
  { "role": "tool", "name": "read_file", "content": "# Auth Spec\nJWT tokens with RS256..." },
  { "role": "assistant", "content": "I've kicked off both tasks. The auth spec confirms we should use RS256." },
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": { "timeout": 300 } }]},
  { "role": "tool", "name": "wait_agent", "content": "2 agents completed:\n- agent-a: Refactored 3 files (auth.ts, middleware.ts, config.ts)\n- agent-b: Updated 12 tests, all passing" },
  { "role": "assistant", "content": "Both tasks are done. The auth module now uses JWT..." }
]
```

The model spawned two agents and read a file in the same tool call, then decided to wait. A different model might call `wait_agent` immediately after spawning, or do several reads first. The tool surface is the same; the model decides the interleaving.

The difference from Pattern 1: the model controls when to collect. It can spawn 5 agents in parallel, do its own file reads, then call `wait_agent`. `wait_agent` can act as a global mailbox that wakes up on subagent completion and returns all available results.

**When to use this:** Multiple independent tasks that can run concurrently. The main agent does not need intermediate results from one subagent to start another.

**Limitations:** The model needs to correctly decide _when_ to wait. A model that calls `wait_agent` immediately after every spawn gets no benefit over Pattern 1. The value depends on the model's ability to interleave its own work between spawn and wait. Results are collected in batch via `wait_agent`, which returns all completed agent outputs since the last call. Still fire-and-forget: no way to send follow-up instructions or course-correct mid-task to subagents.

## [](http://www.philschmid.de/subagent-patterns-2026#3-agent-pool-persistent-agents-with-messaging)3. Agent Pool: Persistent Agents with Messaging

The main agent spawns long-lived subagents and communicates with them through messages. Agents persist across interactions. The main agent can send follow-up instructions, check status, and coordinate work between agents.

This requires a richer tool surface: `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, `kill_agent`.

![Image 4: Pattern 3 diagram](http://www.philschmid.de/static/blog/subagent-patterns-2026/pattern%203.png)

Unlike Pattern 2, agents here are **stateful and interactive**. The main agent sends a message, gets a response, and sends another message to the same agent. The agent retains its full conversation history. This supports multi-step workflows where the main agent coordinates between specialists.

The model controls whether it works with one agent at a time (sequential) or messages multiple agents between waits (parallel). It can send to the researcher and writer simultaneously, or wait for the researcher first:

```
[
  { "role": "user", "content": "Write a blog post about WebAssembly performance" },
 
  { "role": "assistant", "tool_calls": [
    { "name": "spawn_agent", "arguments": { "role": "researcher", "tools": ["web_search", "read_url"] }},
    { "name": "spawn_agent", "arguments": { "role": "writer", "tools": ["write_file", "read_file"] }}
  ]},
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-r (researcher)" },
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-w (writer)" },
 
  { "role": "assistant", "tool_calls": [
    { "name": "send_message", "arguments": { "to": "agent-r", "message": "Research WebAssembly performance benchmarks. Find 5 sources with concrete numbers." } },
    { "name": "send_message", "arguments": { "to": "agent-w", "message": "Outline a blog post structure about WebAssembly performance. 4 sections." } }
  ]},
  { "role": "tool", "name": "send_message", "content": "Delivered to agent-r" },
  { "role": "tool", "name": "send_message", "content": "Delivered to agent-w" },
 
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": {} }]},
  { "role": "tool", "name": "wait_agent", "content": "agent-w responded: Outline ready: intro, benchmarks, real-world, conclusion" },
 
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": {} }]},
  { "role": "tool", "name": "wait_agent", "content": "agent-r responded: Found 5 sources: 1) Chrome benchmark shows 1.2x native speed..." },
 
  { "role": "assistant", "tool_calls": [{ "name": "send_message", "arguments": { "to": "agent-w", "message": "Fill in your outline using these sources: 1) Chrome benchmark shows 1.2x native speed..." } }]},
  { "role": "tool", "name": "send_message", "content": "Delivered to agent-w" },
 
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": {} }]},
  { "role": "tool", "name": "wait_agent", "content": "agent-w responded: Draft complete. Title: 'WebAssembly Is Faster Than You Think'..." },
 
  { "role": "assistant", "tool_calls": [{ "name": "send_message", "arguments": { "to": "agent-r", "message": "Fact-check this draft against your sources: 'WebAssembly Is Faster Than You Think'..." } }]},
  { "role": "tool", "name": "send_message", "content": "Delivered to agent-r" },
 
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": {} }]},
  { "role": "tool", "name": "wait_agent", "content": "agent-r responded: 2 corrections: paragraph 3 cites 2x speed but source says 1.5x..." },
 
  { "role": "assistant", "tool_calls": [
    { "name": "send_message", "arguments": { "to": "agent-w", "message": "Apply these corrections: paragraph 3 should say 1.5x not 2x..." } },
    { "name": "kill_agent", "arguments": { "agent_id": "agent-r" }}
  ]},
  { "role": "tool", "name": "send_message", "content": "Delivered to agent-w" },
  { "role": "tool", "name": "kill_agent", "content": "agent-r terminated" },
 
  { "role": "assistant", "content": "Here is the final post..." }
]
```

`agent-r` is messaged twice (research, then fact-check) and retains its sources from the first task. The model sent work to both agents in parallel at the start, then coordinated sequentially for the fact-check. A different model might serialize everything. The tools are identical; the model controls the orchestration.

Results arrive per-message via `wait_agent`. Each call to `wait_agent` returns the next agent response, so the main agent processes results incrementally and can adjust its next message based on what came back.

**When to use this:** Multi-step workflows where agents need to collaborate. The main agent routes information between specialists.

**Limitations:** The main agent must track multiple agent states, decide when to send follow-ups vs wait, and route information correctly. Smaller models lose track of which agent has which context, or forget to call `kill_agent` when done. Frontier models might handle 2-4 agents okayish.

## [](http://www.philschmid.de/subagent-patterns-2026#4-teams-agents-talk-to-each-other)4. Teams: Agents Talk to Each Other

Agents message each other directly without going through the main agent. The main agent sets up the team, defines roles, and steps back. Agents coordinate among themselves using direct messaging or a shared mailbox.

![Image 5: Pattern 4 diagram](http://www.philschmid.de/static/blog/subagent-patterns-2026/pattern%204.png)

The tool surface includes cross-agent addressing. Each agent gets `send_message` in its own tool set and can address other agents by name or path.

From the main agent's perspective, the conversation is short. It sets up the team, kicks off the planner, and waits for the final report. The model can choose to wait silently, or periodically check in using `list_agents`:

```
[
  { "role": "user", "content": "Build feature X" },
 
  { "role": "assistant", "tool_calls": [
    { "name": "spawn_agent", "arguments": { "role": "planner", "tools": ["read_file", "search_code", "send_message"] } },
    { "name": "spawn_agent", "arguments": { "role": "implementer", "tools": ["read_file", "write_file", "run_command", "send_message"] } },
    { "name": "spawn_agent", "arguments": { "role": "reviewer", "tools": ["read_file", "search_code", "send_message"] } }
  ]},
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-p (planner)" },
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-i (implementer)" },
  { "role": "tool", "name": "spawn_agent", "content": "Spawned agent-v (reviewer)" },
 
  { "role": "assistant", "tool_calls": [{ "name": "send_message", "arguments": { "to": "agent-p", "message": "Plan and coordinate feature X. Your teammates: agent-i (implementer), agent-v (reviewer). Message them directly. Report back to me when done." } }]},
  { "role": "tool", "name": "send_message", "content": "Delivered to agent-p" },
 
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": { "timeout": 60 } }]},
  { "role": "tool", "name": "wait_agent", "content": "Timed out. No agents responded." },
 
  { "role": "assistant", "tool_calls": [{ "name": "list_agents", "arguments": {} }]},
  { "role": "tool", "name": "list_agents", "content": "agent-p: running, agent-i: running, agent-v: idle" },
 
  { "role": "assistant", "tool_calls": [{ "name": "wait_agent", "arguments": { "timeout": 120 } }]},
  { "role": "tool", "name": "wait_agent", "content": "agent-p responded: Feature X complete. 3 files changed, all tests passing. Summary: ..." },
 
  { "role": "assistant", "content": "Feature X is built. Here's what was done..." }
]
```

The planner messaging the implementer, the implementer sending code to the reviewer, the reviewer requesting fixes — all of that happens inside the agents' own conversations. The main agent's context stays clean. The model checked in with `list_agents` after a timeout. It could have called `wait_agent` with no timeout and blocked until completion.

The main agent collects results only when an agent explicitly messages back (here, the planner reports completion). Everything else is invisible to it. Implementations vary in how cross-agent addressing works: hierarchical paths (`/root/planner` to `/root/implementer`), file-based mailboxes, or IPC protocols.

**When to use this:** Large tasks where the coordination logic exceeds what a single agent can manage step-by-step.

**Limitations:** Every agent in the team needs frontier-class model capabilities, not just the main agent. Each team member must independently decide when to message teammates, what to include, and when to report back. Models can message the wrong agent, forget to report completion, or get stuck in loops. Beyond model capability, there are infrastructure challenges: cycle detection (A waits on B, B waits on A), conflict resolution (two agents edit the same file), and shutdown coordination. Debugging is hard because message chains between agents are difficult to trace and failures cascade.

## [](http://www.philschmid.de/subagent-patterns-2026#choosing-a-pattern)Choosing a Pattern

| Pattern | Tools | Main Agent Role | Agent Lifetime |
| --- | --- | --- | --- |
| **Inline Tool** | `call_agent` | Caller | Single task |
| **Fan-Out** | `spawn_agent`, `wait_agent` | Dispatcher | Single task |
| **Agent Pool** | `spawn`, `send`, `wait`, `list`, `kill` | Coordinator | Multi-turn |
| **Teams** | All above + cross-agent `send_message` | Supervisor | Persistent |

Start with Pattern 1. Most tasks that feel like they need a multi-agent system work fine with a well-prompted inline tool call. Move to Pattern 2 for genuinely independent parallel work. Move to Pattern 3 when agents need to collaborate across multiple steps. Pattern 4 is for when coordination logic exceeds what a single agent can manage.

Each step up requires a more capable model. Pattern 1 works with any model that can call tools. Pattern 2 needs a model that reasons about when to wait. Pattern 3 needs a model that tracks multi-agent state across turns. Pattern 4 needs frontier models for every agent. With a smaller or cheaper model, stay with Pattern 1 or 2.

Result collection also changes across patterns. Pattern 1 returns results inline as a tool response. Pattern 2 batches results via `wait_agent`. Pattern 3 delivers results incrementally. Pattern 4 surfaces only what agents explicitly report back; everything else stays inside inter-agent conversations.

For patterns 2-4, `spawn_agent` always returns immediately and `wait_agent` collects results when the model decides to call it. The framework provides the tools. The model controls the orchestration. A task that takes 4 coordinated agents today may be solvable by a single agent with a better model tomorrow.

[Philipp Schmid © 2026](http://www.philschmid.de/philipp-schmid)[Imprint](http://www.philschmid.de/imprint)[RSS Feed](http://www.philschmid.de/rss)

theme

[Mail](mailto:schmidphilipp1995@gmail.com)[Twitter](https://twitter.com/_philschmid)[LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/)[GitHub](https://github.com/philschmid)
