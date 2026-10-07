---
title: "Code Sight version 2025.4.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.4.0.html"
content_id: "hm_PllghVCw4HbSmRKckxQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.371625+00:00"
---

# Code Sight version 2025.4.0

Version 2025.4.0 enhances the display of SCA issue details in VS Code.
It also adds some functionality to improve how Code Sight interacts with other Black Duck Software, Inc. products.

## Enhancements

- Release 2025.4.0 adds several enhancements to the display of SCA issues in VS Code:
  1. **Revamped Upgrade Guidance UI:**

     To enhance usability and clarity, we’ve redesigned the upgrade guidance interface for all SCA results from CSSE,
     Polaris, and Black Duck SCA.
  2. **Direct Upgrade Guidance for Transitive Dependencies:**

     This new feature provides straightforward upgrade guidance for vulnerable transitive dependencies, aiming to improve the developer experience with clear,
     actionable steps.

     This enhancement is available for all SCA results from CSSE, Polaris, and Black Duck SCA.
  3. **Enhanced Polaris SCA Results:**

     We’ve added a dependency tree and component nature (transitive vs. direct) to Polaris SCA results,
     helping developers to more easily identify the origins of vulnerable components.
- When applicable—that is, when running Polaris scans on an Apple®
  silicon system—Code Sight now downloads the
  command-line interface (CLI) for Apple silicon from the Polaris server.
- The command-line interface used by Polaris (Bridge CLI) has been upgraded.
  Code Sight has been upgraded as well, to use the new technology. This does not affect either the behavior or the
  user interface of Code Sight.

Code Sight now supports the following development environments:

- Android Studio 2024.3.1
- Eclipse 2025-03 (4.35)

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 2023-03 (4.27)
- Eclipse 2023-06 (4.28)
- VS Code 1.91
- VS Code 1.92

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Android Studio 2023.2.1
- VS Code 1.93

## See also

Code Sight Support Matrix

Code Sight Known Issues
