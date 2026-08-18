---
title: Google Antigravity — Introducing Custom Agents
created: 2026-08-18
updated: 2026-08-18
type: raw-source
tags: [agent, multi-agent, subagent, harness, configuration, ai-coding]
source_url: https://antigravity.google/blog/introducing-custom-agents
author: The Antigravity Team
published: 2026-08-12
captured: 2026-08-18
source_quality: full-rendered-official-blog
status: captured
---

# Google Antigravity — Introducing Custom Agents

## Source

- URL: https://antigravity.google/blog/introducing-custom-agents
- Publisher: Google Antigravity Blog
- Author: The Antigravity Team
- Published: 2026-08-12
- Captured: 2026-08-18
- Extraction route: rendered browser DOM, main container
- Source quality: full official article body
- Limitation: this is a vendor announcement, not independent production evidence. Configuration fields and paths are current as stated on the publication date and should be checked against current official documentation before use. Navigation and footer boilerplate were omitted.
- Local summary: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260818-153254-🐴-Google-Antigravity-Blog-Introducing-Custom-Agents-452500-188920120-summary.md`

## Article body

# Introducing Custom Agents

Software engineering has shifted from writing lines of code to orchestrating agents. With this shift comes an opportunity for a real productivity unlock via division of labor, breaking complex projects down into specialized agents that can act, verify, and run tasks in parallel.

This is why we are introducing Custom Agents with first-class support in Antigravity 2.0 and the Antigravity CLI, with the Antigravity IDE following shortly.

This post details what custom agents are, how you can set one up in seconds, and some functionalities we have given to custom agents that are unique to Antigravity.

## What Are Custom Agents and Why Do They Matter?

General-purpose coding assistants are great, but they suffer from two major limitations:

**Lack of Specialization:** A general-purpose assistant doesn’t know your specific project’s testing conventions or dependency management rules unless you explain them every single time.

**Context Window Bloat:** Loading a massive, monolithic prompt containing all your coding guidelines, linters, and testing rules into every single chat turns into a token budget disaster.

Custom agents solve this. They are specialized, file-based configurations that define a particular role with its own scoped instructions, tools, and constraints. This keeps your active context clean, minimizes token overhead, and gives you a predictable partner for specific tasks.

Now, you might have read this and thought: aren’t these issues addressed by skills and dynamic subagents? To a large degree, yes! Custom agents don’t replace skills and dynamic subagents, they just provide even more customizability for another level of optimization:

Skills obviously specialize a custom agent by giving additional context and instructions, and with their progressive discovery, helps to address context window bloat by not adding the full additional text in the full prompt by default, even if not needed. Instead, we let the agent determine whether the full skill should be read given the work at hand. But, if you think about the full set of skills you need across all tasks that you may do, that is still a very large list and the descriptions themselves will take a lot of context. Custom agents let you specify the subset of skills that are actually relevant for the specialization at hand. The same extends to MCP servers, hooks, and other existing customization points. And then on top of that, custom agents let you also customize the system instruction, default tools, and other more “core” parts of the agent loop.

We introduced dynamic subagents a couple of months ago, and they also help along these axes by letting the main agent delegate some work to a subagent to not pollute the main agents’ context. The “dynamic” part is that the main agent can specify the prompt that it sends to the subagent. With custom agents, we take this one step further by allowing the main agent to delegate to a custom agent, with its specific customizations as discussed earlier, but also potentially other details like model and permissions.

## What’s Available Today in Antigravity 2.0 & CLI

Custom agents are now fully integrated across both the visual Antigravity 2.0 Desktop App and the Antigravity CLI.

Similar to Skills, we’ve adopted a Markdown file format containing a YAML frontmatter header, allowing for progressive discovery over custom agents as well. You save these files in your local workspace under `.agents/agents/` or user-globally under `~/.gemini/config/agents/`.

By committing project-specific agents to `.agents/agents/`, they automatically become available to every teammate who checks out the repository—giving your entire team standardized, instant workflow assistants out of the box without requiring manual setup.

Here is a basic 101 Blueprint of a simple agent:

```markdown
---
name: dependency-modernizer
description: Helps upgrade local packages and verify that project tests pass.
model: flash
tools:
  - view_file
  - replace_file_content
  - manage_task
  - run_command
---

# Core Instructions
You are a dependency modernizer. Your job is to check configuration files,
update target dependencies, run test suites, and verify the build passes.
```

Setting up specialized agents is just a single Markdown file. The frontmatter tells the product how to run the agent, and the markdown body compiles directly into its system prompt. See the docs on all of the fields that can appear in the frontmatter.

## What Makes Antigravity Custom Agents Special?

If you’ve used other tools in this space, this Markdown + YAML frontmatter layout will look very familiar. We deliberately aligned our file conventions to make porting your existing custom agents as painless as possible.

That being said, how these agents run under the hood in Antigravity is structurally different. Let’s take our basic dependency-modernizer example and build on it to highlight some of the unique possibilities with custom agents in Antigravity.

### 1. True Symmetry: Main Agent vs. Subagent

In other tools in this space, custom agents are restricted to being subagents only. As a user, you interact with the main, default agent, and it decides when to spawn your worker behind the scenes using the frontmatter descriptions. You cannot launch a primary session directly as your custom agent.

Antigravity introduces execution symmetry via simple configuration flags:

```yaml
mainAgent: true
subagent: true
```

**As a Main Agent:** You can select `dependency-modernizer` directly from the dropdown in the Antigravity 2.0 GUI, or run it via the CLI (`agy --agent dependency-modernizer`). The specific core instructions are directly compiled into the system prompt and you adopt all of the agent execution parameters in the frontmatter, allowing you talk directly to your custom agent.

**As a Subagent:** The same agent can be dynamically called as a tool by a coordinator agent, as is standard.

### 2. Scoped Safety Policies (`commandExecutionPolicy`)

Running an agent that executes command-line operations (like dependency installs or test suites) can be incredibly frustrating. If the safety policy is too loose, you risk running unverified code. If the policy is too strict, you get stuck in a loop of constant approval prompts.

While both Antigravity and other tools support basic, all-or-nothing permission levels (like `acceptEdits` or `bypassPermissions`), we add a dedicated execution filter:

```yaml
permissionMode: acceptEdits
commandExecutionPolicy: auto
```

Setting `commandExecutionPolicy: auto` allows the agent to execute standard test and compilation commands autonomously in the background. High-risk commands (like deleting files) remain strictly gated behind manual approvals. This lets the modernizer perform rapid trial-and-error cycles in the background without constantly prompting you for approval.

### 3. Rich Lifecycle Hooks (Nested Interceptors)

Other tools in this space support basic lifecycle hooks scoped to the subagent. Antigravity takes this further by introducing a nested lifecycle hooks schema directly in the agent’s definition.

We can add setup and verification checks to our modernizer at precise execution boundaries:

```yaml
hooks:
  PreInvocation:
    - type: command
      command: scripts/setup.sh
  PreToolUse:
    - matcher: run_command
      hooks:
        - type: command
          command: scripts/verify-local-env.sh
```

In this example:

- `PreInvocation`: runs a setup script to prepare the environment before the agent starts thinking.
- `PreToolUse` with matchers: intercepts specific tool calls. Here, every time the agent tries to run a terminal command, a verification script runs first to ensure the local environment is sound.

There are a number of locations to place hooks, as can be found in the official docs. This granular control keeps the agent from making assumptions about the local execution environment, preventing compilation loops before they even start.

## Looking Forward

Custom agents are the next step toward a cohesive customization story across the product stack, allowing Antigravity to assist on more complex tasks in more efficient ways. The article directs readers to the Custom Agents Guide for the current field definitions.

## Local evidence boundary

This source establishes that Antigravity exposes file-based role profiles, project/global placement, main/subagent flags, scoped tools/models/permissions, command execution policy, and lifecycle hooks as of 2026-08-12. It does not establish that more specialized agents improve outcomes in this Hermes installation, that `commandExecutionPolicy: auto` is safe for every repository, or that role proliferation reduces total context and maintenance cost. Those questions require current official-doc checks and project-local use evidence.
