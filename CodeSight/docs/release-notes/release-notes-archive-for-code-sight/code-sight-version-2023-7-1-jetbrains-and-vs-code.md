---
title: "Code Sight version 2023.7.1 (JetBrains and VS Code)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2023.7.1-jetbrains-and-vs-code-.html"
content_id: "2zACRlzKCjTDqD50~_GmLQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.175285+00:00"
---

# Code Sight version 2023.7.1 (JetBrains and VS Code)

This version is a hotfix that corrects a couple of issues with the plug-in in JetBrains IDEs, including IntelliJ, and in VS Code.

## Bug fixes

- Fixed an issue in VS Code where selecting a contributing event for a Software Risk Manager issue
  would cause the Issue Details tab to spin indefinitely. As of this bug fix, Team View reports all child events.
  UD-12220
- Fixed a bug where opening a file that had special characters (such as '[' or ']') in the file path
  would cause Code Sight to throw an exception in IntelliJ and other JetBrains IDEs.
  UD-11991

## See also

Code Sight Support Matrix

Code Sight Known Issues
