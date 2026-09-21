---
title: "Using Black Duck Security Bulk Onboarding with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-bulk-onboarding-with-polaris.html"
content_id: "Iw324xH3zW4TMJQZBckrtw"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:03.462171+00:00"
---

# Using Black Duck Security Bulk Onboarding with Polaris

This guide explains the variables and token required by Black Duck Security Bulk Onboarding for generating a Polaris scan workflow. Furthermore, an overview of the scan and post scan configuration options are explained.

When an existing `polaris-ci.yml` is detected for a project selected for onboarding, Black Duck Security Bulk Onboarding overrides the content of the existing file.

## Configuring required variables, secrets and token

The table below outlines the variables, and GitLab user token required for generating a workflow for a Polaris scan. Secrets and variables should be configured in the groups and/or projects where the GitLab workflow file will be deployed

Note: A GitLab Personal Access Token is required as a parameter in the workflow file for injecting Merge Request comments in addition to creating fix Merge Requests.

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `BRIDGE_POLARIS_SERVERURL` | Polaris server URL | `https://polaris.example.com` |
| Secret | `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token. You can use either a user access token (created in the Polaris UI) or a service account token here. | `$POLARIS_ACCESSTOKEN` |
| Token | `BRIDGE_GITLAB_USER_TOKEN` | Required for Merge Request comments and Fix Merge Requests.  For detailed instructions on configuring token permissions, please refer to the user guide. | `$GITLAB_USER_TOKEN` |

Note: Ensure all required variables and token are configured before proceeding to generate the scan workflow for review and deployment.

## Configuring a Polaris scan

The `Configure options` screen illustrated below provides an intuitive interface for configuring branches, runner, platform, scan and post-scan options. These are used to generate a GitLab workflow for performing a Polaris scan.

Note: Ensure all required GitLab variables are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

[image: Polaris Scan Configure Options screens]

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

- **Assessment type**: Black Duck Security Bulk Onboarding for Polaris supports two scan types: `SAST` and/or `SCA`. When using Polaris source upload, the following upload modes are supported:
  - **SAST** : hybrid (default), local or remote
  - **SCA**: hybrid (default) or remote
- **Advanced options**:
  - **Capture diagnostics information**: When checked, diagnostics will be captured and uploaded as a GitLab artifact.
  - **Wait for scan to complete**: When checked this will block post scan operations until the scan completes, e.g. injecting Pull Request comments and creating a SARIF file.
  - **Fail build if policy violations are found**: If this option is checked, then if there are policy violations the build will break.

**Post scan options**

The following post scan options can be configured and require a GitLab User Token to be created as outlined in the prerequisites.

- **Decorate pull requests with comments**: When checked, then each new policy violation introduced within a Pull Request will be summarized within a review comment.
- **Automatically create fix pull requests:** When checked, SCA package assessments will automatically open Fix Pull Requests for a default maximum count of 5 dependency upgrades and vulnerabilities.This uses `$GITLAB_USER_TOKEN` secret by default for authentication.
- **Create SARIF file**: When checked, a SARIF file will be created. An additional checkbox will be displayed to provide the option to upload and display issues in GitLab security dashboard.
- **Create and upload GitLab Security Report**: When checked, a GitLab Security Report will be created and uploaded into GitLab Security.

  Note: A Gitlab Ultimate license is required in order to create SAST and SCA (dependency scanning) reports on GitLab.

  [image: image]

**Workflow options**

It can be seen from the screenshot above that a workflow can be generated with the following workflow options:

- **Add additional options as comments in the generated workflow file**: Selected configuration options and scan parameters are documented as inline comments within the generated YAML file for reference.
- **Run the scan using:**
  - `GitLab Template (recommended)`: Generate a scan workflow that uses Black Duck Security Scan Template.
  - `CLI - Black Duck Bridge CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

## Reviewing A Polaris workflow

This section will explain an overview of reviewing a workflow, assuming the following Polaris scan configuration options:

- **Branches:** `main`, `master`, `develop`, `stage`, `release`
- **Runner configuration**: `runner tag names` (Use tags for either Mac/Linux or Windows)
- **Platform**: Polaris
- **Assessment types**: `SAST`, `SCA`
- **Advanced options**:
  - Capture diagnostics information
  - Wait for scan to complete and fail build if policy violations found
- **Post scan options**
  - Decorate Pull Request with comments
  - Automatically create fix pull requests
  - Create SARIF file with upload in GitLab
  - Create and upload GitLab Security Report
- **Workflow options**:
  - Run the scan using:
    - **GitLab Template (recommended)**
    - **CLI - Black Duck Bridge CLI**

Note: By default, the workflow uses the GitLab Template. If Bridge CLI is selected in the Configure Options screen, the generated workflow will include scripts to download and execute Bridge CLI. The preview below reflects both configurations.

The Polaris generated workflow and corresponding `review polaris-ci.yml` screen is displayed below.

**Generated GitLab Template workflow**

```
# Quickstart: Black Duck Security Template with polaris:
# https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-polaris.html    
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml

variables:
  ### Push and Pull Request scan branches
  POLARIS_SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
  POLARIS_PR_TARGET_BRANCHES: "/^(main|master|develop|stage|release)$/"

polaris:
  stage: blackduck_security
  variables:
    ### SCANNING: Required fields
    BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
    BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
    BRIDGE_POLARIS_ASSESSMENT_TYPES: "SAST,SCA"
    BRIDGE_POLARIS_TEST_SAST_LOCATION: hybrid
    BRIDGE_POLARIS_TEST_SCA_LOCATION: hybrid
    ### Configuration if Bridge diagnostic files needs to be uploaded
    INCLUDE_DIAGNOSTICS: "true"
    ### GITLAB token
    BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
    ### PR Comment parameter
    BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"
    ### Fix Pull Request Creation
    BRIDGE_POLARIS_FIXPR_ENABLED: "true"
    ### SARIF Report Generation
    BRIDGE_POLARIS_REPORTS_SARIF_CREATE: "true"
    ### GitLab Security Report parameter
    BRIDGE_POLARIS_REPORTS_GITLAB_CREATE: "true"
  extends: .run-black-duck-tools
  rules:
    - if: (($CI_COMMIT_BRANCH =~ $POLARIS_SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event') ||
        ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $POLARIS_PR_TARGET_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event'))
  ### Required to upload SARIF report or Security Report
  artifacts:
    when: always
    ### Required to upload GitLab Security Report
    reports:
      sast: $CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sast.json  # Required when Polaris assessment type is SAST
      dependency_scanning: $CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sca.json  # Required when Polaris assessment type is SCA
    ### Upload bridge diagnostics to artifact
    paths:
      - .bridge  # Upload bridge diagnostics to artifact
      - .blackduck/integrations/polaris/sarif/report.sarif.json  # Upload SARIF Report to artifact
  tags: ["macos"]
```

**Review** `polaris-ci.yml` **screen** **for GitLab Template**

[image: image]

**Generated Bridge CLI workflow**

```
# Quickstart: Bridge CLI with polaris:
# https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-polaris.html    
variables:
  ### Push and Pull Request scan branches
  POLARIS_SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
  POLARIS_PR_TARGET_BRANCHES: "/^(main|master|develop|stage|release)$/"

polaris:
  stage: blackduck_security
  variables:
    ### Bridge CLI Download URL Base Path
    BRIDGECLI_URL_BASE_PATH: "https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest"
    ### Polaris Parameters
    BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
    BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
    BRIDGE_POLARIS_ASSESSMENT_TYPES: "SAST,SCA"
    BRIDGE_POLARIS_APPLICATION_NAME: $CI_PROJECT_NAME
    BRIDGE_POLARIS_PROJECT_NAME: $CI_PROJECT_NAME
    BRIDGE_POLARIS_BRANCH_NAME: $CI_COMMIT_REF_NAME
    ### GitLab repository information
    BRIDGE_GITLAB_REPOSITORY_NAME: $CI_PROJECT_PATH
    BRIDGE_GITLAB_REPOSITORY_BRANCH_NAME: $CI_COMMIT_REF_NAME
    BRIDGE_POLARIS_TEST_SAST_LOCATION: hybrid
    BRIDGE_POLARIS_TEST_SCA_LOCATION: hybrid
    ### GitLab token
    BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
  rules:
    - if: ($CI_COMMIT_REF_NAME =~ $POLARIS_SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
      variables:
        ### Fix Pull Request Creation
        BRIDGE_POLARIS_FIXPR_ENABLED: "true"
        ### SARIF Report Generation
        BRIDGE_POLARIS_REPORTS_SARIF_CREATE: "true"
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $POLARIS_PR_TARGET_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
      variables:
        ### Pull Request Comments
        BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"
        BRIDGE_GITLAB_REPOSITORY_PULL_NUMBER: $CI_MERGE_REQUEST_IID
        BRIDGE_POLARIS_BRANCH_PARENT_NAME: $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
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
    - $BRIDGE_CLI_INSTALL_DIR --stage polaris --diagnostics  # Generate diagnostics
  ### Required to upload SARIF report or Security Report
  artifacts:
    when: always
    ### Upload bridge diagnostics to artifact
    paths:
      - .bridge  # Upload bridge diagnostics to artifact
      - .blackduck/integrations/polaris/sarif/report.sarif.json  # Upload SARIF Report to artifact
  tags: ["macos"]
```

**Review**  `polaris-ci.yml`  **screen for Bridge CLI**

[image: image]

The following points can be observed:

- The workflow review screen displays a preview of the generated workflow with a default workflow filename of `polaris-ci.yml`.
- The generated workflow contains the triggers for push events and Pull Requests that target the branches: `main`, `master`, `develop`, `stage`, `release`.
- A job named `polaris` has been integrated into the workflow to run in the specified GitLab cloud runner.
- The generated Polaris job performs a checkout of the repository source and then runs the Polaris Scan to execute a scan using the Black Duck Security Scan GitLab Template or Bridge CLI.
  - The bulk onboarding solution has automatically generated the parameters based on the scan options specified in the UI. Please refer to the Black Duck Security Scan Template documentation for an explanation of the available parameters.
  - Documentation and configuration comments are added at the top for clarity and future reference.
  - Prerequisite variables and tokens have been automatically integrated.

    Note: It is recommended that the provided GitLab user token specified as a parameter in the workflow file has the necessary permissions required to create and inject comments on Pull Requests.
- For Bridge CLI generated workflows, additional scripts are added to download and install Bridge CLI for the appropriate pipeline environment (Linux/MacOS/Windows).

To review the generated workflow:

1. Use the **Edit** button, if required to make changes and then click **Save**.
2. Click the **Next** button to confirm that the workflow has been reviewed and any necessary amendments have been made.
