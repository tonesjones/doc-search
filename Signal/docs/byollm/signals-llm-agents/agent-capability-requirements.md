---
title: "Agent Capability Requirements"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/agent-capability-requirements.html"
content_id: "Km58~tIfMxAVPGSsIikLig"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.734146+00:00"
---

# Agent Capability Requirements

Describes the structured-output, tool-calling, and context-window requirements each Signal agent places on its configured model, with failure symptoms and provider-specific notes to help you diagnose scan issues.

**Contents**

- Capability vocabulary
- Per-agent requirements and failure modes
- Provider-specific notes
- Models not recommended for Signal agents

## Capability vocabulary

The per-agent requirements below reference four capability axes. If you are evaluating a model that is not listed in the Recommended models, check it against these first.

**Structured-output mode**

How the response schema is enforced on the wire:

- **OpenAI JSON object mode**. The request instructs the model to produce a JSON object, but the shape is not validated server-side. The most permissive mode; most OpenAI-compatible servers honor it. Signal uses this mode for the `singlefilescan-agent`.
- **OpenAI JSON schema mode**. The request includes the full expected schema and the server validates output against it. Reliable on OpenAI (o-series, `gpt-4o`), Azure OpenAI, and a subset of high-end hosted gateways. **Silently ignored** by most local inference servers (Ollama, llama.cpp, vLLM) — the model generates freely and often wraps output in markdown code fences, which Signal's parser rejects immediately.
- **Anthropic tool-use (function calling)**. The schema is bound as a synthetic tool and the model is forced to "call" it. Signal automatically routes Claude models. Reliable on Anthropic direct, Azure AI Services Anthropic, and AWS Bedrock Anthropic.
- **Dense vector**. Embeddings only. The sole requirement is fixed-dimension output.

**Reasoning tier**

- **Frontier**: GPT-4o / o-series, Claude Sonnet 4.x / Opus 4.x, Gemini 2.5 Pro. Reliable on multi-step reasoning under a schema constraint.
- **Midrange**: GPT-4o-mini, Claude Haiku 4.x, Gemini 2.5 Flash. Suitable for tool-orchestration agents where the model's job is dispatch rather than deep analysis.
- **Small**: Any model roughly 13 B parameters or smaller, including typical 4–8 B-class open models. Not recommended for any Signal agent that enforces structured output; see Models not recommended for Signal agents.

**Tool-calling**

Required for the `dataflow-agent`, `oversight-agent` (via schema-as-tool binding), `exploitation-agent`, and `sca-agent`. The model must implement OpenAI-compatible `tools` / `tool_calls` or Anthropic tool-use natively. This is not the same as "can produce JSON": a model can be a reliable JSON generator and still fail to handle tool calls correctly. Many local models fall in exactly that gap.

**Context window**

A context window of 128k tokens or larger is recommended for the `singlefilescan-agent`, `dataflow-agent`, and `exploitation-agent`. The singlefilescan agent sends entire source files; the dataflow agent accumulates tool-call history across multiple steps; the exploitation agent receives the top findings with their full source context. A minimum of 32k tokens is a hard floor for any agent.

## Per-agent requirements and failure modes

**singlefilescan-agent**

Uses JSON object mode, the most forgiving structured-output method Signal employs. Tool-calling is not required; each invocation is a single-shot prompt. Runs once per source file, so it dominates total LLM spend on large repositories.

**Failure symptoms with underpowered models:** Even midrange models generally return parseable output for this agent, but classification quality degrades visibly — missed vulnerability classes, incorrect rule IDs, inaccurate line ranges. If you notice degraded output quality without errors, upgrade the tier before investigating other agents.

**dataflow-agent**

Uses JSON schema mode with tool-calling. The agent iteratively calls file-inspection tools to trace taint flows across files, then produces a structured finding result. Signal automatically uses the tool-use (function-calling) path for Claude models; JSON schema mode for all others. Runs concurrently across findings, bounded by the `--agent-limit` setting (default 10).

**Failure symptoms:** All three are logged as `FAIL dataflow/<file> (guid=…) after 5 attempts`:

- **Validation Error**. The model returns markdown-fenced output (for example, ```` ```json … ``` ````) instead of a raw JSON object. Root cause: the model or local gateway silently ignored the JSON schema requirement. Retries will not help; switch to a model with reliable structured output.
- **Silent tool-call failures**. The model emits tool calls in an unexpected format; they are dropped silently, and the agent loop stalls. Look for empty AI messages in the debug output.
- **Schema mismatch**. The model returns valid JSON with the wrong shape: missing fields, wrong value types, or incorrect field names. Almost always means the model is too small for the schema complexity. Upgrade to a frontier-tier model.

**oversight-agent**

Runs two prompts through one client: a triage pass that re-labels obvious false positives, and a review pass that optionally augments the model with the top-3 cosine-similar rules from the built-in rule taxonomy (when `oversight_embedding_enabled=true`). Uses the same structured-output and tool-calling requirements as the dataflow agent.

**Failure symptoms:** Same as dataflow. Additionally: if the oversight pass is not re-labeling any findings as false positives, the model may be consistently agreeing with initial scan labels regardless of evidence — a behavior failure rather than a hard error. This is common with midrange models on complex codebases. Upgrade the tier.

**exploitation-agent**

Single-shot prompt against a large input — the top scan findings, each with source context. Only runs when `--summary` is enabled. Uses JSON schema mode / tool-use; tool-calling is not required. Context window matters more here than for the other chat agents because the full finding set is sent in one prompt.

Note: The `exploitation-agent` is not supported when running Signal through Bridge or Polaris. It is available only when invoking Signal directly from the CLI.

**Failure symptoms:** Truncated summaries (context window too small for the input); flat, non-specific attack chains (model cannot reason across multiple findings); hallucinated CVE numbers.

**sca-agent**

LangGraph supervisor pattern: the main agent delegates to a pip-audit sub-agent and a knowledge-base sub-agent. Tool-calling is the agent's primary mechanism — its job is dispatch, not deep analysis, so a reliable mid-tier model with real function-calling is sufficient. Runs independently of the SAST pipeline alongside other agents.

**Failure symptoms:** The supervisor stops delegating (single-model text output instead of tool calls); pip-audit invocation missing from the agent trace. Both indicate the model is not handling tool dispatch correctly.

**mergekey-embed-agent**

Produces dense vector embeddings for finding text so that Signal can link findings across successive scans by cosine similarity. Any embedding model with ≥ 1 024 dimensions works. Dimension is not enforced by Signal itself — but switching embedding models mid-project invalidates the finding-linking index, causing existing findings to appear new every scan even when the underlying issue has not changed. Do not change the embedding model once a project is in active use.

Note: The `mergekey-embed-agent` is not supported when running Signal through Bridge or Polaris. It is available only when invoking Signal directly from the CLI.

**oversight-embed-agent**

Embeds the built-in rule taxonomy and finding descriptions for cosine-similarity matching, then feeds the top-3 matches to the oversight review prompt. Only active when `oversight_embedding_enabled=true`. A smaller, cheaper embedding model is acceptable here (default is `text-embedding-3-small`) because the rule taxonomy strings are short and the top-3 selection is not sensitive to embedding quality above a baseline.

## Provider-specific notes

- **AWS Bedrock (Anthropic).** Signal enables prompt caching by default (`llm_prompt_caching=true`). Cache-write incurs a small premium on the first request; every subsequent request within the cache TTL bills at approximately 10% of the base rate. This is a free performance and cost win — do not disable it unless you have a specific reason to.
- **Azure AI Services Anthropic** (`*.cognitiveservices.azure.com`, `*.services.ai.azure.com` with a Claude model). The Azure proxy rejects "assistant message prefill" — a technique some prompt patterns use. Signal automatically works around this restriction; no operator action is needed. If you see HTTP 400 errors stating "conversation must end with user role," your version of Signal predates this fix; upgrade to the current release.
- **Azure OpenAI** (`*.openai.azure.com`). An explicit `api_version` value is required in your configuration (for example, `2024-12-01-preview`). A missing `api_version` raises `SIGNAL-E117` at startup. This applies only to the Azure OpenAI endpoint; Azure AI Services routes through the Anthropic path and ignores `api_version`.
- **OpenAI o-series** (`o1`, `o3`, `o4` and prefixed variants). These models reject the `temperature` parameter with HTTP 400. Signal handles this automatically; no operator action is needed.
- **GCP Vertex Gemini.** Uses the native Vertex API, not an OpenAI-compatible endpoint. Requires `gcp_project`, `gcp_region`, and a service-account key in your configuration. Structured output uses Vertex's own JSON mode, which behaves similarly to JSON schema mode in its strictness.
- **Local OpenAI-compatible gateways** (Ollama, llama.cpp, vLLM, LM Studio). These servers typically accept any `response_format` field and silently ignore anything they do not understand. See Models not recommended for Signal agents.

## Models not recommended for Signal agents

Small local models — such as Gemma 2/3/4, Llama-3-8B, Mistral-7B, and similarly-sized quantized models served through Ollama, llama.cpp, vLLM, or LM Studio — are not supported for Signal's ReAct agents (`dataflow-agent`, `oversight-agent`, `exploitation-agent`, `sca-agent`).

These models fail every structured-output requirement that the dataflow and oversight agents enforce:

1. They do not honor the JSON schema requirement — the local server forwards the request, but the model does not understand it and generates freely, often wrapped in markdown code fences that Signal's parser immediately rejects.
2. Their tool-calling implementations are typically incomplete — tool calls come out malformed or as free-form text, causing the agent loop to stall without converging.
3. Their context windows are too small for real dataflow traces, which accumulate tool-call history across multiple steps and can grow large on non-trivial codebases.

**What might work:** pointing only the `singlefilescan-agent` at a small local model (using `--llm-singlefilescan-agent-model`) is sometimes viable, because that agent uses the more forgiving JSON object mode. However, you lose all cross-file verification, all false-positive triage, and the executive summary — a significant reduction in scan capability.

**If you must experiment with local models:** configure only the `singlefilescan-agent` to use the local model and keep a frontier model on every other agent. Signal's per-agent configuration surface makes this straightforward — see BYOLLM configuration from the CLI. Treat any findings that do not survive frontier-model dataflow verification as first-pass triage only, not as production results.
