---
title: "Code Sight version 2026.2.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2026.2.0.html"
content_id: "ZAGjWyT6PPtzvR_x2EKIOQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.006399+00:00"
---

# Code Sight version 2026.2.0

## Support Scan Results Export in Code Sight IDE Plugin

The IDE plugin for VS Code now supports saving and exporting scan results for the
following supported scan types: Black Duck SCA, Coverity SAST, and Rapid Scan
Static.

Key Enhancements:

- **Automatic Storage**: The most recent scan results are automatically
  saved as a JSON file within the project's root folder hierarchy.
- **Export Functionality**: Users can export scan results to a location of
  their choice for archiving or sharing.
- **Streamlined Management**: Previous scan results are automatically
  replaced when a new scan is completed, ensuring only the latest findings are
  retained.

## Bug fixes

- (CODESIGHT-11, CODESIGHT-13). Fixed issue for both Coverity
  (`.conf`) and (`.yaml`) scans where the
  scan was failing due to `idir` being set as relative path
  instead of absolute path.

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
