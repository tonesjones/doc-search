---
title: "Event kind (eventKind)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/event-kind-eventkind-.html"
content_id: "WsFNr~tl3UpSMr95POwvRg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:55.051377+00:00"
---

# Event kind (eventKind)

| Event Kind | Description |
| --- | --- |
| MODEL | Corresponds to a function call. In Coverity Connect, model events appear beside a *Show Details* link. |
| PATH | Identifies a conditional branch and the decision necessary for the software issue to occur. Example:Condition !p, taking false branch Related lines 107-108 of sample code: 107 if (!p) 108 return NO_MEM; |
| MULTI | Provides evidence from the source code that supports the checker's finding of a software issue. Also called an Evidence event. |
| NORMAL | References a line of code that is identified as a contributing factor to the software issue found by the checker. Examples: 1. alloc_fn: Storage is returned from allocation function malloc. 2. var_assign: Assigning: p = storage returned from malloc(12U) Related line 5 of sample code: 5 char *p = malloc(12); |
| REMEDIATION | Provides remediation advice that is intended to help you fix the reported software issue, rather than report what is wrong. Used in security defects. |
