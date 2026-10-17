---
title: Closing surveillance detection gaps for emerging digital drug discourse with ontology-enhanced large language models
author: [Danny Valdez, Damir Cavar, Maria A. Parker, Xue-Jing Liu, Jon Agley]
source_type: journal-perspective
source_url: https://www.nature.com/articles/s44482-026-00048-0
doi: 10.1038/s44482-026-00048-0
publisher: npj Digital Public Health
published_at: 2026-10-16
captured_at: 2026-10-17
type: raw-source
tags: [llm, research]
status: raw
extraction_route: direct_html
source_quality: partial
license: CC BY-NC-ND 4.0
---

# Closing surveillance detection gaps for emerging digital drug discourse with ontology-enhanced large language models

## Provenance and capture scope

- Original article: Danny Valdez, Damir Cavar, Maria A. Parker, Xue-Jing Liu and Jon Agley. npj Digital Public Health 1, 41 (2026), published 16 October 2026. DOI: https://doi.org/10.1038/s44482-026-00048-0.
- Retrieved original publisher HTML on 2026-10-17. The original abstract and main article prose were readable; this note deliberately retains only selected original-English excerpts, not a full-article mirror or a generated summary substituted for source text.
- Extracts below retain the original wording; whitespace and presentation are normalized. Figures, bibliography, linked studies and external statistics were not independently checked. Figure captions alone do not establish the figure's contents.
- The article is a conceptual perspective/editorial, not a tested implementation. It supplies no dataset, code, head-to-head benchmark or measured accuracy/latency benefit for its proposed surveillance system.
- The original uses “tea” as a kratom referent in “The impact of semantic drift on drug surveillance models”, but as a nitazenes referent later in “Conceptual framework”. This note records the inconsistency without resolving it or endorsing either mapping as an established slang fact.
- Publisher license: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). These attributed excerpts are not a translation or adaptation of the complete article; the license does not grant permission to distribute adapted material.

## Selected original excerpts

### Conceptual framework: integrating dynamic ontologies with large language models

> Conceptually, this system operates in three stages: (1) at point of inference, the LLM retrieves matching triples to predict the classification of new or ambiguous terms, (2) when a term has no matching triple, the term is flagged as a new candidate referent rather than forced into a classification, and (3) candidate referents are held for expert review, with the source text (i.e., an individual social media entry where the term was identified), surrounding context (i.e., n-grams preceding and following the candidate term), and date of identification (i.e., to track term popularity), before being approved and added to the oRAG as a new triple.

> Model validation will be needed to confirm, for example, whether an LLM’s ontology-guided classification of an ambiguous term is both extracted correctly and classified in a manner that aligns with its pharmacologic properties.

### Data availability

> No datasets were generated or analysed during the current study.

### Acknowledgements

> We also acknowledge that no data or underlying source code was used for this conceptual perspective paper.
