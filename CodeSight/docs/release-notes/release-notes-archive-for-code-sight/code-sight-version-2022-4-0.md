---
title: "Code Sight version 2022.4.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.4.0.html"
content_id: "FA8tKx~4qCcq4JCdaUuFsQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.974135+00:00"
---

# Code Sight version 2022.4.0

With release 2022.4.0, Code Sight introduces full Black Duck support to the Visual Studio Code environment.
This release also updates support for a number of environments, products, and platforms.

## Discontinued support

Support for the following product versions has been discontinued:

- Eclipse versions 4.10 through 4.12
- Visual Studio Code versions 1.58 through 1.60

Support for the following product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Visual Studio version 2015
- Visual Studio Code versions 1.61 and 1.62

Support for the following Black Duck products has been discontinued:

- Black Duck 2020.06 through Black Duck 2020.10.
- Coverity 2020.06

Support for the following Black Duck products has been deprecated, and will be discontinued in a future release of Code Sight:

- Coverity 2020.09

Support for the following platform has been discontinued:

- macOS 10.14

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.2 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

Attention:
Beta support for Android Studio 3.4 has been deprecated, and will be discontinued in a future release of Code Sight.

## Enhancements

- In VS Code, Code Sight now supports connecting to a hosted Black Duck server.
- Version 2022.4.0 adds support for the following Black Duck products:
  - Black Duck 2022.2.0
  - Coverity Analysis and Coverity Connect 2022.3.0
- Version 2022.4.0 adds support for the following development environments:
  - Eclipse version 2022-03 (4.23)
  - Version 2022.1 of the JetBrains environments (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm)
  - Visual Studio Code versions 1.64 and 1.65
- Version 2022.4.0 adds support for the following operating system:
  - macOS 12

## Bug fixes

- If Coverity Analysis tools were not available on the server, Code Sight used to treat this case as an error. Code Sight now handles it as a warning to the user.
  UD-8463
