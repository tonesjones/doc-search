---
title: "Code Sight version 2020.4"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2020.4.html"
content_id: "fnyDIvkutXWrCHmCPqDGKg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.938775+00:00"
---

# Code Sight version 2020.4

Improvements in the 2020.4 release of the Black Duck® Code Sight™ plug-in include adding a new IDE version,
deprecating an older IDE version, and fixing numerous bugs.

## New features

- Code Sight can now use Polaris version 2020.03 or 2020.04.

  It no longer uses previous versions of Polaris.
- New versions of the following IDEs are now supported:
  - Android Studio 3.6
  - Eclipse 2019-12 (4.14)
- Under Limited Availability, Code Sight now supports Black Duck in Visual Studio.
  This helps you choose OSS libraries that are non-vulnerable, and ensures open source security compliance.

## Deprecated support

Support for the following platform has been deprecated, and will be dropped in a future Code Sight release:

- Eclipse 4.6

## Enhancements

- For those IDEs that support Black Duck, the Status log now shows the status of the most recent Black Duck scan.
  UD-4117
- In the previous release, a Black Duck scan was initiated whenever a source file was opened or closed.
  As of Code Sight 2020.4, after the initial scan a new Black Duck (SCA) scan only occurs when a Black Duck configuration file
  is opened or modified.

  Files whose change can trigger a new scan are listed in the *Black Duck®
  Detect* document > Detectors page.
  UD-4221
- Expanded support for the Export Logs feature.

  When a single-file scan fails, the Failure Reason column of the Scans panel (“Scan log”)
  now has a clickable link that says Unexpected error.
  Clicking that link opens an Unexpected Error page that provides a number of support options,
  including an Export Logs button that exports a zipped copy of the current logs.

  The button on the Unexpected Error page works the same as the Export Logs button on the
  Preferences > Black Duck Code Sight Preferences page
  (the button on the Code Sight Preferences page is still available, too).

  UD-4282

  
 [image: Scans panel log of single-file scans: 'Unexpected error' link in 'Failure Reason' column]   

**Scans panel > Log of single-file scans > ‘Unexpected error’ link in ‘Failure Reason’ column**

  
 [image: Status view: ‘Unexpected error’ panel appears after clicking ‘Unexpected error’ link]   

**Status view: ‘Unexpected error’ panel that appears after clicking the ‘Unexpected error’ link**

- In Visual Studio Code a new Code Sight option, Don’t Show
  Again, lets you suppress repeated appearances of the warning that Code
  Sight shows when you attempt to open a file and the current workspace is empty, when
  there is no current workspace, and other related conditions.

  Also, a new option on the Settings page lets you toggle display of the empty-workspace
  warnings. If these warnings have been disabled, then turning on the Warnings: Show All
  option re-enables them once again.

  UD-4391

  
 [image: Code Sight in VS Code: New 'Don't Show Again' button to suppress repeated display of the empty-workspace warning]   

**Code Sight in VS Code: New ‘Don’t Show Again’ button suppresses repeated
display of the empty-workspace warning.**

  
 [image: Code Sight in VS Code: New 'Warnings: Show All option on the Settings page re-enables empty-workspace warnings.]   

**Code Sight in VS Code: New ‘Warnings: Show All’ option on the Settings page re-enables
empty-workspace warnings.**

- In Visual Studio code, the STATUS area of the left-hand side bar now shows icons as convenient shortcuts to view and manage
  the Scan Status panel, the Export Logs page, and the Authentication pages (Edit Server icon).
  UD-4456

  
 [image: View Scans icon]   

**View Scans:**
This icon appears to the right of the Running scans or No running scans entry
in the Scanning section of the STATUS area.
Click it to open the Code Sight Scan Status panel, which appears at the right of the VS Code window.

  
 [image: Export Logs icon]   

**Export Logs:** This icon appears to the right of the
[version-number] entry in the the Code Sight Extension section of
the STATUS area. Click it to display an Export Logs page with an Export
Logs button you can click to save a zipped file of the current scan logs.

  
 [image: Edit Server icon]   

**Edit Server:**
This icon appears to the right of the Server entry in the Tools section of the STATUS area.
Click it to display the Authentication pages, where you can change the server being used, the current Code Sight user,
or both.

- Various enhancements to Black Duck support:

  - Added links to BDSA/CVE records for component details.
  - The Status view > Scans panel now shows
    the status of Black Duck scans.
  - In the Issues view, sorting and filtering Black Duck components has been improved.
  - The overall component impact is now based on the highest-level severity of the component security vulnerabilities
    or policy violations.

  UD-4494
- A new impact type, Critical, has been added to the interface.
  This level of impact is used for security vulnerabilities and policy violations detected by Black Duck.
  The icon appears in the Impact column of the Issues list, and in the Details panel
  for such issues.
  UD-4604

  
 [image: Icon for Critical issues]   

**Issues List and Detail panel: Icon for Critical issues**

## Bug fixes

- When authenticating Black Duck, a client’s credentials could be incorrectly lost.
  This has been fixed.
  UD-4340

- In previous releases, if Code Sight could not use the URL you provided when authenticating, it displayed a message whose
  text read, “This product needs a valid server URL to continue.
  Please confirm your server URL with your administrator.”

  However, this message was not accurate in cases where the URL was valid but the server could not validate the certificate
  that accompanied the address. As of version 2020.4, when Code Sight cannot validate a certificate the message now reads
  as follows: “Unable to validate the certificate from the given URL. Please confirm the URL with your administrator.
  Connecting to a server without a valid certificate can put the integrity and confidentiality of your data at risk.”

  Remember:
  You can configure Code Sight to accept self-signed certificates.
  To do so, add the line `"on_new_cert": "trust"` to your coverity.conf file.
  (You must restart the IDE you use for this change to take effect.)

  UD-4447

- Fixed a bug where the Issues list was displaying duplicate entries for the same issue.
  UD-4513
