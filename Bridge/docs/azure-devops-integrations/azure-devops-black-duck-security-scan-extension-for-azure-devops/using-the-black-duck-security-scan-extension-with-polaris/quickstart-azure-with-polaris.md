---
title: "Quickstart: Azure with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-azure-with-polaris.html"
content_id: "HrMeUNswHZgiZKoURhNKgA"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:23.612605+00:00"
---

# Quickstart: Azure with Polaris

To integrate a [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) pipeline with Polaris a full scan should be run followed by Pull Request scans. A Pull Request scan discovers new issues on the feature branch which are not on the target branch.

A full scan is triggered by push and merge events on specified branches. Conversely, a Pull Request scan is triggered by push events to Pull Requests that target those branches. New security issues introduced by a Pull Request are added as review comments. After a scan completes, appropriate security reports and diagnostic logs can be exported as build artifacts. For full scans Fix Pull Requests will be created to upgrade dependencies.

For further details follow the **[interactive tutorial](https://blackduck.skilljar.com/polaris-azure-devops-integration)** for integrating Polaris with Black Duck Security Scan Extension.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Extension
  - Polaris Prerequisites
  - Pull Request Comments
  - Fix pull requests (Fix PRs)
  - Using the Black Duck Security Scan Extension with Polaris
  - Additional Azure DevOps configuration
- Install the [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) into the ADO organization.
- An Azure Access Token with sufficient privileges for contributing to Pull Requests to allow the pipeline to inject Pull Request review comments, create Fix Pull Requests and upload SARIF reports.
- For security reasons, it is advisable not to store credentials directly in the pipeline. The recommended approach is to use secured variables.
- The following [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) parameters are required to enable injecting review comments into Pull Requests, create Fix Pull Requests and upload SARIF reports:

  Important: Pull Request comments will not be injected, Fix Pull Requests will not be created and SARIF reports will not be uploaded if these parameters and the prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `polaris_application_name` | The name of the Polaris application. For users that do not have a concurrent license this should be created before running the pipeline. | `$(Build.Repository.Name)` |
  | `polaris_prcomment_enabled` | When `true`, this enables PR comments. | `"true"` |
  | `polaris_fixpr_enabled` | When `true` this enables Fix Pull Requests. | `"true"` |
  | `azure_token` | An Azure Access Token required to inject review comments and upload SARIF reports. | `$(System.AccessToken)` |

  Note: The Black Duck Security Scan Extension integrates with Polaris via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (Azure DevOps Project Sidebar > Pipelines > Library > Variable Groups):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `POLARIS_SERVERURL` | Variable | Polaris Server URL | `https://polaris.blackduck.com` |
  | `POLARIS_ACCESSTOKEN` | Secret | Polaris Access Token | `REPLACE_WITH_YOUR_TOKEN` |
- Polaris uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to integrate Polaris with the GitHub workflow for SAST and SCA scans:

1. In an Azure project, navigate to Pipelines > Pipelines
2. Choose **New pipeline**
3. Select repository platform. For this guide, `Azure Repos Git` will be selected
4. Select the repository for which the pipeline should be added
5. Select **Starter Pipeline**
6. Azure will create an `azure-pipelines.yml` file in the root folder of the repository. Add the following code to the `azure-pipelines.yml` file:

   Note: For compiled languages, uncomment the following:
   - `Install JDK` and `Maven Build` tasks
   - `coverity_build_command` and `coverity_clean_command` parameters.

   ```
   ## -----------------------------------------------------------------------------
   # NOTE: The commented lines below are for compiled languages (e.g., Java, C++).
   # If your project requires a build step, uncomment and adjust those lines.
   ## -----------------------------------------------------------------------------
   # Universal Azure DevOps Pipeline for Polaris (Scripted & Compiled Languages)
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
     - group: polaris.variable.group

   steps:
   ## Uncomment and modify build environment setup as appropriate if using compiled languages
   # - task: JavaToolInstaller@0
   #   displayName: 'Install JDK'
   #   inputs:
   #     versionSpec: 21
   #     jdkArchitectureOption: x64
   #     jdkSourceOption: PreInstalled
   #
   ## Uncomment and modify build task as appropriate if using compiled languages requiring compilation
   # - task: Maven@4
   #   displayName: 'Maven Build'
   #   inputs:
   #     options: '-B -DskipTests'

   - task: BlackDuckSecurityScan@2
     displayName: 'Polaris Scan'
     inputs:
       polaris_server_url: $(POLARIS_SERVERURL)
       polaris_access_token: $(POLARIS_ACCESSTOKEN)
       polaris_assessment_types: 'SAST,SCA'
       polaris_application_name: quickstart-$(Build.Repository.Name)
       polaris_prcomment_enabled: true
       polaris_fixpr_enabled: true
       polaris_reports_sarif_create: true
       azure_token: $(System.AccessToken)
       mark_build_status: 'SucceededWithIssues'
       # include_diagnostics: true

       ## Uncomment build and clean commands and modify as appropriate, if using compiled language
       # coverity_build_command: 'mvn clean install'
       # coverity_clean_command: 'mvn clean'
   ```

   In the example above a `polaris` pipeline job runs whenever code is pushed to any branch in the `triggers` list, or when a Pull Request targets one of the branches in the `pr` list. The scan type is automatically determined by the Black Duck Security Scan Extension depending on the context in which the pipeline was triggered. The scan behaviour is explained below.

   The pipeline integrates with a Polaris server instance via the `polaris_server_url` and `polaris_access_token` parameters. A scan will run for a Polaris application named after the Azure DevOps project namespace and name, prefixed by `quickstart`. Within this application, a project will be created, if it doesn’t already exist, to store the scan results. The branch in Polaris is automatically derived from the branch that triggered the scan.

   The behaviour of the scans is as follows:

   - **Full scan**: Triggered by push events to any of the branches listed in the `triggers` section. In this scenario the Black Duck Security Scan Extension will upload artifacts to the Polaris server for scanning:
     - SAST and SCA assessments will be run. To enable DAST assessment, set the `polaris_assessment_types` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - Fix Pull Requests are enabled to raise Pull Requests to upgrade dependencies for full scans of branches. See Fix pull requests (Fix PRs) and Using the Black Duck Security Scan Extension with Polaris for further information and examples that demonstrate how to:
       - Configure order of preference for upgrade guidance.
       - Raise Fix Pull Requests by severity.
       - Enforce a maximum limit for the number of Fix Pull Requests created.
     - A SARIF report will be generated and exported only for full scans.
   - **Pull Request scan**: Triggered for Pull Request push events, where the target branch of the merge matches one of the branches defined in the `pr` section. A Pull Request scan is performed that will run both SAST and SCA assessments. Review comments will be injected (`polaris_pr_comment_enabled: true`) for any new issues introduced since the latest full scan of the Pull Request's target branch.

   Uncomment the `include_diagnostics` parameter to add and upload diagnostics logs from the `.bridge` folder. Artifacts for a completed pipeline job can be accessed and downloaded from the pipeline's job summary page (Azure DevOps Project Sidebar > Pipelines > Your Pipeline > Your Pipeline Job > Summary > Related > Published Artifact Link).
7. Choose **Save and run** and Azure will display a commit message prompt. For this guide, we choose **Commit directly to the main branch**. Choose **Save and run** again to close the prompt
8. A resource authorization notification may be raised. Choose **Authorize resources**
9. The pipeline job may need permissions to run. Choose **Job** to view the pipeline console output. From here the required permissions can be viewed. Select **Permit** to grant access
10. A full scan will be run on the `main` branch.

    A Pull Request can subsequently be created from a feature branch that targets the main branch. This will run a Pull Request scan when code is pushed to the feature branch.

    An example review comment added to a Pull Request after a Pull Request scan has run is shown below:

    [image: PR review comments injected by SCA PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Attention: Request Validation Failed: No concurrent entitlements found for the tenant

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the pipeline, consult [create an application in](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) Polaris.

## Useful resources

- [Polaris product documentation](https://polaris.blackduck.com/developer/default/)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
- Polaris Black Duck Security Scan Extension academy resources
