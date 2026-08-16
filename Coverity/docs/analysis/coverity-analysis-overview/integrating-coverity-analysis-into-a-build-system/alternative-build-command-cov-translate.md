---
title: "Alternative build command: 'cov-translate'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/alternative-build-command-cov-translate-.html"
content_id: "eVVtpXIAi1iHcnOATdASBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:12.620555+00:00"
---

# Alternative build command: 'cov-translate'

The `cov-translate` command translates native compiler command-line
arguments to arguments appropriate for the Coverity compiler, and then calls the
compiler with the `cov-emit` command. If you use
`cov-build` to integrate with the build, there is no need to deal
explicitly with `cov-translate`. All of the options that control how
`cov-translate` works are in the
coverity_config.xml file. You can specify the intermediate
directory, with an emit repository, on the `cov-translate` command line
using the `--dir` option.

To perform manual integration with a build system, the build system needs to be modified
to have an additional target that calls `cov-translate` instead of the
usual compiler. For more information, see Figure 3.
