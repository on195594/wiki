# Wiki tag taxonomy governance plan

Date: 2026-05-13
Status: draft / plan only
Scope: `/home/lin/wiki`

## 1. Goal

Make wiki tags useful for retrieval and automation without rewriting the knowledge base.

This plan governs the existing tag drift between:

- Declared taxonomy: `SCHEMA.md` → `## Tag Taxonomy`
- Actual page frontmatter: `tags: [...]` across `~/wiki/**/*.md`

The goal is not to reduce every page to a tiny fixed vocabulary. The goal is to create a stable, documented, low-noise tag system that supports:

- reliable search and topic grouping;
- future generated indexes;
- avoiding duplicate pages;
- keeping `SCHEMA.md` aligned with real wiki usage.

## 2. Current baseline

A read-only scan on 2026-05-13 found:

- declared taxonomy tags: 18
- tagged pages scanned: 90
- actual unique tags: 110
- tags not declared in `SCHEMA.md`: 96
- invalid tag instances: 246
- declared-but-unused tags: `devops`, `linux`, `networking`, `product`

Top undeclared tags by frequency:

- `investment`: 16
- `governance`: 12
- `trading`: 12
- `validation`: 10
- `lifeos`: 9
- `kickoff`: 8
- `project`: 8
- `ai-coding`: 6
- `claude-code`: 6
- `multi-agent`: 6
- `operating-model`: 6
- `monitoring`: 5

Interpretation:

- This is not a data corruption issue.
- It is a taxonomy drift issue: the wiki evolved faster than `SCHEMA.md`.
- Existing pages are usable, but tag-based retrieval and automation will be noisy unless we normalize the vocabulary.

## 3. Non-goals

Do not do these in the first pass:

- Do not rename pages.
- Do not rewrite article/raw content.
- Do not alter page conclusions.
- Do not force every rare tag into a global taxonomy.
- Do not remove tags purely because they are not in the current schema.
- Do not attempt to fix long pages, draft queries, or unrelated wiki health P2 items in the same commit.
- Do not update Hermes memory or skills for this taxonomy cleanup unless the workflow itself proves reusable after execution.
- Do not prioritize raw article tag replacement in the first pass: raw tags are included in audit counts, but formal wiki pages are the first-pass normalization target.

## 4. Proposed taxonomy model

Use three tag classes, documented in `SCHEMA.md`:

1. **Core tags**
   - Small stable set used across many pages.
   - Examples: `hermes`, `agent`, `workflow`, `automation`, `knowledge-base`, `mcp`, `llm`, `configuration`, `debugging`, `research`, `decision`, `comparison`, `note`.

2. **Domain tags**
   - Stable subject areas that recur enough to support discovery.
   - Criterion: a domain tag names the main subject area of a page.
   - Candidate additions based on current usage:
     - `investment`
     - `trading`
     - `governance`
     - `validation`
     - `monitoring`
     - `project`
     - `memory`
     - `skills`
     - `cron`
     - `browser`
     - `context-engineering`

3. **Facet tags**
   - Narrow but reusable lenses for AI workflow pages.
   - Criterion: a facet tag describes a cross-cutting angle, method, tool mode, or evaluation lens that can apply across multiple subject areas.
   - Candidate additions:
     - `ai-coding`
     - `claude-code`
     - `multi-agent`
     - `subagent`
     - `orchestration`
     - `evaluation`
     - `verification`
     - `operating-model`

Rule of thumb:

- If a tag appears on 3+ pages, consider adding it to `SCHEMA.md`.
- If a tag appears on 1-2 pages, either keep it only when semantically important or map it to an existing broader tag.
- If two tags mean the same thing, keep one canonical spelling and replace the other.

Declared-but-unused tag disposition for the first pass:

- `devops`: retain as reserved for infrastructure/runbook pages.
- `linux`: retain as reserved for system operation pages.
- `networking`: retain as reserved for network troubleshooting pages.
- `product`: retain for product/entity pages unless later audit proves it obsolete.

## 5. Normalization rules

### 5.1 Naming style

Use:

- lowercase
- kebab-case
- singular for abstract concepts when natural: `validation`, `governance`, `automation`
- explicit product/tool names when meaningful: `claude-code`

Avoid:

- mixed singular/plural variants for the same concept;
- temporary session names as tags;
- overly specific article-only tags;
- tags that duplicate `type`, `status`, or directory role.

### 5.2 Candidate mappings to review

These should be reviewed before replacement, not blindly changed:

- `ai-agent` → likely `agent`
- `agents` → likely `agent`
- `agent-workflow` → likely `agent` + `workflow`
- `coding-agent` → likely `ai-coding` or `agent` + `ai-coding`
- `self-validation` → likely `validation` + `verification`
- `review` → likely `validation` or `decision`, depending on page meaning
- `execution` → likely `workflow` or `automation`, depending on page meaning
- `benchmark` → likely `evaluation`
- `model-profiles` → likely keep if multiple model profile pages exist; otherwise map to `evaluation` or `configuration`

## 6. Step-by-step execution plan

### Step 1 — Create a reproducible tag audit script

Add a small script under:

- `_meta/scripts/wiki_tag_audit.py`

Expected behavior:

- parse YAML frontmatter tags from markdown files;
- parse declared taxonomy from `SCHEMA.md`;
- output JSON with:
  - declared tags;
  - actual tag counts;
  - undeclared tags;
  - declared-but-unused tags;
  - files per tag;
  - suggested high-frequency candidates.

Exit code convention should align with `wiki_health_check.py`:

- `0`: audit complete, no undeclared tags found;
- `1`: audit complete, undeclared tags found;
- `2`: CLI/runtime error.

Validation:

```bash
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki --format json
```

### Step 2 — Update `SCHEMA.md` taxonomy structure

Change only the `## Tag Taxonomy` section.

Add the three tag classes:

- Core tags
- Domain tags
- Facet tags

Keep existing legitimate tags unless clearly obsolete.

Merge the current legacy rule line — “新增 tag 前先更新本节，再在页面里使用” — into the updated governance rule block, so `SCHEMA.md` has one coherent taxonomy policy.

Add high-frequency current tags that are stable and useful, especially:

- `investment`
- `trading`
- `governance`
- `validation`
- `project`
- `monitoring`
- `ai-coding`
- `claude-code`
- `multi-agent`
- `operating-model`

Do not add every undeclared tag automatically.

### Step 3 — Normalize only obvious aliases

Apply a small, conservative replacement set first.

Before beginning Step 3, confirm `git status --short` is clean so rollback remains simple.

Candidate first-pass replacements:

- `ai-agent` → `agent`; skip files where `agent` is already present to avoid duplicate tags. For `concepts/typed-ai-agent-boundaries.md`, confirm `ai-coding` is retained before removing `ai-agent`.
- `agents` → `agent`
- `benchmark` → `evaluation`

Only replace when the file context confirms the meaning.

Do not change ambiguous tags in bulk.

### Step 4 — Re-run audit and wiki health checks

Run:

```bash
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki --format json
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
```

Expected gate:

- wiki health remains `pass=true`;
- P0 remains `0`;
- P1 remains `0`;
- undeclared tag count decreases materially, but does not need to reach zero;
- no markdown/frontmatter formatting errors.

### Step 5 — Update `log.md`

Append one concise entry with:

- date;
- scope;
- files changed;
- audit before/after summary;
- validation commands and results.

### Step 6 — Commit as one focused change

Commit only taxonomy-related files.

Suggested commit message:

```text
docs: 治理 wiki tag taxonomy
```

## 7. Files likely to change

Expected:

- `SCHEMA.md`
- `log.md`
- `_meta/scripts/wiki_tag_audit.py`
- selected markdown pages whose tags contain obvious aliases

Should not change:

- raw article content bodies
- existing page conclusions
- unrelated long pages or draft queries
- Hermes memory
- Hermes skills
- cron/runtime/provider config

## 8. Validation checklist

Before commit:

```bash
git status --short
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki --format json
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
```

Manual review:

- confirm `git status --short` was clean before tag replacements began;
- confirm no source URLs or credentials were altered;
- confirm raw content bodies were not rewritten;
- confirm tag replacements are semantic, not mechanical overreach;
- confirm `SCHEMA.md` documents the rule for adding new tags.

## 9. Risks and mitigations

Risk: over-normalizing tags loses useful distinctions.

- Mitigation: first pass only handles high-frequency additions and obvious aliases.

Risk: adding too many tags makes taxonomy meaningless.

- Mitigation: require recurrence or clear future retrieval value.

Risk: tag audit script becomes another maintenance burden.

- Mitigation: keep it small, read-only by default, and aligned with existing `wiki_health_check.py` style.

Risk: generated counts differ from previous custom scan.

- Mitigation: record the script output in the commit evidence; treat the script as the new reproducible baseline.

## 10. Open questions for execution

Resolve during execution, not before planning:

1. Should `lifeos` become a formal domain tag or be mapped to broader tags like `workflow` / `operating-model`?
2. Should `kickoff` remain a tag, or should kickoff pages be discovered by title/path instead?
3. Should `gstack` be kept as a project/product tag, or mapped to `project`?
4. Should `model-profiles` be a formal tag, or grouped under `evaluation` / `configuration`?

Default recommendation:

- Keep ambiguous tags unchanged in the first commit.
- Add stable high-frequency tags to `SCHEMA.md`.
- Normalize only obvious aliases.
