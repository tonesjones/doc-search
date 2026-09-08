---
title: "AI Insight Using Polaris Assist"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/ai-insight-using-polaris-assist.html"
content_id: "NzR0Krbwzc0BCm87M7whZw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:26.607954+00:00"
content_hash: "9974cf8a2d293a91fdbfddd6fb072b4a3181a494668a2737a74f2ffefdd24c06"
---

# AI Insight Using Polaris Assist

When Polaris Assist is configured and enabled, an "AI Insight" section will be available
for findings which have a *Static Analysis* detection method and have the required
information for at least one of the available assessments listed below. (For information
on configuration, see Polaris
Assist.)

Note: Users must have the permission
`Request and view finding assessments from Polaris Assist (Beta)`
for the project, which is included in the default `Reader` role
provided by SRM.

**Warning:** Polaris Assist generates results created by artificial intelligence (AI)
or other automated technologies. Such results are provided for informational purposes
only and should not be relied upon for any specific purpose without verification of its
accuracy or completeness.

Click the AI Assist button to expand the fields.

[image: image]

When possible, SRM will offer up to three sub-assessments:

- **Summary.** Polaris Assist will provide a brief summary of the vulnerability
  and its impact. Requires finding description and CWE.
- **Code Analysis.** Polaris Assist will summarize an excerpt of the affected
  code and surrounding lines and a description of the vulnerability in the context
  of the affected code.
  - Code summary requires a file location with source code.
  - Vulnerability analysis requires a file location with source code,
    finding description, and CWE.
- **Fix Suggestion.** Polaris Assist will suggest an updated code snippet that
  attempts to address the vulnerability.
  - Requires a file location with source code, finding description, and
    CWE.
