---
title: "Shared command options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/shared-command-options.html"
content_id: "gyATELzKut~14MzEIdVTXA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:59.387194+00:00"
---

# Shared command options

Each of the Coverity CLI commands can be preceded by certain shared
options that modify the command's behavior. The syntax of a command that uses a shared
option is as follows:

[`shared-options`] `command`
[`command-specific-options`]

For example, the following option adds debug messages to the output for the scan:

```
coverity --verbose scan --project-dir my-project
```

The following table describes the shared options.

|  |  |
| --- | --- |
| `-h, --help` | Display help for the specified command. |
| `--machine-readable-output` | Use machine-readable output, useful for CICD. |
| `-q, --quiet` | Display only error messages. |
| `--ticker-mode` | Sets the style of the ticker displayed during processing. Must be one of `"none"`, `"no-spin"`, or `"spin"`. Default: `"spin"`. |
| `-V, --verbose` | Add debug messages to provide the highest level of detail possible. |
| `-v, --version` | Display version. |
