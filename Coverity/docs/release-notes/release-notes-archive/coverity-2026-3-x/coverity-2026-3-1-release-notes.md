---
title: "Coverity 2026.3.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2026.3.1-release-notes.html"
content_id: "cBTE4VrvpKrZbRhdWmyWew"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:10.625728+00:00"
---

# Coverity 2026.3.1 Release Notes

## Important information for 2026.3.1

Support for this version of Coverity will be discontinued 18 months after the next major release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Analysis 2026.3.1

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2026.3.1

#### New or changed features

SAT-32857
:   Added support for passing regular expressions to --strip-path. Regular expressions must start with the '^' character and represent an absolute path.

### Coverity CLI 2026.3.1

#### Bug fixes

COVCLI-4355
:   Reported in version: unspecified
:   Thin client HFI analysis with caching disabled could previously fail when TUs changed due to replay. This has now been fixed.

### Coverity Compilers and Capture 2026.3.1

#### Bug fixes

CMPCPP-15281
:   Reported in version: unspecified
:   Fixed missing built-in types and functions related to ARM64 NEON. Also, fixed catastrophic error related to GNU #pragma GCC target and assignment operator class member functions.
