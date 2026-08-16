---
title: "Coverity 2023.9.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2023.9.1-release-notes.html"
content_id: "~SggCrsb1~~zBcsKt7qEZg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:42.025628+00:00"
---

# Coverity 2023.9.1 Release Notes

## Important information for 2023.9.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

## Coverity Platform 2023.9.1

This section provides release notes for Coverity Platform components.

### Coverity Connect 2023.9.1

#### Bug fixes

IM-30824
:   Reported in version: 2022.6.0
:   When selecting "Restrict Issues emailed to the following project", only emails concerning the project mentioned in the notification box will be sent.
