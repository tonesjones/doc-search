---
title: "Code Sight version 2024.3.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2024.3.0.html"
content_id: "THomzIPxMl0GTSHOeUXr2w"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.901427+00:00"
---

# Code Sight version 2024.3.0

Highlights of the 2024.3.0 release include Visual Studio support for Software Risk Manager issues in Team View;
and in Visual Studio Code, interactively enabling or disabling telemetry data collection for all IDEs
(telemetry collection is now disabled unless you explicitly enable it). Version 2024.3.0 also supports building with Bazel
in Coverity 2024.3.0.

## Enhancements

- In Visual Studio, the Code Sight interface now supports Team View for displaying remote issues
  reported by Software Risk Manager servers.
- As of Coverity 2024.3.0, Code Sight supports Bazel.
  Using the Coverity-Bazel integration is described in detail in the
  [*Coverity Analysis User and Administrator Guide*](https://documentation.blackduck.com/bundle/coverity-docs/page/webhelp-files/covanalysis_start.html).
  Code Sight users also need to add certain project settings to their project-specific coverity.conf file:
  See Building with Bazel for particulars.
- In VS Code, you can now enable or disable telemetry collection. If you choose to enable telemetry collection this way,
  it will be enabled for all IDEs on your system that run Code Sight 2024.3.0.
  Telemetry collection is disabled until you explicitly enable it.

Code Sight now supports the following development environments:

- Android™ Studio 2023.2.1
- VS Code 1.87

## Bug fixes

- Fixed an issue where, when upgrading Code Sight from the Eclipse marketplace, the plug-in (not the IDE) would hang on restart.
  UD-12689

## Discontinued support

Support for the following development environments has been discontinued:

- IntelliJ 2022.1
- VS Code 1.81

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- IntelliJ 2022.2
- Visual Studio 2017

## See also

Code Sight Support Matrix

Code Sight Known Issues
