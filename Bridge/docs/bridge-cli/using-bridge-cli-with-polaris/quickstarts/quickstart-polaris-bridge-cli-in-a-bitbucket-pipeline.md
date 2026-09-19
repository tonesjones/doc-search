---
title: "Quickstart: Polaris Bridge CLI in a Bitbucket pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-polaris-bridge-cli-in-a-bitbucket-pipeline.html"
content_id: "I9iSeNJAMd3FweRG7JnJrQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:59.787437+00:00"
---

# Quickstart: Polaris Bridge CLI in a Bitbucket pipeline

As an alternative to the Black Duck Security Scan Pipe, the Bridge CLI can be downloaded and directly executed in a Bitbucket pipeline. It has equivalent functionality, but includes an additional step to [download the Bridge CLI from blackduck-repo](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/).

To discover more about the Black Duck Security Scan Pipe and what it can do, take a look at the overview page.

Note: The Black Duck Security Scan Pipe (recommended) can be used for workflows instead of Bridge CLI by following the quickstart guide: Quickstart: Black Duck Security Scan Pipe with Polaris

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Setting up Black Duck Security Scan Pipe
  - Polaris Prerequisites
  - List of Mandatory and Optional Parameters For Polaris
  - Pull Request Comments
  - Additional Bitbucket configuration
- A [Bitbucket Access Token](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) is required to allow the pipeline to inject Pull Request review comments.
- For security reasons, it is advisable to use [Bitbucket variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) with the `secured` option checked to store credentials and access tokens.
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables or Workspace Settings > Workspace Variables > Add Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_BITBUCKET_API_TOKEN` | Secured Variable | [Bitbucket Access Token](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) | `YOUR_ACCESS_TOKEN` |
  | `BRIDGE_POLARIS_SERVERURL` | Variable | Polaris Server URL | <https://poc.polaris.blackduck.com> |
  | `BRIDGE_POLARIS_ACCESSTOKEN` | Secured Variable | Polaris Access Token. Use either a user access token (created in the Polaris UI) or a service account token here. | `YOUR_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI Download URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- The following Bridge CLI parameters are required to inject Pull Request comments:

  | Parameter | Description | Value |
  | --- | --- | --- |
  | `polaris.prComment.enabled` | Enable PR comments | `true` |
  | `bitbucket.project.repository.pull.number` | ID of PR with source code to scan | `$BITBUCKET_PR_ID` |
- Polaris uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build. If using a compiled language, add the following additional variables to specify the build and clean commands appropriate for the target language:

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_COVERITY_BUILD_COMMAND` | Variable | Build command for compiled languages | `mvn -B -DskipTests package` |
  | `BRIDGE_COVERITY_CLEAN_COMMAND` | Variable | Clean command for compiled languages | `mvn -B clean` |

  See Using Bridge With Compiled Languages and the Coverity section in Client Scan Tools for an overview of the various alternative methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a Bitbucket pipeline that invokes Bridge CLI for Polaris scans:

1. Create the `bitbucket-pipelines.yml` file containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - `image` line
   - `Build` steps
   - Build/clean command environment variables (`BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND`).

   ```
   ## -----------------------------------------------------------------------------
   # NOTE: The commented lines below are for compiled languages (e.g., Java, C++).
   # If your project requires a build step, uncomment and adjust those lines.
   ## -----------------------------------------------------------------------------

   # image: maven:3-eclipse-temurin-21

   pipelines:
     branches:
       "{main,master,develop,stage,release}":
         # - step:
         #     name: Build
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step:
             name: Polaris Full Scan
             # caches:
             #  - maven
             script:
               - apt update && apt install -y curl file unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               - |-
                 /tmp/bridge-cli-bundle-linux64/bridge-cli --stage polaris \
                   polaris.application.name=$BITBUCKET_WORKSPACE-$BITBUCKET_REPO_SLUG \
                   polaris.project.name=$BITBUCKET_REPO_SLUG \
                   polaris.branch.name=$BITBUCKET_BRANCH \
                   polaris.assessment.types=SAST,SCA \
                   polaris.reports.sarif.create='true'

     pull-requests:
       "**":
         # - step:
         #     name: Build
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step:
             name: Polaris PR Scan
             # caches:
             #  - maven
             script:
               - if [[ ! "${BITBUCKET_PR_DESTINATION_BRANCH}" =~ (main|master|develop|stage|release) ]]; then exit; fi
               - apt update && apt install -y curl file unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               - |-
                 /tmp/bridge-cli-bundle-linux64/bridge-cli --diagnostics --stage polaris \
                   polaris.application.name=$BITBUCKET_WORKSPACE-$BITBUCKET_REPO_SLUG \
                   polaris.project.name=$BITBUCKET_REPO_SLUG \
                   polaris.branch.name=$BITBUCKET_BRANCH \
                   polaris.assessment.types=SAST,SCA \
                   polaris.prComment.enabled='true' \
                   bitbucket.workspace.id=$BITBUCKET_WORKSPACE \
                   bitbucket.project.repository.name=$BITBUCKET_REPO_SLUG \
                   bitbucket.project.repository.pull.number=$BITBUCKET_PR_ID
   ```

   The example above performs a full scan when code is pushed or merged to the `main`, `master`, `develop`, `stage` or `release` branches. The Bridge CLI is downloaded from the URL specified by the `BRIDGECLI_LINUX64` variable and a full scan is run, performing SAST and SCA assessments on the branch code. To enable `DAST` assessment, set the `polaris.assessment.types` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.

   SARIF reports are exported for a full scan by setting the `polaris.reports.sarif.create` parameter to `true`.

   For Pull Requests targeting those branches, a Pull Request scan is run to perform SAST and SCA assessments. New issues detected on the feature branch are added as Pull Request comments.

   For both scan scenarios the Polaris application, project and branch are automatically derived from built-in Bitbucket CI environment variables.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: PR review comments injected by Bridge CLI Polaris PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Attention: Request Validation Failed: No concurrent entitlements found for the tenant

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the pipeline, consult [Create An Application](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) in Polaris.

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
