---
title: Agent Skills for Python: File, Code, and Class – Composed in One Provider
created: 2026-05-25
updated: 2026-05-25
type: raw-source
tags: [agent, skills, governance, architecture]
source_url: https://devblogs.microsoft.com/agent-framework/agent-skills-for-python-file-code-and-class-composed-in-one-provider/
source_site: Microsoft Dev Blogs
published: 2026-05-24
extracted: 2026-05-24
extraction_note: Article prose was extracted from Microsoft Dev Blogs public HTML article.entry-content with code blocks preserved and navigation/comment boilerplate removed.
summary_path: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260524-175728-Agent-Skills-for-Python-File-Code-and-Class-Composed-in-One-Provider-4185108-177666200-summary.md
status: captured
---

# Agent Skills for Python: File, Code, and Class – Composed in One Provider

## Provenance

- Source URL: https://devblogs.microsoft.com/agent-framework/agent-skills-for-python-file-code-and-class-composed-in-one-provider/
- Publisher: Microsoft Dev Blogs
- Published: 2026-05-24
- Extracted: 2026-05-24
- Extraction limitation: Public HTML extraction preserved article prose and code blocks; this capture is source text for local knowledge synthesis, not a Hermes implementation decision.
- Gemini summary: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260524-175728-Agent-Skills-for-Python-File-Code-and-Class-Composed-in-One-Provider-4185108-177666200-summary.md`

## Local summary

Source URL: https://devblogs.microsoft.com/agent-framework/agent-skills-for-python-file-code-and-class-composed-in-one-provider/
Source title: Agent Skills for Python: File, Code, and Class – Composed in One Provider
Extraction route: unknown
Fallback reason: corrupted_or_noisy
Source quality: full
Extraction note: Article prose was extracted from Microsoft Dev Blogs public HTML article.entry-content with code blocks preserved and navigation/comment boilerplate removed.

---

标题：Agent Skills for Python: File, Code, and Class – Composed in One Provider

一句话结论：
微软 Agent Framework 推出 Python 版本的 Agent Skills 新特性，支持开发者通过本地文件（File-based）、封装好的 Python 类（Class-based）或内存内联代码（Inline/Code-defined）三种形态自由定义智能体技能，并通过声明式的数据源组合机制（包含聚合、过滤与去重）在统一的 Provider 中进行生命周期与分发管理。

核心观点与论证：
- 观点：技能开发的多样化形态可以通过统一的 SkillsProvider 进行无缝融合与分发。
  依据/论证：作者以一个 HR 自服务智能体的演进为线索进行论证。系统起初采用基于本地目录的 onboarding-guide 技能文件（内含 SKILL.md、参考清单和 check-provisioning.py 脚本），随后直接集成外部团队以 Python 包装好的 benefits-enrollment 类技能（BenefitsEnrollmentSkill），并在发布前临时用 InMemorySkillsSource 桥接了 InlineSkill 编写的 time-off-balance 本地代码技能。这三种不同编写形态的技能均被直接传入同一个 SkillsProvider 中，证明了其架构对于多样化技能的包容性与统一调用体验。
- 观点：通过多源组合机制（Aggregating、Deduplicating、Filtering），可以对智能体能够感知的技能进行高度解耦与按需分发，无需跨团队协调。
  依据/论证：作者在代码示例中展示了 AggregatingSkillsSource 如何将 FileSkillsSource 与 InMemorySkillsSource 的技能流融合成统一的流，再通过 DeduplicatingSkillsSource 遮蔽重名的多余技能（先入为主原则），并通过 FilteringSkillsSource 使用 lambda 表达式（如过滤仅保留 approved_skills 集合中的技能）对智能体进行局部技能暴露。这证明了底层机制能够将“技能定义”与“智能体权限控制”完美剥离开来。
- 观点：在生产环境执行敏感操作时，引入人类审批机制可以建立可靠的安全防线。
  依据/论证：由于技能中的脚本（如 enroll）会写入 HR 系统或对生产 IT 基础设施（如 check-provisioning）进行操作，作者演示了在创建 Provider 时指定 require_script_approval=True 参数。此时，智能体每次试图运行脚本前都会自动暂停，并抛出一个审批请求。这证明了该设计既能保留智能体根据审批决策（如被拒后采取替代路线）进行动态推理的灵活性，又增强了系统的安全边界。

关键细节：
- 文件定义技能的结构：包含技能元数据的 SKILL.md 配置文件，包含运行逻辑的 scripts/ 子目录（如 check-provisioning.py 脚本），以及包含静态参考文档的 references/ 子目录（如 onboarding-checklist.md），其执行依赖于在 SkillsProvider 初始化时传入自定义的 script_runner。
- 脚本执行器配置：示例中 my_runner 基于 Python 的 subprocess.run 执行脚本，设定超时时间为 timeout=30，并警告此代码过于简单，在生产环境必须自行增加沙箱（sandboxing）、资源限制（resource limits）、输入验证（input validation）和日志记录（logging）。
- 类定义技能规则：继承自 ClassSkill，使用 @ClassSkill.resource 与 @ClassSkill.script 装饰器自动发现资源和可执行脚本。如果不为装饰器指定 name 参数，系统会自动将方法名的下划线（_）转换为连字符（-）作为其名称；若将 resource 装饰器与 Python 的 @property 描述符混合使用，必须确保 @property 声明在最外层（最上方）。
- 内联代码技能特性：InlineSkill 允许在应用运行时利用闭包（closure）和局部变量动态构建技能，或在读取时动态生成具有特定权限或上下文的资源。
- 智能体接入：智能体依赖 FoundryChatClient 与指定的 endpoint 进行交互（默认模型为 gpt-4o-mini），并使用 AzureCliCredential 鉴权，将 SkillsProvider 传入 Agent 的 context_providers 中。

可信度与局限：
- 高可信度事实：文章提供的 Python 代码范例非常完整，涵盖了 API 的主要命名空间、装饰器组合嵌套顺序、技能聚合/过滤/去重的链式调用方法。这些类名与逻辑直接对应了 Agent Framework 官方 Python SDK 规范，技术参考度极高。
- 局限性与潜在盲点：
  - 沙箱隔离机制缺失：虽然文章提供了 script_runner 的代码样例，但它直接使用了本地 subprocess。如果开发者在生产环境中未按作者警告的去部署沙箱环境，可能会导致智能体执行外部传入脚本时产生任意代码执行或系统提权的重大安全隐患。
  - 动态发现的 LLM 瓶颈：虽然 DeduplicatingSkillsSource 和 FilteringSkillsSource 能在代码层面对技能进行归流与清洗，但在智能体实际运行时，LLM 能否准确识别并从合并后的几十个甚至上百个技能描述中，无偏差地选择出正确的技能去路由，依然取决于底层模型本身的匹配率与幻觉控制能力。文章没有提供关于复杂技能树下匹配召回率的实测指标。

来源元数据：
- Source URL: https://devblogs.microsoft.com/agent-framework/agent-skills-for-python-file-code-and-class-composed-in-one-provider/
- 提取质量或局限：正文完整提取自微软开发者博客公开的 HTML，保留了所有的 Python 代码块与完整的 API 设计上下文，去除了模板噪声，未丢失任何底层技术逻辑。

工程复盘启发：
- [作者观点映射]：通过统一的提供者（Provider）模式解耦底层物理资产的差异。作者将文件技能、内联内存技能和打包好的类技能，在底层封装为统一的 API 契约，并通过 Composite 模式的 AggregateSource 向上提供一致的接口。这种设计提醒我们在个人或企业知识库构建时，不应局限于单一的数据输入来源，而应优先定义高层的数据/技能抽象接口，再根据演进需要灵活插入或剔除物理存储。
- [推论]：在技能开发和合并过程中，随着协作者增多，技能重名或功能重叠是必然会发生的风险。DeduplicatingSkillsSource 提供了一种“以注册顺序为主”的隐式遮蔽机制。在未来的企业级智能体技能治理实践中，仅靠代码层面的隐式去重很容易引发难以排查的“技能被意外覆盖”故障，需要配合更严格的显式命名空间划分或注册白名单机制。

可执行建议：
- 可执行建议：本文有方法启发，但暂无直接可执行建议。

## Extracted source

Source URL: https://devblogs.microsoft.com/agent-framework/agent-skills-for-python-file-code-and-class-composed-in-one-provider/
Title: Agent Skills for Python: File, Code, and Class – Composed in One Provider
Extraction note: Article prose was extracted from Microsoft Dev Blogs public HTML article.entry-content with code blocks preserved and navigation/comment boilerplate removed.

---

Python developers working with Agent Skills can now author skills as files on disk, as inline Python code, or as reusable classes – and mix them freely through composable source classes that handle discovery, filtering, and deduplication. A skill living in your local repository, one installed from your organization’s internal package index, and a quick inline bridge you wrote ten minutes ago all plug into the same provider.

This is the third post in our Agent Skills series. The first post introduced file-based skills; the second added code-defined skills, script execution, and approval for Python. This post walks through the two additions that complete the picture: class-based skills and multi-source composition .

If you’ve been following the .NET side, the companion post Agent Skills in .NET: Three Ways to Author, One Provider to Run Them covers the same capabilities for C#. Everything shown here is the Python equivalent – same concepts, idiomatic Python API.

## The scenario

Imagine you’re responsible for an HR self-service agent at your company. The first version has a single file-based skill that guides new hires through onboarding. Over the next few weeks, the HR systems team publishes a benefits enrollment skill as an installable Python package on your organization’s internal package index, and you want to slot it in next to the onboarding skill without touching existing code. Meanwhile, you learn they’re also building a time-off balance skill – but the packaged version won’t ship for another sprint. The HR data you need is already reachable through an internal client your application uses elsewhere, so you write a quick inline skill that wraps it. Once the official package lands, you swap out your bridge and move on.

Every step here is independent. Adding one skill never means rewriting another.

## Step 1: Start with a file-based skill

The onboarding guide is a skill directory with a SKILL.md file, a Python script that checks whether IT accounts have been provisioned, and a reference document containing the checklist:

```
skills/
└── onboarding-guide/
 ├── SKILL.md
 ├── scripts/
 │ └── check-provisioning.py
 └── references/
 └── onboarding-checklist.md

name: onboarding-guide
description: >-
 Walk new hires through their first-week setup checklist. Use when a new
 employee asks about system access, required training, or onboarding steps.

## Instructions

1. Ask for the employee's name and start date if not already provided.
2. Run the `scripts/check-provisioning.py` script to verify their IT accounts are active.
3. Walk through the steps in the `references/onboarding-checklist.md` reference.
4. Follow up on any incomplete items.

To let the agent execute that script, provide a script_runner when creating the SkillsProvider and pass the provider to an agent:

import os
from pathlib import Path
from agent_framework import Agent, SkillsProvider
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

def my_runner(skill, script, args=None):
 """Run a file-based script as a subprocess."""
 import subprocess, sys
 script_path = Path(script.full_path)
 cmd = [sys.executable, str(script_path)]
 if isinstance(args, list):
 cmd.extend(args)
 result = subprocess.run(
 cmd, capture_output=True, text=True, timeout=30, cwd=str(script_path.parent)
 )
 return result.stdout.strip()

# Discover skills from the 'skills' directory
skills_provider = SkillsProvider.from_paths(
 skill_paths=Path(__file__).parent / "skills",
 script_runner=my_runner,

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ.get("FOUNDRY_MODEL", "gpt-4o-mini")

client = FoundryChatClient(
 project_endpoint=endpoint,
 model=deployment,
 credential=AzureCliCredential(),

agent = Agent(
 client=client,
 instructions="You are a helpful HR self-service assistant.",
 context_providers=[skills_provider],

When a new hire asks about onboarding, the agent matches the request to the skill description, loads the instructions, and calls the provisioning script to verify account status.

The runner shown here is deliberately simple. In production, wrap it with sandboxing, resource limits, input validation, and logging.

## Step 2: Bring in a class-based skill from a Python package

A few weeks later, the HR systems team publishes contoso-skills-hr-enrollment to your internal Python package index. Class-based skills package everything – metadata, instructions, resources, and scripts – inside a single Python class. They subclass ClassSkill and rely on @ClassSkill.resource and @ClassSkill.script decorators for automatic discovery:

# Inside the contoso-skills-hr-enrollment package
import json
from textwrap import dedent
from agent_framework import ClassSkill, SkillFrontmatter

class BenefitsEnrollmentSkill(ClassSkill):
 """Enroll employees in health, dental, or vision plans."""

 def __init__(self) -> None:
 super().__init__(
 frontmatter=SkillFrontmatter(
 name="benefits-enrollment",
 description=(
 "Enroll an employee in health, dental, or vision plans. "
 "Use when asked about benefits sign-up, plan options, or coverage changes."
 ),

 @property
 def instructions(self) -> str:
 return dedent("""\
 Use this skill when an employee asks about enrolling in or changing their benefits.

 1. Read the available-plans resource to review current offerings and pricing.
 2. Confirm the plan the employee wants to enroll in.
 3. Use the enroll script to complete the enrollment.
 """)

 @ClassSkill.resource(description="Health, dental, and vision plan options with monthly pricing.")
 def available_plans(self) -> str:
 ## Available Plans (2026)
 - Health: Basic HMO ($0/month), Premium PPO ($45/month)
 - Dental: Standard ($12/month), Enhanced ($25/month)
 - Vision: Basic ($8/month)

 @ClassSkill.script(description="Enrolls an employee in the specified benefit plan. Returns a JSON confirmation.")
 def enroll(self, employee_id: str, plan_code: str) -> str:
 success = HrClient.enroll_in_plan(employee_id, plan_code)
 return json.dumps({"success": success, "employee_id": employee_id, "plan_code": plan_code})

A bare @ClassSkill.resource decorator (no arguments) uses the method name as the resource name, converting underscores to hyphens. Pass name="..." and description="..." explicitly when you want different values. The same applies to @ClassSkill.script . Resources work as regular methods or @property descriptors – when combining the two, put @property first.

Now wire the class-based skill into the same provider that already serves the file-based onboarding guide. This is where source composition comes in – import BenefitsEnrollmentSkill from the installed package and combine the sources:

from contoso_skills_hr_enrollment import BenefitsEnrollmentSkill
from agent_framework import (
 AggregatingSkillsSource,
 DeduplicatingSkillsSource,
 FileSkillsSource,
 InMemorySkillsSource,
 SkillsProvider,

skills_provider = SkillsProvider(
 DeduplicatingSkillsSource(
 AggregatingSkillsSource([
 FileSkillsSource(
 Path(__file__).parent / "skills", # file-based: onboarding guide
 InMemorySkillsSource([BenefitsEnrollmentSkill()]), # class-based: benefits enrollment from internal package
 ])

Here AggregatingSkillsSource merges the file-based and in-memory sources into a single stream, and DeduplicatingSkillsSource ensures that if two sources happen to supply a skill with the same name, the first one takes priority. The agent sees both skills in its system prompt and picks the right one based on the employee’s question – no routing logic on your side.

## Step 3: Bridge the gap with an inline skill

The HR systems team is also building a time-off balance skill, but the package won’t be published to the internal index for another sprint. The underlying data is already reachable through the shared HrDatabase client your application uses elsewhere – it’s the same source the official skill will read from. Instead of waiting, you wrap it in an inline skill defined in your application code with InlineSkill :

from agent_framework import InlineSkill, SkillFrontmatter

time_off_skill = InlineSkill(
 name="time-off-balance",
 description="Calculate an employee's remaining vacation and sick days. Use when asked about available time off or leave balances.",
 instructions=dedent("""\
 Use this skill when an employee asks how many vacation or sick days they have left.
 1. Ask for the employee ID if not already provided.
 2. Use the calculate-balance script to get the remaining balance.
 3. Present the result clearly, showing both used and remaining days.
 """),

@time_off_skill.script(description="Calculate remaining leave balance for an employee.")
def calculate_balance(employee_id: str, leave_type: str) -> str:
 # Temporary implementation - replace with the packaged skill when available
 total_days = HrDatabase.get_annual_allowance(employee_id, leave_type)
 days_used = HrDatabase.get_days_used(employee_id, leave_type)
 remaining = total_days - days_used
 return json.dumps({
 "employee_id": employee_id,
 "leave_type": leave_type,
 "total_days": total_days,
 "days_used": days_used,
 "remaining": remaining,
 })

Fold it into the existing provider alongside the other two skills:

 InMemorySkillsSource([
 BenefitsEnrollmentSkill(), # class-based: benefits enrollment from internal package
 time_off_skill, # code-defined: temporary bridge
 ]),

From the agent’s perspective, this skill looks identical to the file-based and class-based ones. When the official package eventually ships, swap out time_off_skill for the class-based version – nothing else changes.

InlineSkill also fits naturally when you need resources that execute logic at read time rather than serving static files, when skill definitions must be constructed at runtime from data (for example, a personalized skill per user session based on role or permissions), or when a skill needs to close over call-site state (local variables, closures) rather than resolve services through **kwargs .

## Step 4: Add human approval for script execution

Some of these scripts carry real weight: check-provisioning hits production infrastructure, and enroll writes to the HR system. Before going live, you’ll want a human to sign off on each script call. Set require_script_approval=True on the provider:

 time_off_skill, # code-defined: temporary time-off balance bridge
 require_script_approval=True,

With this flag set, the agent pauses whenever it wants to run a script and hands your application an approval request. You present it to a reviewer, collect a decision, and resume. If approved, execution proceeds normally. If rejected, the agent is told the call was declined and can adjust its response accordingly. For the complete approval-handling pattern, see Tool approval in the documentation.

## Why this matters

Independent skill ownership. Different teams author and publish skills on their own schedule – as directories in a shared repo or as Python packages on your internal index – and source composition stitches them together without cross-team coordination.

Grow the agent one skill at a time. Each new skill is additive. You don’t refactor existing skills to accommodate new ones; the agent selects the right skill at runtime.

Prototype quickly, replace cleanly. InlineSkill lets you ship behavior the same day you need it. When the official package arrives, the swap is a one-line change – the agent can’t tell the difference.

Human oversight where it counts. Script approval inserts a review step before any script with side effects executes – a practical safeguard for sensitive environments.

Selective exposure from shared libraries. When your organization maintains a central skill repository but individual agents should only see a subset, FilteringSkillsSource handles it with a predicate:

 FilteringSkillsSource,

approved_skills = {"onboarding-guide", "benefits-enrollment"}

 FilteringSkillsSource(
 FileSkillsSource(Path(__file__).parent / "all-skills"),
 predicate=lambda skill: skill.frontmatter.name in approved_skills,

## Wrapping up

The Python SDK for Agent Skills now gives you three authoring options – file-based, code-defined, and class-based – along with composable source classes to combine, filter, and deduplicate them however you need. Start with a skill directory, pull in a packaged class from your internal index, fill gaps with inline code, and let the provider handle the rest. Add script approval when the stakes call for it.

- 📖 Agent Skills documentation on Microsoft Learn

- 💻 Python samples on GitHub

- 🗣️ GitHub Discussions – share feedback and connect with the community
