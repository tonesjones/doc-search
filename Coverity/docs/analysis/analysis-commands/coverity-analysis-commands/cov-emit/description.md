---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "eBqYuq6xO0tdSnQTJw2Vhg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:25.899939+00:00"
---

# Description

The `cov-emit` command parses a source file and outputs it into a
directory (emit repository) that can later be analyzed with
`cov-analyze`. The `cov-emit` command is typically
called by `cov-translate`, which is in turn typically called by
`cov-build` (`cov-emit` is a low-level command and
is not normally called directly). The `cov-emit` command defines the
__COVERITY__ preprocessor symbol.
