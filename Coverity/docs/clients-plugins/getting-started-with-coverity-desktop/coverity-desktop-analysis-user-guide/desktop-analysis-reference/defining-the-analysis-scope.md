---
title: "Defining the analysis scope"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defining-the-analysis-scope.html"
content_id: "uBRVTos0AH1zhj8y57korQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:57.068648+00:00"
---

# Defining the analysis scope

The group of files specified for analysis by `cov-run-desktop` is known as the
analysis scope. This can be specified explicitly (by passing the files to the
`cov-run-desktop` command line), determined by querying your SCM
(using the `--analyze-scm-modified` option), or by using the source
captured from previous builds (using the `--analyze-captured-source`
option).

By default, Desktop Analysis does not return any defects found in files outside of the analysis
scope. This means that, unless directly specified, defects in headers and other
non-primary source files will not be found by `cov-run-desktop`.
Additionally, previously detected defects in such files will be suppressed in the
`cov-run-desktop` output. This behavior can be disabled by setting
the `cov-run-desktop --confine-to-scope` option to
`false` (see the `cov-run-desktop`
description in the Coverity 2026.6.0 Command Reference for details).

As an example of `--confine-to-scope`, the command line `cov-run-desktop
test.c` reports defects in test.c but not in the
headers it might include. The command line `cov-run-desktop --confine-to-scope
false test.c` reports defects in test.c
*and in* its headers.
