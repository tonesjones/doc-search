---
title: "Analyzing translation units in node_modules"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/analyzing-translation-units-in-node_modules.html"
content_id: "U2wvTzppDbOfQPi06LxIhg"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:49.485454+00:00"
---

# Analyzing translation units in node_modules

The behavior of `cov-analyze` has changed in that translation units in
node_modules directories for JavaScript or TypeScript source are no longer analyzed
unless the new `--analyze-node-modules` option is specified.

Even when using the `--tu` or `--tu-pattern` options, you
must specify the `--analyze-node-modules` option in order to analyze
translation units in node_modules.
