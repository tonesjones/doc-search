---
title: "Code Sight version 2023.6.0 (Eclipse, JetBrains, and VS Code)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.6.0-eclipse-jetbrains-and-vs-code-.html"
content_id: "8M~XdaaMJ_R0LibDVsGCiA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.253740+00:00"
---

# Code Sight version 2023.6.0 (Eclipse, JetBrains, and VS Code)

Version 2023.6.0 includes enhancements to the authentication process.
For static analysis, it improves the handling of scan summaries, adds the checker name to issue details,
and makes issues searchable by checker name.

## Enhancements

- For all development environments (IDEs) and all scan engines, Code Sight now saves authentication at the user level, so you don’t have to authenticate
  again when you change context: For example, when you switch to a different IDE or open a new source-code project to scan.
- While connected to a server, Code Analysis (static analysis) now checks the summaries for every scan, and downloads the summaries if necessary.
  This improves the accuracy of results, at a slight cost in performance.
- For Code Analysis (static analysis) issues, the Details view now displays the name of the checker that detected the issue.

  If the checker is a coding-standard issue, the Details view also displays the number of the rule that was violated.
- In the Code Analysis (static analysis) view, you can now search issues by checker name.
  This added capability is especially useful when working with compliance issues; for example, finding a MISRA rule or directive.
- Code Sight can now use the `id` property when this is specified for the `reference_snapshot` field
  of the coverity.conf file.

  For more information about coverity.conf options, please see the *Coverity Desktop Analysis User Guide*.
- Code Sight help is now published in a different format on a different server, and links from the plug-in or extension interface to that help
  have been updated accordingly.

Code Sight now supports the following development environments:

- JetBrains version 2023.1, including IntelliJ
- VS Code 1.77 and 1.78

Code Sight now supports the following Black Duck product versions:

- Coverity Analysis and Coverity Connect 2023.6.0

## Bug fixes

- Fixed an issue in IntelliJ where Code Sight was causing an erroneous language server client warning.
  UD-11680

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 2021-03 (4.19) – 2021-06 (4.20)
- Visual Studio Code 1.70–1.71

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2021-09 (4.21)
- VS Code 1.72–1.74

Support for the following Black Duck product versions has been discontinued:

- Coverity Analysis and Coverity Connect 2021.9.0

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck 2021.10
- Coverity Analysis and Coverity Connect 2021.12.0

## See also

Code Sight Support Matrix

Code Sight Known Issues
