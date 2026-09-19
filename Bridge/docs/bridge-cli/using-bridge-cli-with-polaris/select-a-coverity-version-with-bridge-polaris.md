---
title: "Select a Coverity version with Bridge Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/select-a-coverity-version-with-bridge-polaris.html"
content_id: "k7Y0kayJ8woegUzveJC67Q"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:08.060855+00:00"
---

# Select a Coverity version with Bridge Polaris

In Bridge CLI workflows, Polaris multi version SAST support lets organizations control which supported Coverity version is used to run a local or hybrid SAST scan. This is applicable to SAST full and rapid scan types.

Bridge can accept a `coverity.version` parameter, or use a version from Polaris tool settings and recommended defaults. Polaris then selects the appropriate Coverity and associated Sigma versions for full and Rapid scans, ensuring consistent analysis behavior while still allowing staged upgrades and rollbacks.

Please review Polaris multi version SAST tool support with Bridge for basic requirements.

Important: The Bridge CLI `coverity.version` parameter applies only to **hybrid** and **local** SAST scan modes. **Remote** scan modes use the Coverity version configured in the Polaris Web UI.

## Prerequisites

- Access to a Polaris server with permission granted to create access tokens and projects.
- A [Polaris access token](hhttps://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0d97d272fb42796be0f9f52928a17d57.topic) or [service account token](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ae0e60062f785563c1907b533597e5dd.topic) to allow integration with a Polaris server instance.
- The following parameters are required:

  Table 1. List of mandatory parameters for selecting a Coverity version

  | Input parameter | Description | Mandatory / optional |
  | --- | --- | --- |
  | `BRIDGE_POLARIS_ACCESSTOKEN` | Environment variable containing Polaris access token. Use either a user [access token](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0d97d272fb42796be0f9f52928a17d57.topic) (created in the Polaris UI) or a [service account token](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ae0e60062f785563c1907b533597e5dd.topic) token | Mandatory |
  | `--stage` | Use to specify that Bridge integrates with Polaris. | Mandatory |
  | `polaris.serverurl` | Polaris server URL. | Mandatory |
  | `polaris.application.name` | Name for Polaris application. The specified application must exist on Polaris with appropriate entitlements. | Mandatory |
  | `polaris.project.name` | Name of Polaris project. If the project does not exist on Polaris, it will be created. Set `polaris.onboarding` to `false` to prevent this behavior. | Mandatory |
  | `polaris.branch.name` | Branch name in the Polaris server. Bridge will raise an error if a branch name is not provided. If the branch does not exist in Polaris, Bridge will create the branch. Set `polaris.onboarding` to `false` to prevent this behavior. | Mandatory |
  | `polaris.assessment.types` | Specifies the type of test to be run: - `SAST` - `SAST,SCA` | Mandatory |
  | `polaris.test.sast.location` | Configure the location where source code should be captured, built and analyzed for a SAST assessment type. **Default**: `hybrid`  **Acceptables values:** - hybrid - local - remote  For further details refer to Complete List Of Bridge Commands | Optional Important: SAST scans for **remote** assessment modes will use the Coverity version configured in the Polaris Web UI. |
  | `polaris.test.sast.type` | This parameter allows a full SAST scan, or a rapid SAST scan to be run. If this parameter is not set, the default value will be used. **Default**: `SAST-FULL`  **Acceptable values**: - `SAST-FULL` - `SAST-RAPID`  Bridge automatically selects a compatible Sigma version for Rapid scans. | Optional (This parameter is optional for `SAST-FULL` scans, but it is **mandatory** for `SAST-RAPID` scans.) Important: Before testing a project with Rapid Scan Static, a full SAST test (using the latest version of Coverity that Polaris supports) must be completed. If an attempt is made to run a rapid scan before a full SAST test is completed, Bridge starts a full SAST scan automatically. The full SAST scan must be run with the latest version of Coverity that Polaris supports. This ensures the project has the necessary baseline before performing rapid scans. |
  | `coverity.version` | Select the Coverity version for SAST local or SAST hybrid scans. **Default**: Bridge uses the version configured on Polaris Web UI for the application, project or branch being scanned.  **Acceptable Values**: Versions of Coverity that are supported on Polaris (including deprecated versions).  **Example**:  `2025.6.2`  For further details see Polaris multi version SAST tool support with Bridge | Optional Important: Bridge CLI returns an error if an unsupported version is requested. |

## Instructions

Follow the steps below to select a Coverity version with Bridge CLI.

1. Make the Polaris access token available as an environment variable.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
   ```

   Note: Use either a [user access token](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ae0e60062f785563c1907b533597e5dd.topic) (created in the Polaris UI) or a [service account token](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ae0e60062f785563c1907b533597e5dd.topic) here.
2. Use the Bridge CLI to select a Coverity version.

   **Example:**

   ```
   bridge-cli --stage polaris \
       coverity.version="2025.6.2" \
       polaris.serverurl=$(POLARIS_SERVERURL) \
       polaris.assessment.types=SAST \
       polaris.application.name=$(POLARIS_APPLICATION_NAME) \
       polaris.project.name=$(POLARIS_PROJECT_NAME) \
       polaris.branch.name="main"
   ```

   - Run Bridge CLI with the `--stage` argument set to `polaris`.
   - Use `polaris.serverurl` to specify the base URL for a Polaris server instance.
   - Use `polaris.assessment.types` to specify that a SAST scan should run.
   - Use `polaris.application.name` to specify the name of the application to create.
   - Use `polaris.project.name` to specify the name of the project to create.
   - Use `polaris.branch.name` to specify the name of the branch to create.
   - Use `coverity.version` to specify that Coverity version `2025.6.2` should be used to perform the SAST scan.
   - Defaults:
     - `polaris.test.sast.location` (`hybrid`): Source code and build will be captured locally and uploaded to the Polaris platform for analysis.
     - `polaris.test.sast.type` (`SAST-FULL`): A full SAST scan will run.
3. When the scan completes successfully, the results will be available in the Polaris dashboard.

## Useful resources

- Polaris multi version SAST tool support with Bridge
- Complete List Of Bridge Commands
- [Manage SAST Tool Versions](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/519d3d1f11586ca78fe72370df770f8a.topic)
