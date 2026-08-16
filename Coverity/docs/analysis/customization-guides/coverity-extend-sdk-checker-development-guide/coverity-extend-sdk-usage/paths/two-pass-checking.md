---
title: "Two-pass checking"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/two-pass-checking.html"
content_id: "REVFsUo7ciriPNZ8506NIg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:49.298583+00:00"
---

# Two-pass checking

Because the FPP modules are somewhat computationally expensive, they are disabled until
the checker calls either the COMMIT_ERROR or
OUTPUT_ERROR functions. Once the checker tries to output an
error, the analysis of that function is restarted with the FPP modules enabled. This
saves time in the usual case where a checker does not find any problems on any path, but
still filters out reports from infeasible paths.

This is another reason why cout produces misleading results: your
checker appears to analyze some functions twice due to the activation of the second
pass.
