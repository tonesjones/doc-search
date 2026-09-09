---
title: "Current Detect release notes"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/current-detect-release-notes.html"
content_id: "hpkc4_tDlAR2mPi5vJMIYg"
version: "12.0.0"
section: "Release Notes"
scraped_at: "2026-09-07T21:14:51.404000+00:00"
---

# Current Detect release notes

**Notices**

- Please make use of repo.blackduck.com and detect.blackduck.com for code downloads.

  - Detect script downloads should only be accessed via detect.blackduck.com.
  - Detect 10.0.0 and later will only work when using repo.blackduck.com.
- Black Duck® SCA [SCA Scan Service (SCASS)](https://community.blackduck.com/s/question/0D5Uh00000O2ZSYKA3/black-duck-sca-new-ip-address-requirements-for-2025) requires customers add or update IP addresses configured in their network firewalls or allow lists. This action is required to successfully route scan data to the service for processing.

  - scass.blackduck.com - 35.244.200.22
  - na.scass.blackduck.com - 35.244.200.22
  - na.store.scass.blackduck.com - 34.54.95.139
  - eu.store.scass.blackduck.com - 34.54.213.11
  - eu.scass.blackduck.com - 34.54.38.252
- **Removal of Java 8 support** - Support for Java 8 has been removed in compliance with EU Cyber Resilience Act (CRA) requirements.
- **Deprecation of support for Java versions earlier than 17** - Support for Java versions earlier than 17 has been deprecated in Detect 12.0.0 and will be removed in 13.0.0 to align with EU Cyber Resilience Act (CRA) requirements and compliance timelines.
- **Deprecation of Docker Inspector** - Docker Inspector has been deprecated and will be removed in 13.0.0 release.

## Version 12.0.0

### New features

- The Bazel detector now classifies Bazel Central Registry (BCR) dependencies as direct or transitive when running in Bzlmod mode on Bazel 7.1 or later.
- Introduced the property `detect.project.version.create.when.no.components` (default: true). When configured to false, Detect will refrain from creating a project version in Black Duck® SCA in cases where no components are identified and no other scan tools are active.
- Introduced a property named `detect.diagnostic.archive.path`, which enables the specification of a custom path for the diagnostic archive.
- Added `detect.uv.dependency.groups.only` property for the UV CLI detector. To restrict scanning to specific dependency groups while excluding standard dependencies and optional extras, use this property. When set, Detect limits analysis to the explicitly listed dependency groups defined in the project's pyproject.toml. Multiple groups can be specified as a comma-separated list (e.g., `detect.uv.dependency.groups.only='dev,lint'`). This applies exclusively to groups under the `[dependency-groups]` section; extras under `[project.optional-dependencies]` are not included. If both this property and `detect.uv.dependency.groups.excluded` are configured, the exclusion setting takes precedence for any overlapping groups and Detect will log a warning.
- Added the `detect.npm.excluded.workspaces` and `detect.npm.included.workspaces` configuration properties to control which npm workspaces are included in a Detect scan. If a workspace is specified in both lists, the exclusion takes precedence. Added the `detect.npm.ignore.all.workspaces` property to exclude all npm workspaces when set to true, which is equivalent to excluding every workspace explicitly.
- Support for the following package managers have been extended:

  - RubyGems: 4.0.15
  - Gradle: 9.6.1
  - Maven: 3.9.16
  - Pnpm: 11.8.0
  - NPM: 11.13.0
  - Node.js: 24.17.0

### Changed features

- (IDETECT-5117) The UV detector now scans all dependency groups by default. In previous releases, only the default group was included in the scan. The detector now passes the `--all-groups` flag to the `uv tree` command, ensuring all groups defined under `[dependency-groups]` in `pyproject.toml` are included. To restrict the scan to specific groups, use the `detect.uv.dependency.groups.only` property.
- (IDETECT-5134) Enabled UTF-8 encoding when reading the pnpm-lock.yaml file allowing emojis and non-ASCII characters to be parsed.
- (IDETECT-5146) pnpm scans now complete when the pnpm-lock.yaml has no dependencies.
- Detect Docker Inspector support for RPM-based Linux platforms such as CentOS, and RedHat has been removed in 12.0.0.
- Renamed `detect.quack.patch.output` property to `detect.quack.patch.output.path` for improved clarity.
- `detect.bazel.workspace.rules` property removed.

### Resolved issues

- (IDETECT-5146) Resolved pnpm detector failing when there are no components present in the `pnpm-lock.yaml` file.
- (IDETECT-5134) Resolved pnpm detector failing when there are emojis present in the `pnpm-lock.yaml` file.

### Dependency Updates

- Upgraded direct and transitive dependencies throughout Detect, plugins and add-ons.

  - Detect Docker images were migrated to Chainguard.
  - Update ANTLR library to version 4.13.2.
  - Update Jackson libraries to version 2.22.0.
  - Update Java minimum version to 11.
  - Update Tika library to version 3.2.2.
  - Update Component Locator Library to version 2.4.5
