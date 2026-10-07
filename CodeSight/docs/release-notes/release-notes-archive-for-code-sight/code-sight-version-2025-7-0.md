---
title: "Code Sight version 2025.7.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.7.0.html"
content_id: "ulTRXS3Nu2fyYaNs8jo~qA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.238876+00:00"
---

# Code Sight version 2025.7.0

Code Sight version 2025.7.0 increases the level of support for Polaris, and adds support for
a few new development environments.

## Enhancements

- In VS Code, Local View now supports filters for Polaris issues. Users now have the same filter selection
  as in Team View.
- Polaris users can now initiate a Rapid Scan Static scan directly from the Polaris scan configuration
  by supplying the appropriate Bridge arguments.

  This functionality is an early step toward making SAST Rapid scans a fully integrated, first-class option for SAST assessments.

Code Sight now supports the following development environments:

- Android™ Studio 2025.1.1
- Cursor™ 1.0 in VS Code
- GoLand™ 2025.1
- Rider™ 2025.1
- VS Code™ 1.101
- Windsurf™ 1.10

## Bug fixes

- Changing the current project in IntelliJ would sometimes cause Code Sight to hang when loading the list of issues. This has now been fixed.
  UD-15204
- Fixed an issue in IntelliJ where a working directory migration failure notification would show up incorrectly.
  UD-15185

## Discontinued support

Support for the following platform has been deprecated, and will be discontinued in a future release of Code Sight:

- macOS 13

## See also

Code Sight Support Matrix

Code Sight Known Issues
