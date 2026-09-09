---
title: "Understanding Hybrid (SAST/DAST) Correlation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/understanding-hybrid-sast/dast-correlation.html"
content_id: "71bvl9S44aScgR3WWzZHow"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:58.110712+00:00"
content_hash: "c64fbedc4bf8ab8cea9b590a02594762e2494f53c6df768639a525addd68eb05"
---

# Understanding Hybrid (SAST/DAST) Correlation

When Hybrid Correlation is enabled, URL-located results may be correlated with
file-located results by mapping result URLs to a set of source code locations. Results
with file and URL locations may be correlated if the file location overlaps with any of
the discovered file locations for the given URL. (Data flows are also checked for
overlaps.)

Source code is analyzed (for supported languages
and frameworks) to determine the specific files and line ranges that declare the
endpoint used by the URL path. If binaries are also provided, Software Risk Manager will
automatically build a call graph from the indicated source location to collect
additional locations to compare against. (Call graph generation is only
supported for JVM and CLR binaries.)
