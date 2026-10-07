---
title: "Code Sight version 2024.7.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.7.0.html"
content_id: "YusEWcv1TiNi33hOAMA3zg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.700094+00:00"
---

# Code Sight version 2024.7.0

Version 2024.7.0 adds Team View filtering for Coverity Connect issues.
It also adds suipport for some further development environments, the more up to date Coverity CLI to run analysis,
and support for PyCharm in the Standard Edition.

## Enhancements

- For VS Code users, version 2024.7.0 adds the capability to filter Coverity Connect issues in Team View.
  Supported filters include Impact, Status, Action, Classification, Severity, and custom attributes.
- When it runs a local Coverity Analysis scan, Code Sight no longer uses `cov-capture`, which has been deprecated.
  Instead, it now uses Coverity CLI commands to perform the analysis.

  CAUTION:

  If your local Coverity Analysis engine is older than version 2023.6.0, and you have specified extra `cov-build` arguments
  in your coverity.conf file, the scan might fail.

  There are two possible workarounds if this occurs:

  - Downgrade Code Sight to version 2024.6.0.
  - Upgrade your local Coverity Analysis engine to 2023.6.0 or a more recent version.
- The Code Sight Standard Edition now supports Python analysis in the PyCharm IDE.

Code Sight now supports the following development environments:

- Android Studio 2024.1.1
- Eclipse 2024-06 (4.32)
- VS Code 1.90 and 1.91

## Bug fixes

- Fixed an issue in VS Code where trying to run the Help command would fail.
  UD-13815
- Fixed an issue where sometimes when selecting a source for Coverity issues in Team View, not all projects would be loaded from Coverity Connect.
  UD-13233

## Discontinued support

Support for the following development environments has been discontinued:

- VS Code 1.84

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2022-12 (4.26)
- VS Code 1.86

## See also

Code Sight Support Matrix

Code Sight Known Issues
