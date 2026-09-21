---
title: "Quickstart: Black Duck SCA Bridge CLI in a GitLab template"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-sca-bridge-cli-in-a-gitlab-template.html"
content_id: "NcDZM_K0VSPqoJiY~_yTSw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:15.116528+00:00"
---

# Quickstart: Black Duck SCA Bridge CLI in a GitLab template

As an alternative to the [Black Duck Security Scan Template](https://gitlab.com/blackduck-inc/black-duck-security-scan), the Bridge CLI can be downloaded and directly executed in a GitLab CI/CD pipeline. It has all the functionality of the template, but requires an additional step to [download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Black Duck® SCA parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Template (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The template has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Template and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitLab prerequisites
  - Pull Request comments
  - Fix Pull Requests
  - List of mandatory and optional parameters for Black Duck SCA
  - Additional GitLab parameters
- Admin access to a GitLab repository.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A [GitLab Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) is required to allow the pipeline to inject Merge Request review comments.
- For security reasons, it is advisable to use [GitLab CI/CD Variables](https://docs.gitlab.com/ee/ci/variables/) to store credentials and access tokens. It is recommended that the variables are added as project variables. Group variable inheritance can cause scans to fail under certain conditions.
- Add the following variables and secrets at the project level (GitLab > Project > Settings > CI/CD > Variables)

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BLACKDUCK_URL` | Variable | Black Duck SCA Server URL | `https://blackduck.example.com` |
  | `BLACKDUCK_API_TOKEN` | Masked Variable | Black Duck SCA API Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `GITLAB_USER_TOKEN` | Masked Variable | GitLab Personal Access Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- The following Bridge CLI parameters are required to inject Merge Request comments and raise fix Merge Requests:

  | Parameter | Description | Value | Scan type |
  | --- | --- | --- | --- |
  | `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` | Raise Fix MRs for detected vulnerabilities | `true` | Full |
  | `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` | Enable MR comments | `true` | MR |
  | `BRIDGE_GITLAB_REPOSITORY_PULL_NUMBER` | ID of MR with source code to scan | `$CI_MERGE_REQUEST_IID` |

## Instructions

1. Add the following pipeline configuration to your repository at `.gitlab-ci.yml`.

   Note: For compiled languages, uncomment the build, test, and deploy stages, along with the Maven configuration and Docker image sections. Adjust the build commands and image to align with project specific build tools and requirements, such as Maven, Gradle, or other build systems.

   ```
   stages:
     # Uncomment the build, test, and deploy stages below for compiled languages
     # - build
     # - test
     - security
     # - deploy

   variables:
     SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
     # Uncomment the Maven configuration below for compiled languages
     # MAVEN_OPTS: >-
     #   -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
     # MAVEN_CLI_OPTS: >-
     #   --batch-mode

   # Uncomment the cache section below for compiled languages
   # cache:
   #   paths:
   #     - .m2/repository/
   #     - target/

   # Uncomment the image section below for compiled languages
   # image: maven:3-eclipse-temurin-21

   # Uncomment the build stage below for compiled languages
   # build:
   #   stage: build
   #   script: mvn -B compile

   # Uncomment the test stage below for compiled languages
   # test:
   #   stage: test
   #   script: mvn -B test

   # Uncomment the deploy stage below for compiled languages
   # deploy:
   #   stage: deploy
   #   only:
   #     variables:
   #       - $CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES
   #   script: mvn -B install

   bd-bridge-cli:
     stage: security
     variables:
       BRIDGE_BLACKDUCKSCA_URL: $BLACKDUCK_URL
       BRIDGE_BLACKDUCKSCA_TOKEN: $BLACKDUCK_API_TOKEN
       BRIDGE_GITLAB_REPOSITORY_NAME: $CI_PROJECT_ID
       BRIDGE_GITLAB_REPOSITORY_BRANCH_NAME: $CI_COMMIT_REF_NAME
       BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
       DETECT_PROJECT_NAME: $CI_PROJECT_NAME
     rules:
       - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
         variables:
           BRIDGE_BLACKDUCKSCA_SCAN_FULL: true
           BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: BLOCKER
           BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: true
           BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
           DETECT_PROJECT_VERSION_NAME: $CI_COMMIT_REF_NAME
           DETECT_CODE_LOCATION_NAME: $CI_PROJECT_NAME-$CI_COMMIT_REF_NAME
       - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
         variables:
           BRIDGE_BLACKDUCKSCA_SCAN_FULL: false
           BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: true
           BRIDGE_GITLAB_REPOSITORY_PULL_NUMBER: $CI_MERGE_REQUEST_IID
           DETECT_PROJECT_VERSION_NAME: $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
           DETECT_CODE_LOCATION_NAME: $CI_PROJECT_NAME-$CI_MERGE_REQUEST_TARGET_BRANCH_NAME
     before_script:
       - apt-get -qq update && apt-get -qq install curl unzip
     script:
       - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
       - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca
     #artifacts:
     #  name: "bridge-logs"
     #  when: always
     #  paths:
     #    - .bridge/
     #  expire_in: 30 days
   ```

   The pipeline will download Bridge CLI from the URL contained in the `BRIDGECLI_LINUX64` environment variable for direct execution in the pipeline. One of the following Black Duck SCA scans will be triggered depending on the event type:
   - **Full Scan**: Triggered by push events to the specified branches (main, master, develop, stage, release). This scan:
     - Performs a complete SCA assessment of all dependencies
     - Creates a SARIF report for security findings
     - Enables fix Merge Request generation for vulnerable dependencies
     - Fails the build on BLOCKER severity vulnerabilities
   - **Merge Request Scan**: Triggered for Merge Request events targeting the specified branches. This scan:
     - Performs a differential analysis between the Merge Request and target branch
     - Automatically adds review comments for new vulnerabilities introduced in the Merge Request
     - Uses the target branch as the baseline for comparison

   Note: To enable diagnostic logging, uncomment the "artifacts" section at the end of the pipeline configuration. This will upload Bridge CLI logs as pipeline artifacts for troubleshooting purposes.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: Merge request review comments injected by SCA merge request scan]

## Useful resources

- [Black Duck product documentation](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic&Version=latest)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
