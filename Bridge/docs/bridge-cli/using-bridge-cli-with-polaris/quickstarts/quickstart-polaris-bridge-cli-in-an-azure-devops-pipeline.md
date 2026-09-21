---
title: "Quickstart: Polaris Bridge CLI in an Azure DevOps pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-polaris-bridge-cli-in-an-azure-devops-pipeline.html"
content_id: "Y4m~TGnh8oT5T3FXYe1giQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:58.926234+00:00"
---

# Quickstart: Polaris Bridge CLI in an Azure DevOps pipeline

An alternate solution for integrating Polaris with ADO is via the Bridge CLI. It has all the functionality of the Black Duck Security Scan Extension, but you must add a step to download the Bridge CLI from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries). You must also input the Bridge CLI commands and pass the relevant access tokens. Please review the relevant documentation: Bridge CLI Product Documentation

Note: You can use Black Duck Security Scan Extension (recommended) for your workflow instead of Bridge CLI by following the quickstart guide: Quickstart: Azure with Polaris

## Prerequisites

- In addition to ADO admin account access from your organization, you need Polaris access before you can follow this procedure.
- If the application doesn't already exist in Polaris, Bridge will try and create it before triggering a CI scan. If you have concurrent subscription / team member enabled, the application creation will be successful. If you have parallel subscription, application creation will fail. To create it manually consult [create the relevant applications in Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic).
- We recommend the following reading before you start:

  - Setting up Black Duck Security Scan Extension
  - Polaris prerequisites
  - Fix pull requests (Fix PRs)
  - Using SCA Fix PRs with Bridge
  - Reference: using the Black Duck Security Scan Extension for Azure DevOps with Polaris
  - Additional Azure DevOps configuration

## Instructions

Important: Confirm System.AccessToken has Contribute to PR permissions. In Azure, navigate to ADO > Project > Project Settings > Repositories > Security > Build Service User.

1. Add the following secrets and variables (ADO > Project > Pipelines > Library > New Variable Group):

   | Variable | Type | Description | Example |
   | --- | --- | --- | --- |
   | `POLARIS_SERVER_URL` | Variable | Polaris Server URL | `https://polaris.synopsys.com` (or `https://polaris.blackduck.com` after you [Migrate Polaris to the Black Duck domain](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ee117187a16710bb1231f1919c97c0ed.topic)) |
   | `POLARIS_ACCESS_TOKEN` | Secret | Polaris Access Token. You can use either an access token created in the Polaris UI or a service account token. | `REPLACE_WITH_YOUR_TOKEN` |
   | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL | `https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip` |

   Warning: For security reasons please be sure to add `POLARIS_ACCESS_TOKEN` as a secret to avoid exposing it in CI logs
2. Add a [coverity.yaml](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cli/topics/options_reference.html) file in the project repository. (Uncompiled languages are detected and configured automatically).

   ```
   capture:
     build:
       clean-command: mvn -B clean
       build-command: mvn -B -DskipTests package
   ```

   Note: This example above uses Maven and showcases the contents of coverity.yaml. You can use Maven but you can also substitute your own build and clean commands by following these instructions: [Configuring Coverity Thin Client for use with Bridge CLI and Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/3d79ddc1d59ccc31d9e8859e179b61e7.topic).
3. Add the following YAML to the CI pipeline

   Note: Please remember to substitute example variable values with your own desired values such as correct project branches, repository names, application name.

   Please also remember to replace the placeholders written as such: `<replace_with_your_organization_name>`

   Paste this example and please remember to change the applicable variable values with your own, such as: names of branches, project name, application name.

   ```
   # example pipeline for Polaris scans using the Bridge CLI
   trigger:
   - main
   - develop

   pool:
     vmImage: ubuntu-latest

   variables:
     - group: poc.polaris.synopsys.com

   steps:
   - task: JavaToolInstaller@0
     displayName: 'Use Java 17'
     inputs:
       versionSpec: 17
       jdkArchitectureOption: x64
       jdkSourceOption: PreInstalled

   - task: Maven@4
     displayName: 'Maven Build'
     inputs:
       options: '-B -DskipTests'

   - bash: |
       curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
       $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage polaris
     env:
       BRIDGE_POLARIS_SERVERURL: $(POLARIS_SERVER_URL)
       BRIDGE_POLARIS_ACCESSTOKEN: $(POLARIS_ACCESS_TOKEN)
       BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SAST,SCA'
       BRIDGE_POLARIS_APPLICATION_NAME: $(Build.Repository.Name)
       BRIDGE_POLARIS_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_POLARIS_BRANCH_NAME: $(Build.SourceBranchName)
       BRIDGE_POLARIS_FIXPR_ENABLED: true
       BRIDGE_POLARIS_REPORTS_SARIF_CREATE: true
     displayName: 'Polaris Full Scan'
     condition: not(eq(variables['Build.Reason'], 'PullRequest'))

   - bash: |
       curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
       $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage polaris
     env:
       BRIDGE_POLARIS_SERVERURL: $(POLARIS_SERVER_URL)
       BRIDGE_POLARIS_ACCESSTOKEN: $(POLARIS_ACCESS_TOKEN)
       BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SAST,SCA'
       BRIDGE_POLARIS_APPLICATION_NAME: $(Build.Repository.Name)
       BRIDGE_POLARIS_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_POLARIS_BRANCH_NAME: $(Build.SourceBranchName)
       BRIDGE_POLARIS_BRANCH_PARENT_NAME: $(System.PullRequest.targetBranchName)
       BRIDGE_POLARIS_PRCOMMENT_ENABLED: true
       BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
       BRIDGE_AZURE_ORGANIZATION_NAME: <replace_with_your_organization_name>
       BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(System.PullRequest.SourceBranch)
       BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(System.PullRequest.PullRequestId)
     displayName: 'Polaris PR Scan'
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

   Note: This quickstart example configures SAST and SCA assessments. To configure DAST assessments, set the `POLARIS_ASSESSMENT_TYPES` variable to `DAST`. Please refer to Using Bridge CLI With Polaris for DAST configuration requirements.

## Useful resources

- [Polaris product documentation](https://polaris.blackduck.com/developer/default/)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/3.0.0/)
