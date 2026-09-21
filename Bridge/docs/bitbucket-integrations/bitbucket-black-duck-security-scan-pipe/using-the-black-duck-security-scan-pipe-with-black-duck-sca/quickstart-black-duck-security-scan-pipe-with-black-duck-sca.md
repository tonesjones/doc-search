---
title: "Quickstart: Black Duck Security Scan Pipe with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-pipe-with-black-duck-sca.html"
content_id: "BL6eoshBryv2ScLo5_EpTg"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:04.794893+00:00"
---

# Quickstart: Black Duck Security Scan Pipe with Black Duck SCA

This quickstart explains how to set up the Black Duck Security Scan Pipe for Bitbucket to run a pipeline that integrates with Black Duck® SCA to run a full scan and Pull Request scan. Fix Pull Requests are automatically raised for detected dependency vulnerabilities. Pull Request review comments are only created for new issues that are detected on the feature branch but not the target branch.

The full scan will be triggered by push and merge events on specified branches. Fix Pull Requests will automatically be raised for dependency vulnerabilities detected. Conversely, the Pull Request scan will be triggered by push events to Pull Requests that target those branches. Any new security issues introduced by a Pull Request will be added as review comments on the Pull Request. After the scan completes, appropriate security reports and diagnostic logs will be exported as build artifacts.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Bitbucket Prerequisites
  - List of Mandatory and Optional Parameters For SCA
  - Pull Request Comments
  - Fix Pull Requests
  - Additional Bitbucket Configuration
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A Bitbucket Access Token is required to allow the pipeline to inject Pull Request review comments, raise fix Pull Requests for dependency vulnerablities and upload SARIF reports.
- For security reasons, it is advisable not to store credentials and access tokens directly in the pipeline. The recommended approach is to use [Bitbucket variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) with the `secured` option checked.
- The following Black Duck Security Scan Pipe parameters are required to enable Pull Request comments, raise Fix Pull Requests and upload SARIF reports. These have been included in the quickstart example:

  Important: Pull Request comments, fix Pull Requests and SARIF reports will not function correctly if these parameters and the required prerequisites are not correctly configured.

  | **Parameter** | **Description** | **Example** |
  | --- | --- | --- |
  | `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` | When `true`, this enables Pull Request comments. | `"true"` |
  | `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` | When `true` a full scan will automatically raise fix Pull Requests for detected dependency vulnerabilities. | `"true"` |
  | `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE` | When true this exports SARIF reports for full scans. | `"true"` |
  | `BRIDGE_BLACKDUCKSCA_URL` | URL for Black Duck® SCA server instance. | `$BLACKDUCKSCA_URL` |
  | `BRIDGE_BLACKDUCKSCA_TOKEN` | Black Duck® SCA Access Token to enable integration with Black Duck® SCA server. | `$BRIDGE_BLACKDUCKSCA_TOKEN` |
  | `BRIDGE_BITBUCKET_API_TOKEN` | A Bitbucket Access Token. Required for Pull Request comments, fix Pull Requests and uploading SARIF reports. | `$BITBUCKET_REPO_ACCESS_TOKEN` |
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables) or workspace level (Workspace settings > Workspace variables > Add Variables):

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BLACKDUCKSCA_URL` | Variable | Black Duck® SCA Server URL | `https://sca.blackduck.com` |
  | `BRIDGE_BLACKDUCKSCA_TOKEN` | Secured Variable | Black Duck® SCA Access Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `BITBUCKET_REPO_ACCESS_TOKEN` | Secured Variable | A Bitbucket Access Token. Required for Pull Request comments, fix Pull Requests and uploading SARIF reports. | `REPLACE_WITH_BITBUCKET_ACCESS_TOKEN` |

  Note: The Black Duck Security Scan Pipe integrates with Black Duck® SCA via Bridge CLI. Additional scan configuration options not available through the template's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.

## Instructions

Follow the steps below to configure the Black Duck Security Scan Pipe to run a full scan and Pull Request scan.

1. Create the `bitbucket-pipelines.yml` file that contains the following pipeline:

   ```
   definitions:
     services:
       docker:
         memory: 3072 # Allocate 3GB (3072MB) memory to docker service
     steps:
       - step: &blackduck-security-scan
           name: Black Duck Security Scan
           script:
             - pipe: blackduck-inc/blackduck-security-scan:1.6.0
               variables:
                 BRIDGE_BLACKDUCKSCA_URL: $BLACKDUCKSCA_URL
                 BRIDGE_BLACKDUCKSCA_TOKEN: $BRIDGE_BLACKDUCKSCA_TOKEN
                 BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN
                 BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: "true"
                 BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: "true"
                 BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: "true"
                 BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: BLOCKER
                 DETECT_PROJECT_VERSION_NAME: ${BITBUCKET_PR_DESTINATION_BRANCH:-$BITBUCKET_BRANCH}
                 # INCLUDE_DIAGNOSTICS: true
           # artifacts:
           #  - ".blackduck/integrations/blackducksca/sarif/report.sarif.json"
           #  - ".bridge/**"

   pipelines:
     pull-requests:
       "**":
         - step: *blackduck-security-scan
     branches:
       "{main,master,develop,stage,release}":
         - step: *blackduck-security-scan
   ```

   In the example above a `Black Duck Security Scan` step runs whenever code is pushed to the `main`, `master`, `develop`, `stage` or `release` branches, or when a Pull Request is created. The scan type is automatically determined by the Black Duck Security Scan Pipe depending on the context in which the pipeline was triggered. The scan behavior is explained below.

   The pipeline integrates with a Black Duck® SCA server instance via the `BRIDGE_BLACKDUCKSCA_URL` and `BRIDGE_BLACKDUCKSCA_TOKEN` parameters. A scan will run for a Black Duck® SCA project named after the Bitbucket workspace and repository slug, e.g. `my-bitbucket-workspace/my-repository-slug`. Within this project, the project version is derived from the `DETECT_PROJECT_VERSION_NAME` environment variable. For full scans this corresponds to the name of the branch that had commits pushed. For Pull Request scans the project version is set to the name of the target branch of the Pull Request.

   The behavior of the scans is as follows:

   - **Full Scan**: Triggered by push events to `main`, `master`, `develop`, `stage` or `release` branches. In this scenario the following actions will be performed:

     - An SCA assessment will be run.
     - A SARIF report will be generated and exported only for full scans. This operation requires a Bitbucket Access Token.
     - Fix PRs will be automatically raised to fix vulnerable direct dependencies. This operation requires a Bitbucket Access Token.
   - **Pull Request Scan**: Triggered for Pull Request push events. A Pull Request scan is performed that will run an SCA assessment to scan the source code. Review comments will be injected (`BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT:
     true`) for any new issues introduced since the latest full scan of the Pull Request's target branch. This operation requires a Bitbucket Access Token.

   Both scans will fail the CI/CD build if a [Black Duck SCA Policy](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/8524980fd46bc3a6dece41aa700b842f.topic&Version=latest) violation is detected with a severity level of `BLOCKER`.

   Uncomment the `INCLUDE_DIAGNOSTICS` parameter and `artifacts` section to upload logs and reports as Bitbucket artifacts. These artifacts can be accessed and downloaded from the Artifacts tab of the pipeline's job page in Bitbucket (Repository > Pipelines).
2. Save the `bitbucket-pipelines.yml` pipeline file. If using the [Bitbucket Pipeline Editor](https://support.atlassian.com/bitbucket-cloud/docs/add-edit-and-commit-to-source-files/#Edit-files-online) then click Commit to save the changes to the pipeline. Alternatively, push the changes to the `main`, `master`, `develop`, `stage` or `release` branch of the repository. For example:

   ```
   git add bitbucket-pipelines.yml
   git commit -m "update pipeline to add security scan"
   git push -u origin main
   ```

   Once the changes have been saved to `bitbucket-pipelines.yml` the pipeline should be triggered to run on the `main`, `master`, `develop`, `stage` or `release` branch. Subsequently, it is then possible to open Bitbucket Pull Requests to run one or more Black Duck® SCA Pull Request scans.

   An example review comment added to a Bitbucket Pull Request after a Black Duck® SCA Pull Request scan has run is shown below.

   [image: PR review comments injected by Black Duck SCA PR Scan]

## Troubleshooting and support

If a pipeline error is encountered similar to that shown below, reported by Blackduck SCA Detect, then it is likely that a build tool, e.g. Maven, for the source code under test is unavailable within the image of the pipe.

Attention:

```
INFO: --- ======== Detect Issues ========
INFO: --- 
INFO: --- DETECTORS:
INFO: --- 	Detector Issue
INFO: --- 		Accuracy Not Met: MAVEN
INFO: --- 			Extraction for Maven Project Inspector has accuracy of LOW but HIGH is required by the current detect.accuracy.required configuration.
INFO: --- 
INFO: --- ======== Detect Result ========
```

In this scenario, any of the following actions may be taken to resolve the issue:

- Create and use a custom image that extends the Black Duck® SCA pipe. The custom image should have the required build tools installed, e.g. Maven. An example for using a custom image for a pipe is: `pipe:
  docker://your-registry/your-custom-image:tag`.
- Use the `BRIDGE_DETECT_ARGS` parameter to set project accuracy to `NONE`, i.e. `BRIDGE_DETECT_ARGS:
  --detect.accuracy.required=NONE`.
- Set scan failure severities to `BLOCKER`, i.e. `BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES:
  BLOCKER`.

## Useful resources

- [Black Duck SCA Portal](https://docs.blackduck.com/p/blackducksca)
- [Black Duck Security Scan Pipe Repository](https://bitbucket.org/blackduck-inc/blackduck-security-scan/src/master/)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
