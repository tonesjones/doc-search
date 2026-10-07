---
title: "Code Sight version 2022.9.0 (JetBrains and VS Code)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2022.9.0-jetbrains-and-vs-code-.html"
content_id: "iSkDG2uk0yafnNdzmytcvg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.609779+00:00"
---

# Code Sight version 2022.9.0 (JetBrains and VS Code)

Release 2022.9.0 applies to Code Sight in the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm) and in Visual Studio Code.

## Enhancements

- Release 2022.9.0 adds support for the Code Sight Standard Edition (CSSE) features to
  the JetBrains IDEs, via free trial or purchase.
  This introduces the support of Rapid Scan Static and Rapid Scan SCA scanning.
  (Rapid Scan Static is also available to Coverity scans.)
- This release also limits automatic scanning to the Rapid Scan Static engine.
  Rapid Scan Static scans can be launched manually as well.

  Coverity static analysis and Black Duck open source scans
  *must* now be launched manually.
- As the VS Code interface already does, the IntelliJ interface now displays separate views for Code Analysis and Open Source Analysis.
  Each of these views contains an icon to launch a new scan.

  In both IntelliJ and VS Code the Scans panel (formerly under the Status view) has been removed.
  From this release on, the results shown in an issues list pertain only to the scan performed most recently.
  If there were problems completing the scan, details of the scan error can be accessed from the issues list.
- For Rapid Scan Static, this release adds support for taint flow analysis, which traces the flow of untrusted data
  through the code in order to identify flows into critical APIs such as those that execute an SQL query,
  read a file from the filesystem, or execute an OS command.
- The performance of Rapid Scan Static when running on the entire code base has been improved.
- Code Sight now supports version 2022.2 of the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm).
- Code Sight now supports VS Code 1.70 and VS Code 1.71.
- Code Sight now supports release 2022.9.0 of Coverity Analysis and Coverity Connect.

## Bug fixes

- Fixed a bug where the proxy server URL would be parsed incorrectly when a manually specified username contained a prohibited character
  (for example, '\') as specified by the RFC Internet standard.
  UD-10147
- Fixed an issue where Code Sight would lose Polaris credentials when reopening an existing project.
  UD-10055
- Code Sight now runs the `clean` command for all custom builds, provided a `clean` command has been specified in
  the project-specific coverity.conf file.
  UD-9803
- Fixed a bug where annotations for an issue were incorrect when the issue had duplicate occurrences.
  UD-9737
- Code Sight Standard Edition now requires a valid license for all supported Code Sight versions.
  UD-9432

## Discontinued support

Support for the following development environment has been discontinued:

- VS Code 1.64

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- JetBrains version 2020.3 (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm)
- VS Code 1.66 and 1.67

Support for the following Black Duck product versions has been discontinued:

- Black Duck 2020.12.0 and 2021.1.0
- Releases 2020.12.0 and 2021.1.0 of Coverity Analysis and Coverity Connect

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck 2021.6.0
- Coverity Analysis and Coverity Connect 2021.3.0

## See also

Code Sight Support Matrix

Code Sight Known Issues
