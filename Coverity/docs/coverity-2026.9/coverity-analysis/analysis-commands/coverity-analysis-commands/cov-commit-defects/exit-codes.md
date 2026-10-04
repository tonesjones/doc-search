---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/exit-codes.html"
content_id: "FyonyDRta75RnEVfbW74Sg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:47.637326+00:00"
---

# Exit codes

This command returns the following exit codes:

- 0: Success.
- 3: Non-fatal error.
- Other: Internal error.

Any errors during a commit are recorded in Coverity Connect in the
<install_dir>/logs/cim.log file. Errors and warnings
are also recorded to the
<intermediate-dir>/output/commit-error-log.txt file.
