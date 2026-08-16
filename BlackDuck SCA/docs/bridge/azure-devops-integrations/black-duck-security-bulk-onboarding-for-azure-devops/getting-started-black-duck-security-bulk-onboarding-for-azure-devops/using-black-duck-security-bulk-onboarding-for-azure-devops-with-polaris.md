---
title: "Using Black Duck Security Bulk Onboarding for Azure DevOps with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-bulk-onboarding-for-azure-devops-with-polaris.html"
content_id: "Xt8r~qIfj0LHHEfLYiRXOw"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:50:06.005657+00:00"
---

# Using Black Duck Security Bulk Onboarding for Azure DevOps with Polaris

This guide explains the variables and secrets required by the Black Duck Security Bulk Onboarding for generating a Polaris scan pipeline. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `polaris-pipeline.yml` is detected for a repository selected for onboarding, Black Duck Security Bulk Onboarding overrides the content of the existing file.

## Configuring required variables and secrets

The table below outlines the secrets and variables required for generating a pipeline for a Polaris scan. Secrets and variables should be configured in a variable group within the project(s) where the Azure Pipeline file will be deployed.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `POLARIS_SERVER_URL` | Polaris server URL | `https://polaris.blackduck.com` |
| Secret | `POLARIS_ACCESS_TOKEN` | Polaris access token | `$POLARIS_ACCESS_TOKEN` |

Note: Ensure all required variables and secrets are configured in a variable group before proceeding to generate the scan pipeline for review and deployment.

## Configuring a Polaris scan

The **Configure options** screen provides an intuitive interface for configuring branches, pool, variable groups, platforms, scans, and post-scan options. These are used to generate an Azure Pipeline for performing a Polaris scan.

Note: Ensure all required variable group secrets are configured before clicking **Next** to proceed with generating a scan pipeline for review and deployment.

[image: image]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated.
- **Pool selection**: Choose the agent pool for the Azure Pipeline.
- **Variable groups**: Select the variable group containing Polaris credentials (`POLARIS_SERVER_URL`, `POLARIS_ACCESS_TOKEN`).
- **Platform**: Select Polaris from the platform options.
- **Scan method**: Choose between Azure Pipeline task (recommended) or Bridge CLI.

**Scan options**

A pipeline can be generated with the following scan options:

- **Assessment types**: Two scan types are supported: `SAST` and/or `SCA`. When using Polaris source upload, the following test locations are supported:
  - **SAST** : hybrid (default), local or remote
  - **SCA**: hybrid (default) or remote
- **Advanced options:**
  - **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a build artifact.
  - **Wait for scan to complete**: When checked, this will block injecting pull request comments until the scan completes.
  - **Fail build if policy violations are found**: If this option is checked, then if there are policy violations, the build status will be marked as `SucceededWithIssues`.

**Post scan options**

The following post scan options can be configured:

- **Decorate pull requests with comments:** When checked, each new SCA and/or SAST issue introduced by a pull request will be summarized within a review comment. This uses `$(System.AccessToken)` secret by default for authentication.
- **Automatically create fix pull requests:** When checked, SCA package assessments will automatically open fix pull requests for a default maximum count of 5 dependency upgrades and vulnerabilities. This uses `$(System.AccessToken)` secret by default for authentication.
- **Create SARIF file**: When checked, a SARIF report will be generated with findings from the scan, categorized by severity (CRITICAL, HIGH) and issue types (SAST, SCA). An additional checkbox will be displayed to provide the option to upload and display issues in Azure Advanced Security.

**Workflow options**

- Add additional options as comments in the generated workflow file

## Reviewing a Polaris pipeline

This section explains an overview of reviewing a pipeline, assuming the following Polaris scan configuration options:

- **Branches**: `main`, `master`, `develop`, `stage`, `release`
- **Pool**: Microsoft-hosted with `ubuntu-latest`
- **Variable group**: `polaris`
- **Platform**: Polaris
- **Assessment types**: SCA, SAST
  - **Test location**: `hybrid` for SCA and SAST
- **Scan options**: Wait for scan to complete and fail build if policy violations found
- **Post scan options**:
  - Automatically create fix pull requests
  - Decorate pull requests with comments
  - Create SARIF file with Upload issues in Azure Advanced Security selected
- **Scan method**: Azure Pipeline task (recommended) and CLI – Black Duck Bridge CL

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
  - group: 'polaris'
steps:
  - task: BlackDuckSecurityScan@2
    displayName: Polaris Scan
    inputs:
      POLARIS_SERVER_URL: $(POLARIS_SERVER_URL)
      POLARIS_ACCESS_TOKEN: $(POLARIS_ACCESS_TOKEN)
      POLARIS_ASSESSMENT_TYPES: SAST,SCA
      POLARIS_TEST_SAST_LOCATION: hybrid
      POLARIS_TEST_SCA_LOCATION: hybrid
      POLARIS_PRCOMMENT_ENABLED: true
      AZURE_TOKEN: $(System.AccessToken)
      POLARIS_REPORTS_SARIF_CREATE: true
      POLARIS_FIXPR_ENABLED: true
  ### Upload and display issues in Azure Advanced Security
  - task: AdvancedSecurity-Publish@1
    inputs:
      SarifsInputDirectory: $(Build.SourcesDirectory)/.blackduck/integrations/polaris/sarif
```

Note: By default, the pipeline uses the Azure Pipeline task. If Bridge CLIis selected in the Configure Options screen, the generated pipeline will include scripts to download and execute bridge-cli.

****Generated Bridge CLI workflow****

```
trigger:
  - main
  - master
  - develop
  - stage
  - release
jobs:
  - job: polaris
    displayName: Polaris Scan
    pool:
      vmImage: ubuntu-latest
    variables:
      - group: 'polaris'
      - name: BRIDGECLI_DOWNLOAD_URL
        value: https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest
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
          /tmp/bridge-cli-bundle-${OS}/bridge-cli --stage polaris
        displayName: Polaris Scan (Linux/macOS)
        condition: ne(variables['Agent.OS'], 'Windows_NT')
        env:
          BRIDGE_POLARIS_SERVERURL: $(POLARIS_SERVER_URL)
          BRIDGE_POLARIS_ACCESSTOKEN: $(POLARIS_ACCESS_TOKEN)
          BRIDGE_POLARIS_ASSESSMENT_TYPES: SAST,SCA
          BRIDGE_POLARIS_APPLICATION_NAME: $(Build.Repository.Name)
          BRIDGE_POLARIS_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_POLARIS_BRANCH_NAME: $(Build.SourceBranchName)
          BRIDGE_POLARIS_TEST_SAST_LOCATION: hybrid
          BRIDGE_POLARIS_TEST_SCA_LOCATION: hybrid
          BRIDGE_POLARIS_REPORTS_SARIF_CREATE: true
          BRIDGE_POLARIS_FIXPR_ENABLED: true
          BRIDGE_POLARIS_PRCOMMENT_ENABLED: true
          BRIDGE_POLARIS_BRANCH_PARENT_NAME: $(System.PullRequest.targetBranchName)
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
          & $cli --stage polaris
        displayName: Polaris Scan (Windows)
        condition: eq(variables['Agent.OS'], 'Windows_NT')
        env:
          BRIDGE_POLARIS_SERVERURL: $(POLARIS_SERVER_URL)
          BRIDGE_POLARIS_ACCESSTOKEN: $(POLARIS_ACCESS_TOKEN)
          BRIDGE_POLARIS_ASSESSMENT_TYPES: SAST,SCA
          BRIDGE_POLARIS_APPLICATION_NAME: $(Build.Repository.Name)
          BRIDGE_POLARIS_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_POLARIS_BRANCH_NAME: $(Build.SourceBranchName)
          BRIDGE_POLARIS_TEST_SAST_LOCATION: hybrid
          BRIDGE_POLARIS_TEST_SCA_LOCATION: hybrid
          BRIDGE_POLARIS_REPORTS_SARIF_CREATE: true
          BRIDGE_POLARIS_FIXPR_ENABLED: true
          BRIDGE_POLARIS_PRCOMMENT_ENABLED: true
          BRIDGE_POLARIS_BRANCH_PARENT_NAME: $(System.PullRequest.targetBranchName)
          BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
          BRIDGE_AZURE_ORGANIZATION_NAME: $(azureOrgName)
          BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(bridgeAzureBranchName)
          BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(bridgeAzurePullNumber)
```

**Review workflow screen**s

[image: Review workflow screen Polaris]

The following points can be observed:

- The pipeline review screen displays a preview of the generated pipeline with a default filename of `polaris-pipeline.yml`.
- The generated pipeline contains triggers for push events and pull requests.
- For the Azure pipeline task workflow:
  - `POLARIS_APPLICATION_NAME` and `POLARIS_PROJECT_NAME` are automatically set to `$(Build.Repository.Name)`.
- POLARIS_ASSESSMENT_TYPES is configured based on the assessment types selected in the UI.
- `POLARIS_PRCOMMENT_ENABLED` and `AZURE_TOKEN` are included for pull request comment decoration.
- `POLARIS_FIXPR_ENABLED` and `AZURE_TOKEN` are included for fix pull requests.
- When SARIF reporting is enabled, `POLARIS_REPORTS_SARIF_CREATE` is included for full scans.
- The bulk onboarding solution has automatically generated the parameters based on the scan options specified in the UI.
- For Bridge CLI generated pipelines, both bash (Linux/macOS) and PowerShell (Windows) scripts are included with OS-based conditions.

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.

Please refer to the  Black Duck Security Scan Azure pipeline task documentation  for an explanation of the available parameters.

## Next steps

Once the **Next** button has been clicked then the Dashboard will redirect to the Summary screen where the workflow can be submitted for deployment to the selected repositories.
