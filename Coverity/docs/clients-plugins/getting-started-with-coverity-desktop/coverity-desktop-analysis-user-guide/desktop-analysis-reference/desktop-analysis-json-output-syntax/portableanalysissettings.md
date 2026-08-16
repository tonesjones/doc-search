---
title: "PortableAnalysisSettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/portableanalysissettings.html"
content_id: "HUU9YgL8R3_h_ww3fj4~9g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:11.051758+00:00"
---

# PortableAnalysisSettings

This object contains the "portable" analysis settings for the current invocation of
`cov-run-desktop`.

coding_standard_configs: string
:   The contents of the file passed to
    `--coding_standard_configs`, if any.

covAnalyzeArgs: [string]
:   A sequence of `cov-analyze` command line arguments.

fileCheckerOptions: FileCheckerOption
:   The contents of the argument file to checker options that specify
    files.

fbExcludeConfigurations: string
:   A sequence of the contents of files passed to `--fb-exclude`,
    if any.

fbIncludeConfigurations: string
:   The contents of the file passed to `--fb-include`, if
    any.
