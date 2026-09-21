---
title: "Quickstart: Black Duck Security Scan Action with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-polaris.html"
content_id: "9c381pgzV7V4ZZmI1ALLvQ"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:44.994920+00:00"
---

# Quickstart: Black Duck Security Scan Action with Polaris

Explains how to set up a Black Duck Security Scan Action for a Polaris project that will run a full scan and Pull Request scan. Pull request review comments are created only for new issues detected in the feature branch but not in the target branch.

The full scan will be triggered by push and merge events on specified branches. GitHub issues will be created from scan findings. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments on the Pull Request. For full scans Fix Pull Requests will be created to upgrade dependencies. After the scan completes, appropriate security reports and diagnostic logs will be exported as GitHub artifacts.

To find out more about the Black Duck Security Scan Action and what it can do, take a look at the overview page.

Note: The Bridge CLI can be used directly inside workflows. For further details, view the quickstart guide here: Quickstart: Polaris Bridge CLI in a GitHub workflow

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - GitHub prerequisites
  - Polaris Prerequisites
  - External issues
  - Pull Request Comments
  - Fix pull requests (Fix PRs)
  - Using the Black Duck Security Scan Action with Polaris
  - Additional GitHub configuration
  - This micro-course: [Polaris: Using the Black Duck Security Scan Action](https://blackduck.skilljar.com/polaris-using-the-synopsys-github-action)
- A GitHub Token is required for injecting Pull Request comments, raising Fix Pull Requests and creating GitHub issues from scan findings. See [Polaris: Using the Black Duck Security Scan Action](https://blackduck.skilljar.com/polaris-using-the-synopsys-github-action) if need instructions.

  Important: Confirm that the token has workflow read and write permissions. In GitHub, navigate to Project > Settings > Actions > General > Workflow Permissions.
- For security reasons, it is advisable not to store credentials directly in the workflow. The recommended approach is to use variables.
- The following Black Duck Security Scan Action parameters are required to enable injecting review comments into Pull Requests, raise Fix Pull Requests and create GitHub Issues. These parameters have been included in the quickstart example:

  Important: Pull Request comments will not be injected, Fix Pull Requests will not be raised and issues will not be created from scan findings if these parameters and the required prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `polaris_prComment_enabled` | When `true`, this enables PR comments. | `true` |
  | `polaris_fixpr_enabled` | When `true`, this raises Fix PRs. | `true` |
  | `polaris_externalIssues_create` | When `true`, this enables creation of GitHub issues from scan findings. | `true` |
  | `github_token` | A GitHub Personal Access Token with workflow read and write permissions. Required to inject review comments. | `${{ secrets.GITHUB_TOKEN }}` if using the built in [`GITHUB_TOKEN`](https://docs.github.com/en/actions/tutorials/use-github_token-in-workflows) or `${{ secrets.MY_PAT_TOKEN }}` to reference a custom token. |

  Note: Black Duck Security Scan Action integrates with Polaris via Bridge CLI. Additional scan configuration options not available through the action's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.

  Note: The `polaris_application` and `polaris_project_name` both default to the repository name. Furthermore, `polaris_branch_name` and `polaris_branch_parent_name` use the default values of `github.branch.name` and `github.branch.parent.name` respectively.
- Add the following secrets and variables (GitHub > Project > Settings > Secrets and Variables > Actions):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `POLARIS_SERVER_URL` | Variable | Polaris Server URL | `https://polaris.blackduck.com` |
  | `POLARIS_ACCESS_TOKEN` | Secret | Polaris access token. You can use either a user access token (created in the Polaris UI) or a service account token here. | `REPLACE_WITH_YOUR_TOKEN` |
- Polaris uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to integrate Polaris with the GitHub workflow for SAST and SCA scans:

1. Create a new workflow in GitHub. Navigate to the project, then to Actions > New Workflow > Setup a workflow yourself.
2. Paste the example workflow below into your workflow file.

   Note: For compiled languages, uncomment the build setup step (e.g., Setup Java JDK) and the `coverity_build_command` and `coverity_clean_command` parameters.

   ```
   name: CI-Polaris-Basic
   on:
     push:
       branches: [main, master, develop, stage, release]
     pull_request:
       branches: [main, master, develop, stage, release]
     workflow_dispatch:
      
   jobs:
     build:
       runs-on: [ubuntu-latest]
       steps:
       - name: Checkout Source
         uses: actions/checkout@v5
       # For compiled languages, uncomment and configure the build setup step below:
       # - name: Setup Java JDK
       #   uses: actions/setup-java@v4
       #   with:
       #     java-version: 21
       #     distribution: temurin
       #     cache: maven
       - name: Polaris Scan
         uses: blackduck-inc/black-duck-security-scan@v2
         with:
           ### SCANNING: Required fields
           polaris_server_url: ${{ vars.POLARIS_SERVER_URL }}
           polaris_access_token: ${{ secrets.POLARIS_ACCESS_TOKEN }}
           polaris_assessment_types: "SCA,SAST"
           
           ### SCANNING OPTIONAL
           polaris_application_name: quickstart-${{ github.event.repository.name }}
           
           ### SCANNING OPTIONAL: Pull Request comments
           polaris_prComment_enabled: true
           
           ### SCANNING OPTIONAL: GitHub Issues
           polaris_externalIssues_create: true

           ### SCANNING OPTIONAL: Fix Pull Requests
           polaris_fixpr_enabled: true

           ### GITHUB Token
           # Required when Pull Request comments, Fix Pull Requests or GitHub issues are enabled
           github_token: ${{ secrets.GITHUB_TOKEN }}

           ### ENABLE OPTIONAL SCAN REPORTS
           polaris_reports_sarif_create: true
           polaris_upload_sarif_report: true
           
           ### COVERITY BUILD COMMANDS (uncomment and configure for compiled languages)
           # coverity_build_command: mvn -B -DskipTests package
           # coverity_clean_command: mvn -B clean
           
           ### OPTIONAL DIAGNOSTICS: Upload logs as build artifact if true
           include_diagnostics: false
   ```

   In the example above the `CI-Polaris-Basic` workflow job runs on events defined in the workflow’s `on:` section. The Black Duck Security Scan Action automatically selects the scan type: a full scan for branch push events, or a Pull Request scan for pushes to Pull Requests targeting those branches.

   The workflow integrates with a Polaris server instance via the `polaris_server_url` and `polaris_access_token` parameters. A scan will run for a Polaris application named after the GitHub repository with prefix `quickstart-`. Within this application, a project will be created by Black Duck Security Scan Action, if it doesn’t already exist, to store the scan results. The branch in Polaris is automatically derived from the branch that triggered the scan.

   The behavior of the scans is as follows:

   - **Full scan**: A full scan is performed on key branches like `main` and `develop` to establish a reference point for the code's security and quality. These scans analyze the entire codebase to identify existing issues and set a standard for future changes. Regularly scanning these branches ensures that the codebase is secure and consistent. In this scenario the [Black Duck Security Scan Action](https://plugins.jenkins.io/blackduck-security-scan/) will exhibit the following behavior:
     - SAST and SCA assessments will be performed. To enable DAST assessment, set the `polaris_assessment_types` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - Polaris external issues are enabled to create GitHub issues from scan findings. By default, issues are created for `Critical` and `High` severities, SCA issues are grouped by component–version and the maximum number of issues created per assessment at any given time is `10`. Configuration parameters for Polaris GitHub external issues are documented in Complete List Of Bridge Commands and Create external issues from Polaris scans. Please refer to External issues to learn more about the information that Bridge reports for issues created from scan findings for SAST and SCA assessments.
     - Fix Pull Requests are enabled to raise Pull Requests to upgrade dependencies for full scans of branches. See Fix pull requests (Fix PRs) and Using the Black Duck Security Scan Action with Polaris for further information and examples that demonstrate how to:
       - Configure order of preference for upgrade guidance
       - Raise Fix Pull Requests by severity
       - Enforce a maximum limit for the number of Fix Pull Requests created.
     - SARIF reporting is enabled. This will export the SARIF report as a GitHub artifact. The SARIF report can also be uploaded to GitHub Advanced Security via the `polaris_upload_sarif_report` parameter. This feature is only available for GitHub repositories that satisfy the following [conditions](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
   - **Pull Request scan**: A Pull Request scan ensures that only secure, high-quality code is merged, while keeping feedback targeted and relevant to the changes made. The scan compares the proposed changes against the baseline established by a full scan on key branches like `main` or `develop`. Instead of analyzing the entire codebase, it focuses on identifying new issues introduced, which can be configured to surface directly as comments on the Pull Request (`polaris_prComment_enabled: true`) via the use of a GitHub token configured in the `github_token` parameter.

   Set the `include_diagnostics` parameter to `true` to upload logs and reports contained within the `.bridge` folder as GitHub artifacts.
3. Save the workflow file.

   Once the changes have been saved the workflow should be triggered to run on the branch, e.g. `main` or `develop`. Subsequently, it is then possible to create a Pull Request to run one or more Polaris Pull Request scans.

   An example review comment added to a Pull Request after a Polaris Pull Request scan has run is shown below.

   [image: PR review comments injected by Polaris PR scan]

## Troubleshooting and support

If a workflow error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Important: Request Validation Failed: No concurrent entitlements found for the tenant

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the workflow, consult [create an application in](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) Polaris.

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- [Black Duck Security Scan Action Documentation](https://github.com/marketplace/actions/black-duck-security-scan)
- [Black Duck Security Scan Action Source](https://github.com/blackduck-inc/black-duck-security-scan)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
