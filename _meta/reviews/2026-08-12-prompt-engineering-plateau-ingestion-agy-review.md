# AGY Read-Only Review Report

**Target Workspace**: `/home/lin/wiki`  
**Review Scope**: Uncommitted ingestion of `raw/articles/medium-kritnandan-prompt-engineering-ai-product-2026-08-09.md` and related updates across `concepts/production-ai-agent-evaluation-framework.md`, `index.md`, `log.md`, and `_meta/raw-source-hashes.json`.

---

## Verdict

`PASS_WITH_MINOR_FIXES`

---

## Blocking

`None`

---

## Important

`None`

---

## Minor

1. **Terminology precision for domain data validation (`product codes`) vs source code static analysis**
   - **Location**: [`concepts/production-ai-agent-evaluation-framework.md:L30`](file:///home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md#L30)
   - **Reason**: The raw source article states: *"The model invented product codes... validate every generated code against the actual catalog after generation"* ([`medium-kritnandan-prompt-engineering-ai-product-2026-08-09.md:L80`](file:///home/lin/wiki/raw/articles/medium-kritnandan-prompt-engineering-ai-product-2026-08-09.md#L80)). Translating "product codes" as `"虚构代码"` in Chinese creates ambiguity with programming source code. Rendering it as `"虚构产品编码"` accurately conveys validating domain product SKUs/catalog codes against an actual inventory/catalog.

---

## Passes

- **Source Provenance & Explicit Limitations** ([`raw/articles/medium-kritnandan-prompt-engineering-ai-product-2026-08-09.md:L1-L35`](file:///home/lin/wiki/raw/articles/medium-kritnandan-prompt-engineering-ai-product-2026-08-09.md#L1-L35)): Correctly preserves canonical Medium source URL, publication date (2026-08-09), capture date (2026-08-12), Jina Reader fallback extraction route, complete prose body, code examples, and 4 explicit practitioner limitations.
- **Smallest Correct Durable Unit** ([`concepts/production-ai-agent-evaluation-framework.md:L26-L33`](file:///home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md#L26-L33)): Updating the existing `production-ai-agent-evaluation-framework.md` page under `Core principle` → `Prompt plateau as a failure-layer signal` is the smallest correct durable unit. It avoids creating redundant concept pages while properly framing prompt-tuning plateaus as a signal to diagnose adjacent system failure layers.
- **Separation of Facts, Interpretations, and Hermes Scope**: Source facts (v12 82% vs v47 83% over 200 docs, 5 bug cases), author interpretations (prompting plateaus quickly, prompt tuning for system bugs is an anti-pattern), and Hermes implications (keep experience numbers as source-specific practitioner heuristics, do not elevate to Hermes defaults or active runtime/skills) are clearly segregated.
- **Source-Specific Heuristics Reserved**: The 100-input comparison, 3-point stopping heuristic, 20–50 case Eval set, and 3-attempt retry loop ceiling are explicitly marked as source-specific experience values and NOT adopted as Hermes default thresholds ([`concepts/production-ai-agent-evaluation-framework.md:L32`](file:///home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md#L32), [`log.md:L11`](file:///home/lin/wiki/log.md#L11)).
- **Preserved Schema Validity vs. Semantic Correctness Boundary**: Explicitly highlights that Schema-valid outputs do not equal semantic correctness (e.g., a hallucinated string still passes Pydantic string validation), preserving the requirement for downstream semantic, evidence, and business-rule validation ([`concepts/production-ai-agent-evaluation-framework.md:L32`](file:///home/lin/wiki/concepts/production-ai-agent-evaluation-framework.md#L32)).
- **System Boundaries & Adjacent Owner Page Alignment**: Respects and cross-references adjacent concepts including [`typed-ai-agent-boundaries.md`](file:///home/lin/wiki/concepts/typed-ai-agent-boundaries.md), [`agent-failure-closed-loop-evaluation.md`](file:///home/lin/wiki/concepts/agent-failure-closed-loop-evaluation.md), [`agent-self-validation-loops.md`](file:///home/lin/wiki/concepts/agent-self-validation-loops.md), [`production-agent-evaluation-baselines.md`](file:///home/lin/wiki/concepts/production-agent-evaluation-baselines.md), and [`deterministic-analytics-llm-reasoning-boundary.md`](file:///home/lin/wiki/concepts/deterministic-analytics-llm-reasoning-boundary.md).
- **Coherence Across Artifacts**:
  - `_meta/raw-source-hashes.json`: SHA-256 hash (`2cff78c65c163b9b0258742a75f96f8fa9e26bb59e87d43e7c85010dffcfa892`) matches the raw file exactly.
  - `index.md`: Title count (110) and concept summary updated accurately ([`index.md:L40`](file:///home/lin/wiki/index.md#L40)).
  - `log.md`: Chronological log entry conforms to standard schema format ([`log.md:L6-L13`](file:///home/lin/wiki/log.md#L6-L13)).
  - `wiki_health_check.py`: Passed cleanly with zero P0/P1/P2 link, frontmatter, or index issues.
- **Zero Active-Layer Over-Promotion**: No changes were made to active skills, prompts, memory, runtime, cron, MCP, gateway, or wrappers.

---

## Recommended patches

```diff
--- a/concepts/production-ai-agent-evaluation-framework.md
+++ b/concepts/production-ai-agent-evaluation-framework.md
@@
-文章给出的五类案例把这个诊断原则具体化：JSON 外包装由解析和类型校验处理；虚构代码由真实目录校验拦截；不可违反的权限规则在执行前由代码检查；畸形工具参数在调用前做 Schema 校验并把具体错误反馈给有界重试；硬性展示长度由生成上限和渲染器边界控制。它们共同支持一个边界：主观表达、语气和难以形式化的示例适合 Prompt；可判定真假的约束应尽量进入确定性代码和验证器。
+文章给出的五类案例把这个诊断原则具体化：JSON 外包装由解析和类型校验处理；虚构产品编码由真实目录校验拦截；不可违反的权限规则在执行前由代码检查；畸形工具参数在调用前做 Schema 校验并把具体错误反馈给有界重试；硬性展示长度由生成上限和渲染器边界控制。它们共同支持一个边界：主观表达、语气和难以形式化的示例适合 Prompt；可判定真假的约束应尽量进入确定性代码和验证器。
```

---

## Parent verification and disposition

- Verified the cited raw-source sentence directly: the source says “The model invented product codes” and validates them against the actual catalog.
- Accepted the sole minor finding because `虚构产品编码` removes the source-code ambiguity without changing the claim.
- Pre-review hash comparison confirmed AGY made no changes to the reviewed files or prompt; all six hashes remained identical after the read-only run.
- Blocking findings: 0; important findings: 0; accepted minor fixes: 1; rejected findings: 0.
