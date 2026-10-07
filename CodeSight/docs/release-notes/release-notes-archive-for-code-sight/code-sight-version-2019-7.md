---
title: "Code Sight version 2019.7"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2019.7.html"
content_id: "gQwvGCM87iYQVp6qBULD3A"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.213428+00:00"
---

# Code Sight version 2019.7

The 2019.7 release of the Black Duck® Code Sight™ plug-in introduces new features
and fixes various bugs.

## New features

- The JetBrains® PhpStorm™ IDE is now supported.
- Microsoft® Visual Studio® version 2019 is now supported.
- Code Sight now displays all issues: both those produced by the local scan, and those obtained from your configured server stream or project.
- Code Sight no longer launches local full scans automatically.
  If a full scan has never been run, if one has not been run for a while, and under some other conditions, Code Sight will prompt you to run one.
  This prompt is displayed on the Run Full Scan page of the Notifications view.
- In Visual Studio, running a scan in the background no longer prevents you from starting IDE builds or debugging your application.
- The Dismissed state is now pushed to the server as soon as you click Dismiss.
  (In previous releases, it was not pushed until the end of the timeout interval.)
  Issue states received from the server are still synchronized locally at the end of each interval.
- Code Sight now supports FlexNet® licensing for Coverity® Connect.
  The license file is saved locally as license.config in the <install location>/cov-tools/bin/ directory.

## Bug fixes

- Fixed an issue where Code Sight for Visual Studio would not run C/C++ scans in Visual Studio releases earlier than version 16.1.
  Corrected the problem by using the active build configuration in Visual Studio for Coverity build capture. UD-3003
- Fixed an issue where Code Sight for Visual Studio would interfere with debugging C# web applications. UD-2979
