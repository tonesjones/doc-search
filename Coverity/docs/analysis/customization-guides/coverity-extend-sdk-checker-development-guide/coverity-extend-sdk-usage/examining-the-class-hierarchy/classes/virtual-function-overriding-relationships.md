---
title: "Virtual function overriding relationships"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/virtual-function-overriding-relationships.html"
content_id: "rqnGlylJq__ScC3TM~A98Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:53.920325+00:00"
---

# Virtual function overriding relationships

Given two `function_t` objects, the
`function_t::overrides()` method can be used to determine whether
one overrides the other. This function can only be called if the class hierarchy allows
it. For example, if you call `f1->overrides(f2)`, then
`f1->get_owner_class()->derives_from(f2->get_owner_class())`
must be true.
