---
title: "Using the GitHub App with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-github-app-with-coverity.html"
content_id: "2SbwSoWlZYxvYBaVn9MJew"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:39.348325+00:00"
---

# Using the GitHub App with Coverity

This guide explains the variables, secrets and token required by the GitHub App for generating a Coverity scan workflow. Furthermore, an overview of the scan and post scan configuration options are explained.

## Configuring required variables, secrets and token

- The table below outlines the secrets, variables and GitHub token required for generating a workflow for a Coverity scan. Secrets and variables should be configured in the organization and/or repositories where the GitHub workflow file will be deployed.

  Note: A GitHub Token is required for injecting Pull Request comments in addition to creating fix Pull Requests and SARIF reports. Please refer to secrets and variables setup for further details on how to configure.

  | Type | Name | Description | Example |
  | --- | --- | --- | --- |
  | Variable | `COVERITY_URL` | Coverity server URL | `https://coverity.blackduck.com` |
  | Secret | `COVERITY_USER` | Coverity username | `COVERITY_USERNAME` |
  | Secret | `COVERITY_PASSPHRASE` | Coverity password | `COVERITY_PASSWORD` |
  | Token | `GITHUB_TOKEN` | By default, the workflow uses GitHub’s built-in `GITHUB_TOKEN`, which must be granted [additional permissions](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization) (including write access) in your **repository** or **organization** settings. This option is enabled by default.  Alternatively, for setups that require more granular control, a Personal Access Token (PAT) can be created and stored in a secret associated with the organization or repository.  For detailed instructions on configuring token permissions, please refer to the User Guide. | `github_token: ${{ secrets.GITHUB_TOKEN }}` or  `BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}` |

Note: Ensure all required variables, secrets and the GitHub Token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

## Configuring a Coverity scan

The `Configure options` screen illustrated below provides an intuitive interface for configuring branches, runner, platform, scan and post-scan options. These are used to generate a GitHub workflow for performing a Coverity scan.

Note: Ensure all required GitHub variables and secrets are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

[image: Coverity Scan Options]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the `push events` and `pull request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner**: Choose the environment for the GitHub runner, such as `ubuntu-latest`.
- **Platform**: Select Coverity to generate a workflow that will perform a Coverity scan. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which GitHub variables and secrets are required for the generated workflow to run successfully.

  **Scan method:** Choose between:

  - `GitHub Action (default)`: Generate a scan workflow that uses Black Duck Security Scan GitHub Action.
  - `CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

**Scan options**

It can be seen from the screenshot above that a workflow can be generated with the following scan options:

- **Run analysis locally**: Performs local analysis with full toolkit. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).
- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a GitHub build artifact.
  - **Wait for scan to complete**: When checked this will block injecting pull request comments until the scan completes.
  - **Fail build if policy violations are found**: If this option is checked, then if there are policy violations the build will break.

**Post scan options**

The following post scan options can be configured and require a GitHub Token to be created as outlined in the prerequisites:

- **Decorate pull requests with comments**: Each new policy violation introduced within a Pull Request will be summarised within a review comment.

**Workflow options**

It can be seen from the screenshot above that a workflow can be generated with the following workflow options:

- **Add additional options as comments in the generated workflow file**: Selected configuration options and scan parameters are documented as inline comments within the generated YAML file for reference.
- **Run the scan using:**

  - **GitHub Action – Black Duck Security Scan (recommended, default)**: Executes the scan using the official Black Duck Security Scan GitHub Action (blackduck-inc/black-duck-security-scan@v2).
  - **CLI – Black Duck Bridge CLI**: Downloads and runs the latest Black Duck Bridge CLI directly within the workflow.

## Reviewing a Coverity workflow

This section will explain an overview of reviewing a workflow, assuming the following Coverity scan configuration options:

- **Branches:** `main`, `master`, `develop`, `stage`, `release`
- **Runner configuration**: `ubuntu-latest`
- **Platform**: Coverity
- **Scan options**:
  - Run analysis locally
  - Capture diagnostics information
  - Wait for scan to complete and fail build if policy violations found
- **Post scan options**:
  - Decorate pull request with comments
- **Workflow options**:

  - Run the scan using:

    - GitHub Action – Black Duck Security Scan (recommended, default)
    - CLI – Black Duck Bridge CLI
  - Note: By default, the workflow uses the Black Duck Security Scan GitHub Action. If Black Duck Bridge CLI is selected in the Configure Options screen, the generated workflow will include steps to download and execute the latest Bridge CLI instead of the Action. The preview below reflects the default (recommended) GitHub Action configuration.

The Coverity generated and corresponding `review workflow` screen is displayed below.

**Generated Black Duck Security Scan Action workflow**

```
# Quickstart: Black Duck Security Scan Action with coverity:
#     https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-coverity.html
name: Coverity Scan
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
  contents: write               # Enables pushing commits and creating fix branches
  pull-requests: write          # Allows commenting on and creating pull requests
jobs:
  coverity:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source
        uses: actions/checkout@v5

      - name: Coverity Scan
        id: coverity-scan
        uses: blackduck-inc/black-duck-security-scan@v2
        with:
          ### SCANNING: Required fields
          coverity_url: ${{ vars.COVERITY_URL }}
          coverity_user: ${{ secrets.COVERITY_USER }}
          coverity_passphrase: ${{ secrets.COVERITY_PASSPHRASE }}
          ### GITHUB TOKEN
          github_token: ${{ secrets.GITHUB_TOKEN }}  # Required when PR comments or sarif reports enabled
          coverity_prComment_enabled: true

          ### LOCAL ANALYSIS: Uncomment below to enable
          # coverity_local: false # Enable local analysis mode

          ### SCAN CONFIGURATION: Uncomment below to enable
          # coverity_waitForScan: true # Wait for scan completion before proceeding

          ### Mark build status if policy violating issues are found
          # mark_build_status: failure # Set to success, failure, or skip

          ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
          # include_diagnostics: false
```

**Generated Bridge CLI workflow**

```
name: Coverity Bridge CLI Scan
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
jobs:
  coverity:
    runs-on: ubuntu-latest
    env:
      ### SCANNING: Required fields
      BRIDGE_COVERITY_CONNECT_URL: ${{ vars.COVERITY_URL }}
      BRIDGE_COVERITY_CONNECT_USER_NAME: ${{ secrets.COVERITY_USER }}
      BRIDGE_COVERITY_CONNECT_USER_PASSWORD: ${{ secrets.COVERITY_PASSPHRASE }}
      ### SCANNING: Configuration fields
      BRIDGE_COVERITY_CONNECT_PROJECT_NAME: ${{ github.event.repository.name }}
      BRIDGE_COVERITY_CONNECT_STREAM_NAME: ${{ github.event.repository.name }}-${{ github.base_ref || github.ref_name }}
      ### GitHub repository information
      BRIDGE_GITHUB_REPOSITORY_OWNER_NAME: ${{ github.repository_owner }}
      BRIDGE_GITHUB_REPOSITORY_NAME: ${{ github.event.repository.name }}
      BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME: ${{ github.head_ref || github.ref_name }}
      ### LOCAL ANALYSIS
      BRIDGE_COVERITY_LOCAL: "true"
      ### PULL REQUEST COMMENTS
      BRIDGE_COVERITY_PRCOMMENT_ENABLED: "true"
      ### GITHUB TOKEN
      BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      ### GitHub pull request information
      BRIDGE_GITHUB_REPOSITORY_PULL_NUMBER: ${{ github.event.pull_request.number || github.event.number || 0 }}
      ### TOOLING: Bridge CLI download URL
      BRIDGE_DOWNLOAD_URL: https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest

      ### SCANNING: Optional fields
      # BRIDGE_COVERITY_WAIT_FOR_SCAN: true
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

      - name: Coverity Scan
        run: ${{ env.BRIDGE_CLI_INSTALL_DIR }} --stage connect  --diagnostics
```

**Review workflow screen**

[image: Workflow review UI]

The following points can be observed:

- The workflow review screen displays a preview of the generated workflow with a default workflow filename of `coverity-workflow.yml`.
- The generated workflow contains the triggers for push events and Pull Requests that target the branches: `main`, `master`, `develop`, `stage`, `release`.
- A job named `coverity` has been integrated into the workflow to run in the `ubuntu-latest` environment.
- The generated `coverity` job performs a checkout of the repository source and then runs the `Coverity Scan` step to execute a scan using the Black Duck Security Scan Action.
  - The app has automatically generated the parameters based on the scan options specified in the UI. Please refer to the Black Duck Security Scan Action for Coverity documentation for an explanation of the available parameters.
  - A permissions block is included to support post-scan features (e.g., PR comments).
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
