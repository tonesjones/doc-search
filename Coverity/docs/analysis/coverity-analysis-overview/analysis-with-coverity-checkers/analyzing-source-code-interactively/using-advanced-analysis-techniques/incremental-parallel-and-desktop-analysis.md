---
title: "Incremental, parallel, and desktop analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incremental-parallel-and-desktop-analysis.html"
content_id: "vDk0BxGjglVBSqWZ3uyYQw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:13.684673+00:00"
---

# Incremental, parallel, and desktop analysis

This section describes three analysis modes that you can use to improve performance. For
best results, you should be familiar with how these modes work and how they affect
Coverity performance:

- **Incremental analysis** speeds up analysis by
  relying on data stored in the intermediate directory from previous analyses.
- **Parallel analysis** spawns a number of analysis
  worker processes to carry out the analyses in parallel. The number of workers you
  can use is related to the number of CPUs and available RAM.
- **Desktop analysis** produces a fast desktop or
  IDE-based analysis. Results might differ slightly from a full analysis because only
  changed files are analyzed.

In this section:

- Running analysis as part of a CI/CD pipeline
