# Codex focused closure review prompt

Read-only review in `/home/lin/wiki`. Do not edit files, use network, or inspect unrelated pages.

Inspect only:
- `concepts/ai-assistance-cognitive-substitution-and-skill-formation.md`
- `raw/articles/psychologytoday-ai-cognitive-substitution-skill-formation-2026-08-03.md`
- `_meta/reviews/2026-08-04-psychologytoday-ai-cognitive-substitution-codex-review.md`
- top 25 lines of `log.md`
- current `git diff --check` and Wiki health output if needed

Verify that all seven bounded fixes from the prior review are present and do not create new factual, schema, ownership, or active-layer problems:
1. cross-domain applications labeled local inference;
2. long-term skill-degradation wording weakened;
3. radiology claim scoped to article-reported 82%→45.5%, with no generalization;
4. Hebbian/use-it-or-lose-it neuroscience analogy bounded;
5. local summary path marked local-only and not durable provenance;
6. `refines` changed to `related` for the assumption-challenger page;
7. no-promotion layer list aligned with log.

Output exactly:
- `Verdict: APPROVE_LANDING | REQUEST_BOUNDED_FIXES`
- `Closure:` F1-F7 each `CLOSED` or `OPEN` with one sentence
- `New findings:` None or bounded list
- `Layer boundary:` PASS or FAIL
- `Recommendation:` one paragraph
