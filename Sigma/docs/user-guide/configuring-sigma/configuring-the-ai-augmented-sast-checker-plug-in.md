---
title: "Configuring the AI-augmented SAST checker plug-in"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-the-ai-augmented-sast-checker-plug-in.html"
content_id: "6krqWBOjW~oJvTqSmXlCtA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:05.630724+00:00"
---

# Configuring the AI-augmented SAST checker plug-in

Coverity and Sigma static analysis engines include a plug-in to enable AI-augmented SAST
checkers. These checkers, such as IDOR, add unique capabilities to the SAST engine (see
their respective documentation for details). To configure this plug-in, set the
following environment variables:

- `SIGMA_XX_LLM_URL`: the value should be a URL of the API end point
  that LLM requests are sent to.
- Either `SIGMA_XX_LLM_API_KEY_FILE` or
  `SIGMA_XX_LLM_API_KEY` (no need to set both):
  - The value of `SIGMA_XX_LLM_API_KEY_FILE` should be a path to
    a file. The contents of the file are the LLM API key. You should ensure that
    file system permissions are adequate to protect the secrecy of the API key.
  - Alternatively, the value of `SIGMA_XX_LLM_API_KEY` should be
    set to the LLM API key. You should ensure that access to the system where
    this process runs is adequate to protect the secrecy of the API key.
- `SIGMA_XX_LLM_MODEL_NAME`: the value should be the LLM model name.
  This model name is used as the `model` parameter in the plug-in’s
  HTTPS requests to the LLM, as specified by the [OpenAI spec](https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml). Currently, only the Anthropic
  Sonnet family of models are supported as they performed best for AI-augmented SAST
  features. Using a different LLM model may result in inferior performance of
  AI-augmented checkers (e.g., more false positive, more false negatives, etc.).

Once you’ve configured the plug-in, you must also enable any AI-augmented checkers you
wish to run. If AI-augmented checkers are enabled but these environment variables are
misconfigured or missing, there will be an error message in the logs and AI-augmented
checkers will not report any issues.
