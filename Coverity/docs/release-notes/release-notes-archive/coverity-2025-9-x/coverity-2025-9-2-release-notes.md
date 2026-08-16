---
title: "Coverity 2025.9.2 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.9.2-release-notes.html"
content_id: "qXmMpLdXyM8Sb~O7A8wLAA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:15.426133+00:00"
---

# Coverity 2025.9.2 Release Notes

## Important information for 2025.9.2

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2025.9.2

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.9.2

#### New or changed features

COVDOCS-1915
:   For an on-premises Coverity cloud 2025.9.2 release deployment that uses OCI Redis and MinIO, this release provides new files, Helm keys, and documentation designed to enable you to pull and manage Bitnami images that have been migrated to a new bitnamilegacy repository. Refer to the *Coverity Cloud Deployment Administrator and User Guide*.

#### Bug fixes

COVDOCS-1892
:   Reported in version: unspecified
:   For Dell ECS and for generic custom domains, this release includes new environment variables for custom certificates and new Coverity Connect Helm keys that accept annotations to mount additional storage service storage volumes. Also, the documentation provides more thorough guidance on deploying custom domains for storage service configurations. Refer to the *Coverity Cloud Deployment Administrator and User Guide*.

## Coverity Documentation 2025.9.2

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.9.2

#### Bug fixes

COVDOCS-1954
:   Reported in version: unspecified
:   For Coverity cloud deployments, this release increases the maximum hostname size from a limit of 36 characters to a tested limit of 46 characters. See the *Coverity Cloud Deployment Administrator and User Guide*
