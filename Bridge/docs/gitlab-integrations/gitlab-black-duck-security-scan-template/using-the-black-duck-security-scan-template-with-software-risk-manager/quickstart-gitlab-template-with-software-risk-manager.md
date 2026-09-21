---
title: "Quickstart: GitLab Template with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-gitlab-template-with-software-risk-manager.html"
content_id: "j64fe2dvddV8CqJ282qvmw"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:11.102295+00:00"
---

# Quickstart: GitLab Template with Software Risk Manager

This quickstart explains how to set up the Black Duck Security Scan Template to integrate with a SRM project to run a full scan, triggered by push and merge events on specified branches.

After the scan completes diagnostic logs will be exported as GitLab build artifacts.

Important: Please note that scanning Merge Requests, injecting review comments and creating SARIF reports is not currently supported for pipelines that integrate the Black Duck Security Scan Template with Software Risk Manager.

## Prerequisites

- The following reading is recommended:
  - GitLab prerequisites
  - Using the Black Duck Security Scan Template with Software Risk Manager
  - Additional GitLab configuration
- Access to a GitLab repository with admin access.
- Access to a Software Risk Manager (SRM) server instance.
- An SRM role that allows creation of authentication tokens.
- An [SRM API Key](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/c0c649ef7edc139d4ff29abca83c9855.topic) to enable the Black Duck Security Scan Template to integrate with the Software Risk Manager instance.
- For security reasons, it is advisable not to store credentials directly in the workflow. The recommended approach is to use masked and hidden variables.

  Important: It is adviseable that the variables are added as project variables. Group variable inheritance can cause scans to fail under certain conditions. Be sure to set the mask variable flag for `SRM_API_KEY` to avoid exposure in the CI logs.
- Add the following secrets and variables (GitLab > Project sidebar > Settings > CI/CD > Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `SRM_URL` | Masked | Software Risk Manager Server URL | `https://srm.blackduck.com` |
  | `SRM_API_KEY` | Masked and hidden | Software Risk Manager API Key | `A_SRM_API_KEY` |
- Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge With Compiled Languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure the Black Duck Security Scan Template to run a full scan:

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

   srm:
     stage: security
     variables:
       BRIDGE_SRM_URL: $SRM_URL
       BRIDGE_SRM_APIKEY: $SRM_API_KEY
       BRIDGE_SRM_ASSESSMENT_TYPES: "SAST,SCA"
       BRIDGE_SRM_PROJECT_NAME: $CI_PROJECT_NAME
       BRIDGE_SRM_BRANCH_NAME: $CI_COMMIT_REF_NAME
       # BRIDGE_COVERITY_BUILD_COMMAND and BRIDGE_COVERITY_CLEAN_COMMAND (uncomment and configure for compiled languages)
       # BRIDGE_COVERITY_BUILD_COMMAND: mvn -B -DskipTests package
       # BRIDGE_COVERITY_CLEAN_COMMAND: mvn -B clean
       # INCLUDE_DIAGNOSTICS: true
     rules:
       - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH)
         variables:
           BRIDGE_SRM_BRANCH_PARENT: $CI_DEFAULT_BRANCH
       - if: $CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES
     before_script:
       - apt-get -qq update && apt-get install -y curl file unzip
     extends: .run-black-duck-tools
     #artifacts:
     #  name: "bridge-logs"
     #  when: always
     #  paths:
     #    - .bridge/
     #  expire_in: 30 days
   ```

   In the example above the GitLab Template will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_URL` parameter, using a given API key, `BRIDGE_SRM_APIKEY`. By default a Software Risk Manager project is created before the full scan runs, with a name matching the name of the source repository.

   If a full scan is triggered for a branch that is not the default branch, then the pipeline sets the parent branch (`BRIDGE_SRM_BRANCH_PARENT`) to the default branch. This helps ensure that non-default branches reference the default branch as their base during scanning operations.

   A full scan, including SAST and SCA assessments, will then be triggered by push events for any of the branches defined in the `SCAN_BRANCHES` variable.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports from the `.bridge` folder as GitLab artifacts. These artifacts can be accessed and downloaded from the pipeline's job page in GitLab (Project > Build > Jobs).

   Note: The Black Duck Security Scan Template integrates with Software Risk Manager via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
2. Push a new commit to the source repository to run the pipeline. Alternatively, trigger a manual run by navigating to GitLab Project Sidebar > Build > Pipelines > Run Pipeline. The results of the full scan will be available in the Software Risk Manager Dashboard.

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that organization firewall rules maybe restricting access to the template.

Attention: Unable to create pipeline Project `blackduck-inc/black-duck-security-scan` not found or access denied! Make sure any includes in the pipeline configuration are correctly defined.

The recommended solution is to check that the template is referenced correctly and then perform one of the following actions:

- Arrange access with the organization's IT department.
- Use a GitLab self managed runner.

## Useful resources

- [Software Risk Manager Product Documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- Using Bridge CLI
