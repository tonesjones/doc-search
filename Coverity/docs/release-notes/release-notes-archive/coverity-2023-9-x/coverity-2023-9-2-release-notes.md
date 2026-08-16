---
title: "Coverity 2023.9.2 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2023.9.2-release-notes.html"
content_id: "aQURR3u3nbvKyIkbsYNsIQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:41.367624+00:00"
---

# Coverity 2023.9.2 Release Notes

## Important information for 2023.9.2

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

## Coverity Platform 2023.9.2

This section provides release notes for Coverity Platform components.

### Coverity Connect 2023.9.2

#### New or changed features

IM-30950
:   A new property, `udc.data.collection.disable`, has been added to `cim.properties`. To disable the collection of use and compliance data (UDC), set `udc.data.collection.disable` to `true`.

#### Bug fixes

CNC-2322
:   Reported in version: 2023.3.2, 2023.6.0
:   Fixed a performance issue in the `/api/v2/issues/search` and `/api/v2/issueOccurrences/search` REST API operations that occurred when the request body contained thousands of matchers per filter.

IM-30824
:   Reported in version: 2022.6.0
:   When selecting "Restrict Issues emailed to the following project", only emails concerning the project mentioned in the notification box will be sent.

IM-30898
:   Reported in version: 2023.3.0, 2023.3.2
:   Fixed issue related to the **Component Map** screen.

## Coverity Analysis 2023.9.2

This section provides release notes for Coverity Analysis components.

### Coverity Checkers 2023.9.2

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SATSEC-15537
:   Fixed a false positive for the `OPEN_REDIRECT` checker.

SATW-5303
:   The `CERT DCL60-CPP` checker no longer reports on symbols with no definition. It only reports on symbols with more than one definition.

### Coverity Compilers and Capture 2023.9.2

#### New or changed features

CMPCPP-13791
:   Added support for the Sony PS5 SDK 7.000 compiler.

CMPG-4353
:   Added support for Xtensa `xt-clang` compiler core `BBE32EP` on Windows.

#### Bug fixes

CMPCPP-13683
:   Reported in version: 2023.9.0
:   Fixed a file name normalization error that caused significant performance slowdown for the `cov-emit` command.

CMPCPP-13825
:   Reported in version: 2023.3.2
:   A fix has been added to the C/C++ compiler to avoid Coverity Connect errors such as:

    `Caused by: org.postgresql.util.PSQLException: ERROR: index row size 3568 exceeds btree version 3 maximum 2712 for index "uk_2ypxjm2ayrneyrjikigvmvq24"`
