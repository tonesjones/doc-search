---
title: "Code Sight version 2025.10.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.10.0.html"
content_id: "6o_qUA9OYtYVPG9uo4y57A"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.121920+00:00"
---

# Code Sight version 2025.10.0

For Coverity, Code Sight version 2025.10.0 adds support for the Coverity CLI.

## Enhancements

- When you add a new *scan configuration* for Coverity Analysis, you can choose how scan code.
  - If you choose Coverity (.yaml, .json), then Code Sight scans code by using the
    Coverity CLI.

    In this case, it finds configuration settings in a local configuration file, which can be in either YAML or JSON format.

    This enhancement is available in JetBrains IDEs (including IntelliJ), Visual Studio, and VS Code.

    Using the Coverity CLI is now the recommended method.
  - If you choose Coverity (.conf), then Code Sight continues to scan code by using the `cov-run-desktop` command.

    In this case, Code Sight continues to use the legacy configuration file format, coverity.conf.

  Remember:
  Support for scanning a single file is available from Coverity 2024.6.0 onwards.

## Discontinued support

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- **Polaris users:**

  You must upgrade Code Sight to version 2025.4.0 or a later version by September 15, 2025.
  Failure to upgrade will result in an inability to interact with Polaris.

  For more information, please see
  [[ANNOUNCEMENT] Reminder - Polaris API Deprecations and Important Due Dates for API and Bridge Upgrade Requirements](https://community.blackduck.com/s/question/0D5Uh00000ix5u5KAA/announcement-reminder-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements).

## See also

Code Sight Support Matrix

Code Sight Known Issues
