---
title: "Code Sight version 2023.7.0 (Eclipse, JetBrains, and VS Code)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.7.0-eclipse-jetbrains-and-vs-code-.html"
content_id: "lcBZmt7W6I5_ltYYryZG7g"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.213789+00:00"
---

# Code Sight version 2023.7.0 (Eclipse, JetBrains, and VS Code)

Release 2023.7.0 introduces Team View, a new panel in the IntelliJ and VS Code IDEs that can display the results from software-integrity products
running on networked servers.
Team View supports the Polaris and Software Risk Manager tools.
For Eclipse, IntelliJ, and VS Code, this release also provides improved handling of connections that use self-signed certificates.

## Enhancements

Code Sight now integrates with Polaris and Software Risk Manager.
A new panel named Team View displays issues detected by either of these two servers.
Team View is available in Visual Studio Code and IntelliJ (including other supported JetBrains variants).

With Code Sight 2023.7.0, you can connect to servers that use self-signed certificates.

Code Sight now supports the following development environments:

- Eclipse 2023-06 (4.28)
- VS Code 1.79

Code Sight now supports the following Black Duck product versions:

- Black Duck 2023.7

## Bug fixes

- Fixed a `ConcurrentModificationException` that would occur when using Rapid Scan Static in **Auto mode**.
  UD-11769

## Discontinued support

Support for the following development environments has been discontinued:

- Visual Studio Code 1.72–1.74

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- VS Code 1.75

## See also

Code Sight Support Matrix

Code Sight Known Issues
