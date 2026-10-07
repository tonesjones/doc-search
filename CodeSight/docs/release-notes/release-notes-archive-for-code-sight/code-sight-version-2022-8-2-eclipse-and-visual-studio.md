---
title: "Code Sight version 2022.8.2 (Eclipse and Visual Studio)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.8.2-eclipse-and-visual-studio-.html"
content_id: "snQ9Px5dbDhGk0NFCBZEFA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.557787+00:00"
---

# Code Sight version 2022.8.2 (Eclipse and Visual Studio)

Release 2022.8.2 applies to Code Sight in Eclipse and in Visual Studio.
This is a hotfix release that corrects a couple of bugs and disables telemetry.

## Enhancements

- Telemetry has been disabled for Code Sight in Eclipse and Microsoft Visual Studio.

## Bug fixes

- Fixed a bug where Code Sight would not run clean or rebuild the first time it scanned a custom-built command project that had already been built.
  UD-10366
- Fixed a bug where having projects with duplicate file names within the same Solution prevented successful Coverity scans.
  UD-10130
