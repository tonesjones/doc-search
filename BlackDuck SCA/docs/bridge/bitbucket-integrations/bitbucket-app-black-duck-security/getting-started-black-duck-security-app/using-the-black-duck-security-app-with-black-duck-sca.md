---
title: "Using the Black Duck Security App with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-app-with-black-duck-sca.html"
content_id: "h20ONq1_wEvYxskddDVm1g"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:48:56.284169+00:00"
---

# Using the Black Duck Security App with Black Duck SCA

This guide explains the variables, secrets and token required by the Black Duck Security App for generating a Black Duck® SCA scan workflow. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `bitbucket‑pipelines.yml` is detected for a repository selected for onboarding, the Black Duck Security App merges the new scan workflow to ensure the existing pipeline is not replaced.

## Configuring required variables, secrets and token

- The table below outlines the secrets, variables and Bitbucket token required for generating a workflow for a Black Duck® SCA scan. Secrets and variables should be configured in the workspace and/or repositories where the Bitbucket workflow file will be deployed.

Note: A Bitbucket token is required as a parameter in the workflow file for injecting Pull Request comments in addition to creating fix Pull Requests and SARIF reports.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `BLACKDUCKSCA_URL` | Black Duck SCA server URL | `https://sca.blackduck.com` |
| Secret | `BLACKDUCKSCA_TOKEN` | Black Duck SCA access token | `SCA_ACCESS_TOKEN` |
| Token | `BRIDGE_BITBUCKET_API_TOKEN` | Required for PR comments, Fix PR, and SARIF reports.  For detailed instructions on configuring token permissions, please refer to Configure Bitbucket API token. | `$BITBUCKET_REPO_ACCESS_TOKEN` |

Note: Ensure all required variables, secrets, and token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

## Configuring a Black Duck® SCA scan

The `Configure options` screen illustrated below provides an intuitive interface for configuring branches, runner, platform, scan and post-scan options. These are used to generate a Bitbucket workflow for performing a Black Duck® SCA scan.

Note: Ensure all required Bitbucket variables and secrets are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

[image: Black Duck SCA Configuration Screen]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the `push events` and `pull request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner**: Specify the Bitbucket runner tag. If the runner is windows, the **windows** tag is required along with any other runner tag. Runner tags are comma-separated, for example: `windows`, `my.runner`
- **Platform**: Select Black Duck® SCA to generate a workflow that will perform a Black Duck® SCA scan. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which Bitbucket variables and secrets are required for the generated workflow to run successfully.

  **Scan method:** Choose between:

  - `CLI (default)`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.
  - `Bitbucket Pipe`: Generate a scan workflow that uses Black Duck Security Scan Pipe.

    Important: Bitbucket Pipe workflows are supported by Atlassian for Linux platforms only (Bitbucket cloud and self-hosted runners).

**Scan options**

A workflow can be generated with the following scan options:

- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a Bitbucket artifact in the downloads section.
- **Wait for scan to complete**: If checked the wait operation will block post scan actions until the scan is complete. This ensures that subsequent post scan steps (such as creating a SARIF report or injecting Pull Request comments) will only be executed once the analysis is fully finished.
- **Fail build if policy violations are found**: If this option is checked, then if there are policy violations, the build will break.

**Post scan options**

The following post scan options can be configured and require a Bitbucket Token to be created as outlined in Bitbucket secrets and variables setup

- **Decorate pull requests with comments**: When checked then each new policy violation introduced within a Pull Request will be summarized within a review comment.
- **Automatically create fix pull requests**: When checked then each new policy violation for an SCA package assessment will automatically raise a fix Pull Request.
- **Create SARIF file**: When checked a SARIF file will be created. An additional checkbox will be displayed to provide the option to enable upload of the SARIF file to the downloads section of Bitbucket cloud.

**Workflow options**

It can be seen from the screenshot above that a workflow can be generated with the following workflow options:

- **Add additional options as comments in the generated workflow file**: Selected configuration options and scan parameters are documented as inline comments within the generated YAML file for reference.
- **Run the scan using:**

  - **CLI – Black Duck Bridge CLI (recommended, default)**: Downloads and runs the latest Black Duck Bridge CLI directly within the workflow.
  - **Black Duck Security Scan Pipe**: Executes the scan using the official Black Duck Security Scan Pipe.

## Reviewing a Black Duck® SCA workflow

This section will explain an overview of reviewing a workflow, assuming the following Black Duck® SCA scan configuration options:

- **Branches:** `main`, `master`, `develop`, `stage`, `release`
- **Runner configuration**: `runner-tag`
- **Platform**: Black Duck® SCA
- **Scan options**:

  - Capture diagnostics information
  - Wait for scan to complete and fail build if policy violations found
- **Post scan options**:

  - Decorate pull request with comments
  - Automatically create fix pull requests
  - Create SARIF file with upload in Bitbucket enabled
- **Workflow options**:

  - Run the scan using:

    - CLI – Black Duck Bridge CLI (recommended, default)
    - Black Duck Security Scan Pipe

Note: By default, the workflow uses the Bridge CLI. If Black Duck Security Scan Pipe is selected in the Configure Options screen, the generated workflow will include steps to download and execute the Pipe instead of Bridge CLI. The previews below reflect both configurations.

The Black Duck® SCA generated workflow and corresponding `review workflow` screen is displayed below.

**Generated Bridge CLI workflow**

```
blackduck_sca_unix_step: &blackduck_sca_unix_step
  name: Blackducksca Scan
  script:
    - |-
      ### SCANNING: Required fields
      export BRIDGE_BLACKDUCKSCA_URL="${BLACKDUCKSCA_URL}"
      export BRIDGE_BLACKDUCKSCA_TOKEN="${BLACKDUCKSCA_TOKEN}"
      ### Bitbucket repository information
      export BRIDGE_BITBUCKET_WORKSPACE_ID="${BITBUCKET_WORKSPACE}"
      export BRIDGE_BITBUCKET_PROJECT_REPOSITORY_NAME="${BITBUCKET_REPO_SLUG}"
      export BRIDGE_BITBUCKET_PROJECT_REPOSITORY_BRANCH_NAME="${BITBUCKET_BRANCH}"
      ### TOOLING: Bridge CLI download URL
      export BRIDGECLI_DOWNLOAD_URL="https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest"

      ### Download and Execute Bridge CLI
      # Install curl and unzip
      apt update && apt install -y curl unzip

      # Bridge CLI OS bundle (Linux x64/ARM or macOS x64/ARM)
      UNAME_S="$(uname -s)"; UNAME_M="$(uname -m)"
      if [[ "${UNAME_S}" == "Darwin" ]]; then
        [[ "${UNAME_M}" =~ arm ]] && OS="macos_arm" || OS="macosx"
      else
        [[ "${UNAME_M}" =~ arm ]] && OS="linux_arm" || OS="linux64"
      fi

      # Download & unzip Bridge CLI
      curl -fLsS -o bridge.zip "${BRIDGECLI_DOWNLOAD_URL}/bridge-cli-bundle-${OS}.zip" && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip

      # Execute
      /tmp/bridge-cli-bundle-${OS}/bridge-cli --stage blackducksca

pipelines:
  branches:
    "{main,master,develop,stage,release}":
      - step: *blackduck_sca_unix_step
  pull-requests:
    "**":
      - step: *blackduck_sca_unix_step
```

**Review `bitbucket-pipelines.yml` screen for Bridge CLI**

[image: Review Black Duck SCA Bridge CLI Workflow]

**Generated Black Duck Security Scan Pipe workflow**

```
blackduck_sca_scan: &blackduck_sca_scan
  name: Black Duck SCA Scan
  script:
    - pipe: blackduck-inc/blackduck-security-scan:1.6.0
      variables:
        BRIDGE_BLACKDUCKSCA_URL: $BLACKDUCKSCA_URL
        BRIDGE_BLACKDUCKSCA_TOKEN: $BLACKDUCKSCA_TOKEN
        MARK_BUILD_STATUS: failure

        ### SCAN CONFIGURATION: Uncomment below to wait for scan completion
        # BRIDGE_BLACKDUCKSCA_WAITFORSCAN: "true"

        ### DIAGNOSTICS: Uncomment below to enable capture of diagnostic information
        # INCLUDE_DIAGNOSTICS: "false"

        ### PULL REQUEST COMMENTS: Uncomment below to enable
        # BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: "false"

        ### FIX PULL REQUEST CREATION: Uncomment below to enable
        # BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: "false"

        ### SARIF REPORTS: Uncomment below to enable SARIF report generation
        # BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: "false"

pipelines:
  branches:
    "{main,master,develop,stage,release}":
      - step: *blackduck_sca_scan
  pull-requests:
    "**":
      - step: *blackduck_sca_scan
```

**Review `bitbucket-pipelines.yml` screen for Black Duck Security Scan Pipe**

[image: Bitbucket BlackDuck SCA Pipe Workflow Review Screen]

The following points can be observed:

- The workflow review screen displays a preview of the generated workflow with a default workflow filename of `bitbucket-pipelines.yml`.
- The generated workflow contains the triggers for push events and Pull Requests that target the branches: `main`, `master`, `develop`, `stage`, `release`.
- A job named `Black Duck SCA Scan` has been integrated into the workflow to run in the Bitbucket cloud runner.
- The generated  `Black Duck SCA`  job performs a checkout of the repository source and then runs the `Black Duck Security Scan` step to execute a scan using the Black Duck Security Scan pipe.

  - The app has automatically generated the parameters based on the scan options specified in the UI. Please refer to the Black Duck Security Scan Pipe for Black Duck SCA documentation for an explanation of the available parameters.
  - A permissions block is included to support post-scan features (e.g., PR comments, Fix PRs, SARIF Upload).
  - Configuration comments are added for clarity and future reference.
  - Prerequisite secrets and variables have been automatically integrated.

    Important: It is recommended that the provided Bitbucket token specified as a parameter in the workflow file has the necessary permissions required to perform operations such as creating Pull Requests, uploading SARIF files etc.
- For Bridge CLI generated workflows, an additional step is added to download and install Bridge CLI for the appropriate pipeline environment (Windows or MacOS).

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.

When an existing `bitbucket‑pipelines.yml` is detected for a repository selected for onboarding, the Black Duck Security App merges the new scan workflow to ensure the existing pipeline is not replaced.
