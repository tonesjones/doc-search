---
title: "Using Rapid Scan Static with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-rapid-scan-static-with-bridge.html"
content_id: "0IvGwwAyU2P4qSw~cyZ2OQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:04.265795+00:00"
---

# Using Rapid Scan Static with Bridge

Rapid Scan Static allows Polaris users to perform fast and lightweight static analysis scans in your CI/CD pipeline. The Rapid Scan Static feature downloads the Black Duck Rapid Scan Static tool (Sigma) to the system on which the scan is performed. For example, if you use Bridge to trigger Rapid Scan Static on your build server, the Sigma tool will be downloaded to that server, and it will run the scan. Rapid Scan Static is built for speed, making it suitable for performing scans early and often.

Before you begin, please review [SAST Capture File Types and Supported Frameworks (Rapid Scan Static)](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/7420e1d925f1f5f0729fb771ea66000a.topic) for basic requirements.

Important: Before you can test a project with Rapid Scan Static, a full SAST test (using the latest version of Coverity that Polaris supports) must be completed. If you attempt to run a rapid scan before a full SAST test is completed, Bridge starts a full SAST scan automatically. The full SAST scan must be run with the latest version of Coverity that Polaris supports. This ensures your project has the necessary baseline before performing rapid scans.

## CLI instructions

We will walk through the steps to run a rapid scan in the CLI.

1. You will need the following parameters:

   Table 1. List of mandatory parameters for rapid scan SAST

   | Input parameter | Description | Mandatory / optional |
   | --- | --- | --- |
   | `BRIDGE_POLARIS_ACCESSTOKEN` | Environment variable to pass sensitive information such as your password or access token to Bridge CLI (recommended for security purposes). Note that Bridge CLI automatically picks up values passed through this environment variable. | Mandatory |
   | `--stage` | Specifies the Black Duck security product you are integrating with. | Mandatory |
   | `polaris.serverurl` | Your Polaris server URL. | Mandatory |
   | `polaris.application.name` | Name for Polaris application. The specified application must exist on Polaris with appropriate entitlements. | Mandatory |
   | `polaris.project.name` | Name for Polaris project. If the project doesn’t exist on Polaris, it’ll be created. If you don’t want the project to be created, set `polaris.onboarding` to `false.` | Mandatory |
   | `polaris.branch.name` | Branch name in the Polaris server. Bridge will error out if a branch name is not provided. If the branch doesn’t exist in Polaris, Bridge will create the branch. If you don’t want the branch to be created in Polaris, set `polaris.onboarding` to `false.`. | Mandatory |
   | `polaris.assessment.types` | Specifies the type of test to be run: - `SAST` - `SCA` - `SAST,SCA` | Mandatory |
   | `polaris.test.sast.type` | This parameter allows you to run a full SAST scan, or a rapid SAST scan. If this parameter is not set, the default value will be used. Default value: `SAST-FULL`  Acceptable values: - `SAST-FULL` - `SAST-RAPID` | Optional (This parameter is optional for `SAST-FULL` scans, but it is **mandatory** for `SAST-RAPID` scans.) Important: Before you can test a project with Rapid Scan Static, a full SAST test (using the latest version of Coverity that Polaris supports) must be completed. If you attempt to run a rapid scan before a full SAST test is completed, Bridge starts a full SAST scan automatically. The full SAST scan must be run with the latest version of Coverity that Polaris supports. This ensures your project has the necessary baseline before performing rapid scans. |
2. Make your Polaris access token available as an environment variable.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
   ```

   Note: You can use either a user access token (created in the Polaris UI) or a service account token here.
3. Use the Bridge CLI to run a rapid scan.

   **Example:**

   ```
   bridge-cli --stage polaris polaris.project.name="<PROJECT_NAME>" \
   polaris.branch.name="<BRANCH_NAME>" \
   polaris.application.name="<APPLICATION_NAME>" \
   polaris.serverurl="<SERVERURL>" \
   polaris.assessment.types=SAST \
   polaris.test.sast.type=SAST-RAPID
   ```

   Important: Before you can test a project with Rapid Scan Static, a full SAST test (using the latest version of Coverity that Polaris supports) must be completed. If you attempt to run a rapid scan before a full SAST test is completed, Bridge starts a full SAST scan automatically. The full SAST scan must be run with the latest version of Coverity that Polaris supports. This ensures your project has the necessary baseline before performing rapid scans.
4. When the scan completes successfully, the results will be available in your Polaris dashboard.
