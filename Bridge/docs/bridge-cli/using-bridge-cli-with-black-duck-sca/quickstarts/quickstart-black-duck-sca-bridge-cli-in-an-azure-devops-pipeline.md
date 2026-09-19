---
title: "Quickstart: Black Duck SCA Bridge CLI in an Azure DevOps pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-sca-bridge-cli-in-an-azure-devops-pipeline.html"
content_id: "ciwUJzw7pa1UrIfDJvYLog"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:12.323911+00:00"
---

# Quickstart: Black Duck SCA Bridge CLI in an Azure DevOps pipeline

As an alternative to the [Black Duck Security Scan Extension for Azure DevOps](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-security-scan), the Bridge CLI can be downloaded and directly executed in an Azure DevOps pipeline. It has all the functionality of the extension, but requires an additional step to [download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Black Duck® SCA parameters must be passed directly inside the pipeline. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Extension for Azure DevOps (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The extension has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Extension and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Azure DevOps prerequisites
  - Pull Request comments
  - Fix Pull Requests
  - List Of mandatory And optional parameters for Black Duck SCA
  - Additional Azure DevOps parameters
- Admin access to an Azure DevOps project.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- The built-in Azure DevOps [System Access Token](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/access-tokens) is required to allow the pipeline to inject Pull Request review comments. Ensure that **Contribute to pull requests** , **Create branch** and **Delete or disable repository** are set to **Allow** for the build service user in Project > Project Settings > Repository > Security.
- For security reasons, it is advisable to use [Azure DevOps secret variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#secret-variables) to store credentials and access tokens. Secret variables can be defined locally within a [pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#secret-variables) or shared between pipelines using a [variable group](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops&tabs=azure-pipelines-ui%2Cyaml).
- Add the following variables and secrets to a variable group (Pipelines > Library > Variable groups) or directly within a pipeline (Pipelines > Select A Pipeline > Edit > Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BLACKDUCK_URL` | Variable | Black Duck SCA Server URL | `https://blackduck.example.com` |
  | `BLACKDUCK_API_TOKEN` | Secret | Black Duck SCA API Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- The following Bridge CLI environment variables are used directly within the pipeline to inject Pull Request comments and raise fix Pull Requests:

  | Parameter | Description | Value | Scan type |
  | --- | --- | --- | --- |
  | `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` | Raise Fix PRs for detected issues | `true` | Full |
  | `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` | Enable PR comments | `true` | PR |
  | `BRIDGE_AZURE_REPOSITORY_PULL_NUMBER` | ID of PR with source code to scan | `$(System.PullRequest.PullRequestId)` |

## Instructions

1. Add the following pipeline configuration to your repository at `azure-pipelines.yml`.

   Note: For compiled languages, uncomment build steps (`Install JDK` and `Maven Build`) in the provided pipeline configuration. Adjust the build steps to align with project specific build tools and requirements, such as Maven, Gradle, or other build systems.

   ```
   trigger:
   - main
   - develop
   pool:
     vmImage: ubuntu-latest
   variables:
     - group: blackduck-sca-variables
   steps:
   # - task: JavaToolInstaller@0
   #  displayName: 'Install JDK'
   #  inputs:
   #    versionSpec: 21
   #    jdkArchitectureOption: x64
   #    jdkSourceOption: PreInstalled
   # - task: Maven@4
   #  displayName: 'Maven Build'
   #  inputs:
   #    options: '-B -DskipTests'
   - bash: |
       set -ex
       curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
       $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca
     env:
       BRIDGE_BLACKDUCKSCA_URL: $(BLACKDUCK_URL)
       BRIDGE_BLACKDUCKSCA_TOKEN: $(BLACKDUCK_API_TOKEN)
       BRIDGE_BLACKDUCKSCA_SCAN_FULL: true
       BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: 'BLOCKER'
       BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: true
       BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
       BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
       BRIDGE_AZURE_ORGANIZATION_NAME: <replace_with_your_organization_name>
       BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(Build.SourceBranchName)
       DETECT_PROJECT_NAME: $(Build.Repository.Name)
       DETECT_PROJECT_VERSION_NAME: $(Build.SourceBranchName)
       DETECT_CODE_LOCATION_NAME: $(Build.Repository.Name)-$(Build.SourceBranchName)
     displayName: 'Black Duck Full Scan'
     condition: not(eq(variables['Build.Reason'], 'PullRequest'))
   - bash: |
       set -ex
       curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $(Agent.TempDirectory) bridge.zip && rm -f bridge.zip
       $(Agent.TempDirectory)/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca
     env:
       BRIDGE_BLACKDUCKSCA_URL: $(BLACKDUCK_URL)
       BRIDGE_BLACKDUCKSCA_TOKEN: $(BLACKDUCK_API_TOKEN)
       BRIDGE_BLACKDUCKSCA_SCAN_FULL: false
       BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: true
       BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
       BRIDGE_AZURE_ORGANIZATION_NAME: <replace_with_your_organization_name>
       BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
       BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(System.PullRequest.SourceBranch)
       BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(System.PullRequest.PullRequestId)
       DETECT_PROJECT_NAME: $(Build.Repository.Name)
       DETECT_PROJECT_VERSION_NAME: $(System.PullRequest.targetBranchName)
       DETECT_CODE_LOCATION_NAME: $(Build.Repository.Name)-$(System.PullRequest.targetBranchName)
     displayName: 'Black Duck PR Scan'
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

   The pipeline will download Bridge CLI from the URL contained in the `BRIDGECLI_LINUX64` environment variable for direct execution in the pipeline. Bridge CLI will use the `BRIDGE_AZURE` environment variables to access the repository for scanning branches and Pull Requests.One of the following Black Duck SCA scans will be triggered depending on the event type:
   - **Full scan**: Triggered by push events to the specified branches (main, develop). This scan:
     - Performs a complete SCA assessment of all dependencies
     - Creates a SARIF report for security findings
     - Enables fix pull request generation for vulnerable dependencies
     - Fails the build on BLOCKER severity vulnerabilities
   - **Pull Request scan**: Triggered for pull request events. This scan:
     - Performs a differential analysis between the pull request and target branch
     - Automatically adds review comments for new vulnerabilities introduced in the pull request
     - Uses the target branch as the baseline for comparison

   Note: To enable diagnostic logging, enable the "Copy Log Files" and "Publish Log Files" tasks at the end of the pipeline configuration. This will archive Bridge CLI logs as pipeline artifacts for troubleshooting.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment: [image: Merge request review comments injected by SCA merge request scan]

## Useful resources

- [Black Duck Product documentation](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic&Version=latest)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
- [Azure DevOps pipelines documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/)
