---
title: "Using Rapid Scan Static for pull request workflows"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-rapid-scan-static-for-pull-request-workflows.html"
content_id: "CBO3sFp3VibvYuuuNycJZA"
version: "latest"
section: "How-to"
scraped_at: "2026-10-04T23:28:24.971773+00:00"
content_hash: "922dbf8d881cc6f7ab274e9bd5986d3921d7796294d6fb9b15e4f3864c7ed167"
---

# Using Rapid Scan Static for pull request workflows

Rapid Scan Static is a Polaris feature that provides fast static analysis for pull request workflows and reports issues associated with new or changed code.

## What does Rapid Scan Static do?

Rapid Scan Static provides fast lightweight static analysis that enables developers to receive security feedback early and often during development. It uses Black Duck Rapid Scan Static (Sigma) to analyze code changes and report issues associated with new or changed code.

Rapid Scan Static is designed to complement, not replace, full SAST scans. Run full SAST scans on target branches such as main or develop, and run rapid scans on pull requests that target those branches.

Important: If a rapid scan is attempted before the required full SAST baseline exists, Bridge starts a full SAST scan automatically.

## What are the prerequisites?

Before configuring Rapid Scan Static, ensure you have the following:

- A Polaris access token. Use a user access token created in the Polaris UI or a service account token.
- A completed full SAST scan that establishes the baseline for the target branch, such as `main` or `develop`. The full scan must use the latest version of Coverity supported by Polaris.

## What parameters are required to use Rapid Scan Static?

The following table lists the parameters required to configure Rapid Scan Static. Parameter names vary by CI platform; examples are provided in this FAQ.

Important: Rapid Scan Static requires the prerequisites and parameters described in this FAQ. If the required prerequisites or parameters are not configured, the integration cannot start a Rapid Scan Static scan.

| Input parameter | Description | Requirement |
| --- | --- | --- |
| Polaris server URL | The Polaris server URL. | Mandatory |
| Polaris access token | Access token used to authenticate with the Polaris server. Store the token as a secret or secured CI/CD variable. The examples in this FAQ show the appropriate CI platform parameter for passing the token to the integration. | Mandatory |
| Polaris application name | Name for polaris application. For parallel subscriptions the application must already exist if automatic onboarding is disabled. **Default value:** Git repository name | If not specified, the default value is provided. |
| Polaris project name | Name for the Polaris project. If automatic onboarding is disabled the branch must already exist in Polaris. **Default value**: Git repository name | If not specified, the default value is provided. |
| Polaris branch name | Branch name in the Polaris server. If automatic onboarding is disabled, the branch must already exist in Polaris. For pull request workflows the pull request branch should be specified.  **Default value**: Git branch name | If not specified, the default value is provided. |
| Polaris assessment types | Specifies the assessment types to run. Rapid Scan Static requires a SAST assessment, so include SAST:  - SAST - SAST,SCA | Mandatory |
| Polaris SAST test type | This parameter allows a full SAST scan, or a rapid SAST scan to be run. If this parameter is not set, the default value will be used.  **Default value**: `SAST-FULL`  **Acceptable values**:   - `SAST-FULL` - `SAST-RAPID` | Optional for `SAST-FULL` scans, but mandatory for `SAST-RAPID` scans. |

## What is the workflow for using Rapid Scan Static?

1. Run a full SAST scan on the target branch, such as `main`, and confirm that results appear in Polaris.
2. Create a branch from the target branch.
3. Open a pull request for the new branch.
4. Add and push a new SAST issue on the new branch to trigger a SAST scan.
5. Check CI pipeline logs for the pull request:
   1. Confirm that Bridge detects that `polaris.test.sast.type`, is set to `SAST-RAPID`.
   2. Confirm that Sigma ran and issues were detected.
6. Confirm that pull request comments were posted for new issues.

## Rapid Scan Static CI/CD examples

The following examples show how to configure Rapid Scan Static for Azure DevOps, Bitbucket, GitHub, GitLab, and Jenkins. Each example implements the recommended workflow of running a full SAST scan on protected branches and a rapid scan on pull requests that target those branches.

The examples also demonstrate how to enable pull request comments and configure the required source control management (SCM) credentials so that Bridge can post comments for eligible findings associated with the pull request.

Before using the examples, store the Polaris access token in `POLARIS_ACCESSTOKEN` as a secret or secured variable.

Note:

Polaris uses Coverity to perform SAST assessments. For compiled languages such as C, C++ and Java, additional build capture configuration is required before a scan can be performed. For more information, see Using Bridge with compiled languages

GitHub

This example uses `polaris_test_sast_type` to run a full SAST scan on branch pushes and a rapid scan for pull requests. Pull request comments are enabled by setting `polaris_prComment_enabled` to `true`. The `github_token` parameter uses the GitHub Actions build token (`secrets.GITHUB_TOKEN`) provided to the workflow to authenticate with GitHub and post comments for eligible findings associated with pull request changes. For information about configuring the required permissions, see GitHub prerequisites.

```
- name: Polaris Scan
  uses: blackduck-inc/black-duck-security-scan@v2
  with:
    polaris_server_url: ${{ vars.POLARIS_SERVERURL }}
    polaris_access_token: ${{ secrets.POLARIS_ACCESSTOKEN }}
    polaris_assessment_types: SAST,SCA
    polaris_test_sast_type: ${{ github.event_name != 'pull_request' && 'SAST-FULL' || 'SAST-RAPID' }}
    polaris_application_name: polaris-${{ github.event.repository.name }}
    polaris_prComment_enabled: true
    github_token: ${{ secrets.GITHUB_TOKEN }}
```

Azure

This example uses `polaris_test_sast_type` to run a full SAST scan on branch pushes and a rapid scan for pull requests. Pull request comments are enabled by setting `polaris_prcomment_enabled` to true. The `azure_token` parameter uses the Azure DevOps build token provided to the pipeline (`System.AccessToken`) to authenticate with Azure DevOps and post comments for eligible findings associated with pull request changes. For information about configuring the required permissions, see Setting up Black Duck Security Scan Extension.

```
variables:
  - group: poc.polaris.blackduck.com
  - name: SAST_TYPE
    ${{ if eq(variables['Build.Reason'], 'PullRequest') }}:
      value: 'SAST-RAPID'
    ${{ else }}:
      value: 'SAST-FULL'

steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Polaris Scan'
  inputs:
    polaris_server_url: $(POLARIS_SERVERURL)
    polaris_access_token: $(POLARIS_ACCESSTOKEN)
    polaris_assessment_types: 'SAST,SCA'
    polaris_test_sast_type: $(SAST_TYPE)
    polaris_application_name: $(Build.Repository.Name)
    polaris_prcomment_enabled: true
    azure_token: $(System.AccessToken)
    include_diagnostics: false
    mark_build_status: 'SucceededWithIssues'
```

GitLab

This example uses `BRIDGE_POLARIS_TEST_SAST_TYPE` to run a full SAST scan on the main, master, develop, stage, and release branches, and a rapid scan on merge requests that target those branches.

- A GitLab personal access token (PAT) is required to be configured as a masked CI/CD variable named `GITLAB_USER_TOKEN`. The `BRIDGE_GITLAB_USER_TOKEN` parameter uses this token to authenticate with GitLab and post comments for eligible findings associated with merge request changes. For information about creating and configuring the required token, see Configure GitLab user token.
- Pull request comments are enabled by setting `BRIDGE_POLARIS_PRCOMMENT_ENABLED` to `true`.

```
variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release)$/"

polaris:
  stage: security

  rules:
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES &&
           $CI_PIPELINE_SOURCE == 'merge_request_event')
      variables:
        BRIDGE_POLARIS_TEST_SAST_TYPE: "SAST-RAPID"

    - if: ($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES &&
           $CI_PIPELINE_SOURCE != 'merge_request_event')

  variables:
    BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
    BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
    BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVER_URL
    BRIDGE_POLARIS_APPLICATION_NAME: $CI_PROJECT_NAMESPACE-$CI_PROJECT_NAME
    BRIDGE_POLARIS_ASSESSMENT_TYPES: "SAST,SCA"
    BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"

  extends: .run-black-duck-tools
```

Jenkins

This example is a multibranch pipeline that uses `polaris_test_sast_type` to run a full SAST scan on protected branches and a rapid scan for pull requests that target those branches. Pull request comments are enabled by setting `polaris_prComment_enabled` to `true`.

Before using this example, ensure that the following prerequisites are met:

- Install the Black Duck Security Scan plugin to integrate with a Polaris server instance.
- Install and configure the appropriate Branch Source plugin to enable Jenkins to integrate with a source code repository and validate pull request events.
- Configure the following Jenkins Black Duck Security Scan Plugin parameters via Dashboard > Manage Jenkins > System:
  - Polaris server URL and access token. These enable the pipeline to integrate with the Polaris server.
  - Source code management token for the repository to enable the Black Duck Security Scan plugin to inject pull request review comments for new security issues uncovered during a pull request scan.

  See configure global settings in the UI in the getting started guide for further details.
- Access to a [Jenkins Multibranch Pipeline Project](https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline).

```
pipeline {
    agent {
        label 'node'
    }

    environment {
        REPO_NAME = "${env.GIT_URL.tokenize('/.')[-2]}"

        FULLSCAN = "${env.BRANCH_NAME ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"
        PRSCAN = "${env.CHANGE_TARGET ==~ /^(main|master|develop|stage|release)$/ ? 'true' : 'false'}"

        POLARIS_SAST_TYPE = "${env.PRSCAN == 'true' ? 'SAST-RAPID' : 'SAST-FULL'}"
    }

    stages {
        stage('Polaris') {
            when {
                anyOf {
                    environment name: 'FULLSCAN', value: 'true'
                    environment name: 'PRSCAN', value: 'true'
                }
            }

            steps {
                security_scan(
                    product: 'polaris',
                    polaris_assessment_types: 'SAST,SCA',
                    polaris_application_name: "${REPO_NAME}",
                    polaris_prComment_enabled: true,
                    polaris_test_sast_type: "${env.POLARIS_SAST_TYPE}",
                    mark_build_status: 'UNSTABLE'
                )
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

Bitbucket

This example uses `BRIDGE_POLARIS_TEST_SAST_TYPE` to run a full SAST scan on protected branches and a rapid scan for pull requests that target those branches.

- Store a Bitbucket repository access token as a secured repository variable named `BITBUCKET_REPO_ACCESS_TOKEN`. The `BRIDGE_BITBUCKET_API_TOKEN` parameter uses this token to authenticate with Bitbucket and post comments for eligible findings associated with pull request changes. For information about creating and configuring the required token, see Setting up Black Duck Security Scan Pipe.
- Pull request comments are enabled by setting `BRIDGE_POLARIS_PRCOMMENT_ENABLED` to `true`.

```
definitions:
  services:
    docker:
      memory: 3072 # Allocate 3GB (3072MB) memory to docker service

  steps:
    - step: &blackduck-security-scan
        name: Polaris Black Duck Security Scan

        script:
          - |
              if [[ -z $BITBUCKET_PR_ID ]]; then
                export POLARIS_SAST_TYPE="SAST-FULL"
              else
                export POLARIS_SAST_TYPE="SAST-RAPID"
              fi

          ## For compiled languages, replace standard pipe with image containing build tools.
          ## - pipe: docker://your-registry/your-custom-image:tag
          - pipe: blackduck-inc/blackduck-security-scan:1.6.0
            variables:
              BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
              BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
              BRIDGE_POLARIS_ASSESSMENT_TYPES: "SCA,SAST"
              BRIDGE_POLARIS_TEST_SAST_TYPE: $POLARIS_SAST_TYPE
              BRIDGE_POLARIS_APPLICATION_NAME: $BITBUCKET_REPO_SLUG
              BRIDGE_POLARIS_PRCOMMENT_ENABLED: "true"
              BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN

pipelines:
  pull-requests:
    "**":
      - step: *blackduck-security-scan

  branches:
    "{main,master,develop,stage,release}":
      - step: *blackduck-security-scan
```

## Additional resources

This FAQ focuses on the concepts, prerequisites, workflow, and CI/CD configuration required for Rapid Scan Static. For step-by-step instructions on configuring Bridge CLI to perform Rapid Scan Static scans, see Using Rapid Scan Static with Bridge.
