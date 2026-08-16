---
title: "Coverity 2025.9.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.9.1-release-notes.html"
content_id: "wbt49WiFfDXbdjDlc1NE2Q"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:16.087392+00:00"
---

# Coverity 2025.9.1 Release Notes

## Important information for 2025.9.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2025.9.1

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.9.1

#### Bug fixes

IM-33230
:   Reported in version: unspecified
:   Fixed a critical out-of-memory issue caused by large snapshot tables, leading to server crashes during API calls.

IM-33292
:   Reported in version: unspecified
:   serverInfo/messageOfTheDay GET API now doesn't require `manageServerSettings` Permission.

## Coverity Analysis 2025.9.1

This section provides release notes for Coverity Analysis components.

### Coverity Commands 2025.9.1

#### Bug fixes

IM-33299
:   Reported in version: 2024.12.0, 2025.3.0, 2025.6.0
:   Fixed an issue related to special character handling in stream names within Coverity's management tools.

### Coverity Compilers and Capture 2025.9.1

#### Bug fixes

CMPCPP-15353
:   Reported in version: unspecified
:   Fix the handling of -stdlib++-isystem.

CMPCPP-15356
:   Reported in version: unspecified
:   See CMPCPP-15349.

CMPCPP-15372
:   Reported in version: unspecified
:   See CMPCPP-15345.

CMPJ-2471
:   Reported in version: 2025.9.0
:   Fix issue while trying to replay intermediate directory when Java webapps are present without other non-C TUs.

COVCLI-4100
:   Reported in version: 2025.9.0
:   In the Coverity 2025.9.0 release, a bug was introduced into the Coverity CLI such that the current working directory was being set incorrectly when running user supplied clean and build commands. In the 2025.9.1 release, this was fixed so that the current working directory for user supplied clean and build commands will be set to the project directory as was done in previous releases.

## Coverity Documentation 2025.9.1

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.9.1

#### Bug fixes

COVDOCS-1855
:   Reported in version: 2025.3.0
:   Two `cov-analyze` options for the INTEGER_OVERFLOW checker were added in recent releases, but in the *Command Reference* they were missing from the "Options: Aggressiveness level" topic for `cov-analyze`. They have now been added to the table, "Increasing aggressiveness from 'medium' to 'high'".
