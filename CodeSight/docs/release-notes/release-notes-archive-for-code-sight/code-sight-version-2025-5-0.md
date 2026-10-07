---
title: "Code Sight version 2025.5.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.5.0.html"
content_id: "RilQ1DNC8XwmW7kaIr1Ctg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.330991+00:00"
---

# Code Sight version 2025.5.0

Code Sight version 2025.5.0 extends support for Snippet Analysis to Code Sight Standard Edition (CSSE) customers.

## Enhancements

- Snippet Analysis is now available in VS Code for users of the Code Sight Standard Edition (CSSE).
  Open-source snippets are listed in the LOCAL VIEW while Automatic scan mode is active.
  See Snippet Analysis (VS Code only) for more details.
- In VS Code, it is now mandatory to designate a Working Directory for each Scan Configuration.

  Prior to release 2025.5.0, the Working Directory was allowed to specify a multi-root workspace file.
  This is no longer supported.

  Create a Scan Configuration for every project that you want to scan separately.

Code Sight now supports the following development environments:

- IntelliJ IDEA 2025.1
- VS Code 1.100

## Discontinued support

Support for the following development environments has been discontinued:

- JetBrains IDEs, including IntelliJ IDEA: version 2023.1

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- JetBrains IDEs, including IntelliJ IDEA: version 2023.2

## See also

Code Sight Support Matrix

Code Sight Known Issues
