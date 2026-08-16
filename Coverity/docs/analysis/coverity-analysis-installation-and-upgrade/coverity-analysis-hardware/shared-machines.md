---
title: "Shared machines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/shared-machines.html"
content_id: "VaHyJKajPU~69d8WJwzzWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:48.948602+00:00"
---

# Shared machines

When the analysis runs simultaneously with other programs and makes a significant use of
machine resources, the primary concern is memory. With adequate physical memory for
active processes and adequate virtual memory (swap space) for inactive ones, sharing CPU
time among other processes does not pose problems. If adequate memory is unavailable,
you can reduce the memory usage by configuring the analysis to use only part of
available CPU parallelism.

You can think of the memory as "free physical memory" requirements, however running an
analysis alone in a basic user environment is close enough to "total physical
memory".
