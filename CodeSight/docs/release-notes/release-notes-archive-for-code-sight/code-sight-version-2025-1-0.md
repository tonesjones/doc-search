---
title: "Code Sight version 2025.1.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.1.0.html"
content_id: "Cup_INMU67huJ9LTe~oJ8A"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.483824+00:00"
---

# Code Sight version 2025.1.0

Release 2025.1.0 adds Team View support to the Eclipse IDE.

## Enhancements

- The Eclipse IDE now supports Team View display of remote issues from Polaris scans.
- Snippet Analysis is now available in VS Code for Black Duck SCA users. Open-source snippets are listed in
  the LOCAL VIEW when Automatic Scan mode is active. See
  Snippet Analysis (VS Code only) for more
  details.
- Customers who use an IP safelist should add repo.blackduck.com (34.149.5.115) to this list.

  The sig-repo.synopsys.com site at its old IP (34.110.245.127) will continue to be available through February 2025.
- Code Sight Standard Edition customers who use an IP safelist should add codesight.blackduck.com (34.8.121.57) to this list.

  The codesight.synopsys.com site at its old IP (34.95.116.38) will continue to be available through March 2025.

Code Sight now supports the following development environments:

- Eclipse 2024-12 (4.34)
- VS Code 1.96

## Bug fixes

- Fixed a bug where Coverity Analysis would run twice when scanning all files.
  UD-14837
- In VS Code Team View, selecting an occurrence of a nested issue
  would not navigate the editor to the corresponding source file. This has now been fixed.
  UD-14824
- For Coverity issues from Coverity Connect displayed in Team View, at times Code Sight
  would not locate the issue in local source code despite the user providing a search path in the coverity.conf file. This has now been fixed.
  UD-14698
- For Polaris, projects and branches would not load when the count of items was greater than 200. This has now been fixed.
  UD-14648
- When using Coverity Connect 2024.12 (or a newer version) in a Developer role,
  the Action, Classification, Severity, and custom attribute issue filters
  are now visible in Team View.
  UD-13886

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 2022-12 (4.26)
- IntelliJ 2022.3
- VS Code 1.89

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2023-03 (4.27)
- IntelliJ 2023.1
- VS Code 1.90

Support for the following platforms has been discontinued:

- macOS 12

## See also

Code Sight Support Matrix

Code Sight Known Issues
