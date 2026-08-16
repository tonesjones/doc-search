---
title: "Classification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classification.html"
content_id: "74m1A0BmETRhGal6ro789w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:45.032846+00:00"
---

# Classification

The table below lists descriptions for each of the possible issue
classifications, along with the Issue Kind(s)
each classification can be attributed to.

Table 1. Classifications

| Classification | Description | Issue Kind(s) |
| --- | --- | --- |
| Unclassified | This attribute is the default when a new result is inserted. It is intended for results that have yet to be viewed by a developer. | Quality, Security |
| Pending | An issue that should be fixed eventually, but perhaps is not critical enough to fix in the current source code base, or there are other dependencies that prevent it from being fixed at this time. | Quality, Security |
| False Positive | Results that are not real issues in the code. If these appear to reflect shortcomings or flaws in the analysis engine, report the issue to <https://community.blackduck.com/s/contactsupport>. | Quality, Security |
| Intentional | While the result might be a real bug according to the C/C++ or C# language, it is not a bug in this code because either the code is not important, or the code can never be exercised in a dangerous way in deployment environments. | Quality, Security |
| Bug | Reflects a determination that the issue found by Coverity Analysis is an issue in the code, and is not a False Positive or Intentional. | Quality, Security |
