---
title: "Using Rapid Scan Static with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-rapid-scan-static-with-bridge.html"
content_id: "0IvGwwAyU2P4qSw~cyZ2OQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-10-04T23:28:25.924670+00:00"
content_hash: "c8617d856bed2cb44461c3581e028cecba6f6492322154f38304f6cce8e22947"
---

# Using Rapid Scan Static with Bridge

Rapid Scan Static scans give developers fast, lightweight SAST feedback on pull request and feature branches, while full scans provide in-depth coverage on merges to main and release branches.

Rapid Scan Static allows Polaris users to perform fast and lightweight static analysis scans in your CI/CD pipeline. The Rapid Scan Static feature downloads the Black Duck Rapid Scan Static tool (Sigma) to the system on which the scan is performed. For example, if you use Bridge to trigger Rapid Scan Static on your build server, the Sigma tool will be downloaded to that server, and it will run the scan. Rapid Scan Static is built for speed, making it suitable for performing scans early and often.

Note: For many users, the Using Rapid Scan Static for pull request workflows FAQ is a simpler starting point. The FAQ provides Black Duck Security Scan CI/CD integration examples. Black Duck Security Scan automatically downloads and configures Bridge, reducing the amount of CI/CD configuration required compared to using Bridge CLI directly.

Before you begin, please review [SAST Capture File Types and Supported Frameworks (Rapid Scan Static)](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/7420e1d925f1f5f0729fb771ea66000a.topic) for basic requirements.

Important: Before you can test a project with Rapid Scan Static, a full SAST test using the latest version of Coverity that Polaris supports must be completed. For pull request workflows, complete the full SAST test on the branch that the pull request merges into, for example `main`. If you attempt to run a rapid scan before a full SAST test is completed, Bridge starts a full SAST scan automatically. The full SAST scan must be run with the latest version of Coverity that Polaris supports. This ensures your project has the necessary baseline before performing rapid scans.

## CLI instructions

We will walk through the steps to run a rapid scan in the CLI.

1. You will need the following parameters:

   Table 1. List of parameters for Rapid Scan SAST

   | Input parameter | Description | Mandatory / optional |
   | --- | --- | --- |
   | `BRIDGE_POLARIS_ACCESSTOKEN` | Environment variable to pass sensitive information such as your password or access token to Bridge CLI (recommended for security purposes). Note that Bridge CLI automatically picks up values passed through this environment variable. | Mandatory |
   | `--stage` | Specifies the Black Duck security product you are integrating with. | Mandatory |
   | `polaris.serverurl` | Your Polaris server URL. | Mandatory |
   | `polaris.application.name` | Name for Polaris application. The specified application must exist on Polaris with appropriate entitlements. | Mandatory |
   | `polaris.project.name` | Name for Polaris project. If the project doesn’t exist on Polaris, it’ll be created. If you don’t want the project to be created, set `polaris.onboarding` to `false`. | Mandatory |
   | `polaris.branch.name` | Branch name in the Polaris server. Bridge will error out if a branch name is not provided. If the branch doesn’t exist in Polaris, Bridge will create the branch. If you don’t want the branch to be created in Polaris, set `polaris.onboarding` to `false`.  For pull request workflows, specify the pull request branch. | Mandatory |
   | `polaris.branch.parent.name` | Specifies the branch that the pull request merges into. For example, specify `main` when the pull request targets the `main` branch. | Mandatory for pull request workflows |
   | `polaris.assessment.types` | Specifies the assessment types to run. Rapid Scan Static requires a SAST assessment, so include SAST: - SAST - SAST,SCA | Mandatory |
   | `polaris.test.sast.type` | This parameter allows you to run a full SAST scan, or a rapid SAST scan. If this parameter is not set, the default value will be used.  Default value: `SAST-FULL`  Acceptable values:  - `SAST-FULL` - `SAST-RAPID` | Optional for `SAST-FULL` scans, but mandatory for `SAST-RAPID` scans. |
2. Make your Polaris access token available as an environment variable.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
   ```

   Note: You can use either a user access token (created in the Polaris UI) or a service account token here.
3. Run a full SAST scan on the pull request target branch.

   For pull request workflows, the target branch is the branch that the pull request merges into, for example `main`. This scan provides the baseline required before Bridge can run `SAST-RAPID` on the pull request branch.

   **Example:**

   ```
   bridge-cli --stage polaris \
     polaris.project.name="<PROJECT_NAME>" \
     polaris.branch.name="main" \
     polaris.application.name="<APPLICATION_NAME>" \
     polaris.serverurl="<SERVERURL>" \
     polaris.assessment.types=SAST,SCA \
     polaris.test.sast.type=SAST-FULL
   ```
4. Run a rapid scan on the pull request branch.

   Configure the following for the pull request scan:

   - Set `polaris.branch.name` to the pull request branch.
   - Set `polaris.branch.parent.name` to the branch that is the target of the pull request.
   - Set `polaris.prcomment.enabled` to `true` to create pull request comments.

   If pull request comments are enabled, provide the SCM token and pull request parameters required by your SCM provider so that Bridge can add comments to the pull request. For the SCM token and pull request parameters supported by your SCM provider, please refer to Complete list of Bridge commands.

   **Example:**

   ```
   export GITHUB_USER_TOKEN=<GITHUB_USER_TOKEN>

   bridge-cli --stage polaris \
     polaris.project.name="<PROJECT_NAME>" \
     polaris.branch.name="<PULL_REQUEST_BRANCH>" \
     polaris.branch.parent.name="main" \
     polaris.application.name="<APPLICATION_NAME>" \
     polaris.serverurl="<SERVERURL>" \
     polaris.assessment.types=SAST \
     polaris.test.sast.type=SAST-RAPID \
     polaris.prComment.enabled=true \
     github.repository.name="<REPOSITORY_NAME>" \
     github.repository.owner.name="<REPOSITORY_OWNER>" \
     github.repository.branch.name="<PULL_REQUEST_BRANCH>" \
     github.repository.pull.number="<PULL_REQUEST_NUMBER>"
   ```

   The example above use Bridge CLI directly in a GitHub workflow. In this example, Bridge runs a `SAST-RAPID` scan on the pull request branch and compares the results with the target branch (`main`). The `polaris.prComment.enabled` parameter is set to `true` and the GitHub repository and pull request details are provided. Subsequently, Bridge adds comments to the pull request for issues identified in the pull request comparison.
5. When the scan completes successfully, the results will be available in your Polaris dashboard. If pull request comments are enabled and matching issues are found in the pull request comparison, Bridge creates comments on the pull request.
