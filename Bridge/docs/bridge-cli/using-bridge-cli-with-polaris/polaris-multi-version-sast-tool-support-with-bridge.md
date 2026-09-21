---
title: "Polaris multi version SAST tool support with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/polaris-multi-version-sast-tool-support-with-bridge.html"
content_id: "R1nVYpGOerTE7Z4tM8rqKw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:07.344629+00:00"
---

# Polaris multi version SAST tool support with Bridge

Polaris enables organizations to select from multiple supported versions of client scan tools, providing control over upgrades, minimizing workflow disruptions and supporting organizational policies. This feature ensures consistent and stable analysis results during tool upgrades.

## What is multi version SAST tool support?

Multi Version SAST tool support is a Polaris platform capability that allows organizations to control which version of Coverity is used for tests and workflows.

Instead of being forced to always use the latest tool version, customers can select from several available versions, e.g. the current (N), previous (N-1), and earlier (N-2, N-3) releases, when running security scans.

## What are the benefits?

The ability to select a specific Coverity offers the following benefits:

| Reason | Description |
| --- | --- |
| Control upgrade timing | Allows organizations to decide when to upgrade tool versions, aligning with internal policies and validation schedules. |
| Risk mitigation | Enables rollback to a previous, stable version if issues are found in a new release, minimizing workflow disruptions. |
| Compliance with organizational processes | Supports organizations that require extensive validation and certification before adopting new tool versions. |
| Project and branch flexibility | Permits different projects or branches to use specific tool versions based on unique requirements or dependencies. |
| Access to historical versions | Provides access to previous N versions (e.g., N, N-1, N-2, N-3) for compatibility with legacy codebases or long-term projects. |
| Consistent results across dependencies | Ensures consistent analysis and triage by locking tool versions and their dependencies. For example, selecting a Coverity version automatically selects the compatible Sigma version. |
| Minimize analysis result churn | Prevents unexpected changes in analysis results by allowing teams to lock tool and dependency versions until they are ready to upgrade. |

## Selecting a Coverity version

Use the `coverity.version` parameter to select which Coverity version to use for SAST scans. This is applicable for local and hybrid assessment modes only.

Note: SAST scans for **remote** assessment modes will use the Coverity version configured in the Polaris Web UI.

Available Coverity versions are accessible from the Polaris platform in the application, project or branch being scanned:

- Latest (recommended)
- Specific tool version

Important: If the Coverity version changes, it is recommended that a full scan should be run before running a rapid scan to preserve triage history and prevent analysis result churn.

The table below describes the behavior for how Bridge selects multi version SAST tools.

Table 1. Version selection behavior

| Rule | Description |
| --- | --- |
| Default | Bridge uses the version configured on Polaris Web UI for the application, project or branch being scanned. |
| Specified version | Versions specified for hybrid and local scans using the Bridge CLI `coverity.version` parameter takes precedence over the Polaris Web UI setting. |
| Version validation | Only the latest and specific tool versions configured on the Polaris server are valid. Visit the Polaris [Support Tools](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/7420e1d925f1f5f0729fb771ea66000a.topic) page for supported versions (current and deprecated). |
| Invalid version | Bridge CLI returns an error if an unsupported version is requested. |
| Sigma version | Cannot be directly selected. Bridge automatically selects a compatible Sigma version for Rapid scans. |

The table below describes the scan types and scan modes supported by the `coverity.version` parameter.

Table 2. Scan compatibility

| Feature | Supported options |
| --- | --- |
| Scan types | - SAST full - SAST Rapid |
| Scan modes | - Hybrid - Local |

Note: The Bridge CLI `coverity.version` parameter applies only to **hybrid** and **local** scan modes. **Remote** scan modes use the Coverity version configured in the Polaris Web UI.

## Bridge CLI example

For an example of using Bridge CLI to select the Coverity version used for performing SAST scans please refer to Select a Coverity version with Bridge Polaris.

## Useful resources

- Complete list of Bridge commands
- [Manage SAST tool versions](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/519d3d1f11586ca78fe72370df770f8a.topic)
