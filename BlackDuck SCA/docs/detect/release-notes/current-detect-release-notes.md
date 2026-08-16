---
title: "Current Detect release notes"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/current-detect-release-notes.html"
content_id: "hpkc4_tDlAR2mPi5vJMIYg"
version: "11.5.1"
section: "Release Notes"
scraped_at: "2026-08-08T23:43:57.757385+00:00"
---

# Current Detect release notes

**Notices**

Synopsys Detect has been renamed Black Duck® Detect with page links, documentation, and other URLs updated accordingly. Update any Detect documentation, or other bookmarks you may have. See the [Domain Change FAQ](https://community.blackduck.com/s/article/Black-Duck-Domain-Change-FAQ).

- Please make use of repo.blackduck.com and detect.blackduck.com for code downloads.

  - Detect script downloads should only be accessed via detect.blackduck.com.
  - Detect 10.0.0 and later will only work when using repo.blackduck.com.
  - If you are using Detect 8 or 9 it is essential to update to 8.11.2 or 9.10.1 respectively.
- Black Duck® SCA [SCA Scan Service (SCASS)](https://community.blackduck.com/s/question/0D5Uh00000O2ZSYKA3/black-duck-sca-new-ip-address-requirements-for-2025) requires customers add or update IP addresses configured in their network firewalls or allow lists. This action is required to successfully route scan data to the service for processing.

  - scass.blackduck.com - 35.244.200.22
  - na.scass.blackduck.com - 35.244.200.22
  - na.store.scass.blackduck.com - 34.54.95.139
  - eu.store.scass.blackduck.com - 34.54.213.11
  - eu.scass.blackduck.com - 34.54.38.252
- **Deprecation of Java 8 support** - In alignment with EU Cyber Resilience Act (CRA) requirements and compliance timelines, Java 8 support will be deprecated in the anticipated 2026 Q3 Detect 12.0.0 release.

## Version 11.5.1

### Resolved issues

- (IDETECT-5207) Fixed an IndexOutOfBoundsException in component location analysis that was due to space characters within a version string.
- (IDETECT-5247) Fixed a regression in the Gradle init script where phantom subprojects (modules without a `build.gradle` file) with dependencies declared in the root `build.gradle` were incorrectly assigned an empty configuration set, resulting in 0 components being detected.

### Dependency Updates

- Updated Component Locator Library to version 2.4.4

## Version 11.5.0

### Changed features

- The default output directory of the Quack Patch feature has been updated to use Detect scan output directory. For more information, see Quack Patch Documentation.
- CentOS support in Detect Docker Inspector has been deprecated and will be removed in 12.0.0. For more details, please see Docker Inspector Release Notes.

  - imageinspector.service.port.centos has been deprecated and will be removed in 12.0.0.
- Clarified documentation for `--detect.uv.dependency.groups.excluded`. Optional is not a dependency group in uv but a section defining extras, therefor supplying `optional` as a value has no effect and exclusions must reference the extra name directly (e.g., postgres, redis).

### Resolved issues

- (IDETECT-5125) Fixed failure during Python scans when the `requirements.txt` file contains Python extras syntax using square brackets, e.g.: `kopf[dev]>=1.3`
- (IDETECT-5090) Fixed PIP Native Inspector failure to parse `requirements.txt` lines that contain [PEP 508 environment markers](https://peps.python.org/pep-0508/).
- (IDETECT-5056) Fixed a Cargo Lock detector failure to parse the caret symbol '^' used in `Cargo.toml` dependency declarations.
- (IDETECT-5071) Fixed an issue with Simple Build Tool (sbt) evictions being included in the BOM.
- (IDETECT-5069) Fixed Setuptools parsing for unsupported install_requires syntax in setup.py: Detect now fails fast and logs an error instead of silently misparsing, generating an incorrect BOM, and incorrectly reporting success.
- (IDETECT-5140) Changed the default output directory of the Quack Patch feature to use Detect scan output directory instead of the current working directory.
- (IDETECT-5121) Include Quack Patch output directory as part of diagnostic zip when the feature is enabled.
- (IDETECT-5064) Updated the Gradle init script to explicitly assign an empty configuration set to phantom projects (container modules lacking a `build.gradle` file). This change prevents tools injected by plugins such as Detekt and Ktlint from being included in the dependency report.
- (IDETECT-5097) Updated the Gradle init script to enumerate configurations within `gradle.projectsEvaluated`, ensuring that all `afterEvaluate` callbacks, including those from the Android Gradle Plugin (AGP), have completed before configuration processing begins.
- (IDETECT-5163) Updated the Bazel detector to treat exit code `3` from `query` and `cquery` commands as a partial success. When encountered, the detector now processes any available output and issues a warning indicating that dependency results may be incomplete.
- (IDETECT-5053) / (IDETECT-4988) Fixed pip inspector to correctly parse PEP 440 direct reference packages (`name @ url`), ensuring these packages are included in the dependency tree rather than being omitted.
- (IDETECT-5078) Rather then fail, Detect will now complete scans and generate empty BOMs when a Python Setuptools project has no dependencies.
- (IDETECT-5079) Allow Detect scans to finish with success even if no configured binary file patterns (e.g., .jar, .war, .zip) are found.
- (IDETECT-5118) Fixed UV Lockfile Detector to respect excluded dependency groups for optional‑dependencies. Optional extras specified in exclusion flags are now correctly excluded alongside development dependencies.
- (IDETECT‑5126) Fixed a BitBake layer misidentification issue caused by project folder names colliding with layer names. The detector now resolves layers deterministically, preferring the deepest valid match and falling back to the first valid layer when necessary.
- (IDETECT-5071) Fixed an issue with Simple Build Tool (sbt) evictions being included in the BOM. Dependencies that requested an evicted version are now reported with the version that replaced it.

### Dependency Updates

- Updated Project Inspector to version 2026.6.0 ensuring continued security compliance.
