---
title: "Quickstart: Black Duck Security Scan Pipe with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-pipe-with-software-risk-manager.html"
content_id: "Pn~buBS5wrHMvJRVZwA0oQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:03.209411+00:00"
---

# Quickstart: Black Duck Security Scan Pipe with Software Risk Manager

This quickstart explains how to set up the Black Duck Security Scan Pipe to integrate with a Software Risk Manager project to run a full scan, triggered by push and merge events on specified branches.

Examples are provided for compiled and scripted languages with the option of exporting diagnostic logs as Bitbucket build artifacts.

Important: Please note that scanning Pull Requests, injecting review comments and creating SARIF reports is not currently supported for pipelines that integrate the Black Duck Security Scan Pipe with Software Risk Manager.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Bitbucket Prerequisites
  - List of Mandatory and Optional Parameters For Software Risk Manager
  - Additional Bitbucket Configuration
- Access to a Software Risk Manager (SRM) server instance.
- A Software Risk Manager role that allows creation of authentication tokens.
- The following Black Duck Security Scan Pipe parameters are required to enable scanning of default and non-default branches. These have been included in the quickstart example:

  Important: Scanning will result in an error if these parameters and the required prerequisites are not correctly configured.

  | **Parameter** | **Description** | **Example** |
  | --- | --- | --- |
  | `BRIDGE_SRM_URL` | Software Risk Manager server URL. | `$BRIDGE_SRM_URL` |
  | `BRIDGE_SRM_APIKEY` | Software Risk Manager API Key to enable integration with Software Risk Manager server. | `$BRIDGE_SRM_APIKEY` |
  | `BRIDGE_SRM_ASSESSMENT_TYPES` | Scan assessment types, e.g. `SAST` and/or `SCA`. | `SAST,SCA` |
  | `BRIDGE_SRM_BRANCH_NAME` | Branch name on the SRM server. | `$BITBUCKET_BRANCH` |
  | `BRIDGE_SRM_BRANCH_PARENT` | Parent branch name on the SRM server. Required for scanning new non default branches. | `$BRIDGE_SRM_BRANCH_PARENT` |

  Note: The Black Duck Security Scan Pipe integrates with Software Risk Manager via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables) or workspace level (Workspace settings > Workspace variables > Add Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_SRM_URL` | Variable | Software Risk Manager Server URL | `https://srm.blackduck.com` |
  | `$BRIDGE_SRM_APIKEY` | Secured Variable | Software Risk Manager API Key | `REPLACE_WITH_YOUR_API_KEY` |
- Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Bridge must be configured with build and clean commands to capture and analyze the build.
- - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure the Black Duck Security Scan Pipe to run a full scan:

1. For compiled languages, prepare a custom Docker image that contains the Black Duck Security Scan Pipe script in addition to the tools required for the build environment. There are two choices depending upon the needs of the organization:
   - **Extend Black Duck Security Pipe Image**: Build and publish a Docker image that extends the Black Duck Security Scan Pipe image to install the required build tools. This is the quickest option for simple build environments.
   - **Extend existing organization image**: For organizations using an existing Docker image for their build environment then that image can be extended to install the Black Duck Security Scan Pipe.

   **Note:** This step is only required for compiled languages that need a build environment. Scripted languages can use the standard pipe configuration shown in the next step.
2. Create the `bitbucket-pipelines.yml` file containing the following pipeline:

   Note: For compiled languages, make the following changes:
   - Replace the standard pipe with the custom pipe image.
   - Uncomment the `BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND` parameters.
   - Uncomment the build steps in the branches section.

   ```
   definitions:
     services:
       docker:
         memory: 3072 # Allocate 3GB (3072MB) memory to docker service
     steps:
       - step: &blackduck-security-scan
           name: Black Duck Security Scan SRM
           script:
             - |
               DEFAULT_BRANCH="main"
               if [ "$BITBUCKET_BRANCH" != "$DEFAULT_BRANCH" ]; then
                 echo "BRIDGE_SRM_BRANCH_PARENT=$DEFAULT_BRANCH" >> srm_env.txt
               else
                 echo "BRIDGE_SRM_BRANCH_PARENT=" >> srm_env.txt
               fi
             - source srm_env.txt

             ## For compiled languages, replace the standard pipe below with a custom pipe image:
             ## - pipe: docker://your-registry/your-custom-image:tag
             - pipe: blackduck-inc/blackduck-security-scan:1.6.0
               variables:
                 BRIDGE_SRM_URL: $BRIDGE_SRM_URL
                 BRIDGE_SRM_APIKEY: $BRIDGE_SRM_APIKEY
                 BRIDGE_SRM_ASSESSMENT_TYPES: SAST,SCA
                 BRIDGE_SRM_PROJECT_NAME: $BITBUCKET_REPO_SLUG
                 BRIDGE_SRM_BRANCH_NAME: $BITBUCKET_BRANCH
                 BRIDGE_SRM_BRANCH_PARENT: $BRIDGE_SRM_BRANCH_PARENT
                 ## For compiled languages, uncomment and configure these build commands:
                 # BRIDGE_COVERITY_CLEAN_COMMAND: "mvn -B clean"
                 # BRIDGE_COVERITY_BUILD_COMMAND: "mvn -B -DskipTests package"
                 # INCLUDE_DIAGNOSTICS: "true"
           # artifacts:
           #   - ".bridge/**"

   pipelines:
     branches:
       "{main,master,develop,stage,release}":
         # For compiled languages, uncomment the build step below
         # - step:
         #     name: Build
         #     image: maven:3-eclipse-temurin-21
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step: *blackduck-security-scan
   ```

   In the example above the Black Duck Security Scan Pipe will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_URL` parameter, using a given API key, `BRIDGE_SRM_APIKEY`. The Software Risk Manager project is named with the Bitbucket repository slug.

   If a full scan is triggered for a branch that is not the default branch, then the pipeline sets the parent branch (`BRIDGE_SRM_BRANCH_PARENT`) to the default branch. This helps ensure that non-default branches reference the default branch as their base during scanning operations.

   A full scan, including SAST and SCA assessments, will then be triggered by push events for the `main`, `master`, `develop`, `stage` or `release` branch.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs as Bitbucket artifacts. These artifacts can be accessed and downloaded from the Artifacts tab of the pipeline's job page in Bitbucket (Repository > Pipelines).
3. Push a new commit to the source repository to run the pipeline. Alternatively, trigger a manual run by navigating to Bitbucket Repository Sidebar > Pipelines > Run Pipeline. The results of the full scan will be available in the Software Risk Manager Dashboard.

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the `BRIDGE_SRM_BRANCH_PARENT` parameter has not been set.

Important: ERROR: Branch "develop" does not exist for the project and "srm.branch.parent" is empty but is required along with "srm.branch.name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, `stage` or `release`, the `BRIDGE_SRM_BRANCH_PARENT` parameter must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

## Useful resources

- [Software Risk Manager Product Documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- [Black Duck Security Scan Pipe Repository](https://bitbucket.org/blackduck-inc/blackduck-security-scan/src/master/)
- Bridge Overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
