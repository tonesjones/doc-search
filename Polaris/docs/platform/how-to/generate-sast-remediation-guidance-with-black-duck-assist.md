---
title: "Generate SAST remediation guidance with Black Duck Assist"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/generate-sast-remediation-guidance-with-black-duck-assist.html"
content_id: "m2j8xFN6lF0JlS3QQL6wsg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:22.365168+00:00"
content_hash: "78ff0028ce0fd36cda8940593003a653fdb7616eadfb934e1c6c5347b883a884"
---

# Generate SAST remediation guidance with Black Duck Assist

Use Black Duck Assist to generate remediation guidance (including an issue summary, code analysis, and fix suggestion) for a SAST issue with a large language model (LLM).

## Overview

When you run Black Duck Assist to generate SAST remediation guidance, it formulates prompts using:

- The issue's Common Weakness Enumeration (CWE) identifier
- The issue's description
- The line number on which the issue was found
- A code snippet that includes the issue (approximately 10 lines of code)

... that are sent to a private LLM service to generate remediation guidance that appears in Polaris, including:

- Issue Summary: A short description of the issue.
- Code Analysis: An analysis of the code in which the issue is identified.
- Fix Suggestion: A revision (in code) that may remediate the issue.

Note: The guidance Black Duck Assist generates is not preserved or shared with other users in your organization. If you navigate to a different page or sign out of Polaris, the remediation guidance you generated previously is discarded.

Black Duck Assist is compatible with SAST issues (and all the languages in the SAST Language Support table).

### Data privacy

Black Duck Assist communicates with a LLM that runs on a private cloud service. Please note:

- None of the prompts or responses exchanged between Black Duck Assist and the LLM are used to:
  - Train or improve the LLM.
  - Improve the LLM provider's other products or services.
- Black Duck Assist does not retain source code used in prompts.
- User-submitted feedback on responses is not sent to the LLM.
- Each response from Black Duck Assist is only shared with the user who requests it.
- Data exchanged between Black Duck Assist and the LLM is encrypted for storage and transmission.

### Accuracy and completeness

Warning:

Black Duck Assist generates results created by artificial intelligence (AI) or other automated technologies. Such results are provided for informational purposes only and should not be relied upon for any specific purpose without verification of its accuracy or completeness.

## Enable Black Duck Assist (AI Insight)

Black Duck Assist is disabled by default and can only be enabled by an Organization Administrator. To enable Black Duck Assist, follow these steps:

1. Go to My Organization > Black Duck Assist.
2. Select Enable AI Insight.

## Use Black Duck Assist

To use Black Duck Assist, follow these steps:

1. Go to Portfolio, open an application, and open a SAST & SCA project.
2. Select a SAST issue.

   The Issue Details panel appears.
3. Select AI Insight powered by Black Duck Assist.

   [image: polaris assist gen]

   The Contributing Code Events panel opens, and Polaris generates an Issue Summary, Code Analysis, and Fix Suggestion that you may be able to use to remediate the issue.

   [image: polaris assist result]

   Warning:

   Black Duck Assist generates results created by AI or other automated technologies. Such results are provided for informational purposes only and should not be relied upon for any specific purpose without verification of its accuracy or completeness.

   Select [image: icon assist copy] Copy to copy an Issue Summary, Code Analysis, or Fix Suggestion to your clipboard.
4. (Optional) Use the feedback buttons to submit positive ( [image: icon assist positive] ) or negative ( [image: icon assist negative] ) feedback.

   Tip: To run Black Duck Assist again (and generate new remediation guidance), refresh the page and repeat these steps.
