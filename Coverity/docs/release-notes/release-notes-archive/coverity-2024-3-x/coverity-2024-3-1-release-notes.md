---
title: "Coverity 2024.3.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.3.1-release-notes.html"
content_id: "PuAJyKthoMlvlXfM2U1fnw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:33.442788+00:00"
---

# Coverity 2024.3.1 Release Notes

## Important information for 2024.3.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

## Coverity Platform 2024.3.1

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.3.1

#### Bug fixes

IM-31298
:   Reported in version: 2023.6.0, 2023.12.0
:   Fixed issue where the **Edit Settings** dialog for a View was populated with incorrect data.

IM-31638
:   Reported in version: 2023.12.0, 2023.3.5
:   Fixed issue with the `GET` operation for the REST API `/api/v2/streams` endpoint, where it was earlier returning an incorrect list of streams for non-admin users.

## Coverity Analysis 2024.3.1

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.3.1

#### New or changed features

COVGUI-2534
:   A new checkbox in the Point and Scan login page allows users to use 2-step SSO authentication (via the default browser) to complete the SSO login for Coverity Connect version 2023.12.0 or newer.

    To use 2-step SSO authentication (via the default browser) with Coverity Connect version 2023.12.0 or newer, select the checkbox.
    To use the legacy SSO login (within Point and Scan), keep the checkbox clear. This works with all supported Coverity Connect versions.

#### Bug fixes

COVGUI-2533
:   Reported in version: 2023.12.0, 2023.9.2
:   Resolved issue with SSO login via the Point and Scan application for Coverity Connect version less than 2023.6.0, where the encoutered error was "Error: An object could not be cloned."

### Coverity Compilers and Capture 2024.3.1

#### Bug fixes

CMPCPP-14427
:   Reported in version: 2024.3.0
:   Fixed an issue where C++14 variable templates could cause serious runtime performance and memory consumption regressions in `cov-emit`.

CMPCSH-2014
:   Reported in version: unspecified
:   Addressed an issue with `dotnet` Razor code generation in "record with source" workflows.

### Coverity Point and Scan 2024.3.1

#### New or changed features

COVGUI-2534
:   A new checkbox in the Point and Scan login page allows users to use 2-step SSO authentication (via the default browser) to complete the SSO login for Coverity Connect version 2023.12.0 or newer.

    To use 2-step SSO authentication (via the default browser) with Coverity Connect version 2023.12.0 or newer, select the checkbox.
    To use the legacy SSO login (within Point and Scan), keep the checkbox clear. This works with all supported Coverity Connect versions.

#### Bug fixes

COVGUI-2533
:   Reported in version: 2023.12.0, 2023.9.2
:   Resolved issue with SSO login via the Point and Scan application for Coverity Connect version less than 2023.6.0, where the encoutered error was "Error: An object could not be cloned."
