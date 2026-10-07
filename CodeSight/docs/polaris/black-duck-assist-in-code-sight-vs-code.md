---
title: "Black Duck Assist in Code Sight (VS Code)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/black-duck-assist-in-code-sight-vs-code-.html"
content_id: "I0ecvnoEJTgpHU6wg95bog"
version: "2026.9.0"
section: "Polaris with Code Sight"
scraped_at: "2026-10-06T23:39:54.946108+00:00"
---

# Black Duck Assist in Code Sight (VS Code)

In VS Code, Black Duck Assist is available in Code Sight for users who have authenticated a Polaris server
and enabled Black Duck Assist.
This feature provides AI-generated remediation guidance for SAST issues directly within your IDE.

When you request remediation guidance in Code Sight, only the issue ID is transmitted to Polaris.
Polaris then securely retrieves the necessary context and acts as an intermediary, forwarding the request to a
private LLM service to generate the guidance.

The LLM returns structured output, which includes:

- **Issue summary**

  A concise explanation of the issue
- **Code analysis**

  A breakdown of the problematic code
- **Suggested fix**

  A proposed code change to remediate the issue

CAUTION:

Guidance is generated on-demand and *is not stored*.
If you close the IDE or navigate away, the generated guidance will not persist.

## Data privacy

Black Duck Assist in Code Sight uses a private cloud-hosted LLM,
with Polaris acting as a secure intermediary.
The following privacy protections apply:

- **Minimal data from the IDE**

  Code Sight sends only the issue ID to Polaris.
- **No training**

  Prompts and responses are *not used* to train or improve the LLM or any other services.
- **No retention**

  Source code and prompts are *not stored* by either Black Duck Assist or the LLM provider.
- **No sharing**

  Responses are visible *only to the user who requests them*.
- **No feedback sharing**

  User feedback on responses *is not sent* to the LLM.
- **Encryption**

  All data exchanged between Code Sight, Polaris, and the LLM is encrypted
  during transmission and storage.

## Disclaimer: Accuracy and completeness

Important:
Black Duck Assist generates responses using AI. These are intended for *informational purposes only,* and should not be
relied upon without *manual verification*. Always review and test any suggested fixes before you apply them to your codebase.
