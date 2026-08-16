---
title: "SCMSettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scmsettings.html"
content_id: "LP8PbDgAEUJElGPGDr2mEA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:18.541061+00:00"
---

# SCMSettings

The `SCMSettings` class provides values that correspond to the
`--scm*` arguments to `cov-run-desktop`. It has the
following attributes:

scm?: string
:   Corresponds to `cov-run-desktop --scm`.

tool?: string
:   Corresponds to `cov-run-desktop --scm-tool`.

project_root?: path
:   Corresponds to `cov-run-desktop --scm-project-root`.

tool_args?: string[]
:   Corresponds to `cov-run-desktop --scm-tool-arg`. This accepts a list of
    strings, since this option can be specified multiple times on the command
    line.

command_args?: string[]
:   Corresponds to `cov-run-desktop --scm-command-arg`. This accepts a list of
    strings, since this option can be specified multiple times on the command
    line.
