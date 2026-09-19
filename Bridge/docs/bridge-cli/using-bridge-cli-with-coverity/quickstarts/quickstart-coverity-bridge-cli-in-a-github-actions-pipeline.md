---
title: "Quickstart: Coverity Bridge CLI in a GitHub Actions pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-coverity-bridge-cli-in-a-github-actions-pipeline.html"
content_id: "_FLikXu3acsHkkgdHXL7yg"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:20.784010+00:00"
---

# Quickstart: Coverity Bridge CLI in a GitHub Actions pipeline

As an alternative to the Black Duck Security Scan Action, the Bridge CLI can be downloaded and directly executed in a GitHub workflow. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Coverity parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Action (recommended) can be used for workflows instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Action and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitHub prerequisites
  - Pull Request comments
  - Using Fail Pull Requests With Coverity
  - List of mandatory and optional parameters For Coverity
  - Additional GitHub configuration
- A [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) or the default `GITHUB_TOKEN` is required to allow the pipeline to inject Pull Request review comments.
- For security reasons, it is advisable to use [GitHub Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) and [Variables](https://docs.github.com/en/actions/learn-github-actions/variables) to store credentials and access tokens.
- Add the following variables and secrets at the repository or organization level (Settings > Secrets and Variables > Actions)

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Variable | Coverity Connect Server URL | <https://coverity.example.com> |
  | `COVERITY_USER` | Secret | Coverity Connect Username | `REPLACE_WITH_YOUR_USERNAME` |
  | `COVERITY_PASSPHRASE` | Secret | Coverity Connect Password or Access Token | `REPLACE_WITH_YOUR_PASSWORD` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI Download URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- The following Bridge CLI parameters are required to inject Pull Request comments:

  | Parameter | Description | Value |
  | --- | --- | --- |
  | `coverity.prcomment.enabled` | Enable PR comments | `true` |
  | `github.repository.pull.number` | ID of PR with source code to scan | `${{ github.event.number }}` |

Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge With Compiled Languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a workflow that invokes Bridge CLI for full scans and Pull Request scans:

1. Create a new workflow in GitHub. Navigate to the project, then to **Actions > New Workflow > Setup a workflow yourself**.
2. Paste the example below into your workflow file.

   Note: For compiled languages, uncomment the build setup step (e.g., Setup Java JDK) and the `BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND` environment variables.

   ```
   name: coverity-bridge-cli
   on:
     push:
       branches: [ main, master, develop, stage, release ]
     pull_request:
       branches: [ main, master, develop, stage, release ]
     workflow_dispatch:
   jobs:
     coverity:
       runs-on: ubuntu-latest
       env:
         BRIDGE_COVERITY_CONNECT_URL: ${{ vars.COVERITY_URL }}
         BRIDGE_COVERITY_CONNECT_USER_NAME: ${{ secrets.COV_USER }}
         BRIDGE_COVERITY_CONNECT_USER_PASSWORD: ${{ secrets.COVERITY_PASSPHRASE }}
         ### COVERITY: Build commands for compiled languages (uncomment and configure for compiled languages)
         # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
         # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
         # BRIDGE_COVERITY_LOCAL: true
         BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         BRIDGE_GITHUB_REPOSITORY_OWNER_NAME: ${{ github.repository_owner }}
         BRIDGE_GITHUB_REPOSITORY_NAME: ${{ github.event.repository.name }}
         BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME: ${{ github.ref_name }}
       steps:
       - name: Checkout Source
         uses: actions/checkout@v4
       # For compiled languages, uncomment and configure the build setup step below:
       # - name: Setup Java JDK
       #   uses: actions/setup-java@v4
       #   with:
       #     java-version: 21
       #     distribution: temurin
       #     cache: maven
       - name: Coverity Full Scan
         if: ${{ github.event_name != 'pull_request' }}
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{ runner.temp }} bridge.zip && rm -f bridge.zip
           ${{ runner.temp }}/bridge-cli-bundle-linux64/bridge-cli --stage connect \
               coverity.connect.project.name=${{ github.event.repository.name }} \
               coverity.connect.stream.name=${{ github.event.repository.name }}-${{ github.ref_name }} \
               coverity.connect.policy.view='Outstanding Issues'
         ## Add the coverity.prcomment.impacts parameter to the bridge-cli command in the
         ## Coverity PR Scan step below to add review comments for issues filtered by impact.
         ## Default impact is High if unset
         ## NOTE: Issues matching coverity.connect.policy.view are ignored if set
         # coverity.prcomment.impacts='High' \
       - name: Coverity PR Scan
         if: ${{ github.event_name == 'pull_request' }}
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{ runner.temp }} bridge.zip && rm -f bridge.zip
           ${{ runner.temp }}/bridge-cli-bundle-linux64/bridge-cli --stage connect \
               coverity.connect.project.name=${{ github.event.repository.name }} \
               coverity.connect.stream.name=${{ github.event.repository.name }}-${{ github.base_ref }} \
               coverity.prcomment.enabled=true \
               github.repository.pull.number=${{ github.event.number }}
   #   - name: Save Logs
   #     if: always()
   #     uses: actions/upload-artifact@v4
   #     with:
   #       name: bridge-logs
   #       path: ${{ github.workspace }}/.bridge
   #       include-hidden-files: true
   ```

   Note: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed with the full toolkit. This will override the default behaviour that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans and Pull Request scans.

   A full scan is performed when code is pushed or merged to the `main`, `master`, `develop`, `stage` or `release` branches. The `coverity.connect.policy.view` parameter is configured to break the build if new or outstanding issues are detected as defined by the Outstanding Issues [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html) (see [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) for details).

   For Pull Requests targeting those branches, Bridge CLI is invoked directly to perform a Pull Request scan. New issues detected on the feature branch are added as Pull Request comments. The `coverity.prcomment.impacts` parameter can be used to filter comments by impact level, with a default of "high" if unset.

   For both scan scenarios the Coverity project and stream are automatically derived from built-in GitHub Actions environment variables. The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   Uncomment the `Save Logs` step to upload logs contained within the `.bridge` folder as a GitHub artifact.
3. Run scans

   Once the workflow is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: PR review comments injected by Coverity PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `BRIDGE_COVERITY_LOCAL` environment variable to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity product documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
