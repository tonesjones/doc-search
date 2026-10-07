---
title: "Changing LLM provider"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/changing-llm-provider.html"
content_id: "3w12ZYhSQHUwD2Bnyp0E_w"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:35.739276+00:00"
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

3. For distributed deployment: 
   1. Update the triage-suggestion-service.llm.url and
      triage-suggestion-service.llm.name values in your Helm configuration.
   2. Run the Helm upgrade command to apply the changes: `helm upgrade
      <release> <chart-path-or-name> -n <namespace> -f
      <your-values.yaml>`
