---
title: Stop Choosing Between Local and Cloud LLMs: A Field Guide to Hybrid Patterns
author: Towards Data Science
source_type: article
source_url: https://towardsdatascience.com/stop-choosing-between-local-and-cloud-llms-a-field-guide-to-hybrid-patterns/
published_at: unknown
captured_at: 2026-07-03
status: raw
tags: [llm, agent, delegation, hybrid-llm, hermes, local-cloud]
extraction_limitations: Direct publisher fetch returned HTTP 403; source packet was captured through Jina Reader fallback and cached by gsummary. This raw note preserves the extracted source packet and Gemini summary, not a newly fetched page.
---

# Stop Choosing Between Local and Cloud LLMs: A Field Guide to Hybrid Patterns

## Source
- URL: https://towardsdatascience.com/stop-choosing-between-local-and-cloud-llms-a-field-guide-to-hybrid-patterns/
- Published: unknown
- Captured: 2026-07-03
- Extraction note: Jina Reader fallback after direct publisher fetch returned HTTP 403; extracted markdown body from source URL.

## Compiled concept page
- [[ai-task-delegation-patterns-from-local-cloud-hybrid-llms]]
- [[agent-autonomy-ladder-for-hermes-workflows]]
- [[subagent-orchestration-patterns]]

## Gemini summary

Source URL: https://towardsdatascience.com/stop-choosing-between-local-and-cloud-llms-a-field-guide-to-hybrid-patterns/
Source title: Stop Choosing Between Local and Cloud LLMs: A Field Guide to Hybrid Patterns
Extraction route: jina_reader
Fallback reason: blocked_or_checkpoint
Source quality: full
Extraction note: Jina Reader fallback after direct publisher fetch returned HTTP 403; extracted markdown body from source URL.

---

标题：Stop Choosing Between Local and Cloud LLMs: A Field Guide to Hybrid Patterns

一句话结论：不要在本地模型与云端大模型之间做单选，可以通过构建端云混合模式（如隐私脱敏后云端推理的脱敏-求解模式），同时兼顾云端大模型的强大推理能力与本地数据的隐私安全性。

完整清单（保留原文 5 项）：
1. Sanitize-and-Solve（脱敏与求解）
   - 含义/做法：本地小模型首先处理含有敏感信息的非结构化本地上下文，将其转化为仅包含 load_A、load_B 等匿名 ID 和必要物理事实（时间、能耗、截止时间）的抽象调度问题。云端大模型只接收该匿名问题并进行推理求解，结果传回本地后，由本地模型利用本地映射字典还原并输出给用户。
   - 作者声称的益处：既能利用云端模型的强逻辑推理能力，又能保证家庭或个人敏感隐私数据不泄露到云端。
   - 证据强弱/局限：强证据。作者在文章第 2 节提供了完整的智能家居电费调度代码实例和 Ollama (Gemma 4 E4B) + Azure OpenAI (GPT-5.4) 的具体测试结果。局限在于存在“约束税（Constraint Tax）”，在小模型上强制使用结构化 JSON 格式可能会削弱其提取关键信息（如遗漏截止时间等）的准确性。
2. Plan-then-Ground（规划与落地）
   - 含义/做法：云端大模型首发处理。云端模型首先根据不含敏感数据的抽象目标生成一个通用规划。随后，将该规划发送给本地小模型，由本地小模型作为实际执行者，结合本地真实的敏感隐私数据执行该规划。
   - 作者声称的益处：云端大模型充当高级规划器，本地模型充当隐私敏感的落地执行者，有效实现隐私隔离。
   - 证据强弱/局限：弱证据。仅为作者提出的概念性架构图示（Figure 2），缺乏具体代码实现、案例分析或实验数据支持。
3. Escalate-on-Hard（遇难呈报）
   - 含义/做法：本地小模型首发且有条件地调用云端。本地模型优先处理绝大多数简单请求（如简单提取、分类、摘要或简短回答）。当且仅当遇到本地模型无法可靠解决的复杂问题时，才将请求升级给云端大模型。
   - 作者声称的益处：能够最大程度降低系统调用的成本和响应延迟，无需每次请求都调用高资费的云端 API。
   - 证据强弱/局限：弱证据/经验推论。仅提供了概念模式（Figure 3），没有给出如何判定“复杂/无法可靠解决”的具体量化阈值、路由决策层代码实现或成本/延迟降低的基准对比数据。
4. Draft-then-Refine（草稿与润色）
   - 含义/做法：本地小模型首发。本地模型首先快速生成一个初步草稿提供给用户，与此同时，云端大模型在后台异步进行更深度的推理。如果云端模型生成的精细答案质量明显更优，则用于替换或富化最初由本地模型提供的临时回答。
   - 作者声称的益处：兼顾了首字输出的超低延迟体验与最终回答的高质量保障。
   - 证据强弱/局限：弱证据。仅提供了流程概念（Figure 4），没有展示异步多模型合并输出的具体架构设计、延迟优化数据或用户体验对比。
5. Cross-Check（交叉校验）
   - 含义/做法：本地与云端模型地位平等，双向流且始终触发。两个模型充当独立的评审员，或一者生成一者审计，或两者针对同一问题独立作答，通过两者的符合度/分歧作为下游逻辑流转的判定信号。
   - 作者声称的益处：提升整体应用系统的信任度与运行可靠性。
   - 证据强弱/局限：弱证据。仅有概念拓扑图（Figure 5），未给出如何做多模型语义一致性判定、冲突仲裁机制或系统可靠性增幅的实际测试结果。

总体判断：
- 较稳妥的建议：若应用场景涉及敏感隐私（如家庭作息、名字、日常细节），且涉及需要复杂逻辑计算的问题（如电费及多负载排程），采用“Sanitize-and-Solve（脱敏与求解）”模式是最稳妥且被代码验证可行的。在小模型推理中，应采用提示词引导辅以应用层解析校验，而非强行配置严格 Schema，以规避约束税（Constraint Tax）对推理正确性的损害。
- 偏经验、需谨慎的建议：对于“Escalate-on-Hard”和“Draft-then-Refine”等模式，由于缺少云端升级判定标准和异步融合机制的实现细节，在实际工程落地时需要谨慎评估多模型数据同步和复杂边界的异常处理。

可信度与局限：
- 强证据部分：三步工作流（本地脱敏、云端匿名推理、本地 grounding 还原）具有高可信度，在 Gemma 4 E4B (Ollama 本地部署，硬件配置为 Intel i7-13800H CPU、32 GB RAM、NVIDIA RTX 2000 Ada 8G VRAM) 和 GPT-5.4 组合下运行通过，输出了符合约束的调度方案，证明了“脱敏与求解”模式的技术可行性。
- 弱证据/推论部分：作者引入了 Ray (2026) 关于“约束税（Constraint Tax）”的论文（https://arxiv.org/abs/2605.26128 ）来支持不在本地小模型上强加结构化输出约束的观点，这属于学术界已有的实证证据。但对于除模式 1 以外的其他 4 种混合模式，仅有定性概念描述，缺乏实际落地可信度论证。

来源元数据：
- Source URL / Canonical URL / Share URL：
  - Source URL: https://towardsdatascience.com/stop-choosing-between-local-and-cloud-llms-a-field-guide-to-hybrid-patterns/
  - Ollama 官网及下载链接: https://ollama.com/download
  - Linux 下 Ollama 安装脚本: https://ollama.com/install.sh
  - 结构化输出参考链接: https://towardsdatascience.com/you-probably-dont-need-an-agent-framework/#:~:text=2.4%20Structured%20Output
  - 约束税（Constraint Tax）论文链接: https://arxiv.org/abs/2605.26128
- 提取质量或局限：本摘要提取完整覆盖了原作者提出的 5 种混合模式、3 个考量维度（Direction, Trigger, Purpose）、3 步智能家居调度实现流程，并原样保留了所有技术工具版本与网络 URL，质量较好，未引入原文之外的信息。

工程复盘启发：
- [推论] 混合模式并非简单的负载分发，而是数据安全等级与算力消耗的折中。当涉及到敏感个人隐私或企业核心机密时，本地小模型应该被严格定位为“无状态的数据脱敏器”和“最终呈现的渲染器”，而计算密集型、非隐私敏感的求解器则交由云端处理，这种分工能够极大释放本地有限算力。
- [推论] 端侧小模型（如 Gemma 4 4B 级模型）在被施加严格的结构化格式约束（如 Pydantic JSON schema）时，由于模型容量限制，其注意力会过度集中于语法格式的满足，进而导致对输入长文本中细微逻辑和约束条件的处理能力下降。在工程落地时，应优先采用软引导，并在主应用层编写轻量校验和回滚逻辑，以释放端侧模型最大推理能力。

可执行建议：
1. 搭建本地端侧推理测试环境：
   在 Linux 终端执行 `curl -fsSL https://ollama.com/install.sh | sh` 安装 Ollama，下载端侧推理模型 `ollama pull gemma4:e4b`，并使用命令 `ollama run gemma4:e4b "what's the capital of France?"` 进行连通性与响应延迟验证。
2. 实施“脱敏-求解-还原”智能调度流水线：
   编写本地 Python 脚本，在 Step 1 使用 `LOCAL_SANITIZER_INSTRUCTIONS` 提示词模板促使 Gemma 4 模型将本地设备名及电费作息规则提炼为匿名 JSON（仅含 `load_A`、`load_B`）；在 Step 2 将匿名文本发送至 OpenAI GPT-5.4 接口，开启结构化解析 `responses.parse` 获得调度排程；最后在 Step 3 利用 Gemma 4 根据 `local_mapping` 将匿名负载翻译回设备名称呈现给用户。
3. 优化小模型提示词策略以规避“约束税”：
   对于本地小模型的数据脱敏和最终还原阶段，应避免在 Ollama API 中直接传入 `format` 字段进行硬格式限制，改为在 prompt 内通过 JSON 范例软约束，并调用 `think="high"`，`options={"temperature": 0, "num_ctx": 32768}` 等推理参数，由应用程序（如使用 `json.loads`）自行处理格式异常和重试逻辑。

## Extracted source packet

Source URL: https://towardsdatascience.com/stop-choosing-between-local-and-cloud-llms-a-field-guide-to-hybrid-patterns/
Title: Stop Choosing Between Local and Cloud LLMs: A Field Guide to Hybrid Patterns
Extraction note: Jina Reader fallback after direct publisher fetch returned HTTP 403; extracted markdown body from source URL.

Title: Stop Choosing Between Local and Cloud LLMs: A Field Guide to Hybrid Patterns

URL Source: https://towardsdatascience.com/stop-choosing-between-local-and-cloud-llms-a-field-guide-to-hybrid-patterns/

Published Time: 2026-06-30T12:00:00+00:00

Markdown Content:
LLM applications, two deployment choices are commonly seen: either we go fully cloud, i.e., sending everything to a cloud LLM API, or we go fully local, i.e., run everything with an open model served locally.

Cloud LLMs reason better, but we send our sensitive context outside. Local models keep that context private, but limited by the local compute, they can struggle when tasks get complex.

Naturally, we’d like to ask:

> _Can we enjoy the reasoning capability of the cloud, while still keeping private context local?_

A hybrid local-cloud pattern might achieve that. This is what we’ll explore in this post.

Specifically, we’ll discuss:

*   How to reason about hybrid designs. We’ll look into a three-axis map and illustrate 5 most common patterns.
*   A concrete case study to walk through one of the patterns. We use both a local small language model (Gemma 4 E4B from Google) and a cloud-based large language model (GPT-5.4 from OpenAI).

By the end, you should have a reusable mental model and a working notebook for splitting an LLM application between a local and a cloud model.

* * *

## 1. When Does A Hybrid Local-Cloud LLM Pattern Make Sense?

When people talk about local-cloud hybrid LLM applications, they immediately think of privacy. That’s certainly an important consideration.

**But privacy is not the only reason to go hybrid.**

Based on my experience, I find it useful to reason about this hybrid pattern from the lens of a three-axis coordinate system:

1.   **Direction**, which answers “who acts first?”. It can be local-first or cloud-first.
2.   **Trigger**, which answers “when is the cloud used?”. In some application scenarios, the cloud is always called. At other times, the cloud is only invoked conditionally.
3.   **Purpose**, which answers “why split the workflow?”. As we mentioned previously, privacy is a major motivation. But other factors can be cost & latency, as well as trust & reliability.

With these three axes, we can place many real-world hybrid workflows in the same coordinate map. Although this is far from a perfect taxonomy, I believe it makes the design choices intuitively understandable. Let’s take a look now.

### Pattern 1: Sanitize-and-Solve

This pattern is local-first (axis 1), always triggers cloud LLM (axis 2), and has privacy-preserving in mind (axis 3).

The local model consumes the unstructured, messy private context, but converts it into an abstract problem, which later gets sent to the cloud LLM. The cloud model only sees the abstract problem and solves it. The results get sent back to the local model, which can further process the results and feed them back to the user.

![Image 1](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/pattern_1-1-1024x378.png)

Figure 1. Sanitize-and-Solve pattern. (Image by author)

This is the pattern we will implement in the case study.

### Pattern 2: Plan-then-Ground

This pattern sits in the opposite direction. It is cloud-first (axis 1), the cloud model is always triggered (axis 2), and still privacy-preserving (axis 3).

Here, the cloud model is responsible for producing a generic plan based on an abstract goal. This step doesn’t involve seeing the private data. Then, the plan is sent to the local model, who plays the role of the actual executor that executes the plan against the real sensitive data.

![Image 2](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/pattern_2-1024x425.png)

Figure 2. Plan-then-Ground pattern. (Image by author)

### Pattern 3: Escalate-on-Hard

For many applications, it’s not necessary to call the cloud model for every single user request.

The local model might already be able to handle the easy majority, such as simple extractions, classifications, summarizations, or producing short answers. The cloud model is called only when the local model cannot sufficiently or reliably address the user’s request because it is too complex.

This pattern is local-first (axis 1), the triggering of the cloud model is conditional (axis 2), and often motivated by cost and latency, instead of privacy (axis 3).

![Image 3](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/pattern_3-1024x465.png)

Figure 3. Escalate-on-Hard pattern. (Image by author)

### Pattern 4: Draft-then-Refine

Another commonly seen pattern is to separate response speed from response quality.

In this pattern, the local model produces an immediate draft. Optionally, the cloud model can work in the background to provide a more careful answer. If the cloud answer is better, the application can replace or simply enrich the initial response offered by the local model.

This pattern is local-first (axis 1), may or may not trigger the cloud model (axis 2), and is often motivated also by cost and latency.

![Image 4](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/pattern_4-1024x431.png)

Figure 4. Draft-then-Refine pattern. (Image by author)

### Pattern 5: Cross-Check

Another important pattern worth mentioning is cross-checking.

Here, the local and cloud models are treated more or less as equal. They may both act like independent reviewers, where one model proposes an answer, and the other model checks it, or both models answer the same question, and their agreement/disagreement becomes the signal for downstream processing.

This pattern flows in both directions (axis 1), the cloud model is always on (axis 2), and it’s mainly driven by trust & reliability (axis 3).

![Image 5](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/pattern_5-1024x391.png)

Figure 5. Cross-Check pattern. (Image by author)

## 2. Case Study: Should I Run the Dishwasher Now or Later?

In this section, we move from abstract concepts to a concrete case study. Specifically, we’ll look at a smart-home scheduling problem.

### 2.1 Case Setup

Here, we consider a smart-home assistant system that keeps a private household memory.

Suppose the user asks the assistant:

> _Should the dishwasher run now or later?_

Effectively, the assistant needs to solve a scheduling problem.

To solve that problem, the assistant knows that now is `18:30`, and it has access to the following household memory, device facts, and tariff:

```
Household memory:
- The dishwasher needs to be done before breakfast because kids need clean bowls,
  usually around 06:30.
- Don't let the dishwasher still be running once everyone's in bed,
  usually around 22:30; it's right by the bedrooms and Maya is a light sleeper.
- The EV is Mark's car, and it has to be charged before he leaves at 07:00.
- The robot vacuum often runs after lunch; today it finished a kitchen pass
  around 16:10.

Device facts:
- Dishwasher: runtime about 90 minutes, energy about 1.2 kWh, available now.
- EV charger: runtime about 120 minutes, energy need about 14 kWh, available now.
- Robot vacuum: last cleaning cycle finished at 16:10; battery is at 78% on the dock.

Tariff:
- 17:00-20:00: $0.45/kWh
- 20:00-00:00: $0.22/kWh
- 00:00-06:00: $0.12/kWh
- 06:00-17:00: $0.25/kWh

As we can see, the above context contains quite some private information, such as names, household routines, etc., which we don’t want to send directly to a cloud model.

This naturally calls for a hybrid solution pattern. More concretely, we can design a workflow like this:

*   Step 1: local LLM. Read the private context, abstract the scheduling problem so that it contains no sensitive info.
*   Step 2: cloud LLM. Reason over the anonymous scheduling problem and produce a schedule.
*   Step 3: local LLM. Parse the cloud result back to the household language and present the final answer to the user.

![Image 6](https://contributor.insightmediagroup.io/wp-content/uploads/2026/06/workflow-1024x576.png)

Figure 6. The workflow to be implemented. (Image by author)

That’s the workflow we’ll build next.

### 2.2 Setup Ollama and Gemma 4 model

For this case study, we use **Gemma 4 E4B** model as our local LLM.

Gemma 4 is a model family released by Google this April. It’s designed for reasoning, coding, multimodal understanding, and agentic workflows. It comes in multiple sizes. What matters for us is the edge-friendly variants, i.e., the E4B model.

We’ll serve it locally with Ollama. In case you haven’t used it before, it’s a runtime for downloading, running, and serving local language models from your own machine. Once it is set up, Ollama exposes a local API endpoint.

On Windows machines, you can do that from the official installer:

`https://ollama.com/download`
After installation, you can launch Ollama from the Windows Start menu.

On a Linux machine, you can install Ollama with:

`"curl -fsSL https://ollama.com/install.sh | sh"`
Once Ollama is up and running, we can proceed to download our local language model. We can do that via the command line:

`ollama pull gemma4:e4b`
> _For reference, my laptop has an Intel i7-13800H CPU, 32 GB RAM, and an NVIDIA RTX 2000 Ada Laptop GPU with about 8 GB VRAM. You can choose `gemma4:e2b` instead if E4B feels too slow._

Before moving to the next step, we can do a quick test:

`ollama run gemma4:e4b "what's the capital of France?"`
If you get “Paris” back, then congratulations, Gemma 4 is now available on your local machine through Ollama.

### 2.3 Step 1: Local Sanitization

This step runs fully locally.

Here, the local model sees the full household context, and its objective is to prepare a sanitized scheduling problem for the cloud model by stripping away any sensitive information.

We start by drafting the system instruction:

# Note: This prompt was iterated with AI
LOCAL_SANITIZER_INSTRUCTIONS = """

You are a local smart-home assistant running inside the home.

The system has access to private household memory, device facts, and tariff information.
A user has asked a scheduling question about one household load.
Your role is to prepare the scheduling problem for a cloud reasoning model without exposing household-private details.

The cloud model will reason about timing, energy use, deadlines, and electricity prices.
It does not need to know appliance names, people names, room details, family routines, or why a constraint exists.

Create an anonymous scheduling problem for the cloud model.
Use load IDs such as load_A, load_B, and load_C instead of real device or load names.
Include the loads that matter for answering the user's scheduling question.

Think of scheduling_problem as a message copied directly into a cloud API call.
Anything written in scheduling_problem leaves the home.

Keep the private mapping from anonymous load IDs back to household device names in local_mapping.
The local_mapping field stays inside the home and is the only place where private device names may appear.

Do not answer the user's question or solve the schedule yourself.
Your job is to translate the private household context into a cloud-usable anonymous scheduling problem.

Rules:
- The scheduling_problem field is the exact text that will be sent to the cloud model.
- In scheduling_problem, use only anonymous load IDs, never appliance names, people names, room details, or household explanations. Do not pair load IDs with private names; write "load_A:" rather than labels like "load_A (robot vacuum):".
- Preserve the concrete scheduling facts needed for reasoning: current time, relevant loads, duration, energy use, earliest start time, required completion time, local cutoffs, and tariff windows.
- Put the private load-name mapping only in local_mapping.
""".strip()

Here, we ask the local model to do three things:

1.   Identify which household appliances are actually relevant to the user’s question;
2.   Remove sensitive information such as names, room details, etc.;
3.   Preserve sufficient scheduling facts so that the cloud model can still reason properly.

Next, we define a prompt builder function to prepare the context, which combines the user question, the private household context, and a lightweight output contract:

def build_local_sanitizer_prompt(
    private_context: dict[str, Any],
    user_question: str,
) -> str:
    return f"""
User question:
{user_question}

Private household context:
{format_private_context(private_context)}

Task:
Prepare an anonymous scheduling problem so the cloud reasoning model can analyze and plan the schedule.
Use anonymous load IDs in the scheduling problem, and keep the local-only mapping in local_mapping.

Return your answer as JSON with exactly these fields:

{{
  "target_load_id": "anonymous ID of the load referenced by the user's question",
  "scheduling_problem": "the exact anonymous scheduling problem that will be sent to the cloud",
  "local_mapping": {{
    "load_A": "robot vacuum",
    "load_B": "<household_device_name>"
  }}

The local_mapping example only illustrates the mapping direction.
Choose the actual anonymous load IDs based on the relevant loads you include.
Keys must be anonymous load IDs and values must be the original household device names.
Return only JSON, without a markdown fence.

Finally, we can call the model through Ollama:

# pip install ollama
import ollama
import json

prompt = build_local_sanitizer_prompt(
    private_context=private_context,
    user_question=USER_QUESTION,
)

response = ollama.chat(
    model="gemma4:e4b",
    messages=[
        {"role": "system", "content": LOCAL_SANITIZER_INSTRUCTIONS},
        {"role": "user", "content": prompt},
    ],
    think="high",
    options={"temperature": 0, "num_ctx": 32768},

content = response["message"]["content"]
local_sanitizer_output = json.loads(content)

A couple of things worth mentioning:

*   We need to install Ollama Python client.
*   We build the prompt from the user’s question and private household context.
*   We use the **thinking mode** of the model by supplying the `think` value. Since the local model needs to reason over a messy local context, giving the local model more thinking budget makes sense here.

> _You may notice that I ask Gemma to return JSON directly in the prompt. A more formal approach would be to use **[structured output](https://towardsdatascience.com/you-probably-dont-need-an-agent-framework/#:~:text=2.4%20Structured%20Output)**. Ollama supports that through the `format` argument:_

 model=LOCAL_MODEL,
 messages=messages,
 format=PydanticSchema.model_json_schema(),

> _In theory, this is very useful as the output becomes very easy to parse. However, in my experiments, I noticed that enforcing the output shape of the local LLM can constrain its capability. In our current case study, the model sometimes dropped important scheduling details, such as deadlines or cutoff times. On the other hand, if I only softly guide the output shape by providing examples in the prompt, I see model performs much better._
>
> _This seems to be a known issue called **constraint tax** [1]: for smaller models, hard structured-output constraints can improve schema validity while hurting task correctness._
> _Therefore, for this case study, I used a prompt-level guidance to ensure that local LLM can at least do the task properly. In a production system, I’d probably add validation and retry logic around this step._

### 2.4 Step 2: Cloud Reasoning

In this step, we send the prepared anonymous scheduling problem to the cloud LLM so that we can leverage its strong reasoning capability without disclosing any sensitive information.

We start by configuring the system instruction for the cloud LLM role:

CLOUD_REASONER_INSTRUCTIONS = """

You are a scheduling reasoner.

You receive an anonymous scheduling problem with load IDs, current time, load durations,
energy use, availability, deadlines, latest-finish constraints, and electricity tariff windows.

Your task is to decide whether the target load should start now or later,
then propose a feasible schedule for the relevant loads.

Use only the information in the scheduling problem.
Keep the anonymous load IDs exactly as given.
Do not invent device names, household details, or missing constraints.

When comparing feasible schedules, account for deadlines, latest-finish constraints,
runtime, energy use, and tariff prices.

Return your answer through the structured output schema.

Different from the previous step, we use structured output directly. Here is the output schema:

from typing import Literal
from pydantic import BaseModel, Field

class ScheduledLoad(BaseModel):
    load_id: str = Field(
        ...,
        description="Anonymous load ID from the scheduling problem, such as load_A.",
    start: str = Field(
        description="Scheduled start time in 24-hour HH:MM format.",
    end: str = Field(
        description="Scheduled end time in 24-hour HH:MM format.",
    reason: str = Field(
        description="Short reason for choosing this time window.",

class CloudScheduleReasoning(BaseModel):
    recommendation: Literal["run_now", "run_later"] = Field(
        description="Whether the target load should start now or be deferred.",
    proposed_schedule: list[ScheduledLoad] = Field(
        description="Feasible schedule using only anonymous load IDs from the prompt.",
    reasoning: str = Field(
        description="Concise reasoning based only on the anonymous scheduling facts.",

The cloud LLM will be tasked to fill in this template. Then, we build the prompt for the cloud model:

def build_cloud_reasoning_prompt(local_sanitizer_output: dict[str, Any]) -> str:
Anonymous scheduling problem:
{local_sanitizer_output['scheduling_problem']}

Target load:
{local_sanitizer_output['target_load_id']}

Decide whether the target load should start now or later,
then propose a feasible schedule for the relevant anonymous loads.

Notice that we only send the anonymous scheduling problem to the cloud LLM. No household memory or load mapping.

Finally, we call Azure OpenAI:

from openai import AzureOpenAI

# Setup cloud LLM client
cloud_client = AzureOpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    azure_endpoint=os.environ["OPENAI_API_BASE"],
    api_version=os.environ["OPENAI_API_VERSION"],

# Prepare prompt
cloud_prompt = build_cloud_reasoning_prompt(local_sanitizer_output)

response = cloud_client.responses.parse(
    model="gpt-5.4",
    instructions=CLOUD_REASONER_INSTRUCTIONS,
    input=cloud_prompt,
    reasoning={"effort": "medium"},
    text_format=CloudScheduleReasoning,

cloud_reasoning = response.output_parsed.model_dump()

At this point, the cloud model has worked out the scheduling, but the result is still expressed in anonymous load IDs. That’s why we need a final step to do the translation.

### 2.5 Step 3: Local Grounding

This final step runs locally again.

As usual, we start by configuring the system instruction for step 3 LLM. Its objective is to map the cloud result back into household language and produce the final recommendation:

LOCAL_FINALIZER_INSTRUCTIONS = """

A user asked whether to run a household load now or later.
The cloud model has already reasoned over an anonymous scheduling problem and returned a proposed schedule using load IDs.
You can see the original household context and the local mapping from anonymous load IDs back to household device names.

Your role is to write the response the user will read.
The response should answer the original now-or-later question in normal household language,
using the cloud schedule as the scheduling plan.

Use local_mapping to translate load IDs back to household device names.
Use the private household context only to make the response understandable and locally relevant.

Do not redo the scheduling optimization from scratch.
Do not imply that any appliance has already been started or scheduled automatically.
You are recommending what the user should do.

- Answer the now-or-later question first.
- Use household device names, not anonymous load IDs.
- Preserve the important timing recommendation from the cloud schedule.
- Mention other scheduled loads only when they help explain the recommendation.
- If the cloud result conflicts with the private household context, prefer the local context and say so briefly.
- Keep the response concise and focused on the user's decision.

Then we build the corresponding prompt. Here, the local model receives a couple of things:

*   Original user question;
*   Private household context;
*   Local sanitizer output;
*   Cloud reasoning result.

Here is the builder function:

def build_local_finalizer_prompt(
    local_sanitizer_output: dict[str, Any],
    cloud_reasoning: dict[str, Any],

Local sanitizer output:
{json.dumps(local_sanitizer_output, indent=2)}

Cloud reasoning:
{json.dumps(cloud_reasoning, indent=2)}

Write the final user-facing recommendation.
Answer the user's actual question first.
Use the cloud proposed schedule above and do not create another schedule.
Mention secondary loads only if they help explain the recommendation.
Keep the answer concise and focused on the decision.

Finally, we call Gemma again:

prompt = build_local_finalizer_prompt(
    local_sanitizer_output=local_sanitizer_output,
    cloud_reasoning=cloud_reasoning,

        {"role": "system", "content": LOCAL_FINALIZER_INSTRUCTIONS},
    think="medium",

final_answer = response["message"]["content"]

That’s the full implementation of our three-step workflow.

### 2.6 Running the Workflow

Now let’s run the workflow and inspect the results.

In the first step, we have used the local Gemma model to convert the private household context into an anonymous scheduling problem. Here is the output we got:

{
  "target_load_id": "load_A",
  "scheduling_problem": "Current Time: 18:30\nLoads:\n  load_A:\n    Energy Use: 1.2 kWh\n    Duration Estimate: 90 minutes\n    Earliest Start: 18:30\n    Hard Deadline (Must finish by): 06:30\n    Soft Stop Constraint (Cannot run after): 22:30\n  load_B:\n    Energy Use: 14 kWh\n    Duration Estimate: 120 minutes\n    Earliest Start: 18:30\n    Hard Deadline (Must finish by): 07:00\nTariff Schedule:\n  17:00-20:00: $0.45/kWh\n  20:00-00:00: $0.22/kWh\n  00:00-06:00: $0.12/kWh\n  06:00-17:00: $0.25/kWh",
  "local_mapping": {
    "load_A": "dishwasher",
    "load_B": "EV charger"
  }

We see that the local model correctly filtered the context. The robot vacuum was mentioned in the original household memory, but the local model correctly identified that it’s irrelevant to the current scheduling question, so it is not included.

More importantly, we see that `scheduling_problem` only contains anonymous load IDs, and the cloud LLM only receives the abstract scheduling facts like duration, energy use, deadlines, etc.

In step 2, the cloud LLM returns the anonymous schedule:

  "recommendation": "run_later",
  "proposed_schedule": [
      "load_id": "load_A",
      "start": "20:00",
      "end": "21:30"
    },
      "load_id": "load_B",
      "start": "00:00",
      "end": "02:00"
  ]

Finally, Gemma maps the result back to a user-friendly language:

You should run the dishwasher later.

To save money, wait until 8:00 PM tonight.
Starting then will allow it to finish by 9:30 PM, moving its energy use out of the most expensive time window and into a cheaper one.

The overall plan also schedules your EV charger for midnight (12:00 AM - 2:00 AM) to take advantage of the lowest electricity rates.

This is the pattern in action: we let the local model handle private context and final grounding, and the cloud model handle the heavy reasoning, but only over an anonymous problem.

## 3. Final Thoughts

The smart-home example above shows just one possibility in the larger design space of hybrid local-cloud LLM applications.

I believe the more general lesson here is that we don’t need to treat local and cloud models as two mutually exclusive deployment choices. In many applications, they can play different roles.

That is why I find it useful to ask the following three questions:

*   Who should act first, the local model or the cloud model?
*   When should the cloud model be called?
*   What does the split actually buy us?

The last question is especially important. Privacy is usually the first thing people think of, but there could be other factors, such as cost/latency, reliability, and controllability. Don’t overlook those.

To me, that is the real promise of hybrid local-cloud LLM applications: not a compromise between local and cloud, but a more flexible way to design the application itself.

## Reference

[1] Ray (2026), _The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models_. [https://arxiv.org/abs/2605.26128](https://arxiv.org/abs/2605.26128)
