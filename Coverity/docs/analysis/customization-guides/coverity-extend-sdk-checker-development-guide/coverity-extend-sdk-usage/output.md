---
title: "Output"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/output.html"
content_id: "S7pDiklp69ATjetgtSkyjA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:36.871693+00:00"
---

# Output

**Outputting defects**

So far we have just been using `cout` to communicate information from a
checker, but the Coverity Extend SDK has a more sophisticated defect reporting
mechanism with several advantages:

1. The resulting reports are suitable for display in the Coverity Connect, just
   like other defect reports.
2. They properly take into account path feasibility, a topic covered in more
   detail in False Path Pruning (FPP).
3. A series of reports can be associated with specific variables or expressions,
   allowing the checker to communicate a timeline of important events in the
   diagnosis of the defect. This can greatly improve the comprehensibility of
   the report for flow-sensitive checkers.
