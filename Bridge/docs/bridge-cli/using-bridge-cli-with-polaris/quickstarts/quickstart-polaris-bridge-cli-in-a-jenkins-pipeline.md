---
title: "Quickstart: Polaris Bridge CLI in a Jenkins pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-polaris-bridge-cli-in-a-jenkins-pipeline.html"
content_id: "awDfyMHa01fVMXoYt9X5aA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:02.275816+00:00"
---

# Quickstart: Polaris Bridge CLI in a Jenkins pipeline

As an alternative to the Black Duck Security Scan Plugin, Bridge CLI can be downloaded and directly executed in a Jenkins pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Polaris parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult Using Bridge CLI with Polaris for further details and instructions on use.

Note: You can use Black Duck Security Scan Plugin for Jenkins (recommended) for your workflow instead of Bridge CLI by following the quickstart guide: Quickstart: Jenkins Black Duck Security Scan Plugin with Polaris

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Jenkins Prerequisites
  - Polaris prerequisites
  - Pull Request Comments
  - Fix pull requests (Fix PRs)
  - Using SCA Fix PRs with Bridge
  - List Of Mandatory And Optional Parameters For Polaris
  - Additional Jenkins Parameters
- Administrative access to a GitHub repository.
- A Personal Access Token (PAT) is required to allow the pipeline to inject Pull Request review comments and raise Fix Pull Requests. The PAT should be generated for the SCM platform that Bridge CLI integrates with Polaris from within the Jenkins pipeline, e.g. GitHub, GitLab, Azure, Bitbucket etc.
- The Branch Source plugin must be installed for the appropriate platform to enable Jenkins to integrate with a source code repository and validate Pull Request events.
- For security reasons, it is advisable to use [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) to store sensitive information.
- Add the following credentials in Jenkins (Manage Jenkins > Manage Credentials > System > Global Credentials)

  | Credential ID | Type | Description | Example |
  | --- | --- | --- | --- |
  | `polaris-credentials` | Username with password | Polaris username and password | `REPLACE_WITH_YOUR_TOKEN` |
  | `scm-pat` | Secret text | SCM Platform Personal Access Token (e.g., GitHub, GitLab) | `REPLACE_WITH_YOUR_TOKEN` |
- Ensure the following environment variables are set correctly in the pipeline:

  | Variable | Description | Example |
  | --- | --- | --- |
  | `BRIDGECLI_LINUX64` | Bridge CLI Download URL | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
  | `BRIDGE_POLARIS_SERVERURL` | Polaris server URL. | `https://polaris.blackduck.com` |
  | `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token retrieved from Jenkins credentials. | `credentials('polaris-credentials')` |
  | `BRIDGE_POLARIS_APPLICATION_NAME` | Polaris application name. Defaults to the repository name if not specified. | `jenkins-quickstart-${env.REPO_NAME}` |
  | `BRIDGE_POLARIS_PROJECT_NAME` | Polaris project name. Defaults to the repository name if not specified. | `${env.REPO_NAME}` |
  | `BRIDGE_POLARIS_BRANCH_NAME` | Polaris branch name to scan. Defaults to the current branch name. | `$BRANCH_NAME` |
  | `BRIDGE_POLARIS_ASSESSMENT_TYPES` | Comma-separated list of assessment types to run. Supported values: `SAST`, `SCA`, `DAST`. | `SAST,SCA` |
  | `SCM_PAT` | SCM Platform Personal Access Token from Jenkins credentials. Required to inject Pull Request comments. | `credentials('scm-pat')` |
- The following Bridge CLI parameters are required to inject Pull Request comments:

  | Parameter | Description | Value |
  | --- | --- | --- |
  | `polaris.prcomment.enabled` | Enable Pull Request comments | `true` |
  | `github.repository.pull.number` | ID of Pull Request to scan | `$CHANGE_ID` |

  Note: Parameter `github.repository.pull.number` is specific to adding Pull Request Comments for GitHub. Refer to the SCM Pull Request comments table for the equivalent Bridge CLI parameter required for integrating with other SCM platforms.
- The `polaris.fixPR.enabled` parameter should be set to `true` to enable Bridge to raise Fix Pull Requests from scan findings on non Pull Request branches.

Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge With Compiled Languages and the Coverity section in Bridge Options to Configure Tools for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a Jenkins pipeline that invokes Bridge CLI for full scans and Pull Request scans:

1. Create a Jenkinsfile containing the following pipeline:

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - Tools configuration
   - Build stage
   - Build/clean command environment variables `BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND`.

   ```
   pipeline {
       agent { label 'node' }
       environment {
           ORG_NAME = "${env.GIT_URL.tokenize('/.')[-3]}"
           REPO_NAME = "${env.GIT_URL.tokenize('/.')[-2]}"
           FULLSCAN = "${env.BRANCH_NAME ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
           PRSCAN = "${env.CHANGE_TARGET ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
           BRIDGECLI_LINUX64 = 'https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip'
           BRIDGE_POLARIS_SERVERURL = 'https://polaris.server.blackduck.com'
           BRIDGE_POLARIS_ACCESSTOKEN = credentials('polaris-credentials')
           BRIDGE_POLARIS_APPLICATION_NAME = "jenkins-quickstart-${env.REPO_NAME}"
           BRIDGE_POLARIS_PROJECT_NAME = "${env.REPO_NAME}"
           BRIDGE_POLARIS_BRANCH_NAME = "$BRANCH_NAME"
           BRIDGE_POLARIS_ASSESSMENT_TYPES = 'SAST,SCA'
           // BRIDGE_COVERITY_BUILD_COMMAND = 'mvn -B -DskipTests package'
           // BRIDGE_COVERITY_CLEAN_COMMAND = 'mvn -B clean'
           SCM_PAT = credentials('scm-pat')
       }
       // tools {
       //    maven 'maven-3'
       //    jdk 'openjdk-21'
       // }
       stages {
           // stage('Build') {
           //    steps {
           //        sh 'mvn -B package'
           //    }
           // }
           stage('Polaris Full Scan') {
               when { environment name: 'FULLSCAN', value: 'true' }
               steps {
                   script {
                       status = sh returnStatus: true, script: '''
                           curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $WORKSPACE_TMP bridge.zip && rm -f bridge.zip
                           $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage polaris \
                               polaris.fixPR.enabled=true \
                               polaris.reports.sarif.create=true
                       '''
                       if (status == 8) { unstable 'policy violation' }
                       else if (status != 0) { error 'scan failure' }
                   }
               }
           }
           stage('Polaris PR Scan') {
               when { environment name: 'PRSCAN', value: 'true' }
               steps {
                   script {
                       status = sh returnStatus: true, script: '''
                           curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $WORKSPACE_TMP bridge.zip && rm -f bridge.zip
                           $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage polaris \
                               polaris.prcomment.enabled=true \
                               polaris.branch.parent.name=$CHANGE_TARGET \
                               github.repository.name=$REPO_NAME \
                               github.repository.branch.name=$BRANCH_NAME \
                               github.repository.owner.name=$ORG_NAME \
                               github.repository.pull.number=$CHANGE_ID \
                               github.user.token=$SCM_PAT
                       '''
                       if (status == 8) { unstable 'policy violation' }
                       else if (status != 0) { error 'scan failure' }
                   }
               }
           }
       }
       post {
           always {
               archiveArtifacts allowEmptyArchive: true, artifacts: '.bridge/bridge.log, .bridge/*/idir/build-log.txt'
               //zip archive: true, dir: '.bridge', zipFile: 'bridge-logs.zip'
               cleanWs()
           }
       }
   }
   ```

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans and Pull Request scans.

   A full scan is performed when code is pushed or merged to the `main`, `master`, `develop`, `stage` or `release` branches. Both SAST and SCA assessments are run:
   - Fix Pull Requests are raised to upgrade dependencies via the `polaris.fixPR.enabled=true` parameter.
   - A SARIF report is generated and saved as a build artifact via the `polaris.reports.sarif.create=true` parameter.
   - Issues that violate policy will mark the build as unstable (exit code 8); any other non-zero exit code fails the build.

   For Pull Requests targeting the `main`, `master`, `develop`, `stage` or `release` branches, Bridge CLI is invoked directly to perform a Pull Request scan to inject Pull Request comments for new issues introduced in the feature branch.

   Note: Parameters `github.repository.*` and `github.user.token` are specific to integrating Bridge CLI with GitHub Pull Requests. Refer to the SCM sections of Complete list of Bridge arguments for the equivalent Bridge CLI parameters required for integrating with other SCM platforms.

   The Polaris application name is set to the repository name prefixed with `jenkins-quickstart-`. The project name defaults to the repository name, and the branch name is derived from the Jenkins `BRANCH_NAME` environment variable, which reflects the branch that triggered the build.

   The post-build action archives individual Bridge CLI log files for troubleshooting and cleans the workspace for the next build. The commented zip action (requires [Pipeline Utility Steps](https://plugins.jenkins.io/pipeline-utility-steps/) plugin) provides an alternative to create a single compressed archive containing all Bridge logs.
2. Run Scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`) that include adding one or more outdated or vulnerable dependencies to trigger a Fix Pull Request.
      1. **Review results**: Check that the scan results include one or more automatically generated Fix Pull Requests.
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
      1. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: Merge request review comments injected by Jenkins Polaris merge request scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that the user credentials used to integrate with the Polaris server do not have a concurrent subscription.

Attention: Request Validation Failed: No concurrent entitlements found for the tenant

Automatic application creation will fail for users with a parallel subscription. To create the application manually before running the pipeline, consult [create an application in Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic).

## Useful resources

- [Polaris Product Documentation](https://polaris.blackduck.com/developer/default/)
- Jenkins - Black Duck Security Scan Plugin for Jenkins
- [Black Duck Security Scan Plugin for Jenkins](https://plugins.jenkins.io/blackduck-security-scan/)
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
