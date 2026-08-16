---
title: "When are type_t objects resident in memory?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/when-are-type_t-objects-resident-in-memory-.html"
content_id: "Ej~cHszIRspErQx~NhR0Zw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:57.181835+00:00"
---

# When are type_t objects resident in memory?

In general, a checker should not save type_t pointers beyond the
analysis of the function when they were obtained. The reason is that
type_t objects get loaded and unloaded as the analysis runs. The
analysis guarantees to keep resident the set of types defined when the function being
analyzed was compiled, but not beyond that.
