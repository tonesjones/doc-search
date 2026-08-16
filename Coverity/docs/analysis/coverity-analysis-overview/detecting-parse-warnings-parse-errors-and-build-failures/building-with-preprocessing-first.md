---
title: "Building with preprocessing first"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-with-preprocessing-first.html"
content_id: "7ArqMad6Eqw1lT4Wn3IEmw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:02.887415+00:00"
---

# Building with preprocessing first

Sometimes differences in preprocessed files are very difficult to diagnose or to solve.
In this case, it is possible to tell `cov-build` to preprocess files
with the native compiler and use these preprocessed files to emit code.

To do so, you can either run the `cov-build` command with the
`--preprocess-first` option, or edit your .xml
to add a `<preprocess_first>yes</preprocess_first>` tag in the
`<coverity><config><prevent>` section. If the section does
not exist, create it.
