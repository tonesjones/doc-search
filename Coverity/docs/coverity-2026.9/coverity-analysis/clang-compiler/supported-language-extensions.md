---
title: "Supported Language Extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/supported-language-extensions.html"
content_id: "bWuqjm5D1ao5dPBwLmfgqg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:25.622315+00:00"
---

# Supported Language Extensions

Apple Blocks
:   Support for the Apple Blocks extensions is provided for C and C++ code, and is automatically
    enabled when enabled in native compiler invocations. Interprocedural analysis of
    Block invocations requires that `cov-analyze` be invoked with
    one of the `--enable-single-virtual` or
    `--enable-virtual` options.
