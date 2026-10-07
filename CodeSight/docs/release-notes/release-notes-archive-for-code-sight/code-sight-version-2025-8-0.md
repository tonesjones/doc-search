---
title: "Code Sight version 2025.8.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.8.0.html"
content_id: "_IlfbaMc4I0OQ_6cIP4PTg"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.195904+00:00"
---

# Code Sight version 2025.8.0

Version 2025.8.0 adds a few features to improve ease of use.

## Enhancements

- In IntelliJ, Local View now supports filters for Polaris issues.
  Users now have the same filter selections as they do in Team View.
- In Team View for Microsoft Visual Studio, you can now triage Coverity Connect issues from a new Code Sight Triage panel.
  The panel supports all the fields that are available in the Coverity Connect interface, including custom attributes.
- Version 2025.8.0 adds a Chat Participant as a new AI-powered assistant into Copilot Chat in VS Code.
  This feature is designed to streamline extension usage, including onboarding to Team View and Local View, and scan configuration,
  making it easier to get started and interact with Code Sight functionality directly within your development environment.

  When Code Sight is enabled, the `blackduck-assist` chat participant will appear in the chat participant list
  in the Copilot Chat view.

  To use the Copilot Chat Participant, you must have an active GitHub Copilot license.

Code Sight now supports the following development environments:

- Version 2025.2 of JetBrains IDEs, including IntelliJ IDEA.
- VS Code 1.103

## Discontinued support

Support for the following development environments has been deprecated, and will be discontinued in a future release of Code Sight:

- Eclipse 2023-09 (4.29)
- VS Code 1.94

Support for the following Black Duck product versions has been deprecated, and will be discontinued in a future release of Code Sight:

- **Polaris users:**

  You must upgrade Code Sight to version 2025.4.0 or a later version by September 15, 2025.
  Failure to upgrade will result in an inability to interact with Polaris.

  For more information, please see
  [[ANNOUNCEMENT] Reminder - Polaris API Deprecations and Important Due Dates for API and Bridge Upgrade Requirements](https://community.blackduck.com/s/question/0D5Uh00000ix5u5KAA/announcement-reminder-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements).

## See also

Code Sight Support Matrix

Code Sight Known Issues
