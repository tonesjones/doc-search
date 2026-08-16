---
title: "Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis.html"
content_id: "DvI9wP~VjBrhGITFh~NEiA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:39.347257+00:00"
---

# Coverity Analysis

Users of Test Advisor and Dynamic Analysis who do test capture with
`cov-capture` must change their command lines to use
`cov-build --test-capture`. The tool `cov-capture`
has been replaced in this release with a new tool that captures source code without
wrapping a build.
