---
title: "Code Sight version 2022.8.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.8.0.html"
content_id: "36sUAr1dHEM4YGZP8VgNmQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.706274+00:00"
---

# Code Sight version 2022.8.0

Release 2022.8.0 adds support for a few new product versions and corrects a few bugs.

## Enhancements

- Code Sight now supports Coverity 2022.6.0.
- Code Sight now supports Black Duck 2022.7.0.
- Code Sight now supports Eclipse 2022-06 (4.24).
- Code Sight now supports VS Code 1.68 and 1.69.
- This release of Code Sight adds support for the upcoming 2022.8.2 Rapid Scan Static (Sigma) release.

## Bug fixes

- When a workspace was opened in VS Code on Windows, manually triggered single-file Coverity scans would sometimes fail.
  Scans did succeed when automatically triggered by opening or saving a file: Now manually triggered scans work as well.
  UD-9847
- Fixed a bug where Code Sight was not using the Maven home directory configured in the IntelliJ preferences.
  UD-9503
- Fixed an issue where projects with cyclic dependencies would cause Rapid Scan SCA scans to run indefinitely.
  UD-9477

## Discontinued support

Support for the following product versions has been discontinued:

- Visual Studio Code 1.63

Support for the following product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Visual Studio Code 1.64 and 1.65

Support for the following Black Duck products has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck 2021.4.0

## See also

Code Sight Support Matrix

Code Sight Known Issues
