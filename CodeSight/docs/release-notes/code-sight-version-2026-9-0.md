---
title: "Code Sight version 2026.9.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2026.9.0.html"
content_id: "iwNF56y6wypcYu7hhhLKWA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:57.574223+00:00"
---

# Code Sight version 2026.9.0

## Coverity Scan Comparison ("New vs. Existing" Issues) in Local View

Code Sight now supports scan result comparison for Coverity Connect
in the Local View, aligning with existing Polaris comparison functionality.
Developers can use the new Compare with option in the Local View to select a target
Coverity Connect project and stream as a baseline server snapshot.

**IDEs Supported**: Visual Studio, VS Code

**Key Benefits:**

- **Issue Status Indicators**: Easily identify newly introduced local issues
  (**New**) versus issues already recorded on the server
  (**Existing**).
- **View Filtering**: Filter the Local View by **All**, **New**, or
  **Existing** to focus exclusively on local code changes and avoid
  working on previously triaged items.
- **Configuration Isolation**: Target stream selections and filter states
  are saved per scan configuration, ensuring settings remain isolated across
  different project contexts.

## End of support for macOS 14

Support for macOS 14 (Sonoma) has reached End of Life (EOL) for Code Sight plugins
across supported IDEs, including Eclipse, IntelliJ IDEA, and Visual Studio Code.
Users are advised to upgrade to a supported operating system version to maintain
compatibility with future Code Sight plugin releases. For a complete list of
supported operating systems and IDE environments, refer to the Code Sight Support Matrix.

## Enhancements

Code Sight now supports the following development environments:

- VSCode 1.137

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
