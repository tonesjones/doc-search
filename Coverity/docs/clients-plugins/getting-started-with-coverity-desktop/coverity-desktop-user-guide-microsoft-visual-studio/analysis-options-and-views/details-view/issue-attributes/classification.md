---
title: "Classification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classification.html"
content_id: "THrMNYf3pLLdjdqGLic8Cg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:34.393441+00:00"
---

# Classification

The table below lists descriptions for each of the possible issue
classifications, along with the Issue Kind(s)
each classification can be attributed to.

Table 1. Classifications

| Classification | Description | Issue Kind(s) |
| --- | --- | --- |
| Unclassified | This attribute is the default when a new result is inserted. It is intended for results that have yet to be viewed by a developer. | Quality, Security |
| Pending | An issue that has been examined, but has yet to be conclusively classified. | Quality, Security |
| False Positive | Results that are not real issues in the code. If these appear to reflect shortcomings or flaws in the analysis engine, report the issue to <https://community.blackduck.com/s/contactsupport>. | Quality, Security |
| Intentional | Designates that analysis has accurately diagnosed behavior that is usually unintentional, but in this scenario is actually the intended behavior. | Quality, Security |
| Bug | Reflects a determination that the issue found by Coverity Analysis is an issue in the code, and is not a False Positive or Intentional. | Quality, Security |
