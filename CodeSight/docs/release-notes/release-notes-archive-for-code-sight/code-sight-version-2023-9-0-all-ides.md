---
title: "Code Sight version 2023.9.0 (all IDEs)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.9.0-all-ides-.html"
content_id: "YrtEd397y1KdkiYr6VaL7Q"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.137101+00:00"
---

# Code Sight version 2023.9.0 (all IDEs)

In addition to bug fixes and performance improvements, Code Sight version 2023.9.0 integrates
Microsoft® Visual Studio® into the Code Sight Standard Edition.
The interface for Visual Studio now conforms more closely to the interface for other supported IDEs.

## Enhancements

A number of enhancements bring Code Sight in Visual Studio into parity with how Code Sight runs within the IntelliJ, Eclipse, and VS Code IDEs.

- The Visual Studio development environment is now incorporated in the Code Sight Standard Edition (CSSE).

  As with IntelliJ and other JetBrains IDEs, Eclipse, and VS Code, you can now configure the locations of the Rapid Scan tools to run.
- In Visual Studio, Code Sight now displays separate panels for Code Analysis and Open Source analysis. These new panels let you launch scans yourself;
  for Code Analysis, you can also choose to launch scans automatically.

  The Scans panel, formerly under the Status view, has been removed. The results shown in an issues list pertain only to the scan performed most recently.
- For Visual Studio, while connected to a server, Code Analysis (static analysis) now checks the summaries for every scan, and downloads the summaries if necessary.
  This improves the accuracy of results, at a slight cost in performance.
- In the Code Analysis (static analysis) view for Visual Studio, you can now search issues by checker name. This added capability is especially useful when working with compliance issues;
  for example, finding a MISRA rule or directive.
- Visual Studio now supports connections to servers that use self-signed certificates.
- For Visual Studio, this release of Code Sight adds support for Black Duck®
  Detect 8, a major upgrade.
- For Visual Studio, Code Sight now saves authentication at the user level, so you don’t have to authenticate again when you change context
  (that is, when you switch to a different IDE or open a new source-code project to scan).
- In Visual Studio, Code Sight can now use the `id` property when this is specified for the `reference_snapshot`
  field of the coverity.conf file.
  For more information about coverity.conf options, please see the *Coverity Desktop Analysis User Guide*.
- For each manual scan run in Visual Studio, all the commands that are executed for a scan are saved in real time to a log file.
  For each command that is executed, the log saves the working directory, command line, standard output, standard error, and exit code of the command.
  This information is available in the file you can download by clicking Export Logs.
  It is also available via the Scan Details message that appears while a scan is running and after the scan completes.

Significantly reduced the impact of Code Sight on the Visual Studio startup time. Users might see the startup time reduced by more than 50 percent.

Code Sight now supports Visual Studio 2017 and Visual Studio 2019 via two separate extension versions.
Users need to install the version of Code Sight that matches the version of Visual Studio that they run.

Code Sight can now run the Rapid Scan engines using macOS for Apple silicon platforms.

This release adds support for selecting a *branch* when you configure a source for issues reported by Polaris.
To see issues from Polaris, select an Application, then a Project, and then a Branch.
When you upgrade from a version of Code Sight older than 2023.9.0, Team View will initially display issues for the default branch, typically named “main (default)”.

Improvements have been made to the way Code Sight handles self-signed certificates. It can now handle all certificate validation exceptions.

A more detailed error message is now displayed when the Coverity scan fails due to an invalid coverity.conf file.

Code Sight now supports the following development environments:

- IntelliJ 2023.2 and that version of the other JetBrains IDEs
- Visual Studio:
  - Visual Studio 2017: release 15.8 and greater
  - Visual Studio 2029: release 16.3 and greater
  - Visual Studio 2022: release 17.1 and greater
- VS Code 1.80 and 1.81

Code Sight now supports the following Black Duck product versions:

- Coverity Analysis and Coverity Connect 2023.9.0

## Bug fixes

- With older versions of Rapid Scan Static (Sigma), IntelliJ might throw an exception when trying to scan a decompiled file. The Rapid Scan Static 2023.8.0 release has now fixed this issue.
  UD-12208
- This version fixes a bug that would cause excessive logging when loading large projects in Code Sight for Visual Studio.
  UD-12084

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 2021-09 (4.21)
- IntelliJ 2021.2 and that version of the other JetBrains IDEs
- VS Code 1.75

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2021-12 (4.22)
- IntelliJ 2021.3 and that version of the other JetBrains IDEs
- VS Code 1.76 and 1.77

Support for the following Black Duck product versions has been discontinued:

- Coverity Analysis and Coverity Connect 2021.12.0

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Coverity Analysis and Coverity Connect 2022.3.0

## See also

Code Sight Support Matrix

Code Sight Known Issues
