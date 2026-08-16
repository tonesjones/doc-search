---
title: "Changing LLM provider"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-llm-provider.html"
content_id: "Ju99I47QriTcvvkyjHdwjw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:33.937650+00:00"
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
