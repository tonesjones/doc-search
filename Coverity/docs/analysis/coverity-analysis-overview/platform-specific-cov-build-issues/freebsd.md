---
title: "FreeBSD"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/freebsd.html"
content_id: "a5CDJFfeDkFpPzVzWeQkBw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:11.341522+00:00"
---

# FreeBSD

Many versions of FreeBSD have a statically linked `sh` and
`make`. The `cov-build` command relies on intercepting
`exec()` at the shared library level and cannot intercept compiler
invocations from static build programs such as `sh` and
`make`. The solution is to change the
<`comp_name`> variable in the `coverity_config.xml`
file to recognize `cc1` as the compiler. This works because
`gcc` is usually not statically linked, and `gcc` is a
driver program that calls `cc1` to actually perform the compile. Some
features of `cov-build`, such as automatic preprocessing of files to
diagnose compile errors, might not work in such case.
