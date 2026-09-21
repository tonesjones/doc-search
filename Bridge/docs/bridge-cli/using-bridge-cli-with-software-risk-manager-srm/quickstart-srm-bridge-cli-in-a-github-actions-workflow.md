---
title: "Quickstart: SRM Bridge CLI in a GitHub Actions workflow"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-srm-bridge-cli-in-a-github-actions-workflow.html"
content_id: "GSs5IaWi52PrO8rDKtvw4Q"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:26.667031+00:00"
---

# Quickstart: SRM Bridge CLI in a GitHub Actions workflow

As an alternative to the Black Duck Security Scan Action, the Bridge CLI can be downloaded and directly executed in a GitHub workflow. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use Bridge CLI directly from a pipeline, the correct Bridge CLI Software Risk Manager parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult Using Bridge CLI with Software Risk Manager (SRM) for further details and instructions on use.

Note: The Black Duck Security Scan Action (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide: Quickstart: Black Duck Security Scan Action with SRM. The Black Duck Security Scan Action has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Action and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - GitHub prerequisites
  - List of mandatory and optional parameters for SRM
  - Additional GitHub configuration
- For security reasons, it is advisable to use [GitHub Actions secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) or repository variables to store credentials and access tokens.
- Add the following secrets and variables in your repository settings:

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `SRM_URL` | Repository Variable | SRM server URL | `https://srm.example.com` |
  | `SRM_APIKEY` | Secret | SRM API key | `REPLACE_WITH_YOUR_APIKEY` |
  | `BRIDGECLI_LINUX64` | Repository Variable | Bridge CLI download URL for Linux | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |

Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge with compiled languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a GitHub Actions workflow that invokes Bridge CLI for SRM scans:

1. Create a new workflow in GitHub. Navigate to the project. Click **Actions**, then **New Workflow**, then **Setup a workflow yourself**.
2. Paste the example workflow below

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - `Setup JDK` step
   - Build/clean command environment variables (`BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND`).

   ```
   ## -----------------------------------------------------------------------------
   # NOTE: The commented lines below are for compiled languages (e.g., Java, C++).
   # If your project requires a build step, uncomment and adjust those lines.
   ## -----------------------------------------------------------------------------
   name: srm-bridge-cli
   on:
     push:
       branches: [ main, master, develop, stage, release ]
     workflow_dispatch:
   jobs:
     srm:
       runs-on: ubuntu-latest
       env:
         BRIDGE_SRM_URL: ${{ vars.SRM_URL }}
         BRIDGE_SRM_APIKEY: ${{ secrets.SRM_APIKEY }}
         BRIDGE_SRM_ASSESSMENT_TYPES: SAST,SCA
         BRIDGE_SRM_PROJECT_NAME: ${{ github.event.repository.name }}
         BRIDGE_SRM_BRANCH_NAME: ${{ github.ref_name }}
         BRIDGE_SRM_BRANCH_PARENT: ${{ github.ref_name != github.event.repository.default_branch && github.event.repository.default_branch || '' }}
         # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
         # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
       steps:
       - name: Checkout Source
         uses: actions/checkout@v4
       # - name: Setup Java JDK
       #   uses: actions/setup-java@v4
       #   with:
       #     java-version: 21
       #     distribution: temurin
       #     cache: maven
       - name: SRM Full Scan
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{ runner.temp }} bridge.zip && rm -f bridge.zip
           ${{ runner.temp }}/bridge-cli-bundle-linux64/bridge-cli --stage srm
     # - name: Save Logs
     #   if: always()
     #   uses: actions/upload-artifact@v4
     #   with:
     #     name: bridge-logs
     #     path: ${{ github.workspace }}/.bridge
     #     include-hidden-files: true
   ```

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans.

   The GitHub workflow will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_URL` parameter, using a given API key, `BRIDGE_SRM_APIKEY`. By default a Software Risk Manager project is created before the full scan runs, with a name matching the name of the source repository.

   If a full scan is triggered for a branch that is not the default branch, then the pipeline sets the parent branch (`BRIDGE_SRM_BRANCH_PARENT`) to the default branch. This helps ensure that non-default branches reference the default branch as their base during scanning operations.

   A full scan, including SAST and SCA assessments, is triggered by push events for any of the branches defined in the `on.push.branches` list.

   Uncomment the `Save Logs` section to upload logs and reports from the `.bridge` folder as GitHub artifacts.
3. Run scans

   Once the workflow is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Test:** Monitor the output to verify that the SRM scan completes successfully and issues appear in SRM Dashboard.

## Troubleshooting and support

If errors are encountered during the pipeline run, ensure that all variables are set correctly and that the Bridge CLI can access the SRM server.

If a pipeline error is encountered similar to the example below, then it is likely that the `BRIDGE_SRM_BRANCH_PARENT` parameter has not been set.

Important: ERROR: Branch "develop" does not exist for the project and "srm.branch.parent" is empty but is required along with "srm.branch.name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, `stage` or `release`, the `BRIDGE_SRM_BRANCH_PARENT` parameter must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

For further troubleshooting, enable the optional log archiving by uncommenting the `Save Logs` step in the workflow file.

## Useful resources

- [SRM product documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
