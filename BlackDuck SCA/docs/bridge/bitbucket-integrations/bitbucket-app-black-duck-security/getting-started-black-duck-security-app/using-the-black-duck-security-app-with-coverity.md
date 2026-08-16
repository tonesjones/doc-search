---
title: "Using the Black Duck Security App with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-app-with-coverity.html"
content_id: "pbImldil4toKmsFDd8LHEQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:48:54.719267+00:00"
---

# Using the Black Duck Security App with Coverity

This guide explains the variables, secrets and token required by the Black Duck Security App for generating a Coverity scan workflow. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `bitbucket‑pipelines.yml` is detected for a repository selected for onboarding, the Black Duck Security App merges the new scan workflow to ensure the existing pipeline is not replaced.

## Configuring required variables, secrets and token

- The table below outlines the secrets, variables, and Bitbucket token required for generating a workflow for a Coverity scan. Secrets and variables should be configured in the workspace and/or repositories where the Bitbucket workflow file will be deployed.

Note: A Bitbucket token is required as a parameter in the workflow file for injecting Pull Request comments in addition to creating fix Pull Requests and SARIF reports.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `BRIDGE_COVERITY_URL` | Coverity server URL | `https://coverity.blackduck.com` |
| Secret | `BRIDGE_COVERITY_USER` | Coverity username | `$COVERITY_USER` |
| Secret | `BRIDGE_COVERITY_PASSPHRASE` | Coverity password | `$COVERITY_PASSPHRASE` |
| Token | `BRIDGE_BITBUCKET_API_TOKEN` | Required for PR comments, Fix PR, and SARIF.  For detailed instructions on configuring token permissions, please refer to Configure Bitbucket API token. | `$BITBUCKET_REPO_ACCESS_TOKEN` |

Note: Ensure all required variables, secrets, and the BitBucket token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

## Configuring a Coverity scan

The `Configure options` screen illustrated below provides an intuitive interface for configuring branches, runner, platform, scan and post-scan options. These are used to generate a Bitbucket workflow for performing a Coverity scan.

Note: Ensure all required Bitbucket variables and secrets are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

[image: Bitbucket App Coverity Scan Options]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the `push events` and `pull request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner**: Specify the Bitbucket runner tag. If the runner is windows, the **windows** tag is required along with any other runner tag. Runner tags are comma-separated, for example: `windows`, `my.runner`.
- **Platform**: Select Coverity to generate a workflow that will perform a Coverity scan. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which Bitbucket variables and secrets are required for the generated workflow to run successfully.

  **Scan method:** Choose between:

  - `CLI (default)`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.
  - `Bitbucket Pipe`: Generate a scan workflow that uses Black Duck Security Scan Pipe.

    Important: Bitbucket Pipe workflows are supported by Atlassian for Linux platforms only (Bitbucket cloud and self-hosted runners).

**Scan options**

It can be seen from the screenshot above that a workflow can be generated with the following scan options:

- **Run analysis locally**: Performs local analysis with the full toolkit. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).
- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a Bitbucket build artifact.

  - **Wait for scan to complete**: When checked, this will block injecting pull request comments until the scan completes.
  - **Fail build if policy violations are found**: If this option is checked, then if there are policy violations, the build will break.

**Post scan options**

The following post scan options can be configured and require a Bitbucket Token to be created as outlined in Bitbucket secrets and variables setup

- **Decorate pull requests with comments**: Each new policy violation introduced within a Pull Request will be summarized within a review comment.

**Workflow options**

It can be seen from the screenshot above that a workflow can be generated with the following workflow options:

- **Add additional options as comments in the generated workflow file**: Selected configuration options and scan parameters are documented as inline comments within the generated YAML file for reference.
- **Run the scan using:**

  - **CLI – Black Duck Bridge CLI (recommended, default)**: Downloads and runs the latest Black Duck Bridge CLI directly within the workflow.
  - **Black Duck Security Scan Pipe**: Executes the scan using the official Black Duck Security Scan Pipe.

## Reviewing a Coverity workflow

This section will explain an overview of reviewing a workflow, assuming the following Coverity scan configuration options:

- **Branches:**`main`, `master`, `develop`, `stage`, `release`
- **Runner configuration**: `runner-tag`
- **Platform**: Coverity
- **Scan options**:

  - Run analysis locally
  - Capture diagnostics information
  - Wait for scan to complete and fail build if policy violations found
- **Post scan options**:

  - Decorate pull request with comments
- **Workflow options**:

  - Run the scan using:

    - CLI – Black Duck Bridge CLI
    - Black Duck Security Scan Pipe (recommended, default)

Note: By default, the workflow uses the Bridge CLI. If Black Duck Security Scan Pipe is selected in the `Configure Options` screen, the generated workflow will include steps to download and execute the Pipe instead of Bridge CLI. The previews below reflect both configurations.

**Generated Bridge CLI workflow**

```
coverity_unix_step: &coverity_unix_step
  name: Coverity Scan
  script:
    - |-
      ### SCANNING: Required fields
      export BRIDGE_COVERITY_CONNECT_URL="${COVERITY_URL}"
      export BRIDGE_COVERITY_CONNECT_USER_NAME="${COVERITY_USER}"
      export BRIDGE_COVERITY_CONNECT_USER_PASSWORD="${COVERITY_PASSPHRASE}"
      ### SCANNING: Configuration fields
      export BRIDGE_COVERITY_CONNECT_PROJECT_NAME="${BITBUCKET_REPO_SLUG}"
      export BRIDGE_COVERITY_CONNECT_STREAM_NAME="${BITBUCKET_REPO_SLUG}-${BITBUCKET_PR_DESTINATION_BRANCH:-$BITBUCKET_BRANCH}"
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
      /tmp/bridge-cli-bundle-${OS}/bridge-cli --stage connect

pipelines:
  branches:
    "{main,master,develop,stage,release}":
      - step: *coverity_unix_step
  pull-requests:
    "**":
      - step: *coverity_unix_step
```

**Review** `bitbucket-pipelines.yml` **screen for Bridge CLI**

[image: Bitbucket App Coverity Workflow Review]

**Generated Black Duck Security Scan Pipe workflow**

```
coverity_scan: &coverity_scan
  name: Coverity Scan
  script:
    - pipe: blackduck-inc/blackduck-security-scan:1.6.0
      variables:
        BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
        BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
        BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSPHRASE
        MARK_BUILD_STATUS: failure

        ### OPTIONAL CONFIGURATION: Uncomment below to enable
        # BRIDGE_COVERITY_LOCAL: "false"

        ### SCAN CONFIGURATION: Uncomment below to wait for scan completion
        # BRIDGE_COVERITY_WAITFORSCAN: "true"

        ### PULL REQUEST COMMENTS: Uncomment below to enable
        # BRIDGE_COVERITY_AUTOMATION_PRCOMMENT: "false"

        ### DIAGNOSTICS: Uncomment below to enable capture of diagnostic information
        # INCLUDE_DIAGNOSTICS: "false"

pipelines:
  branches:
    "{main,master,develop,stage,release}":
      - step: *coverity_scan
  pull-requests:
    "**":
      - step: *coverity_scan
```

**Review** `bitbucket-pipelines.yml` **screen for Black Duck Security Scan Pipe**

[image: Bitbucket App Coverity Pipe Workflow Review Screen]

The following points can be observed:

- The workflow review screen displays a preview of the generated workflow with a default workflow filename of `bitbucket-pipelines.yml`.
- The generated workflow contains the triggers for push events and Pull Requests that target the branches: `main`, `master`, `develop`, `stage`, `release`.
- A job named `coverity` has been integrated into the workflow to run in the Bitbucket Cloud runner.
- The generated pipeline job performs a checkout of the repository source and then runs the `Coverity Scan` step to execute a scan using the Black Duck Security Scan pipe.

  - The app has automatically generated the parameters based on the scan options specified in the UI. Please refer to the Black Duck Security Scan Pipe documentation for an explanation of the available parameters.
  - A permissions block is included to support post-scan features (e.g., PR comments).
  - Configuration comments are added for clarity and future reference.
  - Prerequisite secrets and variables have been automatically integrated.

    Important: It is recommended that the provided Bitbucket token specified as a parameter in the workflow file has the necessary permissions required to create and inject comments on Pull Requests.
- For Bridge CLI generated workflows, an additional step is added to download and install Bridge CLI for the appropriate pipeline environment (Windows or MacOS).

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.

Note: When an existing `bitbucket‑pipelines.yml` is detected for a repository selected for onboarding, the Black Duck Security App merges the new scan workflow to ensure the existing pipeline is not replaced.
