---
title: Subagent review — AI and the Two Forms of Authorship wiki ingestion
created: 2026-08-04
type: review
status: completed
sources: [raw/articles/psychologytoday-ai-two-forms-authorship-2026-07-30.md, concepts/ai-assistance-cognitive-substitution-and-skill-formation.md]
---

# Subagent review — AI and the Two Forms of Authorship wiki ingestion

## Reviewer verdict

`PASS_WITH_MINOR_FIXES`

## Reviewer report

### Scope reviewed

- `raw/articles/psychologytoday-ai-two-forms-authorship-2026-07-30.md`
- `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md`
- `log.md` — newest ingestion entry
- `concepts/ai-assumption-challenger-before-execution.md` — ownership comparison

The reviewer used `git status` and `git diff` and confirmed that no non-Wiki active surfaces were changed.

### Finding 1 — provenance cleanliness

- Severity: minor.
- Reviewer claim: the raw body still retained `Facebook / Bluesky / Linkedin` and email-interface text while the metadata said share controls had been removed.
- Proposed fix: weaken the extraction-cleanliness wording.
- Reviewer disposition: required before landing.

### Finding 2 — duplication and concept ownership

- No blocking issue.
- Updating `ai-assistance-cognitive-substitution-and-skill-formation` rather than creating a new concept page is the smallest durable unit.
- The linguistic-versus-cognitive-authorship section extends the existing Contribution test without splitting ownership.

### Finding 3 — boundary with adjacent owner page

- No issue.
- Writing-role design remains owned by `ai-assumption-challenger-before-execution`; the updated concept does not promote the framework into a universal Hermes gate.

### Finding 4 — fact versus inference separation

- No required issue.
- The reviewer suggested an optional explicit `[推论]` prefix on the locally synthesized writing/research questions.

### Finding 5 — schema, wikilinks and log consistency

- No issue.
- Frontmatter, `sources`, related-source links, dates and log shape were consistent with the Wiki schema.

### Finding 6 — active-layer safety

- No issue.
- The change remained inside Wiki raw/concept/log/review files and did not touch memory, skills, prompts, runtime, gateway, cron, MCP or configuration.

## Parent adjudication

### Rejected factual finding: retained share/interface noise

The reviewer's only required fix was based on stale or mismatched line evidence:

- the reviewed raw file has 73 lines, so the cited lines `113–121` do not exist;
- deterministic comparison against the saved Gemini input showed that the raw body matches the extracted article exactly after removing only the trailing `Facebook`, `Bluesky` and `Linkedin` labels;
- the raw file contains none of those labels and no email-interface text;
- therefore the existing statements that share controls were removed are accurate and are not weakened.

Verification evidence:

```text
source_chars: 2755
raw_body_chars: 2726
share_labels_removed: Facebook, Bluesky, Linkedin
exact_after_bounded_cleanup: true
```

### Accepted optional improvement: explicit inference label

The locally synthesized writing/research questions are marked `[推论]` so they cannot be mistaken for an operational checklist supplied by the article.

## Final disposition

`APPROVE_AFTER_ADJUDICATION`

- Required reviewer finding: rejected with deterministic counterevidence.
- Optional inference-label improvement: accepted.
- No new concept page, index entry or active-layer change is warranted.
