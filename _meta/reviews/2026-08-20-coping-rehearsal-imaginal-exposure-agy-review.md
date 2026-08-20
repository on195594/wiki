## Verdict
`PASS_WITH_NOTES`

---

## Blocking
`None`

---

## Important
`None`

---

## Minor

1. **Chronological placement in [`log.md`](file:///home/lin/wiki/log.md#L1523-L1531)**
   - **File & Location**: [`log.md:L1523-1531`](file:///home/lin/wiki/log.md#L1523-L1531)
   - **Issue**: In [`log.md`](file:///home/lin/wiki/log.md), all entries from July 2026 to August 19, 2026 follow reverse-chronological order placed at the top of the file (lines 6–450+). The new `[2026-08-20]` ingestion entry was appended to the very bottom of [`log.md`](file:///home/lin/wiki/log.md) (after the historical `[2026-07-11]` entry).
   - **Impact**: Non-blocking cosmetic inconsistency in log file ordering. Moving the `[2026-08-20]` block under the top header restores uniform reverse-chronological order.

2. **Raw provenance under `## Relations` `depends_on`**
   - **File & Location**: [`concepts/coping-skill-application-and-imaginal-exposure.md:L97-L100`](file:///home/lin/wiki/concepts/coping-skill-application-and-imaginal-exposure.md#L97-L100)
   - **Issue**: Line 99 lists `- depends_on: [[donald-robertson-mentally-rehearse-coping-2026-08-18]]`.
   - **Reasoning**: Per [`SCHEMA.md:L79`](file:///home/lin/wiki/SCHEMA.md#L79) (*"`Relations` records semantic links between wiki pages. Evidence still belongs in `sources`"*) and [`concepts/hermes-wiki-page-writing-standards.md:L91-L97`](file:///home/lin/wiki/concepts/hermes-wiki-page-writing-standards.md#L91-L97) (*"`depends_on`：依赖某个前置规范或概念"*), `depends_on` is intended for conceptual/normative dependencies between formal wiki pages. Raw source evidence is already declared in YAML `sources: [raw/articles/donald-robertson-mentally-rehearse-coping-2026-08-18.md]` and cross-referenced in `## Related`.

---

## Passes

- **Smallest durable unit & appropriate landing**:
  [`concepts/coping-skill-application-and-imaginal-exposure.md`](file:///home/lin/wiki/concepts/coping-skill-application-and-imaginal-exposure.md) captures a distinct, durable capability gap: distinguishing coping skill acquisition from real-world application, identifying "pseudo-coping" avoidance loops, and applying bounded imaginal exposure. It appropriately refines [`concepts/personal-growth-operating-model.md`](file:///home/lin/wiki/concepts/personal-growth-operating-model.md) without polluting that domain root page with specific clinical/psychological protocols, and avoids conflation with AI cognitive offloading in [`concepts/ai-assistance-cognitive-substitution-and-skill-formation.md`](file:///home/lin/wiki/concepts/ai-assistance-cognitive-substitution-and-skill-formation.md).
- **Structured raw capture fidelity & publication cutoff**:
  [`raw/articles/donald-robertson-mentally-rehearse-coping-2026-08-18.md`](file:///home/lin/wiki/raw/articles/donald-robertson-mentally-rehearse-coping-2026-08-18.md) cleanly separates article metadata, Substack DOM extraction route, local summary provenance, practitioner-synthesis limitations, and an explicit public/paid boundary (preserving the complete public portion and noting the subscriber-only continuation is excluded). The 25-step imaginal exposure sequence is captured with clear internal consistency and progressive pacing.
- **Evidence boundaries & draft lifecycle status**:
  The concept page explicitly identifies the source as a practitioner synthesis lacking primary-study citations or clinical trial validation. It categorizes what can be durably retained (acquisition vs. application, avoidance detection, progressive exposure testing) versus what remains unverified (specific clinical efficacy, dosage, indication/contraindication profiles, and the "natural emotional fading" mechanism), correctly setting `status: draft` until peer-reviewed CBT/exposure literature is incorporated.
- **Mental-health safety boundaries**:
  The safety section in both the raw capture and concept page is explicit, prominent, and fail-closed: it proscribes severe trauma/panic/dissociation/self-harm confrontation without professional care, defines immediate cessation criteria, and includes an unambiguous medical disclaimer.
- **Carefully bounded cross-concept links**:
  Links to [`concepts/personal-growth-operating-model.md`](file:///home/lin/wiki/concepts/personal-growth-operating-model.md) ("output over collection"), [`queries/how-i-should-decide-between-doing-nothing-and-taking-action.md`](file:///home/lin/wiki/queries/how-i-should-decide-between-doing-nothing-and-taking-action.md) (noting that exposure practice cannot be mechanically equated to investment rules), and [`concepts/ai-assistance-cognitive-substitution-and-skill-formation.md`](file:///home/lin/wiki/concepts/ai-assistance-cognitive-substitution-and-skill-formation.md) (evaluating performance when support is removed) are precisely bounded.
- **Frontmatter, hash registration & health check**:
  - Tags (`growth`, `learning`, `health`) are registered in [`SCHEMA.md:L182-L189`](file:///home/lin/wiki/SCHEMA.md#L182-L189).
  - SHA-256 for `raw/articles/donald-robertson-mentally-rehearse-coping-2026-08-18.md` (`674d0e6942b729f26a08f3d6c278fb5d8a907850f8707167aa16f683b2d3ea16`) matches `_meta/raw-source-hashes.json` line 11 exactly.
  - [`index.md`](file:///home/lin/wiki/index.md#L5) count was incremented to 112, exactly matching indexed pages.
  - `_meta/scripts/wiki_health_check.py` passes cleanly (`pass: true`, `P0=0`, `P1=0`, `P2=0`).

---

## Recommended patches

### Patch 1: Adjust entry placement in [`log.md`](file:///home/lin/wiki/log.md)

Move the new `[2026-08-20]` block from the bottom of [`log.md`](file:///home/lin/wiki/log.md) to line 6 (immediately below `# Wiki Log` header):

```diff
--- a/log.md
+++ b/log.md
@@ -4,6 +4,15 @@
 > Format: `## [YYYY-MM-DD] action | subject`
 
+## [2026-08-20] ingest | Donald Robertson on coping rehearsal and imaginal exposure
+- Captured structured raw source: `raw/articles/donald-robertson-mentally-rehearse-coping-2026-08-18.md`.
+- Created draft concept: `concepts/coping-skill-application-and-imaginal-exposure.md`.
+- Updated: `index.md`.
+- Durable unit: separate coping-skill acquisition from real-world application; detect self-regulation practices that substitute for action; test transfer only through mild, bounded, progressively realistic contact with discomfort.
+- Evidence boundary: the source is a practitioner synthesis, not a peer-reviewed study or clinical guideline; no efficacy, dosage, indication, contraindication, or unified mechanism was promoted as established fact.
+- Validation: raw/header readback, wiki health check, raw-source hash manifest, and `git diff --check` required before closeout.
+- Boundary: wiki-only ingestion; no memory, active skill/reference, project, config, cron, MCP, runtime, wrapper, gateway, profile/plugin, or Hermes core change was made.
+
 ## [2026-08-19] review | AGY review of staged structured-output sedimentation
 - Review prompt: `_meta/reviews/2026-08-19-staged-structured-output-agy-review-prompt.md`; result: `_meta/reviews/2026-08-19-staged-structured-output-agy-review.md`; AGY `1.1.15`, exit code `0`, empty stderr.
 - AGY verdict: `APPROVE`; Blocking, Important, Minor and Recommended patches were all `None`. It accepted source fidelity, existing-concept placement, proactive optional-skill adoption, separate evaluation dimensions and the no-runtime-leakage boundary.
@@ -1522,10 +1531,0 @@
-
-## [2026-08-20] ingest | Donald Robertson on coping rehearsal and imaginal exposure
-- Captured structured raw source: `raw/articles/donald-robertson-mentally-rehearse-coping-2026-08-18.md`.
-- Created draft concept: `concepts/coping-skill-application-and-imaginal-exposure.md`.
-- Updated: `index.md`.
-- Durable unit: separate coping-skill acquisition from real-world application; detect self-regulation practices that substitute for action; test transfer only through mild, bounded, progressively realistic contact with discomfort.
-- Evidence boundary: the source is a practitioner synthesis, not a peer-reviewed study or clinical guideline; no efficacy, dosage, indication, contraindication, or unified mechanism was promoted as established fact.
-- Validation: raw/header readback, wiki health check, raw-source hash manifest, and `git diff --check` required before closeout.
-- Boundary: wiki-only ingestion; no memory, active skill/reference, project, config, cron, MCP, runtime, wrapper, gateway, profile/plugin, or Hermes core change was made.
```

### Patch 2: Refine `## Relations` in [`concepts/coping-skill-application-and-imaginal-exposure.md`](file:///home/lin/wiki/concepts/coping-skill-application-and-imaginal-exposure.md)

Remove the raw source file from `## Relations` (evidence provenance remains properly captured in YAML `sources` and `## Related`):

```diff
--- a/concepts/coping-skill-application-and-imaginal-exposure.md
+++ b/concepts/coping-skill-application-and-imaginal-exposure.md
@@ -96,7 +96,6 @@
 ## Relations
 
 - refines: [[personal-growth-operating-model]]
-- depends_on: [[donald-robertson-mentally-rehearse-coping-2026-08-18]]
 
 ## Related
```

---

## Safety boundary assessment
No leakage was detected. The commit is strictly confined to the Wiki layer (`raw/articles/`, `concepts/`, `index.md`, `log.md`, `_meta/raw-source-hashes.json`). No changes or side effects were introduced into Hermes memory, active skills/references, project code, cron jobs, MCP configs, model runtime, wrappers, gateways, profile/plugins, or Hermes core.

## Parent disposition

Hermes independently confirmed both Minor findings against the live files and accepted both minimal fixes:

1. moved the ingestion block to reverse-chronological position at the top of `log.md`;
2. removed the raw-source `depends_on` relation while retaining frontmatter `sources` and the `## Related` link.

All five reviewed target hashes matched the pre-review snapshot before fixes (`NO_DRIFT`). Post-fix validation passed: Wiki health `P0=0 / P1=0 / P2=0` and `git diff --check` clean. No active-layer change was made.
