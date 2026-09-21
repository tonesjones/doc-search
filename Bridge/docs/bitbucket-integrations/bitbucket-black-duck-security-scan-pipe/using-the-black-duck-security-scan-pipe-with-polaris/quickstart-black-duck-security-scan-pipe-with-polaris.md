---
title: "Quickstart: Black Duck Security Scan Pipe with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-pipe-with-polaris.html"
content_id: "XyofGonTANhZYCBnHqAhaQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:01.868002+00:00"
---

# Quickstart: Black Duck Security Scan Pipe with Polaris

This quickstart explains how to set up the Black Duck Security Scan Pipe for Bitbucket to run a pipeline that integrates with Polaris to run a full scan and Pull Request scan. Pull Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts. For full scans Fix Pull Requests will be created to upgrade dependencies.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - Polaris Prerequisites
  - Bitbucket Prerequisites
  - List of Mandatory and Optional Parameters For Polaris
  - Pull Request Comments
  - Fix Pull Requests
  - [Micro-course - Polaris: Using the Black Duck Security Scan Action](https://blackduck.skilljar.com/polaris-using-the-synopsys-github-action?_gl=1*zpeive*_gcl_aw*R0NMLjE3NTAzNDYyMjcuRUFJYUlRb2JDaE1JMnRtZTRPUDlqUU1WODBOSEFSMXFiaFdXRUFBWUJDQUFFZ0lTTVBEX0J3RQ..*_gcl_au*MTIwNTY1MjIzOC4xNzQ5NzE1MDcy*_ga*MTU0OTA1MzYyMS4xNzQ5NzE1MDcw*_ga_SDT67CPG8V*czE3NTU3ODQ2NDMkbzE3NSRnMSR0MTc1NTc5MTIyNSRqNDMkbDAkaDA.)
  - Additional Bitbucket Configuration
- A Bitbucket Access Token is required to allow the pipeline to inject Pull Request review comments, raise Fix PR and upload SARIF reports.
- For security reasons, it is advisable not to store credentials and access tokens directly in the pipeline. The recommended approach is to use [Bitbucket variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) with the `secured` option checked.
- The following Black Duck Security Scan Pipe parameters are required to enable injecting review comments into Pull Requests, raise Fix Pull Requests and upload SARIF reports. These have been included in the quickstart example:

  Important: Pull Request comments will not be injected, Fix Pull Requests will not be raised and SARIF reports will not be uploaded if these parameters and the required prerequisites are not correctly configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `BRIDGE_POLARIS_PRCOMMENT_ENABLED` | When `true`, this enables PR comments. | `"true"` |
  | `BRIDGE_POLARIS_FIXPRR_ENABLED` | When `true`, this enables raising Fix PRs. | `"true"` |
  | `BRIDGE_POLARIS_REPORTS_SARIF_CREATE` | When `true`, for full scans this creates and uploads SARIF reports as a pipeline artifact, accessible from the `Artifact` tab of the pipeline job output. | `"true"` |
  | `BRIDGE_POLARIS_SERVERURL` | URL of Polaris server instance. | `$POLARIS_SERVER_URL` |
  | `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris Access Token to enable integration with Polaris server. | `$POLARIS_ACCESS_TOKEN` |
  | `BRIDGE_BITBUCKET_API_TOKEN` | A Bitbucket Access Token. Required to inject review comments and upload SARIF reports. | `$BITBUCKET_REPO_ACCESS_TOKEN` |
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables) or workspace level (Workspace settings > Workspace variables > Add Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `POLARIS_SERVER_URL` | Variable | Polaris Server URL | `https://polaris.blackduck.com` |
  | `POLARIS_ACCESS_TOKEN` | Secured Variable | Polaris Access Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `BITBUCKET_REPO_ACCESS_TOKEN` | Secured Variable | A Bitbucket Access Token. Required to inject review comments, raise Fix PRs and upload SARIF reports. | `REPLACE_WITH_BITBUCKET_ACCESS_TOKEN` |

  Note: The Black Duck Security Scan Pipe integrates with Polaris via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.

  Polaris uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
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
           name: Polaris Black Duck Security Scan
           script:
             ## For compiled languages, replace the standard pipe below with a custom pipe image:
             ## - pipe: docker://your-registry/your-custom-image:tag
             - pipe: blackduck-inc/blackduck-security-scan:1.6.0
               variables:
                 BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
                 BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
                 BRIDGE_POLARIS_ASSESSMENT_TYPES: "SCA,SAST"
                 BRIDGE_POLARIS_APPLICATION_NAME: $BITBUCKET_REPO_SLUG
                 BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"
                 BRIDGE_POLARIS_FIXPR_ENABLED: "true"
                 BRIDGE_POLARIS_REPORTS_SARIF_CREATE: "true"
                 BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN
                 ## For compiled languages, uncomment and configure these build commands:
                 # BRIDGE_POLARIS_CLEAN_COMMAND: "mvn -B clean"
                 # BRIDGE_POLARIS_BUILD_COMMAND: "mvn -B -DskipTests package"
                 # INCLUDE_DIAGNOSTICS: true
           # artifacts:
           #  - ".blackduck/integrations/polaris/sarif/report.sarif.json"
           #  - ".bridge/**"

   pipelines:
     pull-requests:
       "**":
         # For compiled languages, uncomment the build step below
         # - step:
         #     name: Build
         #     image: maven:3-eclipse-temurin-21
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
         #     image: maven:3-eclipse-temurin-21
         #     caches:
         #       - maven
         #     script:
         #       - mvn -B -DskipTests package
         - step: *blackduck-security-scan
   ```

   In the example above a `Polaris Black Duck Security` step runs whenever code is pushed to the `main`, `master`, `develop`, `stage` or `release` branches, or when a Pull Request is created. The scan type is automatically determined by the Black Duck Security Scan Pipe depending on the context in which the pipeline was triggered. The scan behavior is explained below.

   The pipeline integrates with a Polaris server instance via the `BRIDGE_POLARIS_SERVERURL` and `BRIDGE_POLARIS_ACCESSTOKEN` parameters. A scan will run for a Polaris application named using the Bitbucket repository slug. Within this application, a project will be created, if it doesn’t already exist, to report the scan results. The branch in Polaris is automatically derived from the branch in the source repository that triggered the scan.

   The behavior of the scans is as follows:

   - **Full scan**: Triggered by push events to `main`, `master`, `develop`, `stage` or `release` branches. In this scenario the Black Duck Security Scan Pipe will upload artifacts to the Polaris server for scanning:

     - SAST and SCA assessments will be run. To enable DAST assessment, set the `BRIDGE_POLARIS_ASSESSMENT_TYPES` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - Fix Pull Requests are enabled to raise Pull Requests to upgrade dependencies for full scans of branches. See Fix pull requests (Fix PRs) and Using the Black Duck Security Scan Pipe with Polaris for further information and examples that demonstrate how to:
       - Configure order of preference for upgrade guidance.
       - Raise Fix Pull Requests by severity.
       - Enforce a maximum limit for the number of Fix Pull Requests created.
     - A SARIF report will be generated and exported only for full scans. This operation requires a Bitbucket Access Token.
   - **Pull Request scan**: Triggered for Pull Request push events. A Pull Request scan is performed that will run both SAST and SCA assessments. Review comments will be injected (`BRIDGE_POLARIS_PRCOMMENT_ENABLED: true`) for any new issues introduced since the latest full scan of the Pull Request's target branch.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports as Bitbucket artifacts. These artifacts can be accessed and downloaded from the Artifacts tab of the pipeline's job page in Bitbucket (Repository > Pipelines).
3. Save the `bitbucket-pipelines.yml` pipeline file. If using the [Bitbucket Pipeline Editor](https://support.atlassian.com/bitbucket-cloud/docs/add-edit-and-commit-to-source-files/#Edit-files-online) then click Commit to save the changes to the pipeline. Alternatively, push the changes to the `main`, `master`, `develop`, `stage` or `release` branch of the repository. For example:

   ```
   git add bitbucket-pipelines.yml
   git commit -m "update pipeline to add security scan"
   git push -u origin main
   ```

   Once the changes have been saved to `bitbucket-pipelines.yml` the pipeline should be triggered to run on the `main`, `master`, `develop`, `stage` or `release` branch. Subsequently, it is then possible to open Bitbucket Pull Requests to run one or more Polaris Pull Request scans.

   An example review comment added to a Bitbucket Pull Request after a Polaris Pull Request scan has run is shown below.

   [image: PR review comments injected by Polaris PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Important: Request Validation Failed: No concurrent entitlements found for the tenant

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the workflow, consult [create an application in](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) Polaris.

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- [Black Duck Security Scan Pipe Repository](https://bitbucket.org/blackduck-inc/blackduck-security-scan/src/master/)
- Bridge Overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
