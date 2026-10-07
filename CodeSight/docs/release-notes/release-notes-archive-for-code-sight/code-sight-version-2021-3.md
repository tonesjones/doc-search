---
title: "Code Sight version 2021.3"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2021.3.html"
content_id: "qbOO66EBs2pJeObsttmTdA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.513005+00:00"
---

# Code Sight version 2021.3

## Discontinued support

- End-of-life (EOL): Support for macOS® 10.13 has been discontinued.
- Support for Coverity 2019.06 has been deprecated, and will be discontinued
  in a future release of Code Sight.
- Support for VS Code 1.48 and 1.49 has been deprecated, and will be discontinued
  in a future release of Code Sight.
- Support for version 2018.2 of the JetBrains IDEs IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm has been
  deprecated. In a future release of Code Sight, 2019.1 will become the earliest supported version for this family
  of IDEs.

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.1 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

## Enhancements

- In the Code Sight extension for Microsoft Visual Studio, Black Duck is now enabled by default.
- VS Code versions 1.53 and 1.54 are now supported.
- Version 11 of macOS is now a supported platform.

  Attention:
  On macOS 11, the Eclipse Foundation does not support versions of the Eclipse IDE prior to 2020-12 (4.18).
- For Black Duck scans, Code Sight now uses the build tool or package manager path that is saved in the IDE Preferences.
- Code Sight now downloads the Black Duck®
  Detect tool, used to run Black Duck (SCA) scans,
  from the Hosting location URL specified on the client’s Black Duck System Setting web page.

## Bug fixes

- When dismissing a Coverity issue while connected to Polaris,
  the maximum length of the comment you can enter has been increased to 1,000 characters.
  UD-3539
- Fixed a bug where changes to the automatic scanning state would incorrectly hide both previously detected issues,
  and previously run scans, until the corresponding tables were updated.
  UD-6758
- Fixed a bug where, in the VS Code Editor, the Code Sight extension would incorrectly move a static analysis issue message to a wrong line
  when the code was modified.
  UD-6824
- Code Sight now correctly handles Coverity Connect hosts that use a context root: that is,
  a local subdirectory—for example, whose address has the format https://www.example.com/coverity.
  UD-6877
