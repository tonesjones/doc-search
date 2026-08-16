---
title: "Sigma analysis engine platform requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sigma-analysis-engine-platform-requirements.html"
content_id: "auHwOhOq1o8jDQEf5bqZMg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:22.339134+00:00"
---

# Sigma analysis engine platform requirements

If you intend to use Sigma checkers, ensure that your Coverity Analysis host platform
supports Sigma-based analysis. A new column named "Sigma-based analysis" has been added
to the relevant platform support tables in the Supported platforms
chapter. The new column indicates which platforms support Sigma checkers.

Note, in particular, that the minimum `glibc` requirement on Linux has been
incremented from 2.17 to 2.18. The Sigma analysis engine will be disabled if this
requirement is not met.
