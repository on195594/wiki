---
title: "Automating Knowledge Graph Population: Extracting Entities and Triples from Unstructured Text with an LLM"
created: 2026-09-30
updated: 2026-09-30
type: raw-source
source: MachineLearningMastery.com
source_url: https://machinelearningmastery.com/automating-knowledge-graph-population-extracting-entities-and-triples-from-unstructured-text-with-an-llm/
author: Iván Palomares Carrascosa
published: 2026-09-29
captured: 2026-09-30
status: captured
source_quality: full
extraction: "Article-body text captured through web extraction; navigation, sharing widgets, related posts, comments and duplicate code-renderer tables removed. Code text retained with extractor escaping and flattened indentation; this is a reading snapshot, not runnable code. Article image retained as a URL, not visually verified."
---

> Capture scope: original article text from heading/byline through Conclusion, including setup, code text and example outputs. Python indentation is not preserved by the extractor; use the publisher page for executable formatting. No code was executed and no extraction-quality or Graph-RAG benchmark was independently reproduced. The introductory and trailing sharing widgets are omitted.

Automating Knowledge Graph Population: Extracting Entities and Triples from Unstructured Text with an LLM
=========================================================================================================

By [Iván Palomares Carrascosa](https://machinelearningmastery.com/author/ivanpc/) on September 29, 2026 in [Language Models](https://machinelearningmastery.com/category/language-models/ "View all items in Language Models")  [0](https://machinelearningmastery.com/automating-knowledge-graph-population-extracting-entities-and-triples-from-unstructured-text-with-an-llm/#respond)


In this article, you will learn how to automatically extract structured knowledge from raw text and populate a knowledge graph with SPOC quads using a local LLM via Ollama.

Topics we will cover include:

* How to set up Ollama with the Llama 3.2 model to run a free, local LLM for structured data extraction.
* How to design a robust extraction pipeline that converts unstructured Wikipedia text into SPOC (Subject-Predicate-Object-Context) quads using few-shot prompting and JSON output mode.
* How to load the extracted quads into a QuadStore knowledge graph, ready for use in a Graph-RAG retrieval pipeline.

![Automating Knowledge Graph Population: Extracting Entities and Triples from Unstructured Text with an LLM](https://machinelearningmastery.com/wp-content/uploads/2026/09/mlm-automating-knowledge-graph-population-extracting-entities-and-triples-from-unstructured-text-with-an-llm-feature.png)

Introduction
------------

The recent article on [Building a Deterministic 3-Tiered Graph-RAG System](https://machinelearningmastery.com/beyond-vector-search-building-a-deterministic-3-tiered-graph-rag-system/) shows how a hierarchical, graph-based architecture can tackle the issue of hallucinations in standard vector information retrieval.

That article leveraged [Quadstore](https://github.com/mmmayo13/quadstore), a lightweight knowledge graph database implemented in Python, to teach LLMs to respect ground-truth facts, thereby ensuring factual accuracy and deterministic retrieval conflict resolution in applications like RAG systems.

A critical question remains, though: where does the factual graph knowledge come from? This article helps close the loop, showing a free, fully automated approach to extract entities and build SPOC quads (Subject-Predicate-Object-Context) from raw text such as Wikipedia pages. We will do this with the help of a local, free LLM from Ollama. Once these quads are built, we will illustrate how to directly populate the Quadstore.

Prerequisites and Setup
-----------------------

The workflow shown in this article is designed to run seamlessly both in a Google Colab notebook and in your local Python IDE. If you choose the latter, you will need to manually install **Ollama** on your computer first, along with pulling the **Llama 3.2** model locally.

In Google Colab, you can set up Ollama and get Llama 3.2 for your open session using these commands:

!apt-get update -qq && apt-get install -y -qq zstd
!curl -fsSL https://ollama.com/install.sh | sh

Either way, you will need to install these two libraries as well:

!pip install wikipedia requests

Llama 3.2 is a lightweight, free model. Its API is configured to strictly operate in JSON input/output mode, a mandatory standard for reliable data extraction. Using `subprocess`, we can start the Ollama server as a background process and pull our target model:

import subprocess
import time
# 1. Starting the Ollama server in the background
print("Starting Ollama server...")
process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(3) # Give the server a moment to start
# 2. Pulling the Llama 3.2 model (this may take a minute or two on Colab)
print("Pulling Llama 3.2...")
subprocess.run(["ollama", "pull", "llama3.2"])
print("Model ready!")

Automated Knowledge Graph Population
------------------------------------

Let’s look at the process of constructing our knowledge graph from a source of raw text. We will convert narrative text into strictly modeled relationships that extend classical RDF triples of the form `(Subject, Predicate, Object)` by adding a fourth dimension: the context. This is useful for tracking where a fact comes from and whether it is true or not.

A triple like `("LeBron James", "plays_for", "Lakers")` thus becomes `("LeBron James", "plays_for", "Lakers", "NBA_2023_Roster")`.

First, we will create a small, simulated `QuadStore` engine that mimics the framework used in the related article this one follows up on. If you are working in a notebook, run this code in a separate cell to generate a `quadstore.py` file in your workspace on the fly:

%%writefile quadstore.py
class QuadStore:
def \_\_init\_\_(self):
# Using a simple list to store the facts for our lightweight implementation
self.quads = []
def add(self, subject, predicate, obj, context):
"""Adds a new SPOC quad to the knowledge graph."""
quad = (subject, predicate, obj, context)
if quad not in self.quads:
self.quads.append(quad)
def query(self, subject=None, predicate=None, obj=None, context=None):
"""Queries the graph. Returns a list of quads that match the provided criteria."""
results = []
for q\_sub, q\_pred, q\_obj, q\_ctx in self.quads:
if (subject is None or subject == q\_sub) and \
(predicate is None or predicate == q\_pred) and \
(obj is None or obj == q\_obj) and \
(context is None or context == q\_ctx):
results.append((q\_sub, q\_pred, q\_obj, q\_ctx))
return results

A file containing exactly the above code will be created, and we will refer to it later on just like any other Python module, to demonstrate how to load our created knowledge graph into our mock Graph-RAG system.

Back to the main process: we will now pull some raw text from Wikipedia using the namesake API. The `auto_suggest=False` option ensures we correctly fetch the right article name from Wikipedia without automated corrections that may cause a crash.

import wikipedia
print("Fetching Wikipedia summary...")
# Disabling auto\_suggest to prevent the library from renaming "Turing" to "tuning"
wiki\_page = wikipedia.page("Alan Turing", auto\_suggest=False)
text\_content = wiki\_page.summary
# We'll just take the first two paragraphs of the Wikipedia page to keep extraction fast
paragraphs = text\_content.split('\n')[:2]
short\_text = " ".join(paragraphs)
print(f"Extracted {len(short\_text)} characters of text ready for processing.")

Output:

Fetching Wikipedia summary...
Extracted 1244 characters of text ready for processing.

Now comes the core of the entire workflow: the robust extraction engine, modeled by the following function that:

* Works with the target LLM’s formatting engine to extract structured data in the form of quads. To do this, we use few-shot examples as part of the prompt sent to the LLM.
* Post-processes the LLM output to extract a list of facts and build a list of quads accordingly.

import json
import requests
def extract\_spoc\_quads\_final(text, context\_label, model="llama3.2"):
# To abide by Llama3.2's output mode, we ask for a JSON object with a "facts" key
prompt = f"""
You are an expert data extraction algorithm. Extract atomic facts from the text.
You must output a valid JSON object containing a single key called "facts".
The value of "facts" must be an array of objects.
Example output format:
{{
"facts": [
{{"subject": "LeBron James", "predicate": "plays\_for", "object": "Lakers"}},
{{"subject": "Lakers", "predicate": "based\_in", "object": "Los Angeles"}}
]
}}
Text to process:
{text}
"""
payload = {
"model": model,
"prompt": prompt,
"format": "json",
"stream": False,
"temperature": 0.0
}
try:
response = requests.post('http://localhost:11434/api/generate', json=payload)
response.raise\_for\_status()
raw\_llm\_text = response.json()['response']
parsed\_json = json.loads(raw\_llm\_text)
# Looking specifically for the "facts" array
triples = parsed\_json.get("facts", [])
# Fallback: If the LLM still used a different key, grab the first list we find
if not triples and isinstance(parsed\_json, dict):
for key, value in parsed\_json.items():
if isinstance(value, list):
triples = value
break
quads = []
for t in triples:
if not isinstance(t, dict): continue
# Converting keys to lowercase to catch "Subject" vs "subject"
normalized\_t = {str(k).lower().strip(): str(v).strip() for k, v in t.items()}
if all(k in normalized\_t for k in ('subject', 'predicate', 'object')):
quads.append({
"subject": normalized\_t['subject'],
"predicate": normalized\_t['predicate'],
"object": normalized\_t['object'],
"context": context\_label
})
return quads
except Exception as e:
print(f"Extraction failed: {e}")
return []

All that remains is running the pipeline to extract, view, and make use of our newly created quads, which will constitute our knowledge graph.

print("Beginning extraction (this takes a few seconds on a Colab T4 GPU)...\n")
extracted\_quads = extract\_spoc\_quads\_final(
text=short\_text,
context\_label="Wikipedia\_Alan\_Turing"
)
# Viewing the results
for quad in extracted\_quads:
print(f"S: {quad['subject']:<20} | P: {quad['predicate']:<15} | O: {quad['object']:<25} | C: {quad['context']}")

Results:

Beginning extraction (this takes a few seconds on a Colab T4 GPU)...
S: Alan Mathison Turing | P: was | O: an English mathematician, computer scientist, logician, cryptanalyst, philosopher and theoretical biologist | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: was born | O: in London | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: was raised | O: in southern England | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: graduated from | O: King's College, Cambridge | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: earned | O: a doctorate degree from Princeton University | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: worked for | O: the Government Code and Cypher School at Bletchley Park | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: led | O: Hut 8, the section responsible for German naval cryptanalysis | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: devised techniques for | O: speeding the breaking of German ciphers | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: played a crucial role in | O: cracking intercepted messages that enabled the Allies to defeat the Axis powers | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: is | O: widely considered to be the father of theoretical computer science | C: Wikipedia\_Alan\_Turing
S: Alan Mathison Turing | P: was | O: influential in the development of theoretical computer science | C: Wikipedia\_Alan\_Turing

From just two paragraphs of Alan Turing’s Wikipedia article, we extracted around 11 facts, structured as quads. Note that the exact number may vary slightly due to the non-deterministic behavior of the LLM.

We wrap up by seeing how to add these facts into the `QuadStore` object:

from quadstore import QuadStore
facts\_qs = QuadStore()
for quad in extracted\_quads:
facts\_qs.add(
quad["subject"],
quad["predicate"],
quad["object"],
quad["context"]
)
print(f"Successfully loaded {len(extracted\_quads)} automated facts into the Graph RAG system!")

Output:

Successfully loaded 11 automated facts into the Graph RAG system!

Conclusion
----------

This article closed the loop on our [deterministic 3-tiered Graph-RAG architecture](https://machinelearningmastery.com/beyond-vector-search-building-a-deterministic-3-tiered-graph-rag-system/) by showing how to build a knowledge graph consisting of facts extracted directly from unstructured text in the form of quads — all from scratch. You can now integrate this knowledge into your retrieval pipeline to help eliminate issues like LLM hallucinations.
