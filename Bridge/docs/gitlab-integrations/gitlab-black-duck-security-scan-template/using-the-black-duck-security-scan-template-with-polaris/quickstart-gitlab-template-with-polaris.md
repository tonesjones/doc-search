---
title: "Quickstart: GitLab Template with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-gitlab-template-with-polaris.html"
content_id: "lhv1OV1yiNnMnTgy3a8iQQ"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:06.432333+00:00"
---

# Quickstart: GitLab Template with Polaris

This quickstart explains how to set up the Black Duck Security Scan Template to run a pipeline that integrates with Polaris to run a full scan and Merge Request scan. Merge Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Merge Request scan will be triggered by push events to Merge Requests that target those branches. Any new security issues introduced by a Merge Request will be added as review comments. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts. For full scans Fix Merge Requests will be created to upgrade dependencies.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitLab prerequisites
  - Polaris Prerequisites
  - Merge Request Comments
  - Fix Merge Requests
  - Using the Black Duck Security Scan Template with Polaris
  - Additional GitLab configuration
  - [GitLab Pipeline editor](https://docs.gitlab.com/ci/pipeline_editor/)
- A [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access is required to allow the pipeline to inject review comments into GitLab Merge Requests.
- For security reasons, it is advisable not to store credentials directly in the workflow. The recommended approach is to use masked and hidden variables.

  Important: It is adviseable that these are added as project variables. Group variable inheritance can cause scans to fail under certain conditions. Be sure to set the mask variable flag for `POLARIS_ACCESSTOKEN` and `GITLAB_USER_TOKEN` to avoid exposure in the CI logs.
- The following Black Duck Security Scan Template parameters are required to enable injecting review comments into Merge Requests and raise Fix Merge Requests. The parameters have been included in the quickstart example:

  Important: Merge Request comments will not be injected and Fix Merge Requests will not be raised if these parameters and the prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `BRIDGE_POLARIS_APPLICATION_NAME` | The name of the Polaris application. | `$CI_PROJECT_NAME` |
  | `BRIDGE_POLARIS_PRCOMMENT_ENABLED` | When `true`, this enables PR comments. | `"true"` |
  | `BRIDGE_POLARIS_FIXPR_ENABLED` | Enable Fix Merge Request creation for SCA vulnerabilities. Creates Merge Requests with dependency upgrades to fix security issues. | `"true"` |
  | `BRIDGE_GITLAB_USER_TOKEN` | A [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access. Required to inject review comments. The value should be a masked and hidden CI pipeline variable. | `$GITLAB_USER_TOKEN` |

  Note: The Black Duck Security Scan Template integrates with Polaris via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (GitLab > Project sidebar > Settings > CI/CD > Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `POLARIS_SERVERURL` | Masked | Polaris Server URL | `https://polaris.blackduck.com` |
  | `POLARIS_ACCESSTOKEN` | Masked and hidden | Polaris Access Token. You can use either a user access token (created in the Polaris UI) or a service account token here. | `REPLACE_WITH_YOUR_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
  | `GITLAB_USER_TOKEN` | Masked and hidden | [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access. Required to inject review comments in Merge Requests. | `REPLACE_WITH_YOUR_TOKEN` |
- Polaris uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge With Compiled Languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure the Black Duck Security Scan Template to run a full scan and Merge Request scan:

1. Create the `.gitlab-ci.yaml` containing the following pipeline.

   Note: For compiled languages, uncomment the following:
   - Maven build image
   - `BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND` parameters
   - `build`, `test` and `deploy` stages
   - Build related variables, e.g. `MAVEN_OPTS` and `MAVEN_CLI_OPTS`
   - Build related cache paths, e.g. .m2/repository, target

   ```
   include:
     - project: blackduck-inc/black-duck-security-scan
       ref: v2
       file: templates/security_scan.yml

   stages:
     - build
     - test
     - security
     - deploy

   variables:
     SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
   #  MAVEN_OPTS: >-
   #    -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
   #  MAVEN_CLI_OPTS: >-
   #    --batch-mode

   #cache:
   #  paths:
   #    - .m2/repository/
   #    - target/

   # For compiled languages, uncomment and configure the build image below:
   # image: maven:3-eclipse-temurin-21

   # For compiled languages, uncomment and configure the build stages below:
   # build:
   #   stage: build
   #   script: mvn -B compile

   # test:
   #   stage: test
   #   script: mvn -B test

   # deploy:
   #   stage: deploy
   #   only:
   #     variables:
   #       - $CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES
   #   script: mvn -B install

   polaris:
     stage: security
     rules:
       - if:
           (($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event') ||
           ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event'))
     variables:
       BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
       BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESS_TOKEN
       BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVER_URL
       BRIDGE_POLARIS_APPLICATION_NAME: $CI_PROJECT_NAMESPACE-$CI_PROJECT_NAME
       BRIDGE_POLARIS_ASSESSMENT_TYPES: "SAST,SCA"
       BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"
       BRIDGE_POLARIS_FIXPR_ENABLED: "true"
       BRIDGE_POLARIS_REPORTS_SARIF_CREATE: "true"
       BRIDGE_POLARIS_REPORTS_GITLAB_CREATE: "true"
       # BRIDGE_COVERITY_BUILD_COMMAND and BRIDGE_COVERITY_CLEAN_COMMAND (uncomment and configure for compiled languages)
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
       # INCLUDE_DIAGNOSTICS: "true"
     before_script:
       - apt-get -qq update && apt-get install -y curl file unzip
     extends: .run-black-duck-tools
     # artifacts:
     #   name: "bridge-logs"
     #   when: always
     #   paths:
     #     - .bridge/
     #   expire_in: 30 days
   ```

   In the example above a `polaris` pipeline job runs whenever code is pushed to any branch listed in the `SCAN_BRANCHES` variable, or when a Merge Request targets one of those branches. The scan type is automatically determined by the Black Duck Security Scan Template depending on the context in which the pipeline was triggered. The scan behavior is explained below.

   The pipeline integrates with a Polaris server instance via the `BRIDGE_POLARIS_SERVERURL` and `BRIDGE_POLARIS_ACCESSTOKEN` parameters. A scan will run for a Polaris application named after the GitLab project’s namespace and name. Within this application, a project will be created, if it doesn’t already exist, to store the scan results. The branch in Polaris is automatically derived from the branch that triggered the scan.

   The behavior of the scans is as follows:

   - **Full scan**: Triggered by push events to any of the branches defined in the `SCAN_BRANCHES` variable. In this scenario the Black Duck Security Scan Template will upload artifacts to the Polaris server for scanning:
     - SAST and SCA assessments will be run. To enable DAST assessment, set the `BRIDGE_POLARIS_ASSESSMENT_TYPES` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - Fix Merge Requests are enabled to raise Merge Requests to upgrade dependencies for full scans of branches. See Fix Merge Requests and Using the Black Duck Security Scan Template with Polaris for further information and examples that demonstrate how to:
       - Configure order of preference for upgrade guidance.
       - Raise Fix Merge Requests by severity.
       - Enforce a maximum limit for the number of Fix Merge Requests created.
     - A SARIF report and [GitLab Vulnerability Reports](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/c5491cfa4e0e28b3d44d91ad5e01da58.topic) will be generated and exported only for full scans. [GitLab Vulnerability Reports](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/c5491cfa4e0e28b3d44d91ad5e01da58.topic) are available for preview to users with a GitLab Ultimate subscription. If the scan detects a policy violation then the GitLab vulnerability reports will not be uploaded. For details on how to bypass this behaviour visit [How to use GitLab Vulnerability Reports](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/c5491cfa4e0e28b3d44d91ad5e01da58.topic).
   - **Merge Request scan**: Triggered for Merge Request push events, where the target branch of the merge matches one of the branches defined in the `SCAN_BRANCHES` variable. A Merge Request scan is performed that will run both SAST and SCA assessments. Review comments will be injected (`BRIDGE_POLARIS_PRCOMMENT_ENABLED: true`) for any new issues introduced since the latest full scan of the Merge Request's target branch.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports from the `.bridge` folder as GitLab artifacts. These artifacts can be accessed and downloaded from the pipeline's job page in GitLab (Project > Build > Jobs).
2. Save the `.gitlab-ci.yml` pipeline file. If using the [GitLab Pipeline Editor](https://docs.gitlab.com/ci/pipeline_editor) then click Commit Changes to save the changes to the pipeline. Alternatively, push the changes to the `main` or `master` branch of the repository. For example:

   ```
   git add .gitlab-ci.yml
   git commit -m "update pipeline to add security scan"
   git push -u origin main
   ```

   Once the changes have been saved to `.gitlab-ci.yml` the pipeline should be triggered to run on the `main` or `master` branch. Subsequently, it is then possible to open GitLab Merge Requests to run one or more Polaris Merge Request scans.

   An example review comment added to a GitLab Merge Request after a Polaris Pull Request scan has run is shown below.

   [image: Merge Request review comments injected by Polaris Merge Request Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Attention: Request Validation Failed: No concurrent entitlements found for the tenant

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the pipeline, consult [create an application in](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) Polaris.

If a pipeline error is encountered similar to the example below, then it is likely that organization firewall rules maybe restricting access to the template.

Attention: Unable to create pipeline Project `blackduck-inc/black-duck-security-scan` not found or access denied! Make sure any includes in the pipeline configuration are correctly defined.

The recommended solution is to check that the template is referenced correctly and then perform one of the following actions:

- Arrange access with the organization's IT department.
- Use a GitLab self managed runner.

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
