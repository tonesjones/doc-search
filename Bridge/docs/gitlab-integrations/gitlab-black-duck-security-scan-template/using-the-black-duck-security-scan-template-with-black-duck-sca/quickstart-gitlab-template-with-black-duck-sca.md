---
title: "Quickstart: GitLab Template with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-gitlab-template-with-black-duck-sca.html"
content_id: "C7VZ8BRfyKyiCgBJ1FnQiQ"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:08.101347+00:00"
---

# Quickstart: GitLab Template with Black Duck SCA

This quickstart explains how to set up the Black Duck Security Scan Template to run a pipeline that integrates with Black Duck® SCA to run a full scan and Merge Request scan. Merge Request review comments are only created for new issues created that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Conversely, the Merge Request scan will be triggered by push events to Merge Requests that target those branches. Any new security issues introduced by a Merge Request will be added as review comments on the Merge Request. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitLab prerequisites
  - Merge Request Comments
  - Fix Merge Requests
  - Additional GitLab configuration
  - [GitLab Pipeline editor](https://docs.gitlab.com/ci/pipeline_editor/)
- Admin access to a GitLab repository.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access is required to allow the pipeline to inject review comments into GitLab Merge Requests.
- For security reasons, it is advisable not to store credentials directly in the workflow. The recommended approach is to use masked and hidden variables.

  Important: It is adviseable to use project variables. Group variable inheritance can cause scans to fail under certain conditions. Be sure to set the mask variable flag for `BLACKDUCKSCA_API_TOKEN` and `GITLAB_USER_TOKEN` to avoid exposure in the CI logs.
- The following parameters are required to enable inject review comments into Pull Requests and have been included in the quickstart example:

  Important: Merge Request comments will not be injected if these parameters and the required prerequisites are not configured.

  | Parameter | Description | Example |
  | --- | --- | --- |
  | `DETECT_PROJECT_NAME` | Black Duck® SCA project name. | `$CI_PROJECT_NAME` |
  | `DETECT_PROJECT_VERSION_NAME` | Set to Merge Request target branch for differential comparison. | `$CI_MERGE_REQUEST_TARGET_BRANCH_NAME` |
  | `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` | When `true`, enables PR comments. | `"true"` |
  | `BRIDGE_GITLAB_USER_TOKEN` | [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` access for injecting review comments. | `$GITLAB_USER_TOKEN` |

  Note: The Black Duck Security Scan Template integrates with Black Duck® SCA via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the pipeline job.

  - The following variables are required (Gitlab > Project sidebar > Settings > CI / CD > Variables > Add Variables):

    | Variable | Type | Description | Example |
    | --- | --- | --- | --- |
    | `BLACKDUCKSCA_URL` | Masked | Black Duck Server URL | https://sca.blackduck.com |
    | `BLACKDUCKSCA_API_TOKEN` | Masked and hidden | Black Duck API Token | `REPLACE_WITH_YOUR_TOKEN` |
    | `GITLAB_USER_TOKEN` | Masked and hidden | [GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with at least `Developer` privileges and `api` accesss for injecting review comments. | `REPLACE_WITH_YOUR_TOKEN` |

## Instructions

Follow the steps below to configure the Black Duck Security Scan Template to run a full scan and Merge Request scan.

1. Create the `.gitlab-ci.yaml` containing the following pipeline:

   ```
   include:
     - project: blackduck-inc/black-duck-security-scan
       ref: v2
       file: templates/security_scan.yml

   stages:
     - security

   variables:
     SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch|fix)$/"

   sca:
     stage: security
     rules:
       - if: ($CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES)
         variables:
           DETECT_PROJECT_VERSION_NAME: "$CI_MERGE_REQUEST_TARGET_BRANCH_NAME"
       - if: ($CI_PIPELINE_SOURCE != "merge_request_event" && $CI_COMMIT_BRANCH =~ $SCAN_BRANCHES)
         variables:
           DETECT_PROJECT_VERSION_NAME: "$CI_COMMIT_BRANCH"
       - when: "never"
     variables:
       BRIDGE_BLACKDUCKSCA_URL: $BLACKDUCKSCA_URL
       BRIDGE_BLACKDUCKSCA_TOKEN: $BLACKDUCKSCA_API_TOKEN
       BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: BLOCKER
       BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: true
       BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_CREATE: true
       BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: true
       BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: true
       BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
       DETECT_PROJECT_NAME: $CI_PROJECT_NAME
       # INCLUDE_DIAGNOSTICS: true
     before_script:
       - apt-get -qq update && apt-get install -y curl unzip
     extends: .run-black-duck-tools
     # artifacts:
     #  name: "bridge-logs"
     #  when: always
     #  paths:
     #    - .bridge/
     #  expire_in: 30 days
   ```

   In the example above an `sca` pipeline job runs whenever code is pushed to any branch listed in the `SCAN_BRANCHES` variable, or when a Merge Request targets one of those branches. The scan type is automatically determined by the Black Duck Security Scan Template depending on the context in which the pipeline was triggered. The scan behavior is explained below.

   The pipeline integrates with a Black Duck® SCA server instance via the `BRIDGE_BLACKDUCKSCA_URL` and `BRIDGE_BLACKDUCKSCA_TOKEN` parameters. A scan will run for a Black Duck® SCA project named after the GitLab project’s name. Within this project, the project version is derived from the `DETECT_PROJECT_VERSION_NAME` environment variable. For full scans this corresponds to the name of the branch that had commits pushed. For Merge Request scans the project version is set to the name of the target branch of the Merge Request.

   The behavior of the scans is as follows:

   - **Full Scan**: Triggered by push events to any of the branches defined in the `SCAN_BRANCHES` variable. In this scenario the following actions will be performed:
     - An SCA assessment will be run.
     - Issues that have `BLOCKER` severity will cause the scan to report issues.
     - A SARIF report and [GitLab Vulnerability Reports](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/c5491cfa4e0e28b3d44d91ad5e01da58.topic) will be generated and exported only for full scans. [GitLab Vulnerability Reports](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/c5491cfa4e0e28b3d44d91ad5e01da58.topic) are available for preview to users with a GitLab Ultimate subscription. If the scan detects a policy violation then the GitLab vulnerability reports will not be uploaded. For details on how to bypass this behavior visit [How to use GitLab Vulnerability Reports](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/c5491cfa4e0e28b3d44d91ad5e01da58.topic).
     - Fix PRs will be automatically raised to fix vulnerable direct dependencies.
   - **Merge Request Scan**: Triggered for Merge Request push events, where the target branch of the merge matches one of the branches defined in the `SCAN_BRANCHES` variable. A Merge Request scan is performed that will run an SCA assessment to scan the source code. Review comments will be injected (`BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT:
     true`) for any new issues introduced since the latest full scan of the Merge Request's target branch.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports from the `.bridge` folder as GitLab artifacts. These artifacts can be accessed and downloaded from the pipeline's job page in GitLab (Project > Build > Jobs).
2. Save the changes made to the `.gitlab-ci.yml` pipeline file. If using the [GitLab Pipeline Editor](https://docs.gitlab.com/ci/pipeline_editor) then click Commit Changes to save the changes to the pipeline. Alternatively, push the changes to the `main` or `master` branch of the repository. For example:

   ```
   git add .gitlab-ci.yml
   git commit -m "update pipeline to add security scan"
   git push -u origin main
   ```

   Once the changes have been saved to `.gitlab-ci.yml` the pipeline should be triggered to run a full Black Duck® SCA scan on the `main` or `master` branch. Subsequently, it is then possible to open GitLab Merge Requests to run one or more Merge Request scans.

   An example review comment added to a GitLab Merge Request after a Merge Request scan has run is shown below:

   [image: Merge Request review comments injected by rapid scan]

## Next steps

Bridge initiates a Black Duck Detect scan that targets a repository. Detect properties can be passed using the `BRIDGE_BLACKDUCK_ARGS` variable to further configure the scan. The code below is an example of further configuration; however, it is not necessary to include in this scan.

```
BRIDGE_BLACKDUCK_ARGS: --detect.project.name=your_project_name, --detect.project.version.name=v1.7
```

A complete list of Bridge variables for Black Duck® SCA is available at Bridge SCA Variables.

## Troubleshooting and support

If a pipeline error is encountered similar to the example below, then it is likely that organization firewall rules maybe restricting access to the template.

Attention: Unable to create pipeline Project `blackduck-inc/black-duck-security-scan` not found or access denied! Make sure any includes in the pipeline configuration are correctly defined.

The recommended solution is to check that the template is referenced correctly and then perform one of the following actions:

- Arrange access with IT administration of the organization.
- Use a GitLab self managed runner.

## Useful resources

- [Using Black Duck Security Scan Template with Black Duck SCA](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/949207ee3f3436bf9c902370dbac576e.topic)
- [Black Duck SCA Portal](https://docs.blackduck.com/p/blackducksca)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
