---
title: Voyager: An Open-Ended Embodied Agent with Large Language Models
created: 2026-08-15
updated: 2026-08-15
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2305.16291
arxiv_id: "2305.16291v2"
published_at: 2023-10-19
captured_at: 2026-08-15
status: captured
source_quality: primary-paper-full-pdf
---

# Voyager: An Open-Ended Embodied Agent with Large Language Models

## Source metadata

- Authors: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar
- PDF reviewed: `https://arxiv.org/pdf/2305.16291`
- Extraction note: full paper reviewed, including architecture, ablations, transfer experiments, limitations and broader impacts.

## Mechanism captured from the paper

Voyager combines:

1. an automatic curriculum that proposes exploration tasks from current state and progress;
2. an executable JavaScript skill library indexed by natural-language descriptions;
3. iterative prompting that uses environment feedback, execution errors and a GPT-4 self-verification critic to revise code.

A program is admitted to the skill library only after the task is judged successful; later tasks retrieve top-ranked prior skills for reuse and composition.

## Reported evidence

- Evaluated in Minecraft through high-level Mineflayer APIs.
- The paper reports more unique items, longer travel, faster technology-tree milestones and stronger new-world task transfer than its adapted baselines.
- Ablations report large degradation when replacing the automatic curriculum, removing the skill library, or removing self-verification.
- The paper reports high top-k retrieval accuracy for its evaluated skill-description index.

## Limits stated or exposed by the paper

- GPT-4 API cost was about 15 times GPT-3.5 in the reported setting, and performance depended on stronger code generation.
- The curriculum can propose impossible tasks; generated programs can use invalid game rules or nonexistent APIs.
- The agent can get stuck and self-verification can miss valid success signals.
- The system lacked visual input and used high-level APIs rather than pixel-level control.
- Transfer to physical robots would require additional human-designed safety constraints.

## Evidence boundary

The evidence supports an environment-feedback and executable-skill accumulation pattern inside a bounded simulated environment. It does not establish safe autonomous skill promotion, reliable self-verification, or general lifelong learning across real-world domains.
