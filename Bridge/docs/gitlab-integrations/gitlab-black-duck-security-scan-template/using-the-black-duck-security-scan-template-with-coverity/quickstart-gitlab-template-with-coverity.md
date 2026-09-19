---
title: "Quickstart: GitLab Template with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-gitlab-template-with-coverity.html"
content_id: "ln~l1Ogf~wIMEl06k2Ivxg"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:09.766947+00:00"
---

# Quickstart: GitLab Template with Coverity

This quickstart explains how to set up the Black Duck Security Scan Template to run a pipeline that integrates with Coverity to run a full scan and Merge Request scan. Merge Request review comments are only created for new issues that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Merge Request scan will be triggered by push events to Merge Requests that target those branches. Any new security issues introduced by a Merge Request will be added as review comments. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts.

## Prerequisites

- The following readme is recommended:
  - GitLab prerequisites
  - Merge Request Comments
  - Using fail merge requests with Coverity
  - Using the Black Duck Security Scan Template with Coverity
  - Additional GitLab configuration
- Admin access to a GitLab repository.
- Coverity credentials.
- A [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access is required to allow the pipeline to inject review comments into GitLab Merge Requests.
- For security reasons, it is advisable not to store credentials directly in the workflow. The recommended approach is to use masked and hidden variables.

  Important: It is adviseable that the variables are added as project variables. Group variable inheritance can cause scans to fail under certain conditions. Be sure to set the mask variable flag for `COVERITY_USER`, `COVERITY_PASSPHRASE` and `GITLAB_USER_TOKEN` to avoid exposure in the CI logs.
- The following Black Duck Security Scan Template parameters are required to enable injecting review comments into Merge Requests and have been included in the quickstart example:.

  Important: Merge Request comments will not be injected if these parameters and the required prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `BRIDGE_COVERITY_PRCOMMENT_ENABLED` | When `true`, this enables Merge Request comments. | `"true"` |
  | `BRIDGE_GITLAB_USER_TOKEN` | A [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access to inject review comments. | `$GITLAB_USER_TOKEN` |

  Note: The Black Duck Security Scan Template integrates with Coverity via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Add the following secrets and variables (GitLab > Project sidebar > Settings > CI/CD > Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Masked | Coverity Server URL | `https://coverity.blackduck.com` |
  | `COVERITY_USER` | Masked and hidden | Coverity Username | `USER_NAME` |
  | `COVERITY_PASSPHRASE` | Masked and hidden | Coverity Passphase | `PASSPHRASE` |
  | `GITLAB_USER_TOKEN` | Masked and hidden | [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access to inject review comments. | `REPLACE_WITH_YOUR_TOKEN` |
- Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
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

   coverity:
     stage: security
     variables:
       BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
       BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
       BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSPHRASE
       BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
       # BRIDGE_COVERITY_BUILD_COMMAND and BRIDGE_COVERITY_CLEAN_COMMAND (uncomment and configure for compiled languages)
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
       # BRIDGE_COVERITY_LOCAL: true
       # INCLUDE_DIAGNOSTICS: true
     rules:
       - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
         variables:
           BRIDGE_COVERITY_CONNECT_POLICY_VIEW: Outstanding Issues
       - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
         variables:
           BRIDGE_COVERITY_PRCOMMENT_ENABLED: true
           ## Use the parameter below to add comments for issues filtered 
           ## by impact. Default is High if unset
           ## NOTE: Issues matching BRIDGE_COVERITY_CONNECT_POLICY_VIEW are ignored if set
           #BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'High'
     before_script:
       - apt-get -qq update && apt-get install -y curl file unzip
     extends: .run-black-duck-tools
     # artifacts:
     #  name: "bridge-logs"
     #  when: always
     #  paths:
     #    - .bridge/
     #  expire_in: 30 days
   ```

   Important: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled or Coverity versions < 2022.3 the `coverity_local` line in the example should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed with the full toolkit. This will override the default behavior that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above the Black Duck Security Scan Action will download and use the Coverity CLI to scan the codebase of the branch that triggered the pipeline. Branches are defined in the `SCAN_BRANCHES` pipeline variable.

   For a full scan, detected issues that violate the `Outstanding Issues` [Coverity View](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cov-platform-rest-api/topics/views.html) will be uploaded to a Coverity stream within a Coverity Connect project, named after the repository. If the project doesn’t already exist, it is created automatically.

   The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   Each time code is committed to a Merge Request that targets a base branch, a comparison is performed with the latest full scan. Any new issues introduced by the Coverity Fail Merge Request are automatically added as review comments. This behaviour is enabled by setting the `BRIDGE_COVERITY_PRCOMMENT_ENABLED` parameter to *true*. Use the `BRIDGE_COVERITY_PRCOMMENT_IMPACTS` parameter to add comments filtered by impact, with a default of high if unset.

   The source code management token created in the prerequisites is required to inject Merge Request review comments.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports from the `.bridge` folder as GitLab artifacts. These artifacts can be accessed and downloaded from the pipeline's job page in GitLab (Project > Build > Jobs).

   Note: If additional configuration options are required for complex build environments, then the recommended approach is to use a **[`coverity.yml`](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/b111ebf4ee3429ab6eea7cab4f88cbd5.topic)** configuration file in the root of the repository. Such an approach facilitates reuse across repositories.
2. Save the `.gitlab-ci.yml` pipeline file. If using the [GitLab Pipeline Editor](https://docs.gitlab.com/ci/pipeline_editor) then click Commit Changes to save the changes to the pipeline. Alternatively, push the changes to the `main` or `master` branch of the repository. For example:

   ```
   git add .gitlab-ci.yml
   git commit -m "update pipeline to add security scan"
   git push -u origin main
   ```

   Once the changes have been saved to `.gitlab-ci.yml` the pipeline should be triggered to run on the `main` or `master` branch. Subsequently, it is then possible to open GitLab Merge Requests to run one or more Coverity Merge Request scans.

   An example review comment added to a GitLab Merge Request after a Coverity Merge Request scan has run is shown below.

   [image: Merge Request review comments injected by Coverity Merge Request Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `coverity_local` parameter should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are likely not enabled. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `coverity_local` parameter to `true` enables the full analysis toolkit at the client. Subsequently, the scan and analysis will be performed locally by the pipeline. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

If a pipeline error is encountered similar to the example below, then it is likely that organization firewall rules maybe restricting access to the template.

Attention: Unable to create pipeline Project `blackduck-inc/black-duck-security-scan` not found or access denied! Make sure any includes in the pipeline configuration are correctly defined.

The recommended solution is to check that the template is referenced correctly and then perform one of the following actions:

- Arrange access with the organization's IT department.
- Use a GitLab self managed runner.

## Useful resources

- [Coverity Product Documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- [Coverity Tutorials](https://community.blackduck.com/s/article/coverity-tutorials)
- [Coverity Projects and Streams Tutorial](https://community.blackduck.com/s/article/Coverity-Tutorial-Projects-and-Streams)
- [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html)
- Bridge product overview
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
