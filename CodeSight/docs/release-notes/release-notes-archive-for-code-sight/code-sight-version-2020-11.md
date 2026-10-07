---
title: "Code Sight version 2020.11"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2020.11.html"
content_id: "aL7cGiuyU3lvX659tj4dSA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.666687+00:00"
---

# Code Sight version 2020.11

The 2020.11 release of the Black Duck® Code Sight™ plug-in
is a maintenance release that updates support for some programs, and fixes various issues.

## Platform deprecation

- Support for macOS® 10.13 has been deprecated, and in an upcoming release of
  Code Sight will no longer be available.

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| ß Android™ Studio | 3.4 – 4.0 | Windows®, Linux™, macOS® | Java™ |
| ß Microsoft® Visual Studio® Code | 1.41 – 1.49 | Windows, Linux, macOS | C/C++, C# (.NET Core), Java, JavaScript, PHP, Python, Ruby, TypeScript |

- The Android Studio environment uses the same installation steps as IntelliJ.

## Enhancements

- Version 2020-9 (4.17) of the Eclipse IDE is now supported.
- In Code Sight 2020.8, the behavior of the Issues list changed, such that you needed to double-click an entry to
  highlight the corresponding line of code in the IDE Editor.

  In Code Sight 2020.11, if the source file that contains the issue is already open, then once again a single click
  on an entry in the Issues list highlights the corresponding line of code in the Editor.
  If the source file *is not open* in the Editor, then for some IDEs you must double-click the entry to open
  the file: After it opens the file, Code Sight then highlights the line of code that is in question.
- Code Sight now filters out eLearning suggestions that are not relevant to the language
  of the code being scanned.
- [image: Scans panel icon to cancel a running full scan]
   A running full scan can now be cancelled by clicking the Cancel icon in the “Full scans” section
  of the Scans panel.

  [image: Status-bar icon to cancel a running scan]
   For some IDEs, while the scan is running, a progress indicator and the Cancel icon also appear
  in the IDE’s own status bar.
- In certain circumstances Code Sight would try to download and install a scanning tool automatically.
  As of release 2020.11, the user must launch the download and setup process for a tool.
- For Black Duck Source Component Analysis (SCA) scans (a limited-availability feature),
  Code Sight has improved performance by caching security vulnerabilities, potential policy violations, and upgrade
  guidance fetched from the server. By default, the cached data persists for 24 hours.
- Code Sight SCA support has been updated to display how many occurrences of vulnerable components,
  whether direct or transitive, are present in projects managed by GitHub npm™.

  For transitive npm components, Code Sight displays which direct dependency has resulted in the inclusion of
  the vulnerable component.
- For Black Duck SCA, if no scan is running, a Rerun button
  now appears in the “Full scans” section of the
  Status view > Scans panel.
  Clicking Rerun launches a full scan of the target code project.

## Bug fixes

- In some cases, while Code Sight was installed, opening a solution file directly from Windows Explorer would cause Visual Studio 2015
  to freeze on startup. This has now been fixed.
  UD-4296
- Sometimes launching Visual Studio 2017 by double-clicking a .sln file
  would cause Code Sight to hang when the IDE launched the extension. This has now been fixed.
  UD-5104
- In Visual Studio 2017, after opening a solution by double-clicking a .sln file,
  sometimes the “No Solutions have been opened” warning would continue to be displayed.
  This has now been fixed.
  UD-5117
- When Code Sight was configured to run both Coverity Analysis and Black Duck, at times
  the Domain column in the Issues list would display the domain as “Unknown”.
  This has been fixed. A domain is now shown as either SAST or SCA, as appropriate.
  UD-5867.
- Performance in Visual Studio has been improved, especially when switching branches or when loading a new project.
  One consequence of this fix is that for a project or solution, Black Duck scans for reference inclusion/exclusion
  no longer run automatically.
  UD-6135
