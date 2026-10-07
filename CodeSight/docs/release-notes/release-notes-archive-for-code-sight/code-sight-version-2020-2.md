---
title: "Code Sight version 2020.2"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2020.2.html"
content_id: "LgVioCZgugwpK0XuoreO8A"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.002139+00:00"
---

# Code Sight version 2020.2

The 2020.2 release of the Black Duck® Code Sight™
plug-in expands the range of supported IDEs and fixes some bugs.

## New features

- New versions of the following IDEs are now supported:
  - Eclipse 2019-12 (4.14)
- In Visual Studio, while a single-file scan is running, the Scans panel now displays an icon with an X on it to the left of the file name.
  Clicking this icon cancels the scan job.

  
 [image: 'X' icon to cancel a single-file scan]   

**Icon to cancel a single-file scan**

- To help troubleshoot a problem, Support sometimes needs to look at log files.
  You can now obtain the current log files by going to Preferences > Black Duck Code Sight Preferences > Troubleshooting > Log Files,
  and then clicking Export Logs.
  Code Sight zips the current logs and saves them to a location it displays in the Preferences page.
  You can attach this file to a Support request.
- Code Sight for Visual Studio® Code is now supported (in beta).
- Under Limited Availability, Code Sight now provides support for Black Duck in IntelliJ and Eclipse.
  The Black Duck software helps you choose open source libraries that are non-vulnerable,
  in order to ensure open source security compliance.

## Bug fixes

- Fixed an issue where the "Full Scan" notification was not removed after the summary was downloaded. UD-4027
- Improved the error reporting for scan failures: If a build capture fails, the report now includes the build-failure messages. UD-4043
- When many scans were queued, Code Sight would sometimes consume large amounts of RAM. This is now fixed. UD-4096
- On Windows 10, if the language was set to a language other than English, Code Sight would fail to run in Visual Studio 2015.
  This has now been fixed. UD-4106
- In Eclipse, after upgrading the plug-in version, the IDE would appear not to completely refresh the plug-in panes. This has now been fixed.
  UD-4166
- In Code Sight for Visual Studio, the extension’s Welcome page was linking incorrectly to out-of-date documentation.
  It now links correctly to the up-to-date documentation posted on the “Community Black Duck” portal. UD-4300
- On Windows, Code Sight would fail to locate a `coverity.conf` file if that file was saved to the parent directory of a project
  or to a solution directory. This has now been fixed. UD-4330
