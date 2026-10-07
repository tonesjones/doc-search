---
title: "Code Sight version 2024.5.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.5.0.html"
content_id: "2EChbXxT6tVdtLDJgHAQzA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.785876+00:00"
---

# Code Sight version 2024.5.0

This release adds support for some new development environments, and
fixes some bugs in order to improve user experience.

## Enhancements

Code Sight now supports the following language:

- C# (.NET) source in the Code Sight Standard Edition

Code Sight now supports the following development environments:

- Android Studio 2023.3.1
- VS Code 1.89

## Bug fixes

- Fixed a bug in the Visual Studio extension where hovering over the Location field in the Open Source Analysis
  view did not show the full location path.
  UD-13505
- Fixed an issue where Code Sight was unable to determine whether a particular URL pointed at Coverity Connect,
  when proxy systems were between the Code Sight and Coverity Connect systems.
  UD-13426

## Discontinued support

Support for the following development environments has been discontinued:

- VS Code 1.83

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2022-09 (4.25)
- VS Code 1.84

## See also

Code Sight Support Matrix

Code Sight Known Issues
