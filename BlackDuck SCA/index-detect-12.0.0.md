# Black Duck Detect Documentation Index

> Auto-generated catalog for local RAG. Do not hand-edit topic rows — update `sources/detect-12.0.0/manifest.json` statuses and run `python scripts/build-index.py --product detect-12.0.0`.

## Corpus status

| Field | Value |
|-------|-------|
| Product | Black Duck Detect |
| Product key | `detect-12.0.0` |
| Version | **12.0.0** |
| Map ID | `j_bSwuxnjHv5ElV~TQrAQg` |
| TOC nodes | **207** |
| Progress | **207/207 done** (100.0%) · 0 pending · 0 skipped · 0 error |
| Last index build | 2026-09-07T21:17:36.336417+00:00 |
| Manifest | [sources/detect-12.0.0/manifest.json](sources/detect-12.0.0/manifest.json) |
| Raw TOC | [sources/detect-12.0.0/toc.json](sources/detect-12.0.0/toc.json) |
| Docs root | `docs/detect-12.0.0/` |

### Status legend

| Mark | Status | Meaning |
|------|--------|---------|
| `[ ]` | pending | Not scraped yet |
| `[x]` | done | Markdown written under `docs/` |
| `[-]` | skipped | Intentionally not scraped |
| `[!]` | error | Last scrape failed; retry later |

## How to resume

1. Filter `manifest.json` for `status` `pending` (or `error` to retry).
2. `python scripts/scrape-pending.py --product detect-12.0.0 --all-pending`
3. `python scripts/build-index.py --product detect-12.0.0` to refresh this index.

**Content API template:**

```
https://docs.blackduck.com/api/khub/maps/j_bSwuxnjHv5ElV~TQrAQg/topics/{contentId}/content
```

## Section overview

| Section | Topics | Pending | Done | Skipped | Error | Local root |
|---------|--------|---------|------|---------|-------|------------|
| Detect Properties | 53 | 0 | 53 | 0 | 0 | `docs/detect-12.0.0/detect-properties/` |
| Package Manager information for Detect | 40 | 0 | 40 | 0 | 0 | `docs/detect-12.0.0/package-manager-information-for-detect/` |
| Planning and running Detect | 29 | 0 | 29 | 0 | 0 | `docs/detect-12.0.0/planning-and-running-detect/` |
| Detect Integrations | 24 | 0 | 24 | 0 | 0 | `docs/detect-12.0.0/detect-integrations/` |
| Getting started with Detect | 19 | 0 | 19 | 0 | 0 | `docs/detect-12.0.0/getting-started-with-detect/` |
| Configuring Detect | 15 | 0 | 15 | 0 | 0 | `docs/detect-12.0.0/configuring-detect/` |
| Troubleshooting | 8 | 0 | 8 | 0 | 0 | `docs/detect-12.0.0/troubleshooting/` |
| Downloading and Installing Detect | 6 | 0 | 6 | 0 | 0 | `docs/detect-12.0.0/downloading-and-installing-detect/` |
| Release Notes | 4 | 0 | 4 | 0 | 0 | `docs/detect-12.0.0/release-notes/` |
| Detect Components | 4 | 0 | 4 | 0 | 0 | `docs/detect-12.0.0/detect-components/` |
| Viewing and managing Detect scan results | 2 | 0 | 2 | 0 | 0 | `docs/detect-12.0.0/viewing-and-managing-detect-scan-results/` |
| Introduction to Black Duck® Detect | 1 | 0 | 1 | 0 | 0 | `docs/detect-12.0.0/introduction-to-black-duck-detect/` |
| Detect requirements and release information | 1 | 0 | 1 | 0 | 0 | `docs/detect-12.0.0/detect-requirements-and-release-information/` |
| Detect Quickstart guide | 1 | 0 | 1 | 0 | 0 | `docs/detect-12.0.0/detect-quickstart-guide/` |

## Table of contents

- [x] [Introduction to Black Duck® Detect](docs/detect-12.0.0/introduction-to-black-duck-detect.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/introduction-to-black-duck-detect.html)
- [x] [Release Notes](docs/detect-12.0.0/release-notes.md) _(+3)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/release-notes.html)
  - [x] [Current Detect release notes](docs/detect-12.0.0/release-notes/current-detect-release-notes.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/current-detect-release-notes.html)
  - [x] [Release notes for previous Detect versions](docs/detect-12.0.0/release-notes/release-notes-for-previous-detect-versions.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/release-notes-for-previous-detect-versions.html)
  - [x] [Release notes for older Detect versions](docs/detect-12.0.0/release-notes/release-notes-for-older-detect-versions.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/release-notes-for-older-detect-versions.html)
- [x] [Detect requirements and release information](docs/detect-12.0.0/detect-requirements-and-release-information.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-requirements-and-release-information.html)
- [x] [Downloading and Installing Detect](docs/detect-12.0.0/downloading-and-installing-detect.md) _(+5)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/downloading-and-installing-detect.html)
  - [x] [Download Locations for Black Duck® Detect & Plugins](docs/detect-12.0.0/downloading-and-installing-detect/download-locations-for-black-duck-detect-and-plugins.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/download-locations-for-black-duck-detect-plugins.html)
  - [x] [Upgrading Detect](docs/detect-12.0.0/downloading-and-installing-detect/upgrading-detect.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/upgrading-detect.html)
  - [x] [Detect Version Management](docs/detect-12.0.0/downloading-and-installing-detect/detect-version-management.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-version-management.html)
  - [x] [Detect Code Verification](docs/detect-12.0.0/downloading-and-installing-detect/detect-code-verification.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-code-verification.html)
  - [x] [Detect Air Gap mode](docs/detect-12.0.0/downloading-and-installing-detect/detect-air-gap-mode.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-air-gap-mode.html)
- [x] [Detect Quickstart guide](docs/detect-12.0.0/detect-quickstart-guide.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-quickstart-guide.html)
- [x] [Getting started with Detect](docs/detect-12.0.0/getting-started-with-detect.md) _(+7)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/getting-started-with-detect.html)
  - [x] [Detect Key Concepts and Terms](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms.md) _(+11)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-key-concepts-and-terms.html)
    - [x] [BDIO](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/bdio.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bdio.html)
    - [x] [Detectors](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/detectors.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detectors.html)
    - [x] [Vulnerability Impact Analysis](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/vulnerability-impact-analysis.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/vulnerability-impact-analysis.html)
    - [x] [Inspectors](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/inspectors.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/inspectors.html)
    - [x] [JAR](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/jar.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/jar.html)
    - [x] [Detect Properties](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/detect-properties.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-properties.html)
    - [x] [Run](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/run.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/run.html)
    - [x] [Software Composition Analysis (SCA)](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/software-composition-analysis-sca.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/software-composition-analysis-sca-.html)
    - [x] [Scans and projects](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/scans-and-projects.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/scans-and-projects.html)
    - [x] [Script](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/script.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/script.html)
    - [x] [Tools](docs/detect-12.0.0/getting-started-with-detect/detect-key-concepts-and-terms/tools.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/tools.html)
  - [x] [How Detect Works](docs/detect-12.0.0/getting-started-with-detect/how-detect-works.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/how-detect-works.html)
  - [x] [Detect basic workflow](docs/detect-12.0.0/getting-started-with-detect/detect-basic-workflow.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-basic-workflow.html)
  - [x] [Detect Processing](docs/detect-12.0.0/getting-started-with-detect/detect-processing.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-processing.html)
  - [x] [Detect configuration overview](docs/detect-12.0.0/getting-started-with-detect/detect-configuration-overview.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-configuration-overview.html)
  - [x] [User role requirements when running with Black Duck](docs/detect-12.0.0/getting-started-with-detect/user-role-requirements-when-running-with-black-duck.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/user-role-requirements-when-running-with-black-duck.html)
  - [x] [Detect command line help options](docs/detect-12.0.0/getting-started-with-detect/detect-command-line-help-options.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-command-line-help-options.html)
- [x] [Configuring Detect](docs/detect-12.0.0/configuring-detect.md) _(+13)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/configuring-detect.html)
  - [x] [On the command line](docs/detect-12.0.0/configuring-detect/on-the-command-line.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/on-the-command-line.html)
  - [x] [Using environment variables](docs/detect-12.0.0/configuring-detect/using-environment-variables.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/using-environment-variables.html)
  - [x] [Using a configuration file](docs/detect-12.0.0/configuring-detect/using-a-configuration-file.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/using-a-configuration-file.html)
  - [x] [Project settings via JSON](docs/detect-12.0.0/configuring-detect/project-settings-via-json.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/project-settings-via-json.html)
  - [x] [Switching between multiple profiles](docs/detect-12.0.0/configuring-detect/switching-between-multiple-profiles.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/switching-between-multiple-profiles.html)
  - [x] [Additional configuration methods and details](docs/detect-12.0.0/configuring-detect/additional-configuration-methods-and-details.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/additional-configuration-methods-and-details.html)
  - [x] [Providing sensitive values such as credentials](docs/detect-12.0.0/configuring-detect/providing-sensitive-values-such-as-credentials.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/providing-sensitive-values-such-as-credentials.html)
  - [x] [Path properties](docs/detect-12.0.0/configuring-detect/path-properties.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/path-properties.html)
  - [x] [Property wildcard support](docs/detect-12.0.0/configuring-detect/property-wildcard-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/property-wildcard-support.html)
  - [x] [Java regular expression support](docs/detect-12.0.0/configuring-detect/java-regular-expression-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/java-regular-expression-support.html)
  - [x] [Shell script configuration and environment variables](docs/detect-12.0.0/configuring-detect/shell-script-configuration-and-environment-variables.md) _(+1)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/shell-script-configuration-and-environment-variables.html)
    - [x] [Quoting and escaping shell script arguments](docs/detect-12.0.0/configuring-detect/shell-script-configuration-and-environment-variables/quoting-and-escaping-shell-script-arguments.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/quoting-and-escaping-shell-script-arguments.html)
  - [x] [Project, Version, and Code Location Naming](docs/detect-12.0.0/configuring-detect/project-version-and-code-location-naming.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/project-version-and-code-location-naming.html)
  - [x] [BDIO aggregation](docs/detect-12.0.0/configuring-detect/bdio-aggregation.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bdio-aggregation.html)
- [x] [Planning and running Detect](docs/detect-12.0.0/planning-and-running-detect.md) _(+24)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/planning-and-running-detect.html)
  - [x] [Deciding how to use Detect](docs/detect-12.0.0/planning-and-running-detect/deciding-how-to-use-detect.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/deciding-how-to-use-detect.html)
  - [x] [Positioning Detect in the build process](docs/detect-12.0.0/planning-and-running-detect/positioning-detect-in-the-build-process.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/positioning-detect-in-the-build-process.html)
  - [x] [Installation Best Practices](docs/detect-12.0.0/planning-and-running-detect/installation-best-practices.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/installation-best-practices.html)
  - [x] [Choosing the working directory](docs/detect-12.0.0/planning-and-running-detect/choosing-the-working-directory.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/choosing-the-working-directory.html)
  - [x] [Choosing a run method (script, .jar, or Docker container)](docs/detect-12.0.0/planning-and-running-detect/choosing-a-run-method-script-jar-or-docker-container.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/choosing-a-run-method-script-.jar-or-docker-container-.html)
  - [x] [Running the Detect script](docs/detect-12.0.0/planning-and-running-detect/running-the-detect-script.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-the-detect-script.html)
  - [x] [Running the Detect .jar](docs/detect-12.0.0/planning-and-running-detect/running-the-detect-jar.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-the-detect-.jar.html)
  - [x] [Choosing the Detect target type](docs/detect-12.0.0/planning-and-running-detect/choosing-the-detect-target-type.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/choosing-the-detect-target-type.html)
  - [x] [Running with Black Duck® SCA](docs/detect-12.0.0/planning-and-running-detect/running-with-black-duck-sca.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-with-black-duck-sca.html)
  - [x] [Feature availability in online and offline Detect scanning](docs/detect-12.0.0/planning-and-running-detect/feature-availability-in-online-and-offline-detect-scanning.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/feature-availability-in-online-and-offline-detect-scanning.html)
  - [x] [Including and excluding Tools, Detectors, and Directories](docs/detect-12.0.0/planning-and-running-detect/including-and-excluding-tools-detectors-and-directories.md) _(+4)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/including-and-excluding-tools-detectors-and-directories.html)
    - [x] [Detect Tools](docs/detect-12.0.0/planning-and-running-detect/including-and-excluding-tools-detectors-and-directories/detect-tools.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-tools.html)
    - [x] [Detectors](docs/detect-12.0.0/planning-and-running-detect/including-and-excluding-tools-detectors-and-directories/detectors.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detectors.html)
    - [x] [Package Manager Exclusions](docs/detect-12.0.0/planning-and-running-detect/including-and-excluding-tools-detectors-and-directories/package-manager-exclusions.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/package-manager-exclusions.html)
    - [x] [Directory Exclusions](docs/detect-12.0.0/planning-and-running-detect/including-and-excluding-tools-detectors-and-directories/directory-exclusions.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/directory-exclusions.html)
  - [x] [Component Location Analysis](docs/detect-12.0.0/planning-and-running-detect/component-location-analysis.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/component-location-analysis.html)
  - [x] [Concurrent execution](docs/detect-12.0.0/planning-and-running-detect/concurrent-execution.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/concurrent-execution.html)
  - [x] [Detector search and accuracy](docs/detect-12.0.0/planning-and-running-detect/detector-search-and-accuracy.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detector-search-and-accuracy.html)
  - [x] [Running behind a proxy](docs/detect-12.0.0/planning-and-running-detect/running-behind-a-proxy.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-behind-a-proxy.html)
  - [x] [Running Detect within a Docker container](docs/detect-12.0.0/planning-and-running-detect/running-detect-within-a-docker-container.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-detect-within-a-docker-container.html)
  - [x] [Running Detect in air gap mode](docs/detect-12.0.0/planning-and-running-detect/running-detect-in-air-gap-mode.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-detect-in-air-gap-mode.html)
  - [x] [Output Status File](docs/detect-12.0.0/planning-and-running-detect/output-status-file.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/output-status-file.html)
  - [x] [Autonomous Scanning](docs/detect-12.0.0/planning-and-running-detect/autonomous-scanning.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/autonomous-scanning.html)
  - [x] [Container Scan](docs/detect-12.0.0/planning-and-running-detect/container-scan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/container-scan.html)
  - [x] [IaC Scan](docs/detect-12.0.0/planning-and-running-detect/iac-scan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/iac-scan.html)
  - [x] [Rapid Scan](docs/detect-12.0.0/planning-and-running-detect/rapid-scan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/rapid-scan.html)
  - [x] [Stateless Scan](docs/detect-12.0.0/planning-and-running-detect/stateless-scan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/stateless-scan.html)
  - [x] [Quack Patch (Early Access)](docs/detect-12.0.0/planning-and-running-detect/quack-patch-early-access.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/quack-patch-early-access-.html)
- [x] [Detect Components](docs/detect-12.0.0/detect-components.md) _(+3)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-components.html)
  - [x] [Tools](docs/detect-12.0.0/detect-components/tools.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/tools.html)
  - [x] [Detectors](docs/detect-12.0.0/detect-components/detectors.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detectors.html)
  - [x] [Inspectors](docs/detect-12.0.0/detect-components/inspectors.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/inspectors.html)
- [x] [Package Manager information for Detect](docs/detect-12.0.0/package-manager-information-for-detect.md) _(+26)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/package-manager-information-for-detect.html)
  - [x] [Bazel support](docs/detect-12.0.0/package-manager-information-for-detect/bazel-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bazel-support.html)
  - [x] [BitBake support](docs/detect-12.0.0/package-manager-information-for-detect/bitbake-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bitbake-support.html)
  - [x] [Cargo support](docs/detect-12.0.0/package-manager-information-for-detect/cargo-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/cargo-support.html)
  - [x] [Carthage support](docs/detect-12.0.0/package-manager-information-for-detect/carthage-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/carthage-support.html)
  - [x] [C/C++ (Clang) support](docs/detect-12.0.0/package-manager-information-for-detect/c-c-clang-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/c/c-clang-support.html)
  - [x] [Conan support](docs/detect-12.0.0/package-manager-information-for-detect/conan-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/conan-support.html)
  - [x] [Conda Support](docs/detect-12.0.0/package-manager-information-for-detect/conda-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/conda-support.html)
  - [x] [CPAN Support](docs/detect-12.0.0/package-manager-information-for-detect/cpan-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/cpan-support.html)
  - [x] [Dart Support](docs/detect-12.0.0/package-manager-information-for-detect/dart-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/dart-support.html)
  - [x] [Detect Docker image support](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support.md) _(+13)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-docker-image-support.html)
    - [x] [Detect Docker Inspector Release notes](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/detect-docker-inspector-release-notes.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-docker-inspector-release-notes.html)
    - [x] [Supported image formats](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/supported-image-formats.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/supported-image-formats.html)
    - [x] [Black Duck® Detect workflow](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/black-duck-detect-workflow.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/black-duck-detect-workflow.html)
    - [x] [File permissions](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/file-permissions.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/file-permissions.html)
    - [x] [Black Duck® Detect's scan target](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/black-duck-detects-scan-target.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/black-duck-detect-s-scan-target.html)
    - [x] [Isolating application components](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/isolating-application-components.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/isolating-application-components.html)
    - [x] [Inspecting Windows Docker images](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/inspecting-windows-docker-images.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/inspecting-windows-docker-images.html)
    - [x] [Inspecting Docker images on Windows](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/inspecting-docker-images-on-windows.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/inspecting-docker-images-on-windows.html)
    - [x] [Detect architecture overview](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/detect-architecture-overview.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-architecture-overview.html)
    - [x] [Advanced Detect topics](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/advanced-detect-topics.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/advanced-detect-topics.html)
    - [x] [Advanced properties](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/advanced-properties.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/advanced-properties.html)
    - [x] [Deploying Detect Docker Inspector](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/deploying-detect-docker-inspector.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/deploying-detect-docker-inspector.html)
    - [x] [Troubleshooting Docker Inspector](docs/detect-12.0.0/package-manager-information-for-detect/detect-docker-image-support/troubleshooting-docker-inspector.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/troubleshooting-docker-inspector.html)
  - [x] [Git project support](docs/detect-12.0.0/package-manager-information-for-detect/git-project-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/git-project-support.html)
  - [x] [GoLang support](docs/detect-12.0.0/package-manager-information-for-detect/golang-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/golang-support.html)
  - [x] [Gradle support](docs/detect-12.0.0/package-manager-information-for-detect/gradle-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/gradle-support.html)
  - [x] [Erlang/Hex/Rebar support](docs/detect-12.0.0/package-manager-information-for-detect/erlang-hex-rebar-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/erlang/hex/rebar-support.html)
  - [x] [Ivy (Ant) support](docs/detect-12.0.0/package-manager-information-for-detect/ivy-ant-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/ivy-ant-support.html)
  - [x] [Lerna support](docs/detect-12.0.0/package-manager-information-for-detect/lerna-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/lerna-support.html)
  - [x] [Maven support](docs/detect-12.0.0/package-manager-information-for-detect/maven-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/maven-support.html)
  - [x] [NPM support](docs/detect-12.0.0/package-manager-information-for-detect/npm-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/npm-support.html)
  - [x] [NuGet support](docs/detect-12.0.0/package-manager-information-for-detect/nuget-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/nuget-support.html)
  - [x] [Opam Support](docs/detect-12.0.0/package-manager-information-for-detect/opam-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/opam-support.html)
  - [x] [pnpm support](docs/detect-12.0.0/package-manager-information-for-detect/pnpm-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pnpm-support.html)
  - [x] [Python support](docs/detect-12.0.0/package-manager-information-for-detect/python-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/python-support.html)
  - [x] [Rush support](docs/detect-12.0.0/package-manager-information-for-detect/rush-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/rush-support.html)
  - [x] [SBT support](docs/detect-12.0.0/package-manager-information-for-detect/sbt-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/sbt-support.html)
  - [x] [Swift & Xcode support](docs/detect-12.0.0/package-manager-information-for-detect/swift-and-xcode-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/swift-xcode-support.html)
  - [x] [Yarn support](docs/detect-12.0.0/package-manager-information-for-detect/yarn-support.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/yarn-support.html)
- [x] [Detect Properties](docs/detect-12.0.0/detect-properties.md) _(+5)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-properties.html)
  - [x] [Basic Properties](docs/detect-12.0.0/detect-properties/basic-properties.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/basic-properties.html)
  - [x] [All Properties](docs/detect-12.0.0/detect-properties/all-properties.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/all-properties.html)
  - [x] [Detect configuration property details](docs/detect-12.0.0/detect-properties/detect-configuration-property-details.md) _(+20)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-configuration-property-details.html)
    - [x] [binary-scanner](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/binary-scanner.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/binary-scanner.html)
    - [x] [blackduck-server](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/blackduck-server.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/blackduck-server.html)
    - [x] [cleanup](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/cleanup.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/cleanup.html)
    - [x] [container-scanner](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/container-scanner.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/container-scanner.html)
    - [x] [debug](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/debug.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/debug.html)
    - [x] [default](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/default.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/default.html)
    - [x] [detector](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/detector.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detector.html)
    - [x] [general](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/general.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/general.html)
    - [x] [global](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/global.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/global.html)
    - [x] [iac-scan](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/iac-scan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/iac-scan.html)
    - [x] [impact-analysis](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/impact-analysis.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/impact-analysis.html)
    - [x] [logging](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/logging.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/logging.html)
    - [x] [paths](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/paths.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/paths.html)
    - [x] [project](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/project.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/project.html)
    - [x] [project-inspector](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/project-inspector.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/project-inspector.html)
    - [x] [proxy](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/proxy.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/proxy.html)
    - [x] [quack-patch](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/quack-patch.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/quack-patch.html)
    - [x] [rapid-scan](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/rapid-scan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/rapid-scan.html)
    - [x] [report](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/report.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/report.html)
    - [x] [signature-scanner](docs/detect-12.0.0/detect-properties/detect-configuration-property-details/signature-scanner.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/signature-scanner.html)
  - [x] [Detect Detector properties](docs/detect-12.0.0/detect-properties/detect-detector-properties.md) _(+27)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-detector-properties.html)
    - [x] [bazel](docs/detect-12.0.0/detect-properties/detect-detector-properties/bazel.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bazel.html)
    - [x] [bitbake](docs/detect-12.0.0/detect-properties/detect-detector-properties/bitbake.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bitbake.html)
    - [x] [cargo](docs/detect-12.0.0/detect-properties/detect-detector-properties/cargo.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/cargo.html)
    - [x] [conan](docs/detect-12.0.0/detect-properties/detect-detector-properties/conan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/conan.html)
    - [x] [conda](docs/detect-12.0.0/detect-properties/detect-detector-properties/conda.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/conda.html)
    - [x] [cpan](docs/detect-12.0.0/detect-properties/detect-detector-properties/cpan.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/cpan.html)
    - [x] [dart](docs/detect-12.0.0/detect-properties/detect-detector-properties/dart.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/dart.html)
    - [x] [docker](docs/detect-12.0.0/detect-properties/detect-detector-properties/docker.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/docker.html)
    - [x] [go](docs/detect-12.0.0/detect-properties/detect-detector-properties/go.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/go.html)
    - [x] [gradle](docs/detect-12.0.0/detect-properties/detect-detector-properties/gradle.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/gradle.html)
    - [x] [hex](docs/detect-12.0.0/detect-properties/detect-detector-properties/hex.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/hex.html)
    - [x] [lerna](docs/detect-12.0.0/detect-properties/detect-detector-properties/lerna.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/lerna.html)
    - [x] [maven](docs/detect-12.0.0/detect-properties/detect-detector-properties/maven.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/maven.html)
    - [x] [npm](docs/detect-12.0.0/detect-properties/detect-detector-properties/npm.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/npm.html)
    - [x] [nuget](docs/detect-12.0.0/detect-properties/detect-detector-properties/nuget.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/nuget.html)
    - [x] [opam](docs/detect-12.0.0/detect-properties/detect-detector-properties/opam.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/opam.html)
    - [x] [packagist](docs/detect-12.0.0/detect-properties/detect-detector-properties/packagist.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/packagist.html)
    - [x] [pear](docs/detect-12.0.0/detect-properties/detect-detector-properties/pear.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pear.html)
    - [x] [pip](docs/detect-12.0.0/detect-properties/detect-detector-properties/pip.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pip.html)
    - [x] [pnpm](docs/detect-12.0.0/detect-properties/detect-detector-properties/pnpm.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pnpm.html)
    - [x] [poetry](docs/detect-12.0.0/detect-properties/detect-detector-properties/poetry.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/poetry.html)
    - [x] [python](docs/detect-12.0.0/detect-properties/detect-detector-properties/python.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/python.html)
    - [x] [ruby](docs/detect-12.0.0/detect-properties/detect-detector-properties/ruby.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/ruby.html)
    - [x] [sbt](docs/detect-12.0.0/detect-properties/detect-detector-properties/sbt.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/sbt.html)
    - [x] [swift](docs/detect-12.0.0/detect-properties/detect-detector-properties/swift.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/swift.html)
    - [x] [uv](docs/detect-12.0.0/detect-properties/detect-detector-properties/uv.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/uv.html)
    - [x] [yarn](docs/detect-12.0.0/detect-properties/detect-detector-properties/yarn.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/yarn.html)
  - [x] [Deprecated Properties](docs/detect-12.0.0/detect-properties/deprecated-properties.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/deprecated-properties.html)
- [x] [Viewing and managing Detect scan results](docs/detect-12.0.0/viewing-and-managing-detect-scan-results.md) _(+1)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/viewing-and-managing-detect-scan-results.html)
  - [x] [Risk Report generation via Detect](docs/detect-12.0.0/viewing-and-managing-detect-scan-results/risk-report-generation-via-detect.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/risk-report-generation-via-detect.html)
- [x] [Troubleshooting](docs/detect-12.0.0/troubleshooting.md) _(+7)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/troubleshooting.html)
  - [x] [Collecting Detect log information](docs/detect-12.0.0/troubleshooting/collecting-detect-log-information.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/collecting-detect-log-information.html)
  - [x] [Common Detect complications](docs/detect-12.0.0/troubleshooting/common-detect-complications.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/common-detect-complications.html)
  - [x] [Detect Diagnostic mode](docs/detect-12.0.0/troubleshooting/detect-diagnostic-mode.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-diagnostic-mode.html)
  - [x] [Detect Exit Codes](docs/detect-12.0.0/troubleshooting/detect-exit-codes.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-exit-codes.html)
  - [x] [Common Detect troubleshooting solutions](docs/detect-12.0.0/troubleshooting/common-detect-troubleshooting-solutions.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/common-detect-troubleshooting-solutions.html)
  - [x] [Detect usage metrics collection](docs/detect-12.0.0/troubleshooting/detect-usage-metrics-collection.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-usage-metrics-collection.html)
  - [x] [Windows OS hints for Detect](docs/detect-12.0.0/troubleshooting/windows-os-hints-for-detect.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/windows-os-hints-for-detect.html)
- [x] [Detect Integrations](docs/detect-12.0.0/detect-integrations.md) _(+5)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-integrations.html)
  - [x] [Detect Jenkins Plugin](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin.md) _(+11)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-jenkins-plugin.html)
    - [x] [Release Notes for Jenkins Plugin](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/release-notes-for-jenkins-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/release-notes-for-jenkins-plugin.html)
    - [x] [Requirements for Black Duck® Detect for Jenkins](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/requirements-for-black-duck-detect-for-jenkins.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/requirements-for-black-duck-detect-for-jenkins.html)
    - [x] [Downloading, Installing, and Updating the Plugin](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/downloading-installing-and-updating-the-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/downloading-installing-and-updating-the-plugin.html)
    - [x] [Configuring the Jenkins Plugin](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/configuring-the-jenkins-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/configuring-the-jenkins-plugin.html)
    - [x] [Users and roles for Jenkins Plugin](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/users-and-roles-for-jenkins-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/users-and-roles-for-jenkins-plugin.html)
    - [x] [Running Black Duck® Detect in Jenkins](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/running-black-duck-detect-in-jenkins.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-black-duck-detect-in-jenkins.html)
    - [x] [Detect in Jenkins Pipeline job](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/detect-in-jenkins-pipeline-job.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-in-jenkins-pipeline-job.html)
    - [x] [Detect in Jenkins Freestyle job](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/detect-in-jenkins-freestyle-job.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-in-jenkins-freestyle-job.html)
    - [x] [Auto-escaping Parameters](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/auto-escaping-parameters.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/auto-escaping-parameters.html)
    - [x] [Jenkins Air Gap mode](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/jenkins-air-gap-mode.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/jenkins-air-gap-mode.html)
    - [x] [Using Docker Containers - Best Practice](docs/detect-12.0.0/detect-integrations/detect-jenkins-plugin/using-docker-containers-best-practice.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/using-docker-containers-best-practice.html)
  - [x] [Detect Azure DevOps (ADO) Plugin](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin.md) _(+7)_ · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-azure-devops-ado-plugin.html)
    - [x] [Release Notes for Azure DevOps Plugin](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/release-notes-for-azure-devops-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/release-notes-for-azure-devops-plugin.html)
    - [x] [Requirements for Azure DevOps](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/requirements-for-azure-devops.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/requirements-for-azure-devops.html)
    - [x] [Installing the Azure DevOps plugin](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/installing-the-azure-devops-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/installing-the-azure-devops-plugin.html)
    - [x] [Configuring and Running the Plugin](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/configuring-and-running-the-plugin.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/configuring-and-running-the-plugin.html)
    - [x] [Auto-escaping Parameters](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/auto-escaping-parameters.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/auto-escaping-parameters.html)
    - [x] [Configuring a Build Agent](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/configuring-a-build-agent.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/configuring-a-build-agent.html)
    - [x] [Running the Task](docs/detect-12.0.0/detect-integrations/detect-azure-devops-ado-plugin/running-the-task.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-the-task.html)
  - [x] [Detect GitLab integration](docs/detect-12.0.0/detect-integrations/detect-gitlab-integration.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-gitlab-integration.html)
  - [x] [Detect Bitbucket integration](docs/detect-12.0.0/detect-integrations/detect-bitbucket-integration.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-bitbucket-integration.html)
  - [x] [Azure Container Registry scanning with Detect](docs/detect-12.0.0/detect-integrations/azure-container-registry-scanning-with-detect.md) · [source](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/azure-container-registry-scanning-with-detect.html)

---

*Generated from Fluid Topics map `j_bSwuxnjHv5ElV~TQrAQg` (12.0.0). Official docs: [Black Duck Detect](https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/).*
