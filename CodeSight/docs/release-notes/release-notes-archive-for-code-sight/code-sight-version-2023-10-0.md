---
title: "Code Sight version 2023.10.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.10.0.html"
content_id: "ouPuagmUPFuGUvIbgVuZFw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.093067+00:00"
---

# Code Sight version 2023.10.0

Updates to version 2023.10.0 improve the installation process and enable connection to Coverity Connect.
This version adds support for the latest version of Black Duck®
Detect, and in VS Code, enables filtering of Polaris issues.
As usual, it includes bug fixes and changes to which product versions are currently supported.

## Enhancements

As of version 2023.10.0, scan engines no longer download automatically after the server has been authenticated.
To download Coverity or Black Duck (Black Duck®
Detect), go to the Products and Licenses panel and click to install the scan engines you choose to run locally.
This can be a time saver, especially if you prefer to view Coverity issues on the server.
For the Code Sight Standard Edition, the Rapid Scan engines download automatically, as they did in previous releases.

You can now authenticate to a Coverity Connect server by using an authentication key.
This enhancement lets you connect to a SAML-enabled (single sign-on) Coverity Connect server from within the IDE.

For VS Code users, release 2023.10.0 adds the capability to filter Polaris issues in TEAM VIEW.
Supported filters include: Owner, Tool Type, and Triage Status.

Version 2023.10.0 adds support for Black Duck®
Detect 9, a major upgrade.

Code Sight now supports the following development environments:

- VS Code 1.82

## Bug fixes

- Fixed a problem where Eclipse would not run an SAST scan on a file that was not in the current workspace.
  Now it will do so, but there still is a chance the scan will fail if the file is not present in the current build capture. UD-12263

## Discontinued support

Support for the following development environments has been discontinued:

- VS Code 1.76

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2022-03 (4.23)
- VS Code 1.78

Support for the following Black Duck product versions has been discontinued:

- Black Duck 2021.10

## See also

Code Sight Support Matrix

Code Sight Known Issues
