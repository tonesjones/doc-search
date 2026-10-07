---
title: "Code Sight version 2025.9.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.9.0.html"
content_id: "MnB9QPh4OMis_0L7royDNQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.158460+00:00"
---

# Code Sight version 2025.9.0

Version 2025.9.0 adds Local View support and improved Polaris support to Visual Studio.
For VS Code, it adds an improvement to the LOCAL VIEW display, and moves the control to turn on analyzing while you type.

## Enhancements

- In Visual Studio, the Code Analysis and Open Source Analysis views are
  now consolidated into a single Local View, which displays results of scans run locally.
  The scans themselves can be of various types, and are managed using a new *scan configuration* interface.
- In the VS Code LOCAL VIEW, while Automatic Scan mode is active, results for Code Analysis (Rapid Scan)
  are now grouped into two categories: Secrets and Vulnerabilities.
  All issues related to hardcoded secrets in the code base are now grouped under Secrets.
  All other issue types are now grouped under Vulnerabilities.
- In VS Code, the Automatic Scan option for analyzing code while you type has moved to the Automatic Scan Configuration tab.
  The UI no longer has a Rapid Scan Static Configuration tab.
- In Visual Studio, you can install Rapid Scan Static to perform static application security testing (SAST) locally.
  Once Polaris has been authenticated and Rapid Scan Static has been installed, you can run scans either manually or automatically.
  The controls for local scanning, and the results of a local scan, appear in Local View.

## Bug fixes

- When running a Black Duck SCA scan, the scan engine was trying to download dependencies by connecting to
  bd-repo.blackduck.com.
  Since all dependencies are already included, no download should have been performed. This has now been fixed.
  UD-15487

## Discontinued support

Support for the following platforms has been discontinued:

- macOS 13
- Windows 10

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- **Polaris users:**

  You must upgrade Code Sight to version 2025.4.0 or a later version by September 15, 2025.
  Failure to upgrade will result in an inability to interact with Polaris.

  For more information, please see
  [[ANNOUNCEMENT] Reminder - Polaris API Deprecations and Important Due Dates for API and Bridge Upgrade Requirements](https://community.blackduck.com/s/question/0D5Uh00000ix5u5KAA/announcement-reminder-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements).

## See also

Code Sight Support Matrix

Code Sight Known Issues
