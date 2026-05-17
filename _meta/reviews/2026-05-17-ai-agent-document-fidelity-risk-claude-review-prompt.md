# Claude review prompt: AI Agent Document Fidelity Risk wiki ingestion

请对本次 wiki 沉淀做只读独立审查。不要修改文件。

## 背景
用户要求把 VentureBeat 文章《Frontier AI models don't just delete document content — they rewrite it, and the errors are nearly impossible to catch》沉淀为 wiki，并让 Claude 独立审查。

## 本次变更范围
- 新增 raw source: `/home/lin/wiki/raw/articles/venturebeat-frontier-ai-document-fidelity-risk-2026-05-13.md`
- 新增 concept page: `/home/lin/wiki/concepts/ai-agent-document-fidelity-risk.md`
- 更新 index/log:
  - `/home/lin/wiki/index.md`
  - `/home/lin/wiki/log.md`
- 更新 cross-links:
  - `/home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md`
  - `/home/lin/wiki/concepts/agent-self-validation-loops.md`
  - `/home/lin/wiki/concepts/typed-ai-agent-boundaries.md`

## 审查问题
1. 这个沉淀层级是否合适：raw source + concept page，而不是 skill/runtime/cron？
2. concept page 是否准确保留了原文核心：DELEGATE-52、多轮文档退化、前沿模型的隐蔽重写、通用工具加剧退化、RAG 噪声复利、可逆任务/round-trip relay？
3. 是否有过度推广、硬编码外部 benchmark、把新闻性模型排名沉淀成长期结论的问题？
4. 是否符合 wiki schema：frontmatter、sources、tags、至少 2 个 wikilinks、index/log 更新、cross-link 不过度？
5. 是否存在应修补的 blocking/important 问题？

## 输出格式
请用中文输出：

Verdict: PASS / PASS_WITH_MINOR_FIXES / NEEDS_CHANGES

Blocking:
- ...

Important:
- ...

Minor:
- ...

Recommended patches:
- ...

Evidence checked:
- ...
