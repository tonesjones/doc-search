---
title: "Quickstart: Polaris Bridge CLI in a GitLab template"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-polaris-bridge-cli-in-a-gitlab-template.html"
content_id: "incuyObq1r6MXCPrzaD2~Q"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:01.227842+00:00"
---

# Quickstart: Polaris Bridge CLI in a GitLab template

As an alternative to the [Black Duck Security Scan Template](https://gitlab.com/blackduck-inc/black-duck-security-scan), the Bridge CLI can be downloaded and directly executed in a GitLab pipeline. It has all the functionality of the template, but you must add a step to [download the Bridge CLI from blackduck-repo](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/).

To find out more about the Black Duck Security Scan Template and what it can do, take a look at the overview page.

Note: You can use Black Duck Security Scan Template (recommended) for your workflow instead of Bridge CLI by following the quickstart guide: Quickstart: GitLab Template with Polaris

## Prerequisites

- In addition to a GitLab repo, you need Polaris access before you start this workflow.
- If the application doesn't already exist in Polaris, Bridge will try and create it before triggering a CI scan. If you have concurrent subscription / team member enabled, the application creation will be successful. If you have parallel subscription, application creation will fail. To create it manually consult [create the relevant applications in Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic).
- We recommend the following reading before you start:

  - The Black Duck Security Scan Template prerequisites page
  - Polaris prerequisites
  - Fix pull requests (Fix PRs)
  - Using SCA Fix PRs with Bridge
  - Reference: using the Black Duck Security Scan Template with Polaris
  - Additional GitLab Parameters

## Instructions

1. Add the following variables (GitLab → Project → Settings → CI/CD → Variables)

   | Variable | Type | Description | Example |
   | --- | --- | --- | --- |
   | `BRIDGE_POLARIS_SERVERURL` | Variable | Polaris Server URL | <https://poc.polaris.synopsys.com> (or <https://poc.polaris.blackduck.com> after you [Migrate Polaris to the Black Duck domain](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ee117187a16710bb1231f1919c97c0ed.topic)) |
   | `BRIDGE_POLARIS_ACCESS_TOKEN` | Secret | Polaris Access Token. You can use either a user access token (created in the Polaris UI) or a service account token here. | `REPLACE_WITH_YOUR_TOKEN` |
   | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |

   Note: be sure to set the mask variable flag for BRIDGE_POLARIS_ACCESSTOKEN to avoid exposing it in CI logs
2. Add a [coverity.yaml](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cli/topics/options_reference.html) file in the project repository. (Uncompiled languages are detected and configured automatically).

   ```
   capture:
     build:
       clean-command: mvn -B clean
       build-command: mvn -B -DskipTests package
   ```

   Note: This example above uses Maven and showcases the contents of coverity.yaml. You can use Maven but you can also substitute your own build and clean commands by following these instructions: [Configuring Coverity Thin Client for use with Bridge CLI and Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/3d79ddc1d59ccc31d9e8859e179b61e7.topic).
3. Add a "security" stage to the list of stages to be executed in the CI pipeline

   ```
   stages:
     - build
     - test
     - security
     - deploy
   ```
4. Add the following to the CI pipeline.

   ```
   Polaris:
     stage: security
     variables:
       BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
       BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
       BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SAST,SCA'
       BRIDGE_POLARIS_APPLICATION_NAME: $CI_PROJECT_NAME
       BRIDGE_POLARIS_PROJECT_NAME: $CI_PROJECT_NAME
       BRIDGE_POLARIS_BRANCH_NAME: $CI_COMMIT_REF_NAME
       BRIDGE_GITLAB_REPOSITORY_NAME: $CI_PROJECT_ID
       BRIDGE_GITLAB_REPOSITORY_BRANCH_NAME: $CI_COMMIT_REF_NAME
       BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
       BRIDGE_POLARIS_FIXPR_ENABLED: true
       SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/"
     rules:
       - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
         variables:
           BRIDGE_POLARIS_FIXPR_ENABLED: true: 'true'
           BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
       - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
         variables:
           BRIDGE_POLARIS_BRANCH_PARENT_NAME: $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
           BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'
           BRIDGE_GITLAB_REPOSITORY_PULL_NUMBER: $CI_MERGE_REQUEST_IID
     before_script:
       - apt-get -qq update && apt-get install -y curl unzip
     script:
       - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
       - /tmp/bridge-cli-bundle-linux64/bridge-cli --verbose --stage polaris
     #artifacts:
     #  name: "bridge-logs"
     #  when: always
     #  paths:
     #    - .bridge/
     #  expire_in: 30 days
   ```

   Fix pull requests are enabled to raise pull requests to upgrade dependencies for full scans of branches. See Fix pull requests (Fix PRs) and Using SCA Fix PRs with Bridge for further information and examples that demonstrate how to:
   - Configure order of preference for upgrade guidance
   - Raise Fix Pull Requests by severity
   - Enforce a maximum limit for the number of Fix Pull Requests created

   Note: This quickstart example configures SAST and SCA assessments. To configure DAST assessments, set the `BRIDGE_POLARIS_ASSESSMENT_TYPES` variable to `DAST`. Please refer to Using Bridge CLI With Polaris for DAST configuration requirements.

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
