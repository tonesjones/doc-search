---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "AArgLNhwDhsD1ikB4Drkjg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:33.304645+00:00"
---

# Description

The `cov-emit-go` command parses source files and packages and saves
`go build` output to the emit repository in the intermediate
directory.

For code bases that contain CGo dependencies (in other words, Go code that imports the
pseudo-package "C"): Your environment must be configured to successfully compile such
code using the native Go compiler before you execute `cov-emit-go` or
`cov-build` on your code base. This requirement is necessitated
because the `cov-emit-go` command, the Go compiler, and the CGo tool,
must access additional tools to process such code (they execute a C compiler and
generate bindings for the compiled C functions). These same tools execute underneath the
`cov-build` command.

C code that is compiled as part of processing CGo dependencies will not be captured for
analysis by either `cov-build` or `cov-emit-go`.
