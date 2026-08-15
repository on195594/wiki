---
title: Toolformer: Language Models Can Teach Themselves to Use Tools
created: 2026-08-15
updated: 2026-08-15
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2302.04761
arxiv_id: "2302.04761"
published_at: 2023-02-09
captured_at: 2026-08-15
status: captured
source_quality: primary-paper-full-pdf
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

## Source metadata

- Authors: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- PDF reviewed: `https://arxiv.org/pdf/2302.04761`
- Extraction note: full arXiv PDF text reviewed, including training construction, downstream tables, limitations and conclusion.

## Mechanism captured from the paper

Toolformer generates candidate API calls from a small number of demonstrations, executes them, keeps calls whose results reduce future-token prediction loss, and fine-tunes the same language model on the filtered corpus. The evaluated tools include question answering, Wikipedia search, calculator, calendar and machine translation APIs.

## Reported evidence

- The paper evaluates zero-shot downstream behavior after tool-use fine-tuning.
- It reports gains on factual, mathematical, multilingual, temporal and question-answering tasks, with some results competitive with larger models.
- Table 8 reports that adding tool-use training did not materially degrade the evaluated language-modeling perplexity when APIs were disabled.
- Benefits depend on model scale and task/tool fit; results are not uniform across all benchmarks.

## Limits stated by the paper

- No tool chaining: outputs from one API are not learned as inputs to another.
- No interactive browsing or iterative query reformulation.
- Tool-use decisions are sensitive to wording.
- Useful training examples can be sample-inefficient for some APIs.
- Tool-dependent computational cost is not part of the decision rule.

## Evidence boundary

Toolformer is evidence about training-time acquisition of tool-use behavior. It is not evidence that a runtime agent should expose every tool, use semantic Top-K routing, skip schema validation, or omit permission and cost controls.
