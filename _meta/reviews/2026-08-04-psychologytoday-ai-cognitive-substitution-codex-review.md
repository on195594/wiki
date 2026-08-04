# Codex review: Psychology Today AI cognitive substitution ingestion

Verdict: PASS_WITH_MINOR_FIXES

Blocking findings: None

Important findings:

1. `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md:82-96` 将高中数学、知识工作者调查和放射科研究外推到写作、研究、专业判断及产品设计；这些应用主要是本地推论，不是原文直接证据。现有边界说明较好，但应更明确标注跨场景迁移。
2. `concepts/...:53,66` 对“技能退化”和放射科准确率的表述略显因果化；`raw/...:74,82` 中的神经科学简化表述也应明确不是 AI 导致脑损伤或长期退化的证据。

Minor findings:

1. `raw/...:26` 的 `~/.hermes/...` 摘要路径存在，但未明确标注为本机辅助证据。
2. `concepts/...:116` 使用 `refines`，但正文称其与相邻页面是“补充”关系；`related` 更符合实际所有权。与 `production-ai-agent-evaluation-framework` 的单向链接不是 schema 问题，也未造成孤立或重复。
3. 新概念的 Layer boundary 未逐项列出 prompt、provider、profile/plugin、credentials、deployment、dependencies 等层；日志已完整声明，属于文档一致性小缺口。

Accepted strengths:

- 原始页包含标题、作者、日期、URL、审核者、提取路线、摘要路径、正文、参考文献和限制说明；“substantially complete” 已明确限定为非 byte-faithful，没有无条件声称 full capture。
- 新概念形成了清晰且独立的 durable unit：compensation、scaffolding、substitution、augmentation，加上 withdrawal/contribution tests。
- 已明确区分即时表现与学习/能力形成，并对相关关系、单一试验、康复机器人类比和可及性风险作出限制。
- 与 assumption challenger、human outcome、Dijkstra 页面已有反向链接；production evaluator 仍保留生产指标与评测框架所有权。
- frontmatter、tags、wikilinks、index count、log、页面长度均通过检查；health check 为 101/101，P0/P1/P2 为空，`git diff --check` 通过。
- 当前 diff 只涉及 Wiki、`_meta/reviews` 和目标 raw/concept 文件；未发现 memory、skill/reference、prompt、runtime/config、cron、MCP、gateway、provider、profile/plugin、credentials、deployment、dependency 或外部服务变更。

Exact bounded fixes:

1. `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md:80`，在 `## Practical implications by context` 后增加一句：以下 learning/writing/professional/product 应用是基于来源机制的本地推论，不是 Psychology Today 文章直接验证的跨领域结论。
2. `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md:53`，将“却使已有技能退化、技能学错，或从未形成”收窄为“并可能伴随已有技能退化、技能学错或未形成的风险；本页不将单一来源视为长期因果证明”。
3. `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md:66`，将“显著降低”改为“文章转述一项乳腺影像研究，在错误 AI 建议条件下报告准确率由 82% 降至 45.5%；该结果不应推广为一般医疗场景或长期 deskilling 结论，原论文尚未在本次入库中独立复核”。
4. `raw/articles/psychologytoday-ai-cognitive-substitution-skill-formation-2026-08-03.md:30-36`，在限制项中补充：文中 Hebb、“use it or lose it”等神经科学表述是作者的简化解释或类比，不是 AI 导致神经损伤、长期技能退化或跨领域迁移的直接证据。
5. `raw/articles/psychologytoday-ai-cognitive-substitution-skill-formation-2026-08-03.md:26`，将 local summary 标注为“本机 local-only 辅助路径，不作为稳定长期来源”。
6. `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md:116`，将 `refines: [[ai-assumption-challenger-before-execution]]` 替换为 `related: [[ai-assumption-challenger-before-execution]]`。
7. `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md:107-112`，补充与 `log.md:13` 一致的禁止推广层列表。

Layer-boundary check: PASS

Landing recommendation: 建议按上述 bounded text-only fixes 修正后落地该 Wiki ingestion；无需新增 pilot、evaluator、monitor 或 active workflow。修正后重新运行 health check 与 `git diff --check`，并保持当前 Wiki-only 边界。
