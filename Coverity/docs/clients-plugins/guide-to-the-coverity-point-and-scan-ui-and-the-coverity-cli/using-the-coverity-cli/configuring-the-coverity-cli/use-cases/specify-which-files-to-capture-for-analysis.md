---
title: "Specify which files to capture for analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-which-files-to-capture-for-analysis.html"
content_id: "aoNVAelTTIxfA8cpzfSCIg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:52.904430+00:00"
---

# Specify which files to capture for analysis

The Coverity CLI allows you to fine-tune which files are captured for analysis.
This is primarily controlled through two `coverity capture` configuration options:

- `languages`

  Specify which programming languages to include or exclude.
- `files`

  Uses patterns to identify specific files or directories to include or exclude.

See also Capture configuration.

Note:
Prior to Coverity 2025.6.0, the `files` option only applied to languages captured via buildless capture.
As of Coverity 2025.9.0, the `files` option applies to languages captured via both build capture *and* buildless capture.
A key implication of this change is that the set of default exclusions that only applied to files captured via buildless capture now also applies to build capture;
that is, the default exclusions apply irrespective of how the file was captured.
