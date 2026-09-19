---
title: "Quickstart: Coverity Bridge CLI in a Jenkins pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-coverity-bridge-cli-in-a-jenkins-pipeline.html"
content_id: "D_ymOD7ePOPDqiji8LrA3w"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:22.597905+00:00"
---

# Quickstart: Coverity Bridge CLI in a Jenkins pipeline

As an alternative to the Black Duck Security Scan Plugin, the Bridge CLI can be downloaded and directly executed in a Jenkins pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Coverity parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Plugin plugin (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Security Scan plugin and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Jenkins Prerequisites
  - Pull Request Comments
  - Using Fail Pull Requests With Coverity
  - List of Mandatory and Optional Parameters For Coverity
  - Additional Jenkins configuration
- Administrative access to a GitHub repository.
- A Personal Access Token (PAT) is required to allow the pipeline to inject Pull Request review comments. The PAT should be generated for the SCM platform that Bridge CLI integrates with from within the Jenkins pipeline, e.g. GitHub, GitLab, Azure, Bitbucket etc.
- The Branch Source plugin must be installed for the appropriate platform to enable Jenkins to integrate with a source code repository and validate pull requests events.
- For security reasons, it is advisable to use [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) to store sensitive information.
- Add the following credentials in Jenkins (Manage Jenkins > Manage Credentials > System > Global Credentials)

  | Credential ID | Type | Description | Example |
  | --- | --- | --- | --- |
  | `coverity-credentials` | Username with password | Coverity username and password | `YOUR_CREDENTIALS` |
  | `scm-pat` | Secret text | SCM Platform Personal Access Token (e.g., GitHub, GitLab) | `YOUR_TOKEN` |
- Ensure the following environment variables are set correctly in the pipeline:

  | Variable | Description | Example |
  | --- | --- | --- |
  | `BRIDGECLI_LINUX64` | Bridge CLI Download URL | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
  | `BRIDGE_COVERITY_CONNECT_URL` | Coverity Connect Server URL | `https://cov.server.blackduck.com` |
  | `BRIDGE_COVERITY_CONNECT_USER_NAME` | Coverity Connect Username | `YOUR_USERNAME` |
  | `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` | Coverity Connect Password | `YOUR_PASSWORD` |
  | `SCAM_PAT` | SCM Platform Personal Access Token from Jenkins credentials. Required to inject Pull Request comments. | `credentials('scm-pat')` |
- The following Bridge CLI parameters are required to inject Pull Request comments:

  | Parameter | Description | Value |
  | --- | --- | --- |
  | `coverity.prcomment.enabled` | Enable PR comments | `true` |
  | `github.repository.pull.number` | ID of PR to scan | `$CHANGE_ID` |

  Note: Parameter `github.repository.pull.number` is specific to adding Pull Request Comments for GitHub. Refer to the SCM Pull Request comments table for the equivalent Bridge CLI parameter required for integrating with other SCM platforms.

Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See  Using Bridge With Compiled Languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a Jenkins pipeline that invokes Bridge CLI for full scans and Pull Request scans:

1. Create a `Jenkinsfile` containing the following pipeline:

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
           BRIDGECLI_LINUX64 = 'https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip'
           BRIDGE_COVERITY_CONNECT_URL = 'https://coverity.server.blackduck.com'
           COVERITY_CREDENTIALS = credentials('coverity-credentials')
           BRIDGE_COVERITY_CONNECT_USER_NAME = "${env.COVERITY_CREDENTIALS_USR}"
           BRIDGE_COVERITY_CONNECT_USER_PASSWORD = "${env.COVERITY_CREDENTIALS_PSW}"
           // BRIDGE_COVERITY_BUILD_COMMAND = 'mvn -B -DskipTests package'
           // BRIDGE_COVERITY_CLEAN_COMMAND = 'mvn -B clean'
           // BRIDGE_COVERITY_LOCAL = true
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
           stage('Coverity Full Scan') {
               when { environment name: 'FULLSCAN', value: 'true' }
               steps {
                   script {
                       status = sh returnStatus: true, script: '''
                           curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $WORKSPACE_TMP bridge.zip && rm -f bridge.zip
                           $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage connect \
                               coverity.connect.project.name=$REPO_NAME \
                               coverity.connect.stream.name=$REPO_NAME-$BRANCH_NAME \
                               coverity.connect.policy.view='Outstanding Issues' \
                               coverity.args="-o commit.connect.description=$BUILD_TAG"
                       '''
                       if (status == 8) { unstable 'policy violation' }
                       else if (status != 0) { error 'scan failure' }
                   }
               }
           }
           stage('Coverity PR Scan') {
               when { environment name: 'PRSCAN', value: 'true' }
               steps {
                   script {
                       status = sh returnStatus: true, script: '''
                           curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $WORKSPACE_TMP bridge.zip && rm -f bridge.zip
                           $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage connect \
                               coverity.connect.project.name=$REPO_NAME \
                               coverity.connect.stream.name=$REPO_NAME-$CHANGE_TARGET \
                               coverity.prcomment.enabled=true \
                               # Use the parameter below to add comments for issues filtered \
                               # by impact. Default is High if unset \
                               # NOTE: Issues matching coverity.connect.policy.view are ignored if set \
                               # coverity.prcomment.impacts='High' \
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

   Note: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed with the full toolkit. This will override the default behaviour that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans and Pull Request scans.

   A full scan is performed when code is pushed or merged to the `main`, `master`, `develop`, `stage` or `release` branches. The Coverity analysis is tagged with the Jenkins build identifier, providing build traceability for security findings. The `coverity.connect.policy.view` parameter is configured to break the build if new or outstanding issues are detected as defined by the Outstanding Issues [policy view](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_issues_by_snapshot.html) (see [View Management](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/view_management.html) for details).

   For Pull Requests targeting those branches, Bridge CLI is invoked directly to perform a Pull Request scan to inject Pull Request comments for new issues introduced in the feature branch. Uncomment the `coverity.prcomment.impacts` parameter to inject comments filtered by impact level, with a default of "High" if unset.

   Note: Parameters `github.repository.*` and `github.user.token` are specific to integrating Bridge CLI with GitHub Pull Requests. Refer to the SCM Pull Request comments table for the equivalent Bridge CLI parameters required for integrating with other SCM platforms.

   The Coverity project and stream are automatically derived from built-in Jenkins environment variables and Git repository information. The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect.

   The post-build action archives individual Bridge CLI log files for troubleshooting and cleans the workspace for the next build. The commented zip action (requires [Pipeline Utility Steps](https://plugins.jenkins.io/pipeline-utility-steps/) plugin) provides an alternative to create a single compressed archive containing all Bridge logs.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: PR review comments injected by Coverity PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `BRIDGE_COVERITY_LOCAL` environment variable should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `BRIDGE_COVERITY_LOCAL` environment variable to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally by the workflow. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity Product Documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- Bridge product overview
- Jenkins Security Scan Plugin for Coverity
