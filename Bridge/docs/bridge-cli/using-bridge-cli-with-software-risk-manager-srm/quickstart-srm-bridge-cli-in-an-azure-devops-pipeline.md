---
title: "Quickstart: SRM Bridge CLI in an Azure DevOps pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-srm-bridge-cli-in-an-azure-devops-pipeline.html"
content_id: "vM1t4rCUpsqE2qJuvytlzQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:25.249343+00:00"
---

# Quickstart: SRM Bridge CLI in an Azure DevOps pipeline

As an alternative to the Black Duck Security Scan Extension, the Bridge CLI can be downloaded and directly executed in a Azure DevOps pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use Bridge CLI directly from a pipeline, the correct Bridge CLI Software Risk Manager parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult Using Bridge CLI with Software Risk Manager (SRM) for further details and instructions on use.

Note: The Black Duck Security Scan Extension (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide: Quickstart: Black Duck Security Scan Action with SRM. The Black Duck Security Scan Extension has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Extension and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - Setting up Black Duck Security Scan Extension
  - List of mandatory and optional parameters for SRM
  - Additional Azure DevOps configuration
- For security reasons, it is advisable to use [Azure DevOps variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables) or variable groups to store credentials and access tokens.
- Add the following variables in a variable group or pipeline variables (Pipelines > Library > Variable groups):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `SRM_URL` | Variable | SRM server URL | `https://srm.example.com` |
  | `SRM_APIKEY` | Secret Variable | SRM API key | `REPLACE_WITH_YOUR_APIKEY` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI download URL for Linux | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |

  Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
  - See Using Bridge With Compiled Languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure an Azure DevOps pipeline that invokes Bridge CLI for SRM scans:

1. Create the `azure-pipelines.yml` file containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - `Install JDK` step
   - `Maven Build` Step
   - Build/clean command environment variables (`BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND`).

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
     - job: Bridge_CLI_SRM_Scan
       variables:
         - group: srm.variable.group
         - name: DEFAULT_BRANCH
           value: main
         - name: BRANCH_PARENT
           value: $[ iif(eq(variables['Build.SourceBranchName'], variables['DEFAULT_BRANCH']), '', variables['DEFAULT_BRANCH']) ]
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
         #     options: '-B -DskipTests'
         - bash: |
             curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
             $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage srm
           env:
             BRIDGE_SRM_URL: $(SRM_URL)
             BRIDGE_SRM_APIKEY: $(SRM_APIKEY)
             BRIDGE_SRM_ASSESSMENT_TYPES: 'SAST,SCA'
             BRIDGE_SRM_PROJECT_NAME: $(Build.Repository.Name)
             BRIDGE_SRM_BRANCH_NAME: $(Build.SourceBranchName)
             BRIDGE_SRM_BRANCH_PARENT: $(BRANCH_PARENT)
             # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
             # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
           displayName: 'SRM Scan'
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

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans.

   The Azure Pipeline will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_URL` parameter, using a given API key, `BRIDGE_SRM_APIKEY`.

   The Software Risk Manager project will be created if it does not already exist and named with the Azure DevOps repository slug. Similarily the SRM branch name is derived from the source branch name.

   A full scan, including SAST and SCA assessments, is triggered by push events for the `main` and `develop` branch.

   Optional log archiving and publishing artifact tasks are included but disabled by default. Enable these tasks for troubleshooting by setting their `enabled` property to `true`. Artifacts for a completed pipeline job can be accessed and downloaded from the pipeline's job summary page (Azure DevOps Project Sidebar> > Pipelines > Your Pipeline > Your Pipeline Job > Summary > Related > Published Artifact Link).
2. Run scans

   Once the workflow is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Test:** Monitor the output to verify that the SRM scan completes successfully and issues appear in SRM Dashboard.

## Troubleshooting and support

If errors are encountered during the pipeline run, ensure that all variables are set correctly and that the Bridge CLI can access the SRM server.

If a pipeline error is encountered similar to the example below, then it is likely that the `BRIDGE_SRM_BRANCH_PARENT` parameter has not been set.

Important: ERROR: Branch "develop" does not exist for the project and "srm.branch.parent" is empty but is required along with "srm.branch.name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, `stage` or `release`, the `BRIDGE_SRM_BRANCH_PARENT` parameter must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

For further troubleshooting, enable the optional log archiving and publishing artifact tasks in the YAML by setting their `enabled` property to `true`.

## Useful resources

- [SRM product documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
