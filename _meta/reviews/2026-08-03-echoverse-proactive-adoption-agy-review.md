# Independent Review: Echoverse proactive adoption — 2026-08-03

**Reviewer:** Antigravity (independent, read-only session)
**Prompt:** `/home/lin/wiki/_meta/reviews/2026-08-03-echoverse-proactive-adoption-agy-review-prompt.md`
**Scope:** Wiki + active-skill/reference changes; governance references; backup diff

---

## Verdict

**PASS_WITH_MINOR_FIXES**

Two minor fixes are recommended (both P3, no blocking issues). No changes to wiki raw capture, concept architecture, optional reference trigger/skip, or governance logic require reversal. The change set is proportionate and within the declared intended decision.

---

## Findings (ordered by severity)

### P3-1 — `SKILL.md` pointer wording could falsely imply `effect:"confirmed"` is business-state proof

**File/section:** [`computer-use/SKILL.md`](file:///home/lin/.hermes/skills/autonomous-ai-agents/computer-use/SKILL.md) line 75, within **Step 3 — Verify**

**Evidence:**

Step 3 reads:
```
**Step 3 — Verify.** After any state-changing action, re-capture. You
can save a round-trip by asking for the post-action capture inline:
```
Followed immediately by the optional reference pointer:
```
For durable business outcomes, see the optional [authoritative outcome verification reference](references/authoritative-outcome-verification.md).
```

Later, the verify → escalate ladder (lines 117–127) defines:
```
- `effect`: `"confirmed"` (driver read the result back — done)
```
and the step-by-step escalation (line 129) says:
```
1. **Element, background (default).** `click(element=N)`. If `effect:"confirmed"`, you're done.
```

This creates a mild internal tension: a reader can follow the escalation ladder to the conclusion "if `effect:\"confirmed\"`, you're done," then never notice the optional reference pointer that says `confirmed` only proves an interaction-layer effect for durable business states. The pointer placement in Step 3 is correct but its proximity to the `capture_after` example — rather than to the escalation ladder — slightly reduces its discoverability for agents reading the ladder.

**Risk:** Low. The optional reference is explicit on this point ("Screenshot changes, accessibility/driver `confirmed`, a success toast, or a control disappearing only establish an interaction-layer effect."). The pointer is present. This is a discoverability issue, not a contradiction.

**Minimal remediation:** Add one parenthetical sentence at the end of the `effect:"confirmed"` escalation entry (line 129–130) to make the boundary visible without duplicating the reference:

```diff
 1. **Element, background (default).** `click(element=N)`. If `effect:"confirmed"`,
-   you're done.
+   you're done. (For durable business-state outcomes, this is interaction-layer confirmation
+   only — see the optional [authoritative outcome verification reference](references/authoritative-outcome-verification.md).)
```

Alternatively, the existing pointer at line 75 can be left as-is and this finding accepted as a known minor discoverability gap rather than a contradiction. Either resolution is acceptable.

---

### P3-2 — `article-derived-workflow-adoption-governance.md` table row still implies `OPTIONAL_REFERENCE` requires `DEFAULT_GUIDANCE`/`HARD_GATE` evidence

**File/section:** [`article-derived-workflow-adoption-governance.md`](file:///home/lin/.hermes/skills/hermes/hermes-knowledge-and-workflow-governance/references/article-derived-workflow-adoption-governance.md) lines 22–26 (the three-track table), and the Pre-patch gates section (lines 85–93, gate #1)

**Evidence:**

The table row for "Active skill/reference/default gate" now correctly reads:
```
`OPTIONAL_REFERENCE` when the proactive evidence conditions below all hold; `DEFAULT_GUIDANCE`/`HARD_GATE` only with reactive evidence or explicit skip-level approval
```
This is correct after the governance correction.

However, the **Pre-patch gates section** (gate #1) was updated from the backup version:

*Before (backup):*
```
1. **Observed failure:** What recurring Hermes failure does this prevent? If none, stop at `DRAFT_ONLY`.
```
*After (current):*
```
1. **Evidence track:** Is this using reactive local evidence, or the proactive `OPTIONAL_REFERENCE` path? If proactive, are all conditions in the dual-track section documented? Lack of local failure blocks `DEFAULT_GUIDANCE`/`HARD_GATE` and runtime promotion, but does not by itself block a qualifying optional reference.
```

This is internally consistent and correct. No contradiction found here on second reading.

The **Existing-project reuse exception** (line 49) contains one residual phrase that was not updated from the backup version:

*Backup (line 49):*
```
Promoting to an active reference/skill **patch** still requires reaching `DEFAULT_GUIDANCE`/`HARD_GATE` and passing every question in `Pre-patch gates` below; this exception does not shortcut that.
```
*Current (line 49):*
```
Promoting beyond a bounded `OPTIONAL_REFERENCE` into `DEFAULT_GUIDANCE`/`HARD_GATE` still requires the stronger evidence and every question in `Pre-patch gates` below; this exception does not shortcut that.
```

This was correctly updated. No issue here.

**Re-assessment:** On careful re-reading, P3-2 resolves as **no actionable fix required**. The governance correction is internally consistent across the table, the dual-track evidence section, the pre-patch gates, and the existing-project reuse exception. Retaining as informational only.

---

### Informational — `knowledge-promotion-gates.md` graduation check wording silently tightened

**File/section:** [`knowledge-promotion-gates.md`](file:///home/lin/.hermes/skills/hermes/hermes-knowledge-and-workflow-governance/references/knowledge-promotion-gates.md) line 72

**Before (backup):**
```
- Wiki concept → skill/reference: the idea changes a repeatable method, gate, pitfall, boundary, or verification step;
  preferably it has appeared in more than one decision, review, or failure pattern, or it resolves a concrete ambiguity
  in an existing umbrella skill.
```
**After (current):**
```
- Wiki concept → skill/reference: the idea changes a repeatable method, gate, pitfall, boundary, or verification step.
  `OPTIONAL_REFERENCE` may use the documented proactive evidence path when it is narrow, low-ceremony, reversible and
  verifiable; `DEFAULT_GUIDANCE`/`HARD_GATE` still requires reactive/local evidence or explicit skip-level approval.
```

The new wording removed the "preferably it has appeared in more than one decision" soft gate for wiki→skill, replacing it with the explicit dual-track distinction. This is a correct and necessary correction: the old wording was the source of the over-conservatism the intended decision targets. The new wording is consistent with `article-derived-workflow-adoption-governance.md`. No fix needed; recording for transparency.

---

## Q&A on review questions

### Q1 — Raw-source facts: faithful to source? Unsupported claims?

**PASS.** All quantitative figures in the raw article capture are verifiable against the gsummary:

| Claim | Raw article | gsummary |
|---|---|---|
| 12 worlds (10 domain + 2 capability) | ✓ | ✓ |
| Allrecipes 80→75% shallow / 85% deep | ✓ | ✓ |
| HuggingFace 48% shallow / 65% deep | ✓ | ✓ |
| EchoStay booking 48→78% after fix | ✓ | ✓ |
| EchoStay score 16.2→38.5%; GPT-5.4 at 50.4% | ✓ | ✓ |
| Qwen3.5-9B 36.5→67.1%; GPT-5.4 at 80.7% | ✓ | ✓ |
| Date-picker 34→54%; nested-filter 84.1% | ✓ | ✓ |
| Online-Mind2Web 29.5→34.3% | ✓ | ✓ |
| RL: 58→69% on 25 held-out tasks | ✓ | ✓ |
| WebVoyager 66.5→71.5%; GitHub 58.5→63.4% | ✓ | ✓ |
| Trajectory scale 6,400→20,000: Mind2Web 40.1→37.2% | ✓ | ✓ |
| EchoForum ~2.55M forum comments | ✓ | ✓ (255万) |

Source quality note: direct HTTP fetch returned 403; browser DOM extraction recovered full rendered article. This is documented in both the raw capture frontmatter and the extraction note, which is appropriate.

Inference separation: Hermes-inferred mappings are labelled `[推论]` in both the concept and the raw article. The reading boundary section explicitly states the evidence supports a testable distinction, not a prescription. **No unsupported numbers or unmarked inferences found.**

---

### Q2 — New concept: distinct from existing wiki pages?

**PASS.** `stateful-agent-environments-and-grounded-verification` is a new concept with a materially distinct scope:

- `production-ai-agent-evaluation-framework` covers retrieval/generation/agent-behavior/production layers and references the new concept explicitly in the new "Relationship to stateful environments" section — this cross-link is correct and sufficient.
- The new concept does not duplicate the failure-attribution table or the evaluation dimensions in any existing page.
- Index entry at line 33 is accurate: "有状态 Agent 评测单元：把环境、任务与验证器结合…"
- Frontmatter: `type: concept`, `status: stable`, `sources` link to raw article, `aliases`, `tags` all correct per wiki writing standards.
- Wikilinks in the Related section are all to existing wiki pages; no phantom links detected.

---

### Q3 — Optional reference: hidden hard gate risk?

**PASS.** The `authoritative-outcome-verification.md` reference passes all ceremony checks:

| Check | Status |
|---|---|
| Trigger explicit | ✓ "when the action depends on a persistent business result and a more authoritative read-back exists" |
| Skip explicit | ✓ "Skip for read-only browsing, navigation, transient UI interactions, tasks with no authoritative state contract, or cases where read-back would add material danger or a new side effect" |
| Cheapest validation | ✓ "reuse one existing low-risk, reversible task and perform one `action → readback` check" |
| Boundary explicit | ✓ "does not grant credentials, production access, destructive authority, runtime behavior, cron jobs, MCP/gateway changes" |
| Rollback explicit | ✓ "Remove this reference and its single pointer from `SKILL.md`; no data migration, runtime restoration, or dependency rollback is required." |
| Hard-gate risk | None. The reference says "Adoption class: proactive `OPTIONAL_REFERENCE`; this is bounded guidance, not a default workflow gate." |

The reference is narrow, reversible, and not self-expanding.

---

### Q4 — SKILL.md pointer: conflict with `effect:"confirmed"` wording?

**MINOR ISSUE (P3-1 above).** There is a mild discoverability gap — the pointer is placed in Step 3 but the semantically closest text (`effect:"confirmed"` in the escalation ladder) does not repeat the business-state boundary. There is no internal contradiction: both the escalation ladder and the optional reference are correct in isolation. The optional reference explicitly addresses this. The remediation in P3-1 would close the gap.

---

### Q5 — Two governance references: internally consistent?

**PASS.** After diffing backup vs. current:

| Consistency check | Result |
|---|---|
| Three-track table (`article-derived` ref) matches dual-track text | ✓ |
| Pre-patch gate #1 updated to allow proactive optional reference | ✓ |
| `knowledge-promotion-gates` graduation check updated to match | ✓ |
| `knowledge-promotion-gates` external failure fast path correctly distinguishes wiki vs. skill levels | ✓ |
| One-change budget unchanged (still 0/1/2/>2) | ✓ |
| Independent safety approvals not relaxed | ✓ — "does not by itself block a qualifying optional reference" explicitly preserves credentials/production/destructive as independent blockers |
| Maturity ladder unchanged | ✓ — `OPTIONAL_REFERENCE` row present and unchanged |

One slight wording inconsistency to note (not a correctness issue): `knowledge-promotion-gates.md` (backup) said "skill/reference patch" requires having "appeared in more than one decision, review, or failure pattern"; the current version removed that soft gate for `OPTIONAL_REFERENCE`. This is the governance correction under review and is intentional. The two references now share a single canonical statement of the dual-track distinction, which is correct.

---

### Q6 — Scope: smallest proactive landing?

**PASS.** The change set consists of:
- 1 raw source capture (read-only knowledge)
- 1 new wiki concept (durable, source-backed)
- 1 update to `production-ai-agent-evaluation-framework` (one cross-link paragraph + Related entry)
- 1 index entry
- 1 log entry
- 1 optional reference file (30 lines, explicit trigger/skip/boundary/rollback)
- 1 single-line pointer in `SKILL.md`
- 2 governance reference patches (correcting over-conservatism, not expanding scope)

No fixtures, projects, monitors, multi-agent chains, cron/MCP/gateway changes, credentials, memory writes, RL/database-grader requirements, or synthetic world requirements were introduced. **The change is proportionate and within the one-change budget.**

---

### Q7 — Pre-existing validator failures?

**PASS / NOT APPLICABLE.** The review prompt asks whether any validator failures are pre-existing rather than introduced by this change. No validators were run or modified by this change. The optional reference's minimum validation path ("reuse one existing low-risk reversible task") is a future adoption-time check, not a change introduced now. No regression introduced.

---

## Accepted Architecture Summary

The architecture after this change consists of:

1. **Raw source** (`raw/articles/microsoft-research-echoverse-computer-use-agent-environments-2026-07-30.md`): structured capture of the Microsoft Research Echoverse article. HTTP 403 was handled via browser DOM extraction, documented in frontmatter. Numbers are faithful to source; inferences are labelled `[推论]` in the reading boundary section.

2. **Wiki concept** (`concepts/stateful-agent-environments-and-grounded-verification.md`): introduces the durable unit `environment + tasks + verifier` as an evaluation design frame for stateful computer-use agents. Covers five evaluation dimensions (behavioral fidelity, state coherence, workflow depth, authoritative outcome verification, domain value), a failure-attribution table (model / environment / task / verifier), capability worlds, co-evolution, and Hermes mappings (all labelled `[推论]`). Correctly linked from `production-ai-agent-evaluation-framework` and listed in `index.md`.

3. **Optional reference** (`computer-use/references/authoritative-outcome-verification.md`): narrow 30-line guidance that for durable-business-outcome actions, the agent should read back the most authoritative available state before claiming completion. Has explicit trigger, skip, cheapest validation, boundary, and rollback. Adoption class is explicitly `OPTIONAL_REFERENCE`, not a default gate.

4. **SKILL.md pointer** (line 75): a single sentence linking to the optional reference from Step 3 of the canonical workflow. Not in the escalation ladder (minor discoverability gap, P3-1).

5. **Governance corrections** (both references): The article-derived adoption governance now has a dual-track structure. A qualifying narrow, low-ceremony, reversible, verifiable `OPTIONAL_REFERENCE` does not require prior Hermes-local failure. `DEFAULT_GUIDANCE`, `HARD_GATE`, and runtime promotion remain gated on reactive/local evidence or explicit skip-level approval. Independent safety boundaries (credentials, production, destructive) are not relaxed. Both references are internally consistent.

---

## Confirmation

I made **no edits** to any file during this review. All operations were strictly read-only.
