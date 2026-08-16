---
title: "Testing hypotheses"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/testing-hypotheses.html"
content_id: "jiFH9O1vZ_yzYkb8tCtl4w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:03.544032+00:00"
---

# Testing hypotheses

It is often useful to perform small experiments to determine the root cause of parse
errors. For example, copy the original source file into a temporary file and add the
identifiers to macros whose value you wish to test at the end of the temporary file.
Next, preprocess the temporary file and look at the expansion of the macros.

Another useful method is to reduce a preprocessed source file while preserving the parse
error. If a small enough example can be generated this way, it might be possible to send
Coverity an example that exhibits the problem. This greatly increases the chances that
Coverity is able to find a workaround for the problem in a timely manner.
