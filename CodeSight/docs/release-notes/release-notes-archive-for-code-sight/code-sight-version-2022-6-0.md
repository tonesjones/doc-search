---
title: "Code Sight version 2022.6.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.6.0.html"
content_id: "CMO22lfpxl_VVv763XZQnA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.819802+00:00"
---

# Code Sight version 2022.6.0

Release 2022.6.0, offers improved proxy support, and in VS Code, the ability to sort SCA issues by impact.
This release also updates support for a number of environments, products, and platforms.

## Enhancements

- Code Sight now supports version 2022 of Visual Studio.
- Code Sight now supports versions 1.66 and 1.67 of VS Code.
- Code Sight now supports Windows 11 and Windows Server 2022.
- Code Sight now recognizes system-level proxy settings such as environment variables, manual settings, and Proxy Auto Configuration (PAC).
- In VS Code, you can now sort SCA issues by impact.
- VS Code now supports single sign-on (SSO) authentication to Black Duck using auth tokens.

## Bug fixes

- In the 2022.4.0 release, we fixed a bug where Code Sight would exclude Win32 from the build configurations.
  UD-8067
- Release 2022.6.0 restores an Export Logs control.
  UD-9333
- Fixed a bug that prevented Sigma full scans from completing under certain circumstances.
  UD-9469

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.2 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

Attention:
Beta support for Android Studio 3.4 has been deprecated, and will be discontinued in a future release of Code Sight.

## Discontinued support

Support for the following product versions has been discontinued:

- Release 2020.1 of the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm)
- Eclipse 4.13 and 4.14
- Visual Studio 2015
- Visual Studio Code 1.61 and 1.62

Support for the following product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Release 2020.2 of the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm)
- Visual Studio Code 1.63 and 1.64

Support for the following Black Duck products has been discontinued:

- Coverity 2020.09

Support for the following Black Duck products has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck 2020.12 through 2021.2
- Coverity 2020.12

Support for the following platform has been deprecated, and will be discontinued in a future release of Code Sight:

- macOS 10.15

## See also

Code Sight Support Matrix

Code Sight Known Issues
