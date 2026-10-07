---
title: "Code Sight version 2024.8.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.8.0.html"
content_id: "2KprEMLzUUoZj46nYpRLqQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.659975+00:00"
---

# Code Sight version 2024.8.0

Enhancements for Code Sight 2024.8.0 include the ability to filter Software Risk Manager issues in Team View for VS Code.

## Enhancements

- For VS Code users, Code Sight 2024.8.0 adds the capability to filter Software Risk Manager issues in Team View.
  Supported filters include Assignee, Policy Violations, Triage Status, Severity,
  Finding ID, and Tool.

  Filters are available for Software Risk Manager 2024.3.0 and later releases.
- Code Sight 2024.8.0 makes some changes to the Coverity Connect issue filters in Team View for VS Code.

  **Filters that are in:**

  - **Filtering by CID**

    You have to type in full CID values, but you can also input multiple CIDs by separating each value with a comma ( `,` ).
  - **Filtering by Custom Filters of text type**

    This filter requires an exact string-matching string. But this filter is also affected by the permissions bug that affected the last Coverity Connect filters release.
    (You must have admin-level access to see the triage attributes: See the known issue for UD-13886.)

  **Filters that are no longer included:**

  - Owner name

Code Sight now supports the following development environments:

- VS Code 1.92

## Bug fixes

- For Coverity scans, Code Sight performs the capture step using `cov-capture` via `cov-run-desktop`, once again.
  Changes to perform this step using the Coverity CLI (command-line interface), introduced in the 2024.7.0 release, have been rolled back until future notice.

## Discontinued support

Support for the following development environments has been discontinued:

- VS Code 1.85

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- VS Code 1.87

## See also

Code Sight Support Matrix

Code Sight Known Issues
