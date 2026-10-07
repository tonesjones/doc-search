---
title: "Code Sight version 2020.1"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2020.1.html"
content_id: "kUupWw5tVALWsfPBfZSE5Q"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.052719+00:00"
---

# Code Sight version 2020.1

The 2020.1 release of the Black Duck® Code Sight™ plug-in expands the range of supported IDEs
and fixes some bugs.

## New features

- New versions of the following IDEs are now supported:
  - IntelliJ IDEA 2019.3
  - PhpStorm 2019.3
  - PyCharm 2019.3
  - RubyMine 2019.3
  - WebStorm 2019.3
- The End User Software License and Maintenance Agreement for Code Sight
  has been updated to Version 2019.03.
- The top toolbar of the Code Sight window now has an icon that opens a
  Black Duck Community page with links to the Code Sight help.

  
 [image: Icon to open web page with help links]

## Discontinued support

The following platforms are no longer supported:

- macOS 10.12
- Windows 7

## Bug fixes

- Fixed an issue in Code Sight for Visual Studio where the Code Sight window would interrupt IDE use and
  steal focus during Coverity tool downloads. UD-3829
- Fixed an issue in Code Sight for Visual Studio where queued scans were incorrectly
  reporting a Last Scanned time of Now.
  UD-3830
