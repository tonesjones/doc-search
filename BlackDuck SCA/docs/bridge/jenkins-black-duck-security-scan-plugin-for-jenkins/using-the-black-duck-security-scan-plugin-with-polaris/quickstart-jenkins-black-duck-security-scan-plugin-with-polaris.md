---
title: "Quickstart: Jenkins Black Duck Security Scan Plugin with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-jenkins-black-duck-security-scan-plugin-with-polaris.html"
content_id: "xdcjg22VAMpPXrRrY9MGBw"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:39.872707+00:00"
---

# Quickstart: Jenkins Black Duck Security Scan Plugin with Polaris

This quickstart explains how to set up a [Jenkins multibranch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/) for a Polaris project that will run a full scan and Pull Request scan. Pull Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments on the Pull Request. After the scan completes, appropriate security reports will be exported as Jenkins build artifacts.

## Prerequisites

- The following reading is recommended before starting the quickstart:
  - Jenkins Prerequisites
  - Polaris Prerequisites
  - Pull Request Comments
  - Fix Pull Requests
- Install the Black Duck Security Scan plugin to integrate with a Polaris server instance.
- Install and configure the appropriate Branch Source plugin to enable Jenkins to integrate with a source code repository and validate pull request events.
- Configure a source code management token to enable the Black Duck Security Scan plugin to inject Pull Request review comments for new security issues uncovered during a Pull Request scan.
- Access to a [Jenkins Multibranch Pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) project.
- Important: The following Black Duck Security Scan Plugin parameters are required to run a Pull Request scan and inject review comments. These are included in this quickstart example and listed in the table below. A Pull Request scan will not run if these parameters and quickstart prerequisites are not configured. This includes providing a source code management token to allow review comments to be added by the plugin.

  | **Parameter** | **Description** | **Example** |
  | --- | --- | --- |
  | `polaris_application_name` | The name of the Polaris application. For users that do not have a concurrent license this should be created before running the pipeline. | "application-$REPOSITORY_NAME" |
  | `polaris_project_name` | The Polaris project name. | `"$REPOSITORY_NAME"` |
  | `polaris_prComment_enabled` | When `true`, this enables Pull Request comments. | `"true"` |

  Note: The Black Duck Security Scan Plugin integrates with Polaris via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Polaris uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
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
           PRSCAN = "${env.CHANGE_TARGET ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
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
           stage('Polaris') {
               when {
                   anyOf {
                       environment name: 'FULLSCAN', value: 'true'
                       environment name: 'PRSCAN', value: 'true'
                   }
               }
               steps {
                   security_scan product: 'polaris',
                       polaris_assessment_types: 'SAST,SCA',
                       polaris_application_name: "spears-$REPO_NAME",
                       polaris_project_name: "$REPO_NAME",
                       polaris_prComment_enabled: true,
                       polaris_fixpr_enabled: true,
                       polaris_reports_sarif_create: true,
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

   The pipeline above will trigger one of the following security scans, depending upon the `FULLSCAN` and `PRSCAN` variables:

   - **Full scan**: A full scan is triggered by a push or merge event to a predefined set of branches, defined in the `FULLSCAN` environmental variable. In this scenario the [Black Duck Security Scan Plugin](https://plugins.jenkins.io/blackduck-security-scan/) will exhibit the following behavior:
     - SAST and SCA assessments will be performed. To enable DAST assessment, set the `polaris_assessment_types` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - Fix pull requests are enabled to raise Pull Requests to upgrade dependencies for full scans of branches. See Fix pull requests (Fix PRs) and Multibranch pipeline for further information and examples that demonstrate how to:
       - Configure order of preference for upgrade guidance
       - Raise Fix Pull Requests by severity
       - Enforce a maximum limit for the number of Fix Pull Requests created.
     - SARIF reporting is enabled. This will automatically upload the SARIF report as a Jenkins build artifact.
   - **Pull Request scan**: A Pull Request scan is triggered for push events on Pull Requests, where the target branch matches any of the branches defined in the `PRSCAN` variable. This behavior is activated by setting the `polaris_prComment_enabled` variable to `true`. In this scenario the Black Duck Security Scan Plugin will exhibit the following behavior:
     - A scan is executed to perform a differential analysis between the Pull Request and its parent branch.
     - The source code management token created in the prerequisites will be used to inject Pull Request review comments for new security issues detected since the last full scan of the parent branch.
     - SAST and SCA assessments will be performed. To enable DAST assessment, set the `polaris_assessment_types` parameter to `DAST`. Please refer to Using Bridge CLI With Polaris for configuration details.
     - A SARIF report will not be created since this is a Pull Request scan.

   It can be seen from the example above that, for both scans, the Jenkins build result status will be marked as `UNSTABLE` when policy violations are detected.

   If the `include_diagnostics` parameter is set to `true` then the Bridge CLI logs contained within the `.bridge` folder will be uploaded as a Jenkins build artifact to enable access to logs and diagnostics. Once the build completes, these can be downloaded from the `Artifacts` section within the build's `Status` page.
2. Once the Jenkinsfile has been saved and pushed to source code repository branches then a full scan should be performed, e.g. on the `main`, `develop` or `production` branch. At this point it should be possible to view issues uncovered by the full scan within Polaris. Furthermore, it should then be possible to run a Polaris Pull Request scan and inject review comments for new issues uncovered.

   [image: GitLab Merge Request with review comments injected]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Important: Request validation failed: No concurrent entitlements found for the tenant.

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the pipeline, consult [create an application in](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) Polaris.

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- Jenkins - Black Duck Security Scan Plugin for Jenkins
- [Black Duck Security Scan Plugin for Jenkins](https://plugins.jenkins.io/blackduck-security-scan/)
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
