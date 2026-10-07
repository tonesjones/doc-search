---
title: "Code Sight version 2025.3.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.3.0.html"
content_id: "Bp9mvjTc0Bur9dYLirn_uw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.408764+00:00"
---

# Code Sight version 2025.3.0

This release adds Team View suppoprt to the Eclipse IDE, and discontinues the earlier Remote mode.
It also enhances the filtering options for Coverity issues in the JetBrains IDEs (including IntelliJ) and VS Code.

## Enhancements

- In Eclipse, remote issues detected by Polaris,
  Coverity Connect and Coverity on Polaris
  now display in Team View.

  The Remote mode in the Code Analysis view has been removed.
  Issues detected locally continue to display in the Code Analysis view.

  If previously you had a stream or project configured in a coverity.conf or polaris.yaml file,
  to view remote issues you now need to configure the stream or project in the
  Preferences → Sources panel.
  (Local scans will continue to use coverity.conf or polaris.yaml for stream and project configuration.)
- For remote Coverity issues in Code Sight (Team View in JetBrains IDEs and VS Code),
  the filtering options now include filtering components by name.
- Code Sight Standard Edition customers who use an IP safelist should add codesight.blackduck.com
  (34.8.121.57) to this list.

Code Sight now supports the following development environments:

- VS Code 1.97 and VS Code 1.98

## Bug fixes

- Fixed a bug that could cause Coverity scans to not find any issues when scanning compiled languages
  (such as C/C++ and C#) if the solution had previously been built but not cleaned.
  UD-14154

## Discontinued support

Support for the following development environments has been discontinued:

- Android Studio 2022.3.1

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Android Studio 2023.1.1
- Eclipse 2023-03 (4.27) and Eclipse 2023-06 (4.28)

## See also

Code Sight Support Matrix

Code Sight Known Issues
