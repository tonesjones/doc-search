---
title: "Quickstart: Jenkins Black Duck Security Scan Plugin with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-jenkins-black-duck-security-scan-plugin-with-software-risk-manager.html"
content_id: "rUzKTr2ruGYBZhX~LoEyIg"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:48.067240+00:00"
---

# Quickstart: Jenkins Black Duck Security Scan Plugin with Software Risk Manager

This quickstart explains how to set up a [Jenkins multibranch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/) for a Software Risk Manager project that will run a full scan, triggered by push and merge events on specified branches.

After the scan completes diagnostic logs will be exported as Jenkins build artifacts.

Important: Please note that scanning Pull Requests and injecting review comments is not currently supported for pipelines that integrate the Black Duck Security Scan Plugin with Software Risk Manager.

## Prerequisites

- The following reading is recommended before starting the quickstart:
  - Jenkins Prerequisites
- Install the Black Duck Security Scan plugin to integrate with a Software Risk Manager server instance.
- Install and configure the appropriate Branch Source plugin to enable Jenkins to integrate with a source code repository and validate pull request events.
- Access to a [Jenkins Multibranch Pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) project.
- Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge With Compiled Languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

1. Create a `Jenkinsfile` in the root of a source repository for all branches.

   Note: For compiled languages, uncomment:
   - `tools` section
   - `Build` stage
   - `coverity_build_command` and `coverity_clean_command` parameters.

   ```
   pipeline {
       agent { label 'node' }
       environment {
           REPO_NAME = "${env.GIT_URL.tokenize('/.')[-2]}"
           FULLSCAN = "${env.BRANCH_NAME ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
       }
       // Uncomment the tools section below for compiled languages
       // tools {
       //     maven 'maven-3'
       //     jdk 'openjdk-21'
       // }
       stages {
           // Uncomment the Build stage below for compiled languages
           // stage('Build') {
           //     steps {
           //         sh 'mvn -B package'
           //     }
           // }
           stage('SRM') {
               when {
                   anyOf {
                       environment name: 'FULLSCAN', value: 'true'
                   }
               }
               steps {
                   security_scan product: 'srm',
                       srm_assessment_types: 'SAST,SCA',
                       srm_project_name: "$REPO_NAME",
                       srm_branch_name: "$BRANCH_NAME",
                       // Uncomment the build and clean commands below for compiled languages
                       // coverity_build_command: 'mvn -B -DskipTests package',
                       // coverity_clean_command: 'mvn -B clean',
                       include_diagnostics: false,
                       mark_build_status: 'UNSTABLE'
               }
           }
       }
       post {
           always {
               cleanWs()
           }
       }
   }
   ```

   The pipeline above will trigger a full scan for a push or merge event to a predefined set of branches, defined in the the `FULLSCAN` environmental variable. In this scenario the [Black Duck Security Scan Plugin](https://plugins.jenkins.io/blackduck-security-scan/) will exhibit the following behavior:

   - Artifacts and issues will stored in a Software Risk Manager project named after the source code repository. The branch name will be set to the name of the branch that triggered the build. If it does not already exist it will be created.
   - SAST and SCA assessments will be performed.

   It can be seen from the example above that the Jenkins build result status will be marked as `UNSTABLE` when policy violations are detected.

   If the `include_diagnostics` parameter is set to `true` then the Bridge CLI logs contained within the `.bridge` folder will be uploaded as a Jenkins build artifact to enable access to logs and diagnostics. Once the build completes, these can be downloaded from the `Artifacts` section within the build's `Status` page.

   Note: The Black Duck Security Scan Plugin integrates with Software Risk Manager via Bridge CLI. Additional scan configuration options not available through the plugins's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
2. Once the Jenkinsfile has been saved and pushed to source code repository branches then a full scan should be performed, e.g. on the `main`, `develop` or `production` branch. At this point it should be possible to view issues uncovered by the full scan within Software Risk Manager.

## Useful resources

- [Software Risk Manager Product Documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Jenkins - Black Duck Security Scan Plugin for Jenkins
- [Black Duck Security Scan Plugin for Jenkins](https://plugins.jenkins.io/blackduck-security-scan/)
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
