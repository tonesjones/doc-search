---
title: "Code Sight version 2026.1.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2026.1.0.html"
content_id: "TjOtKbibW1x4EoN3IfJlWQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.044007+00:00"
---

# Code Sight version 2026.1.0

## Added support for Detect 11

Code Sight now supports Detect version 11. This update allows users to integrate the
latest features and improvements from Detect 11 into their workflow. Users can
expect enhanced scanning capabilities and improved vulnerability detection.

## Added Filter Support for Polaris Policy Violations

We are pleased to announce the addition of multi-select functionality for the Policy
Violations filter in both Local and Team Views. This enhancement allows users to
filter issues based on specific policy violations, improving the ability to manage
and triage vulnerabilities effectively.

The new Policy Violations filter has been integrated into the Local and Team
Views for VS Code and IntelliJ IDEs, enabling users to select multiple
policy violation criteria for more precise filtering.

## Expanded Project Type Support in Code Sight for Visual Studio

Code Sight for Visual Studio now supports multiple project types and multi‑folder
workspaces, allowing you to use Code Sight when opening folders and
CMake‑based projects. This enhancement broadens compatibility and improves
flexibility for developers working with diverse project structures.

Please note that this capability is **not available in Visual Studio 2017**.

## Enhancements

- Code Sight now supports the following development environments:

  - Microsoft Visual Studio Code™ 1.108
  - IntelliJ IDEA (and other JetBrains IDEs) 2025.3

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
