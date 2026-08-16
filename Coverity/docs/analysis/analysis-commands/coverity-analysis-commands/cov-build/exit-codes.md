---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exit-codes.html"
content_id: "PZLoNh7IUbi759d2WJ7hhQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:05.377013+00:00"
---

# Exit codes

By default, `cov-build` returns the exit code from the native build. For
example, if native build command returns `57`,
`cov-build` will return `57`. However, in the case
of invalid arguments, `cov-build` can return `16`, which
can also occur if the native build returns `16`.

If you pass --return-emit-failures to `cov-build`, the return codes
change to match the specified emit failure responses.
