---
title: "Changing LLM provider"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-llm-provider.html"
content_id: "EoNhLGzyPtxJJPiFkwNT7Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:07.241686+00:00"
---

# Changing LLM provider

To change the LLM provider for the AI-assisted Triage Plug-in, you need to modify LLM
key and URL.

To change the LLM API keys

1. Set the LLM key using the `/config/system/ai/globalLlmKey` or
   `/config/projects/llmKey` REST APIs in Connect (request
   scoped). To update the LLM key, use the corresponding PUT REST API.
2. To update the LLM key, use the corresponding PUT REST API.

To change the LLM URL

3. For standalone deployment: 
   1. Update the llm_url and llm_name values in the
      triage-suggestion-service.json (or YAML) file used during binary
      invocation.
   2. Restart the service for the changes to take effect.
