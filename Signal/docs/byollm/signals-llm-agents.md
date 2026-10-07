---
title: "Signal's LLM Agents"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-s-llm-agents.html"
content_id: "OuG~YeoACrFy1KVAN_MfRw"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.710506+00:00"
---

# Signal's LLM Agents

Describes Signal's seven LLM agents, their roles in the analysis pipeline, and guidance for selecting models in a BYOLLM configuration.

**Contents**

- Overview
- Quick reference
- Recommended models for each agent
- Mixed Provider Configurations

## Overview

Signal uses 7 distinct LLM agents, splitting the LLM traffic into 5 **chat agents** (which consume a `BaseChatModel` client at runtime) and 2 **embedding agents** (which consume an `Embeddings` client). Every agent has its own precedence chain, so any agent can be overridden without affecting the others.

Since each agent serves a specific purpose in the analysis pipeline, they have very different performance characteristics — which is why you may want to assign different models, providers, or timeouts to each one.

Table 1.

| Agent | Purpose | Typical Workload |
| --- | --- | --- |
| **singlefilescan-agent** | Single-file vulnerability detection; the primary security-analysis pass. Runs once per source file in the scan target. | Highest per-call token spend in the pipeline. Use your most capable reasoning model here. |
| **dataflow-agent** | Cross-file dataflow tracing; walks control flow through function calls, module boundaries, and class hierarchies. | Many small calls per target. Latency compounds because the agent chains decisions; use a fast reasoning model. |
| **oversight-agent** | False-positive triage and second-pass review. Runs both the initial triage prompt and the follow-up review prompt through one client. | Lower per-target volume than dataflow, but every finding runs through it before it reaches the SARIF report. |
| **exploitation-agent** | Exploit summaries and attack-chain narrative. Runs per-finding to produce the human-readable exploitation description. Note: The `exploitation-agent` is not supported when running Signal through Bridge or Polaris. It is available only when invoking Signal directly from the CLI. | Similar to dataflow and oversight; typically shares their model choice. |
| **sca-agent** | Software composition analysis; supervisor and sub-agents for dependency and CVE reasoning. | Volume depends on the dependency graph. Requires reliable tool-calling; a solid mid-tier model handles this well. |
| **mergekey-embed-agent** | Vector embeddings for **merge keys**; the mechanism that links a finding across successive scans so it stays trackable when files are renamed or line numbers shift. Note: The `mergekey-embed-agent` is not supported when running Signal through Bridge or Polaris. It is available only when invoking Signal directly from the CLI. | Embedding calls only. Requires an embedding model such as `text-embedding-3-large`, `text-embedding-005` (GCP), or `amazon.titan-embed-text-v2:0` (Bedrock). |
| **oversight-embed-agent** | Vector embeddings for **oversight-rule text**; matches findings against the built-in vulnerability classification rules via cosine similarity. | Embedding calls only. Can safely use a cheaper embedding model than mergekey-embed since the strings are shorter and the accuracy bar is lower. |

## Quick reference

The table below shows the recommended default model and the key capability requirement for each agent. For a full explanation of what each requirement means and how to diagnose failures, see Agent Capability Requirements.

Table 2.

| Agent | Purpose | Recommended default | Key requirement |
| --- | --- | --- | --- |
| `singlefilescan-agent` | Per-file vulnerability detection | `claude-sonnet-4-6` | Frontier reasoning; large context window |
| `dataflow-agent` | Cross-file taint tracing via ReAct and file tools | `o3-mini` | Native tool-calling; strict structured output |
| `oversight-agent` | False-positive triage and rule review | `o3-mini` | Native tool-calling; strict structured output |
| `exploitation-agent` | Executive summary, zero-day list and attack chain | `o3-mini` | Long-context reasoning; strict structured output |
| `sca-agent` | Python SCA (supervisor + audit + KB sub-agents) | `gpt-4o` | Native tool-calling; JSON tool arguments |
| `mergekey-embed-agent` | Finding-linking embeddings | `text-embedding-3-large` | ≥ 1024-dim embedding; stable across runs |
| `oversight-embed-agent` | Rule-taxonomy cosine matching | `text-embedding-3-small` | ≥ 512-dim embedding model |

## Recommended models for each agent

**Your most capable reasoning model — singlefilescan-agent**

The `singlefilescan-agent` is the primary vulnerability-detection engine: every source file in the scan target is analysed once through this client. Its dominant cost concern is reasoning depth; a model that misses subtle injection paths or skips entire control flows produces false negatives, and false negatives in security analysis are the most expensive kind of error because they are invisible.

- **Recommended models:** Claude Sonnet 4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, `o3-mini`.
- **Deviation case:** On small targets where total LLM spend is already low, a smaller model keeps iteration fast during config tuning — but switch back to a top-tier model before relying on the results.
- **Symptom of under-provisioning:** Findings volume drops without a corresponding decrease in target complexity, or `--check-llm` passes but real scans return suspiciously empty result sets.

Table 3. singlefilescan-agent: recommended models by provider

| Provider | Recommended |
| --- | --- |
| OpenAI | `gpt-4o`, `gpt-4.1` |
| Anthropic direct | `claude-sonnet-4-6`, `claude-opus-4-6` |
| Azure OpenAI | `gpt-4o` or `gpt-4.1` deployments |
| Azure AI Anthropic | `claude-sonnet-4-6` |
| AWS Bedrock Anthropic | `anthropic.claude-sonnet-4-6`, `anthropic.claude-opus-4-6` |
| GCP Vertex Gemini | `gemini-2.5-pro` |

**Smaller reasoning models — dataflow, oversight, and exploitation agents**

These three agents run after the singlefilescan pass, mostly per-finding, and consume far fewer tokens per call. Latency matters more here than peak reasoning depth; every agent makes many small decisions in series, and a slow model multiplies wait time.

- **Recommended models:** Claude Sonnet 4, Gemini 2.5 Pro, `o3-mini`, `o4-mini`, `o3`, `o1`.
- **Deviation case:** If your codebase pushes oversight or dataflow into territory a smaller model handles poorly (deeply nested call graphs, large polyglot dataflow), you can run the same model as your singlefilescan-agent across all three. The cost premium is bounded because their combined volume is a fraction of singlefilescan.
- **Symptom of under-provisioning:** Oversight false-positive rate climbs, dataflow agent gives up early or loops without converging, exploitation summaries read as generic boilerplate.

Table 4. dataflow, oversight, and exploitation agents: recommended models by provider

| Provider | Recommended |
| --- | --- |
| OpenAI | `o3-mini`, `o4-mini`, `o3`, `o1` |
| Anthropic direct | `claude-sonnet-4-6`, `claude-opus-4-6` |
| Azure OpenAI | `o3-mini`, `gpt-4o` deployments |
| Azure AI Anthropic | `claude-sonnet-4-6` |
| AWS Bedrock Anthropic | `anthropic.claude-sonnet-4-6`, `anthropic.claude-opus-4-6` |
| GCP Vertex Gemini | `gemini-2.5-pro` |

**Midrange reasoning model — sca-agent**

The `sca-agent` uses a supervisor pattern where the model's job is dispatch — delegating to a pip-audit sub-agent and a knowledge-base sub-agent — rather than deep analysis. Frontier reasoning is not required here; a reliable mid-tier model with real tool-calling handles it well.

- **Recommended models:** GPT-4o, GPT-4.1, Claude Sonnet 4, Gemini 2.5 Pro or Flash.
- **Symptom of under-provisioning:** The supervisor stops delegating (produces plain text output instead of tool calls); pip-audit is not invoked.

Table 5. sca-agent: recommended models by provider

| Provider | Recommended |
| --- | --- |
| OpenAI | `gpt-4o`, `gpt-4.1` |
| Anthropic direct | `claude-sonnet-4-6` |
| Azure OpenAI | `gpt-4o` deployment |
| Azure AI Anthropic | `claude-sonnet-4-6` |
| AWS Bedrock Anthropic | `anthropic.claude-sonnet-4-6` |
| GCP Vertex Gemini | `gemini-2.5-pro`, `gemini-2.5-flash` acceptable |

**The embedding agents**

The `mergekey-embed-agent` and `oversight-embed-agent` produce vector embeddings, not text completions — the model lists are completely separate from the chat agents. Both benefit from high-dimensional embeddings (better semantic separation), but `mergekey-embed-agent` in particular needs embeddings **stable across runs**: merge keys link findings between successive scans, so switching embedding models mid-project causes findings to appear new even when the underlying issue has not changed.

- **Recommended models:** `text-embedding-3-large` / `text-embedding-3-small` (OpenAI-compatible), `text-embedding-005` (GCP Vertex), `amazon.titan-embed-text-v2:0` (Bedrock).
- **Deviation case:** The oversight-embed agent operates on shorter strings (classification rules) than mergekey-embed does (finding summaries), so a cheaper embedding model is acceptable for oversight-embed without meaningfully affecting accuracy. Signal's managed-mode defaults already split them this way.
- **Symptom of under-provisioning:** Merge keys churn between scans (existing findings appear as new ones), or oversight classification accuracy drops sharply on borderline rules.

Table 6. Embedding agents: recommended models by provider

| Provider | Recommended (mergekey-embed / oversight-embed) |
| --- | --- |
| OpenAI | `text-embedding-3-large` / `text-embedding-3-small` |
| Azure OpenAI | `text-embedding-3-large` deployment |
| AWS Bedrock | `amazon.titan-embed-text-v2:0`, `cohere.embed-multilingual-v3` |
| GCP Vertex | `text-embedding-005`, `gemini-embedding-001` |

## Mixed Provider Configurations

Signal supports mixing different providers within the same scan, enabling different providers and models to be used for different agents. Each agent serves a specific purpose in the analysis pipeline, and they have very different performance characteristics — which is why enabling models from different providers can have many benefits, including:

- **Cost optimisation:** The `singlefilescan-agent` processes every source file and dominates LLM spend. You might use a cost-effective model on one provider for singlefilescan while using a premium model on another provider for the four lighter chat agents where reasoning quality matters most, or vice versa.
- **Capability matching:** Embedding models and chat models have different strengths. OpenAI's `text-embedding-3-large` may outperform alternatives for embeddings, while Anthropic Claude or Google Gemini may be preferred for code analysis.
- **Infrastructure constraints:** Your organisation may have separate contracts, quotas, or network paths for different cloud providers.
- **Gradual migration:** When moving from one provider to another, you can switch one agent at a time and validate results before completing the transition.
