---
title: "Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis.html"
content_id: "HHAzfk~Tnf86qPdMHTUl4g"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:50.869607+00:00"
---

# Coverity Analysis

## Coverity primitives in Go

The module path for Coverity primitives in Go has been updated from
`synopsys.com/coverity-primitives` to
`blackduck.com/coverity-primitives`.

This is a breaking change: Source code that currently contains import statements such
as

`import . "synopsys.com/coverity-primitives"`

must be updated to read

`import . "blackduck.com/coverity-primitives"`

instead.

This is a legal requirement, therefore it cannot be avoided or mitigated.

## Coverity capture

Buildless capture and filesystem capture have been discontinued. The
`cov-capture` binaries and the related options for
`cov-build` have been removed from Coverity. To analyze the
source of a compiled language, you can use `cov-build`. To analyze
source that is not compiled, such as scripts or an interpreted language, use
`coverity capture` in the Command Line Interface (CLI).
