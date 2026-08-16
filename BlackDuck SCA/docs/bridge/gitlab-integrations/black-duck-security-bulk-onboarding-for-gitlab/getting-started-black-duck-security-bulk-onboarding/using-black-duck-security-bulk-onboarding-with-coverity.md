---
title: "Using Black Duck Security Bulk Onboarding with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-bulk-onboarding-with-coverity.html"
content_id: "gqiMobU4ULgUBn4Ajk0WhQ"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:47:58.973212+00:00"
---

# Using Black Duck Security Bulk Onboarding with Coverity

This guide explains the variables, secrets and token required by Black Duck Security Bulk Onboarding for generating a Coverity scan workflow. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `coverity-ci.yml` is detected for a project selected for onboarding, Black Duck Security Bulk Onboarding overrides the content of the existing file.

## Configuring required variables, secrets and token

The table below outlines the variables, and GitLab user token required for generating a workflow for a Coverity scan. Secrets and variables should be configured in the groups and/or projects where the GitLab workflow file will be deployed

Note: A GitLab Personal Access Token is required as a parameter in the workflow file for injecting Merge Request comments in addition to creating fix Merge Requests.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `BRIDGE_COVERITY_CONNECT_URL` | Coverity server URL | `https://coverity.blackduck.com` |
| Secret | `BRIDGE_COVERITY_CONECT_USER_NAME` | Coverity username | `$COVERITY_USER` |
| Secret | `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` | Coverity password | `$COVERITY_PASSWORD` |
| Token | `BRIDGE_GITLAB_USER_TOKEN` | Required for Merge Request comments and Fix Merge Requests.  For detailed instructions on configuring token permissions, please refer to the User Guide. | `$GITLAB_USER_TOKEN` |

Note: Ensure all required variables and token are configured before proceeding to generate the scan workflow for review and deployment.

## Configuring a Coverity scan

The `Configure options` screen illustrated below provides an intuitive interface for configuring branches, runner, platform, scan and post-scan options. These are used to generate a GitLab workflow for performing a Coverity scan.

Note: Ensure all required GitLab variables are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

[image: Coverity Scan Configure Options screen]

**General options**

- **Branches**: Scans can be configured to trigger in response to push events and when a Merge Request is created or updated. Use the `push events` and `merge request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner tag**: Choose the environment for the GitLab runner. To generate runner OS specific scripts, select **Mac/Linux** or **Windows** from the `Runner Configuration` option. By default, a Mac/Linux (Bash) script will be generated. Runner tags are comma-separated, for example: `docker,linux,group1-runner`.

  Note: Please select only one type of runner tags (either Mac/Linux or Windows) for the selected projects. If you mix runner types, the workflow may fail because the scripts use different shells (bash vs. PowerShell).

- **Platform**: Select the Black Duck platform for scanning in the project. Supported platforms include Coverity, Black Duck® SCA and Polaris. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which GitLab CI/CD variables are required for the generated workflow to run successfully.
- **Scan method:** Choose between:

  - `GitLab Template (recommended)`: Generate a scan workflow that uses Black Duck Security Scan Template.
  - `CLI - Black Duck Bridge CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

**Scan options**

It can be seen from the screenshot above that a workflow can be generated with the following scan options:

- **Run analysis locally**: Performs local analysis with the full toolkit. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).
- **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a GitLab build artifact.
  - **Wait for scan to complete**: When checked, this will block injecting Pull Request comments until the scan completes.
  - **Fail build if policy violations are found**: If this option is checked, then if there are policy violations, the build will break.

**Post scan options**

The following post scan options can be configured and require a GitLab User Token to be created as outlined in the prerequisites.

- **Decorate pull requests with comments**: Each new policy violation introduced within a Pull Request will be summarized within a review comment.

**Workflow options**

It can be seen from the screenshot above that a workflow can be generated with the following workflow options:

- **Add additional options as comments in the generated workflow file**: Selected configuration options and scan parameters are documented as inline comments within the generated YAML file for reference.
- **Run the scan using:**
  - `GitLab Template (recommended)`: Generate a scan workflow that uses Black Duck Security Scan Template.
  - `CLI - Black Duck Bridge CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

## Reviewing a Coverity workflow

This section will explain an overview of reviewing a workflow, assuming the following Coverity scan configuration options:

- **Branches:** `main`, `master`, `develop`, `stage`, `release`
- **Runner configuration**: `runner tag name` (Use tags for either Mac/Linux or Windows)
- **Platform**: Coverity
- **Scan options**:
  - Run analysis locally
  - Capture diagnostics information
  - Wait for scan to complete and fail build if policy violations found
- **Post scan options**
  - Decorate Pull Request with comments
- **Workflow options**:
  - Run the scan using:
    - **GitLab Template (recommended)**
    - **CLI - Black Duck Bridge CLI**

Note: By default, the workflow uses the GitLab Template. If Bridge CLI is selected in the Configure Options screen, the generated workflow will include scripts to download and execute Bridge CLI. The preview below reflects both configurations.

**Generated GitLab Template workflow**

```
# Quickstart: Black Duck Security Template with coverity:
#     https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-coverity.html
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml

variables:
  ### Push and Pull Request scan branches
  COVERITY_SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
  COVERITY_PR_TARGET_BRANCHES: "/^(main|master|develop|stage|release)$/"

coverity:
  stage: blackduck_security
  variables:
    ### SCANNING: Required fields
    BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
    BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
    BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
    ### Run analysis locally
    BRIDGE_COVERITY_LOCAL: "true"
    ### Configuration if Bridge diagnostic files needs to be uploaded
    INCLUDE_DIAGNOSTICS: "true"
    ### GitLab token
    BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
    ### Pull Request Comments
    BRIDGE_COVERITY_PRCOMMENT_ENABLED: "true"
  extends: .run-black-duck-tools
  rules:
    - if: (($CI_COMMIT_BRANCH =~ $COVERITY_SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event') ||
        ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $COVERITY_PR_TARGET_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event'))
  artifacts:
    when: always
    ### Required to upload Bridge diagnostics
    paths:
      - .bridge  # Upload bridge diagnostics to artifact
```

**Review** `coverity-ci.yml`  **screen for GitLab Template**

[image: Coverity Workflow Review Screen]

**Generated Bridge CLI workflow**

```
# Quickstart: Bridge CLI with coverity:
#     https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-coverity.html
variables:
  ### Push and Pull Request scan branches
  COVERITY_SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
  COVERITY_PR_TARGET_BRANCHES: "/^(main|master|develop|stage|release)$/"

coverity:
  stage: blackduck_security
  variables:
    ### Bridge CLI Download URL Base Path
    BRIDGECLI_URL_BASE_PATH: "https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest"
    ### Coverity Parameters
    BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
    BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
    BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
    BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $CI_PROJECT_NAME
    ### GitLab repository information
    BRIDGE_GITLAB_REPOSITORY_NAME: $CI_PROJECT_PATH
    BRIDGE_GITLAB_REPOSITORY_BRANCH_NAME: $CI_COMMIT_REF_NAME
    ### Run analysis locally
    BRIDGE_COVERITY_LOCAL: "true"
    ### GitLab token
    BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
  rules:
    - if: ($CI_COMMIT_REF_NAME =~ $COVERITY_SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
      variables:
        BRIDGE_COVERITY_CONNECT_STREAM_NAME: $CI_PROJECT_NAME-$CI_COMMIT_REF_NAME
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $COVERITY_PR_TARGET_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
      variables:
        BRIDGE_COVERITY_CONNECT_STREAM_NAME: $CI_PROJECT_NAME-$CI_MERGE_REQUEST_TARGET_BRANCH_NAME
        ### Pull Request Comments
        BRIDGE_COVERITY_PRCOMMENT_ENABLED: "true"
        BRIDGE_GITLAB_REPOSITORY_PULL_NUMBER: $CI_MERGE_REQUEST_IID
  before_script:
    - OS=$([[ "$(uname -s)" == "Darwin" ]] && ([[ $(uname -m) =~ arm ]] && echo macos_arm || echo macosx) || ([[ $(uname -m) =~ arm ]] && echo linux_arm || echo linux64))
    - ZIP_PATH="/tmp/bridge.zip"
    - curl -sSL -o "$ZIP_PATH" "$BRIDGECLI_URL_BASE_PATH/bridge-cli-bundle-$OS.zip"
    - command -v unzip >/dev/null 2>&1 || (apt-get update && apt-get install -y unzip)
    - unzip -qo "$ZIP_PATH" -d /tmp
    - BRIDGE_CLI_INSTALL_DIR="/tmp/bridge-cli-bundle-$OS/bridge-cli"
    - chmod +x "$BRIDGE_CLI_INSTALL_DIR"
    - rm -f "$ZIP_PATH"
  script:
    - $BRIDGE_CLI_INSTALL_DIR --stage connect --diagnostics  # Generate diagnostics
  artifacts:
    when: always
    ### Upload bridge diagnostics to artifact
    paths:
      - .bridge  # Upload bridge diagnostics to artifact
```

**Review**  `coverity-ci.yml`  **screen for Bridge CLI**

[image: Workflow Review Coverity Bridge CLI]

The following points can be observed:

- The workflow review screen displays a preview of the generated workflow with a default workflow filename of `coverity-ci.yml`.
- The generated workflow contains the triggers for push events and Pull Requests that target the branches: `main`, `master`, `develop`, `stage`, `release`.
- A job named `coverity` has been integrated into the workflow to run in the specified GitLab runner.
- The generated pipeline job performs a checkout of the repository source and then runs the Coverity Scan to execute a scan using the Black Duck Security Scan GitLab Template or Bridge CLI.
  - The bulk onboarding solution has automatically generated the parameters based on the scan options specified in the UI. Please refer to the Black Duck Security Scan Template documentation for an explanation of the available parameters.
  - Documentation and configuration comments are added at the top for clarity and future reference.
  - Prerequisite variables and tokens have been automatically integrated.

    Note: It is recommended that the provided GitLab user token specified as a parameter in the workflow file has the necessary permissions required to create and inject comments on Pull Requests.
- For Bridge CLI generated workflows, additional scripts are added to download and install Bridge CLI for the appropriate pipeline environment (Linux/MacOS/Windows).

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.
