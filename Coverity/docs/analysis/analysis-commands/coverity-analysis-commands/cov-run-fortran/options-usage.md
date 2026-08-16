---
title: "Options usage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-usage.html"
content_id: "x98OCX12WfeaKR5AKxLafQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:16.427818+00:00"
---

# Options usage

As shown in the command synopsis, `cov-run-fortran` control options and
analysis options separated by a `--` argument. Control options govern the
operation of `cov-run-fortran` as a whole, while analysis options
govern only the analysis. Analysis options include the names of the source files on
which Coverity Fortran Syntax Analysis operates as well as library file names and
supplementary output file names.

Analysis options may act globally or locally. When listed before any source file name,
the effect of the option is global. It acts upon all of the listed source files unless
explicitly overridden. When specified within the source file list, the effect of an
option is local. It acts only upon the immediately following source file name. Analysis
options can be negated by prefixing the option name with `-n` or
`-no-` option syntax.
