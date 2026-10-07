---
title: "Code Sight version 2023.11.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.11.0.html"
content_id: "IDG0OST~tt2EOCvwaAApbA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.054952+00:00"
---

# Code Sight version 2023.11.0

In version 2023.11.0, the interface for authenticating scanning products has been streamlined. For IntelliJ (the JetBrains family) and VS Code, remote issues
from the Coverity server now appear in Team View rather than the Code Analysis view. When you configure remote Coverity issues, you can choose which Project and
Stream to display.
Multiple source streams can accommodate multiple Projects or Streams.

## Enhancements

- When you install Coverity, Code Sight detects whether your platform runs on x86 or on Apple silicon, and downloads the appropriate installer.

  CAUTION:

  This does not work when installing Coverity from an x86 version of your IDE while running on an Apple silicon machine.
  See known issue UD-12727.
- Enabling or authenticating an analysis product now uses the standard Authentication Preferences interface for that product.
- In IntelliJ and VS Code, remote issues detected by Coverity Connect and Coverity on Polaris now display in Team View.
  The Remote mode in the Code Analysis view has been removed. Issues detected locally continue to display in the Code Analysis view.

  If previously you had a stream or project configured in a coverity.conf or polaris.yml file,
  to view remote issues you will need to configure the stream or project in the Preferences → Sources panel.
  (Local scans will continue to use coverity.conf or polaris.yaml for stream and project configuration.)

  These changes do not apply to Eclipse or Visual Studio.
- The Code Sight documentation has been reorganized to accommodate the multiple products Code Sight now supports, be easier to navigate,
  and to foreground setup requirements.

Code Sight now supports the following development environments:

- CLion™

  For currently supported versions of CLion, please see the Support matrix page.

  Custom build commands will be required for scanning with Coverity.
  For information about setting these up, see Specifying custom build tools.
- Eclipse 2023-09 (4.29)
- VS Code 1.83

Code Sight now supports the following Black Duck product versions:

- Black Duck 2023.10

## Discontinued support

Support for the following development environments has been discontinued:

- Eclipse 2021-12 (4.22)
- VS Code 1.77

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- VS Code 1.79

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- Black Duck 2022.2

## See also

Code Sight Support Matrix

Code Sight Known Issues
