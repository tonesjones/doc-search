---
title: "Using SCA Container Scan with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-sca-container-scan-with-bridge.html"
content_id: "UBfUyYK9U4b4HEsgOLqXtA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:10.100193+00:00"
---

# Using SCA Container Scan with Bridge

Bridge CLI can upload a pre-built container image archive, such as a Docker image exported as a .tar file, to Polaris for SCA analysis, including analysis of container image layers, open source components, vulnerabilities, and license information.

Container scanning examines each layer of a container image to determine which open source components are present and which layer introduced each component. This makes it particularly valuable for assessing risk in images built from third-party base images, multi-stage builds, or images where not every layer in the stack is under the organization's control.

To run a container scan, Bridge CLI uploads a container image archive, e.g. created with `docker save`, to Polaris. Container scanning runs as a standalone scan type and cannot be combined with other scan types in the same test. Subsequent uploads add their contents to the existing results rather than replacing them.

## Limitations

Review the following limitations before running an SCA container scan.

| Limitation | Description |
| --- | --- |
| **Standalone SCA container test type** | `SCA_CONTAINER` must be configured as a standalone value for `polaris.test.sca.type`. Do not combine it with other SCA test types such as `SCA_PACKAGE`, `SCA_SIGNATURE` or `SCA_BINARY`. |
| **SAST cannot be configured with SCA container scans within the same Polaris project** | SAST scans use branch resources, while SCA container scans use container resources. A Polaris project instance cannot contain both resource types at the same time. If SAST is configured with SCA container scanning, Bridge CLI returns an error. Do not include both SAST and SCA in `polaris.assessment.types` when `polaris.test.sca.type` is set to `SCA_CONTAINER`. |
| **Unsupported features** | The following features are not supported for SCA container scans.:   - Pull request comments in synchronous mode - Fix pull request workflows in synchronous mode - GitHub Issues - SARIF report - GitLab report generation   Note: If any of the above features are configured then Bridge CLI will log a warning and will skip the stages in the workflow. |
| **Artifact format** | Use .tar, .zip, .tgz or .gz archives |
| **Artifact size limits** | If the artifact exceeds the maximum supported size of **10GB** then Bridge CLI logs the error and exits with a non-zero exit code. |
| **Upgrade guidance** | Direct upgrade guidance is available for components where the version is identified, but transitive upgrade guidance is not. No upgrade guidance is available for components where only the component name (but not the version) is identified. |
| **Component data availability in container scans** | Container scanning identifies components by analyzing binary signatures rather than package manager manifests. In some cases, only the component name can be determined. Version and origin information may be unavailable, meaning vulnerability and upgrade guidance data will be limited. Missing details can be added manually via component editing in Polaris. |

## Prerequisites

Make sure the following prerequisites are met before running the scan:

- A Polaris tenant entitled for SCA container scanning.
- Bridge CLI installed and available on system `PATH`.
- A Polaris access token with SCA permissions, exported as an environment variable.

  ```
  export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESSTOKEN>"
  ```
- A container image tar file to scan, such as `container-image.tar`. An example that uses docker is shown below:

  ```
  docker save -o container-image.tar myimage:latest
  ```

The following configuration parameters are required.

Warning: If any required field is not provided, Bridge CLI returns an error

| Parameter | Description |
| --- | --- |
| `BRIDGE_POLARIS_ACCESSTOKEN` | Environment variable containing a Polaris access token with SCA permissions. |
| `polaris.serverUrl` | URL of the Polaris server. |
| `polaris.application.name` | Name of the Polaris application. |
| `polaris.project.name` | Name of the Polaris project. The type of Polaris project should be for container resources only. If the project is an existing project that contains branches then Bridge CLI will raise an error and exit with a non-zero exit code. |
| `polaris.assessment.types` | Must be set to `SCA` only. |
| `polaris.container.name` | A name to associate with the container image. The container name will be listed in the containers section of the project in the Polaris web UI and can also be used as a filter. |
| `polaris.test.sca.type` | Must be set to `SCA_CONTAINER` and not combined with other SCA test types, e.g. `SCA_PACKAGE`, `SCA_SIGNATURE` or `SCA_BINARY`. |
| `polaris.artifactToUpload` | Path to the container archive file to upload for SCA container scanning. Supports .tar, .zip, .tgz or .gz archive files. Absolute and relative paths are supported; relative paths are resolved against the current working directory. Note: Directory paths are not supported. |

## Instructions

Follow the steps below to use Bridge to run an SCA container scan with Polaris.

1. Run the SCA container scan with Bridge CLI.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESSTOKEN>"

   bridge-cli --stage polaris 
     polaris.serverUrl="<POLARIS_SERVER_URL>" 
     polaris.application.name="<APPLICATION_NAME>" 
     polaris.project.name="<PROJECT_NAME>" 
     polaris.container.name="<CONTAINER_NAME>" 
     polaris.assessment.types=SCA 
     polaris.test.sca.type=SCA_CONTAINER 
     polaris.artifactToUpload="/path/to/container-image.tar"
   ```
2. Review scan results in Polaris

   - Open the results URL printed in the Bridge CLI log output or login to Polaris.
   - Open the project and select the most recent SCA container test execution.

The SCA container scan results are available in Polaris:

- **Layer statistics:** The Polaris container scan test summary provides statistics for each layer, including the total number of components added and removed. For added components, the summary reports a count of high, medium and low-risk components.
- **Components per layer:** which open source components were added or removed in each layer.
- **Security risk per layer:** the number of components at each risk level in each layer: critical, high, medium, low, and none.
- **Component security details:** when version and origin information are available, results can include:
  - NVD CVE data with enhanced vulnerability information.
  - Black Duck Security Advisories (BDSAs).
  - Component origins, such as Linux distro backport patches, Node.js, and NuGet.
  - Direct upgrade guidance.

After the scan completes, use the results to update policies, fix issues and plan follow-up scans as needed.
