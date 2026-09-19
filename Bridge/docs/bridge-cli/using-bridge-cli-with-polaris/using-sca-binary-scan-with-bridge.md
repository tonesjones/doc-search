---
title: "Using SCA Binary Scan with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-sca-binary-scan-with-bridge.html"
content_id: "Z6G03zHl6mufvly7tIubvw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:09.398840+00:00"
---

# Using SCA Binary Scan with Bridge

Use Bridge CLI to upload a binary or archive for SCA in Polaris without requiring access to source code or a build environment.

Bridge CLI supports SCA binary scanning with Polaris, enabling detection of open source and license risk even when source code is not available.

With tenant‑level binary entitlements, SCA binary scans can run as part of Polaris project scans to produce more complete SBOMs, with results uploaded to Polaris

This guide explains how to configure and run an SCA binary scan on Polaris using Bridge CLI.

## Limitations

Review the following limitations before running an SCA binary scan.

| Limitation | Description |
| --- | --- |
| **Standalone SCA binary test type** | `SCA_BINARY` must be configured as a standalone value for `polaris.test.sca.type`. Do not combine it with other SCA test types. |
| **Unsupported features** | Pull Request Comments and Fix Pull Request workflows are not supported for SCA binary scans in synchronous mode. Note: If `polaris.prComment.enabled` or `polaris.fixPR.enabled` is set to `true`, Bridge CLI logs a warning and skips the Pull Request Comment and Fix Pull Request workflow, similar to signature scans in synchronous mode. |
| **Artifact format** | Use binary or archive files.  Note: Directory paths are not supported. |
| **Artifact size limits** | If the artifact exceeds the maximum supported size then Bridge CLI logs the error and exits with a non-zero exit code. The maximum supported size on Polaris is:  - **Archive**: 10GB. A file within the archive has a maximum limit of 1GB. - **Binary**: 10GB |

## Prerequisites

Make sure the following prerequisites are met before running the scan:

- A Polaris tenant entitled for SCA binary scanning.
- Bridge CLI installed and available on system `PATH`.
- A Polaris access token with SCA permissions, exported as an environment variable.

  ```
  export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESSTOKEN>"
  ```
- A binary or zip archive artifact to scan, such as `my-binary-archive.zip`.

The following configuration parameters are required.

| Parameter | Description |
| --- | --- |
| `BRIDGE_POLARIS_ACCESSTOKEN` | Environment variable containing a Polaris access token with SCA permissions. |
| `polaris.serverUrl` | URL of the Polaris server. |
| `polaris.application.name` | Name of the Polaris application. |
| `polaris.project.name` | Name of the Polaris project. |
| `polaris.branch.name` | Name of the branch associated with the scan. |
| `polaris.assessment.types` | Must be set to `SCA`. |
| `polaris.test.sca.type` | Must be set to `SCA_BINARY` and not combined with other SCA types. |
| `polaris.artifactToUpload` | Path to the binary or zip archive file to upload for SCA binary scanning. Supports absolute and relative paths; relative paths are resolved against the current working directory. Note: Directory paths are not supported. |

## Instructions

Follow the steps below to use Bridge to run an SCA binary scan with Polaris.

1. Run the SCA binary scan with Bridge CLI.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESSTOKEN>"

   bridge-cli --stage polaris 
     polaris.serverUrl="<POLARIS_SERVER_URL>" 
     polaris.application.name="<APPLICATION_NAME>" 
     polaris.project.name="<PROJECT_NAME>" 
     polaris.branch.name="<BRANCH_NAME>" 
     polaris.assessment.types=SCA 
     polaris.test.sca.type=SCA_BINARY 
     polaris.artifactToUpload="/path/to/my-binary-archive.zip"
   ```
2. Review scan results in Polaris

   - Open the results URL printed in the Bridge CLI log output or login to Polaris.
   - Open the project and select the most recent SCA binary test execution.

The SCA binary scan results are available in Polaris, including identified components, vulnerabilities and license information.

After the scan completes, use the results to update policies, fix issues and plan follow-up scans as needed.
