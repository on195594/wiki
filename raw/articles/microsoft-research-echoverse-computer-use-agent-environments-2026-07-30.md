---
title: Echoverse: Deep, evolving environments for computer-use agents
author: Akshay Nambi, Yash Pandya, Sahil Gupta, Sarthak Harne, Archana Yadav, Kavyansh Chourasia, Yash Lara, Ahmed Awadallah, Ece Kamar
created: 2026-08-03
updated: 2026-08-03
type: raw-source
status: captured
source: Microsoft Research
source_url: https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents/
published: 2026-07-30T10:00:00-07:00
captured: 2026-08-03
extraction: Direct fetch returned HTTP 403; browser main DOM extraction recovered the complete rendered article (about 31,494 characters) and retained bounded author/share/site boilerplate; the local gsummary output is auxiliary evidence.
tags: [agent, browser, research, evaluation, validation, workflow]
---

# Echoverse: Deep, evolving environments for computer-use agents

## Provenance

- Source URL: https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents/
- Source: Microsoft Research
- Authors: Akshay Nambi, Yash Pandya, Sahil Gupta, Sarthak Harne, Archana Yadav, Kavyansh Chourasia, Yash Lara, Ahmed Awadallah, Ece Kamar
- Published: 2026-07-30T10:00:00-07:00
- Captured: 2026-08-03
- Technical report: https://www.microsoft.com/en-us/research/publication/echoverse-deep-evolving-environments-for-training-computer-use-agents-at-scale/
- Official code: https://github.com/microsoft/Echoverse
- Dataset: https://huggingface.co/datasets/microsoft/Echoverse
- Local summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260803-123849-Echoverse-Deep,-evolving-environments-for-computer-use-agents-138238-688552880-summary.md`
- Extraction note: direct deterministic fetch returned HTTP 403. Browser extraction from the verified main DOM obtained the full rendered article. This file is a structured capture, not a verbatim mirror; bounded site boilerplate was retained in the extraction source but is not reproduced below.
- Source quality: official Microsoft Research article with a linked technical report, code repository and dataset.

## Source-backed capture

The durable unit described by Echoverse is an environment coupled to tasks and a grounded verifier. The article argues that environment depth—behavioral fidelity and causal structure—matters more for transfer than simply increasing the number of pages or trajectories.

### Environment system

- Echoverse contains 12 training worlds: 10 deep domain worlds and 2 capability-focused worlds.
- The domain worlds cover communication (`EchoMail`, `EchoCalendar`, `EchoChat`), technology (`EchoML`, `EchoForge`), compliance/transactions (`EchoBank`, `EchoCare`), and community/media/travel (`EchoForum`, `EchoTunes`, `EchoStay`).
- The two capability worlds target date pickers and nested filters. The article describes six component classes across ten date-picker contexts and 20 component families for nested filters.
- The environments are compiled from React frontends and FastAPI + SQLite backends. Seed data is intended to be realistic; for example, `EchoStay` uses Inside Airbnb data and `EchoForum` contains about 2.55 million public forum comments.
- Deep environments preserve behavior across pages and users, persistent state, realistic constraints and meaningful write effects. Shallow environments expose similar-looking screens without the same causal structure.

### Grounded verifier

- Read operations are evaluated by SQL-semantic equivalence, so numerically equivalent values can pass even when their formatting differs.
- Write operations are evaluated from database row-state transitions and before/after diffs.
- Mixed read/write tasks use the lower of the read and write scores.
- This grounded verifier supplies a resettable, database-backed outcome signal for synthetic training and evaluation. It is distinct from screenshot similarity or an unconstrained visual judge.

### Reported experiments

- In controlled shallow-versus-deep comparisons with the same domain exposure, Allrecipes fell from 80.0% to 75.0% in the shallow condition, while the deep condition reached 85.0%. Hugging Face remained at 48.0% in the shallow condition and reached 65.0% in the deep condition; over-limit tasks fell from 15 to 9.
- After environment and control fixes, the completed-booking rate for `EchoStay` rose from 48% to 78%. The reported `EchoStay` score rose from 16.2% in v1 to 38.5% in v2; GPT-5.4 was reported at 50.4% on that setting.
- A Qwen3.5-9B base model averaged 36.5% before training and 67.1% after training across 14 synthetic evaluation sets. GPT-5.4 was reported at 80.7%; the article reports parity or better for the trained model on some EchoBank, EchoMail and nested-filter tasks.
- Capability-world training improved unseen-layout date-picker performance from 34.0% to 54.0%, and the unseen-combination nested-filter result reached 84.1%. Online-Mind2Web transfer rose from 29.5% to 34.3%.
- On five Echo domains, two epochs of RL using GPT-4.1 language/vision reward judges improved 25 held-out tasks from 58% to 69%.
- Reported real-web transfer included WebVoyager from 66.5% to 71.5% and GitHub tasks from 58.5% to 63.4% after EchoForge training.

### Scaling and co-evolution

- Increasing trajectories in one environment from 6,400 to 20,000 saturated or reduced real-web transfer; Mind2Web fell from 40.1% to 37.2% in the cited comparison.
- The article presents environment breadth and diversity, rather than repeated samples from one environment, as the more useful generalization lever.
- The environment, model, task and verifier are treated as co-evolving components. Failures are inspected repeatedly to distinguish model failure, broken environment controls, task defects and verifier error. Fixing the environment is therefore part of evaluation, not merely infrastructure maintenance.

## Limitations and evidence boundary

- The quantitative results are tied to Echoverse's particular synthetic worlds, task distributions, evaluation protocol and 9B model; the article does not establish the same gains for arbitrary models, business systems or production environments.
- Real-web gains are smaller than the synthetic gains in the reported transfer results. The authors attribute this partly to coverage of login- and write-heavy workflows in public benchmarks; this remains a transfer limitation, not a universal explanation.
- The RL results depend in part on GPT-4.1 and GPT-4.1 Vision reward judges, so judge preferences are an additional dependency.
- Echoverse's SFT/RL recipe, database grader and synthetic worlds are source-specific mechanisms. This capture does not turn them into a requirement for ordinary browsing or computer-use tasks.

## Reading boundary

The experiment supports a testable distinction between visible interaction progress and grounded business outcome. Applying that distinction to Hermes computer-use guidance, and deciding when an authoritative read-back is worth its cost, is an explicit `[推论]` recorded in the derived concept rather than a claim that Echoverse itself prescribes ordinary browser use.
