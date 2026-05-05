---
title: AI Coding Agents Guide: A Map of the Four Workflow Types
author: Ben Batman
source_type: article
source_url: https://realpython.com/ai-coding-agents-guide/
published_at: 2026-04-29
captured_at: 2026-04-30
status: raw
---

# AI Coding Agents Guide: A Map of the Four Workflow Types

Source: Real Python
Original share link: https://share.google/JuxwaSxi5sDgRivpI
Canonical URL: https://realpython.com/ai-coding-agents-guide/
Extraction note: Captured from the canonical Real Python page DOM. Non-article navigation/footer text was omitted from this structured raw capture.

## Article summary

AI coding agents can read code, reason about changes, and act on behalf of a developer. The article argues that choosing an agent is easier when developers classify the desired workflow by interaction mode: integrated development environment (IDE), terminal, pull request (PR), or cloud.

Unlike standard chatbots that provide one-off answers, coding agents operate through a repeated loop:

1. Read relevant files and context.
2. Reason about the steps needed.
3. Act by editing files, running commands, or using tools.
4. Evaluate whether the result is sufficient.

The loop stays similar across tools, but the execution environment changes how users interact with the agent.

## IDE agents

IDE agents live inside the editor and work alongside the developer in real time. They suggest inline edits, show visual diffs, and let the user accept or reject changes without leaving the editing environment.

The article distinguishes two forms:

- AI-native IDEs such as Cursor, Windsurf, and Kiro. Some support spec-driven workflows where the user describes the task upfront.
- IDE integrations such as GitHub Copilot extension, Claude Code in VS Code, and Gemini Code Assist. These tend to support file-targeted interactive editing and refactoring.

The main advantage is real-time proximity to the code. The main caveat is privacy: cloud-backed IDE agents may send code to external services, so teams may require approved tools or local-model options such as Continue.

## Terminal agents

Terminal agents run in the shell. The developer describes a task; the agent reads files, proposes edits, and runs commands, usually with step-by-step approval.

The article positions terminal agents as strong for:

- Complex multi-file changes.
- Navigating large codebases.
- Getting up to speed in unfamiliar projects.
- Piping logs, chaining CLI tools, and running inside automation scripts.

Examples include Claude Code, Aider, Gemini CLI, OpenCode, and Codex CLI. Terminal agents provide high control in interactive mode and may support local models through tools like Ollama when proprietary code cannot leave the machine.

## Pull request agents

PR agents are asynchronous. They typically trigger when a pull request is opened or updated, run without the user watching, and leave review comments or suggested fixes.

This workflow operates on shared branches rather than local workspaces. It works as a safety net before merging: the agent may catch edge cases, missing tests, style issues, or logic problems, but human review remains the final gate.

Examples include CodeRabbit and GitHub Copilot code review. Privacy decisions often happen at the organization or repository level because these tools act on shared code hosting platforms.

## Cloud agents

Cloud agents offer the highest autonomy. The user describes a task, the agent works in a remote or managed environment, and later reports back with a branch, pull request, or prototype.

The article presents cloud agents as useful for:

- Greenfield prototyping.
- Longer tasks that should run without constant supervision.
- Clearly scoped work with reviewable output.

Examples include Devin, Claude Code on the web, Codex web, and Cursor Cloud Agents. The tradeoff is reduced real-time control and greater security/compliance sensitivity because execution happens outside the local machine. Vendor execution models differ: Anthropic-managed infrastructure, GitHub Actions ephemeral environments, or user-controlled machines.

## Category overlap

The article stresses that the four categories are workflow types, not strict product categories. A single product can span several modes:

- Claude Code can run in the terminal, editor integrations, web/cloud, and PR review paths.
- Cursor spans IDE, CLI, Cloud Agents, and Bugbot PR review.
- GitHub Copilot spans IDE, CLI, PR code review, and cloud-agent handoff.

The taxonomy describes how the developer is working, not which vendor owns the workflow.

## Common pitfalls

The article warns against three recurring mistakes:

- Assuming one agent type handles everything.
- Ignoring privacy and compliance constraints.
- Over-automating without human review.

Its practical rule is to treat coding agents as collaborators, not replacements. Match the workflow to the task, respect code privacy boundaries, and review generated code before merging or shipping.
