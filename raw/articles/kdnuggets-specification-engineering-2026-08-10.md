---
title: Specification Engineering: The New Skill After Prompt Engineering
author: Kanwal Mehreen
source: KDnuggets
source_url: https://www.kdnuggets.com/specification-engineering-the-new-skill-after-prompt-engineering
published: 2026-08-10
captured: 2026-08-18
type: raw-source
status: raw
tags: [llm, ai-coding, workflow, software-engineering]
extraction: full rendered article body from div#post-, with promotional and related-post boilerplate removed
---

# Specification Engineering: The New Skill After Prompt Engineering

## Source

- URL: https://www.kdnuggets.com/specification-engineering-the-new-skill-after-prompt-engineering
- Author: Kanwal Mehreen, KDnuggets Technical Editor & Content Specialist
- Published: 2026-08-10
- Captured: 2026-08-18
- Extraction route: rendered browser DOM, exact KDnuggets `div#post-` container
- Source quality: full article body
- Limitation: this is a cleaned rendered-text capture rather than a byte-for-byte HTML mirror. Promotional inserts and the trailing “More On This Topic” list were removed. Research figures and vendor claims remain secondary-source statements and require checking against the cited papers or official reports before becoming normative Hermes rules.
- Local Chinese summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260818-155804-Specification-Engineering-The-New-Skill-After-Prompt-Engineering-472993-186899200-summary.md`

## Captured article

For the last two years, people have learned to get better results from large language models (LLMs) by writing clearer prompts: add context, define the role, give examples, specify the format, and iterate. This is still useful. But as AI moves from chatbots to coding agents, research assistants, data science copilots, and autonomous workflows, "good prompting" is no longer enough.

The new skill is specification engineering: the ability to define the goal, constraints, expected outputs, edge cases, tests, success criteria, and failure modes of an AI-assisted task. In simple terms:

Prompt engineering is how you ask. Specification engineering is how you define what "done correctly" means.

## Why Prompt Engineering Is Not Enough

A prompt can produce a good-looking answer. A specification defines whether that answer is actually acceptable.

This distinction matters because modern AI systems are not just generating paragraphs. They are writing SQL queries, modifying codebases, analyzing spreadsheets, producing structured JSON, building applications, and making multi-step decisions. In these settings, the main problem is not only "Can the model respond?" It is:

- Did it satisfy the requirement?
- Did it respect the constraints?
- Did it handle edge cases?
- Can the output be validated?
- Can another system consume the result?
- Did it optimize the wrong thing?

That last question is especially important. AI safety researchers have long studied specification gaming, where an AI system satisfies the written objective while missing the intended outcome.

This is the same problem we now see in everyday AI work. Ask an AI coding agent to "fix the bug," and it may produce a patch that passes a visible test but breaks a hidden assumption. Ask a model to "summarize this report," and it may produce a fluent summary while omitting the one metric leadership actually needed. Ask it to "clean this dataset," and it may silently drop rows that should have been investigated.

The prompt worked. The specification failed.

## What Specification Engineering Means

Specification engineering is the practice of turning a vague task into an executable, testable, reviewable instruction set.

A weak prompt says:

> Analyze this customer churn dataset and give me insights.

A better specification says:

> Analyze this customer churn dataset. Identify missing values, class imbalance, leakage risk, and top predictive features. Split the data into train/test before preprocessing. Compare logistic regression, random forest, and XGBoost. Report accuracy, precision, recall, F1, ROC-AUC, PR-AUC, and a confusion matrix. Do not claim causality. Include three business recommendations linked only to observed correlations.

The second version does more than prompt. It defines the work.

A good specification usually includes:

- Objective: What should the model achieve?
- Context: What does the model need to know?
- Inputs: What data, files, tools, or assumptions are allowed?
- Output format: What should the final answer look like?
- Constraints: What should the model avoid?
- Evaluation criteria: How will we judge correctness?
- Edge cases: What could go wrong?
- Verification steps: What tests or checks must pass?

This is why specification engineering feels closer to product management, software testing, data validation, and research design than traditional prompting.

## The Research Is Already Pointing This Way

A 2024 paper on Requirement-Oriented Prompt Engineering argues that much prompt training focuses on tricks like role-play or "think step by step," while complex LLM use depends more on clear requirement articulation. In a randomized study with 30 novices, their ROPE training improved users' requirement-writing ability by 20%, compared with 1% for conventional prompt engineering training. The authors also found a direct relationship between the quality of input requirements and the quality of LLM outputs.

We see the same trend in production AI tools. OpenAI's Structured Outputs feature lets developers constrain model responses to match a JSON schema, with strict schema adherence reported in its own evals. This is specification engineering in API form: instead of hoping the model returns valid JSON, the developer defines the structure the output must obey.

OpenAI's Model Spec and Anthropic's Constitution show the same idea at the model-behavior level. OpenAI describes the Model Spec as a document that specifies how its models should behave in ChatGPT and the API, while Anthropic's Constitutional AI uses written principles to guide model behavior.

In other words, the AI industry itself is moving from prompts to specifications.

## From Vibe Coding to Spec-Driven Coding

The difference becomes very clear in AI coding.

A prompt-engineering approach might say:

> Build me a simple expense tracker app.

A specification-engineering approach says:

> Build a React expense tracker with add, edit, delete, category filter, monthly total, and local storage persistence. Validate that amount is positive, date is required, and category is selected. Include unit tests for adding, deleting, filtering, and total calculation. Do not use external paid APIs. Return the file structure first, then implement one file at a time.

The second version gives the AI less room to improvise in dangerous ways.

This matters because software engineering benchmarks are increasingly built around real issues, tests, and validation. SWE-bench, for example, evaluates whether models can resolve real GitHub issues by editing codebases, not just produce isolated code snippets. OpenAI's SWE-bench Verified was created as a human-validated subset to more reliably evaluate real-world software issue solving.

Even then, tests are not perfect. A study of agent-generated patches on SWE-bench Verified found that even patches passing tests could differ meaningfully from human patches, showing limitations in benchmark test coverage. Another paper, SWT-Bench, found that generated tests can act as an effective filter for proposed code fixes, doubling the precision of SWE-Agent.

## The New Workflow

The future AI workflow will look less like this:

> prompt → output → manually fix

and more like this:

> specification → generation → validation → revision → audit

For example:

1. Write the task specification.
2. Ask the AI to identify missing requirements.
3. Ask it to generate the solution.
4. Run tests or checks.
5. Ask it to revise only against failed checks.
6. Log the final assumptions and limitations.

This is especially important for agentic systems. OpenAI's practical agent guidance recommends breaking down dense resources into smaller, clearer steps and ensuring every step maps to a specific action or output. That is specification engineering applied to workflows.

Google's DORA research also supports this direction. The report surveyed nearly 5,000 technology professionals and concluded that AI acts as an amplifier of existing organizational strengths and weaknesses. Strong platforms and quality processes help teams get more value from AI. Weak processes are amplified too.

That should be a warning. AI does not remove the need for engineering discipline. It increases the payoff from having it.

## Final Thoughts

Prompt engineering is not dead. It is becoming part of a larger discipline.

The early AI era rewarded people who could get better answers from chatbots. The next era will reward people who can design reliable AI work: tasks with clear requirements, structured outputs, evaluation checks, and explicit boundaries.

The skill is no longer just asking:

> How do I get the model to answer?

It is asking:

> How do I define the task so the model, the user, and the evaluator agree on what a correct answer is?

That is specification engineering. And as AI systems become more autonomous, it may become one of the most important technical skills after prompt engineering.

Kanwal Mehreen is a machine learning engineer and a technical writer with a profound passion for data science and the intersection of AI with medicine. She co-authored the ebook "Maximizing Productivity with ChatGPT". As a Google Generation Scholar 2022 for APAC, she champions diversity and academic excellence. She's also recognized as a Teradata Diversity in Tech Scholar, Mitacs Globalink Research Scholar, and Harvard WeCode Scholar. Kanwal is an ardent advocate for change, having founded FEMCodes to empower women in STEM fields.
