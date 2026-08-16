---
title: "Security considerations for the AI-augmented SAST checker plug-in"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/security-considerations-for-the-ai-augmented-sast-checker-plug-in.html"
content_id: "PPB7VIXkqZ_l2S6w_5gk8g"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:06.270504+00:00"
---

# Security considerations for the AI-augmented SAST checker plug-in

Configuring the AI-augmented SAST checker plug-in is necessary to enable AI-augmented
SAST checkers (for more information, see Configuring the AI-augmented SAST checker plug-in).
Configuring the plug-in allows these checkers to consult the configured LLM when
deciding if and how to report issues. The scope of data sharing with the configured LLM
is limited to what is necessary for AI-augmented checkers to perform their function;
nevertheless, this data *does* include unredacted source files and issue data.

The configuration of this plug-in includes a URL to an LLM provider of your choice.
Ensure that your organization’s policy allows the sharing of the aforementioned data
with the configured LLM. Configuration of this plug-in and enabling AI-augmented
checkers constitutes opt-in to this data sharing. Should you wish to opt-out of future
data sharing, remove the configuration for this plug-in and disable AI-augmented
checkers. Should you wish to use a different LLM provider, change the URL and API key as
desired.

In addition, you should ensure that you

- Manage the API key in a secure way.
- Run SAST scans on secure infrastructure and in a secure network environment.

Note: Future versions of AI-augmented SAST checkers may have different security
considerations.
