---
title: "Import SCM configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/import-scm-configuration.html"
content_id: "OpE0SbEH~doKQe56WjICsA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:03.989507+00:00"
---

# Import SCM configuration

Use the following keys to specify how to import data about source file changes from the source control management (SCM) system
that you use.

| Key | Type | Description |
| --- | --- | --- |
| `cov-import-scm-args` | array of strings | (Optional) Additional arguments to pass to the `cov-import-scm` command following a capture. |
| `filenanme-regex` | string | (Optional) A regular expression that specifies the set of files for which to import change information. Default: Include all source files |
| `ms-delay` | integer | (Optional) Sets a delay in milliseconds between calls to the underlying SCM. Default: No delay |
| `scm` | string | (Required) The name of the source control management system being used. |
