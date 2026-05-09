---
title: 23 Tips for Smart Claude Code Token Saving
created: 2026-05-09
type: raw-source
source_type: article
source: Analytics Vidhya
source_url: https://www.analyticsvidhya.com/blog/2026/05/tips-for-claude-code-token-saving/
author: Harsh Mishra
published: 2026-05-08
captured: 2026-05-09
status: captured
limitations: Direct HTML extraction required slicing from full page text; minor site boilerplate may have been removed manually. Tool/version-specific commands require verification before operational use.
---

# 23 Tips for Smart Claude Code Token Saving

## Provenance
- Source: Analytics Vidhya
- Author: Harsh Mishra
- Published/updated: 2026-05-08
- URL: https://www.analyticsvidhya.com/blog/2026/05/tips-for-claude-code-token-saving/
- Captured: 2026-05-09
- Extraction note: direct HTML body text was sliced from the article intro through conclusion. Cookie/navigation/recommendation/footer text was excluded where identifiable.

## Raw extracted article text

Using Claude Code in large projects can lead to skyrocketing token costs. A 2025 Stanford study reveals developers waste thousands of tokens daily, draining budgets as unchecked context limits pile up. By setting strict boundaries from the outset, teams can reduce costs without compromising code quality. Optimizing token usage and context window sizes early on ensures efficiency and keeps projects on track. In this article, we’ll break down the key steps to take to save Claude Code tokens and manage your API costs.
Table of contents
The Core Concept
High-Impact Tactics for Context Management
Instruction and File Optimization
Tool and Output Limits
Model and Agent Strategies
File Access and Workflow Control
Recommended Configurations
Optimal Prompt Template
Conclusion
Frequently Asked Questions
The Core Concept
As your chat context expands, so do token costs. This includes not only file reads and command outputs but also system instructions and chat history. According to Anthropic, token costs increase as the context size grows. To avoid unnecessary expenses, it’s crucial to keep your working context compact. By optimizing your context window sizes from the start, you can better manage token usage and keep costs in check across projects.
High-Impact Tactics for Context Management
1. Clear the Chat Between Tasks
Clear your chat when switching tasks. Type
/clear
to start a fresh session. This prevents old debugging logs from wasting tokens. You reduce Claude Code cost by starting fresh.
Use:
/rename auth-debug-apr30
/clear
Resume later:
/resume
2. Compact the Context for Continuity
Use the
/compact
command for long tasks. This action summarizes the chat. It keeps the thread but drops old data. This boosts Claude Code token saving efforts.
Add custom instructions to
CLAUDE.md
:
# Compact instructions
When compacting, preserve:
- current task goal
- files changed
- commands already run
- failing tests and exact errors
- decisions made
- next action list
Drop:
- old exploration paths
- repeated logs
- irrelevant discussion
In the Claude code use
/compact
3. Lower the Auto-Compact Threshold
Compact the chat sooner than the default limit. Claude compacts near 95 percent capacity. Set an override to 70 for normal work.
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=70
Use 50 for noisy workflows.
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50
This tactic helps you manage token usage.
4. Monitor Usage Metrics
Watch your limits with specific commands. Type
/context
to see what consumes space. Type
/usage
to track your session spend. Run these before large tasks to optimize context window space.
5. Add a Live Status Line
Add a status line to your terminal. This shows live context percentage and model costs. It prevents unexpected token spikes. This improves your AI coding assistant experience.
Use this JSON configuration in ~/.claude/settings.json file
{
"statusLine": {
"type": "command",
"command": "jq -r '\"[\\(.model.display_name)] \\(.context_window.used_percentage // 0)% context\"'"
}
Or you can have Claude Code create this for you automatically by running this command inside the Claude Code chat:
/statusline show model name and context percentage
Also Read: Top 28 Claude Shortcuts that will 10X your Speed
Instruction and File Optimization
6. Shrink Your Global Instructions
Keep your main instruction file short. Anthropic suggests keeping CLAUDE.md under 200 lines. Big files cost tokens every session. Store only crucial facts there. This strategy improves Claude Code token saving.
# Project essentials
- Package manager: pnpm
- Test command: pnpm test
- Typecheck: pnpm typecheck
- Main app code: src/
- API handlers: src/api/
- Do not edit generated files in src/generated/
7. Use Path-Scoped Rules
Use path-scoped rules instead of global ones. Place specific rules in folders.  These load only when Claude edits matching files. You reduce Claude Code cost by hiding irrelevant instructions.
---
paths:
- "src/api/**/*.ts"
---
# API rules
- Validate all request inputs.
- Use the standard error response shape.
- Add tests for authorization failures.
To use path-scoped rules in Claude Code , you should add them to a markdown file within the .claude/rules/ directory of your project.
Create a new .md file inside the rules folder. A common naming convention is to name it after the subsystem it governs:
.claude/rules/api-validation.md (or any name ending in .md).
8. Isolate Specialized Workflows
Move specialized workflows into distinct skills. Skills load on demand. Add a disable flag to hide them until needed. This keeps the prompt clean. It helps you manage token usage.
You can add Claude SKILL in .claude/skills/<skill-name>/SKILL.md (at your project root) or even add Global skills in global .claude/ folder.
---
name: fix-issue
description: Fix a GitHub issue by number
disable-model-invocation: true
allowed-tools: Bash(gh *) Bash(pnpm test *) Read Grep Edit
---
Fix GitHub issue $ARGUMENTS.
Steps:
1. Use gh issue view to read the issue.
2. Identify the smallest relevant files.
3. Write or update tests first.
4. Implement the fix.
5. Run the targeted test.
6. Summarize files changed.
Invoke it using:
/fix-issue 123
Tool and Output Limits
9. Prefer CLI Tools
Prefer CLI tools over server tools. Anthropic favors standard tools over MCP servers. CLI tools cause less overhead. Disable unused MCP servers at once. This streamlines your AI coding assistant.
Good prompt:
Use
gh
to inspect PR 42 and return only the failing check names.
10. Cap Server Output
Cap your tool output sizes. Tool outputs flood your chat context. Set the maximum limit to 8000. You optimize context window space this way.
export MAX_MCP_OUTPUT_TOKENS=8000
11. Cap Terminal Output
Cap your terminal command output. Long test logs drain tokens fast. Set the bash output length to 20000. This secures Claude Code token saving.
export BASH_MAX_OUTPUT_LENGTH=20000
12. Filter Logs
Filter log outputs before Claude sees them. Do not feed raw logs into the chat. Use basic commands to extract error lines. This step helps reduce Claude Code cost.
pnpm test 2>&1 | grep -A 5 -E "FAIL|ERROR|Error|failed" | head -120
If you want to start a full session with the filtered logs pre-loaded into the context, pipe the output into the standard claude command.
Start the Claude Code with the following command
pnpm test 2>&1 | grep -A 5 -E "FAIL|ERROR|Error|failed" | head -120 | claude
Model and Agent Strategies
13. Deploy Subagents
Deploy subagents for verbose research tasks. Subagents handle heavy reading in an isolated space. They return clean summaries to the main chat. This helps you manage token usage.
Use a subagent to inspect the failing auth tests and logs. Return only:
1. failing test names
2. likely root cause
3. files that need edits
4. shortest fix plan
If you perform let’s say an investigator task frequently, you can define a permanent subagent by creating a MD file at .claude/agents/investigator.md
After saving, you can simply type
/investigator "auth tests are failing"
to trigger the workflow.
Or simply you can use Claude to generate this
Use
/agents
in Claude Code.
Press left key to go to Library and select create new agent.
Then select Personal or Project Scope and then Generate with Claude.
14. Pick Cheaper Models
Select cheaper models for standard work. Sonnet handles most daily coding tasks. It costs less than Opus. Reserve Opus for deep architectural reasoning. This fits a smart AI coding assistant workflow.
claude --model haiku
15. Lower the Effort Level
Lower the effort level for simple tasks. Low effort runs fast and costs less. Use medium effort for standard coding. Avoid the max setting. This supports Claude Code token saving.
/effort low
16. Disable Extended Thinking
Disable extended thinking for simple edits. Thinking tokens count as output tokens. Set a strict token cap for basic tasks. You reduce Claude Code cost a lot this way.
export CLAUDE_CODE_DISABLE_THINKING=1
17. Use Code Plugins
Install code intelligence plugins for typed languages. These plugins provide accurate symbol navigation. Claude skips reading irrelevant files. You optimize context window limits with this tactic.
File Access and Workflow Control
18. Deny Noisy Files
Deny access to noisy project files. Edit your local settings file. Block access to logs and build folders. Claude cannot discover these ignored files. This protects your AI coding assistant process.
Open ~/.claude/settings.json and Merge the JSON into your existing file
{
"permissions": {
"deny": [
"Read(./.env)",
"Read(./.env.*)",
"Read(./secrets/**)",
"Read(./node_modules/**)",
"Read(./dist/**)",
"Read(./build/**)",
"Read(./coverage/**)",
"Read(./.next/**)",
"Read(./tmp/**)",
"Read(./logs/**)",
"Read(./*.log)"
]
}
19. Avoid Broad Scans
Do not ask Claude to read the whole repository. Vague prompts trigger massive file scans. Give exact file names instead. This simple rule helps manage token usage.
Good prompt:
The login redirect fails. Start with src/auth/session.ts. Read only related files.
20. Provide Verification Targets
Provide verification targets up front. Tell Claude how to check its work. Provide expected outputs and exact test names. This prevents correction loops and aids Claude Code token saving.
21. Course-Correct the Model
Course-correct the model early in the process. Interrupt Claude if it reads irrelevant files. Rewind the session to a safe point. You reduce Claude Code cost by stopping bad paths.
22. Use a Shorter System Prompt
Use a shorter system prompt for Opus 4.7 . Enable this hidden setting with care. It drops long tool descriptions. This trick helps optimize context window space.
export CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=1
23. Remove Git Instructions
Remove built-in git rules if needed. Disable default
git
flows. Do this only if you use custom workflows. It shrinks the baseline prompt for your AI coding assistant.
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1
Recommended Configurations
Use this local setup for standard coding tasks:
{
"permissions": {
"deny": [
"Read(./.env)",
"Read(./.env.*)",
"Read(./secrets/**)",
"Read(./node_modules/**)",
"Read(./dist/**)",
"Read(./build/**)",
"Read(./coverage/**)",
"Read(./.next/**)",
"Read(./tmp/**)",
"Read(./logs/**)",
"Read(./*.log)"
]
},
"env": {
"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "70",
"BASH_MAX_OUTPUT_LENGTH": "20000",
"MAX_MCP_OUTPUT_TOKENS": "8000",
"CLAUDE_CODE_EFFORT_LEVEL": "medium"
}
Use this setup for aggressive savings:
{
"env": {
"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
"BASH_MAX_OUTPUT_LENGTH": "12000",
"MAX_MCP_OUTPUT_TOKENS": "5000",
"CLAUDE_CODE_EFFORT_LEVEL": "low"
}
Optimal Prompt Template
Follow this template format to save tokens:
Task: Fix [specific bug] in [specific files].
Scope:
- Start with: [file1], [file2]
- Do not scan the whole repo.
- Only read additional files if they are imported.
Token discipline:
- Keep command output short.
- Filter test output to failures only.
- Summarize findings before editing.
- If context exceeds 70%, compact the chat.
Verification:
- Add or update targeted tests.
- Run only the relevant test file first.
- Run broader tests after the targeted test passes.
Things to Avoid
Do not rely on outdated ignore files. The system deprecates these old settings. Use the deny permissions setting instead.
Do not install every available plugin. Extra plugins add constant overhead. Disable unused tools to maintain speed.
Do not always default to the most expensive model. Use Opus for complex tasks. Rely on Sonnet for your daily workflow.
Also Read: Claude Skills Explained: Use Custom Skills on Claude Code
Conclusion
Taking control of your tools builds confidence in your project and helps secure your budget. Managing token usage properly sharpens your AI assistant and makes development more efficient and cost-effective. Teams that optimize context window space can reduce API costs significantly. Setting clear boundaries: like clearing chats, restricting file access, and writing concise prompts, leads to real savings. By applying these strategies to your next project, you’ll improve both your budget and code quality.
Frequently Asked Questions
Q1. How do I start a fresh conversation context?
A. Type the /clear command in your terminal. This drops all previous context and starts fresh.
Q2. Why does Claude read too many files?
A. Vague prompts trigger massive codebase scans. Provide precise file names to restrict the search scope.
Q3. How do I stop massive test logs?
A. Set the
BASH_MAX_OUTPUT_LENGTH
limit in your environment. Filter test outputs with standard bash tools.
Harsh Mishra
Harsh Mishra is an AI/ML Engineer who spends more time talking to Large Language Models than actual humans. Passionate about GenAI, NLP, and making machines smarter (so they don’t replace him just yet). When not optimizing models, he’s probably optimizing his coffee intake. 🚀☕
AI Agents Generative AI Intermediate
Login to continue reading and enjoy expert-curated content.
Keep Reading for Free
Free Courses
0
AI Interview Questions & Answers Masterclass
Master AI interview questions with expert answers.
0
Agentic AI Masterclass: Building Multi-Agent Systems with AutoGen, LangGraph & CrewAI
Build multi-agent systems using AutoGen, LangGraph, CrewAI.
0
Graph RAG: Build Knowledge Graph Powered Retrieval Systems
Build Graph RAG systems using knowledge graphs.
4.7
Advanced Strands Agents with MCP
Build enterprise-grade agentic AI using Strands SDK and MCP.
4.5
LangChain Fundamentals
Learn LangChain fundamentals, LCEL, and LangGraph to build LLM apps.
Recommended Articles
GPT-4 vs. Llama 3.1 – Which Model is Better?
Llama-3.1-Storm-8B: The 8B LLM Powerhouse Surpa...
A Comprehensive Guide to Building Agentic RAG S...
Top 10 Machine Learning Algorithms in 2026
45 Questions to Test a Data Scientist on Basics...
90+ Python Interview Questions and Answers (202...
8 Easy Ways to Access ChatGPT for Free
Prompt Engineering: Definition, Examples, Tips ...
What is LangChain?
What is Retrieval-Augmented Generation (RAG)?
Responses From Readers
Cancel reply
Become an Author
Share insights, grow your voice, and inspire the data community.
Reach a Global Audience
Share Your Expertise with the World
Build Your Brand & Audience
Join a Thriving AI Community
Level Up Your AI Game
Expand Your Influence in Genrative AI
Flagship Programs
GenAI Pinnacle Program | GenAI Pinnacle Plus Program | AI/ML BlackBelt Program | Agentic AI Pioneer Program
Free Courses
Generative AI | DeepSeek | OpenAI Agent SDK | LLM Applications using Prompt Engineering | DeepSeek from Scratch | Stability.AI | SSM & MAMBA | RAG Systems using LlamaIndex | Building LLMs for Code | Python | Microsoft Excel | Machine Learning | Deep Learning | Mastering Multimodal RAG | Introduction to Transformer Model | Bagging & Boosting | Loan Prediction | Time Series Forecasting | Tableau | Business Analytics | Vibe Coding in Windsurf | Model Deployment using FastAPI | Building Data Analyst AI Agent | Getting started with OpenAI o3-mini | Introduction to Transformers and Attention Mechanisms
Popular Categories
AI Agents | Generative AI | Prompt Engineering | Generative AI Application | News | Technical Guides | AI Tools | Interview Preparation | Research Papers | Success Stories | Quiz | Use Cases | Listicles
Generative AI Tools and Techniques
GANs | VAEs | Transformers | StyleGAN | Pix2Pix | Autoencoders | GPT | BERT | Word2Vec | LSTM | Attention Mechanisms | Diffusion Models | LLMs | SLMs | Encoder Decoder Models | Prompt Engineering | LangChain | LlamaIndex | RAG | Fine-tuning | LangChain AI Agent | Multimodal Models | RNNs | DCGAN | ProGAN | Text-to-Image Models | DDPM | Document Question Answering | Imagen | T5 (Text-to-Text Transfer Transformer) | Seq2seq Models | WaveNet | Attention Is All You Need (Transformer Architecture) | WindSurf | Cursor
Popular GenAI Models
Llama 4 | Llama 3.1 | GPT 4.5 | GPT 4.1 | GPT 4o | o3-mini | Sora | DeepSeek R1 | DeepSeek V3 | Janus Pro | Veo 2 | Gemini 2.5 Pro | Gemini 2.0 | Gemma 3 | Claude Sonnet 3.7 | Claude 3.5 Sonnet | Phi 4 | Phi 3.5 | Mistral Small 3.1 | Mistral NeMo | Mistral-7b | Bedrock | Vertex AI | Qwen QwQ 32B | Qwen 2 | Qwen 2.5 VL | Qwen Chat | Grok 3
AI Development Frameworks
n8n | LangChain | Agent SDK | A2A by Google | SmolAgents | LangGraph | CrewAI | Agno | LangFlow | AutoGen | LlamaIndex | Swarm | AutoGPT
Data Science Tools and Techniques
Python | R | SQL | Jupyter Notebooks | TensorFlow | Scikit-learn | PyTorch | Tableau | Apache Spark | Matplotlib | Seaborn | Pandas | Hadoop | Docker | Git | Keras | Apache Kafka | AWS | NLP | Random Forest | Computer Vision | Data Visualization | Data Exploration | Big Data | Common Machine Learning Algorithms | Machine Learning | Google Data Science Agent
Company
About Us
Contact Us
Careers
Discover
Blogs
Expert Sessions
Learning Paths
Comprehensive Guides
Learn
Free Courses
AI&ML Program
Pinnacle Plus Program
Agentic AI Program
Engage
Hackathons
Events
Podcasts
Contribute
Become an Author
Become a Speaker
Become a Mentor
Become an Instructor
Enterprise
Our Offerings
Trainings
Data Culture
AI Newsletter
Terms & conditions Refund Policy Privacy Policy Cookies Policy © Analytics Vidhya 2026.All rights reserved.
SKIP
Continue your learning for FREE
Login with Google Login with Email Forgot your password?
I accept the Terms and Conditions
Receive updates on WhatsApp
Enter email address to continue
Email address
Get OTP
Enter OTP sent to
Edit
Wrong OTP.
Enter the OTP
Resend OTP
Resend OTP in 45s
Verify OTP
