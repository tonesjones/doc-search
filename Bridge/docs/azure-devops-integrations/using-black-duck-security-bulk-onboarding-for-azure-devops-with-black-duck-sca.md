---
title: "Using Black Duck Security Bulk Onboarding for Azure DevOps with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-bulk-onboarding-for-azure-devops-with-black-duck-sca.html"
content_id: "F3eJYFQ7i7aYYMYefPRpng"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:51:13.545281+00:00"
---

# Using Black Duck Security Bulk Onboarding for Azure DevOps with Black Duck SCA

This guide explains the variables and secrets required by the Black Duck Security Bulk Onboarding for generating a Black Duck® SCA scan pipeline. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `blackducksca-pipeline.yml` is detected for a repository selected for onboarding, Black Duck Security Bulk Onboarding overrides the content of the existing file.

## Configure required variables and secrets

The table below outlines the secrets and variables required for generating a pipeline for a Black Duck® SCA scan. Secrets and variables should be configured in a variable group within the project(s) where the Azure Pipeline file will be deployed.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `BLACKDUCKSCA_URL` | Black Duck® SCA server URL | `https://sca.blackduck.com` |
| Secret | `BLACKDUCKSCA_TOKEN` | Black Duck® SCA access token | `$SCA_TOKEN` |

Note: Ensure all required variables and secrets are configured in a variable group before proceeding to generate the scan pipeline for review and deployment.

## Configuring a Black Duck® SCA scan

The **Configure options** screen provides an intuitive interface for configuring branches, pool, variable groups, platforms, scans, and post-scan options. These are used to generate an Azure Pipeline for performing a Black Duck® SCA scan.

Note: Ensure all required variable group secrets are configured before clicking Next to proceed with generating a scan pipeline for review and deployment.

[image: image]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated.
- **Pool selection**: Choose the agent pool for the Azure Pipeline.
- **Variable groups**: Select the variable group containing Black Duck® SCA credentials (`BLACKDUCKSCA_URL`, `BLACKDUCKSCA_TOKEN`).
- **Platform**: Select **Black Duck® SCA** from the platform options.
- **Scan method**: Choose between Azure Pipeline task (recommended) or Bridge CLI.

**Scan options**

A pipeline can be generated with the following scan options:

- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a build artifact.
- **Wait for scan to complete**: If checked, the wait operation will block post-scan actions until the scan is complete. This ensures that subsequent post-scan steps (such as creating a SARIF file or injecting Pull Request comments) will only be executed once the analysis is fully finished.
- **Fail build if policy violations are found**: If this option is checked, then if there are policy violations, the build status will be marked as `SucceededWithIssues`.

**Post scan options**

The following post scan options can be configured:

- **Decorate pull requests with comments:** When checked a review comment will be created summarizing new vulnerabilities, dependency risks and license issues introduced by the Pull Request.
- **Automatically create fix pull requests**: When checked, SCA package assessments will automatically open Fix Pull Requests for a maximum count of 5 dependency upgrades and vulnerabilities. This uses `$(System.AccessToken)` for authentication.
- **Create SARIF file**: When checked, a SARIF file will be created and can be used for integration with Azure DevOps security features. An additional checkbox will be displayed to provide the option to upload and display issues in Azure Advanced Security.

**Workflow options**

- Add additional options as comments in the generated workflow file

## Reviewing a Black Duck® SCA pipeline

This section explains an overview of reviewing a pipeline, assuming the following Black Duck® SCA scan configuration options:

- **Branches**: `main`, `master`, `develop`, `stage`, `release`
- **Pool**: Microsoft-hosted with `ubuntu-latest`
- **Variable group**: `blackducksca`
- **Platform**: Black Duck® SCA
- **Scan options**: Wait for scan to complete
- **Post scan options**:
  - Decorate pull requests with comments
  - Automatically raise fix pull requests
  - Create SARIF file with Upload issues in Azure Advanced Security selected
- **Scan method**: Azure Pipeline task (recommended) or Bridge CLI

**Generated Azure Pipeline task workflow**

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
  - group: 'blackducksca'
steps:
  - task: BlackDuckSecurityScan@2
    displayName: Black Duck SCA Scan
    inputs:
      BLACKDUCKSCA_URL: $(BLACKDUCKSCA_URL)
      BLACKDUCKSCA_TOKEN: $(BLACKDUCKSCA_TOKEN)
      BLACKDUCKSCA_PRCOMMENT_ENABLED: true
      AZURE_TOKEN: $(System.AccessToken)
      BLACKDUCKSCA_FIXPR_ENABLED: true
      BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
  ### Upload and display issues in Azure Advanced Security
  - task: AdvancedSecurity-Publish@1
    inputs:
      SarifsInputDirectory: $(Build.SourcesDirectory)/.blackduck/integrations/blackducksca/sarif
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
  - job: blackducksca
    displayName: Black Duck SCA Scan
    pool:
      vmImage: ubuntu-latest
    variables:
      - group: 'blackducksca'
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
          /tmp/bridge-cli-bundle-${OS}/bridge-cli --stage blackducksca
        displayName: Black Duck SCA Scan (Linux/macOS)
        condition: ne(variables['Agent.OS'], 'Windows_NT')
        env:
          BRIDGE_BLACKDUCKSCA_URL: $(BLACKDUCKSCA_URL)
          BRIDGE_BLACKDUCKSCA_TOKEN: $(BLACKDUCKSCA_TOKEN)
          BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: true
          BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: true
          BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
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
          & $cli --stage blackducksca
        displayName: Black Duck SCA Scan (Windows)
        condition: eq(variables['Agent.OS'], 'Windows_NT')
        env:
          BRIDGE_BLACKDUCKSCA_URL: $(BLACKDUCKSCA_URL)
          BRIDGE_BLACKDUCKSCA_TOKEN: $(BLACKDUCKSCA_TOKEN)
          BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: true
          BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: true
          BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
          BRIDGE_AZURE_USER_TOKEN: $(System.AccessToken)
          BRIDGE_AZURE_ORGANIZATION_NAME: $(azureOrgName)
          BRIDGE_AZURE_REPOSITORY_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_PROJECT_NAME: $(Build.Repository.Name)
          BRIDGE_AZURE_REPOSITORY_BRANCH_NAME: $(bridgeAzureBranchName)
          BRIDGE_AZURE_REPOSITORY_PULL_NUMBER: $(bridgeAzurePullNumber)
```

**Review workflow screen**

[image: Review blackducksca]

The following points can be observed

- The pipeline review screen displays a preview of the generated pipeline with a default filename of `blackducksca-pipeline.yml`.
- The generated pipeline contains triggers for push events and pull requests.
- The bulk onboarding solution has automatically generated the parameters based on the scan options specified in the UI.
- When SARIF reporting is enabled, `POLARIS_REPORTS_SARIF_CREATE` is included for full scans
- For Bridge CLI generated pipelines, both bash (Linux/macOS) and PowerShell (Windows) scripts are included with OS-based conditions.

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
3. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.

Please refer to the Black Duck Security Scan Azure pipeline task documentation for an explanation of the available parameters.

## Next steps

Once the **Next** button has been clicked then the Dashboard will redirect to the Summary screen where the workflow can be submitted for deployment to the selected repositories.
