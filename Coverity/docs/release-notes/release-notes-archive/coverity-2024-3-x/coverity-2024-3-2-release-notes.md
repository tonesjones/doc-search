---
title: "Coverity 2024.3.2 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.3.2-release-notes.html"
content_id: "VSTzVUxy3_pQl2UABhqeHQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:32.785274+00:00"
---

# Coverity 2024.3.2 Release Notes

## Important information for 2024.3.2

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

## Coverity Analysis 2024.3.2

This section provides release notes for Coverity Analysis components.

### Coverity CLI 2024.3.2

#### Bug fixes

COVCLI-3271
:   Reported in version: 2024.3.0
:   Fixed a performance issue in Coverity CLI buildless capture that caused excessive runtime for projects with a large number of modules and a highly connected dependency tree. This issue impacted buildless capture for Java, C# and Go.

COVCLI-3296
:   Reported in version: 2024.6.0
:   Coverity CLI C# buildless capture will now capture and analyze C# files where the project directory only contains a solution (`.sln`) file. Previously, when capturing a project using buildless capture, C# files would only be captured and analyzed using buildless capture if the project directory contained a C# project (`.csproj`) file or no known project files.

### Coverity Compilers and Capture 2024.3.2

#### New or changed features

CCK-2636
:   Added support for HighTec Tricore GCC 4.9.4.1 on Windows.

#### Bug fixes

CAP-2298
:   Reported in version: 2024.3.0
:   Bazel execution root path replacement will now work for source files in nested directories.

CMPGO-477
:   Reported in version: 2024.3.0
:   Fixed an issue in `cov-emit-go` where generic types could cause analysis to crash with missing declaration errors.

CMPJS-1212
:   Reported in version: unspecified
:   Fixed an issue where JavaScript files with paths that contained non-ASCII characters were not properly recorded in a record with source build.

## Coverity Desktop 2024.3.2

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2024.3.2

#### Bug fixes

PRD-12994, PRD-13043, PRD-13047, PRD-13086
:   Reported in version: 2023.6.0
:   Fixed an issue where the Eclipse, IntelliJ and Visual Studio plugins could no longer show the remote issues for users with a Developer role. A two-part fix has been put in place. The customer must upgrade the Coverity Desktop plugins to the 2024.3.2 version or newer and Coverity Connect to version 2024.3.0 or newer to see remote issues again.

    Coverity Desktop plugins can also be downloaded from the SIG Repo at <https://sig-repo.synopsys.com/artifactory/coverity-desktop-plugin-releases/>.

#### Known issues and solutions

PRD-13057
:   Set owner functionality in the context menu in the issues grid is not functioning as expected in IntelliJ, Eclipse and Visual Studio. Please use the assign owner functionality in the issue details section.

### Coverity Desktop for Intellij IDEA 2024.3.2

#### Bug fixes

PRD-12994, PRD-13043, PRD-13047, PRD-13086
:   Reported in version: 2023.6.0
:   Fixed an issue where the Eclipse, IntelliJ and Visual Studio plugins could no longer show the remote issues for users with a Developer role. A two-part fix has been put in place. The customer must upgrade the Coverity Desktop plugins to the 2024.3.2 version or newer and Coverity Connect to version 2024.3.0 or newer to see remote issues again.

    Coverity Desktop plugins can also be downloaded from the SIG Repo at <https://sig-repo.synopsys.com/artifactory/coverity-desktop-plugin-releases/>.

#### Known issues and solutions

PRD-13057
:   Set owner functionality in the context menu in the issues grid is not functioning as expected in IntelliJ, Eclipse and Visual Studio. Please use the assign owner functionality in the issue details section.

### Coverity Desktop for Microsoft Visual Studio 2024.3.2

#### Bug fixes

PRD-12994, PRD-13043, PRD-13047, PRD-13086
:   Reported in version: 2023.6.0
:   Fixed an issue where the Eclipse, IntelliJ and Visual Studio plugins could no longer show the remote issues for users with a Developer role. A two-part fix has been put in place. The customer must upgrade the Coverity Desktop plugins to the 2024.3.2 version or newer and Coverity Connect to version 2024.3.0 or newer to see remote issues again.

    Coverity Desktop plugins can also be downloaded from the SIG Repo at <https://sig-repo.synopsys.com/artifactory/coverity-desktop-plugin-releases/>.

#### Known issues and solutions

PRD-13057
:   Set owner functionality in the context menu in the issues grid is not functioning as expected in IntelliJ, Eclipse and Visual Studio. Please use the assign owner functionality in the issue details section.
