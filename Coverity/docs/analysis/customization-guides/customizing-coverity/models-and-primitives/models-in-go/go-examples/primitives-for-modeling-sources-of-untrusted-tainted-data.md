---
title: "Primitives for modeling sources of untrusted (tainted) data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/primitives-for-modeling-sources-of-untrusted-tainted-data.html"
content_id: "Jcuk_XZ4cI~Wf4PPhhChTA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:51.344555+00:00"
---

# Primitives for modeling sources of untrusted (tainted) data

To model untrusted data sources, you can use the `TaintSource()`
primitive, described in Go security primitives.
`TaintSource()` primitive models a method that returns a string-like
or a simple collection object that the analysis treats as tainted data.

Most taint types can be trusted or distrusted using the
`cov-analyze`
command's `trust` or
`distrust` command-line options; for example,
`--trust-http` and `--distrust-http`. These options
are described in the Coverity 2026.6.0 Command Reference.
