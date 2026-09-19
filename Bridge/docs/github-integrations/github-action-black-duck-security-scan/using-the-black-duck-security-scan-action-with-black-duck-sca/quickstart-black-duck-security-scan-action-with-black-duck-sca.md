---
title: "Quickstart: Black Duck Security Scan Action with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-black-duck-sca.html"
content_id: "700kuerTqlyFnaByt1Bx3Q"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:46.656266+00:00"
---

# Quickstart: Black Duck Security Scan Action with Black Duck SCA

Explains how to set up the Black Duck Security Scan Action to run a workflow that integrates with Black Duck® SCA to run a full scan and Pull Request scan. Pull request review comments are created only for new issues detected in the feature branch but not in the target branch.

The full scan will be triggered by push and merge events on specified branches. GitHub issues will be created from scan findings. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments on the Pull Request. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitHub prerequisites
  - External issues
  - Pull Request Comments
  - Fix Pull Requests
  - Using the Black Duck Security Scan Action With Black Duck® SCA
  - Additional GitHub configuration
- Admin access to a GitHub repository.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with read and write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A GitHub token is required to allow the Black Duck Security Scan Action to inject Pull Request comments and create GitHub issues from scan findings.
- For security reasons, it is advisable not to store credentials directly in the workflow. The recommended approach is to use secrets.
- The following environment variables must be defined in the `env:` section of your GitHub Actions workflow to enable Pull Request scanning and automated review comment injection.

  Important: If these variables and the prerequisites are not properly configured, the workflow will not inject comments into Pull Requests.

  | Environment Variable | Description | Example |
  | --- | --- | --- |
  | `DETECT_PROJECT_NAME` | Black Duck® SCA project name. | `${{ github.event.repository.name }}` |
  | `DETECT_PROJECT_VERSION_NAME` | Set to target branch of Pull Request to allow differential comparison. | `${{ github.event_name != 'pull_request' && github.ref_name || github.event.pull_request.base.ref }}` |
- The following parameters have been included in the quickstart example and are required to inject review comments and create GitHub issues:

  Important: If these parameters and the prerequisites are not configured, the workflow will not inject comments into Pull Requests and GitHub Issues will not be created.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `blackducksca_prcomment_enabled` | When `true`, enables PR comments. | `true` |
  | `blackducksca_externalIssues_create` | When `true`, this enables creation of GitHub issues from scan findings. | `true` |
  | `github_token` | A GitHub Personal Access Token with workflow read and write permissions. Required to inject review comments. | `${{ secrets.GITHUB_TOKEN }}` if using the built in [`GITHUB_TOKEN`](https://docs.github.com/en/actions/tutorials/use-github_token-in-workflows) or `${{ secrets.MY_PAT_TOKEN }}` to reference a custom token. |

  Note: Black Duck Security Scan Action integrates with Black Duck® SCA via Bridge CLI. Additional scan configuration options not available through the action's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (GitHub > Project > Settings > Secrets and Variables > Actions):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BLACKDUCK_URL` | Variable | Black Duck® SCA Server URL | `https://sca.blackduck.com` |
  | `BLACKDUCK_TOKEN` | Secret | Black Duck® SCA Access Token | `REPLACE_WITH_YOUR_TOKEN` |

## Instructions

Follow the steps below to configure the Black Duck Security Scan Action to run a full scan and Pull Request scan.

1. Create a new workflow in GitHub. Navigate to the project. Click Actions, then New Workflow, then Setup a workflow yourself.
2. Paste the example workflow below and please remember to change the applicable variable values as required, such as: names of branches, project name etc.

   ```
   name: CI-BlackDuck-SCA-Basic
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
       - name: Black Duck SCA Scan
         id: black-duck-sca-scan
         uses: blackduck-inc/black-duck-security-scan@v2
         
         ## DETECT Environment Variables
         env:
           DETECT_PROJECT_NAME: ${{ github.event.repository.name }}
           DETECT_PROJECT_VERSION_NAME: ${{ github.event_name != 'pull_request' && github.ref_name || github.event.pull_request.base.ref }}

         with:
           ### SCANNING: Required fields
           blackducksca_url: ${{ vars.BLACKDUCK_URL }}
           blackducksca_token: ${{ secrets.BLACKDUCK_TOKEN }}
           
           ### SCANNING: Optional fields
           # blackducksca_scan_failure_severities: 'BLOCKER,CRITICAL'

           ### PULL REQUEST COMMENTS
           blackducksca_prcomment_enabled: true
           
           ### FIX PULL REQUEST CREATION
           blackducksca_fixpr_enabled: true
           
           ### GitHub ISSUES CREATION
           blackducksca_externalIssues_create: true

           # Required when PR comments, Fix PR, Sarif Upload or GitHub Issues creation is enabled
           github_token: ${{ secrets.GITHUB_TOKEN }}

           ### SARIF report generation
           blackducksca_reports_sarif_create: true
           blackducksca_upload_sarif_report: true

           ## OPTIONAL DIAGNOSTICS: Upload logs as build artifact if true
           include_diagnostics: false
   ```

   In the example above the `CI-BlackDuck-SCA-Basic` workflow job runs on events defined in the workflow’s `on:` section. The Black Duck Security Scan Action automatically selects the scan type: a full scan for branch push events, or a Pull Request scan for pushes to Pull Requests targeting those branches. A list of configuration parameters for the Black Duck Security Scan Action is available here.

   The workflow integrates with a Black Duck® SCA server instance via the `blackducksca_url` and `blackducksca_token` parameters. A scan will run for a Black Duck® SCA project named after the GitHub repository name. This is configured by the `DETECT_PROJECT_NAME` environment variable. Within this project, the project version is derived from the `DETECT_PROJECT_VERSION_NAME` environment variable. For full scans the version is the name of the branch that had commits pushed. For Pull Request scans the version is set to the name of the target branch of the Pull Request.

   The behavior of the scans is as follows:
   - **Full scan**: Triggered by push events to any of the branches defined in the `on: push: branches:` section. In this scenario the following actions will be performed:
     - An SCA assessment and signature scan will be run.
     - Issues that are of `BLOCKER` or `CRITICAL` severity will break the build by default.
     - A SARIF report will be generated and exported only for full scans. The `blackducksca_upload_sarif_report` parameter uploads the SARIF report to GitHub Advanced Security. This feature is only available for GitHub repositories that satisfy the following [conditions](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
     - Fix PRs will be automatically raised to fix vulnerable direct dependencies.
     - Black Duck external issues are enabled to create GitHub issues from scan findings. By default, issues are created for `Critical` and `High` severities, SCA issues are grouped by component–version and the maximum number of issues created per assessment at any given time is `10`. Configuration parameters for Black Duck GitHub external issues are documented in Complete List Of Bridge Commands and Create external issues from Black Duck SCA scans. Please refer to External issues to learn more about the information that Bridge reports for issues created from scan findings for SAST and SCA assessments.
   - **Pull Request scan**: A Pull Request scan ensures that only secure, high-quality code is merged, while keeping feedback targeted and relevant to the changes made. The scan compares the proposed changes against the baseline established by a full scan on key branches like `main` or `develop`. Instead of analyzing the entire codebase, it focuses on identifying new issues introduced, which can be configured to surface directly as comments on the Pull Request (`blackducksca_prcomment_enabled: true`). A GitHub Personal Access Token should be configured in the `github_token` parameter to enable the workflow to add Pull Request comments.

   Set the `include_diagnostics` parameter to `true` to upload logs contained within the `.bridge` folder as GitHub artifacts.
3. Click Commit Changes

   Once the changes have been saved the workflow should be triggered to run on the branch, e.g. `main` or `develop`. Subsequently, it is then possible to create a Pull Request to run one or more Pull Request scans.

   An example review comment added to a Pull Request after a Pull Request scan has run is shown below.

   [image: PR review comments injected by SCA PR scan]

## Next steps

Bridge initiates a Black Duck Detect scan that targets a repository. Detect properties can be passed using the `detect_args` parameter to further configure the scan. The code below is an example of further configuration; however, it is not necessary to include in this scan.

```
detect_args: --detect.project.name=your_project_name, --detect.project.version.name=v1.7
```

A complete list of Bridge variables for Black Duck® SCA is available at Bridge SCA Variables.

## Useful resources

- [Black Duck Security Scan Action Documentation](https://github.com/marketplace/actions/black-duck-security-scan)
- [Black Duck Security Scan Action Source](https://github.com/blackduck-inc/black-duck-security-scan)
- [Black Duck SCA Portal](https://docs.blackduck.com/p/blackducksca)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
