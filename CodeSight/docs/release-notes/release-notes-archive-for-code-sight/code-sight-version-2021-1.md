---
title: "Code Sight version 2021.1"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2021.1.html"
content_id: "Cz80eHqU2OF0rWdKuvhKCw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.584935+00:00"
---

# Code Sight version 2021.1

Version 2021.1 introduces support for Black Duck® software composition analysis and for
Microsoft® Visual Studio® Code.
In addition, some interface improvements make it easier to manage and schedule code scans.

## Discontinued support

- End-of-life (EOL): Support for Eclipse 4.6 has been discontinued.
- Support for Eclipse 4.7 has been deprecated, and will be discontinued in a future release of Code Sight.
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

- Code Sight 2021.1 introduces support for Black Duck Black Duck software composition analysis (SCA).
  This feature helps you maintain open-source software (OSS) security compliance by identifying known vulnerabilities
  in free OSS (FOSS) packages at development time. Black Duck scanning is currently supported for the Eclipse
  and IntelliJ IDEs. Visual Studio will remain in limited customer availability (LCA) until further notice.
  Visual Studio Code does not have Black Duck support.
- The Visual Studio Code (VS Code) environment is now supported.
  The supported versions are 1.48 through 1.52.
- Release 2021.1 adds support for IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm version 2020.3.
- Release 2021.1 adds support for Android Studio 4.1 in beta.
- The Code Sight for IntelliJ plug-in no longer restricts which versions of Java may be used.
  If the Coverity Analysis (SAST) tool does not support a particular version of Java, the scan will fail.
- Code Sight now lets users manually launch a single-file Coverity Analysis scan from various locations:
  - [image: image]
     In the Single-file scans area of the Scans panel,
    the user can click the Scan next icon.
  - [image: image]
     For an SAST issue, the Issues view > Issue Details panel shows the same icon.
  - In the IDE Editor, the right-click context menu now has a Scan with Code Sight choice.
  - In the IDE Explorer, the right-click context menu has the same choice,
    which appears when a source file (but *not* a project or solution) is selected.
- New preferences let a user enable or disable automatic scanning at either the IDE level or the project/solution/workspace
  level.
  (The plug-in for Eclipse provides this preference setting for the workspace level only.)

## Black Duck (SCA) Enhancements

- For a Black Duck issue, the Fix It page now shows a drop-down list so users can choose
  between recommended and most recent versions of a dependency. This drop-down list is available in IntelliJ and Eclipse only.
- Visual Studio now supports the Fix It button in the Details view of Black Duck issues.
  Clicking Fix It provides guidance on manually replacing vulnerable components.
  It also provides auto-remediation, if that feature is available for the package manager used by the current project.

  For the 2021.1 release of Code Sight, Visual Studio supports Black Duck scanning only on a
  limited customer availability (LCA) basis.
- The Details panel now displays the Fix It button even if there is no upgrade guidance for a vulnerability.
  In this case, Code Sight displays the Manual tab, which provides more details on why Black Duck did
  not find any upgrade guidance.
- For a Black Duck issue, the Contributing Events view now
  shows a dependency tree. With the help of this tree view, users can get more details about
  vulnerable dependency occurrences.
- The Details view for a Black Duck issue now shows a warning if local npm dependencies are missing.
  This warning is followed by a Details link, which takes you to a page called
  “Get Help on the Community Portal”. The new page has links to both the Portal pages and
  Support, and includes a button to Export Logs, whose output can help
  Support diagnose the problem.
- [image: image]  
  For Black Duck issues in the Issue Details view, Code Sight now displays an Edit icon.
  Clicking this icon opens the dependencies file (for example, pom.xml) in the IDE Code Editor, allowing users to manually
  correct the issue occurrence by updating this file.

## Bug fixes

- Fixed an issue where Code Sight data would not migrate from a version of the plug-in
  older than the immediately previous version.
  UD-5467
- After updating a vulnerable component found by a Black Duck scan, in some cases the
  issue was not removed from the Issues list. This has been fixed.
  UD-5953
- Black Duck (SCA) issues with a location were not appearing in the Current File scope.
  This has now been fixed, and such issues appear correctly when the scope of the Issues list
  is Current File.
  UD-6161
- Fixed an issue where an error message was still displayed after successfully authenticating the user.
  UD-6207
