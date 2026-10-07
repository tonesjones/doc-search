---
title: "Code Sight version 2021.5"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2021.5.html"
content_id: "5hZ_8P_1g_uvzkQ9JSJB7g"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.449393+00:00"
---

# Code Sight version 2021.5

## Discontinued support

- End-of-life (EOL): Support for Coverity® 2019.06 has been discontinued.
- End-of-life (EOL): Support for version 2018.2 of the JetBrains IDEs IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm has been
  discontinued.
- End-of-life (EOL): Support for Visual Studio Code 1.48 and 1.49 has been discontinued.
- Support for versions 4.7 and 4.8 of Eclipse has been deprecated, and will be discontinued in a future release of Code Sight.
- Support for Coverity 2019.09 has been deprecated, and will be discontinued in a future release of Code Sight.

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.1 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

## Enhancements

- Version 2021-03 (4.19) of Eclipse is now supported.
- Version 1.55 of Visual Studio Code is now supported.
- For the JetBrains IDEs—IntelliJ IDEA, PhpStorm, PyCharm, RubyMine, and WebStorm—version 2021.1 is
  now the most recently supported version.
- Long-running Black Duck scans now take less time to complete.
  Projects with many dependencies will see greater performance improvement.
- In Eclipse, IntelliJ, and Visual Studio, updated the welcome message to include information about Black Duck.

## Bug fixes

- Fixed an issue in the Scans panel, where sorting any column other than the first one did not work.
  UD-6426
- Code Sight now correctly handles Coverity Connect hosts that strictly require LDAP domains for authentication.
  UD-6739
- In VS Code, the Issue Details view for Coverity (SAST) issues now correctly displays the "How to resolve this issue" section.
  UD-7082
- While running Code Sight in Eclipse 2020.12 on macOS 11 (Big Sur), the Refresh icon now correctly appears in the single-file Scans table.
  UD-7086
- Fixed an issue where the IntelliJ IDE would sometimes hang on startup due to a threading issue.
  UD-7500
