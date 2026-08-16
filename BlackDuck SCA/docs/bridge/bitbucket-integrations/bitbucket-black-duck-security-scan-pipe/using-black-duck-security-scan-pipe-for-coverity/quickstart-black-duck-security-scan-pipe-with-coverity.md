---
title: "Quickstart: Black Duck Security Scan Pipe with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-pipe-with-coverity.html"
content_id: "KLqDnDbC2AdQNyrP5LPEdA"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:06.366989+00:00"
---

# Quickstart: Black Duck Security Scan Pipe with Coverity

This quickstart explains how to set up the Black Duck Security Scan Pipe for Bitbucket to run a pipeline that integrates with Coverity to run a full scan and Pull Request scan. Pull Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - Bitbucket Prerequisites
  - List of Mandatory and Optional Parameters For Coverity
  - Pull Request Comments
  - Using Fail Pull Requests With Coverity
  - Additional Bitbucket Configuration
- Coverity credentials.
- A Bitbucket Access Token is required to allow the pipeline to inject Pull Request review comments.
- For security reasons, it is advisable not to store credentials and access tokens directly in the pipeline. The recommended approach is to use [Bitbucket variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) with the `secured` option checked.
- The following Black Duck Security Scan Pipe parameters are required to enable injecting review comments into Pull Requests. These have been included in the quickstart example:

  Important: Pull Request comments will not be injected if these parameters and the required prerequisites are not correctly configured.

  | **Parameter** | **Description** | **Example** |
  | --- | --- | --- |
  | `BRIDGE_COVERITY_CONNECT_URL` | URL for Coverity Server | `$COVERITY_URL` |
  | `BRIDGE_COVERITY_CONNECT_USER_NAME` | Coverity Connect user name | `$COVERITY_USER` |
  | `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` | Coverity Connect user password | `COVERITY_PASSPHRASE` |
  | `BRIDGE_COVERITY_PRCOMMENT_ENABLED` | When `true`, this enables PR comments. | `"true"` |
  | `BRIDGE_BITBUCKET_API_TOKEN` | A Bitbucket Access Token. Required to inject review comments and upload SARIF reports. | `$BITBUCKET_REPO_ACCESS_TOKEN` |
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables) or workspace level (Workspace settings > Workspace variables > Add Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Variable | Coverity Server URL | `https://coverity.blackduck.com` |
  | `COVERITY_USER` | Secured Variable | Coverity Username | `USER_NAME` |
  | `COVERITY_PASSPHRASE` | Secured Variable | Coverity Passphrase | `PASSPHRASE` |
  | `BITBUCKET_REPO_ACCESS_TOKEN` | Secured Variable | A Bitbucket Access Token. Required to inject Pull Request comments. | `REPLACE_WITH_BITBUCKET_ACCESS_TOKEN` |

  Note: The Black Duck Security Scan Pipe integrates with Coverity via Bridge CLI. Additional scan configuration options not available through the pipe parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.

  Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Bridge must be configured with build and clean commands to capture and analyze the build.

  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure the Black Duck Security Scan Pipe to run a full scan and Pull Request scan:

1. For compiled languages, prepare a custom Docker image that contains the Black Duck Security Scan Pipe script in addition to the tools required for the build environment. There are two choices depending upon the needs of the organization:
   - **Extend Black Duck Security Pipe Image**: Build and publish a Docker image that extends the Black Duck Security Scan Pipe image to install the required build tools. This is the quickest option for simple build environments.
   - **Extend existing organization image**: For organizations using an existing Docker image for their build environment then that image can be extended to install the Black Duck Security Scan Pipe.
2. Create the `bitbucket-pipelines.yml` file that contains the following pipeline:

   Note: For compiled languages, make the following changes:
   - Replace the standard pipe with the custom pipe image.
   - Uncomment the `BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND` parameters.
   - Uncomment the build steps in both the pull-requests and branches sections.The quickstart uses a custom pipe image directly as described in step 2 of this guide. You can also use the `CUSTOM_IMAGE` parameter for custom images.

   ```
   definitions:
     services:
       docker:
         memory: 3072 # Allocate 3GB (3072MB) memory to docker service
     steps:
       - step: &blackduck-security-scan
           name: Coverity Black Duck Security Scan
           script:
             - |
               if [[ -z $BITBUCKET_PR_ID ]]; then
                 export COVERITY_POLICY_VIEW="Outstanding Issues"
               else
                 export COVERITY_POLICY_VIEW=""
               fi
             ## Uncomment the BRIDGE_COVERITY_PRCOMMENT_IMPACTS parameter to the variables below
             ## to adds review comments for issues filtered
             ## by impact. Default is High if unset.
             ## NOTE: Issues matching BRIDGE_COVERITY_CONNECT_POLICY_VIEW are ignored if set

             ## For compiled languages, replace the standard pipe below with a custom pipe image:
             ## - pipe: docker://your-registry/your-custom-image:tag
             - pipe: blackduck-inc/blackduck-security-scan:1.6.0
               variables:
                 BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
                 BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
                 BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
                 BRIDGE_COVERITY_CONNECT_POLICY_VIEW: $COVERITY_POLICY_VIEW
                 BRIDGE_COVERITY_PRCOMMENT_ENABLED: "true"
                 # BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'High'
                 BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN
                 # BRIDGE_COVERITY_LOCAL: "true"
                 ## For compiled languages, uncomment and configure these build commands:
                 # BRIDGE_COVERITY_BUILD_COMMAND: "mvn clean compile"
                 # BRIDGE_COVERITY_CLEAN_COMMAND: "mvn clean"
                 # INCLUDE_DIAGNOSTICS: "true"
           # artifacts:
           #  - ".bridge/**"

   pipelines:
     pull-requests:
       "**":
         # For compiled languages, uncomment the build step below
         # - step:
         #     name: Build
         #     image: maven:3-eclipse-temurin-17
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step: *blackduck-security-scan

     branches:
       "{main,master,develop,stage,release}":
         # For compiled languages, uncomment the build step below
         # - step:
         #     name: Build
         #     image: maven:3-eclipse-temurin-17
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step: *blackduck-security-scan
   ```

   Important: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled the `BRIDGE_COVERITY_LOCAL` line in the example should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed. This will override the default behavior that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above a `Coverity Black Duck Security` step runs whenever code is pushed to the `main`, `master`, `develop`, `stage` or `release` branches, or when a Pull Request is created. The scan type is automatically determined by the Black Duck Security Scan Pipe depending on the context in which the pipeline was triggered. The scan behavior is explained below.

   The pipeline integrates with a Coverity server instance via the `BRIDGE_COVERITY_CONNECT_URL`, `BRIDGE_COVERITY_CONNECT_USER_NAME` and `BRIDGE_COVERITY_CONNECT_PASSWORD` parameters.

   The Black Duck Security Scan Pipe will download and use the Coverity CLI to scan the codebase of the branch that triggered the workflow. Detected issues will be uploaded to a Coverity stream within a Coverity Connect project that is named after the repository. If the project doesn’t already exist, it is created automatically.

   The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   For full scans the `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` parameter will break the build if new or outstanding issues are detected as defined by the `Outstanding Issues` [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html). Consult [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) within the Coverity documentation for further details.

   Each time code is committed to a Pull Request branch that targets one of the specified base branches, a comparison is performed between the scan of the Pull Request branch and the latest full scan of its parent branch. Any new issues introduced by the Pull Request are automatically added as review comments. Coverity Fail Pull Requests are enabled by setting the `BRIDGE_COVERITY_PRCOMMENT_ENABLED` parameter to *true*. Use the `BRIDGE_COVERITY_PRCOMMENT_IMPACTS` parameter to add comments filtered by impact, with a default of `High` if unset. The source code management token created in the prerequisites is required to inject Pull Request review comments.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports as Bitbucket artifacts. These artifacts can be accessed and downloaded from the Artifacts tab of the pipeline's job page in Bitbucket (Repository > Pipelines).
3. Save the `bitbucket-pipelines.yml` pipeline file. If using the [Bitbucket Pipeline Editor](https://support.atlassian.com/bitbucket-cloud/docs/add-edit-and-commit-to-source-files/#Edit-files-online) then click Commit to save the changes to the pipeline. Alternatively, push the changes to the `main`, `master`, `develop`, `stage` or `release` branch of the repository. For example:

   ```
   git add bitbucket-pipelines.yml
   git commit -m "update pipeline to add security scan"
   git push -u origin main
   ```

   Once the changes have been saved to `bitbucket-pipelines.yml` the pipeline should be triggered to run on the `main`, `master`, `develop`, `stage` or `release` branch. Subsequently, it is then possible to open Bitbucket Pull Requests to run one or more Polaris Pull Request scans.

   An example review comment added to a Bitbucket Pull Request after a Coverity Pull Request scan has run is shown below.

   [image: PR review comments injected by Coverity PR Scan]

## Troubleshooting and support

If an error is encountered similar to the example below, then the `BRIDGE_COVERITY_LOCAL` parameter should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the workflow uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `BRIDGE_COVERITY_LOCAL` parameter to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity Product Documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- [Coverity Tutorials](https://community.blackduck.com/s/article/coverity-tutorials)
- [Coverity Projects and Streams Tutorial](https://community.blackduck.com/s/article/Coverity-Tutorial-Projects-and-Streams)
- [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html)
- [Black Duck Security Scan Pipe Repository](https://bitbucket.org/blackduck-inc/blackduck-security-scan/src/master/)
- Bridge Overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
