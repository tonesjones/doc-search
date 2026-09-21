---
title: "Quickstart: Jenkins Black Duck Security Scan Plugin with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-jenkins-black-duck-security-scan-plugin-with-coverity.html"
content_id: "t9zP9noMBs_q34xmF57Xeg"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:45.579416+00:00"
---

# Quickstart: Jenkins Black Duck Security Scan Plugin with Coverity

This quickstart explains how to set up a [Jenkins multibranch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/) to run a Coverity full scan and Pull Request scan for branches in a repository. The quickstart explains how to achieve this for languages with and without a build system such as `make` or `Maven`.

The full scan will be triggered by push and merge events on specified branches. Full scan issues that violate a policy view will be uploaded to a Coverity Connect instance as a snapshot within a stream. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target specific branches. Pull Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

## Prerequisites

- The following reading is recommended before starting the quickstart:
  - Jenkins Prerequisites
  - Using the Black Duck Security Scan Plugin with Coverity
  - PR Comments
  - Using Fail Pull Requests With Coverity
- Install the Black Duck Security Scan plugin to integrate with a Coverity Connect instance.
- Install and configure the appropriate Branch Source plugin to enable Jenkins to integrate with a source code repository and validate pull request events.
- Configure a source code management token to enable the Black Duck Security Scan plugin to inject Pull Request review comments for new security issues uncovered during a Pull Request scan.
- Access to a [Jenkins Multibranch Pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) project.
- Warning: Please note that the following Black Duck Security Scan Plugin parameters are required to run a Pull Request scan and inject review comments. These are included in this quickstart example and listed in the table below. A Pull Request scan will not run if these parameters and quickstart prerequisites are not configured. This includes providing a source code management token to allow review comments to be added by the plugin.

  | **Parameter** | **Description** | **Example** |
  | --- | --- | --- |
  | `coverity_project_name` | The name of the Coverity Connect project. | `"$REPOSITORY_NAME"` |
  | `coverity_stream_name` | The Coverity Connect stream name that stores scan snapshots. | `"$REPOSITORY_NAME-$BRANCH_NAME"` |
  | `coverity_prComment_enabled` | When `true`, this enables Pull Request comments. | `"true"` |

  Note: The Black Duck Security Scan Plugin integrates with Coverity via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.
- Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge With Compiled Languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

1. Create a `Jenkinsfile` in the root of the source repository for all branches.

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
           stage('Coverity') {
               when {
                   anyOf {
                       environment name: 'FULLSCAN', value: 'true'
                       environment name: 'PRSCAN', value: 'true'
                   }
               }
               steps {
                   security_scan product: 'coverity',
                       coverity_project_name: "$REPO_NAME",
                       coverity_stream_name: "$REPO_NAME-$BRANCH_NAME",
                       coverity_args: "-o commit.connect.description=$BUILD_TAG",
                       coverity_policy_view: 'Outstanding Issues',
                       coverity_prComment_enabled: true,
                       
                       // Uncomment the coverity_prComment_impacts line below to
                       // add comments for issues filtered by impact. Default is High if unset
                       // NOTE: Issues matching coverity_policy_view are ignored if set
                       // coverity_prComment_impacts: 'High'
                       
                       // Uncomment the coverity_local line below if using traditional Coverity deployments or 
                       // Cloud Native Coverity (CNC) with scan services disabled
                       // coverity_local: true,
                       
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

   Warning: For deployments with [scan_services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) disabled or Coverity versions < 2022.3 the `coverity_local` line in the example should be uncommented. Subsequently, the full Coverity client will be used to enable a local analysis to be performed. This will override the default behavior that uses the Coverity thin client to capture and upload artifacts, with analysis being performed on the server.

   In the example above the Black Duck Security Scan Plugin will download and use the Coverity CLI to scan the codebase of the branch that triggered the pipeline. Branches are defined in the `FULLSCAN` environment variable. Any issues that violate the *Outstanding Issues* policy view will be uploaded to a Coverity stream within a Coverity Connect project that is named after the repository. If the project doesn’t already exist, it is created automatically.

   The Coverity stream is named using the format `repository-name-branch-name` and stores a snapshot of the issues identified during the scan, ready for review in Coverity Connect. The Jenkins build tag is used to identify the snapshot.

   Each time code is committed to a Pull Request branch that targets one of the specified base branches (defined in the `PRSCAN` variable), a comparison is performed between the scan of the Pull Request branch and the latest full scan of its parent branch. New issues introduced by the Coverity Fail Pull Request are automatically added as review comments. This behavior is enabled by setting the `coverity_prComment_enabled` parameter to *true*. The source code management token created in the prerequisites is required to inject Pull Request review comments. Use the `coverity_prComment_impacts` parameter to add comments filtered by impact, with a default of high if unset.

   It can be seen from the example above that the Jenkins build result status will be marked as `UNSTABLE` when policy view violations are detected.

   If the `include_diagnostics` parameter is set to `true` then the Bridge CLI logs contained within the `.bridge` folder will be uploaded as a Jenkins build artifact to enable access to logs and diagnostics. Once the build completes, these can be downloaded from the `Artifacts` section within the build's `Status` page.
2. Once the Jenkinsfile has been saved and pushed to source code repository branches then a full scan should be performed, e.g. on the `main`, `develop` or `production` branch. At this point it should be possible to view issues uncovered by the full scan within Coverity Connect. Furthermore, it should then be possible to open a Pull Request to run a Coverity Pull Request scan and inject review comments for new issues uncovered.

   [image: GitLab Merge Request with review comments injected]

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then the `coverity_local` parameter should be uncommented in the quickstart code example.

Attention: ERROR: Failed to retrieve tool information details: Fetch tool information: received unexpected response status code '500' from Connect API

In this scenario either [scan services](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cnc/topics/scan_service.html) are not enabled or a Coverity version prior to 2022.3 is deployed. The default behavior is that the pipeline uses the Coverity thin client to upload artifacts, with the analysis performed at the server. Setting the `coverity_local` parameter to `true` enables the full analysis at the client. Subsequently, the scan and analysis will be performed locally on the Jenkins build agent. For further details relating to the different Coverity deployment models supported, please refer to [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html).

## Useful resources

- [Coverity Product Documentation](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/webhelp-files/help_center_start.html)
- [Coverity Tutorials](https://community.blackduck.com/s/article/coverity-tutorials)
- [Coverity Projects and Streams Tutorial](https://community.blackduck.com/s/article/Coverity-Tutorial-Projects-and-Streams)
- [Coverity Deployment Architecture](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/help-center/topics/deployment_architecture.html)
- [Black Duck Security Scan Plugin for Jenkins](https://plugins.jenkins.io/blackduck-security-scan/)
- Jenkins - Black Duck Security Scan Plugin for Jenkins
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
