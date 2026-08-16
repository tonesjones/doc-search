---
title: "Quickstart: Azure with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-azure-with-black-duck-sca.html"
content_id: "rmrEvYiPwOAyo0t1eVaJ5w"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:25.941379+00:00"
---

# Quickstart: Azure with Black Duck SCA

To integrate a [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) pipeline with Black Duck® SCA a full scan should be run followed by Pull Request scans. A Pull Request scan discovers new issues on the feature branch which are not on the target branch.

A full scan is triggered by push and merge events on specified branches. Conversely, a Pull Request scan is triggered by push events to Pull Requests that target those branches. New security issues introduced by a Pull Request are added as review comments. After a scan completes, appropriate security reports and diagnostic logs can be exported as build artifacts.

For further details follow the **[interactive tutorial](https://blackduck.skilljar.com/black-duck-sca-azure-devops-integration)** for integrating Black Duck® SCA with Black Duck Security Scan Extension.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Extension
  - Pull Request Comments
  - Fix Pull Requests
  - Using the Black Duck Security Scan Extension with Polaris
  - Additional Azure DevOps configuration
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- Install the [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) into the ADO organization.
- An Azure Access Token with sufficient privileges for contributing to Pull Requests to allow the pipeline to inject Pull Request review comments, create Fix Pull Requests and upload SARIF reports.
- For security reasons, it is advisable not to store credentials directly in the pipeline. The recommended approach is to use secured variables.
- The following [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) parameters are required to enable injecting review comments into Pull Requests and have been included in the quickstart example:

  Important: Pull Request comments will not be injected if these parameters and the prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `blackducksca_prcomment_enabled` | When `true`, this enables Pull Request comments. | `"true"` |
  | `azure_token` | An Azure access token required to inject review comments. | `$(System.AccessToken)` |

  Note: The Black Duck Security Scan Template integrates with Black Duck® SCA via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the pipeline job.
- Add the following secrets and variables (Azure DevOps Project Sidebar > Pipelines > Library > Variable Groups):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BLACKDUCKSCA_URL` | Variable | Black Duck SCA Server URL | [https://server.blackduck.com](https://server.blackduck.com/) |
  | `BLACKDUCKSCA_TOKEN` | Secret | Black Duck SCA API Token | `REPLACE_WITH_YOUR_TOKEN` |

## Instructions

1. In an Azure project, navigate to Pipelines > Pipelines
2. Choose **New pipeline**
3. Select repository platform. For this guide, `Azure Repos Git` will be selected
4. Select the repository for which the pipeline should be added
5. Select **Starter Pipeline**
6. Azure will create an `azure-pipelines.yml` file in the root folder of the repository. Add the following code to the `azure-pipelines.yml` file:

   ```
   # Example pipeline for Black Duck SCA scans using the Black Duck Security Scan Extension for ADO
   # https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan
   trigger:
     branches:
       include:
         - main
         - develop

   pr:
     branches:
       include:
         - main
         - develop

   pool:
     vmImage: ubuntu-latest

   variables:
     - group: Black Duck Pipeline Variables

   steps:
     - task: BlackDuckSecurityScan@2
       displayName: "Black Duck SCA Scan"
       env:
         DETECT_PROJECT_NAME: $(Build.Repository.Name)
       inputs:
         blackducksca_url: $(BLACKDUCK_URL)
         blackducksca_token: $(BLACKDUCK_API_TOKEN)
         blackducksca_scan_failure_severities: "BLOCKER"
         blackducksca_fixpr_enabled: true
         blackducksca_prcomment_enabled: true
         blackducksca_reports_sarif_create: true
         azure_token: $(System.AccessToken)
         mark_build_status: "SucceededWithIssues"
         # include_diagnostics: true
   ```

   In the example above the `Black Duck SCA Scan` task runs whenever code is pushed to any branch listed in the `triggers` section, or when a Pull Request push event occurs. The scan type is automatically determined by the Black Duck Security Scan Extension depending on the context in which the pipeline was triggered. The scan behaviour is explained below.

   The pipeline integrates with a Black Duck® SCA server instance via the `BLACKDUCKSCA_URL` and `BLACKDUCKSCA_TOKEN` parameters. A scan will run for a Black Duck® SCA project named after the Azure project’s name, configured using the `DETECT_PROJECT_NAME` environment variable.

   The behaviour of the scans is as follows:

   - **Full scan**: Triggered by push events to any of the branches defined in the `triggers` section. In this scenario the following actions will be performed:
     - An SCA assessment will be run. To enable DAST assessment, set the `BRIDGE_POLARIS_ASSESSMENT_TYPES` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - Issues that have `BLOCKER` severity will cause the scan to report blocker issues.
     - A SARIF report will be generated and exported only for full scans.
     - Fix PRs will be automatically raised to fix vulnerable direct dependencies.
   - **Pull Request scan**: Triggered for Pull Request push events, where the target branch of the merge matches one of the branches defined in the `triggers` section. A Pull Request scan is performed that will run an SCA assessment to scan the source code. Review comments will be injected (`blackducksca_automation_prcomment: true`) for any new issues introduced since the latest full scan of the Pull Request's target branch.Uncomment the `include_diagnostics` parameter to add and upload diagnostics from the `.bridge` folder. Artifacts for a completed pipeline job can be accessed and downloaded from the pipeline's job summary page (Azure DevOps Project Sidebar > Pipelines > Your Pipeline > Your Pipeline Job > Summary > Related > Published Artifact Link).
7. Choose **Save and run** and Azure will display a commit message prompt. For this guide, we choose **Commit directly to the main branch**. Choose **Save and run** again to close the prompt
8. A resource authorization notification may be raised. Choose **Authorize resources**
9. The pipeline job may need permissions to run. Choose **Job** to view the pipeline console output. From here the required permissions can be viewed. Select **Permit** to grant access
10. A full scan will be run on the `main` branch.

    A Pull Request can subsequently be created from a feature branch that targets the main branch. This will run a Pull Request scan when code is pushed to the feature branch.

    An example review comment added to a Pull Request after a Pull Request scan has run is shown below:

    [image: PR review comments injected by SCA PR scan]

## Useful resources

- [Using Black Duck Security Scan Template with Black Duck SCA](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/949207ee3f3436bf9c902370dbac576e.topic)
- [Black Duck SCA Portal](https://docs.blackduck.com/p/blackducksca)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
- Black Duck SCA academy resources
