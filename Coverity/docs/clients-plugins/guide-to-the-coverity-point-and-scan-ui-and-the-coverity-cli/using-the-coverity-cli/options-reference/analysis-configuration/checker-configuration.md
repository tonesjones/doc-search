---
title: "Checker configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checker-configuration.html"
content_id: "hBgoMbRF0SL7mF6LTM0eZA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:07.345617+00:00"
---

# Checker configuration

The following keys determine what checkers to use in analysis.

| Key | Type | Description |
| --- | --- | --- |
| `all` | Boolean | Indicates whether all checkers should be enabled. Default: `false` |
| `all-security` | Boolean | Indicates whether all security checkers should be enabled. This includes the Security, Android Security, and Web App Security categories, as well as other security checkers that require explicit enablement. Default: `false` |
| `android-security` | Boolean | Java, Kotlin: If set to `true`, enables Android security checkers. Default: `false` |
| `audit` | Boolean | When `true`, enables audit checkers for C#, Java, JavaScript, TypeScript, and Visual Basic. Default: `false` |
| `brakeman` | Boolean | For Ruby only: Indicates whether the brakeman checkers should be enabled or disabled. Default: `true` |
| `c-family-security` | Boolean | Enables C, C++, Objective-C, and Objective-C++ security-related checkers that are disabled by default. |
| `checker-config` | Map from a string to a specific checker configuration | A map from a checker name to a configuration for the checker. The configuration indicates whether the checker should be enabled or not and allow users to set options used to configure the checker.  Default: empty map |
| `codexm` | array of strings | Specifies CodeXM (.cxm) files to use in the analysis. |
| `concurrency` | Boolean | Enables C and C++ concurrency checkers that are disabled by default. |
| `cra` | Boolean | Enables EU Cyber Resilience Act (CRA) analysis mode. |
| `default` | Boolean | Specifies whether to enable the default set of checkers.  - Set to `true` to enable the default set of checkers. - Set to `false` to get finer control over which checkers are enabled.   Default: `true` |
| `pmd` | Boolean | Enables or disables PMD analysis for APEX code. |
| `recommended-security-checkers` | Boolean | Enables or disables the recommended security checkers.  Default: `true` |
| `rule` | Boolean | Enables or disables C and C++ rule checkers. |
| `webapp-security` | Web app security configuration | Specifies how Web application security analysis should be done. By default, the Web app security checkers are enabled with an aggressiveness level of `low`. |
