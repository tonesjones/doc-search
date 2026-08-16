---
title: "Quickstart: Jenkins Black Duck Security Scan Plugin with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-jenkins-black-duck-security-scan-plugin-with-black-duck-sca.html"
content_id: "0VGNuu08vFBAN~c4AhmRPw"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:42.699347+00:00"
---

# Quickstart: Jenkins Black Duck Security Scan Plugin with Black Duck SCA

This quickstart explains how to set up a [Jenkins multibranch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/) for a Black Duck® SCA project that will run a full scan and Pull Request scan. Pull Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments on the Pull Request.

## Prerequisites

- The following reading is recommended before starting the quickstart:
  - Jenkins Prerequisites
  - Using the Black Duck Security Scan Plugin with Black Duck® SCA
  - Pull Request Comments
  - Fix Pull Requests
- Install the Black Duck Security Scan plugin to integrate with a Black Duck® SCA server instance.
- Install and configure the appropriate Branch Source plugin to enable Jenkins to integrate with a source code repository and validate Pull Request events.
- Configure a source code management token to enable the Black Duck Security Scan plugin to inject Pull Request review comments for new security issues uncovered during a Pull Request scan.
- Access to a [Jenkins Multibranch Pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) project.
- Important:

  Please note that the following Black Duck Security Scan Plugin parameters are required to run a Pull Request scan and inject review comments. These are included in this quickstart example and listed in the table below. A Pull Request scan will not run if these parameters and quickstart prerequisites are not configured. This includes providing a source code management token to allow review comments to be added by the plugin.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `DETECT_ARGS` | Enables the plugin to identify the appropriate Black Duck® SCA project and version. For Pull Request scans, the project version is set to the parent branch of the Pull Request, allowing for an accurate comparison of changes. | `--detect.project.name='${env.DETECT_PROJECT_NAME}' --detect.project.version.name=${version}` |
  | `blackducksca_prComment_enabled` | When `true`, this enables Pull Request comments. | `"true"` |

  Note: Note: The Black Duck Security Scan Plugin integrates with Black Duck® SCA via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the pipeline job.

## Instructions

1. Create a `Jenkinsfile` in the root of a source repository for all branches. The `Jenkinsfile` should contain the pipeline listed in the example below:

   ```
   def getProjectVersion() {
       return env.PRSCAN == 'true' ? env.CHANGE_TARGET : env.BRANCH_NAME
   }

   pipeline {
       agent { label 'node' }
       environment {
           REPOSITORY_NAME = "${env.GIT_URL.tokenize('/.')[-2]}"
           FULLSCAN = "${env.BRANCH_NAME ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
           PRSCAN = "${env.CHANGE_TARGET ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
           DETECT_PROJECT_NAME = "${env.REPOSITORY_NAME}"
       }
       stages {
           stage('Black Duck SCA') {
               when {
                   anyOf {
                       environment name: 'FULLSCAN', value: 'true'
                       environment name: 'PRSCAN', value: 'true'
                   }
               }
               steps {
                   script {
                       def version = getProjectVersion()
                       
                       security_scan product: 'blackducksca',
                           blackducksca_scan_failure_severities: 'BLOCKER',
                           blackducksca_prComment_enabled: true,
                           blackducksca_reports_sarif_create: true,
                           detect_args: "--detect.project.name='${env.DETECT_PROJECT_NAME}' --detect.project.version.name=${version}",
                           mark_build_status: 'UNSTABLE',
                           include_diagnostics: false
                   }
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

   The pipeline in the example above will trigger one of the following security scans, depending upon the `FULLSCAN` and `PRSCAN` variables:

   - **Full scan**: A full scan is triggered by a push or merge event to a predefined set of branches, defined in the the `FULLSCAN` environmental variable. In this scenario the [Black Duck Security Scan Plugin](https://plugins.jenkins.io/blackduck-security-scan/) will exhibit the following behavior:
     - A full scan will be performed for the Black Duck® SCA project and version defined in the `detect_args` parameter. If the specified project and version do not exist they will be created dynamically at runtime. The project version corresponds to the name of the branch that triggered the full scan, (e.g. `main`, `develop` etc.).
     - The SCA assessment will scan the source code up to a folder depth of 20 (`detect_search_depth: 20`).
     - SARIF reporting is enabled. This will automatically upload the SARIF report as a Jenkins build artifact.
   - **Pull Request scan**: A Pull Request scan is triggered for push events on Pull Requests, where the target branch matches any of the branches defined in the `PRSCAN` variable. This behavior is activated by setting the `blackducksca_prComment`_enabled to `true`. In this scenario the [Black Duck Security Scan Plugin](https://plugins.jenkins.io/blackduck-security-scan/) will exhibit the following behavior:
     - A scan is executed to perform a differential analysis between the Pull Request and its parent branch. The `detect_args` parameter enables the plugin to identify the appropriate project and version for the scan. In this case, the project version is set to the parent branch of the Pull Request, allowing for an accurate comparison of changes.
     - The token created in the prerequisite steps will be used to inject Pull Request review comments for new security issues detected since the last full scan.
     - The SCA assessment will scan the source code up to a folder depth of 20 (`detect_search_depth: 20`).

   It can be seen from the example above that, for both scans, the Jenkins build result status will be marked as `UNSTABLE` when policy violations are detected.

   If the `include_diagnostics` parameter is set to `true` then the Bridge CLI logs contained within the `.bridge` folder will be uploaded as a Jenkins build artifact to enable access to logs and diagnostics. Once the build completes, these can be downloaded from the `Artifacts` section within the build's `Status` page.
2. Once the Jenkinsfile has been saved and pushed to your source code repository branches then a full scan should be performed, e.g. on the `main`, `develop` or `production` branches. At this point it should be possible to view issues uncovered by the full scan within Black Duck® SCA. Subsequently, a Pull Request scan can then be run to detect new issues since the full scan was performed. These new issues will be highlighted as review comments, as illustrated below.

   [image: GitLab Merge Request with review comments injected]

## Useful resources

- [Black Duck® SCA Product Documentation](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic&Version=latest)
- Jenkins - Black Duck Security Scan Plugin for Jenkins
- [Black Duck Security Scan Plugin for Jenkins](https://plugins.jenkins.io/blackduck-security-scan/)
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
