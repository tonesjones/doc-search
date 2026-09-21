---
title: "Using Black Duck Security Bulk Onboarding for Azure DevOps with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-bulk-onboarding-for-azure-devops-with-coverity.html"
content_id: "9WQjns46Kq7_mizxDQN8kA"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:49:59.804039+00:00"
---

# Using Black Duck Security Bulk Onboarding for Azure DevOps with Coverity

This guide explains the variables and secrets required by Black Duck Security Bulk Onboarding for generating a Coverity scan pipeline. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `coverity-pipeline.yml` is detected for a repository selected for onboarding, Black Duck Security Bulk Onboarding overrides the content of the existing file.

## Configuring required variables and secrets

The table below outlines the variables and secrets required for generating a pipeline for a Coverity scan. Secrets and variables should be configured in a variable group within the project(s) where the Azure Pipeline file will be deployed.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `COVERITY_URL` | Coverity server URL | `https://coverity.blackduck.com` |
| Secret | `COVERITY_USER` | Coverity username | `$COVERITY_USER` |
| Secret | `COVERITY_PASSPHRASE` | Coverity password | `$COVERITY_PASSPHRASE` |

Note: Ensure all required variables are configured in a variable group before proceeding to generate the scan pipeline for review and deployment.

## Configuring a Coverity scan

The **Configure options** screen provides an intuitive interface for configuring branches, pool, variable groups, platform, scan and post-scan options. These are used to generate an Azure Pipeline for performing a Coverity scan.

Note: Ensure all required variable group secrets are configured before clicking Next to proceed with generating a scan pipeline for review and deployment.

[image: image]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the push events and pull request text box to specify which branches will initiate scans for each type of event.
- **Pool selection**: Choose the agent pool for the Azure Pipeline. Select from Microsoft-hosted pools (e.g., `ubuntu-latest`) or self-hosted pools available in your project.
- **Variable groups**: Select the variable group containing Coverity credentials (`COVERITY_URL`, `COVERITY_USER`, `COVERITY_PASSPHRASE`).
- **Platform**: Select Coverity from the platform options. The Dashboard UI will dynamically update to display Coverity specific scan options.
- **Scan method**: Choose between:

  - **Azure Pipeline - Black Duck Security Scan (recommended)**: Generate a scan pipeline using the `BlackDuckSecurityScan@2` task.
  - **CLI - Black Duck Bridge CLI**: Generate a scan pipeline that downloads and uses Bridge CLI directly.

**Scan options**

A pipeline can be generated with the following scan options:

- **Run analysis locally**: Performs local analysis with the full toolkit. For further details relating to the different Coverity deployment models supported, see [Coverity deployment architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/deploy-install-guide/topics/deployment_planning1.html).
- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a build artifact.
- **Wait for scan to complete**: When checked, this will block injecting pull request comments until the scan completes.
- **Fail build if policy violations are found**: If this option is checked, then if there are policy violations, the build status will be marked as `SucceededWithIssues`.

**Post scan options**

The following post scan options can be configured:

- **Decorate pull requests with comments**: Each new policy violation introduced within a Pull Request will be summarized within a review comment. This requires `$(System.AccessToken)` to be available in the pipeline.

**Workflow options**

- Add additional options as comments in the generated workflow file

## Reviewing a Coverity pipeline

This section explains an overview of reviewing a pipeline, assuming the following Coverity scan configuration options:

- **Branches**: `main`, `master`, `develop`, `stage`, `release`
- **Pool**: Microsoft-hosted with `ubuntu-latest`
- **Variable group**: `coverity`
- **Platform**: Coverity
- **Scan options**: Wait for scan to complete
- **Post scan options**: Decorate pull requests with comments
- **Scan method**: Azure Pipeline task (recommended) or Bridge CLI

**Generated Azure pipeline task workflow**

```
trigger:
  - main
  - master
  - develop
  - stage
  - release
pool:
  vmImage: ubuntu-latest
variables:
  - group: 'coverity'
  - name: coverityStreamName
    value: $[format('{0}-{1}', variables['Build.Repository.Name'], coalesce(variables['System.PullRequest.targetBranchName'], variables['Build.SourceBranchName']))]
steps:
  - task: BlackDuckSecurityScan@2
    displayName: Coverity Scan
    inputs:
      COVERITY_URL: $(COVERITY_URL)
      COVERITY_USER: $(COVERITY_USER)
      COVERITY_PASSPHRASE: $(COVERITY_PASSPHRASE)
      COVERITY_PROJECT_NAME: $(Build.Repository.Name)
      COVERITY_STREAM_NAME: $(coverityStreamName)
      COVERITY_PRCOMMENT_ENABLED: true
      AZURE_TOKEN: $(System.AccessToken)
```

Note: By default, the pipeline uses the Azure Pipeline task. If Bridge CLIis selected in the Configure Options screen, the generated pipeline will include scripts to download and execute bridge-cli.

**Generated Bridge CLI workflow**

```
trigger:
  - main
  - master
  - develop
  - stage
  - release
jobs:
  - job: coverity
    displayName: Coverity Scan
    pool:
      vmImage: ubuntu-latest
    variables:
      - group: 'coverity'
      - name: BRIDGECLI_DOWNLOAD_URL
        value: https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest
      - name: coverityStreamName
        value: $[format('{0}-{1}', variables['Build.Repository.Name'], coalesce(variables['System.PullRequest.targetBranchName'], variables['Build.SourceBranchName']))]
      - name: azureOrgName
        value: $[replace(replace(variables['System.CollectionUri'], 'https://dev.azure.com/', ''), '/', '')]
      - name: bridgeAzureBranchName
        value: $[coalesce(variables['System.PullRequest.SourceBranch'], variables['Build.SourceBranchName'])]
      - name: bridgeAzurePullNumber
        value: $[coalesce(variables['System.PullRequest.PullRequestId'], '0')]
    steps:
      - bash: |-
          # Detect OS bundle (Linux x64/ARM or macOS x64/ARM)
          UNAME_S="$(uname -s)"; UNAME_M="$(uname -m)"
          if [[ "${UNAME_S}" == "Darwin" ]]; then
            [[ "${UNAME_M}" =~ arm ]] && OS="macos_arm" || OS="macosx"
          else
            [[ "${UNAME_M}" =~ arm ]] && OS="linux_arm" || OS="linux64"
          fi

          # Download & unzip Bridge CLI
          curl -sSL -o bridge.zip "${BRIDGECLI_DOWNLOAD_URL}/bridge-cli-bundle-${OS}.zip"
          unzip -qo -d /tmp bridge.zip && rm -f bridge.zip

          # Execute
          /tmp/bridge-cli-bundle-${OS}/bridge-cli --stage connect
        displayName: Coverity Scan (Linux/macOS)
        condition: ne(variables['Agent.OS'], 'Windows_NT')
        env:
          BRIDGE_COVERITY_CONNECT_URL: $(COVERITY_URL)
          BRIDGE_COVERITY_CONNECT_USER_NAME: $(COVERITY_USER)
          BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $(COVERITY_PASSPHRASE)
          BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_COVERITY_CONNECT_STREAM_NAME: $(coverityStreamName)
          BRIDGE_COVERITY_PRCOMMENT_ENABLED: true
          BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
          BRIDGE_AZURE_ORGANIZATION_NAME: $(azureOrgName)
          BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(bridgeAzureBranchName)
          BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(bridgeAzurePullNumber)
      - powershell: |-
          curl.exe -sSL -o $env:TEMP\bridge.zip "$env:BRIDGECLI_DOWNLOAD_URL/bridge-cli-bundle-win64.zip"
          Expand-Archive $env:TEMP\bridge.zip -DestinationPath $env:TEMP\bridge -Force
          $cli = (Get-ChildItem $env:TEMP\bridge -Recurse -Filter bridge-cli.exe | Select-Object -First 1).FullName

          # Execute
          & $cli --stage connect
        displayName: Coverity Scan (Windows)
        condition: eq(variables['Agent.OS'], 'Windows_NT')
        env:
          BRIDGE_COVERITY_CONNECT_URL: $(COVERITY_URL)
          BRIDGE_COVERITY_CONNECT_USER_NAME: $(COVERITY_USER)
          BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $(COVERITY_PASSPHRASE)
          BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_COVERITY_CONNECT_STREAM_NAME: $(coverityStreamName)
          BRIDGE_COVERITY_PRCOMMENT_ENABLED: true
          BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
          BRIDGE_AZURE_ORGANIZATION_NAME: $(azureOrgName)
          BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(bridgeAzureBranchName)
          BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(bridgeAzurePullNumber)
```

**Review workflow screen**

[image: Review workflow screen coverity]

The following points can be observed:

- The pipeline review screen displays a preview of the generated pipeline with a default filename of `coverity-pipeline.yml`.
- The generated pipeline contains the triggers for push events and Pull Requests that target the configured branches.
- The generated pipeline job performs a checkout of the repository source and then runs the Coverity scan using the Black Duck Security Scan Azure pipeline task or Bridge CLI.
- The bulk onboarding solution has automatically generated the parameters based on the scan options specified in the UI.
- For Bridge CLI generated pipelines, both bash (Linux/macOS) and PowerShell (Windows) scripts are included with OS-based conditions.

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.

Please refer to the Black Duck Security Scan Azure pipeline task documentation for an explanation of the available parameters.

## Next steps

Once the **Next** button has been clicked then the Dashboard will redirect to the Summary screen where the workflow can be submitted for deployment to the selected repositories.
