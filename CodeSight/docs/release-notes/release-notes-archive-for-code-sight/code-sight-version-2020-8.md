---
title: "Code Sight version 2020.8"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2020.8.html"
content_id: "N2ZedHlyhcnOoRuL8le0dQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.808128+00:00"
---

# Code Sight version 2020.8

The 2020.8 release of the Black Duck® Code Sight™ plug-in
includes a number of enhancements to improve ease of use and the accuracy of information displayed.
It adds support for some IDE versions, and fixes a number of bugs as well.

## Discontinued support

- For JetBrains IDEs, version 2018.1 is no longer supported.
  2018.2 is the earliest version now supported.

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| ß Android™ Studio | 3.4 – 4.0 | Windows®, Linux™, macOS® | Java™ |
| ß Microsoft® Visual Studio® Code | 1.41 – 1.47 | Windows, Linux, macOS | C/C++, C# (.NET Core), Java, JavaScript, PHP, Python, Ruby, TypeScript |

- The Android Studio environment uses the same installation steps as IntelliJ.

## Behavior Change

- In the Issues list, clicking the entry for an issue still updates the Details display,
  but to display the issue in the environment Editor, you now need to double-click the issue.

  If the source file with the issue was not already open in the editor, double-clicking
  the issue entry opens that source file to the line where the issue was detected.

## Enhancements

- Version 2020.2 of the various JetBrains IDEs is now supported.
- Android Studio version 4.0 is now supported in beta.
- Microsoft Visual Studio Code versions 1.46 and 1.47 are now supported in beta.
- The Full Scans area of the Scans panel now shows the state
  of the most recent full scan attempt, and the time of the last successful full scan.

  Code Sight displays this scan information for each installed analysis tool.

  While a full scan is running, the “in progress” icon for the scan is now animated.
- In Notifications,the Update Scanning Tool page now displays as
  a “Warning” instead of as “Info”.
- The Issue Details display for Black Duck issues now sorts vulnerabilities by severity.
- In the Issues list, you can now search for the tool that reported the issue.
  At present, these are the acronyms
  `SAST` (*Static Application Security Testing)* for Coverity Analysis, and
  `SCA` (*Software Composition Analysis)* for Black Duck.

  The list of issues now includes a new column,
  Domain, that indicates which tool located this particular issue.
  This column, like the others, is sortable.
- If a Black Duck scan fails, the Full Scans area of the Scans panel now shows
  the message “Error: <error link>”.
  Clicking <error link> displays the Error Details page, which displays information that can help you,
  or Support, understand the error and find ways to correct it.
- This release supports SCA Auto-Remediation: This is the ability of Black Duck to automatically
  upgrade a vulnerable component version to a secure version.
  Upgrades are suggested by the Black Duck Upgrade guidance service.

  For Code Sight 2020.8.0, NPM is the only supported package manager.
  For Auto-Remediation to run successfully, `npm` must be present in
  the system `PATH` variable, and `npm install` must have been
  run at the command line before launching the IDE.

  Auto-Remediation is only available for direct dependencies.
  For transitive dependencies, you must upgrade manually.
  When this is the case, Code Sight messages display advice on how you can do so.

## Bug fixes

- When Black Duck server authentication failed, Code Sight was displaying a message
  specific to Coverity Analysis. This has been fixed.
  UD-4476
- If the Black Duck server is unreachable, or if responses are timing out during a Black Duck (SCA) scan,
  then Code Sight reports that the scan has failed, and displays an appropriate error message.
  UD-4900
- If the Black Duck server’s SSL certificate verification fails during a Black Duck (SCA) scan,
  then Code Sight now displays an appropriate error message.
  UD-4902
- Fixed an issue where the recommended version for remediating SCA issues was
  being displayed as a hash string.
  UD-5188
- Fixed a bug where Code Sight had issues connecting to Coverity Connect server over a TLS connection.
  UD-5375
- Code Sight for Visual Studio Code was initiating Black Duck scans, which it does not support. This has been fixed.
  UD-5459
