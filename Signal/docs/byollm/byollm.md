---
title: "BYOLLM"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/byollm.html"
content_id: "YUNO2lj47cRmGK1ZaaD75w"
version: "latest"
section: "BYOLLM"
scraped_at: "2026-10-04T23:27:49.674995+00:00"
---

# BYOLLM

Bring Your Own Large Language Model (BYOLLM) allows customers to connect Signal to their own Large Language Model (LLM) endpoints instead of using the managed Signal LLM service.

Signal performs software static analysis using an LLM-based approach, where all LLM interactions go through the Black Duck gateway. However, when customers enable BYOLLM, they are able to point Signal to a supported LLM provider of their choice, so all AI-powered analysis runs against the infrastructure they control, which is particularly interesting for customers with strict data residency requirements, existing enterprise LLM agreements, or cost optimization goals.

## Benefits of enabling BYOLLM

- **Data sovereignty:** Keep source code and analysis prompts within their own cloud tenancy or on-premises network; nothing leaves your perimeter.
- **Cost control:** Use existing enterprise LLM contracts, reserved capacity, or volume discounts instead of additional spend.
- **Model preference:** Choose specific model versions (e.g., GPT-4o, Claude Sonnet, Gemini 2.5 Pro) that match their accuracy or latency requirements.
- **Air-gapped environments:** Run Signal in networks with no outbound internet access by pointing at an internal LLM proxy.
- **Compliance:** Satisfy regulatory requirements that prohibit sending data to third-party AI services.
- **Auth support in V1:** Static API keys or Bearer tokens for URI-based providers (OpenAI, LiteLLM, Azure), GCP service-account JSON keys with auto-refreshed OAuth2 for Vertex AI, and IAM service-specific Bearer credentials for AWS Bedrock.

## Auth support in V1

- Static API keys or Bearer tokens for URI-based providers, such as OpenAI, LiteLLM and Azure.
- GCP service-account JSON keys with auto-refreshed OAuth2 for Vertex AI.
- IAM service-specific Bearer credentials for AWS Bedrock.
