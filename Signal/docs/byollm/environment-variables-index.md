---
title: "Environment Variables Index"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/environment-variables-index.html"
content_id: "9nrUoYGQPMyyXc_tqWjExA"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.876898+00:00"
---

# Environment Variables Index

Signal reads several environment variables as fallback values for sensitive or environment-specific fields. Use them when you do not want to put a secret in your `.signal` file (so it can be source-controlled safely) or when running in CI where the credential is already exported by the pipeline. Every variable below is read at process start; changing one mid-scan has no effect.

|  |  |  |
| --- | --- | --- |
| Variable | Used for | When it applies |
| `OPENAI_API_KEY` | `--llm-key` / `[LLM] key` (non-Azure URI resolved) | Used when neither the CLI flag nor any config field supplies an API key. The standard OpenAI SDK convention. Honoured for any URI-based provider whose hostname is not Azure, not just direct OpenAI. |
| `AZURE_OPENAI_ENDPOINT` | `[LLM] uri` | Used when `[LLM] uri` is unset in byo mode. Fills the general URI from the SDK-standard Azure env var. |
| `AZURE_OPENAI_API_KEY` | `[LLM] key` (Azure URI resolved) | Used when the resolved `[LLM] uri` matches an Azure suffix and `[LLM] key` is unset. |
| `AZURE_OPENAI_API_VERSION` | `[LLM] api_version` (Azure URI resolved) | Used when the resolved `[LLM] uri` matches an Azure suffix and `[LLM] api_version` is unset. |
| `AWS_BEARER_TOKEN_BEDROCK` | `--aws-bearer-token` / `[LLM] aws_bearer_token` | Used when neither the CLI flag nor config field supplies the Bearer token. Recommended for CI: export it from a secret manager instead of templating it into the config file. |
| `AWS_REGION` | `--aws-bedrock-region` / `[LLM] aws_bedrock_region` | Used when neither the CLI flag nor config field supplies a region; if still unset, the factory falls back to `us-east-1`. Order: `--aws-bedrock-region` beats `[LLM] aws_bedrock_region` beats `AWS_REGION` beats `us-east-1`. |
| `GOOGLE_APPLICATION_CREDENTIALS` | `[LLM] gcp_service_account_key` | Used when `[LLM] gcp_service_account_key` is unset in byo mode. Value is a file path (matches the standard GCP SDK convention). |
| `GOOGLE_CLOUD_PROJECT`, then `GCP_PROJECT` | `[LLM] gcp_project` | Tried in order when `[LLM] gcp_project` is unset in byo mode. |
| `GOOGLE_CLOUD_REGION`, then `GCP_REGION` | `[LLM] gcp_region` | Tried in order when `[LLM] gcp_region` is unset in byo mode. |

Every SDK-env-var fallback in the table above applies **only in byo mode** and **only to the** `[LLM]` **general section**. Per-agent sections inherit these values through the normal precedence chain (per-agent CLI → per-agent config → general CLI → `[LLM]` → SDK env → default/error); ambient env vars never populate per-agent slots directly.

## How variable expansion works in config files

If a config-file value contains a `$` character, Signal runs `os.path.expandvars` on it before resolving the rest of the inheritance chain. This applies to **every BYOLLM field**: `uri`, `key`, `model`, `timeout`, `api_version` on any `[LLM_<AGENT>_AGENT]` section, and every field on `[LLM]` including the GCP and AWS credential fields. So `key = ${OPENAI_API_KEY}` in your `.signal` file is equivalent to leaving that field unset and exporting `OPENAI_API_KEY` in your shell; pick whichever is more convenient for your secret-management workflow. Unresolved references (env var not set at process start) surface as a single `SIGNAL-E117` listing every offending section/field/name so you can fix them all in one pass.

Shell-style default syntax like `${VAR:-fallback}` is **not** supported; export the variable instead. Use `$$` if you need a literal `$` in a value.
