---
title: "Code Sight version 2020.6"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2020.6.html"
content_id: "UiNeaoJWognfD1mvIoRmnw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.873570+00:00"
---

# Code Sight version 2020.6

In the 2020.6 release of the Black Duck® Code Sight™ plug-in,
new IDE versions are supported and various bugs have been fixed.

## Enhancements

- For the JetBrains IDEs (IntelliJ, PhpStorm, PyCharm, RubyMine, and WebStorm), version 2020.1 is now supported.
- For Microsoft VS Code, versions 1.44 and 1.45 are now supported.
  (The VS Code version of Code Sight is a beta release.)
- For Eclipse, version 2020-03 (4.15) is now supported.
- The JetBrains environments RubyMine, PhpStorm, and WebStorm can now use Code Sight to run Black Duck scans.
- When you start Code Sight for the first time, it now displays a Code Sight Configuration
  page that lets you choose which tool you want to install first.
- With appropriate permission and enablement, as of 2020.6 you can run Black Duck scans without having to first install Coverity Analysis.
  When Black Duck is the only tool in use, the Scans panel does not display single-file scan errors.
- The Code Sight Preferences panel now shows whether “credentials”
  (user authentication and the server name) are valid.
  If there is a current problem with the connection to the server, it displays an error message.
- To improve performance time, Black Duck scans no longer report Policy Violations.
  If you want to see Policy Violation reports, you can enable them by setting the environment variable
  `SYNOPSYS_DESKTOP_BD_ENABLE_POLICY_VIOLATIONS` to equal `1`.
  To disable Policy Violation reports once more, set the value of the variable to empty
  or remove the variable from your environment altogether.

## Discontinued support

Code Sight no longer works with Black Duck instances whose version is earlier than 2020.2.

- As of Code Sight 2020.6, only Black Duck instances of version 2020.02, or a later
  version, are supported. These instances use version 2 of the Black Duck API.

## Bug fixes

- In Visual Studio Code, fixed the navigation when multiple events are found on the same line of code.
  Now the currently selected event appears at the top of the pop-up list.
  UD-4035
- Fixed an issue in Eclipse, where after an upgrade from a previous version of Code Sight, the plug-in would sometimes
  fail to report issues or notifications displayed by the previous version.
  UD-4636
- Enabled workaround of an issue where Code Sight for Visual Studio changes the build output verbosity.
  To avoid this behavior, set the environment variable `SYNOPSYS_DESKTOP_DISABLE_COMPILED_EMIT` to equal `1`.
  UD-4683
- Fixed an issue with Black Duck scans where Policy Violations were not displayed.
  This occurred when Policy Violations had Vulnerability Conditions set to `"Exploit Available = Yes"`.
  UD-4909

  Note:
  To improve performance time, as of Code Sight 2020.6, Black Duck scans do not report Policy Violations
  unless you have enabled them by setting the environment variable
  `SYNOPSYS_DESKTOP_BD_ENABLE_POLICY_VIOLATIONS` to equal `1`.
- Fixed a Black Duck scanning issue where components that reported
  Policy Violations but no Security Vulnerabilities would not display their results.
  UD-4985
