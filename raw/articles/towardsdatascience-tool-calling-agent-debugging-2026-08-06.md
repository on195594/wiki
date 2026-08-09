---
title: I Built a Tool-Calling Agent in Python. Here’s How I Debugged It
author: [Abdullahi Dattijo]
created: 2026-08-09
updated: 2026-08-09
type: raw-source
status: captured
source: Towards Data Science
source_url: https://towardsdatascience.com/i-built-a-tool-calling-agent-in-python-heres-how-i-debugged-it/
published: 2026-08-06
captured: 2026-08-09
extraction: browser DOM main.innerText via persistent CDP; complete visible article prose through Selected Sources with author/share/publisher footer removed; code indentation and figure pixels are not preserved; not byte-faithful HTML
tags: [agent, debugging, evaluation, tool]
---

# I Built a Tool-Calling Agent in Python. Here’s How I Debugged It

## Provenance

- Source URL: https://towardsdatascience.com/i-built-a-tool-calling-agent-in-python-heres-how-i-debugged-it/
- Source: Towards Data Science
- Author: Abdullahi Dattijo
- Published: 2026-08-06
- Captured: 2026-08-09
- Local summary (local-only auxiliary path, not a stable long-term source): `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260809-230723-I-Built-a-Tool-Calling-Agent-in-Python.-Here’s-How-I-Debugged-It-3200861-612734240-summary.md`
- Extraction route: rendered `main.innerText` from the live browser through persistent CDP
- Source quality: complete visible article prose from the opening through `Selected Sources`; author/share/publisher footer removed; not a byte-faithful HTML capture

## Source limitations

- This is a hands-on practitioner tutorial and one reported debugging run, not a comparative reliability benchmark or production incident dataset.
- The opening model failure is a reported provider/server error that occurred before tool execution; it demonstrates a boundary but does not establish failure frequency.
- The malformed-argument recovery was produced by deliberate fault injection, because the author states the normal API did not emit invalid JSON in that run.
- Weights & Biases Weave is the author’s optional trace implementation, not evidence that Hermes should adopt that product or add new telemetry.
- Browser DOM extraction preserves visible prose and code text but flattens code indentation and does not preserve figure pixels or byte-faithful HTML.

## Extracted article body

AGENTIC AI
I Built a Tool-Calling Agent in Python. Here’s How I Debugged It

A minimal loop with real API calls, validation, compact outputs, and trace evidence before adding an agent framework.

Abdullahi Dattijo
Aug 6, 2026
21 min read
A transparent two-stage tool-calling system converts a Lagos map location into coordinates, validates them, retrieves a rain forecast, and records each step along an evidence trace. Image generated with ChatGPT.

I asked my tool-calling agent about the weather in a city that doesn’t exist, expecting the failure to show up in my own code, a tool that couldn’t find the place. Instead, the call to the AI model itself failed first, before any of my code or my tools ever ran, and the script crashed with a raw stack trace. I added one thing: a try/except around that model call. With it in place, the same broken prompt no longer crashed. It came back as a clean error instead, telling me exactly which step had failed:

Screenshot by author. The agent was given a made-up city, but the request failed before the location tool could run.

That distinction, model request versus tool execution, is the reason the loop needs a separate error path for each one.

That gap, between a crash and a readable failure, is what this article is actually about. A tool-calling agent is impressive when it works. But when it fails, the final answer alone is not enough. Stop judging a tool-calling agent by its final answer. Judge it by the model request, the schema validation, the Python execution, the compact tool result, the error path, and the final answer, together.

If you have built a small agent around a product API, a retrieval endpoint, a database lookup, a weather service, or a Model Context Protocol (MCP) tool, you have probably seen the same problem. The model says it checked something. Maybe it did. Maybe it sent malformed arguments. Maybe the API returned no result. Maybe the model request failed before your tool ran at all. Without the message history, tool arguments, returned payload, and final answer in one place, you are trusting a story instead of inspecting a run.

This article builds that inspectable loop from the ground up: an agent instructed to answer a weather question by calling two real public APIs, validates every tool argument with JSON Schema before anything runs, keeps tool outputs compact, catches model request failures instead of crashing on them, and can write the full run to a Weights & Biases (W&B) Weave trace for review. Weather is standing in for the service-backed tasks agents usually get built for: checking a package, retrieving a customer record, looking up inventory, pricing an order, calling an internal API. By the end, you will have a script that can:

define tools with JSON Schema for an OpenAI model
run a bounded tool calling loop
validate tool names and arguments before execution
keep tool outputs compact before returning them to the model
return a structured error if the model request itself fails
capture run evidence in console output and Weave
Image by author. The useful review points are the model request, Python validation, Python execution, compact result shaping, final answer, and trace record.
The run should answer four questions

A tool-calling agent may answer, “I checked the API,” but the useful questions start after that sentence:

Which tool did the model request?
What arguments did it send?
What did Python return?
Did the final answer use the returned data or hide a failure?

The tutorial builds a small agent around those questions. The user asks whether to carry an umbrella in Lagos. The model is expected to request a city lookup, receive coordinates, request weather, receive a forecast, and answer from that returned data. When it works, the final answer looks like this:

Yes, you should carry an umbrella in Lagos tomorrow. There is a high chance of rain (84%) with about 6.5 mm of precipitation expected.

Every step behind that one sentence, the tool requests, the arguments, the returned data, is printed and can be traced.

If you can inspect this small loop, the same habit carries into more serious service-backed agents. A refund agent should show the order lookup, policy check, refund decision, and final message. A document agent should show the search query, retrieved passages, and answer. An MCP tool should still show the tool name, arguments, result, and error path.

What a tool calling agent actually does

A tool calling agent in Python is a loop driven by a large language model, or LLM. It lets the model request named functions, receive their results, and continue with updated messages.

That sounds close to a chatbot, but the behavior is different. A chatbot receives text and returns text. A tool calling agent receives text, may request action, waits for your application to execute that action, reads the tool result, and then decides what to say or do next.

The important pieces are plain engineering objects:

The model decides whether it needs a tool.
The tool is a Python function owned by your application.
The schema specifies the arguments the tool accepts.
The messages are the running record of the user request, model tool requests, tool results, and final answer.
The agent loop is your Python code that keeps the process running until the model stops requesting tools.

A basic function call is one request and one result. An agent loop is the repeated version. The model can ask for one tool, read the result, ask for another tool, and keep going until it has enough context.

The weather example uses two tools:

geocode_city, which turns a city name into latitude, longitude, and country.
get_weather, which turns latitude and longitude into a compact weather report.

In a real application, those functions call external APIs. A package tool might call a shipping provider. A flight tool might call an airline status service. A shopping tool might call an inventory system. In this article, the tools use Nominatim from OpenStreetMap for geocoding and Open-Meteo for weather data. Those services keep the example real while still being small enough to read. They also do not require API keys for this tutorial run, so the only key you need is the OpenAI key used for the model call.

The message loop this article exposes

Your app sends the user message and the list of available tools to the model. If the model needs a tool, it returns a structured request. Your Python application reads that request, runs the matching function, sends the result back as a tool message, and asks the model to continue.

The newer OpenAI Responses API follows the same idea. It also supports built in tools, including web search and file search, so the tool can be provided by OpenAI or by your own application.

The first useful idea is simple: the model chooses, but your code executes.

That boundary matters. Your application should still decide whether a requested tool exists, whether the arguments match the schema, whether the call is allowed, how much data to return, what to log, and when to stop the loop.

Why start without a framework

It is worth building one custom Python loop before adopting a larger agent framework. The first version teaches you what is easy to inspect. Once you understand the raw message flow, you can make a better decision about whether a framework removes complexity or hides it.

The same idea applies to MCP. The official MCP documentation describes MCP as a standard way for applications to provide context to large language models. An MCP server can expose tools, resources, and prompts to an AI client, but the design questions remain the same: What arguments are valid? What should the tool return? What happens when the model request fails? What happens when the tool returns no result?

Path	Best when you need	What you give up
Direct model API	Direct access to messages, schemas, retries, logging, and cost	You write the loop yourself
MCP server	A standard way to expose tools, resources, or prompts across AI clients	You still need to design the tool behavior and error shape
Local model runtime	Local execution, data locality, or offline testing	Model support and output formats can vary
Agent framework	Many tools, state, routing, memory, or shared team patterns	More abstraction around the exact message flow

For this tutorial, the main path uses the OpenAI Python software development kit, or SDK. Local runtimes that support tool calling, including Ollama, follow the same pattern with different response formats. The goal here is to build the loop once where every object is visible.

Create one folder and set up the environment

Create one working folder for this article, then run every setup and execution command from that folder. The folder will contain the virtual environment and openai_tool_calling_agent.py. Use Python 3.11 or newer. You do not need a graphics processing unit, or GPU, because the main path calls a hosted OpenAI model. The geocoding and weather tools use public APIs that do not require their own keys.

On macOS or Linux, open a terminal in that working folder and run:

python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install openai requests weave jsonschema

On Windows PowerShell, open the same working folder and run:

py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install openai requests weave jsonschema

In the same activated terminal, set your OpenAI key before the model run. On macOS or Linux, run:

export OPENAI_API_KEY="your_api_key_here"

On Windows PowerShell, run:

$env:OPENAI_API_KEY="your_api_key_here"

In the same activated terminal, if you want Weave tracing, log in to W&B:

wandb login

Verify the Python version:

python --version

Expected output will look similar to this:

Python 3.11.9
Save the complete runnable script

Save the following code as openai_tool_calling_agent.py in the same working folder where you created .venv. This is the only file readers need to create. The sections after the code explain the design choices, but they do not add any additional required code.

```python
import argparse
import json
import os
from typing import Any

import requests
from jsonschema import ValidationError, validate
from openai import OpenAI, OpenAIError

try:
    import weave
except ImportError:
    weave = None


REQUEST_TIMEOUT = 10
USER_AGENT = "tool-calling-agent-python/1.0"
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1")


def geocode_city(city: str) -> dict[str, Any]:
    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": city, "format": "jsonv2", "limit": 1, "addressdetails": 1},
        headers={"User-Agent": USER_AGENT},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    results = response.json()
    if not results:
        return {"error": f"City not found: {city}"}

    first = results[0]
    address = first.get("address", {})
    return {
        "city": first.get("name", city),
        "country": address.get("country"),
        "latitude": float(first["lat"]),
        "longitude": float(first["lon"]),
    }


def get_weather(latitude: float, longitude: float, city: str) -> dict[str, Any]:
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,precipitation,rain,weather_code",
            "daily": (
                "weather_code,temperature_2m_max,temperature_2m_min,"
                "precipitation_sum,precipitation_probability_max"
            ),
            "forecast_days": 2,
            "timezone": "auto",
        },
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    data = response.json()
    current = data.get("current", {})
    daily = data.get("daily", {})

    def tomorrow_value(field: str) -> Any:
        values = daily.get(field) or []
        return values[1] if len(values) > 1 else None

    return {
        "city": city,
        "temperature_c": current.get("temperature_2m"),
        "precipitation_mm": current.get("precipitation"),
        "rain_mm": current.get("rain"),
        "weather_code": current.get("weather_code"),
        "tomorrow_weather_code": tomorrow_value("weather_code"),
        "tomorrow_temperature_max_c": tomorrow_value("temperature_2m_max"),
        "tomorrow_temperature_min_c": tomorrow_value("temperature_2m_min"),
        "tomorrow_precipitation_sum_mm": tomorrow_value("precipitation_sum"),
        "tomorrow_rain_chance_percent": tomorrow_value("precipitation_probability_max"),
    }


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "geocode_city",
            "description": "Find latitude, longitude, and country for a supported city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name, such as Lagos, London, or New York.",
                    }
                },
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get a compact weather report for a known location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                    "city": {"type": "string"},
                },
                "required": ["latitude", "longitude", "city"],
                "additionalProperties": False,
            },
        },
    },
]

TOOL_REGISTRY = {
    "geocode_city": geocode_city,
    "get_weather": get_weather,
}

SCHEMAS_BY_TOOL = {
    tool["function"]["name"]: tool["function"]["parameters"]
    for tool in TOOLS
}


def compact_tool_result(result: dict[str, Any]) -> dict[str, Any]:
    if "error" in result:
        return {"error": result["error"]}

    allowed_keys = {
        "city",
        "country",
        "latitude",
        "longitude",
        "temperature_c",
        "precipitation_mm",
        "rain_mm",
        "weather_code",
        "tomorrow_weather_code",
        "tomorrow_temperature_max_c",
        "tomorrow_temperature_min_c",
        "tomorrow_precipitation_sum_mm",
        "tomorrow_rain_chance_percent",
    }
    return {key: value for key, value in result.items() if key in allowed_keys}


def execute_tool_call(tool_name: str, tool_args: dict[str, Any]) -> dict[str, Any]:
    if tool_name not in TOOL_REGISTRY:
        return {"error": f"Unknown tool: {tool_name}"}

    try:
        validate(instance=tool_args, schema=SCHEMAS_BY_TOOL[tool_name])
    except ValidationError as exc:
        return {"error": "Invalid tool arguments", "details": exc.message}

    try:
        return TOOL_REGISTRY[tool_name](**tool_args)
    except Exception as exc:
        return {"error": "Tool execution failed", "details": str(exc)}


def maybe_trace(name):
    if weave is None:
        return lambda fn: fn
    return weave.op(name=name)


@maybe_trace("run_agent")
def run_agent(user_prompt: str, max_turns: int = 4) -> dict[str, Any]:
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": (
                "You are a concise weather assistant. "
                "Call tools only when they add facts needed for the answer."
            ),
        },
        {"role": "user", "content": user_prompt},
    ]
    transcript: list[dict[str, Any]] = []

    for turn in range(max_turns):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOLS,
            )
        except OpenAIError as exc:
            return {
                "model": MODEL,
                "user_prompt": user_prompt,
                "answer": "",
                "error": {
                    "type": "model_request_failed",
                    "details": str(exc),
                },
                "transcript": transcript,
            }
        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        tool_calls = assistant_message.tool_calls or []
        if not tool_calls:
            return {
                "model": MODEL,
                "user_prompt": user_prompt,
                "answer": assistant_message.content or "",
                "transcript": transcript,
            }

        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            try:
                tool_args = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError as exc:
                tool_args = {"raw_arguments": tool_call.function.arguments}
                raw_result = {
                    "error": "Malformed tool arguments",
                    "details": str(exc),
                }
            else:
                raw_result = execute_tool_call(tool_name, tool_args)
            tool_result = compact_tool_result(raw_result)

            transcript.append(
                {
                    "turn": turn + 1,
                    "tool": tool_name,
                    "arguments": tool_args,
                    "result": tool_result,
                }
            )
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(tool_result),
                }
            )

    return {
        "model": MODEL,
        "user_prompt": user_prompt,
        "answer": "I could not finish because the agent reached its tool call limit.",
        "transcript": transcript,
    }


def verify() -> dict[str, Any]:
    bad_arguments = execute_tool_call("get_weather", {"city": "Lagos"})
    unknown_tool = execute_tool_call("lookup_package", {"tracking_id": "123"})
    schema_names = sorted(SCHEMAS_BY_TOOL)
    return {
        "status": "ok",
        "model": MODEL,
        "tools": schema_names,
        "bad_arguments_check": bad_arguments,
        "unknown_tool_check": unknown_tool,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["verify", "run"], default="run")
    parser.add_argument(
        "--prompt",
        default="Should I carry an umbrella in Lagos tomorrow?",
    )
    parser.add_argument("--weave-project", default="")
    args = parser.parse_args()

    if args.mode == "verify":
        print(json.dumps(verify(), indent=2))
        return

    if args.weave_project:
        if weave is None:
            raise RuntimeError("Install weave before using --weave-project.")
        weave.init(args.weave_project)

    result = run_agent(args.prompt)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

Run a preflight check before spending tokens

Run this command from the same working folder and the same activated terminal. It checks imports, the tool registry, JSON Schema validation, and unknown tool handling without using the OpenAI API.

python openai_tool_calling_agent.py --mode verify

Captured output from my preflight run:

{
  "status": "ok",
  "model": "gpt-4.1",
  "tools": [
    "geocode_city",
    "get_weather"
  ],
  "bad_arguments_check": {
    "error": "Invalid tool arguments",
    "details": "'latitude' is a required property"
  },
  "unknown_tool_check": {
    "error": "Unknown tool: lookup_package"
  }
}

This is the first reason to build the loop yourself. Before the model is involved, you can check that the Python layer refuses an unknown tool and catches a malformed get_weather call.

Run the agent against real APIs

After setting OPENAI_API_KEY, run the full tool calling loop from the same working folder and activated terminal:

python openai_tool_calling_agent.py --mode run --prompt "Should I carry an umbrella in Lagos tomorrow?"

The script prints JSON. It includes the model name, the user prompt, the final answer, and a transcript of each tool call. In my successful weather run, the model requested geocode_city first, then get_weather, then wrote the final answer from the compact weather payload.

For readability, the same captured run is formatted below as a step-by-step trace:

[MODEL]
gpt-4.1

[USER PROMPT]
Should I carry an umbrella in Lagos tomorrow?

[OPENAI REQUESTS TOOL turn 1]
{
  "arguments": {
    "city": "Lagos"
  },
  "tool": "geocode_city"
}

[PYTHON RUNS geocode_city]
{
  "city": "Lagos",
  "country": "Nigeria",
  "latitude": 6.4550575,
  "longitude": 3.3941795
}

[OPENAI REQUESTS TOOL turn 2]
{
  "arguments": {
    "city": "Lagos",
    "latitude": 6.4550575,
    "longitude": 3.3941795
  },
  "tool": "get_weather"
}

[PYTHON RUNS get_weather]
{
  "city": "Lagos",
  "precipitation_mm": 0.0,
  "rain_mm": 0.0,
  "temperature_c": 27.7,
  "tomorrow_precipitation_sum_mm": 6.5,
  "tomorrow_rain_chance_percent": 84,
  "tomorrow_temperature_max_c": 28.9,
  "tomorrow_temperature_min_c": 24.6,
  "tomorrow_weather_code": 80,
  "weather_code": 3
}

[FINAL ANSWER]
Yes, you should carry an umbrella in Lagos tomorrow. There is a high chance of rain (84%) with about 6.5 mm of precipitation expected.

That output is the audit trail. The model did not magically know Lagos weather. It requested coordinates, your Python code fetched them, the model requested a forecast, your Python code fetched a compact forecast, and the final answer used that returned data.

Run one messy prompt

A clean run proves the loop can finish. It does not prove the loop is pleasant to debug when something goes wrong. This is the messier prompt from the opening, in full:

OPENAI_MODEL=gpt-4.1-mini python openai_tool_calling_agent.py --mode run --prompt "Should I carry an umbrella in Xqznotacity tomorrow? If that place is not real, tell me what failed."

The prompt was meant to exercise the geocoder path with a place that should not exist. The first failure appeared earlier than that: the model request itself returned a server error. Before adding the OpenAIError handler, this crashed the script with a stack trace. After the change, the agent returned a structured failure:

{
  "model": "gpt-4.1-mini",
  "user_prompt": "Should I carry an umbrella in Xqznotacity tomorrow? If that place is not real, tell me what failed.",
  "answer": "",
  "error": {
    "type": "model_request_failed",
    "details": "Error code: 500 ... server_error"
  },
  "transcript": []
}

This is a better edge case than I expected. The first boundary in a tool calling agent is the model request. If that fails, the application should return a useful error instead of hiding the problem behind a generic crash.

Testing the other failure path: malformed arguments

The OpenAIError handler above covers the model request itself failing. The json.JSONDecodeError handler covers a different failure: the model successfully returns a tool call, but the arguments string cannot be parsed as JSON.

OpenAI’s API does not actually return invalid JSON in normal use, so this path cannot be triggered just by asking a broken question. To test it for real rather than assume it works, I let the agent make its normal request, then deliberately truncated the real arguments the model sent, right before they reached json.loads, and let the rest of the loop run unmodified:

[FAULT INJECTION] real arguments were: {"city":"Lagos"}
[FAULT INJECTION] truncated to:         {"city":

The handler caught it and returned a result instead of crashing:

{
  "turn": 1,
  "tool": "geocode_city",
  "arguments": {
    "raw_arguments": "{\"city\":"
  },
  "result": {
    "error": "Malformed tool arguments"
  }
}

What happened next was not something I coded: on the next turn, the model read that error and retried the same tool with valid arguments on its own.

{
  "turn": 2,
  "tool": "geocode_city",
  "arguments": {
    "city": "Lagos"
  },
  "result": {
    "city": "Lagos",
    "country": "Nigeria",
    "latitude": 6.4550575,
    "longitude": 3.3941795
  }
}

From there the run continued normally, called get_weather, and finished with a real answer. The full sequence, including the recovery, is logged in this Weave trace.

A structured error does more than avoid a crash. It becomes something the model itself can read and act on, which is why the shape of an error matters as much as whether one gets caught at all.

Add a Weave trace

To record the same run in Weave, run this command from the same working folder and activated terminal:

python openai_tool_calling_agent.py --mode run --weave-project wb-authors/tool-calling-agent-python --prompt "Should I carry an umbrella in Lagos tomorrow?"

The trace is useful because it preserves the sequence that matters: user prompt, model tool request, validated Python call, compact tool result, and final answer. I captured the output above from my own run, and the same run is logged in this Weave trace. The Weave tracing docs describe the same review pattern for logged model calls.

Screenshot by author. The trace shows the geocode_city tool call turning “Lagos” into country and coordinates before the weather lookup runs.
Screenshot by author. The annotations highlight the tool timeline, the validated get_weather input arguments, and the compact forecast payload used by the final answer.

Before you consider this first version finished, review the run output and the Weave trace. You should see the model request geocode_city, Python run the Nominatim lookup, the model request get_weather, Python run the Open-Meteo forecast call, and the model write an answer from the compact weather payload. That visibility is the baseline to preserve before adding more tools, frameworks, evaluations, or dashboards.

How the script maps to the agent loop

The script has six pieces.

First, geocode_city and get_weather are narrow tools that call real services. Nominatim turns a city into coordinates, and Open-Meteo turns those coordinates into a forecast. Nominatim also asks public clients to send a clear user agent string, which is why the script sets USER_AGENT.

Second, TOOLS describes those functions with JSON Schema. The schema is the contract the model sees. It says which function exists, what arguments it accepts, which fields are required, and whether extra fields are allowed.

Third, TOOL_REGISTRY and execute_tool_call keep execution inside your application. The model can request a tool, but Python decides whether the tool is known, whether the arguments match the schema, and what structured error to return when something is wrong.

Fourth, compact_tool_result removes fields the model does not need. Tool outputs are messages back to the model, not complete API dumps. Compact payloads make the answer cheaper to produce and easier to inspect later.

Fifth, run_agent keeps a bounded loop. It sends messages and tool schemas to the model, receives tool calls, executes the matching Python functions, appends tool results, and stops when the model returns a normal answer or the loop reaches max_turns.

Sixth, the OpenAIError handler turns model request failures into structured output, and a matching json.JSONDecodeError handler around the tool argument parsing does the same when the model’s own arguments are not valid JSON. Both keep server errors, connection failures, authentication mistakes, and malformed arguments visible to the caller instead of burying them in a traceback.

That is the basic loop most teams need to understand before adopting a larger framework. Frameworks are easier to evaluate after you have seen the raw message flow once.

Reliability starts where the loop is visible

Production tool calling agents fail at the edges. A model request can fail before a tool is chosen. Arguments arrive in the wrong format. A tool times out. A model picks the wrong function. A call repeats without adding information. The complete script handles the first guardrails directly: model request errors, schema validation, unknown tool errors, request timeouts, compact tool results, and a loop limit.

A useful preflight check is already built into --mode verify. It calls get_weather with only a city, even though the schema requires latitude, longitude, and city. The script returns a structured error instead of running a broken tool call. It also checks that an unknown tool name returns a structured error.

That small preflight path matters. It lets readers check the Python layer before they spend money on model calls, and it gives teams a place to add more checks later. The messy prompt adds the other side of the reliability story: live model calls can fail too, so the agent should make that failure visible.

Where this leaves the agent

You now have the basic tool calling agent pattern in Python: define narrow tools, describe them with schemas, let the model request them, execute only known functions, return compact results, handle model request failures, and keep the loop bounded.

The weather example is only one use case. The same loop can call a document search tool, a customer database, a pricing service, a test runner, or an internal workflow API.

Do one thing before you add more tools: run the agent with a prompt that should fail. Ask for an unsupported city. Break one argument. Return an oversized payload. Watch what the loop does.

That will tell you more than another clean, happy path.

The same instinct applies beyond tool calling. In a follow-up piece on debugging coding agents, I apply the same evidence-first approach to an agent that edits UI code, recording what it inspected, patched, and verified instead of trusting its own “fixed” summary. It held up on a completely different kind of model too: when I fine-tuned a robot learning model on a rented GPU, the useful record was the same kind, logged evidence of what actually ran, not a single reported number.

The useful lesson is bigger than weather. Tool calling starts as a loop you can inspect before it becomes an architecture decision. Once the loop is visible, a framework or MCP decision becomes easier: adopt one when it removes repeated routing, state, retries, tool packaging, or observability work, after you understand what it hides. The final answer is only one part of the run.

Selected Sources
OpenAI function calling and tools documentation: Used for the OpenAI tool schema and tool calling flow.
OpenAI Python SDK: Used for the Python client interface.
Model Context Protocol documentation: Used for the MCP comparison and tool boundary discussion.
Nominatim Search API documentation: Used for city geocoding.
Nominatim usage policy: Used for public geocoding service usage rules and the User-Agent note.
Open-Meteo Forecast API documentation: Used for weather forecast fields.
Weights & Biases Weave tracing documentation: Used for trace logging and review.
Ollama tool support documentation: Used for the local model tool calling comparison.
