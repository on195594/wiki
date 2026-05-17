---
title: Claude Review - AI Agent Document Fidelity Risk Wiki Ingestion
created: 2026-05-17
updated: 2026-05-17
type: review
status: complete
---

# Claude Review - AI Agent Document Fidelity Risk Wiki Ingestion

## Verdict

PASS_WITH_MINOR_FIXES

## Blocking

- 无。

## Important

- Claude flagged the raw source phrase `Gemini 3.1 Pro, Claude 4.6 Opus, and GPT 5.4` as a possible source-integrity concern because `Claude 4.6 Opus` does not match known Claude naming conventions. Follow-up verification fetched the live VentureBeat HTML directly with browser-like headers and extracted the `<article>` text; the same phrase appears in the live article text. Therefore this is preserved as source text, while the concept page correctly avoids turning model names/rankings into durable conclusions.

## Minor

1. Raw source repeated the extraction note in both frontmatter and source metadata.
2. `summary_path` points outside the wiki under `/home/lin/.hermes/...`; acceptable as a traceability pointer, but not a durable wiki-internal source.
3. Concept page tags could include `research` because the page is grounded in a reported Microsoft benchmark.

## Accepted patches

- Removed the duplicate extraction-note bullet from the raw source metadata section.
- Added `research` to the concept page tags.
- Left the external `summary_path` as traceability metadata.
- Left the model-name phrase unchanged in raw source after direct HTML verification; concept page keeps model names out of durable claims.

## Evidence checked by Claude

- `raw/articles/venturebeat-frontier-ai-document-fidelity-risk-2026-05-13.md`: frontmatter present; raw source captured; model-name anomaly flagged.
- `concepts/ai-agent-document-fidelity-risk.md`: DELEGATE-52, multi-step degradation, hidden rewriting, generic-tool degradation, RAG noise compounding, and round-trip relay are preserved; benchmarks are labelled as source-specific directional figures.
- `index.md`: new concept entry present.
- `log.md`: ingestion entry present.
- Cross-links reviewed:
  - `concepts/production-ai-agent-evaluation-framework.md`
  - `concepts/agent-self-validation-loops.md`
  - `concepts/typed-ai-agent-boundaries.md`

## Follow-up verification

Command used for source phrase verification:

```bash
python3 - <<'PY'
import requests
from bs4 import BeautifulSoup
url='https://venturebeat.com/orchestration/frontier-ai-models-dont-just-delete-document-content-they-rewrite-it-and-the-errors-are-nearly-impossible-to-catch'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36','Accept':'text/html,application/xhtml+xml','Accept-Encoding':'identity'}
html=requests.get(url,headers=headers,timeout=30).text
soup=BeautifulSoup(html,'html.parser')
text=(soup.select_one('article') or soup).get_text('\n', strip=True)
for line in text.splitlines():
    if 'Claude' in line or 'GPT 5.4' in line or 'Gemini 3.1' in line:
        print(line)
PY
```

Result: live article text contains the same model-name phrase.
