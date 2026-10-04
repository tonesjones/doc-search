---
title: "Preflight validation"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/preflight-validation.html"
content_id: "4uJU~WyShorEC8fjQO1Z5g"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.831424+00:00"
---

# Preflight validation

A full Signal scan can take tens of minutes on a large target, so discovering halfway through that one of your seven LLM agents is misconfigured; bad URL, expired key, missing model deployment, wrong API version; is an expensive failure. The `--check-llm` flag exists to surface that class of failure in seconds, before a single source file is scanned.

**What `--check-llm` actually does**

When you pass `--check-llm True`, Signal **skips the scan entirely** and instead walks every agent you have configured, instantiates the same client class that a real scan would use, and runs a minimal probe against the live endpoint:

- **Chat agents** (`singlefilescan`, `dataflow`, `oversight`, `exploitation`, `sca`); issues an `invoke("Hello")` completion to verify that the URL resolves, the key authenticates, the model exists on the endpoint, and (for Azure OpenAI) the `api_version` is acceptable.
- **Embedding agents** (`mergekey-embed`, `oversight-embed`); issues an `embed_query` for the fixed string `"test"` and verifies the returned vector has non-zero dimensionality.

Each agent's result is reported with its endpoint, model name, provider, latency, and (on failure) the agent-tagged error message; the same message you would see if the same problem surfaced mid-scan, so debugging the preflight failure is identical to debugging the real one.

**Use cases**

- **First-time setup** — run it once after writing your initial `.signal` file or assembling your CLI invocation. Almost every "BYOLLM doesn't work" issue customers report is caught by preflight.
- **After credential rotation** — Bedrock service-specific credentials, Azure keys, GCP service-account keys all change. Run `--check-llm` after every rotation to confirm the new credential reaches every agent before triggering a real scan.
- **In CI, before queueing a scan** — exit code 0 means every configured agent is reachable. Exit code 1 means at least one agent failed; fail your pipeline early instead of consuming scan budget.
- **As a smoke test after upgrading Signal** — provider integrations occasionally shift between releases (model deprecations, API version requirements changing). Preflight catches the regression cheaply.

**Output modes**

The default human-readable output is a Rich table. For machine consumption, pass `--check-llm-json True` (which implies `--check-llm
True`) and Signal emits a single JSON document on stdout; no other noise; The JSON schema is versioned (`schema_version: "1"`) and is the stable contract these tools rely on; field additions are non-breaking, removals or type changes bump the version. The `test_check_llm_json_e2e.py` integration suite regression-tests the schema, so the JSON shape will not drift silently between releases.

**Valid Configuration output example**

```
                                LLM Endpoint Validation
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Agent                 ┃ Endpoint                     ┃ Model                    ┃ Status                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ singlefilescan-agent  │ GCP Vertex AI                │ gemini-2.5-pro           │ ✅ OK                  │
│ dataflow-agent        │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ oversight-agent       │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ exploitation-agent    │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ sca-agent             │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ mergekey-embed-agent  │ https://litellm.example/v1   │ text-embedding-3-large   │ ✅ OK (dim=3072)       │
│ oversight-embed-agent │ https://litellm.example/v1   │ text-embedding-3-small   │ ✅ OK (dim=1536)       │
└───────────────────────┴──────────────────────────────┴──────────────────────────┴────────────────────────┘

All LLM endpoints validated successfully.
```

**Invalid Configuration output example**

A failed agent shows `✗ FAIL: E<code>: <message>` in the Status column with the message truncated to 80 characters. The same information appears in the JSON output under `agents[].error_code` and `agents[].error_message` with no truncation.

```
                                                                                          LLM Endpoint Validation                                                                                           
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Agent                 ┃ Endpoint                                               ┃ Model                  ┃ Status                                                                                         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ singlefilescan-agent  │ https://llm.labs.blackduck.com/v1/                     │ claude-sonnet-4        │ ✗ FAIL: E110: Error code: 401 - {'error': {'message': 'Authentication Error, Invalid proxy ser │
│ dataflow-agent        │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ oversight-agent       │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ exploitation-agent    │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ sca-agent             │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ mergekey-embed-agent  │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ text-embedding-3-large │ ✅ OK (dim=3072)                                                                               │
│ oversight-embed-agent │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ text-embedding-3-small │ ✅ OK (dim=1536)                                                                               │
└───────────────────────┴────────────────────────────────────────────────────────┴────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────┘
```
