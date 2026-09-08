---
title: "Polaris Assist (Beta)"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/polaris-assist-beta-.html"
content_id: "RunJkdvGyusjF2UQYbpy_A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:59.064918+00:00"
content_hash: "b68ff8db1b3b85ce61ee8379c87929c560579931b504d22f31f5eecc1673ab43"
---

# Polaris Assist (Beta)

Use the "Polaris Assist (Beta)" tab on the Settings page to configure and enable Polaris
Assist. SRM uses Azure OpenAI APIs, namely the [Chat Completion](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#chat-completions) API, and the Azure OpenAI URL
must refer to a service which exposes this endpoint.

**Warning:** Polaris Assist generates results created by artificial intelligence (AI)
or other automated technologies. Such results are provided for informational purposes
only and should not be relied upon for any specific purpose without verification of its
accuracy or completeness.

SRM will use the model `gpt-4o` in its requests, which requires that a
model with that name be available in the provided API.

Note: The
model `gpt-4o` is the default. To change this model, see Polaris Assist in the *Install Guide*.

[image: image]

Enter your Azure OpenAI URL and API Key, then click Test Connection. Use the checkbox to
enable Polaris Assist.

The "Test Connection" button will perform a test request using the configured
`model-id`.

For more information on configuring Polaris Assist and AI Insight, please refer to the
Install Guide.
