---
title: "Configure compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-compilers.html"
content_id: "pSkx126OhMB7cSNPY9JFrg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:39.480477+00:00"
---

# Configure compilers

Coverity will attempt to generate configurations for each compiler used in a Bazel build
captured with `cov-build`. This process will work for compilers that are
well known and named with their canonical name (for example, `gcc`, `g++`, `clang`, `java`).
That is, it will work for any compiler that could be configured with `cov-configure --template --compiler <compiler name>`
(without specifying a compiler type).

If the configuration generation fails, a file containing the paths of the compilers that
could not be configured will be written to the intermediate directory. The
`cov-build` command will print an error containing the path to that
file and the path to the generated configuration for the remainder of the compilers.
Compilers that could not be configured automatically will need to be manually
configured; see Using the Compiler Integration Toolkit (CIT) for
information on configuring Coverity Analysis to emulate arbitrary compilers.

Configurations passed to `cov-build` directly with the
`-c/-config` flag will be respected, and passing a configuration in
this way will prevent Coverity from attempting to generate configurations
automatically.
