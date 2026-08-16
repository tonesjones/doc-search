---
title: "Analysis of the reference structure"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-of-the-reference-structure.html"
content_id: "4h6fip2vP7UaFMVgek9UWw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:41.336553+00:00"
---

# Analysis of the reference structure

If the `-anref` option and the `-rigorous` is in effect the
call tree will be traversed to detect unsaved common blocks and modules with unsaved
public data which are not specified in the root of referencing program units.

Recursive references are traced, also if one of the entries of a procedure in the chain
is being referenced. If recursive reference is not supported, or the procedures in the
chain are not specified RECURSIVE, these procedures are flagged. Moreover, if the
`-ancmpl` option has been specified and a procedure is specified
RECURSIVE but is not recursively referenced, it is flagged.
