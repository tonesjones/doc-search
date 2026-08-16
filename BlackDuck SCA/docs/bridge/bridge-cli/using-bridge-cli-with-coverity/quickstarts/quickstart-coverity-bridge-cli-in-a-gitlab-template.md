---
title: "Quickstart: Coverity Bridge CLI in a GitLab template"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-coverity-bridge-cli-in-a-gitlab-template.html"
content_id: "soatkYyjc6vQ1azDjrmv4g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:21.730342+00:00"
---

# Quickstart: Coverity Bridge CLI in a GitLab template

As an alternative to the Black Duck Security Scan Template, the Bridge CLI can be downloaded and directly executed in a GitLab workflow. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Coverity parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Template (recommended) can be used for workflows instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Template and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitLab prerequisites
  - Merge Request Comments
  - Using Fail Merge Requests With Coverity
  - List of Mandatory and Optional Parameters For Coverity
  - Additional GitLab configuration
- A [GitLab Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) is required to allow the pipeline to inject merge request review comments.
- For security reasons, it is advisable to use [GitLab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/) to store credentials and access tokens.
- Add the following variables in your GitLab project or group settings (Settings > CI/CD > Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `COVERITY_URL` | Variable | Coverity Connect Server URL | `https://coverity.example.com` |
  | `COVERITY_USER` | Masked Variable | Coverity Connect Username | `YOUR_USERNAME` |
  | `COVERITY_PASSPHRASE` | Masked Variable | Coverity Connect Password or Access Token | `YOUR_PASSWORD` |
  | `GITLAB_USER_TOKEN` | Masked Variable | [GitLab Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) | `YOUR_ACCESS_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI Download URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
  | `SCAN_BRANCHES` | Variable | Regex pattern for branches to scan | `/^(main|master|develop|stage|release)$/` |

Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge With Compiled Languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a workflow pipeline that invokes Bridge CLI for full scans and Merge Request scans:

1. Create the `.gitlab-ci.yml` containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
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

   # cache:
   #   paths:
   #     - .m2/repository/
   #     - target/

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

   coverity-bridge-cli:
     stage: security
     variables:
       BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
       BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
       BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSPHRASE
       BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $CI_PROJECT_NAME
       # BRIDGE_COVERITY_BUILD_COMMAND and BRIDGE_COVERITY_CLEAN_COMMAND (uncomment and configure for compiled languages)
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
       BRIDGE_GITLAB_REPOSITORY_NAME: $CI_PROJECT_ID
       BRIDGE_GITLAB_REPOSITORY_BRANCH_NAME: $CI_COMMIT_REF_NAME
       BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
       # BRIDGE_COVERITY_LOCAL: true

     rules:
       - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
         variables:
           BRIDGE_COVERITY_CONNECT_STREAM_NAME: $CI_PROJECT_NAME-$CI_COMMIT_REF_NAME
           BRIDGE_COVERITY_CONNECT_POLICY_VIEW: 'Outstanding Issues'
       ## Add BRIDGE_COVERITY_PRCOMMENT_IMPACTS to variables in the rule below to add review comments
       ## for issues filtered by impact. Default is High if unset
       ## NOTE: Issues matching BRIDGE_COVERITY_CONNECT_POLICY_VIEW are ignored if set
       # BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'High'
       - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
         variables:
           BRIDGE_COVERITY_CONNECT_STREAM_NAME: $CI_PROJECT_NAME-$CI_MERGE_REQUEST_TARGET_BRANCH_NAME
           BRIDGE_COVERITY_PRCOMMENT_ENABLED: true
           BRIDGE_GITLAB_REPOSITORY_PULL_NUMBER: $CI_MERGE_REQUEST_IID
     
     before_script:
       - apt-get -qq update && apt-get -qq install curl file unzip
     script:
       - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
       - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage connect
     # artifacts:
     #   name: "bridge-logs"
     #   when: always
     #   paths:
     #     - .bridge/
     #   expire_in: 30 days
   ```

   Note: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed with the full toolkit. This will override the default behaviour that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans and Merge Request scans.

   A full scan is run when code is pushed or merged to branches matching the `SCAN_BRANCHES` pattern (main, master, develop, stage, or release). The `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` environment variable is configured to break the build if new or outstanding issues are detected as defined by the Outstanding Issues [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html) (see [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) for details).

   For merge requests targeting those branches, Bridge CLI is invoked directly to perform a merge request scan. New issues detected on the feature branch are added as merge request comments. The `BRIDGE_COVERITY_PRCOMMENT_IMPACTS` parameter can be used to filter comments by impact level, with a default of "High" if unset.

   For both scan scenarios the Coverity project and stream are automatically derived from built-in GitLab CI environment variables. The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   Uncomment the `bridge-logs` artifacts section to upload logs contained within the `.bridge` folder as a GitLab artifact.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Merge Request scanning**: Create a Merge Request targeting that branch. Merge Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Merge Request.

   Example review comment:

   [image: Merge Request review comments injected by Coverity Merge Request Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `BRIDGE_COVERITY_LOCAL` environment variable to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity Product Documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
