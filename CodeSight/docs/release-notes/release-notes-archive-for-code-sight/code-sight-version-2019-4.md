---
title: "Code Sight version 2019.4"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2019.4.html"
content_id: "G0di52iNMc70CsvhyHwM4Q"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.331250+00:00"
---

# Code Sight version 2019.4

The 2019.4 release of the Black Duck® Code Sight™ plug-in introduces new features
and fixes a number of bugs, particularly bugs related to usability and error handling.

## New features

- The plug-in now supports C/C++ analysis in Visual Studio®.
- New IDEs are now supported:
  - IntelliJ® 2019.1
  - RubyMine™ 2018.1 to 2019.1
  - Eclipse 2019-03 (4.11)

## Bug fixes

- Fixed an issue where no error was reported if no analysis tools were found on the Polaris server. UD-2438
- Fixed an issue where the Visual Studio 2015 IDE suddenly became unresponsive and crashed intermittently with
  the unhandled exception `System.NullReferenceException`.
  UD-2588
- Updated the plug-in to support analysis of C/C++ projects in Visual Studio. UD-2486
- Reduced the scope of what incremental builds capture, in order to improve performance of fast-desktop Coverity scans. UD-1003
- Fixed an issue where the Code Sight configuration in the Visual Studio option dialog had
  invisible labels while using the dark display theme. UD-2492
- Fixed an issue that caused Visual Studio to change the editor focus after a scan completed. UD-2451
- In Visual Studio, added search capabilities for the scan log listing. UD-2186
- Improved the layout of messages. While viewing the Welcome page, the Close button is
  now always visible, even when scrolling through the message. UD-2304
- Fixed an issue that would occasionally cause the plug-in to scan files again after a summary download or generation. UD-2320
- Added additional feedback to the active scan messaging, which now exposes more of what the scan is doing. UD-2514
- Fixed an issue where a local analysis scan would not be performed if the summaries on Polaris were incompatible. UD-2300
- The plug-in now only listens for files that belong to the active project. This means
  that results for unrelated files are no longer incorrectly displayed. UD-1834
- For Visual Studio, improved the startup performance of Code Sight.
  VS 2015 and 2017 no longer recommend disabling the plug-in (the “extension”). UD-1338
- The following views and sections have been renamed:
  - The Overview tab is now called Status.
  - The Plug-in panel is now called Notifications.
  - The Scan Log panel is now called Scans.

  UD-2487
- The plug-in now supports a `Cancelled` scan result.
  This is displayed in the Scan Result column of the Scans panel when the user cancels an in-progress file scan. UD-1479
- Server URLs specified in swip.yml will now be considered
  when populating the authentication dialogs
  and attempting to connect automatically using existing credentials. UD-2385
