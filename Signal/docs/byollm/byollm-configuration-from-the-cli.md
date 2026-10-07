---
title: "BYOLLM configuration from the CLI"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/byollm-configuration-from-the-cli.html"
content_id: "oY1M8GQfpRz2bPXRNVTiKQ"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.777217+00:00"
---

# BYOLLM configuration from the CLI

You can configure BYOLLM from the command line, from a `.signal` config file, or mix both. CLI flags take precedence over config-file values. For configuring through a config file, see BYOLLM configuration using Config Files.

**Contents**

- Provider Selection
- General LLM Settings
- GCP Vertex AI Settings
- AWS Bedrock Settings
- Per-Agent Settings (BYOLLM only)
- TLS Settings
- Preflight Validation
- CLI Invocation Examples
  - Minimal BYOLLM
  - Azure OpenAI
  - GCP Vertex AI
  - AWS Bedrock
  - GCP for singlefilescan + LiteLLM for the rest

## Provider Selection

The `--llm-mode` flag (Type `managed|byo`), is the LLM operating mode and has `managed` as a default. `managed` uses Black Duck's hosted endpoints. `byo` activates the per-agent flag surface (`--llm-<agent>-*`) and suppresses the managed default URI so a missing configuration fails E117 at parse time instead of silently routing customer traffic to the managed gateway. Can also be set as `[LLM]
mode` in the config file.

Passing any per-agent flag (`--llm-<agent>-*`) alongside `--llm-mode managed` is a hard error. If that happens, Signal exits with code 2 and prints which flag was rejected. This prevents a scan customer from accidentally sending customer traffic through the managed gateway while thinking they had switched to their own endpoint.

## General LLM Settings

These flags set defaults that apply to **all agents** unless overridden by a per-agent flag. This is convenient when every agent shares the same endpoint; you only need to specify the URI and key once.

|  |  |  |  |
| --- | --- | --- | --- |
| Flag | Type | Default | Description |
| `--llm-uri` | `str` | `https://llm.core.blackduck.com/` | Default LLM endpoint URI for all agents. In `byo` mode the managed default is **only** used when you pass `--llm-uri` explicitly on the command line; otherwise agents without a URI either fall through to the cloud provider (GCP/Bedrock) or surface a validation error. This suppression is the safety net that prevents byo customer traffic from silently reaching the managed gateway when a URI is missing. |
| `--llm-key` | `str` | `None` | Default LLM API key for all agents. In byo mode with URI-based endpoints, falls back to the `OPENAI_API_KEY` env var when neither this flag nor `[LLM] key` is set. Env-var interpolation (`${VAR}`) applies to the config-file value. |
| `--llm-api-version` | `str` | `None` | Default Azure API version for all agents. **Required** for Azure OpenAI endpoints (`*.openai.azure.com`). Also accepted for Azure AI Services endpoints (`*.cognitiveservices.azure.com` or `*.services.ai.azure.com`) but not required when the model is Claude / Anthropic (which uses the Anthropic native API). Ignored for non-Azure endpoints. Example: `2024-12-01-preview`. |
| `--llm-timeout` | `int` | `300` | Default timeout in seconds for all LLM requests. Per-agent timeouts (`--llm-<agent>-timeout`) override this. |
| `--model-completion-limit` | `int` | Model-specific (16384 when Signal does not know the model). | Maximum completion tokens per LLM response for the `singlefilescan` agent. Override when you use a model whose token limit is not in Signal's built-in table; Signal prints a warning when this happens. |

## GCP Vertex AI Settings

These are global; no per-agent variant; and are how you tell Signal to route agents to Vertex AI natively. When `gcp_service_account_key` is set, agents **without** a per-agent `uri` will use GCP Vertex AI. Agents **with** a per-agent `uri` will use the URI-based provider (Azure OpenAI, Azure AI Services, or standard OpenAI-compatible), enabling mixed provider configurations.

|  |  |  |  |
| --- | --- | --- | --- |
| Flag | Type | Default | Description |
| `--gcp-service-account-key` | `str` | `None` | Path to a GCP service-account JSON key file, base64-encoded key string, or raw JSON string. Relative paths are resolved against the directory of the `.signal` file at load time; a value like `gcp-sa-key.json` works when the JSON sits next to the config file, regardless of where you invoke Signal from. |
| `--gcp-project` | `str` | `None` | GCP project ID. **Required when using GCP Vertex AI**; missing project surfaces E118 at config-parse time. Falls back to the `GOOGLE_CLOUD_PROJECT` or `GCP_PROJECT` env var when set on `[LLM]` in byo mode. |
| `--gcp-region` | `str` | `None` | GCP region (e.g., `us-central1`). **Required when using GCP Vertex AI**; missing region surfaces E118. Falls back to `GOOGLE_CLOUD_REGION` or `GCP_REGION`. |

## AWS Bedrock Settings

These are global; no per-agent variant; and are how you tell Signal to route agents to Bedrock natively. When either `aws_bearer_token` or `aws_bedrock_region` is set, agents **without** a per-agent `uri` will use AWS Bedrock. Agents **with** a per-agent `uri` will use the URI-based provider.

|  |  |  |  |
| --- | --- | --- | --- |
| Flag | Type | Default | Description |
| `--aws-bearer-token` | `str` | `None` | AWS Bedrock Bearer token (IAM service-specific credential secret). Also via `AWS_BEARER_TOKEN_BEDROCK` env var. IAM service-specific credentials have a maximum lifetime of 30 days; rotate before expiry. |
| `--aws-bedrock-region` | `str` | `None` (factory falls back to `us-east-1`) | AWS region for Bedrock endpoints (e.g., `us-east-2`). Also via `AWS_REGION` env var. If neither `--aws-bedrock-region` nor `AWS_REGION` is set, the Bedrock client falls back to `us-east-1` inside the factory; Typer does not supply this default at the CLI layer, so the empty cell on the CLI does not mean "no region is used," it means "the factory will pick one." |

## Per-Agent Settings (BYOLLM only)

Each of the seven agents can override the general settings with its own URI, key, model, timeout, and Azure API version. This is how you configure different providers or models for different parts of the analysis pipeline.

The mental model worth holding before reading the seven per-agent tables: **most customers only override** `model`. The `[LLM]` section sets the URI, key, and timeout once; each agent section just names a different model.

**Use Cases**

You would reach for the other per-agent overrides in three specific situations, and recognising which situation you are in tells you which override to use:

1. **Different providers per agent** — override `uri` and `key` on the agent that should target a different endpoint. The presence of a per-agent `uri` is the switch that takes an agent off the global cloud-native path (GCP / Bedrock) and onto a URI-based path (Azure / LiteLLM / direct OpenAI). This is the entire mechanism behind *Mixed Provider Configurations*.
2. **singlefilescan is slow on a particular model** — override `timeout` per agent. The default of 300 s is fine for most chat models, but reasoning-heavy models (o3, Claude Sonnet on long inputs) routinely take 4–10 minutes per request when analysing a complex file. Set `[LLM_SINGLEFILESCAN_AGENT] timeout = 600` (or higher) if you see timeouts only on that agent. This is the most common operational dial customers reach for after their first scan.
3. **Different Azure API versions per agent** — override `api-version` per agent. Rare, but happens when one Azure deployment has been upgraded ahead of another, or when one model on Azure requires a newer API version than the rest of your config can use.

Every per-agent flag table follows the same shape: `model`, `uri`, `key`, `timeout`, and `api-version` (Azure only). Anything you omit falls back through the inheritance chain described in the Inheritance / Fallback Logic section.

Rather than repeating the same table verbatim seven times, the flags and defaults are identical across the seven agents; only the `<agent>` name in the flag prefix and the section header differs. The generalised shape is:

|  |  |  |  |
| --- | --- | --- | --- |
| Flag | Type | Default (byo) | Notes |
| `--llm-<agent>-model` | `str` | none | **Required in byo mode**; a missing model surfaces E117 at config-parse time. Rejected under `--llm-mode managed`. |
| `--llm-<agent>-uri` | `str` | falls back to `--llm-uri` | Setting a per-agent URI takes that agent off the global cloud-native path (GCP / Bedrock) and onto whichever URI-based provider matches the hostname. Rejected under `--llm-mode managed`. |
| `--llm-<agent>-key` | `str` | falls back to `--llm-key` (which itself falls back to `OPENAI_API_KEY`) | Env-var interpolation (`${VAR}`) applies on config-file values. Rejected under `--llm-mode managed`. |
| `--llm-<agent>-timeout` | `int` | falls back to `--llm-timeout` (default 300) | Rejected under `--llm-mode managed`. |
| `--llm-<agent>-api-version` | `str` | falls back to `--llm-api-version` | Only used when the agent's endpoint is Azure. Rejected under `--llm-mode managed`. |

Substitute `<agent>` with any of: `singlefilescan-agent`, `dataflow-agent`, `oversight-agent`, `exploitation-agent`, `sca-agent`, `mergekey-embed-agent`, `oversight-embed-agent`. That gives 35 per-agent flags in total (5 slots × 7 agents).

For clarity, the specific flag names for each agent are:

- **singlefilescan-agent** — `--llm-singlefilescan-agent-model`, `--llm-singlefilescan-agent-uri`, `--llm-singlefilescan-agent-key`, `--llm-singlefilescan-agent-timeout`, `--llm-singlefilescan-agent-api-version`
- **dataflow-agent** — `--llm-dataflow-agent-model`, `--llm-dataflow-agent-uri`, `--llm-dataflow-agent-key`, `--llm-dataflow-agent-timeout`, `--llm-dataflow-agent-api-version`
- **oversight-agent** — `--llm-oversight-agent-model`, `--llm-oversight-agent-uri`, `--llm-oversight-agent-key`, `--llm-oversight-agent-timeout`, `--llm-oversight-agent-api-version`
- **exploitation-agent** — `--llm-exploitation-agent-model`, `--llm-exploitation-agent-uri`, `--llm-exploitation-agent-key`, `--llm-exploitation-agent-timeout`, `--llm-exploitation-agent-api-version`
- **sca-agent** — `--llm-sca-agent-model`, `--llm-sca-agent-uri`, `--llm-sca-agent-key`, `--llm-sca-agent-timeout`, `--llm-sca-agent-api-version`
- **mergekey-embed-agent** — `--llm-mergekey-embed-agent-model`, `--llm-mergekey-embed-agent-uri`, `--llm-mergekey-embed-agent-key`, `--llm-mergekey-embed-agent-timeout`, `--llm-mergekey-embed-agent-api-version`
- **oversight-embed-agent** — `--llm-oversight-embed-agent-model`, `--llm-oversight-embed-agent-uri`, `--llm-oversight-embed-agent-key`, `--llm-oversight-embed-agent-timeout`, `--llm-oversight-embed-agent-api-version`

## TLS Settings

These settings control how Signal verifies TLS certificates when connecting to LLM endpoints. You may need to adjust them if your endpoints use self-signed certificates or a private CA. Applies to every agent; Signal reuses one httpx client bundle across the seven agents.

|  |  |  |  |
| --- | --- | --- | --- |
| Flag | Type | Default | Description |
| `--llm-ssl-verify` | `True|False` | `True` | Enable TLS certificate verification. Set to `False` for self-signed certificates. Signal logs a warning whenever verification is disabled; it is meant for on-prem endpoints, not production public endpoints. |
| `--llm-ca-bundle` | `str` | `None` | Path to a CA bundle PEM file for custom TLS verification. Used instead of the system CA store when set. |

## Preflight Validation

Before running a full scan, you can verify that all configured LLM endpoints are reachable and authenticated. This is especially useful when setting up BYOLLM for the first time or after rotating credentials.

|  |  |  |  |
| --- | --- | --- | --- |
| Flag | Type | Default | Description |
| `--check-llm` | `True|False` | `False` | Validate all LLM endpoints and exit. Runs a minimal probe against every configured agent's endpoint (1 chat completion for chat agents, one `embed_query` for embedding agents), reports the result per agent, and exits with code 0 if every configured agent passed or was skipped, or code 1 if any failed. |
| `--check-llm-json` | `True|False` | `False` | Emit preflight results as a single JSON document on stdout instead of the Rich-table. Implies `--check-llm True`. |

## CLI Invocation Examples

You can drive BYOLLM entirely from the command line; useful for CI/CD pipelines where you would rather not check a config file in, or for quick one-off scans. Every flag mirrors a config-file field one-to-one; see the CLI Flags section for the full reference.

Conventions:

- `<target>` is the directory you want to scan (the same positional argument you would pass without BYO LLM).
- `\` line continuations are for readability; paste the whole command on one line if you prefer.
- Replace placeholder credentials (`sk-...`, `${AZURE_OPENAI_API_KEY}`, etc.) with your real values. **Never commit real keys to source control.**
- The CLI flags below assume Signal is on your `PATH` as `signal`; substitute your local invocation if different.

**Minimal BYOLLM (single endpoint, all agents)**

```
signal <target> \   
--llm-mode byo \   
--llm-uri https://api.openai.com/v1 \   
--llm-key "$OPENAI_API_KEY" \
--llm-singlefilescan-agent-model gpt-4o \
--llm-dataflow-agent-model gpt-4o-mini \
--llm-oversight-agent-model gpt-4o-mini \
--llm-exploitation-agent-model gpt-4o-mini \ 
--llm-sca-agent-model gpt-4o-mini \   
--llm-mergekey-embed-agent-model text-embedding-3-large \   
--llm-oversight-embed-agent-model text-embedding-3-small
```

Every agent must be given a model in byo mode; there are no defaults, even for the embedding agents. That is verbose on the CLI; this is one of the two main reasons customers prefer the `.signal` file for anything beyond the simplest configurations.

**LiteLLM Proxy (all agents)**

```
signal <target> \
  --llm-mode byo \
  --llm-uri https://your-litellm-proxy.example.com/v1 \
  --llm-key "$LITELLM_KEY" \
  --llm-singlefilescan-agent-model claude-sonnet-4 \
  --llm-dataflow-agent-model gpt-4o \
  --llm-oversight-agent-model gpt-4o \
  --llm-exploitation-agent-model gpt-4o \
  --llm-sca-agent-model gpt-4o \
  --llm-mergekey-embed-agent-model text-embedding-3-large \
  --llm-oversight-embed-agent-model text-embedding-3-small \
  --llm-timeout 300
```

LiteLLM's own router picks the underlying provider based on the model prefix (`bedrock/…`, `azure/…`, `vertex_ai/…`), so a single Signal invocation can effectively route to multiple clouds through one proxy without the per-agent URI overrides.

**Azure OpenAI (all agents)**

`--llm-api-version` is **required** for Azure OpenAI endpoints. Use the per-agent variants if different agents target different API versions.

```
signal <target> \
  --llm-mode byo \
  --llm-uri https://your-resource.openai.azure.com/ \
  --llm-key "$AZURE_OPENAI_API_KEY" \
  --llm-api-version 2025-01-01-preview \
  --llm-singlefilescan-agent-model o3-mini \
  --llm-dataflow-agent-model o3-mini \
  --llm-oversight-agent-model o3-mini \
  --llm-exploitation-agent-model o3-mini \
  --llm-sca-agent-model o3-mini \
  --llm-mergekey-embed-agent-model text-embedding-3-large \
  --llm-oversight-embed-agent-model text-embedding-3-small
```

**GCP Vertex AI (all agents)**

No URI or API key; Signal authenticates with your service-account key and refreshes OAuth2 tokens automatically.

```
signal <target> \
  --llm-mode byo \
  --gcp-service-account-key ./gcp-sa-key.json \
  --gcp-project your-gcp-project-id \
  --gcp-region us-central1 \
  --llm-singlefilescan-agent-model gemini-2.5-pro \
  --llm-dataflow-agent-model gemini-2.5-flash \
  --llm-oversight-agent-model gemini-2.5-flash \
  --llm-exploitation-agent-model gemini-2.5-flash \
  --llm-sca-agent-model gemini-2.5-flash \
  --llm-mergekey-embed-agent-model text-embedding-005 \
  --llm-oversight-embed-agent-model text-embedding-005 \
  --llm-singlefilescan-agent-timeout 600 \
  --llm-dataflow-agent-timeout 600
```

**AWS Bedrock (all agents)**

Provide the Bearer token using either `--aws-bearer-token` or the `AWS_BEARER_TOKEN_BEDROCK` env var. `--aws-bedrock-region` (or `AWS_REGION`) is recommended; the built-in default is `us-east-1`.

```
export AWS_BEARER_TOKEN_BEDROCK="$(aws iam create-service-specific-credential \
  --user-name your-iam-user \
  --service-name bedrock.amazonaws.com \
  --credential-age-days 30 \
  --query 'ServiceSpecificCredential.ServiceCredentialSecret' \
  --output text)"
sleep 10   # let IAM propagate before first use

signal <target> \
  --llm-mode byo \
  --aws-bedrock-region us-east-2 \
  --llm-singlefilescan-agent-model us.anthropic.claude-sonnet-4-20250514-v1:0 \
  --llm-dataflow-agent-model us.anthropic.claude-3-5-haiku-20241022-v1:0 \
  --llm-oversight-agent-model us.anthropic.claude-3-5-haiku-20241022-v1:0 \
  --llm-exploitation-agent-model us.anthropic.claude-3-5-haiku-20241022-v1:0 \
  --llm-sca-agent-model us.anthropic.claude-3-5-haiku-20241022-v1:0 \
  --llm-mergekey-embed-agent-model amazon.titan-embed-text-v2:0 \
  --llm-oversight-embed-agent-model amazon.titan-embed-text-v2:0 \
  --llm-singlefilescan-agent-timeout 600
```

**Mixed: GCP for singlefilescan + LiteLLM for the rest**

GCP supplies singlefilescan (no URI → cloud-provider path); LiteLLM URIs on the other agents override the cloud provider and route to `ChatOpenAI` / `OpenAIEmbeddings`.

```
signal <target> \
  --llm-mode byo \
  --gcp-service-account-key ./gcp-sa-key.json \
  --gcp-project your-gcp-project-id \
  --gcp-region us-central1 \
  --llm-singlefilescan-agent-model gemini-2.5-pro \
  --llm-dataflow-agent-uri https://your-litellm-proxy.example.com/v1 \
  --llm-dataflow-agent-key "$LITELLM_KEY" \
  --llm-dataflow-agent-model gpt-4o \
  --llm-oversight-agent-uri https://your-litellm-proxy.example.com/v1 \
  --llm-oversight-agent-key "$LITELLM_KEY" \
  --llm-oversight-agent-model gpt-4o \
  --llm-exploitation-agent-uri https://your-litellm-proxy.example.com/v1 \
  --llm-exploitation-agent-key "$LITELLM_KEY" \
  --llm-exploitation-agent-model gpt-4o \
  --llm-sca-agent-uri https://your-litellm-proxy.example.com/v1 \
  --llm-sca-agent-key "$LITELLM_KEY" \
  --llm-sca-agent-model gpt-4o \
  --llm-mergekey-embed-agent-uri https://your-litellm-proxy.example.com/v1 \
  --llm-mergekey-embed-agent-key "$LITELLM_KEY" \
  --llm-mergekey-embed-agent-model text-embedding-3-large \
  --llm-oversight-embed-agent-uri https://your-litellm-proxy.example.com/v1 \
  --llm-oversight-embed-agent-key "$LITELLM_KEY" \
  --llm-oversight-embed-agent-model text-embedding-3-small
```

The verbosity of a fully-mixed CLI invocation is the second main reason customers reach for the `.signal` file; the config-file version of the same setup is roughly a third as long and easier to review.
