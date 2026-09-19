---
title: "Using the GitHub App with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-github-app-with-black-duck-sca.html"
content_id: "7~8Z5RF~RGZk7QMxGcX7iw"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:40.572430+00:00"
---

# Using the GitHub App with Black Duck SCA

This guide explains the variables, secrets and token required by the GitHub App for generating a Black Duck® SCA scan workflow. Furthermore, an overview of the scan and post scan configuration options are explained.

## Configuring required variables, secrets and token

- **Secrets and variables**: The table below outlines the secrets, variables and GitHub token required for generating a workflow for a Black Duck® SCA scan. Secrets and variables should be configured in the organization and/or repositories where the GitHub workflow file will be deployed.

  Note: A GitHub Token is required for injecting Pull Request comments in addition to creating fix Pull Requests and SARIF reports. Please refer to secrets and variables setup for further details on how to configure.

  | Type | Name | Description | Example |
  | --- | --- | --- | --- |
  | Variable | `BLACKDUCKSCA_URL` | Black Duck® SCA server URL | `https://sca.blackduck.com` |
  | Secret | `BLACKDUCKSCA_TOKEN` | Black Duck® SCA access token | `SCA_ACCESS_TOKEN` |
  | Token | `GITHUB_TOKEN` | By default, the workflow uses GitHub’s built-in `GITHUB_TOKEN`, which must be granted [additional permissions](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization) (including write access) in your **repository** or **organization** settings. This option is enabled by default.  Alternatively, for setups that require more granular control, a **Personal Access Token (PAT)** can be created and stored in a secret associated with the organization or repository.  For detailed instructions on configuring token permissions, please refer to the User Guide. | `github_token: ${{ secrets.GITHUB_TOKEN }}` or  `BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}` |

Note: Ensure all required GitHub variables, secrets and the GitHub Token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

## Configuring a Black Duck® SCA scan

The `Configure options` screen illustrated below provides an intuitive interface for configuring branches, runner, platform, scan and post-scan options. These are used to generate a GitHub workflow for performing a Black Duck® SCA scan.

Note: Ensure all required GitHub variables and secrets are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

[image: BlackDuck SCA Scan Options]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the `push events` and `pull request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner**: Choose the environment for the GitHub runner, such as `ubuntu-latest`.
- **Platform**: Select Black Duck® SCA to generate a workflow that will perform a Black Duck® SCA scan. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which GitHub variables and secrets are required for the generated workflow to run successfully.
- **Scan method:** Choose between:

  - `GitHub Action (default)`: Generate a scan workflow that uses Black Duck Security Scan GitHub Action.
  - `CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

**Scan options**

A workflow can be generated with the following scan options:

- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a GitHub build artifact.
- **Wait for scan to complete**: If checked the wait operation will block post scan actions until the scan is complete. This ensures that subsequent post scan steps (such as creating a SARIF file or injecting Pull Request comments) will only be executed once the analysis is fully finished.
- **Fail build if policy violations are found**: If this option is checked, then if there are policy violations the build will break.

**Post scan options**

The following post scan options can be configured and require a GitHub Token as outlined in the prerequisites:

[image: Black Duck SCA Post Scan Options]

- **Decorate pull requests with comments**: When checked then each new policy violation introduced within a Pull Request will be summarised within a review comment.
- **Automatically create fix pull requests**: When checked then each new policy violation for an SCA package assessment will automatically raise a fix Pull Request.
- **Create SARIF file**: When checked a SARIF file will be created. An additional checkbox will be displayed to provide the option to enable upload of the SARIF file to GitHub Advanced Security (requires GitHub Code Security).
- **Upload and display issues in GitHub**: Black Duck® SCA provides two options for integrating scan results with GitHub:
  - **GitHub Issues (default)**: Select this option to have Black Duck® SCA create issues directly in a GitHub repository. To support this workflow, enable **Create SARIF file** so that a SARIF report is generated and used to populate GitHub Issues.
  - **GitHub Advanced Security**: Select this option to have Black Duck® SCA create issues directly in GitHub Advanced Security. The **Create SARIF file** option will automatically be selected so that a SARIF report is generated and used to populate GitHub Advanced Security. You can unselect **Create SARIF file**, however in this case issues will not be uploaded to GitHub Advanced Security.

    Warning: The Create SARIF file option can be unselected. Please note that if the option is unselected then issues will be not be created in GitHub Advanced Security.

**Workflow options**

It can be seen from the screenshot above that a workflow can be generated with the following workflow options:

- **Add additional options as comments in the generated workflow file**: Selected configuration options and scan parameters are documented as inline comments within the generated YAML file for reference.
- **Run the scan using:**

  - **GitHub Action – Black Duck Security Scan (recommended, default)**: Executes the scan using the official Black Duck Security Scan GitHub Action (blackduck-inc/black-duck-security-scan@v2).
  - **CLI – Black Duck Bridge CLI**: Downloads and runs the latest Black Duck Bridge CLI directly within the workflow.

## Reviewing a Black Duck® SCA workflow

This section will explain an overview of reviewing a workflow, assuming the following Black Duck® SCA scan configuration options:

- **Branches:** `main`, `master`, `develop`, `stage`, `release`
- **Runner configuration**: `ubuntu-latest`
- **Platform**: Black Duck® SCA
- **Run scan using**:
  - GitHub Action – Black Duck Security Scan (recommended, default)
  - CLI – Black Duck Bridge CLI

  Note: By default, the workflow uses the Black Duck Security Scan GitHub Action. If Black Duck Bridge CLI is selected in the Configure Options screen, the generated workflow will include steps to download and execute the latest Bridge CLI instead of the Action. The preview below reflects the default (recommended) GitHub Action configuration
- **Scan options**:
  - Capture diagnostics information
  - Wait for scan to complete and fail build if policy violations found
- **Post scan options**:
  - Decorate pull request with comments
  - Automatically create fix pull requests
  - Upload and display issues in GitHub using:
    - GitHub Issues (Selected for Bridge CLI example)
    - GitHub Advanced Security (Selected for Black Duck Security Scan example)
  - Create SARIF file
- **Workflow options**:

  - Add additional options as comments in the generated workflow file

The Black Duck® SCA generated workflow and corresponding `review workflow` screen is displayed below.

****Generated Black Duck Security Scan Action workflow****

```
 # Quickstart: Black Duck Security Scan Action with blackducksca:
#     https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-black-duck-sca.html
name: Black Duck Security Scan
on:
  push:
    branches:
      - main
      - master
      - develop
      - stage
      - release
  pull_request:
    branches:
      - main
      - master
      - develop
      - stage
      - release
  workflow_dispatch: {}
# GitHub token permissions for post-scan actions. Required for built-in GITHUB_TOKEN; if using a PAT with equivalent scopes, permissions block can be commented out.
permissions:
  contents: write               # Required to push changes or create fix branches
  pull-requests: write          # Required to add comments or create fix pull requests
  security-events: write        # Required to upload SARIF results to GitHub Security
jobs:
  blackducksca:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5

      - name: Black Duck Security Scan
        id: black-duck-security-scan
        uses: blackduck-inc/black-duck-security-scan@v2
        with:
          ### SCANNING: Required fields
          blackducksca_url: ${{ vars.BLACKDUCKSCA_URL }}
          blackducksca_token: ${{ secrets.BLACKDUCKSCA_TOKEN }}
          ### Configuration if Bridge diagnostic files needs to be uploaded
          include_diagnostics: true
          ### GITHUB TOKEN
          github_token: ${{ secrets.GITHUB_TOKEN }}  # Required when PR comments or sarif reports enabled
          blackducksca_prComment_enabled: true
          ### FIX PULL REQUEST CREATION
          blackducksca_fixpr_enabled: true
          ### SARIF report parameters
          blackducksca_upload_sarif_report: true  # Upload SARIF report in GitHub Advanced Security tab
          blackducksca_reports_sarif_create: true  # Create SARIF report and upload it as artifact

          ### SCAN CONFIGURATION: Uncomment below to enable
          # blackducksca_waitForScan: true # Wait for scan completion before proceeding

          ### Mark build status if policy violating issues are found
          # mark_build_status: failure # Set to success, failure, or skip
```

**Generated Bridge CLI workflow**

```
# Quickstart: Bridge CLI with blackducksca:
#     https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-cli-with-black-duck-sca.html
name: Black Duck Bridge CLI Scan
on:
  push:
    branches:
      - main
      - master
      - develop
      - stage
      - release
  pull_request:
    branches:
      - main
      - master
      - develop
      - stage
      - release
  workflow_dispatch: {}
# GitHub token permissions for post-scan actions. Required for built-in GITHUB_TOKEN; if using a PAT with equivalent scopes, permissions block can be commented out.
permissions:
  contents: write               # Required to push changes or create fix branches
  pull-requests: write          # Required to add comments or create fix pull requests
  issues: write                 # Required to create github issues
jobs:
  blackducksca:
    runs-on: ubuntu-latest
    env:
      ### SCANNING: Required fields
      BRIDGE_BLACKDUCKSCA_URL: ${{ vars.BLACKDUCKSCA_URL }}
      BRIDGE_BLACKDUCKSCA_TOKEN: ${{ secrets.BLACKDUCKSCA_TOKEN }}
      ### GitHub repository information
      BRIDGE_GITHUB_REPOSITORY_OWNER_NAME: ${{ github.repository_owner }}
      BRIDGE_GITHUB_REPOSITORY_NAME: ${{ github.event.repository.name }}
      BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME: ${{ github.head_ref || github.ref_name }}
      ### PULL REQUEST COMMENTS
      BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: "true"
      ### FIX PULL REQUEST CREATION
      BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: "true"
      ### SCANNING: Optional fields
      BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_CREATE: "true"
      ### SARIF report parameters
      BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: "true"
      ### GITHUB TOKEN
      BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      ### GitHub pull request information
      BRIDGE_GITHUB_REPOSITORY_PULL_NUMBER: ${{ github.event.pull_request.number || github.event.number || 0 }}
      ### TOOLING: Bridge CLI download URL
      BRIDGE_DOWNLOAD_URL: https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest

      ### SCANNING: Optional fields
      # BRIDGE_WAIT_FOR_SCAN: true
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5

      - name: Download & Setup Bridge CLI on Windows
        if: runner.os == 'Windows'
        shell: powershell
        run: |-
          curl.exe -L -o $env:TEMP\bridge.zip "$env:BRIDGE_DOWNLOAD_URL/bridge-cli-bundle-win64.zip"
          Expand-Archive $env:TEMP\bridge.zip -DestinationPath $env:TEMP\bridge -Force
          $exe = Get-ChildItem $env:TEMP\bridge -Recurse -Filter bridge-cli.exe | Select-Object -First 1
          "BRIDGE_CLI_INSTALL_DIR=$($exe.FullName)" | Out-File -FilePath $env:GITHUB_ENV -Append

      - name: Download & Setup Bridge CLI on macOS/Linux
        if: runner.os != 'Windows'
        shell: bash
        run: |-
          OS=$([[ "$RUNNER_OS" == "macOS" ]] && ([[ $(uname -m) =~ arm ]] && echo macos_arm || echo macosx) || ([[ $(uname -m) =~ arm ]] && echo linux_arm || echo linux64))
          curl -sSL -o bridge.zip "$BRIDGE_DOWNLOAD_URL/bridge-cli-bundle-$OS.zip"
          unzip -qo bridge.zip -d "$RUNNER_TEMP"
          echo "BRIDGE_CLI_INSTALL_DIR=$(find "$RUNNER_TEMP" -type f -name bridge-cli | head -n1)" >> "$GITHUB_ENV"

      - name: Black Duck SCA Scan
        run: ${{ env.BRIDGE_CLI_INSTALL_DIR }} --stage blackducksca 
# Quickstart: Bridge CLI with polaris:
#     https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-polaris.html
name: Polaris Bridge CLI Scan
on:
  push:
    branches:
      - main
      - master
      - develop
      - stage
      - release
  pull_request:
    branches:
      - main
      - master
      - develop
      - stage
      - release
  workflow_dispatch: {}
# GitHub token permissions for post-scan actions. Required for built-in GITHUB_TOKEN; if using a PAT with equivalent scopes, permissions block can be commented out.
permissions:
  contents: write               # Required to push changes or create fix branches
  pull-requests: write          # Required to add comments or create fix pull requests
  issues: write                 # Required to create github issues
jobs:
  polaris:
    runs-on: ubuntu-latest
    env:
      ### SCANNING: Required fields
      BRIDGE_POLARIS_SERVERURL: ${{ vars.POLARIS_URL }}
      BRIDGE_POLARIS_ACCESSTOKEN: ${{ secrets.POLARIS_ACCESS_TOKEN }}
      ### ASSESSMENT TYPES
      BRIDGE_POLARIS_ASSESSMENT_TYPES: SAST,SCA
      ### SCANNING: Configuration fields
      BRIDGE_POLARIS_APPLICATION_NAME: ${{ github.event.repository.name }}
      BRIDGE_POLARIS_PROJECT_NAME: ${{ github.event.repository.name }}
      BRIDGE_POLARIS_BRANCH_NAME: ${{ github.head_ref || github.ref_name }}
      ### GitHub repository information
      BRIDGE_GITHUB_REPOSITORY_OWNER_NAME: ${{ github.repository_owner }}
      BRIDGE_GITHUB_REPOSITORY_NAME: ${{ github.event.repository.name }}
      BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME: ${{ github.head_ref || github.ref_name }}
      ### SCANNING: Optional fields
      BRIDGE_POLARIS_TEST_SAST_LOCATION: hybrid
      BRIDGE_POLARIS_TEST_SCA_LOCATION: hybrid
      ### Polaris PR Comments
      BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"
      BRIDGE_POLARIS_EXTERNALISSUES_CREATE: "true"
      ### SARIF report parameters
      BRIDGE_POLARIS_REPORTS_SARIF_CREATE: "true"
      ### GITHUB TOKEN
      BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      ### GitHub pull request information
      BRIDGE_GITHUB_REPOSITORY_PULL_NUMBER: ${{ github.event.pull_request.number || github.event.number || 0 }}
      ### TOOLING: Bridge CLI download URL
      BRIDGE_DOWNLOAD_URL: https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest

      ### SCANNING: Optional fields
      # BRIDGE_POLARIS_WAIT_FOR_SCAN: true # Wait for scan to complete
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5

      - name: Download & Setup Bridge CLI on Windows
        if: runner.os == 'Windows'
        shell: powershell
        run: |-
          curl.exe -L -o $env:TEMP\bridge.zip "$env:BRIDGE_DOWNLOAD_URL/bridge-cli-bundle-win64.zip"
          Expand-Archive $env:TEMP\bridge.zip -DestinationPath $env:TEMP\bridge -Force
          $exe = Get-ChildItem $env:TEMP\bridge -Recurse -Filter bridge-cli.exe | Select-Object -First 1
          "BRIDGE_CLI_INSTALL_DIR=$($exe.FullName)" | Out-File -FilePath $env:GITHUB_ENV -Append

      - name: Download & Setup Bridge CLI on macOS/Linux
        if: runner.os != 'Windows'
        shell: bash
        run: |-
          OS=$([[ "$RUNNER_OS" == "macOS" ]] && ([[ $(uname -m) =~ arm ]] && echo macos_arm || echo macosx) || ([[ $(uname -m) =~ arm ]] && echo linux_arm || echo linux64))
          curl -sSL -o bridge.zip "$BRIDGE_DOWNLOAD_URL/bridge-cli-bundle-$OS.zip"
          unzip -qo bridge.zip -d "$RUNNER_TEMP"
          echo "BRIDGE_CLI_INSTALL_DIR=$(find "$RUNNER_TEMP" -type f -name bridge-cli | head -n1)" >> "$GITHUB_ENV"

      - name: Polaris Scan
        run: ${{ env.BRIDGE_CLI_INSTALL_DIR }} --stage polaris --diagnostics
```

**Review workflow screen**

[image: Workflow review UI]

The following points can be observed:

- The workflow review screen displays a preview of the generated workflow with a default workflow filename of `blackducksca-workflow.yml`.
- The generated workflow contains the triggers for push events and Pull Requests that target the branches: `main`, `master`, `develop`, `stage`, `release`.
- A job named `blackducksca` has been integrated into the workflow to run in the `ubuntu-latest` environment.
- The generated `blackducksca` job performs a checkout of the repository source and then runs the `Black Duck Security Scan` step to execute a scan using the Black Duck Security Scan Action.
  - The app has automatically generated the parameters based on the scan options specified in the UI. Please refer to the Black Duck Security Scan Action for Black Duck® SCA documentation for an explanation of the available parameters.
  - A permissions block is included to support post-scan features (e.g., PR comments, Fix PRs, SARIF Upload).
  - Documentation and configuration comments are added at the top for clarity and future reference.
  - Prerequisite secrets and variables have been automatically integrated.

    Important: It is recommended that the built-in GitHub token configured with read-write permission is used in the `github_token` parameter: `github_token: ${{ secrets.GITHUB_TOKEN }}`.
- For Bridge CLI generated workflows an additional step is added to download and install Bridge CLI for the appropriate pipeline environment (Windows or MacOS).

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Use the **Filename** text box to update the default workflow filename if required.
3. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.

## Next steps

Once the **Next** button has been clicked then the Dashboard will redirect to the Summary screen where the workflow can be submitted for deployment to the selected repositories.
