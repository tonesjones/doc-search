---
title: "Quickstart: Coverity Bridge CLI in a Bitbucket pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-coverity-bridge-cli-in-a-bitbucket-pipeline.html"
content_id: "NxPOiPDW3AkW1floKQxlyw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:19.840545+00:00"
---

# Quickstart: Coverity Bridge CLI in a Bitbucket pipeline

As an alternative to the Black Duck Security Scan Pipe, the Bridge CLI can be downloaded and directly executed in a Bitbucket pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Coverity parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Pipe (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Pipe and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Pipe
  - Pull Request comments
  - Using Fail Pull Requests With Coverity
  - List of mandatory and optional parameters for Coverity
  - Additional Bitbucket configuration
- A Bitbucket Access Token is required to allow the pipeline to inject Pull Request review comments.
- For security reasons, it is advisable to use [Bitbucket variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) with the `secured` option checked to store credentials and access tokens.
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables or Workspace Settings > Workspace Variables > Add Variables>

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_COVERITY_CONNECT_URL` | Variable | Coverity Connect Server URL | `https://cov.example.com` |
  | `BRIDGE_COVERITY_CONNECT_USER_NAME` | Secured Variable | Coverity Connect Username | `YOUR_USERNAME` |
  | `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` | Secured Variable | Coverity Connect Password or Access Token | `YOUR_PASSWORD` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI Download URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
  | `BRIDGE_BITBUCKET_API_TOKEN` | Secured Variable | A Bitbucket Access Token required to inject Pull Request Comments | `YOUR_ACCESS_TOKEN` |
- The following Bridge CLI parameters are required to inject pull request comments:

  | Parameter | Description | Value |
  | --- | --- | --- |
  | `coverity.prcomment.enabled` | Enable PR comments | `true` |
  | `bitbucket.project.repository.pull.number` | ID of PR with source code to scan | `$BITBUCKET_PR_ID` |
- Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

  If using a compiled language, add the following additional variables to specify the build and clean commands appropriate for the target language:

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_COVERITY_BUILD_COMMAND` | Variable | Build command for compiled languages | `mvn -B -DskipTests package` |
  | `BRIDGE_COVERITY_CLEAN_COMMAND` | Variable | Clean command for compiled languages | `mvn -B clean` |

  See Using Bridge With Compiled Languages and the Coverity section in Client scan tool parameters for an overview of the various alternative methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.
- For on-premises Coverity deployments, consider setting the `BRIDGE_COVERITY_LOCAL` environment variable to `true`. This instructs Bridge to download the full analysis kit and perform capture and analysis locally, which may be required for deployments with scan services disabled. See List of Mandatory and Optional Parameters For Coverity for more details.

## Instructions

Follow the steps below to configure a Bitbucket pipeline that invokes Bridge CLI for full scans and Pull Request scans:

1. Create the `bitbucket-pipelines.yml` containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - maven build image
   - build steps and caches

   ```
   # image: maven:3-eclipse-temurin-21
   pipelines:
     branches:
       '{main,master,develop,stage,release}':
         # - step:
         #     name: Build
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step:
             name: Coverity Full Scan
             # caches:
               # - maven
             script:
               - apt update && apt install -y curl file unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage connect
                   coverity.connect.project.name=$BITBUCKET_REPO_SLUG
                   coverity.connect.stream.name=$BITBUCKET_REPO_SLUG-$BITBUCKET_BRANCH
                   coverity.connect.policy.view='Outstanding Issues'
     pull-requests:
       '**':
           # - step:
           #     name: Build
           #     caches:
           #       - maven
           #     script:
           #       - mvn -B -DskipTests package
         - step:
             name: Coverity PR Scan
             # caches:
               # - maven
             script:
               - if [[ ! "${BITBUCKET_PR_DESTINATION_BRANCH}" =~ (main|master|develop|stage|release) ]]; then exit; fi
               - apt update && apt install -y curl file unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               ## Add the coverity.prcomment.impacts parameter to the bridge-cli command below
               ## This parameter adds review comments for issues filtered
               ## by impact. Default is High if unset.
               ## NOTE: Issues matching coverity.connect.policy.view are ignored if set
               # coverity.prcomment.impacts='High'
               - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage connect
                   coverity.connect.project.name=$BITBUCKET_REPO_SLUG
                   coverity.connect.stream.name=$BITBUCKET_REPO_SLUG-$BITBUCKET_PR_DESTINATION_BRANCH
                   coverity.prcomment.enabled='true'
                   bitbucket.workspace.id=$BITBUCKET_WORKSPACE
                   bitbucket.project.repository.name=$BITBUCKET_REPO_SLUG
                   bitbucket.project.repository.pull.number=$BITBUCKET_PR_ID
   ```

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans and Pull Request scans.

   A full scan is performed when code is pushed or merged to the `main`, `master`, `develop`, `stage` or `release` branches. The `coverity.connect.policy.view` parameter is configured to break the build if new or outstanding issues are detected as defined by the Outstanding Issues [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html) (see [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) for details).

   For Pull Requests targeting those branches, Bridge CLI is invoked directly to perform a Pull Request scan. New issues detected on the feature branch are added as Pull Request comments. Add the commented `coverity.prcomment.impacts` parameter to the Bridge CLI command to filter comments by impact level, with a default of "High" if unset.

   For both scan scenarios the Coverity project and stream are automatically derived from built-in Bitbucket CI environment variables. The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: PR review comments injected by Coverity PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `BRIDGE_COVERITY_LOCAL` environment variable should be set to `true`.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `BRIDGE_COVERITY_LOCAL` environment variable to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity Product documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
