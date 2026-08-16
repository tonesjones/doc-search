---
title: "Uninstalling AI-Assisted Triage Plug-in"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/uninstalling-ai-assisted-triage-plug-in.html"
content_id: "SieSDPp3jjOXMpCeQ4UZtw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:06.110785+00:00"
---

# Uninstalling AI-Assisted Triage Plug-in

This topic describes the steps to uninstall AI-Assisted Triage Plug-in from your
environment.

**To uninstall a standalone deployment of the triage suggested
service**:

1. Invoke a PUT request on `/config/system/ai/globalLlmKey` or
   `/config/projects/llmKey` in Connect to set the LLM key to an
   empty value for each project.
2. Stop and remove the Docker container, if applicable.
3. Delete any bind-mounted directories associated with the service.
4. Remove `triage-suggestion-service.json` and any associated
   files, including authentication keys, encryption keys, and other sensitive
   data.
5. Delete all service binaries from the host system.
