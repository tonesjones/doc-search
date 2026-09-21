---
title: "Quickstart: Azure with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-azure-with-software-risk-manager.html"
content_id: "Doq~ovl5hDKZHjdfgEzcgg"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:30.194286+00:00"
---

# Quickstart: Azure with Software Risk Manager

To integrate a [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) pipeline with Software Risk Manager a workflow can be configured to run scans that perform both SCA and SAST assessments. This provides comprehensive security analysis for applications.

A Software Risk Manager scan can be triggered by push and merge events on specified branches. When a scan runs, it performs both SCA and SAST assessments providing comprehensive security analysis. After a scan completes, appropriate security reports and diagnostic logs can be exported as build artifacts.

Note: Scanning Pull Requests, injecting Pull Request review comments and creating SARIF reports is not currently supported for pipelines that integrate the [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) with Software Risk Manager.

For an introduction to Software Risk Manager follow the **[interactive tutorial](https://blackduck.skilljar.com/introduction-to-software-risk-manager)**.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Extension
  - List of Mandatory and Optional Parameters For Software Risk Manager
  - Additional Azure DevOps configuration
- Install the [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) into the ADO organization.
- For security reasons, it is advisable not to store credentials directly in the pipeline. The recommended approach is to use secured variables.
- Note: The Black Duck Security Scan Extension integrates with Software Risk Manager via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (Azure DevOps Project Sidebar > Pipelines > Library > Variable Groups):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `SRM_URL` | Variable | Software Risk Manager Server URL | `https://server.blackducksrm.com` |
  | `SRM_APIKEY` | Secret | Software Risk Manager API Token | `REPLACE_WITH_YOUR_API_TOKEN` |
- Software Risk Manager supports both compiled and interpreted languages. For compiled languages that use a build system (such as C++, Java, etc.), Software Risk Manager must be configured with build and clean commands to capture and analyze the build for SAST analysis.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Software Risk Manager to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to integrate Software Risk Manager with the [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) for comprehensive security scans:

1. In an Azure project, navigate to Pipelines > Pipelines
2. Choose **New pipeline**
3. Select repository platform. For this guide, `Azure Repos
   Git` will be selected
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
   trigger:
     - main
     - develop
   pool:
     vmImage: ubuntu-latest
   jobs:
     - job: Bridge_SRM_Scan
       variables:
         - group: srm.variable.group
         - name: DEFAULT_BRANCH
           value: main
         - name: BRANCH_PARENT
           value: $[ iif(eq(variables['Build.SourceBranchName'], variables['DEFAULT_BRANCH']), '', variables['DEFAULT_BRANCH']) ]
       steps:
         # - task: JavaToolInstaller@0
         #   displayName: "Install JDK"
         #   inputs:
         #     versionSpec: "21"
         #     jdkArchitectureOption: "x64"
         #     jdkSourceOption: "PreInstalled"
         # - task: Maven@4
         #   displayName: "Maven Build"
         #   inputs:
         #     options: "-B -DskipTests"
         - task: BlackDuckSecurityScan@2
           displayName: "SRM Scan"
           inputs:
             srm_url: $(SRM_URL)
             srm_apikey: $(SRM_APIKEY)
             srm_branch_name: $(Build.SourceBranchName)
             srm_branch_parent: $(BRANCH_PARENT)
             srm_assessment_types: "SAST,SCA"
             # coverity_build_command: mvn -B -DskipTests package
             # coverity_clean_command: mvn -B clean
             include_diagnostics: false
             mark_build_status: "SucceededWithIssues"
   ```

   In the example above the Black Duck Security Scan Pipe will authenticate with the Software Risk Manager server specified in the `srm_url`parameter, using a given API key, `srm_apikey`. The Software Risk Manager project is named with the Azure DevOps repository slug.

   A full scan, including SAST and SCA assessments, will then be triggered by push events for the `main` or `develop` branch.

   The branch name (`srm_branch_name`) associated with a full scan is derived from the source branch of the push event. If a full scan is triggered for a branch that is not the default branch, then the pipeline sets the parent branch (`srm_branch_parent`) to the default branch. This helps ensure that non-default branches reference the default branch as their base during scanning operations.

   The `mark_build_status` parameter is set to `SucceededWithIssues` to indicate that the build should be marked as succeeded but with issues when security vulnerabilities are found.

   Set the `include_diagnostics` parameter to `true` to add and upload diagnostics logs. Artifacts for a completed pipeline job can be accessed and downloaded from the pipeline's job summary page (Azure DevOps Project Sidebar > Pipelines > Your Pipeline > Your Pipeline Job > Summary > Related > Published Artifact Link).
7. Choose **Save and run** and Azure will display a commit message prompt. For this guide, we choose **Commit directly to the main branch**. Choose **Save and run** again to close the prompt
8. A resource authorization notification may be raised. Choose **Authorize resources**
9. The pipeline job may need permissions to run. Choose **Job** to view the pipeline console output. From here the required permissions can be viewed. Select **Permit** to grant access
10. A comprehensive scan will be run on the `main` branch.

    The scan will perform both SCA and SAST assessments, providing a complete security analysis of the application. Results will be available through the Software Risk Manager Dashboard.

## Troubleshooting and support

If errors are encountered during the pipeline run, ensure that all global variables are set correctly and that the Bridge CLI can access the Software Risk Manager server.

If a pipeline error is encountered similar to the example below, then it is likely that the `srm_branch_parent` parameter has not been set correctly.

Important: ERROR: Branch "develop" does not exist for the project and "srm_branch_parent" is empty but is required along with "srm_branch_name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, the `srm_branch_parent` parameter must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

For further troubleshooting, set the `include_diagnostics` parameter to `true`. Access and download the artifacts from the pipeline's job summary page (Azure DevOps Project Sidebar > Pipelines > Your Pipeline > Your Pipeline Job > Summary > Related > Published Artifact Link).

## Useful resources

- [Software Risk Manager product documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
