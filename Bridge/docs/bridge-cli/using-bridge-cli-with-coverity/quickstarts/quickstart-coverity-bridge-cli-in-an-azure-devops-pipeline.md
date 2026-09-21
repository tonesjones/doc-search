---
title: "Quickstart: Coverity Bridge CLI in an Azure DevOps pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-coverity-bridge-cli-in-an-azure-devops-pipeline.html"
content_id: "6FSuOWHbNByNFERehWXD1g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:18.966402+00:00"
---

# Quickstart: Coverity Bridge CLI in an Azure DevOps pipeline

As an alternative to the Black Duck Security Scan Extension, the Bridge CLI can be downloaded and directly executed in a Azure DevOps pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use Bridge CLI directly from a pipeline, the correct Bridge CLI Coverity parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Extension (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The Black Duck Security Scan Extension has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Extension and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Extension
  - Pull Request comments
  - Using Fail Pull Requests With Coverity
  - List of mandatory and optional parameters for Coverity
  - Additional Azure DevOps configuration
- The built-in Azure DevOps [System Access Token](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/access-tokens) is required to allow the pipeline to inject Pull Request review comments. Ensure that **Contribute to pull requests**, **Create branch** and **Delete or disable repository** are set to **Allow** for the build service user in Project > Project Settings > Repository > Security
- For security reasons, it is advisable to use [Azure DevOps variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables) or variable groups to store credentials and access tokens.
- Add the following variables in a variable group or pipeline variables (Pipelines > Library > Variable groups):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Variable | Coverity Connect Server URL | `https://coverity.example.com` |
  | `COV_USER` | Secret Variable | Coverity Connect Username | `REPLACE_WITH_YOUR_USERNAME` |
  | `COVERITY_PASSPHRASE` | Secret Variable | Coverity Connect Password or Access Token | `REPLACE_WITH_YOUR_PASSWORD` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI download URL for Linux | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |

Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge With Compiled Languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure an Azure DevOps pipeline that invokes Bridge CLI for full scans and Pull Request scans:

1. Create the `azure-pipelines.yml` containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - `Install JDK` step
   - `Maven Build` Step
   - Build/clean command environment variables (`BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND`).

   ```
   trigger:
   - main
   - develop
   pool:
     vmImage: ubuntu-latest
   variables:
     - group: cnc.variable.group
   steps:
   # - task: JavaToolInstaller@0
   #   displayName: 'Install JDK'
   #   inputs:
   #     versionSpec: 21
   #     jdkArchitectureOption: x64
   #     jdkSourceOption: PreInstalled
   # - task: Maven@4
   #   displayName: 'Maven Build'
   #   inputs:
   #   options: '-B -DskipTests'
   - bash: |
       set -ex
       curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
       $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage connect
     env:
       BRIDGE_COVERITY_CONNECT_URL: $(COVERITY_URL)
       BRIDGE_COVERITY_CONNECT_USER_NAME: $(COV_USER)
       BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $(COVERITY_PASSPHRASE)
       BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_COVERITY_CONNECT_STREAM_NAME: $(Build.Repository.Name)-$(Build.SourceBranchName)
       # BRIDGE_COVERITY_LOCAL: true
       BRIDGE_COVERITY_CONNECT_POLICY_VIEW: 'Outstanding Issues'
       ### COVERITY: Build commands for compiled languages (uncomment and configure for compiled languages)
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
     displayName: 'Coverity Full Scan'
     condition: not(eq(variables['Build.Reason'], 'PullRequest'))
   - bash: |
       set -ex
       curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
       $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage connect
     env:
       BRIDGE_COVERITY_CONNECT_URL: $(COVERITY_URL)
       BRIDGE_COVERITY_CONNECT_USER_NAME: $(COV_USER)
       BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $(COVERITY_PASSPHRASE)
       BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_COVERITY_CONNECT_STREAM_NAME: $(Build.Repository.Name)-$(System.PullRequest.targetBranchName)
       BRIDGE_COVERITY_PRCOMMENT_ENABLED: true
       ## Use the parameter below to add comments for issues filtered
       ## by impact. Default is High if unset
       ## NOTE: Issues matching BRIDGE_COVERITY_CONNECT_POLICY_VIEW are ignored if set
       # BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'High'

       ### COVERITY: Build commands for compiled languages (uncomment and configure for compiled languages)
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
       BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
       BRIDGE_AZURE_API_URL: "https://dev.azure.com"
       BRIDGE_AZURE_ORGANIZATION_NAME: blackduck
       BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(System.PullRequest.SourceBranch)
       BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(System.PullRequest.PullRequestId)
       # BRIDGE_COVERITY_LOCAL: true
     displayName: 'Coverity PR Scan'
     condition: eq(variables['Build.Reason'], 'PullRequest')
   - task: ArchiveFiles@2
     displayName: 'Copy Log Files'
     condition: succeededOrFailed()
     enabled: false
     inputs:
       rootFolderOrFile: .bridge
       includeRootFolder: false
       archiveFile: '$(Build.ArtifactStagingDirectory)/bridge-logs.zip'
   - task: PublishBuildArtifacts@1
     displayName: 'Publish Log Files'
     condition: succeededOrFailed()
     enabled: false
     inputs:
       PathtoPublish: '$(Build.ArtifactStagingDirectory)'
       ArtifactName: 'logs'
   ```

   Note: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed with the full toolkit. This will override the default behaviour that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans and Pull Request scans.

   A full scan is performed when code is pushed or merged to the `main` or `develop` branches. The `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` parameter is configured to break the build if new or outstanding issues are detected as defined by the Outstanding Issues [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html) (see [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) for details).

   For Pull Requests targeting those branches, Bridge CLI is invoked directly to perform a Pull Request scan. New issues detected on the feature branch are added as Pull Request comments using the built-in Azure DevOps access token. Uncomment the `BRIDGE_COVERITY_PRCOMMENT_IMPACTS` environment variable to filter comments by impact level, with a default of "high" if unset.

   The Coverity project and stream are automatically derived from built-in Azure DevOps environment variables. The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   Optional log archiving and publishing artifact tasks are included but disabled by default. Enable these tasks for troubleshooting by setting their `enabled` property to `true`.
2. Run scans

   Once the workflow is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: PR review comments injected by Coverity PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `BRIDGE_COVERITY_LOCAL` environment variable to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity product documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- Bridge product overview
- [Black Duck Security Scan Extension for Azure DevOps](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan)
