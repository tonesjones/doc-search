---
title: "Running parallel builds"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-parallel-builds.html"
content_id: "qj3YFCRZ8c6~sC3_ZYbdgg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:13.910150+00:00"
---

# Running parallel builds

Coverity Analysis for C/C++ supports multiple parallel build scenarios to
provide integration with a native build system with minimal or no system modifications.
Because of I/O and synchronization costs, parallel builds might not take place more
quickly than the builds described in Record/Replay: Deferred builds and parallelizing single-process builds.

In this section:

- Single build on a single machine
- Multiple builds on a single machine
- Multiple builds on multiple machines
