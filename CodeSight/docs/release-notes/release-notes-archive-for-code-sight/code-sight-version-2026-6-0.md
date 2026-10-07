---
title: "Code Sight version 2026.6.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2026.6.0.html"
content_id: "B9zRfJIu41N26rEZsbyqSg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:57.855527+00:00"
---

# Code Sight version 2026.6.0

## Environment variable configuration support

You can now configure environment variables directly in the Code Sight VS Code extension, at three levels:

1. **User level** — Variables applied to all scans across all projects on
   your machine (e.g., `JAVA_HOME`,
   `MAVEN_HOME`).
2. **Project/Workspace level** — Variables applied only to scans within the
   current project or workspace.
3. **Scan configuration level** — Variables applied only when a specific scan
   runs.

When a scan executes, Code Sight merges variables from all levels,
with more specific levels taking precedence (scan config > project > user > OS).
This is particularly useful on macOS and Linux, where IDEs launched from the desktop
may not inherit environment variables from your shell profile.

## Enhancements

Code Sight now supports the following development environments:

- Eclipse 2026-03 (4.39)

## Discontinued Support

Support for the following Black Duck product versions has
been deprecated, and will be discontinued in a future release of :

- **Polaris users:**

  You must upgrade Code Sight to version 2025.4.0 or a later
  version by September 15, 2025. Failure to upgrade will result in an
  inability to interact with Polaris.

  For more information, please see [[ANNOUNCEMENT] Reminder - Polaris API Deprecations and
  Important Due Dates for API and Bridge Upgrade Requirements](https://community.blackduck.com/s/question/0D5Uh00000ix5u5KAA/announcement-reminder-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements).

## See Also

Code Sight Support Matrix

Code Sight Known Issues
