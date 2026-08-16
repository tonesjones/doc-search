---
title: "ExtendDirectories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/extenddirectories.html"
content_id: "Wubm2l7SVVOO36qCQHaUFQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:27.639706+00:00"
---

# ExtendDirectories

The `ExtendDirectories` class allows users to run Extend SDK checkers during the
`cov-run-desktop` analysis. It has the following attributes:

version?: string
:   A version number which the custom checker works with; this value matches
    the version specified in the `KnownInstallation` object.
    During evaluation, custom checkers defined for a version other than the
    effective value of the $(version) variable are ignored. If this value is
    omitted, the checker is assumed to be compatible with the current version of
    the tools.

platform?: string
:   The platform which the custom checker works with; this value matches
    the platform specified in a `KnownInstallation` object.
    During evaluation, custom checkers defined for a platform other than the
    effective value of the `$(platform)` variable are ignored. If
    this value is omitted, the checker is assumed to be compatible with the
    current platform.

directory?: path
:   A directory containing the custom checker executables.

checkers?: string[]
:   The names of custom checkers. These names will be equivalent to the
    executable names, but without the executable file extension.

An example of using extend_directories is:

```
{
  // other settings...
  "extend_directories": [
    {
      "version": "$(version)",
      "platform": "$(platform)",
      "directory": "$(install_dir)/bin/sdk",
      "checkers": [
        "CUSTOM_CHECKER_A",
        "CUSTOM_CHECKER_B"
      ]
    }
  ]
}
```
