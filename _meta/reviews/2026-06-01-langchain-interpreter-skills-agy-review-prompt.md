# AGY read-only wiki review prompt

Reviewer: AGY

Scope: read-only review of the Hermes wiki sedimentation for LangChain's “Interpreter Skills: Building Workflows for Agents”. Do not modify files, run commits, edit skills, update memory, touch cron/MCP/runtime/wrapper/gateway/Hermes core, or promote anything to the active layer.

Files under review:
- `raw/articles/langchain-interpreter-skills-2026-05-30.md`
- `concepts/hermes-ai-workflow-formalization-principles.md`
- `log.md`

Context:
- The intended decision was to preserve the raw source, reuse the existing concept page instead of creating a duplicate concept, and add only the smallest durable wiki-layer unit.
- The intended durable unit is: model routes and selects parameters; deterministic code executes reviewed workflow logic and returns verifiable structure.
- Candidate status should remain concept-only. Any future skill/reference promotion requires repeated local Hermes evidence, schema/fixture/validator coverage, rollback path, and explicit approval.
- Active-layer boundary must stay explicit: no memory, active skill/reference, cron, MCP, runtime, wrapper, gateway, or Hermes core change.

Review questions:
1. Source fidelity: does the raw page preserve enough provenance and article content without confusing extracted prose with interpretation?
2. Smallest durable unit: does the concept update add a distinct principle, or does it duplicate existing skill/governance concepts?
3. Layer routing: are candidate status, graduation/promotion conditions, and active-layer boundaries clear enough?
4. Wiki quality: are links, frontmatter sources, headings, and log entry useful and consistent with nearby wiki patterns?
5. Risk: does anything accidentally imply that LangChain's TypeScript interpreter or `SKILL.md + module` design should become a Hermes runtime/skill implementation now?

Output shape:

Verdict: PASS | PASS_WITH_MINOR_FIXES | NEEDS_CHANGES

Blocking:
- ...

Important:
- ...

Minor:
- ...

Passes:
- ...

Recommended patches:
- For each accepted-worthy finding, name the file, section, and exact intent of the patch. Do not perform the patch.
