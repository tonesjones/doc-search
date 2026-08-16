---
title: "Function procedure"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/function-procedure.html"
content_id: "gl2OBEZi_~Kf8pj~bUOcnQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:39.326858+00:00"
---

# Function procedure

If a function performs external I/O, (de)allocates memory, contains a
`STOP` or `PAUSE` statement, modifies any argument,
common-block object or saved item, and the `-rigorous` option has been
enabled, the function is flagged as ”impure”.
