# Read-only review: Antigravity Custom Agents sedimentation

Review only the exact candidate snapshots below. Do not inspect or modify live files, run commands, use tools, create files, or propose expanding the change beyond the listed targets.

## Intended decision

- Preserve the official Antigravity article as a raw source.
- Update the existing `hermes-model-specific-harness-profiles` concept instead of creating a duplicate concept.
- Add one bounded optional reference section to the existing AGY runtime/config customization reference.
- Do not create a Custom Agent, new skill/workflow, router, runtime profile, memory entry, cron, MCP, plugin, or configuration change.
- Keep Hermes as parent owner of authorization, verification, and final acceptance.

## Review questions

1. Is the placement correct and non-duplicative?
2. Are article claims separated from Hermes-local inference and vendor-evidence limitations?
3. Are project/global paths, `mainAgent`/`subagent`, `commandExecutionPolicy`, and hooks represented accurately from the supplied official source?
4. Does the optional reference have clear trigger and skip conditions without turning Custom Agents into a default?
5. Are security and active-layer boundaries preserved?
6. Is any wording materially incorrect, overbroad, stale, or internally inconsistent?

## Required output

Verdict: PASS | PASS_WITH_NOTES | REQUEST_CHANGES
Blocking findings: each with snapshot evidence, why it matters, and minimal fix; or None
Important notes: non-blocking notes; or None
Safety boundary assessment: concise
Execution-force assessment: concise
Recommended next step: exactly one action

## Wiki tracked-file diff

```diff
diff --git a/_meta/raw-source-hashes.json b/_meta/raw-source-hashes.json
index 5c1b14e..7faf81c 100644
--- a/_meta/raw-source-hashes.json
+++ b/_meta/raw-source-hashes.json
@@ -9,6 +9,7 @@
   "raw/articles/dijkstra-ewd667-natural-language-programming-1978.md": "6363a9caf61d2e9e09cc87b12ab62c73b7d8b26331168d946026012921d5448c",
   "raw/articles/dtdt666-ordinary-investor-how-to-invest-2026-03-10.md": "e730ecf272adcc0ebc5beca6ba022626afb0411764ccdd666d2b660b2f8da7f7",
   "raw/articles/forbes-ai-implementation-startup-founders-human-needs-2026-06-16.md": "bcb4ba38b811ff6a404d6b028f9eb2bbc40273bf16ca05a2d7ff75aa5006e3cc",
+  "raw/articles/google-antigravity-custom-agents-2026-08-12.md": "ffe0c0dad6f8c318d30f2d873b26e203210674b6822f39e2a023026b849ee04e",
   "raw/articles/google-sre-gemini-cli-outages-2026-01-22.md": "f14e88d9b1274c90538c6f39fb7dcd6f53293982de5c8cba75fb85c939fa2439",
   "raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md": "202341a1eb37bad92fc29fd01fc55338accb159a84b5b4302695558d2a758902",
   "raw/articles/gvm-money-work-for-you-1-percent-investor-wisdom-2026-04-14.md": "d10fbbaff7cde327e5c7717278ecc3d2fd551e601416b8f01ff720072b56a5e9",
diff --git a/concepts/hermes-model-specific-harness-profiles.md b/concepts/hermes-model-specific-harness-profiles.md
index 8b579e6..447b7a3 100644
--- a/concepts/hermes-model-specific-harness-profiles.md
+++ b/concepts/hermes-model-specific-harness-profiles.md
@@ -1,10 +1,10 @@
 ---
 title: Hermes Model-Specific Harness Profiles
 created: 2026-04-30
-updated: 2026-04-30
+updated: 2026-08-18
 type: concept
 tags: [hermes, agent, harness, model-profiles, skills, context-engineering, verification]
-sources: [raw/articles/langchain-tuning-deep-agents-different-models-2026-04-29.md, concepts/hermes-agent-workflow-layering-and-adoption-order.md, concepts/hermes-context-layer-operating-rules.md]
+sources: [raw/articles/langchain-tuning-deep-agents-different-models-2026-04-29.md, raw/articles/google-antigravity-custom-agents-2026-08-12.md, concepts/hermes-agent-workflow-layering-and-adoption-order.md, concepts/hermes-context-layer-operating-rules.md]
 status: stable
 description: 定义 Hermes 针对不同模型配置 harness profile 的适配原则和验证路径。
 aliases: [model-specific-harness, harness-profiles]
@@ -35,6 +35,20 @@ LangChain 的 Deep Agents 文章给 Hermes 的核心启发是：Agent 的能力
 
 所以 Hermes 的 model-specific harness 不是一个单点配置文件，而是一组跨层 overlay。
 
+### 1.1 Agent-level harness profile：角色范围比模型范围更窄
+
+Google Antigravity 的 Custom Agents 补充了一个更窄的 harness 单元：同一模型和 provider 内，可以用文件化角色配置限定 system instruction、默认工具、Skill/MCP 子集、模型、权限与生命周期 Hook，并选择该角色能作为主 Agent、子 Agent或两者运行。项目级角色放在 `.agents/agents/`，稳定的用户级角色放在 `~/.gemini/config/agents/`；这些路径和字段属于随产品演进的外部接口，使用前仍需核对当前官方文档。
+
+Hermes 映射不是增加一套通用编排层，而是让现有 `coding-agent-delegation` 的 AGY lane 在确有重复角色时获得更小的上下文和工具面：
+
+- 优先把项目测试、依赖或构建约定放进仓库级角色，不复制到 Hermes 全局指令。
+- 用户级角色只承载跨项目稳定职责，例如只读审查；不要预建架构师、测试员、文档员等角色目录。
+- `mainAgent` / `subagent` 只决定 AGY 内的启动形态，不改变 Hermes 作为父级的范围、授权、验证和最终裁决责任。
+- `commandExecutionPolicy` 和 Hook 是 provider 侧执行控制，不是 Hermes 的批准替代品；写操作、生产、凭证、DB、cron、runtime 与外部副作用仍受原有边界约束。
+- 先用真实重复配置或上下文膨胀证明角色值得存在；一次性任务继续使用 bounded task packet 或普通 subagent。
+
+这强化了本页的 `overlay before core` 原则，但没有提供创建新 Hermes runtime profile、自动路由器或默认多 Agent 工作流的证据。
+
 ### 2. 当前不应马上新建 Hermes runtime profile
 当前运行状态显示 Hermes 只有 `default` profile，模型为 `gpt-5.5`，provider 为 OpenAI Codex，Gateway 正常运行，Telegram 是主要入口。这符合现阶段策略：保持主脑稳定，不因为一篇文章就立刻增加 runtime profile。
 
diff --git a/index.md b/index.md
index 2188cf6..da86cdd 100644
--- a/index.md
+++ b/index.md
@@ -66,7 +66,7 @@
 - [[hermes-lifeos-layer-boundary-contract]] — Hermes LifeOS 的层边界契约：以 default profile 为主脑，明确 wiki、memory、skill、cron、MCP、profile 与 session 的职责和越界规则
 - [[hermes-layer-routing-decision-checklist]] — Hermes 的层间路由判定清单：什么进 wiki、memory、skill、cron、MCP，按官方定义和本地知识层分开判断
 - [[hermes-memory-governance-notes]] — 一次实际 memory 减脂后沉淀出的治理规则：什么该继续留在 memory，什么该迁移到 wiki、skill 或 session
-- [[hermes-model-specific-harness-profiles]] — Hermes 的 model-specific harness profile 原则：把 Codex、Claude、Gemini 的模型差异转成 skill / wrapper / project context / verification overlay，而不是贸然扩张 runtime profile
+- [[hermes-model-specific-harness-profiles]] — Hermes 的 model/role-specific harness 原则：把模型差异和 AGY Custom Agent 角色边界转成 skill、project context、窄工具面与 verification overlay，而不是扩张 runtime profile 或预建角色目录
 - [[hermes-memory-skills-wiki-boundaries]] — Hermes memory / skills / wiki 的边界规范：把当前状态、稳定事实、历史事件和可复用规程路由到不同层，而不是全部写进 memory
 - [[hermes-retrieval-priority-and-answer-path]] — Hermes 检索优先级与回答路径：先查 wiki，再按 memory/skills/sessions/external 补全
 - [[hermes-wiki-lint-and-health-check-standards]] — Hermes wiki lint / 健康检查规范：链接、索引、frontmatter、标签、陈旧性与结构健康
diff --git a/log.md b/log.md
index a3c1bba..5b18406 100644
--- a/log.md
+++ b/log.md
@@ -3,6 +3,13 @@
 > Chronological record of wiki actions.
 > Format: `## [YYYY-MM-DD] action | subject`
 
+## [2026-08-18] ingest + optional reference | Google Antigravity Custom Agents
+- Captured the full rendered official article at `raw/articles/google-antigravity-custom-agents-2026-08-12.md`, preserving author/date, current paths and fields, extraction route, source quality and vendor-evidence limitations.
+- Updated `concepts/hermes-model-specific-harness-profiles.md` rather than creating a duplicate concept: added agent-level role profiles as a narrower harness overlay with project/global placement, main/subagent symmetry, scoped tools and explicit parent-verification boundaries.
+- Updated the existing index description and added one bounded optional reference update in `skill:autonomous-ai-agents/coding-agent-delegation/references/agy-cli-runtime-config-customization.md`; no new workflow, skill, role directory, runtime profile or router was created.
+- Promotion boundary: Custom Agents are candidates only for repeated AGY roles or measured context/tool-surface problems; provider permission policy and hooks do not replace Hermes approval, drift checks or parent verification.
+- Backup: `/home/lin/.hermes/backups/antigravity-custom-agents-20260818_154438`.
+
 ## [2026-08-18] review | AGY review of human-machine scientific discovery ingestion
 - Reviewed exact commit `04665602eeb929a07b437a3e3ab4fb66facaf3c6` (`docs: add verification scarcity concept`).
 - Review prompt: `_meta/reviews/2026-08-18-human-machine-scientific-discovery-agy-review-prompt.md`; result: `_meta/reviews/2026-08-18-human-machine-scientific-discovery-agy-review.md`; exit code `0`.
```

## New raw source snapshot

```markdown
1|---
2|title: Google Antigravity — Introducing Custom Agents
3|created: 2026-08-18
4|updated: 2026-08-18
5|type: raw-source
6|tags: [agent, multi-agent, subagent, harness, configuration, ai-coding]
7|source_url: https://antigravity.google/blog/introducing-custom-agents
8|author: The Antigravity Team
9|published: 2026-08-12
10|captured: 2026-08-18
11|source_quality: full-rendered-official-blog
12|status: captured
13|---
14|
15|# Google Antigravity — Introducing Custom Agents
16|
17|## Source
18|
19|- URL: https://antigravity.google/blog/introducing-custom-agents
20|- Publisher: Google Antigravity Blog
21|- Author: The Antigravity Team
22|- Published: 2026-08-12
23|- Captured: 2026-08-18
24|- Extraction route: rendered browser DOM, main container
25|- Source quality: full official article body
26|- Limitation: this is a vendor announcement, not independent production evidence. Configuration fields and paths are current as stated on the publication date and should be checked against current official documentation before use. Navigation and footer boilerplate were omitted.
27|- Local summary: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260818-153254-🐴-Google-Antigravity-Blog-Introducing-Custom-Agents-452500-188920120-summary.md`
28|
29|## Article body
30|
31|# Introducing Custom Agents
32|
33|Software engineering has shifted from writing lines of code to orchestrating agents. With this shift comes an opportunity for a real productivity unlock via division of labor, breaking complex projects down into specialized agents that can act, verify, and run tasks in parallel.
34|
35|This is why we are introducing Custom Agents with first-class support in Antigravity 2.0 and the Antigravity CLI, with the Antigravity IDE following shortly.
36|
37|This post details what custom agents are, how you can set one up in seconds, and some functionalities we have given to custom agents that are unique to Antigravity.
38|
39|## What Are Custom Agents and Why Do They Matter?
40|
41|General-purpose coding assistants are great, but they suffer from two major limitations:
42|
43|**Lack of Specialization:** A general-purpose assistant doesn’t know your specific project’s testing conventions or dependency management rules unless you explain them every single time.
44|
45|**Context Window Bloat:** Loading a massive, monolithic prompt containing all your coding guidelines, linters, and testing rules into every single chat turns into a token budget disaster.
46|
47|Custom agents solve this. They are specialized, file-based configurations that define a particular role with its own scoped instructions, tools, and constraints. This keeps your active context clean, minimizes token overhead, and gives you a predictable partner for specific tasks.
48|
49|Now, you might have read this and thought: aren’t these issues addressed by skills and dynamic subagents? To a large degree, yes! Custom agents don’t replace skills and dynamic subagents, they just provide even more customizability for another level of optimization:
50|
51|Skills obviously specialize a custom agent by giving additional context and instructions, and with their progressive discovery, helps to address context window bloat by not adding the full additional text in the full prompt by default, even if not needed. Instead, we let the agent determine whether the full skill should be read given the work at hand. But, if you think about the full set of skills you need across all tasks that you may do, that is still a very large list and the descriptions themselves will take a lot of context. Custom agents let you specify the subset of skills that are actually relevant for the specialization at hand. The same extends to MCP servers, hooks, and other existing customization points. And then on top of that, custom agents let you also customize the system instruction, default tools, and other more “core” parts of the agent loop.
52|
53|We introduced dynamic subagents a couple of months ago, and they also help along these axes by letting the main agent delegate some work to a subagent to not pollute the main agents’ context. The “dynamic” part is that the main agent can specify the prompt that it sends to the subagent. With custom agents, we take this one step further by allowing the main agent to delegate to a custom agent, with its specific customizations as discussed earlier, but also potentially other details like model and permissions.
54|
55|## What’s Available Today in Antigravity 2.0 & CLI
56|
57|Custom agents are now fully integrated across both the visual Antigravity 2.0 Desktop App and the Antigravity CLI.
58|
59|Similar to Skills, we’ve adopted a Markdown file format containing a YAML frontmatter header, allowing for progressive discovery over custom agents as well. You save these files in your local workspace under `.agents/agents/` or user-globally under `~/.gemini/config/agents/`.
60|
61|By committing project-specific agents to `.agents/agents/`, they automatically become available to every teammate who checks out the repository—giving your entire team standardized, instant workflow assistants out of the box without requiring manual setup.
62|
63|Here is a basic 101 Blueprint of a simple agent:
64|
65|```markdown
66|---
67|name: dependency-modernizer
68|description: Helps upgrade local packages and verify that project tests pass.
69|model: flash
70|tools:
71|  - view_file
72|  - replace_file_content
73|  - manage_task
74|  - run_command
75|---
76|
77|# Core Instructions
78|You are a dependency modernizer. Your job is to check configuration files,
79|update target dependencies, run test suites, and verify the build passes.
80|```
81|
82|Setting up specialized agents is just a single Markdown file. The frontmatter tells the product how to run the agent, and the markdown body compiles directly into its system prompt. See the docs on all of the fields that can appear in the frontmatter.
83|
84|## What Makes Antigravity Custom Agents Special?
85|
86|If you’ve used other tools in this space, this Markdown + YAML frontmatter layout will look very familiar. We deliberately aligned our file conventions to make porting your existing custom agents as painless as possible.
87|
88|That being said, how these agents run under the hood in Antigravity is structurally different. Let’s take our basic dependency-modernizer example and build on it to highlight some of the unique possibilities with custom agents in Antigravity.
89|
90|### 1. True Symmetry: Main Agent vs. Subagent
91|
92|In other tools in this space, custom agents are restricted to being subagents only. As a user, you interact with the main, default agent, and it decides when to spawn your worker behind the scenes using the frontmatter descriptions. You cannot launch a primary session directly as your custom agent.
93|
94|Antigravity introduces execution symmetry via simple configuration flags:
95|
96|```yaml
97|mainAgent: true
98|subagent: true
99|```
100|
101|**As a Main Agent:** You can select `dependency-modernizer` directly from the dropdown in the Antigravity 2.0 GUI, or run it via the CLI (`agy --agent dependency-modernizer`). The specific core instructions are directly compiled into the system prompt and you adopt all of the agent execution parameters in the frontmatter, allowing you talk directly to your custom agent.
102|
103|**As a Subagent:** The same agent can be dynamically called as a tool by a coordinator agent, as is standard.
104|
105|### 2. Scoped Safety Policies (`commandExecutionPolicy`)
106|
107|Running an agent that executes command-line operations (like dependency installs or test suites) can be incredibly frustrating. If the safety policy is too loose, you risk running unverified code. If the policy is too strict, you get stuck in a loop of constant approval prompts.
108|
109|While both Antigravity and other tools support basic, all-or-nothing permission levels (like `acceptEdits` or `bypassPermissions`), we add a dedicated execution filter:
110|
111|```yaml
112|permissionMode: acceptEdits
113|commandExecutionPolicy: auto
114|```
115|
116|Setting `commandExecutionPolicy: auto` allows the agent to execute standard test and compilation commands autonomously in the background. High-risk commands (like deleting files) remain strictly gated behind manual approvals. This lets the modernizer perform rapid trial-and-error cycles in the background without constantly prompting you for approval.
117|
118|### 3. Rich Lifecycle Hooks (Nested Interceptors)
119|
120|Other tools in this space support basic lifecycle hooks scoped to the subagent. Antigravity takes this further by introducing a nested lifecycle hooks schema directly in the agent’s definition.
121|
122|We can add setup and verification checks to our modernizer at precise execution boundaries:
123|
124|```yaml
125|hooks:
126|  PreInvocation:
127|    - type: command
128|      command: scripts/setup.sh
129|  PreToolUse:
130|    - matcher: run_command
131|      hooks:
132|        - type: command
133|          command: scripts/verify-local-env.sh
134|```
135|
136|In this example:
137|
138|- `PreInvocation`: runs a setup script to prepare the environment before the agent starts thinking.
139|- `PreToolUse` with matchers: intercepts specific tool calls. Here, every time the agent tries to run a terminal command, a verification script runs first to ensure the local environment is sound.
140|
141|There are a number of locations to place hooks, as can be found in the official docs. This granular control keeps the agent from making assumptions about the local execution environment, preventing compilation loops before they even start.
142|
143|## Looking Forward
144|
145|Custom agents are the next step toward a cohesive customization story across the product stack, allowing Antigravity to assist on more complex tasks in more efficient ways. The article directs readers to the Custom Agents Guide for the current field definitions.
146|
147|## Local evidence boundary
148|
149|This source establishes that Antigravity exposes file-based role profiles, project/global placement, main/subagent flags, scoped tools/models/permissions, command execution policy, and lifecycle hooks as of 2026-08-12. It does not establish that more specialized agents improve outcomes in this Hermes installation, that `commandExecutionPolicy: auto` is safe for every repository, or that role proliferation reduces total context and maintenance cost. Those questions require current official-doc checks and project-local use evidence.
150|
```

## Active optional-reference diff

```diff
--- /home/lin/.hermes/backups/antigravity-custom-agents-20260818_154438/agy-cli-runtime-config-customization.md	2026-08-18 15:44:38.492000000 +0800
+++ /home/lin/.hermes/skills/autonomous-ai-agents/coding-agent-delegation/references/agy-cli-runtime-config-customization.md	2026-08-18 15:46:11.956000000 +0800
@@ -28,6 +28,18 @@
 
 If multiple layers could fit, ask the user to choose before writing. Do not silently pick Hermes skills as a fallback.
 
+## Custom Agent role profiles
+
+Use Antigravity Custom Agents only when an AGY role has repeated project-specific instructions or a measured context/tool-surface problem; do not pre-create a catalog of specialist roles. Confirm current fields and paths against official docs before writing because this is a vendor-controlled interface.
+
+- Project-scoped roles belong in `.agents/agents/`; user-global roles belong in `~/.gemini/config/agents/` only when the responsibility is stable across projects.
+- `mainAgent` / `subagent` control whether AGY can launch the role directly, delegate to it, or both. They do not transfer Hermes parent ownership of scope, authorization, verification, or final acceptance.
+- Limit each role to the smallest relevant system instruction, tools, Skill/MCP subset, model and permissions. A Custom Agent complements skills and bounded task packets; it does not replace either.
+- Treat `commandExecutionPolicy` and lifecycle hooks as AGY-side controls, not blanket safety approval. Hooks must be deterministic, repository-owned, cheap, non-secret-bearing and separately validated; high-risk commands and production, credential, DB, cron, runtime or external side effects retain their existing approval gates.
+- Prefer a read-only reviewer as the first reusable role. Add implementation roles only after repeated configuration proves that a plain delegated prompt is insufficient.
+
+Skip Custom Agents for one-off tasks, ordinary summaries/lookups, roles that differ only by prose style, or cases where a normal bounded delegation packet already supplies all required context.
+
 ## Safe edit workflow
 
 1. Restate the target as AGY CLI runtime/config, not Hermes skill governance.
```
