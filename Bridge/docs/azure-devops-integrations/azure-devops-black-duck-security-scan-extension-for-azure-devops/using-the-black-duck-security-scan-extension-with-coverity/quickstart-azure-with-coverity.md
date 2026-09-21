---
title: "Quickstart: Azure with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-azure-with-coverity.html"
content_id: "Iw9Ymue26epLx_uBvG6y6Q"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:28.247536+00:00"
---

# Quickstart: Azure with Coverity

To integrate a [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) pipeline with Coverity a full scan should be run followed by Pull Request scans. A Pull Request scan discovers new issues on the feature branch which are not on the target branch.

A full scan is triggered by push and merge events on specified branches. Conversely, a Pull Request scan is triggered by push events to Pull Requests that target those branches. New security issues introduced by a Pull Request are added as review comments. After a scan completes, appropriate security reports and diagnostic logs can be exported as build artifacts.

For further details follow the **[interactive tutorial](https://blackduck.skilljar.com/coverity-azure-devops-integration)** for integrating Coverity with Black Duck Security Scan Extension.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Extension
  - Using the Black Duck Security Scan Extension with Coverity
  - Pull Request Comments
  - Using Fail Pull Requests With Coverity
  - Additional Azure DevOps configuration
- Install the [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) into the ADO organization.
- An Azure Access Token with sufficient privileges for contributing to Pull Requests to allow the pipeline to inject Pull Request review comments.
- For security reasons, it is advisable not to store credentials directly in the pipeline. The recommended approach is to use secured variables.
- The following [Black Duck Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan) parameters are required to enable injecting review comments into Pull Requests:

  Important: Pull Request comments will not be injected if these parameters and the prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `coverity_prcomment_enabled` | When `true`, this enables PR comments. | `"true"` |
  | `azure_token` | An Azure Access Token required to inject review comments. | `$(System.AccessToken)` |

  Note: The Black Duck Security Scan Extension integrates with Coverity via Bridge CLI. Additional scan configuration options not available through the ADO Extension Coverity parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (Azure DevOps Project Sidebar > Pipelines > Library > Variable Groups):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Variable | Coverity Server URL | `https://coverity.blackduck.com` |
  | `COV_USER` | Secret | Coverity Username | `REPLACE_WITH_YOUR_USERNAME` |
  | `COVERITY_PASSPHRASE` | Secret | Coverity Passphrase | `REPLACE_WITH_YOUR_PASSPHRASE` |
- Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to integrate Coverity with the Azure DevOps pipeline for SAST scans:

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
   # NOTE: Some commented lines below are for compiled languages (e.g., Java, C++).
   # If your project requires a build step, uncomment and adjust those lines.
   ## -----------------------------------------------------------------------------
   trigger:
     - main
     - develop
   pool:
     vmImage: ubuntu-latest
   variables:
     - group: coverity.variable.group
     - name: COVERITY_VIEW
       ${{ if eq(variables['Build.Reason'], 'PullRequest') }}:
         value: ""
       ${{ else }}:
         value: "Outstanding Issues"
   steps:
     ## Uncomment build environment setup if using compiled languages
     # - task: JavaToolInstaller@0
     #   displayName: "Install JDK"
     #   inputs:
     #     versionSpec: 21
     #     jdkArchitectureOption: x64
     #     jdkSourceOption: PreInstalled
     ## Uncomment build task if using compiled languages requiring compilation
     # - task: Maven@4
     #   displayName: "Maven Build"
     #   inputs:
     #     options: "-B -DskipTests"
     - task: BlackDuckSecurityScan@2
       displayName: "Coverity Scan"
       inputs:
         coverity_url: $(COVERITY_URL)
         coverity_user: $(COV_USER)
         coverity_passphrase: $(COVERITY_PASSPHRASE)
         coverity_policy_view: $(COVERITY_VIEW)
         coverity_prcomment_enabled: true
         ## Use the parameter below to add comments for issues filtered 
         ## by impact. Default is High if unset
         ## NOTE: Issues matching coverity_policy_view are ignored if set
         # coverity_prcomment_impacts: 'High,Medium,Low,Audit'
         ## Uncomment build and clean commands and modify as appropriate, if using compiled language
         # coverity_build_command: mvn -B -DskipTests package
         # coverity_clean_command: mvn -B clean
         ## Perform local analysis with full toolkit
         # coverity_local: true
         azure_token: $(System.AccessToken)
         include_diagnostics: false
         mark_build_status: "SucceededWithIssues"
   ```

   Important: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled the `coverity_local` line in the example should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed. This will override the default behavior that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above a `Coverity Scan` task runs whenever code is pushed to any branch in the `triggers` list, or when a Pull Request targets one of those branches. The scan type is automatically determined by the Black Duck Security Scan Extension depending on the context in which the pipeline was triggered. The scan behaviour is explained below.

   The pipeline integrates with a Coverity server instance via the `coverity_url`, `coverity_user`, and `coverity_passphrase` parameters. A scan will run for a Coverity project and stream derived from the Azure DevOps repository name and branch.

   The Coverity stream stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   For full scans the `coverity_policy_view` parameter will break the build if new or outstanding issues are detected as defined by the `Outstanding Issues` [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html). Consult [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) within the Coverity documentation for further details.

   Each time code is committed to a Pull Request branch that targets one of the specified base branches, a comparison is performed between the scan of the Pull Request branch and the latest full scan of its parent branch. Any new issues introduced by the Pull Request are automatically added as review comments.

   Coverity Fail Pull Requests are enabled by setting the `coverity_pr_comment_enabled` parameter to *true*. Use the `coverity_prcomment_impacts` parameter to add comments filtered by impact, with a default of `High` if unset. The source code management token created in the prerequisites is required to inject Pull Request review comments.

   Set the `include_diagnostics` parameter to true to add and upload diagnostics logs from the `.bridge` folder. Artifacts for a completed pipeline job can be accessed and downloaded from the pipeline's job summary page (Azure DevOps Project Sidebar > Pipelines > Your Pipeline > Your Pipeline Job > Summary > Related > Published Artifact Link).
7. Choose **Save and run** and Azure will display a commit message prompt. For this guide, we choose **Commit directly to the main branch**. Choose **Save and run** again to close the prompt
8. A resource authorization notification may be raised. Choose **Authorize resources**
9. The pipeline job may need permissions to run. Choose **Job** to view the pipeline console output. From here the required permissions can be viewed. Select **Permit** to grant access
10. A full scan will be run on the `main` branch.

    A Pull Request can subsequently be created from a feature branch that targets the main branch. This will run a Pull Request scan when code is pushed to the feature branch.

    An example review comment added to a Pull Request after a Pull Request scan has run is shown below:

    [image: PR review comments injected by Coverity PR Scan]

## Troubleshooting and support

If an error is encountered similar to the example below, then the `coverity_local` parameter should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the workflow uses the Coverity thin client to upload artifacts, with the analysis performed at the server.

Setting the `coverity_local` parameter to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the pipeline. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity product documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
- Coverity Black Duck Security Scan Extension academy resources
