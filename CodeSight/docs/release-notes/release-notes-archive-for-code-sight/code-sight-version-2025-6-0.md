---
title: "Code Sight version 2025.6.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.6.0.html"
content_id: "TTZRcHmgTWLU100czZpVTw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.293569+00:00"
---

# Code Sight version 2025.6.0

Version 2025.6.0 adds enhancements to the display of SCA issues in JetBrains IDEs, including IntelliJ IDEA.
For VS Code, it also adds the Black Duck Assist feature.

## Enhancements

- Release 2025.6.0 adds several enhancements to the display of SCA issues in JetBrains IDEs, including IntelliJ IDEA:
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
- In VS Code, Black Duck Assist is now available in Code Sight for users who have
  authenticated a Polaris server and enabled Black Duck Assist.
  This feature provides AI-generated remediation guidance for SAST issues directly within your IDE.

Code Sight now supports the following development environments:

- Eclipse 2025-06 (4.36)

## Bug fixes

- Resolved an issue in VS Code where Code Sight would prevent users from selecting a previously downloaded
  Detect ZIP file if a network error had blocked the automatic download from the Black Duck SCA repository.
  UD-15316
- In the Visual Studio code editor, the underline to highlight a Rapid Scan Static issue was not matching the issue’s description. This has now been fixed.
  UD-15232

## Discontinued support

Support for the following development environments has been discontinued:

- VS Code 1.93

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2023-09 (4.29)
- VS Code 1.94

## See also

Code Sight Support Matrix

Code Sight Known Issues
