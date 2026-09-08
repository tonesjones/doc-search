---
title: "Polaris Assist"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/polaris-assist.html"
content_id: "KdaMV8unRwADhmX0~CyatA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:40.364122+00:00"
content_hash: "61c86a6d61d1da85de9d32fdb1364e93aeae30d111253d72b4427ee844240bc8"
---

# Polaris Assist

Polaris Assist can be configured using the properties listed below. For more information,
see AI Insight Using
Polaris Assist in the *User Guide*.

## Properties Settings

The following properties can be set in the Software Risk Manager properties file:

- `assist.model-id [default: 'gpt-4o']` - The ID of the LLM
  that will be requested by SRM.
- `assist.code-context.max-lines [default: 100]` - The maximum
  number of lines of code to include as context for requests to the LLM
  (including the line range indicated by the finding and any surrounding
  lines).
- `assist.code-context.max-chars [default: 2048]` - The maximum
  number of characters of code to include as context for requests to the
  LLM.

  Lines of code will be excluded entirely if they would be
  truncated by this limit. For assessments on minified files that consist
  of a single line, this typically prevents code from being included at
  all.
- `assist.max-response-tokens [default: 100]` - The number of
  response tokens to request from the LLM for each assessment.
- `assist.max-file-size [default: 500000]` - The maximum file
  size (in bytes) of a source file that may be read to build the code-context
  for requests to the LLM.

  Source files which exceed this size will not be
  used when making requests to the LLM, regardless of
  `assist.code-context` settings.

## Model ID, LLM API

SRM supports connection to [Azure OpenAI APIs](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#chat-completions), making requests to
`{Azure OpenAI URL}/openai/deployments/{model-id}/completions`
with an `api-key` header.

Polaris Assist has been tested and validated with base models of GPT-3.5 Turbo,
GPT-4, and GPT-4o. We do not recommend fine tuning or the use of other models.

### Azure OpenAI

For installations connecting directly to Azure OpenAI, `model-id`
will be the "Deployment name" of the model deployed with Azure OpenAI Studio.
SRM does not use batch APIs, and the model's deployment type in Azure OpenAI
Studio must *not* be "Batch."
