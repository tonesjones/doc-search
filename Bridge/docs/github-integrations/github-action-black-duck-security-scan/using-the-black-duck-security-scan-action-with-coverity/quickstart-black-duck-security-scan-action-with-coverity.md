---
title: "Quickstart: Black Duck Security Scan Action with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-coverity.html"
content_id: "Ucb9PwMLEc03_l8gKEa5Yg"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:48.324388+00:00"
---

# Quickstart: Black Duck Security Scan Action with Coverity

This quickstart explains how to set up the Black Duck Security Scan Action to run a Coverity full scan and Pull Request scan for branches in a repository.

The full scan will be triggered by push and merge events on specified branches. Full scan issues will be uploaded to a Coverity Connect instance as a snapshot within a stream. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target specific branches. Pull Request review comments are only created for new issues created that are detected on the feature branch but not the target branch. After the scan completes, diagnostic logs and report will be exported as GitHub build artifacts.

## Prerequisites

- The following reading is recommended:
  - GitHub prerequisites
  - Pull Request Comments
  - Using Fail Pull Requests With Coverity
  - Using the Black Duck Security Scan Action with Coverity
  - Additional GitHub configuration
- Admin access to a GitHub repository.
- Coverity credentials.
- To enable the Black Duck Security Scan Action to add Pull Request Comments, a GitHub Personal Access Token is required.
- The following Black Duck Security Scan Action parameters are required to enable inject review comments into Pull Requests.

  Important: Pull Request comments will not be injected if these parameters and the required prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `coverity_prComment_enabled` | When `true`, this enables Pull Request comments. | `"true"` |
  | `github_token` | A GitHub Personal Access Token with workflow read and write permission. Required to inject review comments. | `${{ secrets.GITHUB_TOKEN }}` if using the built in [`GITHUB_TOKEN`](https://docs.github.com/en/actions/tutorials/use-github_token-in-workflows) or `${{ secrets.MY_PAT_TOKEN $}}` to reference a custom token. |

  Note: The Black Duck Security Scan Action integrates with Coverity via Bridge CLI. Additional scan configuration options not available through the action's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (GitHub > Project > Settings > Secrets and Variables > Actions):

  Important: For security reasons, it is advisable not to store credentials, tokens and secrets directly in the workflow. The recommended approach is to use secrets.

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Variable | Coverity Server URL | [https://coverity.blackduck.com](https://coverity.blackduck.com/) |
  | `COVERITY_USER` | Secret | Coverity Username | `REPLACE_WITH_YOUR_USERNAME` |
  | `COVERITY_PASSPHRASE` | Secret | Active Coverity Authentication Key | `REPLACE_WITH_YOUR_TOKEN` |
- Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

1. Create a new workflow in GitHub. Navigate to the project, then to **Actions > New Workflow > Setup a workflow yourself**.
2. Paste the example below into your workflow file.

   Note: For compiled languages, uncomment the build setup step (e.g., Setup Java JDK) and the `coverity_build_command` and `coverity_clean_command` parameters.

   ```
   name: coverity-action
   on:
     push:
       branches: [main, master, develop, stage, release]
     pull_request:
       branches: [main, master, develop, stage, release]
     workflow_dispatch:
   jobs:
     coverity:
       runs-on: ubuntu-latest
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
         - name: Coverity Scan
           uses: blackduck-inc/black-duck-security-scan@v2
           with:
             ### SCANNING: Required fields
             coverity_url: ${{ vars.COVERITY_URL }}
             coverity_user: ${{ secrets.COVERITY_USER }}
             coverity_passphrase: ${{ secrets.COVERITY_PASSPHRASE }}
             
             ### POLICY ENFORCEMENT: Break build on full scan when encounter outstanding issues
             coverity_policy_view: ${{ github.event_name != 'pull_request' && 'Outstanding Issues' || '' }}
             
             ### PULL REQUEST COMMENTS:
             coverity_prComment_enabled: true
             
             # Required when PR comments is enabled
             github_token: ${{ secrets.GITHUB_TOKEN }}
             
             ### Perform local analysis with full toolkit
             # coverity_local: true
             ## Use the parameter below to add comments for issues filtered 
             ## by impact. Default is High if unset
             ## NOTE: Issues matching coverity_policy_view are ignored if set
             # coverity_prComment_impacts: 'High'
             
             ### COVERITY: Build commands for compiled languages (uncomment and configure for compiled languages)
             # coverity_build_command: mvn -B -DskipTests package
             # coverity_clean_command: mvn -B clean
             
             ## OPTIONAL DIAGNOSTICS: Upload logs as build artifact if true
             include_diagnostics: false
   ```

   Important: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled, the `coverity_local` line in the example should be uncommented. This enables local analysis using the full Coverity client, overriding the default thin client behavior.

   The Black Duck Security Scan Action downloads and uses the Coverity CLI to scan the codebase of the branch that triggered the workflow. Branches are defined in the `on` block. Detected issues are uploaded to a Coverity stream within a Coverity Connect project named after the repository. If the project does not exist, it is created automatically.

   The Coverity stream is named `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   For full scans, the `coverity_policy_view` parameter will break the build if new or outstanding issues are detected as defined by the `Outstanding Issues` [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html). Consult [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) for further details.

   Each time code is committed to a Pull Request branch that targets one of the specified base branches, a comparison is performed between the scan of the Pull Request branch and the latest full scan of its parent branch. This allows new issues to be added as review comments. Coverity Fail Pull Requests are enabled by setting the `coverity_prComment_enabled` parameter to *true*. Use the `coverity_prComment_impacts` parameter to add comments filtered by impact, with a default of `high` if unset. The source code management token created in the prerequisites is required to inject Pull Request review comments.

   Set the `include_diagnostics` parameter to `true` to upload logs contained within the `.bridge` folder as GitHub artifacts.
3. Click Commit Changes.

   Once the changes have been saved, the workflow should be triggered to run on the branch (e.g., `main` or `develop`). You can then create a Pull Request to run one or more Coverity Pull Request scans.

   An example review comment added to a Pull Request after a Coverity Pull Request scan has run is shown below.

   [image: PR review comments injected by Coverity PR scan]

## Troubleshooting and support

If a workflow error is encountered similar to the example below, then the `coverity_local` parameter should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the workflow uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `coverity_local` parameter to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity Product Documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- [Coverity Tutorials](https://community.blackduck.com/s/article/coverity-tutorials)
- [Coverity Projects and Streams Tutorial](https://community.blackduck.com/s/article/Coverity-Tutorial-Projects-and-Streams)
- [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html)
- [Coverity Deployment Guide](https://community.blackduck.com/s/article/Coverity-Deployment-Guide)
- [Black Duck Security Scan Action Documentation](https://github.com/marketplace/actions/black-duck-security-scan)
- [Black Duck Security Scan Action Source](https://github.com/blackduck-inc/black-duck-security-scan)
- Bridge product overview
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
