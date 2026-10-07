---
title: "Code Sight version 2024.9.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.9.0.html"
content_id: "zPXdjqufFsKJZgMLtD37yw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.617799+00:00"
---

# Code Sight version 2024.9.0

The main enhancement in the 2024.9.0 release is the introduction, for VS Code, of Local View and
*scan configurations*. Local View displays results from scans that run on your local system, and
scan configurations provide a convenient way to set up and manage how such scans are run.

## Enhancements

- In the VS Code editor, the Code Analysis and Open Source Analysis views are now consolidated into
  a single Local View, which displays results of scans run locally. The scans themselves can be of various types, and
  are managed using a new *scan configuration* interface.
- For Coverity Connect issues in Team View in VS Code,
  you can now filter by Owner Name.
  This lets you view issues that belong to a particular user. A drop-down menu lets you choose among the available users.
- An upcoming release of Black Duck®
  SCA will offer *multi-factor authentication*
  (MFA; also known as *two-factor authentication* or 2FA).
  To support this, if Code Sight detects that a Black Duck server has enabled MFA, it
  directs the Code Sight user to authenticate using an authentication token rather than a password.

Code Sight now supports the following development environments:

- Version 2024.2 of the following JetBrains IDEs: CLion, IntelliJ IDEA, PhpStorm, PyCharm, RubyMine, and WebStorm.

## See also

Code Sight Support Matrix

Code Sight Known Issues
