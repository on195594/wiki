# AGY read-only wiki review prompt

你是 AGY，请做只读审查。不要修改任何文件，不要提交，不要写 memory / skill / cron / MCP / runtime / wrapper / gateway / profile。只读 `/home/lin/wiki` 下列文件和必要相邻页面。

## Review target

本次新增/更新：

- `raw/articles/xda-claude-creative-workflow-reframe-2026-06-20.md`
- `concepts/ai-assumption-challenger-before-execution.md`
- `index.md`
- `log.md`

相邻概念，请重点检查是否重复或链接是否合理：

- `concepts/agent-context-engineering.md`
- `concepts/claude-code-practical-workflow-tips.md`
- `concepts/hermes-context-layer-operating-rules.md`
- `concepts/subagent-orchestration-patterns.md`

## Source context

来源文章：XDA Developers — `I use Claude to reframe my creative workflow, and it turned out to be the best creative partner`

来源 URL： https://www.xda-developers.com/use-claude-to-reframe-creative-workflow/

沉淀意图：把文章中的“Claude/AI 在执行前作为假设挑战者、怀疑者、不满意客户、反迎合思维伙伴”的原则沉淀为 wiki 概念；不推广为 active skill/default gate。

## Questions

请审查：

1. 是否过度沉淀：这篇文章是否足够支撑一个独立 concept，而不是只更新 `claude-code-practical-workflow-tips` 或 `agent-context-engineering`？
2. 最小 durable unit 是否清楚：概念是否聚焦在“执行前假设挑战”，而不是泛泛 AI 创意伙伴？
3. 来源保真：raw page 的 provenance、limitation、source quality 是否足够清楚？是否有把个人经验过度泛化为工程事实？
4. 层级边界：是否明确没有推广 memory、active skill、cron、MCP、runtime、wrapper、gateway？
5. 链接质量：wikilinks 是否指向合适 owner pages？有无应补/应删的链接？
6. index/log 是否准确表达本次变更？

## Output format

请用中文输出：

Verdict: PASS / PASS_WITH_NOTES / REQUEST_CHANGES
Blocking: <如无写 none>
Important: <重要但非阻断问题>
Minor: <小修建议>
Passes: <做得对的点>
Recommended patches: <如需补丁，给最小修改建议；不要自己改文件>
