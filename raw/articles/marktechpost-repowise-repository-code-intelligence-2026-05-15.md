---
title: How to Build Repository-Level Code Intelligence with Repowise Using Graph Analysis, Dead-Code Detection, Decisions, and AI Context
author: Sana Hassan
source_type: article
source_url: https://www.marktechpost.com/2026/05/15/how-to-build-repository-level-code-intelligence-with-repowise-using-graph-analysis-dead-code-detection-decisions-and-ai-context/
publisher: MarkTechPost
published_at: 2026-05-15
captured_at: 2026-05-17
extraction: nested_jina_reader_after_direct_extract_summary
status: raw
tags: [ai-coding, architecture, workflow]
---

# How to Build Repository-Level Code Intelligence with Repowise Using Graph Analysis, Dead-Code Detection, Decisions, and AI Context

Source URL: https://www.marktechpost.com/2026/05/15/how-to-build-repository-level-code-intelligence-with-repowise-using-graph-analysis-dead-code-detection-decisions-and-ai-context/

Extraction note: Generic extraction returned a generated summary instead of source prose. Direct MarkTechPost access is bot-challenged, so this raw capture uses the verified nested Jina Reader fallback (`https://r.jina.ai/http://r.jina.ai/http://<source-url>`), then removes obvious navigation, share, and publisher-promo boilerplate. Some code snippets are preserved as raw extracted lines because the source is a tutorial.

Gemini summary path: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260517-171907-MarkTechPost-Repowise-repository-level-code-intelligence-321801-070283600-summary.md`

## Raw article text

Title: How to Build Repository-Level Code Intelligence with Repowise Using Graph Analysis, Dead-Code Detection, Decisions, and AI Context

URL Source: https://www.marktechpost.com/2026/05/15/how-to-build-repository-level-code-intelligence-with-repowise-using-graph-analysis-dead-code-detection-decisions-and-ai-context/

Published Time: 2026-05-16T06:45:19+00:00

Markdown Content:

How to Build Repository-Level Code Intelligence with Repowise Using Graph Analysis, Dead-Code Detection, Decisions, and AI Context

By Sana Hassan

May 15, 2026

In this tutorial, we explore how to use [**Repowise**](https://github.com/repowise-dev/repowise) to build repository-level intelligence for the itsdangerous Python project in a practical and reproducible way.
import os, sys, json, subprocess, textwrap, shutil, re
from pathlib import Path
TARGET = Path("/content/itsdangerous")
assert TARGET.exists(), "Run §1–§2 first to clone the target repo."
os.chdir(TARGET)
def sh(cmd, check=False, cwd=None, timeout=None, env=None):
   print(f"\n$ {cmd}")
   proc = subprocess.run(
       cmd, shell=True,
       env={**os.environ, **(env or {})},
       cwd=cwd, text=True, timeout=timeout,
       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
   )
   if proc.stdout:
       print(proc.stdout.rstrip())
   print(f"  ↳ exit {proc.returncode}")
   if check and proc.returncode != 0:
       raise RuntimeError(f"command failed (exit {proc.returncode}): {cmd}")
   return proc
def banner(t):
   print(f"\n{'═'*(len(t)+4)}\n  {t}\n{'═'*(len(t)+4)}")

We begin by importing the required libraries, setting the target repository path, and moving into the itsdangerous project directory. We define a reusable sh() helper function to run shell commands, capture their output, and display exit codes clearly. We also create a banner() function so each tutorial section prints with a readable heading.

 Join 150k+ members of our ML Subreddit Community..
banner("§5  Building intelligence layers (fixed)")
sh("repowise --version")
sh("repowise init --help")
HAS_ANTHROPIC = bool(os.environ.get("ANTHROPIC_API_KEY"))
HAS_OPENAI    = bool(os.environ.get("OPENAI_API_KEY"))
HAS_LLM       = HAS_ANTHROPIC or HAS_OPENAI
if HAS_ANTHROPIC:
   provider, model = "anthropic", "claude-sonnet-4-5"
elif HAS_OPENAI:
   provider, model = "openai", "gpt-4o-mini"
else:
   provider, model = "mock", "mock"
(TARGET / ".repowise").mkdir(exist_ok=True)
(TARGET / ".repowise" / "config.yaml").write_text(textwrap.dedent(f"""
   provider: {provider}
   model: {model}
   embedding_model: voyage-3
   reasoning: auto
   git:
     co_change_commit_limit: 200
     blame_enabled: true
   dead_code:
     enabled: true
     safe_to_delete_threshold: 0.7
   maintenance:
     cascade_budget: 10
""").lstrip())
print(f"Provider chosen: {provider}  |  LLM available: {HAS_LLM}")
init_cmd = "repowise init . --index-only" if not HAS_LLM else "repowise init ."
res = sh(init_cmd, timeout=20*60)
if res.returncode != 0:
   print("\n  init still failed. Things to try:")
   print("   • pip install -U repowise   (older versions lacked --index-only)")
   print("   • set an ANTHROPIC_API_KEY  and re-run without --index-only")
   print("   • copy the FIRST error line above — it tells the real story")
   raise SystemExit(1)

We start the Repowise initialization stage by checking the installed version and viewing the supported init options. We determine whether an Anthropic or OpenAI API key is available, then automatically select the correct provider and model configuration. We write the .repowise/config.yaml file and run Repowise initialization, using index-only mode when no LLM key is available.

banner("§6  .repowise/ artifact tree")
for p in sorted((TARGET / ".repowise").rglob("*")):
   if p.is_file():
       print(f"  {str(p.relative_to(TARGET)):60s}  {p.stat().st_size:>9,d} B")
banner("§7  Graph Intelligence")
import networkx as nx
G = None
for gp in (TARGET / ".repowise").rglob("*"):
   if gp.is_file() and gp.suffix in {".json", ".gml", ".graphml"} and "graph" in gp.name.lower():
       try:
           if gp.suffix == ".json":
               data = json.loads(gp.read_text())
               if isinstance(data, dict) and "nodes" in data:
                   G = nx.node_link_graph(data)
           elif gp.suffix == ".gml":
               G = nx.read_gml(gp)
           elif gp.suffix == ".graphml":
               G = nx.read_graphml(gp)
           if G is not None:
               print(f"Loaded {gp.name}: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
               break
       except Exception as e:
           print(f"  ({gp.name}: {e})")
pr = {}
if G is not None:
   pr = nx.pagerank(G)
   print("\nTop 10 nodes by PageRank:")
   for n, s in sorted(pr.items(), key=lambda x: -x[1])[:10]:
       print(f"  {s:.4f}  {n}")
   try:
       from networkx.algorithms.community import greedy_modularity_communities
       comms = list(greedy_modularity_communities(G.to_undirected()))
       print(f"\n{len(comms)} communities detected; sizes:",
             [len(c) for c in comms[:8]])
   except Exception as e:
       print(f"  communities skipped: {e}")
else:
   print("(no graph artifact found — your version may name it differently;"
         " run  `ls -R .repowise/`  to inspect.)")

We inspect the generated .repowise artifact tree to understand what files Repowise creates after indexing the repository. We then search for graph artifacts, load the repository graph using NetworkX, and print the number of nodes and edges. We calculate PageRank scores, display the most important nodes, and detect communities to understand how the codebase is structurally grouped.

banner("§8  Git Intelligence")
sh("repowise status")
banner("§9  Doc Intelligence")
if HAS_LLM:
   sh('repowise search "URL-safe token signing"')
   sh('repowise query "How does Signer detect tampered payloads?"')
else:
   print("(skipped — no LLM key set; provider=mock can't answer real questions)")
banner("§10  Dead-code detection")
sh("repowise dead-code")
sh("repowise dead-code --safe-only")
banner("§11  Architectural decisions")
src = TARGET / "src" / "itsdangerous" / "signer.py"
if src.exists() and "DECISION:" not in src.read_text():
   src.write_text(
       "# DECISION: Signers are stateless by design — secrets are passed at\n"
       "# construction so signing can be parallelised safely.\n"
       + src.read_text()
   )
   sh('git -c user.email=demo@x -c user.name=demo commit -am "demo: inline decision"')
sh("repowise update .")
sh("repowise decision list")
sh("repowise decision health")

We use Repowise status to inspect Git intelligence and understand the current repository state. We then run documentation-focused search and query commands when an LLM key is available, while safely skipping them in mock mode. We also run dead-code detection, insert an inline architectural decision into signer.py, update Repowise, and check the decision list and decision health.

banner("§12  CLAUDE.md")
sh("repowise generate-claude-md")
md = TARGET / "CLAUDE.md"
if md.exists():
   print(md.read_text()[:4000])
banner("§13  MCP tools via CLI")
base = [
   ("get_dead_code",            "repowise dead-code --safe-only"),
   ("search_codebase",          'repowise search "timestamp expiry validation"'),
]
llm_only = [
   ("get_overview",             'repowise query "Architecture overview please"'),
   ("get_context",              'repowise query "Explain signer and serializer modules"'),
   ("get_risk",                 'repowise query "What is risky about changing signer.py?"'),
   ("get_why",                  'repowise query "Why are signers stateless?"'),
   ("get_dependency_path",      'repowise query "How does URLSafeSerializer reach Signer?"'),
   ("get_architecture_diagram", 'repowise query "Produce a Mermaid diagram of the package"'),
]
for name, cmd in base + (llm_only if HAS_LLM else []):
   print(f"\n────  {name}  ────")
   sh(cmd)
if not HAS_LLM:
   print("\n(7 of 9 tools above need an LLM key — set ANTHROPIC_API_KEY and re-run §13.)")
banner("§14  Graph plot")
if G is not None:
   import matplotlib.pyplot as plt
   top = [n for n, _ in sorted(pr.items(), key=lambda x: -x[1])[:40]]
   H = G.subgraph(top).copy()
   sizes = [4000 * pr[n] / max(pr.values()) + 80 for n in H.nodes]
   plt.figure(figsize=(12, 8))
   pos = nx.spring_layout(H, seed=7, k=0.9)
   nx.draw_networkx_edges(H, pos, alpha=0.25, arrows=False)
   nx.draw_networkx_nodes(H, pos, node_size=sizes, node_color="#F59520", alpha=0.85)
   nx.draw_networkx_labels(H, pos,
       labels={n: Path(n).name if isinstance(n, str) else n for n in H.nodes},
       font_size=8)
   plt.title("itsdangerous — top-40 nodes by PageRank")
   plt.axis("off"); plt.tight_layout(); plt.show()
print("\n done.")

We generate a CLAUDE.md file to expose useful project context for AI-assisted development. We then run several Repowise MCP-style tools through CLI commands, including dead-code checks, code search, and LLM-powered architecture queries when available. Also, we visualize the top PageRank nodes in the repository graph to clearly see the most influential files and relationships.

In conclusion, we created a practical workflow for turning a standard code repository into an intelligence-rich project workspace that supports a deeper understanding of the codebase. We used Repowise to index and inspect the codebase, uncover graph relationships, identify important files, detect potential dead code, document architectural decisions, and prepare context files for AI-assisted development. This gives us a clear view of how repository intelligence tools can improve code understanding, maintenance, refactoring, collaboration, and future onboarding, while still working in both LLM-enabled and mock-provider modes.
