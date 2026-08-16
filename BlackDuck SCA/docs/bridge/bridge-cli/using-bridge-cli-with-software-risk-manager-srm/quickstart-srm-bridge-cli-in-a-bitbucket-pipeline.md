---
title: "Quickstart: SRM Bridge CLI in a Bitbucket pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-srm-bridge-cli-in-a-bitbucket-pipeline.html"
content_id: "RY3ASea6IDMpG00JPMwzig"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:25.960289+00:00"
---

# Quickstart: SRM Bridge CLI in a Bitbucket pipeline

As an alternative to the Black Duck Security Scan Pipe, the Bridge CLI can be downloaded and directly executed in a Bitbucket pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use Bridge CLI directly from a Bitbucket pipeline, the correct Bridge CLI Software Risk Manager parameters must be passed directly inside the workflow. Appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Pipe (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Bitbucket Security Scan Pipe and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - Setting up Black Duck Security Scan Pipe
  - List of mandatory and optional parameters for SRM
  - Additional Bitbucket configuration
- For security reasons, it is advisable to use [Bitbucket variables and secrets](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) to store credentials and access tokens.
- Add the following variables and secrets in your Bitbucket repository or workspace settings:

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `SRM_URL` | Repository Variable | SRM server URL | `https://srm.example.com` |
  | `SRM_APIKEY` | Repository Secret | SRM API key | `REPLACE_WITH_YOUR_APIKEY` |
  | `BRIDGECLI_LINUX64` | Repository Variable | Bridge CLI download URL for Linux | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

  If using a compiled language, add the following additional variables to specify the build and clean commands appropriate for the target language:

  | Parameter | Type | Description | Value |
  | --- | --- | --- | --- |
  | `BRIDGE_COVERITY_BUILD_COMMAND` | Variable | Build command for compiled languages | `mvn -B -DskipTests package` |
  | `BRIDGE_COVERITY_CLEAN_COMMAND` | Variable | Clean command for compiled languages | `mvn -B clean` |

  See Using bridge with compiled languages and the Coverity section in Bridge Options to Configure Tools for an overview of the various alternative methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a Bitbucket pipeline that invokes Bridge CLI for SRM scans:

1. Create the `bitbucket-pipelines.yml` file containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - Maven build image
   - `Build` step
   - `caches` section in the `SRM Full Scan` step

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
         #     runs-on:
         #       - self.hosted
         #       - macos
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step:
             name: SRM Full Scan
             # caches:
             #   - maven
             script:
               - apt update && apt install -y curl file unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               - export DEFAULT_BRANCH=main
               - export BRANCH_PARENT=$( [ "$BITBUCKET_BRANCH" != "$DEFAULT_BRANCH" ] && echo "$DEFAULT_BRANCH" || echo "" )
               - |
                 /tmp/bridge-cli-bundle-linux64/bridge-cli --stage srm \
                  srm.url=$SRM_URL \
                  srm.apikey=$SRM_APIKEY \
                  srm.project.name=$BITBUCKET_REPO_SLUG \
                  srm.branch.name=$BITBUCKET_BRANCH \
                  srm.branch.parent="$BRANCH_PARENT" \
                  srm.assessment.types=SAST,SCA
   ```

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans.

   The Bitbucket Pipeline will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_URL` parameter, using a given API key, `BRIDGE_SRM_APIKEY`.

   The Software Risk Manager project will be created if it does not already exist and named with the Bitbucket repository slug. Similarily the SRM branch name is derived from the source branch name.

   A full scan, including SAST and SCA assessments, is triggered by push events for the `main` and `develop` branch.
2. Run scans

   Once the workflow is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Test:** Monitor the output to verify that the SRM scan completes successfully and issues appear in SRM Dashboard.

## Troubleshooting and support

If errors are encountered during the pipeline run, ensure that all variables are set correctly and that the Bridge CLI can access the SRM server.

If a pipeline error is encountered similar to the example below, then it is likely that the `BRIDGE_SRM_BRANCH_PARENT` parameter has not been set.

Important: ERROR: Branch "develop" does not exist for the project and "srm.branch.parent" is empty but is required along with "srm.branch.name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, `stage` or `release`, the `BRIDGE_SRM_BRANCH_PARENT` parameter must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

## Useful resources

- [SRM product documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
