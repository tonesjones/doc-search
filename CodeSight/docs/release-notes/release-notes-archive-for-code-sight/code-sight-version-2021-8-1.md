---
title: "Code Sight version 2021.8.1"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2021.8.1.html"
content_id: "9gnRI0A83nAMP~WEa7~1dw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.276060+00:00"
---

# Code Sight version 2021.8.1

Version 2021.8.1 corrects a few bugs in Code Sight behavior, and a few errors in the documentation.

## Beta support

These tables show the IDEs and products that are supported in beta.

| IDE | Versions | Platforms | Languages |
| --- | --- | --- | --- |
| Android™ Studio | 3.4 – 4.2 | Windows®, Linux™, macOS® | Java™ |

- The Android Studio environment uses the same installation steps as IntelliJ.

Attention:
Beta support for Android Studio 3.4 has been deprecated, and will be discontinued in a future release of Code Sight.

## Bug fixes

- Attempting to launch a manual scan would throw an IDE exception when the Code Sight plug-in had not been initialized.
  This has been fixed.
  UD-8173
- The Installed Plug-in and Tool Versions page would show an Install Black Duck button after Black Duck was already installed. This has now been fixed.
  UD-8270
- Fixed a bug in Code Sight for Visual Studio where certain Solution configurations would prevent a Black Duck scan from running successfully.
  UD-8374, ID-8491
- Black Duck Rapid Scans would fail if the standard port (443) was included in the Black Duck server URL used during authentication. This has been fixed.
  UD-8452
