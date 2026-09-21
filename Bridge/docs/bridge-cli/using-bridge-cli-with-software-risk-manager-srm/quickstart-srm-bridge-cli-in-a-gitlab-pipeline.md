---
title: "Quickstart: SRM Bridge CLI in a GitLab pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-srm-bridge-cli-in-a-gitlab-pipeline.html"
content_id: "UYVanktAPBINQ8VA3VRNEw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:27.364628+00:00"
---

# Quickstart: SRM Bridge CLI in a GitLab pipeline

As an alternative to the Black Duck Security Scan Template, the Bridge CLI can be downloaded and directly executed in a GitLab pipeline. This guide provides a ready-to-use pipeline and step-by-step instructions for integrating SRM scanning into your build process.

To use Bridge CLI directly from a GitLab pipeline, the correct Bridge CLI Software Risk Manager parameters must be passed directly inside the workflow. Appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Template (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Template and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - GitLab prerequisites
  - List of mandatory and optional parameters for SRM
  - Additional GitLab configuration
- For security reasons, it is advisable to use [GitLab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/) to store credentials and access tokens.
- Add the following variables and secrets in your GitLab project or group settings:

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `SRM_URL` | Project Variable | SRM server URL | `https://srm.example.com` |
  | `SRM_APIKEY` | Project Variable (masked / secret) | SRM API key | `YOUR_APIKEY` |
  | `BRIDGECLI_LINUX64` | Project Variable | Bridge CLI download URL for Linux | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |

Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge with compiled languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a GitLab pipeline that invokes Bridge CLI for SRM scans:

1. Create the `.gitlab-ci.yml` file containing the following pipeline:

   Note: For compiled languages, uncomment the following:
   - Maven build image
   - `BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND` parameters
   - `build`, `test` and `deploy` jobs
   - Build related variables, e.g. `MAVEN_OPTS` and `MAVEN_CLI_OPTS`
   - Build related cache paths, e.g. .m2/repository, target

   ```
   ## -----------------------------------------------------------------------------
   # NOTE: The commented lines below are for compiled languages (e.g., Java, C++).
   # If your project requires a build step, uncomment and adjust those lines.
   ## -----------------------------------------------------------------------------

   stages:
     # - build
     # - test
     - security
     # - deploy

   variables:
     SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"
     # MAVEN_OPTS: >-
     #   -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
     # MAVEN_CLI_OPTS: >-
     #   --batch-mode

   # cache:
   #   paths:
   #     - .m2/repository/
   #     - target/

   # image: maven:3-eclipse-temurin-21

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

   srm-bridge-cli:
     stage: security
     variables:
       BRIDGE_SRM_URL: $SRM_URL
       BRIDGE_SRM_APIKEY: $SRM_APIKEY
       BRIDGE_SRM_ASSESSMENT_TYPES: SAST,SCA
       BRIDGE_SRM_PROJECT_NAME: $CI_PROJECT_NAME
       BRIDGE_SRM_BRANCH_NAME: $CI_COMMIT_REF_NAME
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
     rules:
       - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH)
         variables:
           BRIDGE_SRM_BRANCH_PARENT: $CI_DEFAULT_BRANCH
       - if: $CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES
     before_script:
       - apt-get -qq update && apt-get -qq install curl file unzip
     script:
       - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
       - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage srm
     #artifacts:
     #  name: "bridge-logs"
     #  when: always
     #  paths:
     #    - .bridge/
     #  expire_in: 30 days
   ```

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans.

   The GitLab pipeline will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_URL` parameter, using a given API key, `BRIDGE_SRM_APIKEY`.

   The Software Risk Manager project will be created if it does not already exist and named with the GitLab project name. Similarily the SRM branch name is derived from the source branch name.

   A full scan, including SAST and SCA assessments, is triggered by push events for the branches defined in the `SCAN_BRANCHES` variable.

   Uncomment the `artifacts` section to upload logs and reports from the `.bridge` folder as GitLab artifacts. These artifacts can be accessed and downloaded from the pipeline's job page in GitLab (Project > Build > Jobs).
2. Run scans

   Once the workflow is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Test:** Monitor the output to verify that the SRM scan completes successfully and issues appear in SRM Dashboard.

## Troubleshooting and support

If errors are encountered during the pipeline run, ensure that all variables are set correctly and that the Bridge CLI can access the SRM server.

If a pipeline error is encountered similar to the example below, then it is likely that the `BRIDGE_SRM_BRANCH_PARENT` parameter has not been set.

Important: ERROR: Branch "develop" does not exist for the project and "srm.branch.parent" is empty but is required along with "srm.branch.name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, `stage` or `release`, the `BRIDGE_SRM_BRANCH_PARENT` parameter must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

For further troubleshooting, enable optional log archiving by uncommenting the `bridge-logs` artifacts section in the YAML file.

## Useful resources

- [SRM product documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
