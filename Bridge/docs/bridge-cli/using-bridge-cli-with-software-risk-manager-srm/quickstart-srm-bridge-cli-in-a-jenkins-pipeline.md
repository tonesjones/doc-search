---
title: "Quickstart: SRM Bridge CLI in a Jenkins pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-srm-bridge-cli-in-a-jenkins-pipeline.html"
content_id: "eZIBNcbcaLZFkh6roQhMOw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:28.081140+00:00"
---

# Quickstart: SRM Bridge CLI in a Jenkins pipeline

As an alternative to the Black Duck Security Scan Plugin for Jenkins, the Bridge CLI can be downloaded and directly executed in a Jenkins pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use Bridge CLI directly from a Jenkins pipeline, the correct Bridge CLI Software Risk Manager parameters must be passed directly inside the pipeline. Furthermore, appropriate access credentials are required to download and use it. Consult Using Bridge CLI with Software Risk Manager (SRM) for further details and instructions on use.

Note: The Black Duck Security Scan Plugin for Jenkins (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide: Quickstart: Jenkins Black Duck Security Scan Plugin with Software Risk Manager. The Black Duck Security Scan Plugin for Jenkins has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Plugin for Jenkins and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:
  - Jenkins prerequisites
  - List of mandatory and optional parameters for SRM
  - Additional Jenkins configuration
- The Branch Source plugin must be installed for the appropriate platform to enable Jenkins to integrate with a source code repository.
- For security reasons, it is advisable to use [Jenkins credentials](https://www.jenkins.io/doc/book/using/using-credentials/) to store sensitive information.
- Add the following credentials in Jenkins (Manage Jenkins > Manage Credentials > System > Global Credentials)

  | Credential ID | Type | Description | Example |
  | --- | --- | --- | --- |
  | `srm-apikey` | Secret text | SRM API Key | `YOUR_TOKEN` |
- Ensure the following environment variables are set correctly in the pipeline:

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_SRM_SERVERURL` | Variable | SRM server URL | `https://srm.server.blackduck.com` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI download URL for Linux | <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |

Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.

- The instructions below use the Bridge `COVERITY_BUILD_COMMAND` and `COVERITY_CLEAN_COMMAND` environment variables to specify the build and clean commands.
- See Using Bridge with compiled languages and the Coverity section in Client scan tool parameters for an overview of the various methods available for configuring Bridge CLI to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

Follow the steps below to configure a Jenkins pipeline that invokes Bridge CLI for SRM scans:

1. Add the following Jenkinsfile to the project repository

   Note: For compiled languages, uncomment the following and modify with appropriate settings for the target language:
   - `tools` section (e.g., Maven, JDK)
   - `Build` stage
   - Build/clean command environment variables (`BRIDGE_COVERITY_BUILD_COMMAND` and `BRIDGE_COVERITY_CLEAN_COMMAND`).

   ```
   // -----------------------------------------------------------------------------
   // NOTE: The commented lines below are for compiled languages (e.g., Java, C++).
   // If your project requires a build step, uncomment and adjust those lines.
   // -----------------------------------------------------------------------------

   pipeline {
     agent {
       label 'linux64'
     }

     // tools {
     //   maven 'maven-3.9'
     //   jdk 'openjdk-17'
     // }

     environment {
       REPO_NAME              = "${env.GIT_URL.tokenize('/.')[-2]}"
       DEFAULT_BRANCH         = "main"
       SCAN_BRANCHES          = "${env.BRANCH_NAME ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"

       BRIDGE_SRM_URL         = "https://srm.server.blackduck.com"
       BRIDGE_SRM_APIKEY      = credentials('srm-apikey')
       BRIDGE_SRM_ASSESSMENT_TYPES = "SAST,SCA"

       BRIDGE_SRM_PROJECT_NAME = "${env.REPO_NAME}"
       BRIDGE_SRM_BRANCH_NAME  = "${env.BRANCH_NAME}"
       BRIDGE_SRM_BRANCH_PARENT = "${env.SCAN_BRANCHES == 'true' && env.BRANCH_NAME != env.DEFAULT_BRANCH ? env.DEFAULT_BRANCH : ''}"

       BRIDGECLI_LINUX64 = "https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip"

       // BRIDGE_COVERITY_BUILD_COMMAND = "mvn -B -DskipTests package"
       // BRIDGE_COVERITY_CLEAN_COMMAND = "mvn -B clean"
     }

     stages {

       // stage('Build') {
       //   steps {
       //     sh 'mvn -B -DskipTests package'
       //   }
       // }

       stage('SRM Scan') {
         when {
           environment name: 'SCAN_BRANCHES', value: 'true'
         }
         steps {
           script {
             status = sh(
               returnStatus: true,
               script: '''
                 curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 &&
                 unzip -qo -d $WORKSPACE_TMP bridge.zip &&
                 rm -f bridge.zip &&
                 $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage srm
               '''
             )

             if (status == 8) {
               unstable 'policy violation'
             } else if (status != 0) {
               error 'bridge failure'
             }
           }
         }
       }
     }

     post {
       always {
         archiveArtifacts(
           allowEmptyArchive: true,
           artifacts: '.bridge/bridge.log, .bridge/*/idir/build-log.txt, .bridge/*/report.sarif.json'
         )

         // zip archive: true, dir: '.bridge', zipFile: 'bridge-logs.zip'
         cleanWs()
       }
     }
   }
   ```

   In the example above it can be observed that the pipeline downloads and executes the Bridge CLI directly for running full scans.

   The Jenkins pipeline will authenticate with the Software Risk Manager server specified in the `BRIDGE_SRM_SERVERURL` global variable, using the API key stored in Jenkins credentials as `srm-apikey`. By default a Software Risk Manager project is created before the full scan runs, with a name matching the name of the source repository.

   If a full scan is triggered for a branch that is not the default branch, then the pipeline sets the parent branch (`BRIDGE_SRM_BRANCH_PARENT`) to the default branch (main). This helps ensure that non-default branches reference the default branch as their base during scanning operations.

   A full scan, including SAST and SCA assessments, is triggered by commits to any of the monitored branches. The pipeline includes proper error handling that marks builds as unstable for policy violations.

   The `archiveArtifacts` step archives logs and reports from the `.bridge` folder as Jenkins artifacts for troubleshooting.
2. Run scans

   Once the pipeline is configured:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Test:** Monitor the Jenkins console output to verify that the SRM scan completes successfully and issues appear in SRM Dashboard.

## Troubleshooting and support

If errors are encountered during the pipeline run, ensure that all global variables are set correctly and that the Bridge CLI can access the SRM server.

If a pipeline error is encountered similar to the example below, then it is likely that the `BRIDGE_SRM_BRANCH_PARENT` environment variable has not been set correctly.

Important: ERROR: Branch "develop" does not exist for the project and "srm.branch.parent" is empty but is required along with "srm.branch.name" for creating the branch.

When scanning new non-default branches, e.g. `develop`, `stage` or `release`, the `BRIDGE_SRM_BRANCH_PARENT` environment variable must be set to the name of the default branch, e.g. `main`. An example is shown in the Quickstart code example in the Instructions section.

For further troubleshooting, check the archived artifacts that include detailed logs from the `.bridge` folder.

## Useful resources

- [SRM product documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
