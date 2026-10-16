---
title: "历史砌体监测中的 RAG 多智能体案例：证据融合与上下文敏感性"
created: 2026-10-16
updated: 2026-10-16
type: raw-source
status: captured
tags: [agent, llm, multi-agent, evaluation, monitoring]
sources: [https://www.nature.com/articles/s41598-026-57424-2]
source_title: "A RAG-enhanced multi-agent LLM/VLM framework for auditable and region-aware structural health monitoring of a historic masonry structure"
authors: [Kemal Hacıefendioğlu, Volkan Kahya, Tunahan Aslan]
publisher: Scientific Reports
published: 2026-10-15
extracted: 2026-10-16
doi: 10.1038/s41598-026-57424-2
extraction_route: direct_html
source_quality: partial
capture_type: selected-verbatim-excerpts
license: CC-BY-4.0
---

# 历史砌体监测中的 RAG 多智能体案例：证据融合与上下文敏感性

## Capture scope and attribution

- 原文：Hacıefendioğlu, K., Kahya, V. & Aslan, T. *A RAG-enhanced multi-agent LLM/VLM framework for auditable and region-aware structural health monitoring of a historic masonry structure.* Scientific Reports 16, 32428 (2026). https://doi.org/10.1038/s41598-026-57424-2
- 原文 HTML 提取后的选段，以下英文段落按原文保留；章节标题与编者说明用于定位，不是整篇镜像、生成式摘要或独立复现。省略未选段落、公式、参考文献列表及网页导航，不据此声称全文完整。
- 已读正文涵盖摘要、方法、应用、讨论、结论及数据可用性；链接表格内容、图像像素、实现代码和原始数据未独立核查。部分代码标识在 HTML 文本提取中缺失。
- 论文许可为 [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)。本笔记仅作选段与编排；图像及第三方材料仍以原文单独标注为准。
- 编者边界：这是单个宣礼塔的概念验证。没有独立、同步的损伤真实值；风险下降不等于诊断准确率提高，也不能证明评分归零的区域安全。原文关于固定与自适应融合权重的描述未完全一致，以下保留冲突，不替作者补全实现。
- 概念归纳由 [[deterministic-analytics-llm-reasoning-boundary]] 与 [[production-ai-agent-evaluation-framework]] 维护；上下文信任边界参见 [[llm-context-engineering-layer]]。

## Original excerpts — Abstract

Historic masonry structures require monitoring workflows that are non-destructive, interpretable, and robust to field variability. This paper presents a proof-of-concept, RAG-enhanced structural health monitoring (SHM) workflow demonstrated on a single historic masonry minaret case study, in which a manager–orchestrator coordinates signal analysis, visual analysis, and cross-modal fusion. Vibration data from four sensors installed on this minaret are processed through a reproducible pipeline that includes data cleaning, PSD-based baseline characterisation, adaptive windowing, robust normalisation, and anomaly screening with a 1D convolutional autoencoder trained on healthy reference data (Measurements 1–12), followed by evaluation on Measurements 13–20. Localisation is strengthened through relation-based autoencoders on sensor pairs and sensor-to-zone damage mapping. In parallel, a VLM analyses sensor-linked inspection images from the same case study, while a curated retrieval-augmented structural memory package for the monitored minaret (geometry, materials, baseline dynamics, FE notes, and inspection playbook) supports context-aware interpretation. A three-agent decision layer (Agent A: LLM+RAG, Agent B: VLM+RAG, Agent C: fusion + RAG) reconciles agreements and conflicts between signal- and image-derived evidence to produce case-specific global and zone-level risk assessments. The study compares with-RAG and without-RAG analysis modes within this single deployment and reports structured, traceable outputs, including JSON artefacts, per-image findings, per-sensor summaries, narrative reports, and final risk maps. Its main contribution is to demonstrate how signal-derived anomalies, image-derived evidence, and retrieval-grounded structural memory can be combined within a traceable multi-agent SHM workflow for one monitored historic masonry minaret.

## Original excerpts — Methodology: common zone-level evidence space

To clarify the mechanism behind this fusion process, the proposed framework projects all evidence sources into a common zone-level evidence space before the final decision stage. In this study, the minaret is represented by the zone set Z = {base, lower_shaft, transition, balcony, upper_shaft, cap}. The signal branch transforms the raw vibration records into global anomaly indicators and pairwise relation-change scores. These pairwise scores are first aggregated at sensor level and then projected to the corresponding structural zones through the predefined sensor-to-zone mapping. The visual branch transforms sensor-linked inspection images into image-level severity and confidence values, which are then aggregated into the same zone set. The RAG branch does not generate an independent numerical damage score; instead, it retrieves structural context associated with each zone, such as geometry, material characteristics, intervention history, baseline dynamic behaviour, FE-related notes, and inspection rules.

Accordingly, the information transmission pathway can be summarised as follows: vibration data are transformed into signal-based zone evidence, inspection images are transformed into visual zone evidence, and retrieved memory is transformed into contextual constraints for interpretation. The final fusion layer operates on these three aligned components: signal evidence, visual evidence, and retrieved structural context. This design avoids direct fusion of heterogeneous raw data. Instead, it performs fusion after each modality has been converted into a comparable zone-level representation. This mechanism improves interpretability because every final zone-wise risk output can be traced back to the signal branch, the visual branch, and the retrieved contextual evidence that influenced its interpretation.

## Original excerpts — Methodology: baseline and evaluation boundaries

The term “healthy-reference” is used here in an operational modelling sense. Measurements 1–12 were selected as the baseline period because they correspond to the earliest available monitoring records and showed no abrupt discontinuity or unresolved invalid-data pattern during the initial signal inspection. However, this does not imply that the structure was independently certified as damage-free during these measurement intervals. Rather, the baseline assumption is treated as a modelling condition that enables the AE to learn a reference dynamic pattern against which later observations can be compared.

It is important to clarify that the evaluation period (Measurements 13–20) is not treated as an independently labelled damage period. Rather, it is used as an out-of-sample evaluation period in which deviations from the healthy-reference baseline are examined. Since no independent time-synchronised ground-truth damage map is available for all evaluation measurements, anomaly scores obtained from this period are interpreted as risk-oriented indicators and inspection-priority evidence, not as confirmed damage labels.

## Original excerpts — Methodology: image input versus video infrastructure

It should be clarified that the video-camera-based monitoring system described here represents the broader non-contact sensing infrastructure of the project. In the final multi-agent decision layer reported in this paper, the visual branch does not use video-derived displacement or optical-flow motion features as direct inputs to Agent B. Instead, Agent B evaluates sensor-linked inspection images and produces image-level visual findings, severity values, and confidence scores. Therefore, optical-flow-based video monitoring and VLM-based image assessment should be understood as related but distinct components: the former provides the broader measurement and displacement-tracking context, whereas the latter provides the visual evidence used in the agent-wise fusion stage of the present study.

## Original excerpts — Methodology: RAG and deterministic numerical roles

In this framework, RAG is used as a context-injection layer, not as a model-update mechanism. No fine-tuning is applied, no vector database is used, and retrieval is performed through lightweight lexical matching over the project memory package using task-specific zone and evidence keywords. Quantitative differences between with-RAG and without-RAG runs are reported in the application/results part; here, we describe only the methodological role of RAG.

Therefore, the role of RAG should not be interpreted as improving the numerical reconstruction capability of the autoencoder models. The signal models are trained and evaluated independently of the retrieval layer. The contribution of RAG occurs after numerical score formation, at the interpretation and decision-support stage. In this stage, retrieved context helps determine whether a zone-level anomaly or visual cue is structurally plausible, whether it coincides with known vulnerable components or intervention-sensitive regions, and whether it may instead be explained by expected architectural texture, restoration traces, or low-confidence visual evidence. In this sense, RAG improves the plausibility, traceability, and engineering consistency of the final decision rather than directly modifying the learned signal model.

The LLM component of Agent C does not replace the numerical fusion rule. The fused zone scores are computed from the explicit signal and visual branch scores using the defined reliability-bounded weighting procedure. The LLM is then used to explain the resulting agreement, conflict, uncertainty, and action-priority patterns in a structured format. This separation is important because it keeps the numerical decision pathway reproducible while allowing the final report to include engineering reasoning and contextual explanation.

## Original excerpts — Fusion-weight ambiguity

编者定位：以下分别摘自 “Agent C (Without RAG)”、 “Agent C (Fusion + RAG)” 及应用结果。公式 (34) 另写为信号 0.75、视觉 0.25 的加权；此处不重建公式，也不将冲突解释为已查明的实现缺陷。

In the implemented workflow, the visual weight is bounded between 0.20 and 0.70, and the signal weight is computed as one minus the visual weight. Thus, the fused zone score is calculated as a weighted combination of the signal-based zone score and the VLM-based visual zone score. This design keeps the final decision anchored in dynamic-response evidence while still allowing high-confidence visual evidence to influence zone-level prioritisation. The bounds were selected as conservative engineering limits rather than optimised parameters, because independently labelled damage states were not available for data-driven calibration.

The same reliability-bounded adaptive weighting rule is retained in the RAG-enabled mode. Therefore, differences between with-RAG and without-RAG outputs arise from two coupled effects: (i) changes in Agent B visual severity/confidence values due to retrieved context, and (ii) the corresponding change in VLM reliability and visual-branch weight. Retrieved structural memory does not directly overwrite the numerical fusion formula; instead, it affects the visual evidence and reliability information that enter the fusion process. This makes the RAG-enabled fusion context-aware while keeping the arithmetic fusion rule explicit and reproducible.

Using the RAG-enabled fusion output, Agent C keeps the numerical fusion weights unchanged but updates the interpretation of visual reliability through RAG-aware contextual checks. In this run, the final global risk decreases from the without-RAG output to the with-RAG output, indicating that retrieved structural context substantially changes the decision pathway. However, this reduction should not be interpreted as proof that the RAG-assisted output is objectively more accurate, because no independent ground-truth damage map is available for the evaluation period.

## Original excerpts — Application: Agent B with RAG

From agent_b_vlm_rag.json, Agent B shows the strongest RAG-induced change. Zone scores become base = 0.00, lower shaft = 0.00, transition = 0.00, balcony = 0.571, upper shaft = 1.00, and cap = 0.00. Relative to the non-RAG run, this indicates a substantial context-induced change in visual interpretation, particularly in the base, lower shaft, and transition zones, where the scores decrease from 1.00 to 0.00, 1.00 to 0.00, and 0.912 to 0.00, respectively. Mean sensor severity also decreases from 0.686 to 0.075, while mean sensor confidence decreases from 0.875 to 0.688.

This behaviour should not be interpreted as external proof that the RAG-assisted visual output is more accurate. Rather, it indicates that the VLM-based visual branch is sensitive to the contextual information inserted into the prompt. In the RAG-enabled run, the retrieved context constrains the interpretation of visually ambiguous cues, such as façade texture, decorative bands, masonry colour variation, restoration traces, moisture-related marks, shadows, and architectural details that may resemble crack or spalling patterns. Therefore, the reduction in lower-body visual scores is interpreted as a context-constrained change in decision behaviour, not as independently verified correction of false positives.

## Original excerpts — Discussion: reported global score change and its limits

The application results show that the proposed multi-agent design produces a coherent risk narrative across signal evidence, visual evidence, and fusion logic. In the non-RAG run, Agent C reports a High global risk (0.816), with damage concentration from transition to lower-shaft/base zones. In the RAG-aware run, the final global risk decreases to Medium (0.491), indicating that a significant part of the initial high-risk marking was driven by context-free visual over-calling rather than structurally supported deterioration. This confirms that a purely score-based comparison is not sufficient; interpretation quality and evidence consistency are equally critical.

The interpretation of the RAG-induced risk reduction requires caution. In the absence of independent ground-truth damage labels, a lower risk score in the with-RAG mode cannot be treated as direct evidence of higher diagnostic accuracy. The more appropriate interpretation is that RAG changes the decision boundary of the agent system by introducing structural memory, zone semantics, intervention history, and visual ambiguity constraints. This makes the output more conservative and traceable, but it does not by itself validate the output as correct. Therefore, the with-RAG/without-RAG comparison is presented as a decision-support sensitivity analysis rather than a formal accuracy benchmark.

The strong RAG-induced change in the visual branch also indicates that VLM-based image interpretation is sensitive to prompt context. This is an expected but important characteristic of LLM/VLM-assisted workflows. Retrieval context can reduce the influence of visually ambiguous cues by reminding the model of architectural textures, restoration traces, decorative elements, and zone-specific interpretation rules. However, the same mechanism may also suppress potentially relevant visual evidence if the retrieved context is overly restrictive or if the image evidence is weakly expressed. Therefore, VLM outputs should not be treated as standalone damage labels. In this study, they are used as visual decision-support indicators and are fused with signal-based evidence under confidence and contextual constraints. Future work should evaluate visual-branch stability through prompt-variation tests, repeated image acquisition, expert-labelled visual datasets, and independent inspection records.

## Original excerpts — Discussion: global-anomaly-first gate

As defined in the methodology and applied in the case-study workflow, the global-anomaly-first gating rule helps control over-interpretation of local relation changes. Localisation outputs are considered diagnostically active only when the global AE indicates a meaningful deviation from the healthy-reference baseline. If this global condition is not satisfied, the workflow reports global stability and treats local pairwise fluctuations as inactive or low-priority indicators for that monitoring cycle. This rule improves robustness against false localisation, although it may delay the recognition of very early local deterioration that has not yet produced a measurable global anomaly.

## Original excerpts — Application and limitations: reproducibility and scope

A fixed random seed was not enforced in the original exploratory notebook; therefore, minor run-to-run variations may occur due to neural-network initialisation and mini-batch ordering. This is acknowledged as an implementation limitation. For fully deterministic replication, future code releases should fix NumPy/PyTorch random seeds and deterministic backend settings.

This study is conducted on a single historic minaret with structure-specific geometry, intervention history, and support-condition uncertainty; therefore, direct generalisation to other masonry towers should be made carefully. The evidence base is also constrained by a finite sensor network (four channels), limited image coverage per zone, and the absence of a fully independent, time-synchronised ground-truth damage map for all analysed periods. In addition, while the global-anomaly-first policy improves robustness against false localisation, it may delay detection of very early local deterioration when no global anomaly is yet visible. For this reason, periodic targeted local inspections remain necessary even during globally stable intervals.

The datasets generated and/or analyzed during the current study are available from the corresponding author on reasonable request.
