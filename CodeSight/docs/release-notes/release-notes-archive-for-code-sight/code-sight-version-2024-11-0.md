---
title: "Code Sight version 2024.11.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.11.0.html"
content_id: "C2XcUPG7O~A30VaiUB5p5w"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.521878+00:00"
---

# Code Sight version 2024.11.0

The main enhancement in the 2024.11.0 release is the introduction, for JetBrains IDEs including IntelliJ IDEA, of Local View and *scan configurations*.
Local View displays results from scans that run on your local system, and scan configurations provide a convenient way to set up and manage how
such scans are run.

## Enhancements

- In IntelliJ as in VS Code, the Code Analysis and Open Source Analysis views are now consolidated
  into a single Local View, which displays results of scans run locally. The scans themselves can be of various types, and are managed
  by the scan configuration controls. See Local View.
- In VS Code, the Scan Configuration tab now provides a Copy scan configuration button that lets you create a new
  scan configuration by copying an existing one.
- Polaris users now have the ability to run Rapid Scan Static scans.
- Customers who use an IP safelist should add repo.blackduck.com (34.149.5.115) to this list.

  The sig-repo.synopsys.com site at its old IP (34.110.245.127) will continue to be available through February 2025.
- Code Sight Standard Edition customers who use an IP safelist should add codesight.blackduck.com (34.8.121.57) to this list.

  The codesight.synopsys.com site at its old IP (34.95.116.38) will continue to be available through March 2025.

Code Sight now supports the following development environments:

- IntelliJ IDEA (and other JetBrains IDEs) 2024.3
- VS Code 1.95

## Bug fixes

- Fixed a bug where Code Sight would not try to download a valid Coverity license in order to
  replace a nonexistent or an expired one.
  UD-14608
- Fixed a bug where Code Sight would sometimes not start up properly when using IntelliJ 2024.3.0.
  UD-14380

## Discontinued support

Support for the following development environments has been discontinued:

- VS Code 1.88

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- VS Code 1.89

## See also

Code Sight Support Matrix

Code Sight Known Issues
