---
title: "Coverity 2024.6.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.6.1-release-notes.html"
content_id: "Z4cRcB9F_mt7rJghVkx9ww"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:29.984016+00:00"
---

# Coverity 2024.6.1 Release Notes

## Important information for 2024.6.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2024.6.1

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.6.1

#### Bug fixes

CNC-2953
:   Reported in version: 2024.6.0
:   Fixed a Coverity cloud deployment issue that occurred with Connect web application high availability (HA) deployed, where users were unable to login to certain Connect web application URLs.

IM-31728
:   Reported in version: 2023.3.2
:   You can use the new `--ignore_corrupted_events` option for the `cov-archive` command to bypass PL/pgSQL import errors in Coverity Connect. For this scenario, we advise to also raise a ticket with customer support and attach the `cov-archive.log` file to help identify the root cause of the problem.

IM-31917
:   Reported in version: 2023.12.0
:   Fixed a Coverity Connect issue where, when selecting a defect, the source browser would not jump to the correct line.

IM-31993
:   Reported in version: 2024.6.0
:   Fixed issue with the Export Defect Handler that enables non-Jira external bug tracking system integration in Coverity Connect.

IM-32080
:   Reported in version: 2024.6.0
:   Fixed Coverity Connect issues when performing operations when a context path is configured, which resulted in 404-type errors.

### Coverity Report Generators 2024.6.1

#### Bug fixes

RG-1876, RG-1888
:   Reported in version: 2023.12.0, 2023.9.0
:   The CWE/SANS Top 40 weaknesses are correctly displayed in the Synopsys Software Integrity Report.

## Coverity Analysis 2024.6.1

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.6.1

#### Bug fixes

SAT-45896
:   Reported in version: unspecified
:   Fixed an issue when uploading results to Polaris when a defect is detected in the `main` function in a top-level file at the root of the directory tree, after path stripping.
