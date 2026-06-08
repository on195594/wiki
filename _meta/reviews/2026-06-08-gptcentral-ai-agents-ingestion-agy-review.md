I will start by listing the contents of the `/home/lin/wiki` directory to locate the files under review and understand the repository structure.
I will now view the raw source article file under review to examine its content and provenance metadata.
I will read `concepts/subagent-orchestration-patterns.md` to see the changes made under commit `ae6ad15` (e.g., the added single-agent first escalation rule and how it integrates with the rest of the concept).
I will search for `gptcentral` inside `log.md` using the grep search tool to see the specific log entry for this ingestion.
I will view the relevant lines around the log entry for the GPT Central article in `log.md` to analyze its structure, compliance with logging rules, and details.
I will list the contents of the `concepts` directory to verify the names of adjacent concept files and identify potential missing links or relationships.
I will read `SCHEMA.md` to review the repository standards for metadata frontmatter, page structures, and other wiki hygiene guidelines.
I will check if `index.md` has been updated to link to the new raw source or concept update by searching for `gptcentral` inside `index.md`.
I will search for references to `subagent-orchestration-patterns` in `index.md` to see how it's linked.
I will search for the word `raw/` in `index.md` to see if raw sources are usually listed and linked there.
I will view the beginning of `index.md` to see its section organization and check if there is a place where new raw sources or new files should be registered.
I will list the files in `/home/lin/wiki/raw/articles` to locate other raw articles and compare their frontmatter format.
I will view the frontmatter of `raw/articles/langchain-interpreter-skills-2026-05-30.md` to see what fields are expected in raw articles.
I will view the frontmatter of `towardsdatascience-most-ai-agents-built-backwards-2026-05-27.md` to see what "the peer TDS schema" looks like.
I will view the beginning of `concepts/agent-context-engineering.md` to see if there is any overlapping context or if it should be linked to/from the subagent orchestration patterns page.
I will check `concepts/agent-closed-loop-learning-from-corrections-to-rules.md` to see its relevance and whether there are links or overlaps between it and the updated subagent patterns concept.
I will run a read-only git command to list the files modified in commit `ae6ad15` to ensure we haven't missed any other affected files.
- Verdict: PASS_WITH_MINOR_FIXES

- Blocking:
None.

- Important:
1. **Wiki Hygiene / Index Synchronization**: The `index.md` file was not updated. Line 5 of [index.md](file:///home/lin/wiki/index.md) still reads `Last updated: 2026-05-28 | Total pages: 84`. Since [concepts/subagent-orchestration-patterns.md](file:///home/lin/wiki/concepts/subagent-orchestration-patterns.md) was updated on `2026-06-08`, this violates the [SCHEMA.md](file:///home/lin/wiki/SCHEMA.md) operating rule: *"新建或更新页面后，必须同步更新 index.md"* (Every new or updated page must synchronize `index.md`).
2. **Raw-Source Frontmatter Inconsistencies**: The frontmatter for [raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md](file:///home/lin/wiki/raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md) deviates from the standard schema defined in [SCHEMA.md](file:///home/lin/wiki/SCHEMA.md) and peer pages:
   - Missing required `status: captured` field.
   - Non-standard metadata keys: it uses `source_site` and writes the URL to `source` with a `docs:` prefix. It should use `source` for the site/author name and `source_url` for the raw URL.
   - Non-schema metadata key `summary_path` is used to store an absolute local-only transient path, which risks cluttering the frontmatter schema. Local-only grounding files should instead be documented inside the `extraction:` field text.

- Minor:
1. **Grounding Path Relocation**: Relocate the transient absolute path `/home/lin/.hermes/...` from the custom `summary_path` key to a descriptive note inside the standard `extraction` string to prevent custom schema pollution.
2. **Contextual Cross-links**: Although [concepts/subagent-orchestration-patterns.md](file:///home/lin/wiki/concepts/subagent-orchestration-patterns.md) links to related concepts at the bottom, adding inline mentions of [concepts/agent-context-engineering.md](file:///home/lin/wiki/concepts/agent-context-engineering.md) (re: tool boundaries and system instructions) and [concepts/agent-closed-loop-learning-from-corrections-to-rules.md](file:///home/lin/wiki/concepts/agent-closed-loop-learning-from-corrections-to-rules.md) (re: rule escalation) under the new `Single-agent first escalation rule` section would improve internal wiki cohesion.

- Passes:
1. **Durable Ingestion Unit**: The ingestion choice is correct. Reusing the existing [concepts/subagent-orchestration-patterns.md](file:///home/lin/wiki/concepts/subagent-orchestration-patterns.md) instead of creating a generic "AI Agent Intro" concept page complies with the page threshold and deduplication guidelines in [SCHEMA.md](file:///home/lin/wiki/SCHEMA.md).
2. **Escalation Pattern Placement**: The new `Single-agent first escalation rule` section is logically positioned right before the orchestration modes. It maps a clear hierarchy (deterministic rules → single agent → subagents → pools/teams) compatible with the parent page.
3. **Fidelity and Provenance**: The raw source page preserves high fidelity. The extraction quality details, URL, and reader limitations are kept distinct from the raw markdown content.
4. **Link Reciprocity**: The links are correctly set up. [concepts/subagent-orchestration-patterns.md](file:///home/lin/wiki/concepts/subagent-orchestration-patterns.md) links to the raw source, and [raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md](file:///home/lin/wiki/raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md) reciprocates under the `Extraction note` on line 17.
5. **Layer Boundary Integrity**: The ingestion respects the hard boundaries. The change is restricted to the wiki documentation layer, explicitly stating that a general tutorial does not justify active-layer promotions (e.g., active skills, cron, MCP).
6. **Log Compliance**: The ingestion was correctly logged in [log.md](file:///home/lin/wiki/log.md#L900-L905) under lines 900–905.

- Recommended patches:

#### Patch 1: Synchronize `index.md` Update Date
Apply the following diff to [index.md](file:///home/lin/wiki/index.md):
```diff
--- index.md
+++ index.md
@@ -2,5 +2,5 @@
 
 > Hermes 长期知识目录。
 > 这里记录正式沉淀页面，不记录原始聊天。
- > Last updated: 2026-05-28 | Total pages: 84
+ > Last updated: 2026-06-08 | Total pages: 84
```

#### Patch 2: Normalize Raw-Source Frontmatter
Apply the following diff to [raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md](file:///home/lin/wiki/raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md) to align metadata and remove non-schema fields:
```diff
--- raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md
+++ raw/articles/gptcentral-ultimate-guide-building-ai-agents-2026-06-05.md
@@ -2,9 +2,10 @@
 title: The Ultimate Guide to Building AI Agents
 created: 2026-06-08
 type: raw-source
-source: docs:https://gptcentral.substack.com/p/the-ultimate-guide-to-building-ai
-source_site: GPT Central / ChatGPT Central
+source: GPT Central / ChatGPT Central
+source_url: https://gptcentral.substack.com/p/the-ultimate-guide-to-building-ai
 published: 2026-06-05
 captured: 2026-06-08
-extraction: Jina Reader direct fetch from Substack canonical page
-summary_path: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260608-084702-The-Ultimate-Guide-to-Building-AI-Agents-3749496-396700720-summary.md
+status: captured
 tags: [agent, workflow, orchestration, subagent, raw-source]
+extraction: Jina Reader direct fetch from Substack canonical page. Gemini summary run saved locally at /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260608-084702-The-Ultimate-Guide-to-Building-AI-Agents-3749496-396700720-summary.md (local-only grounding path).
---
```
