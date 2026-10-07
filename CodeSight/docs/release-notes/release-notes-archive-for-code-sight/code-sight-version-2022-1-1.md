---
title: "Code Sight version 2022.1.1"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.1.1.html"
content_id: "XoVMnS8Hjbk0WRrSWLnPLg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.065362+00:00"
---

# Code Sight version 2022.1.1

Version 2022.1.1 is a hotfix that fixes a few critical bugs, and adds support for newer JetBrains IDEs.

## Enhancements

- Code Sight now supports version 2021.3 of IntelliJ IDEA and other JetBrains IDEs
  (PhpStorm, PyCharm, RubyMine, and WebStorm).

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.2 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

Attention:
Beta support for Android Studio 3.4 has been deprecated, and will be discontinued in a future release of Code Sight.

## Bug fixes

- Fixed an issue where Code Sight would fail to start within IntelliJ 2021.3.
  UD-8781
- Fixed an issue in which the VS Code extension was creating a log file at the root of the project.
  UD-8849
- In VS Code, we fixed a bug where configured proxy settings were not being used by the Code Sight Standard Edition trial registration.
  UD-8898
