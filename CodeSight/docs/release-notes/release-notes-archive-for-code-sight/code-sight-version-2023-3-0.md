---
title: "Code Sight version 2023.3.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.3.0.html"
content_id: "lWSls_O8tCQ9oakXPe~j8Q"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.423151+00:00"
---

# Code Sight version 2023.3.0

Release 2023.3.0 includes feature changes to Code Sight in the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm) and in Visual Studio Code.
It does not include feature changes to Code Sight in Eclipse or Visual Studio, except for some updates to IDE version support.

In Visual Studio Code, static-analysis issue details now appear in their own view (rather than a pop-up), to improve readability
and better parallel the IntelliJ interface.

## Enhancements

In VS Code, the details of Code Analysis issues are now displayed in their own view, as they are for Open Source Analysis.
The drop-down that appears when you hover over highlighted code in the Editor has been updated to mimic the model set by the other IDEs.
The new Details view also has the ability to show eLearning links.

As of IntelliJ 2022.2, Code Sight can run Open Source scans by using the EMBEDDED run-time Maven.

Code Sight now supports the following development environments:

- Eclipse 2022-12 (4.26)
- VS Code 1.74

Code Sight now supports the following Black Duck product versions:

- Black Duck 2023.1
- Coverity Analysis and Coverity Connect 2023.3.0.

## Bug fixes

- Fixed an issue where certain newer license validation codes were not handled correctly.
  UD-11263
- Fixed a link in the VS Code Marketplace that was pointing to nothing when it needed to point to the Coverity quick tour.
  UD-11154
- Fixed a problem where a Coverity local full scan was finding significantly fewer issues than the results found by the central scan in the remote server.
  UD-11004
- Fixed an issue for Code Sight in IntelliJ where the IDE would hang when Rapid Scan Static (Sigma) was installed.
  UD-10725

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 2020-03 (4.15), 2020-06 (4.16), 2020-09 (4.17), and 2020-12 (4.18)
- Visual Studio Code 1.68

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2021-03 (4.19) and 2021-06 (4.20)
- Visual Studio 2017

Support for the following Black Duck product versions has been discontinued:

- Black Duck 2021.4 and 2021.6
- Coverity Analysis and Coverity Connect 2021.06

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck 2021.8
- Detect versions 6.1–7.3
- Coverity Analysis and Coverity Connect 2021.9

## See also

Code Sight Support Matrix

Code Sight Known Issues
