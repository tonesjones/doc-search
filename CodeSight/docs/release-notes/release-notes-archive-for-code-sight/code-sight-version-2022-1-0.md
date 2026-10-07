---
title: "Code Sight version 2022.1.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.1.0.html"
content_id: "i~0db1EZ10WEoqDZyrizWw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.142707+00:00"
---

# Code Sight version 2022.1.0

Release 2022.1.0 introduces the Code Sight Standard Edition, a version of Code Sight for Microsoft Visual Studio Code
that configures quickly, runs quickly, and adds Software Composition Analysis (SCA) to the VS Code editor.

Code Sight for VS code and for the other development environments continues to support the legacy
SAST and SCA scan engines, and is free to customers who subscribe to Coverity (SAST), Black Duck (SCA), or both.

## Discontinued support

Support for the following product versions has been discontinued:

- Eclipse 4.8 (Photon) and 4.9 (2018-09)
- Version 2019.3 of the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine and Webstorm)
- VS Code 1.52–1.57
- Windows 8.1

Support for the following product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 4.10 (2018-12) through 4.14 (2019-12)
- Version 2020.1 of the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine and Webstorm)
- VS Code 1.58–1.60

Support for the following Black Duck products has been discontinued:

- Coverity Analysis and Coverity Connect 2020.03.

Support for the following Black Duck products has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck (SCA) 2020.06 through 2020.10.
- Coverity Analysis and Coverity Connect 2020.06.

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.2 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

Attention:
Beta support for Android Studio 3.4 has been deprecated, and will be discontinued in a future release of Code Sight.

## Enhancements

- Code Sight in VS Code now provides the Code Sight Standard Edition, which not only supports
  Rapid Scan Static (Sigma) scanning, as in the 2021.8.x versions, but introduces Rapid Scan SCA scanning
  so VS Code users can assess the security of open source components in their code base.
- Code Sight now supports versions 4.21 (2021-09) and 4.22 (2021-12) of Eclipse.
- Code Sight now supports version 2021.2 of IntelliJ IDEA and other JetBrains IDEs
  (PhpStorm, PyCharm, RubyMine, and WebStorm).
- Code Sight now supports versions 1.59 through 1.63 of Microsoft Visual Studio Code.

## Bug fixes

- Fixed a bug where canceling a full Black Duck (SCA) scan wouldn’t work.
  UD-7928
- Corrected filter behavior in VS Code. Turning off the Coverity filter now turns off all sub-filters associated with that engine as well.
  Similarly, turning on one of the sub-filters for Coverity now turns on the Coverity filter as well.
  UD-8136
- For projects in Polaris, Code Sight now uses the same project-name resolution method as Polaris does.
  UD-8264
- When using older versions of Coverity Analysis, scanning would sometimes fail due to a crash during compilation.
  The Coverity Analysis 2021.12.0 release has now fixed this issue.
  UD-8345
- Installing Code Sight Eclipse to an air-gapped system would fail because of the inability to download unrelated dependencies.
  Now, users can choose to install C/C++ support without installing Java support, and *vice versa*.
  UD-3674, UD-8407
- Specifying too long a path for the intermediate directory (idir) would cause files not to be captured.
  Code Sight now compresses the path length to avoid this issue.
  UD-8506, UD-8623, UD-8754
- Sigma processes weren’t being properly terminated on exit from VS Code. This has now been fixed.
  UD-8762

  Important:
  If you run Code Sight in VS Code and you are upgrading from Code Sight version 2021.8.0 or 2021.8.1, please see
  these upgrade instructions.
