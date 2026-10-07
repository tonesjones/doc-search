---
title: "Code Sight version 2023.4.0 (Eclipse, JetBrains, and VS Code)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.4.0-eclipse-jetbrains-and-vs-code-.html"
content_id: "Y2SsueJNUyfJp3gG_lM0~A"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.332155+00:00"
---

# Code Sight version 2023.4.0 (Eclipse, JetBrains, and VS Code)

Release 2023.4.0 adds the Eclipse IDE to the Code Sight Standard Edition (CSSE).
It also adds some development environment versions, support for Black Duck®
Detect 8, and a new
VS Code interface for configuring local installations of Java and the package manager you use.

## Enhancements

The URL for an installation of Black Duck®
Detect has changed.
The updated URL now has the form, blackduck-detect-<version>-air-gap-no-docker.zip.
See Specify a custom download location for Black Duck Detect for further details.

The Eclipse development environment is now incorporated in the Code Sight Standard Edition (CSSE).
As with IntelliJ (JetBrains IDEs in general) and VS Code, you can configure the locations of the Rapid Scan tools to run.
Code Sight now displays separate panels for Code Analysis and Open Source analysis. These new panels let you launch scans yourself;
for Code Analysis, you can also choose to launch scans automatically.
(The Scans panel, formerly under the Status view, has been removed.
The results shown in an issues list pertain only to the scan performed most recently.)

For each manual scan run in Eclipse as in IntelliJ and VS Code, all the commands that are executed for a scan are logged in real time in a file.
For each command that is executed, the working directory, command line, standard output, standard error, and exit code of the command are logged in the file.
This information is available in the file saved by Export Logs.
It is also available via the Scan Details message that appears while a scan is running and after the scan completes.

In Eclipse, the user can now specify the location of the Rapid Scan engines that have been installed locally.

In VS Code, a new Configure Paths panel for Rapid Scan SCA enables users to specify the location of the Java installation
and the package manager that they use when running Open Source Analysis.

In Eclipse, IntelliJ, and VS Code, Code Sight adds support for Black Duck®
Detect 8, a major upgrade.

Code Sight now supports the following development environments:

- Eclipse 2023-03 (4.27)
- VS Code 1.75 and 1.76

## Bug fixes

- Improved detection of the Java version, which is used to scan Java projects using Coverity Analysis.
  UD-11432
- Corrected the syntax of the sample configuration code in the topic
  Configure Coverity Analysis to use Coverity Connect.
  UD-11386

## Discontinued support

Support for the following development environments has been discontinued:

- IntelliJ 2020.2, 2021.1, and those versions of the other JetBrains IDEs
- VS Code 1.69

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- IntelliJ 2021.2 and that version of the other JetBrains IDEs
- VS Code 1.71

Support for the following Black Duck product versions has been discontinued:

- Black Duck 2021.8
- Detect versions 6.1 through 7.6

## See also

Code Sight Support Matrix

Code Sight Known Issues
