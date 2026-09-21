---
title: "Quickstart: Black Duck SCA Bridge CLI in a Jenkins pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-sca-bridge-cli-in-a-jenkins-pipeline.html"
content_id: "ZZ18N3gkVdEMzPGDxSM58Q"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:16.064551+00:00"
---

# Quickstart: Black Duck SCA Bridge CLI in a Jenkins pipeline

As an alternative to the [Black Duck Security Scan Plugin for Jenkins](https://plugins.jenkins.io/blackduck-security-scan/), the Bridge CLI can be downloaded and directly executed in a Jenkins pipeline. It has all the functionality of the plugin, but requires an additional step to [download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Black Duck® SCA parameters must be passed directly inside the pipeline. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Plugin for Jenkins (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Plugin and what it can do, take a look at the overview page.

The quickstart uses Bridge CLI directly within a Jenkins pipeline to integrate with a GitHub repository. Bridge CLI can integrate with various SCM platforms, e.g. Azure, Bitbucket, GitLab. Adjust the parameters and Personal Access Token (PAT) to match the required SCM platform for integrating with Jenkins. Refer to the reference tables within the Black Duck SCA section for the Bridge CLI parameters needed to integrate with SCM platforms for Fix Pull Requests and Pull Request Comments.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Jenkins prerequisites
  - Pull Request comments
  - Fix Pull Requests
  - List of mandatory and optional parameters for Black Duck SCA
  - Additional Jenkins parameters
- Admin access to a Jenkins instance.
- A Jenkins agent with a label configured, e.g. `linux64`.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A Personal Access Token (PAT) is required to allow the pipeline to inject Pull Request review comments and raise Fix Pull Requests. The PAT should be generated for the SCM platform that Bridge CLI integrates with from within the Jenkins pipeline, e.g. GitHub, GitLab, Azure, Bitbucket etc.
- The Branch Source plugin must be installed for the appropriate platform to enable Jenkins to integrate with a source code repository and validate pull requests events.
- For security reasons, it is advisable to use [Jenkins credentials](https://www.jenkins.io/doc/book/using/using-credentials/) to store credentials and access tokens. It is recommended that the credentials are added at the appropriate scope level.
- Add the following credentials in Jenkins (Manage Jenkins > Manage Credentials > System > Global credentials)

  | Credential ID | Type | Description | Example |
  | --- | --- | --- | --- |
  | `blackduck-sca-api-token` | Secret text | Black Duck SCA API Token | `YOUR_TOKEN` |
  | `scm-pat` | Secret text | SCM Platform Personal Access Token (e.g., GitHub, GitLab) | `YOUR_TOKEN` |
- Ensure the following environment variables are set correctly in the pipeline:

  | Variable | Description | Example |
  | --- | --- | --- |
  | `BRIDGECLI_LINUX64` | URL for downloading Bridge CLI binary | `https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip` |
  | `BRIDGE_BLACKDUCKSCA_URL` | Black Duck SCA server URL | `https://sca.field-test.blackduck.com` |
  | `BRIDGE_BLACKDUCKSCA_TOKEN` | Black Duck SCA API token from Jenkins credentials | `credentials('blackduck-sca-api-token')` |
  | `DETECT_PROJECT_NAME` | Project name for Black Duck SCA detection | `${env.REPO_NAME}` |
  | `SCM_PAT` | SCM Platform Personal Access Token from Jenkins credentials. Required to inject Pull Request comments and raise Fix Pull Requests. | `credentials('scm-pat')` |
- The following Bridge CLI parameters are required to inject Pull Request comments and raise fix Pull Requests:

  | Parameter | Description | Value | Scan type |
  | --- | --- | --- | --- |
  | `blackducksca.fixpr.enabled` | Raise Fix PRs for detected vulnerabilities | `true` | Full |
  | `blackducksca.automation.prcomment` | Enable PR comments | `true` | PR |
  | `github.repository.pull.number` | ID of Pull Request to scan | `$CHANGE_ID` |

  Note: Parameter `github.repository.pull.number` is specific to adding Pull Request Comments for GitHub. Refer to the SCM Pull Request comments table within the Black Duck SCA section for the equivalent Bridge CLI parameter required for integrating with other SCM platforms.

## Instructions

1. Add the following pipeline configuration to your repository as a `Jenkinsfile`.

   Note: For compiled languages, uncomment the build sections and tools in the provided pipeline configuration. Adjust the tools and build steps to align with project specific build tools and requirements, such as Maven, Gradle, or other build systems.

   ```
   pipeline {
       agent { label 'linux64' }
       environment {
           ORG_NAME = "${env.GIT_URL.tokenize('/.')[-3]}"
           REPO_NAME = "${env.GIT_URL.tokenize('/.')[-2]}"
           FULLSCAN = "${env.BRANCH_NAME ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
           PRSCAN = "${env.CHANGE_TARGET ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
           BRIDGECLI_LINUX64 = 'https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip'
           BRIDGE_BLACKDUCKSCA_URL = 'https://sca.server.blackduck.com'
           BRIDGE_BLACKDUCKSCA_TOKEN = credentials('blackduck-sca-api-token')
           DETECT_PROJECT_NAME = "${env.REPO_NAME}"
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
           stage('Black Duck Full Scan') {
               when { environment name: 'FULLSCAN', value: 'true' }
               steps {
                   script {
                       status = sh returnStatus: true, script: '''
                           curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $WORKSPACE_TMP bridge.zip && rm -f bridge.zip
                           $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca \
                               blackducksca.scan.full=true \
                               blackducksca.scan.failure.severities='BLOCKER' \
                               blackducksca.fixpr.enabled=true \
                               blackducksca.reports.sarif.create=true \
                               github.repository.name=$REPO_NAME \
                               github.repository.branch.name=$BRANCH_NAME \
                               github.repository.owner.name=$ORG_NAME \
                               github.user.token=$SCM_PAT
                       '''
                       if (status == 8) { unstable 'policy violation' }
                       else if (status != 0) { error 'scan failure' }
                   }
               }
           }
           stage('Black Duck PR Scan') {
               when { environment name: 'PRSCAN', value: 'true' }
               steps {
                   script {
                       status = sh returnStatus: true, script: '''
                           curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d $WORKSPACE_TMP bridge.zip && rm -f bridge.zip
                           $WORKSPACE_TMP/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca \
                               blackducksca.scan.full=false \
                               blackducksca.automation.prcomment=true \
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
               archiveArtifacts allowEmptyArchive: true, artifacts: '.bridge/bridge.log, .bridge/*/report.sarif.json'
               //zip archive: true, dir: '.bridge', zipFile: 'bridge-logs.zip'
               cleanWs()
           }
       }
   }
   ```

   The pipeline will download Bridge CLI from the URL contained in the `BRIDGECLI_LINUX64` environment variable for direct execution in the pipeline. One of the following Black Duck SCA scans will be triggered depending on the event type:
   - **Full scan**: Triggered by push events to the specified branches (main, master, develop, stage, release). This scan:
     - Performs a complete SCA assessment of all dependencies
     - Creates a SARIF report for security findings
     - Enables fix pull request generation for vulnerable dependencies
     - Fails the build on BLOCKER severity vulnerabilities
   - **Pull Request scan**: Triggered for pull request events targeting the specified branches. This scan:
     - Performs a differential analysis between the pull request and target branch
     - Automatically adds review comments for new vulnerabilities introduced in the pull request
     - Uses the target branch as the baseline for comparison

   Note: Parameters `github.repository.*` and `github.user.token` are specific to integrating Bridge CLI with GitHub Pull Requests. Refer to the SCM Pull Request comments table within the Black Duck SCA section for the equivalent Bridge CLI parameter required for integrating with other SCM platforms.

   The post-build action archives individual Bridge CLI logs and SARIF reports for troubleshooting and cleans the workspace for the next build. The commented zip action (requires [Pipeline Utility Steps](https://plugins.jenkins.io/pipeline-utility-steps/) plugin) provides an alternative to create a single compressed archive containing all Bridge logs.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment:

   [image: PR review comments injected by SCA PR scan]

## Useful resources

- [Black Duck product documentation](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic&Version=latest)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
- [Jenkins pipeline documentation](https://www.jenkins.io/doc/book/pipeline/)
