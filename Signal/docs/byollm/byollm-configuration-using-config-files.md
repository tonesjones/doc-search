---
title: "BYOLLM configuration using Config Files"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/byollm-configuration-using-config-files.html"
content_id: "grdVX0rwt1f_SCmS2_9kFw"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.811263+00:00"
---

# BYOLLM configuration using Config Files

You can configure BYOLLM from the command line, from a `.signal` config file, or mix both. CLI flags take precedence over config-file values. For configuring through CLI flags, see BYOLLM configuration from the CLI.

**Contents**

- Overview
- General Settings
- GCP Vertex AI Settings
- AWS Bedrock Settings
- Per-Agent Overrides
- Environment Variables and Path Resolution
- Example configurations
  - Minimal BYOLLM
  - Azure OpenAI
  - GCP Vertex AI
  - AWS Bedrock

## Overview

Signal uses an **INI-format** configuration file (typically named `.signal`) to store LLM settings. The config file is organised into sections that map directly to the agent system:

|  |  |  |
| --- | --- | --- |
| Config Section | Maps To | Purpose |
| `[LLM]` | General defaults | Shared settings inherited by all seven agents |
| `[LLM_SINGLEFILESCAN_AGENT]` | singlefilescan-agent | Single-file vulnerability detection |
| `[LLM_DATAFLOW_AGENT]` | dataflow-agent | Cross-file dataflow tracing |
| `[LLM_OVERSIGHT_AGENT]` | oversight-agent | False-positive triage and review |
| `[LLM_EXPLOITATION_AGENT]` | exploitation-agent | Exploit summary generation |
| `[LLM_SCA_AGENT]` | sca-agent | Software composition analysis |
| `[LLM_MERGEKEY_EMBED_AGENT]` | mergekey-embed-agent | Merge-key embeddings |
| `[LLM_OVERSIGHT_EMBED_AGENT]` | oversight-embed-agent | Oversight-rule embeddings |

The `[LLM]` section acts as a **parent** — any setting you place there becomes the default for all seven agent sections. Per-agent sections only need to specify values that **differ** from the general defaults. This keeps configurations concise: if every agent shares the same endpoint and key, you set those once in `[LLM]` and only specify the model name in each agent section.

## General Settings

```
[LLM]
mode = byo 
uri = https://your-endpoint.example.com/v1 
key = ${OPENAI_API_KEY} 
timeout = 600
```

The `mode` field on `[LLM]` is the config-file equivalent of `--llm-mode`; you can set it here so users do not need to remember the flag. An explicit `--llm-mode` on the command line still wins.

## GCP Vertex AI Settings

When using GCP Vertex AI (native integration), add these fields to `[LLM]`:

```
[LLM]
mode = byo 
gcp_service_account_key = gcp-sa-key.json 
gcp_project = your-gcp-project-id 
gcp_region = us-central1
```

The relative path `gcp-sa-key.json` is resolved against the directory containing the `.signal` file at load time; the JSON key file can sit next to the config file and the resolution succeeds regardless of the current working directory when Signal is invoked.

When `gcp_service_account_key` is set, agents without a per-agent `uri` route to GCP Vertex AI. Agents with a per-agent `uri` route to the URI-based provider, enabling mixed configurations.

## AWS Bedrock Settings

When using AWS Bedrock (native integration), add these fields to `[LLM]`:

```
[LLM]
mode = byo 
aws_bearer_token = ${AWS_BEARER_TOKEN_BEDROCK} 
aws_bedrock_region = us-east-2
```

The `${AWS_BEARER_TOKEN_BEDROCK}` reference is expanded at load time; you can equivalently omit the line entirely and rely on the SDK-standard env var, which Signal's fallback path reads directly. The same pattern applies to `aws_bedrock_region` via `AWS_REGION`.

When `aws_bearer_token` is set, agents without a per-agent `uri` route to AWS Bedrock. Agents with a per-agent `uri` route to the URI-based provider. This cannot be combined with `gcp_service_account_key` — both providers use the same "no URI" detection mechanism, so the factory cannot determine which cloud provider an agent without a URI should use if both are configured. Signal exits with E118 at config-parse time if both are present.

## Per-Agent Overrides

Each of the seven agent sections accepts the same five fields: `model`, `uri`, `key`, `timeout`, `api_version`. The example below shows one, but the configuration is identical for all seven.

```
[LLM_SINGLEFILESCAN_AGENT] 
model = gpt-4o 
timeout = 600
                 
[LLM_DATAFLOW_AGENT] 
model = gpt-4o-mini
                 
[LLM_OVERSIGHT_AGENT] 
model = gpt-4o-mini
                 
[LLM_EXPLOITATION_AGENT] 
model = gpt-4o-mini  

[LLM_SCA_AGENT] 
model = gpt-4o-mini  

[LLM_MERGEKEY_EMBED_AGENT] 
model = text-embedding-3-large
                 
[LLM_OVERSIGHT_EMBED_AGENT] 
model = text-embedding-3-small
```

In byo mode, **every agent must have a** `model` **set** somewhere in its inheritance chain; no built-in defaults apply, even for the embedding agents. This is deliberate: the OpenAI-branded default embedding-model names (`text-embedding-3-large`, `text-embedding-3-small`) do not exist on Bedrock or Vertex, so a silent fall-through would surface as a mid-scan model-not-found (E112) instead of an upfront config-validation error (E117). Managed mode still applies those defaults; only byo mode requires the explicit choice.

## Environment Variables and Path Resolution

Two non-obvious behaviours apply to values you enter in the config file, in addition to the CLI-flag / env-var fallback chain covered elsewhere in this document.

**Environment-variable expansion in** `.signal`**.** Signal walks every BYOLLM field on `[LLM]` and every per-agent section and applies `os.path.expandvars` to expand `${VAR}` or `$VAR` references. This includes:

- `[LLM]`: `uri`, `key`, `timeout`, `api_version`, `gcp_service_account_key`, `gcp_project`, `gcp_region`, `aws_bearer_token`, `aws_bedrock_region`.
- Every `[LLM_<AGENT>_AGENT]` section: `uri`, `key`, `model`, `timeout`, `api_version`.

Every field listed above is expanded; URIs, model names, and GCP fields included. Unresolved references (env var not set at process start) are aggregated into a single E117 error listing every offending section/field/name so you can fix them all in one pass instead of one at a time. Shell-style defaults like `${VAR:-fallback}` are **not** supported; export the variable instead. Use `$$` if you need a literal `$` in the value.

```
[LLM]                
mode = byo 
uri = https://api.openai.com/v1 
key = ${OPENAI_API_KEY}                # expanded at load time  

[LLM] 
mode = byo
aws_bearer_token = ${AWS_BEARER_TOKEN_BEDROCK}   # equivalent to leaving it unset
                                                 # and exporting the env var; Signal 
                                                 # reads AWS_BEARER_TOKEN_BEDROCK 
                                                 # directly if the field is empty. 
aws_bedrock_region = us-east-2
```

**SDK env-var fallbacks (byo mode,** `[LLM]` **only).** After `${VAR}` expansion runs, Signal fills unset fields on `[LLM]` from well-known provider SDK env vars; but only in byo mode, and only on the general section (per-agent sections inherit through the normal precedence chain rather than picking up ambient env vars):

|  |  |
| --- | --- |
| `[LLM]` field | Env var (in order tried) |
| `uri` | `AZURE_OPENAI_ENDPOINT` |
| `key` (Azure hostname resolved) | `AZURE_OPENAI_API_KEY` |
| `api_version` (Azure hostname resolved) | `AZURE_OPENAI_API_VERSION` |
| `key` (non-Azure) | `OPENAI_API_KEY` |
| `gcp_service_account_key` | `GOOGLE_APPLICATION_CREDENTIALS` |
| `gcp_project` | `GOOGLE_CLOUD_PROJECT`, then `GCP_PROJECT` |
| `gcp_region` | `GOOGLE_CLOUD_REGION`, then `GCP_REGION` |
| `aws_bearer_token` | `AWS_BEARER_TOKEN_BEDROCK` |
| `aws_bedrock_region` | `AWS_REGION` |

The Azure fallbacks are gated on the resolved URI hostname actually matching an Azure suffix, so a generic OpenAI-compatible endpoint does not accidentally pick up an `AZURE_OPENAI_API_KEY` that happens to be exported.

**Relative** `gcp_service_account_key` **paths.** When `gcp_service_account_key` is a relative path, Signal resolves it against the directory of the config file, **not** the current working directory. So `gcp_service_account_key = gcp-sa-key.json` works when the JSON sits next to the `.signal` file, regardless of where you invoke `signal` from. Absolute paths and base64-encoded-JSON / raw-JSON values are passed through unchanged.

## Example configurations

**Minimal BYOLLM (single endpoint for all agents)**

The simplest configuration: every agent shares one endpoint and key. Only the model names differ.

```
[LLM]
mode = byo
uri = https://api.openai.com/v1
key = ${OPENAI_API_KEY}

[LLM_SINGLEFILESCAN_AGENT]
model = gpt-4o

[LLM_DATAFLOW_AGENT]
model = gpt-4o-mini

[LLM_OVERSIGHT_AGENT]
model = gpt-4o-mini

[LLM_EXPLOITATION_AGENT]
model = gpt-4o-mini

[LLM_SCA_AGENT]
model = gpt-4o-mini

[LLM_MERGEKEY_EMBED_AGENT]
model = text-embedding-3-large

[LLM_OVERSIGHT_EMBED_AGENT]
model = text-embedding-3-small
```

Byo mode requires an explicit model for every agent including both embedding agents. The ${OPENAI_API_KEY} reference is expanded at config-load time; export OPENAI_API_KEY in the shell that runs signal (or set the value directly in the file, though env-var interpolation keeps secrets out of source control).

**Azure OpenAI (all agents)**

Every agent points at Azure OpenAI. `api_version` is required at the `[LLM]` level so all seven agents pick it up through inheritance.

```
[LLM]
mode = byo
uri = https://your-resource.openai.azure.com/
key = ${AZURE_OPENAI_API_KEY}
api_version = 2025-01-01-preview

[LLM_SINGLEFILESCAN_AGENT]
model = o3-mini

[LLM_DATAFLOW_AGENT]
model = o3-mini

[LLM_OVERSIGHT_AGENT]
model = o3-mini

[LLM_EXPLOITATION_AGENT]
model = o3-mini

[LLM_SCA_AGENT]
model = o3-mini

[LLM_MERGEKEY_EMBED_AGENT]
model = text-embedding-3-large

[LLM_OVERSIGHT_EMBED_AGENT]
model = text-embedding-3-small
```

Azure deployment names are case-sensitive; `model = o3-mini` means Signal will send the request to the deployment literally named `o3-mini` on your resource, not to a model called `o3-mini`. Match the deployment name in the Azure portal exactly.

**GCP Vertex AI (all agents)**

No URI or API key needed; authentication is handled via the GCP service-account key. Signal generates and refreshes OAuth2 access tokens automatically.

```
[LLM]
mode = byo
gcp_service_account_key = gcp-sa-key.json
gcp_project = your-gcp-project-id
gcp_region = us-central1

[LLM_SINGLEFILESCAN_AGENT]
model = gemini-2.5-pro
timeout = 600

[LLM_DATAFLOW_AGENT]
model = gemini-2.5-flash
timeout = 600

[LLM_OVERSIGHT_AGENT]
model = gemini-2.5-flash
timeout = 600

[LLM_EXPLOITATION_AGENT]
model = gemini-2.5-flash
timeout = 600

[LLM_SCA_AGENT]
model = gemini-2.5-flash
timeout = 600

[LLM_MERGEKEY_EMBED_AGENT]
model = text-embedding-005

[LLM_OVERSIGHT_EMBED_AGENT]
model = text-embedding-005
```

Vertex AI model names use the bare form without any `google/` publisher prefix; the native SDK handles the resolution internally. The `gcp-sa-key.json` path is relative to the directory of the `.signal` file at load time.

**AWS Bedrock (all agents)**

No URI or API key needed; authentication is handled via the IAM service-specific credential (Bearer token). The chat wrappers speak to Bedrock's `/model/{id}/invoke` endpoint directly using `httpx` with `Authorization: Bearer
<token>`; no boto3 or SigV4 is involved.

```
[LLM]
mode = byo
aws_bearer_token = ${AWS_BEARER_TOKEN_BEDROCK}
aws_bedrock_region = us-east-2

[LLM_SINGLEFILESCAN_AGENT]
model = us.anthropic.claude-sonnet-4-20250514-v1:0
timeout = 600

[LLM_DATAFLOW_AGENT]
model = us.anthropic.claude-3-5-haiku-20241022-v1:0
timeout = 600

[LLM_OVERSIGHT_AGENT]
model = us.anthropic.claude-3-5-haiku-20241022-v1:0
timeout = 600

[LLM_EXPLOITATION_AGENT]
model = us.anthropic.claude-3-5-haiku-20241022-v1:0
timeout = 600

[LLM_SCA_AGENT]
model = us.anthropic.claude-3-5-haiku-20241022-v1:0
timeout = 600

[LLM_MERGEKEY_EMBED_AGENT]
model = amazon.titan-embed-text-v2:0

[LLM_OVERSIGHT_EMBED_AGENT]
model = amazon.titan-embed-text-v2:0
```

Bedrock model IDs include the full inference profile (e.g. the `us.` prefix for the US regional profile). Get the ID from the Bedrock console under **Model access**; a wrong model ID surfaces as a 404 from the Bedrock endpoint and is classified as E112 by Signal.
