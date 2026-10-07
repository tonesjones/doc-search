---
title: "Code Sight version 2024.1.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.1.0.html"
content_id: "F7V28dxxOerUxfXOwTDfMw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.978075+00:00"
---

# Code Sight version 2024.1.0

Code Sight 2024.1.0 adds support for Team View in Visual Studio
and analysis of Kotlin source in Android Studio. It also improves the display of open-source vulnerabilities

## Enhancements

- The Code Sight interface in Visual Studio now supports Team View for displaying remote issues
  reported by Polaris servers.
- Code Sight now supports analysis of Kotlin source in Android Studio, as well as analysis of mixed Kotlin/Java projects.

  Kotlin and Kotlin/Java support have specific setup requirements. See
  Set up Kotlin analysis for Android Studio for details.
- The Issue Details view for Open Source Analysis now shows the associated
  CVE (Common Vulnerabilities and Exposures) number as part of the header, removing the need to expand a particular vulnerability
  to find its associated CVE.

Code Sight now supports the following development environments:

- Eclipse version 2023-12 (4.30)
- Version 2023.3 of the following JetBrains IDEs:
  CLion, IntelliJ IDEA, PhpStorm, PyCharm, RubyMine, and WebStorm
- VS Code 1.84 and 1.85

Code Sight now supports the following platforms:

- macOS 14

## Bug fixes

- In some cases, an Open Source scan would not report the correct path to locate a vulnerable component.
  Code Sight now obtains this information (the file path and line number) from Black Duck®
  Detect, so the component location it displays is reliable.
  UD-12783, UD-9191

  **To obtain this fix:**
  Upgrade to Black Duck®
  Detect 8.11 and Black Duck server 2022.2.

  Note:
  By default, Code Sight displays a single level of dependencies for Black Duck issues.
  You can adjust this level: See “To view duplicate dependencies”.
- Fixed an issue in VS Code 1.82 where Code Sight would sometimes hang after the extension was upgraded.
  UD-12618
- Fixed a bug where validation would sometimes fail when trying to specify a local Rapid Scan Static binary.
  UD-12600
- When using Black Duck®
  Detect 9 and npm 9.8.1, Code Sight now correctly displays line numbers for issue events found in version 3
  package-lock.json files.
  UD-12553

## Discontinued support

Support for the following development environments has been discontinued:

- Version 2021.3 of the following JetBrains IDEs:
  IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm.
- VS Code 1.78 and 1.79

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Version 2022.1 of the following JetBrains development environments:
  IntelliJ, PhpStorm, PyCharm, RubyMine, and Webstorm
- VS Code 1.80 and 1.81

Support for the following platforms has been discontinued:

- macOS 11

## See also

Code Sight Support Matrix

Code Sight Known Issues
