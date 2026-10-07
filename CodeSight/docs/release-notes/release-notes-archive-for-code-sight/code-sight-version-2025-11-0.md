---
title: "Code Sight version 2025.11.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.11.0.html"
content_id: "wsJXAHViZsRI_9d5FoqnTQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.083455+00:00"
---

# Code Sight version 2025.11.0

## Rapid Scan Static Engine Upgrade

Users can now update the Rapid Scan Static scan engine to the latest version,
starting with Rapid Scan Static 2025.11.0.

## Enhanced Issue Display in VS Code Editor

Users can now filter issues based on the currently active file, with all issue
markers displayed directly in the file editor for easier identification and
resolution in context.

This enhancement applies to:

- Both Auto and Manual scan modes
- Local and Team Views
- Results from Polaris, Coverity Connect, and Black Duck®
  SCA

Additionally, Polaris users can easily identify:

- Issue policy violations in both Local and Team Views
- In Local View, new issues are marked in red, while existing issues are marked
  in purple for clear differentiation

## Local View Support in Eclipse IDE

Code Sight has consolidated the Code Analysis and Open Source Analysis views into a
single Local View in the Eclipse IDE. This feature allows users to view and manage
code security issues directly within Eclipse, similar to the functionality available
in IntelliJ. Users can assess vulnerabilities and compliance directly in their
projects, helping to streamline their workflow.

## Enhancements

- Code Sight now supports the following development environments:

  - Microsoft Visual Studio Code™ 1.104, 1.105

## Bug fixes

- (UD-15549). The error message displayed when a scan fails in both Auto and
  Manual modes in VS Code has been improved for clarity and actionability.
  Users will now receive more helpful guidance on how to address the
  issue.
- (UD-15754). Rapid Scan Static full scan in Manual mode will no longer skip
  hidden files.

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
