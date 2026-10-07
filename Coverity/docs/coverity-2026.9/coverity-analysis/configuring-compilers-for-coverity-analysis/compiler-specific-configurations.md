---
title: "Compiler-specific configurations"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/compiler-specific-configurations.html"
content_id: "fbANW3xTtdTqvnXMD0daZA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:25.542826+00:00"
---

# Compiler-specific configurations

Some compilers have unique compilation environments that Coverity Analysis simulates to
properly parse the source code. Especially important are the predefined macros and
include directories built into the compiler. Predefined macros can be configured into
nodefs.h, and pre-included directories into
coverity_config.xml. For more information about how to get
`cov-translate` to add and remove command-line arguments to pass to
`cov-emit`, see Using Coverity Analysis configuration files in the analysis.
