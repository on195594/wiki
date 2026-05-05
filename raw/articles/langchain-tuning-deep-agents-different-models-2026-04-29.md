---
title: Tuning Deep Agents to Work Well with Different Models
author: Vivek Trivedy; Mason Daugherty
source_type: article
source_url: https://www.langchain.com/blog/tuning-deep-agents-different-models
share_url: https://share.google/i7rcqOBBckeuD4pf3
published_at: 2026-04-29
captured_at: 2026-04-30
status: raw
---

# Summary capture

## Core claim
LangChain 认为 Deep Agents 不能继续只靠一套通用 harness 适配所有模型；不同模型需要不同的 prompt、tool schema / tool naming、middleware 和 subagent/skill 配置。于是 Deep Agents 引入 model-specific `HarnessProfile`，让 `create_deep_agent` 在调用点不变的情况下，根据模型或 provider 自动应用不同 harness override。

## Key points
- 单一通用 harness 无法最优适配所有 LLM，因为 OpenAI Codex、Anthropic Claude、Google Gemini 等模型家族的 prompt guide、工具命名和工具使用习惯不同。
- 同一底层模型在不同 harness 下表现可能差异很大；文章引用 Terminal-Bench 2.0 和 LangChain 先前 harness engineering 实验作为证据。
- Deep Agents 新增 `HarnessProfile`，以声明式方式覆盖 system prompt prefix/suffix、工具启用/命名、中间件、subagent 配置和 skills。
- 默认内置 OpenAI、Anthropic、Google profiles；开发者可覆盖、叠加或通过插件分发自己的 profile。
- 在 `tau2-bench` 困难子集上，custom profile 让 GPT 5.3 Codex 从 33% 提升到 53%，Claude Opus 4.7 从 43% 提升到 53%。

## Important facts
- Codex profile 的核心调整：用 `apply_patch` 替代默认 file edit；把 execute 别名成 `shell_command`；提示模型在工具调用前一次性决定所需文件和资源，并并行批量读取/搜索。
- Opus profile 的核心调整：用 prompt 强化工具结果反思、主动观察真实状态、读文件后再描述、跑测试后再声称通过、搜索后再断言符号是否存在。
- 文章明确说该功能当前只在 Python 中可用，TypeScript 版本将随后支持。

## Practical takeaway
Agent 的实际能力不是 `model` 单变量，而是 `model + harness` 的组合能力。对多模型 agent 系统来说，prompt、tool schema、middleware 和 verification discipline 应该被当作随模型变化的配置层，而不是全局常量。

## Applicability
- 多模型 agent runtime
- coding / research / long-horizon autonomous tasks
- 需要在 OpenAI、Claude、Gemini 等模型之间切换的工程系统
- 需要用 eval 证明 prompt/tool/middleware 改动收益的 agent 团队

## Limits
- `tau2-bench` 结果来自挑选的困难子集，不等同于完整 benchmark 全局表现。
- 文章是工程发布与设计说明，不是严格学术实验。
- 对 Hermes 的落地不能直接等同于修改 Hermes runtime profile；应先在 skill / workflow / validation project 层验证，再决定是否提升到 runtime 配置。

## Compiled wiki outputs
- Concept: [[hermes-model-specific-harness-profiles]]
- Hermes plan: [[hermes-system-model-specific-harness-optimization-plan]]

---

# Extracted source text

来源：用户 share.google 链接已解析到 canonical URL: https://www.langchain.com/blog/tuning-deep-agents-different-models

# Tuning Deep Agents to Work Well with Different Models

![Image 8](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)

![Image 9](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)

Vivek Trivedy

Mason Daugherty

April 29, 2026

![Image 10](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)

5

min

[Go back to blog](http://www.langchain.com/blog)

[Create agents](http://www.langchain.com/blog/tuning-deep-agents-different-models#)

Share

[](http://www.langchain.com/blog/tuning-deep-agents-different-models#)[](http://www.langchain.com/blog/tuning-deep-agents-different-models#)[](http://www.langchain.com/blog/tuning-deep-agents-different-models#)

![Image 11](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)

## Key Takeaways

‍💡**TL;DR:**[Deep Agents](https://github.com/langchain-ai/deepagents) was previously designed in a generic way to work well across model families. Today we’re adding model-specific profiles to adjust prompts, tools, and middleware. This allows us to better conform to prompting guides specific to model families. We ship profiles for OpenAI, Anthropic, and Google models out of the box, which we see leads to a 10–20 point jump on a subset of tau2-bench over the default harness.

Until today, `deepagents` shipped with a single set of prompts, tools, and middleware aimed to work well across _all_ Large Language Models. Builders could swap in different models or extend the harness with additional tools extensions to the system prompt. But the base prompts, tools, and middleware were fixed and not optimized per model.

As of today, we’re excited to launch **harness profiles** as a way to control these parameters on a per-model basis. This matters because:

*   **Prompting guides differ per model.** OpenAI's [Codex Prompting Guide](https://developers.openai.com/codex/prompting) prescribes specific tool implementations and names (`apply_patch`, `shell_command`) that move the needle on Codex models. Anthropic's [Claude prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) emphasizes a different set of conventions. Even within a family, the Opus 4.6 → 4.7 migration guide flags prompt-level changes worth making.
*   **Eval leaderboards show that the same model in a different harness can yield much different performance.**[Terminal-Bench 2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0) is the cleanest public example. The [Claude Code harness ranks last](https://www.tbench.ai/leaderboard/terminal-bench/2.0?models=Claude+Opus+4.6) among Opus 4.6 submissions. We saw similar effects of careful harness engineering in previous work: [Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering). Here we took `gpt-5.2-codex` from 52.8% to 66.5% on Terminal-Bench 2.0 (Top 30 → Top 5 at the time of publishing) _just by applying harness layer changes_ like prompts and middleware hooks.

A single harness can't be optimal for every model. So we make it easy to support varying the harness per model.

How much does this matter?

## Results on measuring the effect of profiles

In order to judge how much this matters, we measured performance on a subset of [tau2-bench](https://github.com/sierra-research/tau2-bench) (multi-turn tool use + instruction following). We use a curated subset of more difficult tasks that frontier models haven’t yet saturated so we can better measure the impacts of harness level changes on agents.

| Model | Base Deep Agents Harness | With Custom Profile |
| --- | --- | --- |
| GPT 5.3 Codex | 33% | 53% |
| Claude Opus 4.7 | 43% | 53% |

### What changed per model

We use the [Codex](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) and [Claude](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) prompting guides as the source for what changes we applied per profile.

For Codex the main changes included:

*   **Tool changes:** overriding the default `file_edit` implementation in `deepagents` with the recommended `apply_patch` tool, and aliasing the `execute` tool name in `deepagents` as `shell_command`
*   **Prompt changes:** largely around tool calling and planning using details from the prompting guide

> Before any tool call, decide ALL files and resources you will need. Batch reads, searches, and other independent operations into parallel tool calls instead of issuing them one at a time.

For Opus the main changes were all prompting focused on tool usage and planning. For example, below are two snippets that were added to the prompt.

> <tool_result_reflection>
> 
> After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
> 
> </tool_result_reflection>

> <tool_usage>
> 
> When a task depends on the state of files, tests, or system output, use tools to observe that state directly rather than reasoning from memory about what it probably contains. Read files before describing them. Run tests before claiming they pass. Search the codebase before asserting a symbol does or does not exist. Active investigation with tools is the default mode of working, not a fallback.
> 
> </tool_usage>

Our takeaway is that exposing an interface for customizing the harness per model is a helpful primitive for builders to manage profiles per agent, version them, and easily test differences in configurations.

## Try it today

To use this today, simply start using `deepagents`: `uv add deepagents`

```bash
agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    tools=[internet_search],
    system_prompt=research_instructions,
)
```

The profiles will be automatically applied for supported models. If you want to look into the details of what each default profile looks like today, you can inspect the code in the [repo](https://github.com/langchain-ai/deepagents). To learn how to register your own profile, keep reading.

### How profiles work under the hood

A harness profile is a declarative override layer for the parts of the harness that vary per model: system prompt prefix/suffix, tool inclusion and naming, middleware selection, subagent configuration, and skills. You register a profile for a model or provider (or load a preexisting one from YAML), and `create_deep_agent` adapts when you swap the model. Importantly, your call site doesn't change.

We ship defaults for OpenAI, Anthropic, and Google models. You can override them, layer your own on top, or distribute profiles as plugins.

```python
from deepagents import (
    HarnessProfile,
    register_harness_profile,
)

register_harness_profile(
    "openai:gpt-5.4",
    HarnessProfile(
        system_prompt_suffix="Respond in under 100 words.",
        excluded_tools={"execute"},
        excluded_middleware={"SummarizationMiddleware"},
    ),
)
```

Or declare a profile in YAML:

```yaml
# openai.yaml
base_system_prompt: You are helpful.
system_prompt_suffix: Respond briefly.
excluded_tools:
  - execute
  - grep
excluded_middleware:
  - SummarizationMiddleware
  - my_pkg.middleware:TelemetryMiddleware
general_purpose_subagent:
  enabled: false
```

For more custom details read the [Profiles docs](https://docs.langchain.com/oss/python/deepagents/profiles) for the full field surface, merge semantics, and plugin packaging. Register a profile at startup for the models you use, or rely on the built-in profiles we ship.

If you're building on Deep Agents and want to share a profile, [open a PR](https://github.com/langchain-ai/deepagents) or [distribute it as a plugin](https://docs.langchain.com/oss/python/deepagents/profiles#ship-a-profile-as-a-plugin) via entry points. We'll keep extending the profile surface across models. The goal is that whichever model you reach choose, Deep Agents gives you the tools and defaults to create the best harness for your task. We’ll be releasing more information and walkthroughs showing how builders can customize their agent harness for their tasks.

_Note: This is currently only available in Python but is coming soon to TypeScript_
