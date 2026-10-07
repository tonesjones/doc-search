---
title: "Code Sight version 2019.9"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2019.9.html"
content_id: "ob7WiGDo0X3018280zLe6Q"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.159958+00:00"
---

# Code Sight version 2019.9

The 2019.9 release of the Black Duck® Code Sight™ plug-in introduces new features
and fixes various bugs.

## New features

- Android™ Studio 3.4 is now a supported IDE (in beta for this release).
- The Eclipse®, IntelliJ®, and Visual Studio® environments
  can now analyze TypeScript source.
- The Visual Studio environment can now analyze VB.NET source.
- A new Filter feature filters out issues that were found by a full scan, but not found by a
  single-file scan.
  (You can view these hidden issues if you want to.)
- When you dismiss an issue or un-dismiss it, a dialog now requires you to enter
  a reason for why you are doing so.

## Bug fixes

- When you edit the coverity.conf file, now Code Sight automatically regenerates its compiler configuration data.
  You do not have to restart the plug-in for the changes to take effect. UD-2953
- When running with Polaris, Code Sight would sometimes continue to show issues that had been closed.
  This has been fixed. UD-3595
- In IntelliJ 2019.2.1+, when running the 2019.7.2 version of the Code Sight plug-in, opening the Preferences
  dialog and choosing the Black Duck Code Sight page would cause an exception.
  This has now been fixed.
  UD-3632
- When running with Polaris, Code Sight now accurately verifies the version of analysis tools and summary downloads.
  UD-3627
