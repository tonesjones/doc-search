---
title: "Buildless capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/buildless-capture.html"
content_id: "g2WKj2aFoC1xvh6SA7HoZg"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:49.528367+00:00"
---

# Buildless capture

The `--dir` option to the `cov-capture` command was
previously optional but is now required. This option specifies the location of the
intermediate directory. You must ensure that all calls to `cov-capture`
include this option.

The `--dot-coverity-location` option to the `cov-capture`
command is no longer supported. If you currently use this option to specify a location
for diagnostics and related data for `cov-capture`, you must remove it.
The diagnostic directory is now always created in the intermediate directory and is
called `cov-capture`.
