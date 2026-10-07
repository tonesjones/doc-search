---
title: "Code Sight version 2024.4.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.4.0.html"
content_id: "2~tC3u01XIW6TbYOuE18Gw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.828715+00:00"
---

# Code Sight version 2024.4.0

For the Visual Studio Team View, release 2024.4.0 adds the ability to display remote Coverity issues, and to filter Polaris issues.
This release also extends interactive telemetry enabling to all supported IDEs.

## Enhancements

- For remote Coverity Connect issues listed in Team View, if Secure Code Warrior pages are relevant to an issue, the Details panel
  displays links to those pages.
  Secure Code Warrior must have been enabled on your Coverity Connect server, and you must be running Coverity version 2023.12.0 or a later version.
  Secure Code Warrior support applies to JetBrains IDEs (including IntelliJ IDEA), Visual Studio, and VS Code.
- In Visual Studio, remote issues detected by Coverity Connect and Coverity on Polaris now display in Team View.
  The Remote mode in the Code Analysis view has been removed.
  Issues detected locally continue to display in the Code Analysis view.
  If in previous Code Sight releases you had a stream or project configured in a coverity.conf or polaris.yml file,
  to view remote issues you will need to configure the stream or project in the Preferences → Sources panel.
  (Local scans will continue to use coverity.conf or polaris.yaml for stream and project configuration.)
- Code Sight now shows the full name of Coverity servers (either Coverity Connect or Coverity on Polaris)
  to reduce confusion when connecting to Polaris versus Coverity on Polaris.
- For Visual Studio users, Code Sight adds the capability to filter Polaris issues in Team View.
  Supported filters include Owner, Tool Type, and Triage Status.
- For Code Sight in Eclipse, the preferences interface has been reorganized to make it clearer,
  and to parallel the preferences interfaces in JetBrains IDEs, including IntelliJ IDEA.
  For Code Sight in JetBrains and in Visual Studio, the organization and layout of some preference dialogs
  have been rearranged for better clarity.
- For Team View in JetBrains IDEs (including IntelliJ), the issue lists now retain their column width and ordering across
  IDE restarts. This retention is specific to the server being used.
- Release 2024.4.0 adds the ability to enable or disable telemetry collection in IDEs besides VS Code:
  that is, in Eclipse, in IntelliJ and other JetBrains IDEs, and in Visual Studio.
- For Polaris, fAST Dynamic projects are not supported at present. Code Sight does not list them or allow you to select them.
- For those IDEs we support on Linux, the tested variants are now Ubuntu 20.04 and 22.04.

Code Sight now supports the following development environments:

- Eclipse 2024-03 (4.31)
- JetBrains (including IntelliJ IDEA) 2024.1
- VS Code 1.88

## Bug fixes

- Fixed a bug that could cause issues when Code Sight for Visual Studio retrieved information about the solution as a precursor to running scans.
  UD-13422

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 4.23 (2022-03)
- VS Code 1.82

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 4.24 (2022-06)
- IntelliJ and other JetBrains IDEs 2022.3
- VS Code 1.83

## See also

Code Sight Support Matrix

Code Sight Known Issues
