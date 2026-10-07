---
title: "Troubleshooting"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/troubleshooting.html"
content_id: "SnBif4W_krb2UVHzvyqvDg"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.856673+00:00"
---

# Troubleshooting

When something goes wrong, Signal does not surface a generic "LLM call failed" message; every BYOLLM error is **agent-tagged** so you know whether the problem is in `singlefilescan-agent`, `dataflow-agent`, `oversight-agent`, `exploitation-agent`, `sca-agent`, `mergekey-embed-agent`, or `oversight-embed-agent`. The same agent tag appears in `--check-llm` table output, in `--check-llm-json`'s per-item records, and in the live scan log when a request fails partway through. If you see `SIGNAL-E110: Authentication
failure for provider 'openai_compatible' (agent: mergekey-embed-agent)` , you know exactly which section of your `.signal` file (or which CLI flag prefix) to inspect.

Errors fire at one of three lifecycle stages:

- **Config-parse time**: Your `.signal` file or CLI flags fail validation before any LLM call is made. These are the cheapest errors to debug because they fire before Signal does any work; the message names the missing or contradictory field directly. Examples: `gcp_project is required for Vertex AI`, `Cannot configure both GCP and AWS Bedrock`, `At least one LLM endpoint URI must be set in byo
  mode`, `Azure endpoint detected but no api_version
  provided`.
- **Preflight time (**`--check-llm`**)**: The config parsed cleanly, but the live probe against the endpoint fails. These tell you the endpoint exists in Signal's view of the world but the customer's view of the world (network, IAM, model deployment) does not agree. Run `--check-llm True` first whenever you suspect a runtime issue; it isolates the failure to one agent and gives you the exact error message a real scan would surface.
- **Mid-scan**: The same probe passed, but a real request fails partway through (rate limiting, model deprecation, transient network issue, token expiry). These errors carry the same agent tag and are usually identical to what `--check-llm` would have shown; re-run preflight to reproduce cheaply.

The exit-code contract: `0` means everything Signal could check was healthy at the moment of checking; `1` means at least one agent failed. Use that in CI to gate scan jobs on preflight success.

**Common errors and fixes**

The table below lists common errors, their root causes, and how to fix them. Quoted text is close to what you would see in your terminal; the exact wording is subject to change but the numeric code is stable.

|  |  |  |
| --- | --- | --- |
| Error (excerpt) | Cause | Fix |
| `SIGNAL-E110: Authentication failure ... (agent: oversight-agent)` | Invalid API key on the oversight agent | Verify `--llm-oversight-agent-key` or `[LLM_OVERSIGHT_AGENT] key`; check the general `--llm-key` too, since per-agent falls back to it. |
| `SIGNAL-E111: Connection failure ... (agent: ...)` | Network / firewall issue | Check endpoint URL and network connectivity; retry once (E111 is marked retryable). |
| `SIGNAL-E112: Model not found ... Model: <name>` | Model does not exist on the endpoint | Verify the model name matches what your endpoint exposes exactly. For Azure OpenAI, the model name is the deployment name; case-sensitive. For Bedrock, use the full model ID including any regional inference-profile prefix. |
| `SIGNAL-E113: Rate limited ... (agent: ...)` | 429 from the provider | Reduce `--llm-limit` and `--agent-limit`, or wait. Retryable. |
| `SIGNAL-E114: Quota exceeded` | Provisioned capacity exhausted | Request a quota increase with the provider, or switch the failing agent's `model` to a different one with available capacity. |
| `SIGNAL-E115: Authentication token expired` | Temporary credential rotation (GCP OAuth2, Bedrock bearer) expired mid-scan | Rotate the credential. Retryable. |
| `SIGNAL-E117: Configuration validation failure ...` | Missing required field, or invalid combination (e.g. Azure OpenAI without `api_version`) | The message names the specific field. Fix and re-run. |
| `SIGNAL-E118: Cloud provider configuration error` | GCP or Bedrock configured incorrectly, or both configured simultaneously | Set only one cloud provider globally; use per-agent URIs to reach the other. |
| `Azure endpoint detected (...) but no api_version provided.` | Azure OpenAI hostname matched but no API version was supplied | Set `--llm-api-version` (e.g. `2024-12-01-preview`) or the per-agent variant. Not needed for Azure AI Services Claude endpoints. |
| `URI does not end with '/v1'` (warning, not error) | Non-standard endpoint path | Most OpenAI-compatible endpoints use `/v1` — verify your endpoint URL. Warning only; Signal proceeds. |
| `gcp_project is required for Vertex AI` | Missing GCP project | Set `--gcp-project` or `[LLM] gcp_project`. |
| `gcp_region is required for Vertex AI` | Missing GCP region | Set `--gcp-region` or `[LLM] gcp_region`. |
| `Failed to load GCP credentials` | Invalid SA key | Verify the key format (file path, base64, or raw JSON) and file permissions. |
| `Cannot configure both GCP Vertex AI and AWS Bedrock` | Both providers set globally | Use only one cloud provider globally; front the other through a URI-based proxy for the agents that need it. |
| `403 Forbidden` from Bedrock (immediately after credential creation) | IAM eventual consistency | Sleep ~10 seconds after `aws iam create-service-specific-credential`, then retry. |
| Agent uses GCP / Bedrock when it should use LiteLLM / Azure | Missing per-agent `uri` on that agent's section | Set `uri` and `key` on the agent's `[LLM_<AGENT>_AGENT]` section to route it to the URI-based path. |
| Agent uses LiteLLM / Azure when it should use GCP / Bedrock | Per-agent `uri` is set on an agent that should reach the cloud provider | Remove `uri` and `key` from that agent's section so the factory picks the cloud provider. |
