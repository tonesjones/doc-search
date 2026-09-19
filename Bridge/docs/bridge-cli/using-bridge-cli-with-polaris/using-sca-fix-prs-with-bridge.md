---
title: "Using SCA Fix PRs with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-sca-fix-prs-with-bridge.html"
content_id: "mJXuqqevpdNQu8yjbbc6tA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:03.626909+00:00"
---

# Using SCA Fix PRs with Bridge

Bridge can create Fix Pull Requests from Polaris SCA scan results in CI workflows. Fix Pull Requests update dependency versions in a repository based on upgrade guidance from Polaris SCA scans on branches, e.g. `main`, `develop`, `staging` or `release`.

Note:

Fix PRs are intended for use with scans on monitored branches. If Fix PRs are enabled for a Pull Request scan, Bridge logs a warning and skips the Fix PR workflow:

`fixPR is enabled, but this is a Pull Request scan. Will skip Fix PR workflow.`

## Prerequisites

- Bridge CLI 4.1.2 or newer
- Read the related information links:
  - Using Fix Pull Requests with Bridge.
  - Commands for integrating Bridge to connect with Polaris and a Source Code Management system to raise Fix Pull Requests.
  - Prerequisites for Bridge to integrate with Polaris.
  - Package managers supported by Detect for Component Location Analysis, e.g. NPM, Maven, Gradle, NuGet, Go modules etc.
- Access to a source code repository.
- To enable Bridge CLI  to create Fix Pull Requests in a source code repository, an access token is required. This can be an ephemeral build token if Bridge CLI is used directly in a CI pipeline or a Personal Access Token (PAT) token.
- The following secrets are required:

  | Secret | Description |
  | --- | --- |
  | `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token to enable Bridge CLI to integrate with a Polaris server. |
  | Access token | Source Code Management system ephemeral build token or Personal Access Token (PAT) that allows Bridge to raise Fix Pull Requests. Consult related information to determine the Bridge environment variable for the appropriate SCM system, for example, `BRIDGE_GITHUB_USER_TOKEN` for GitHub. |

## Instructions

Perform the following steps to use Fix Pull Requests with Bridge Polaris

1. Make the Polaris access token available as an environment variable or secret.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
   ```
2. Make a source code repository access token available as an environment variable or secret.

   ```
   export BRIDGE_GITHUB_USER_TOKEN=<GITHUB_ACCESSTOKEN>
   ```
3. Use Bridge CLI to run a scan with Fix Pull Requests enabled.

   Note: Bridge can integrate with a variety of Source Code Management systems, such as GitHub, GitLab and others. The examples provided demonstrate how to integrate with a GitHub repository to raise Fix Pull Requests. Consult the related information to discover the equivalent Bridge commands to use for the Source Code Management system in use by your organization.

   **JSON**

   Save the following text to a JSON file and give the file an appropriate name, e.g., `input.json`.

   ```
   {
     "data": {
       "polaris": {
         "serverUrl": "https://polaris.example.com",
         "application": {
           "name": "sample-polaris-application"
         },
         "project": {
           "name": "sample-polaris-project"
         },
         "branch": {
           "name": "main"
         },
         "assessment": {
             "types": [ "SCA" ]
         },
         "fixPR": {
           "enabled": true,
           "useUpgradeGuidance": "SHORT_TERM,LONG_TERM",
           "filter": {
             "severities": "CRITICAL,HIGH"
           },
           "maxCount": 3
         }
       },
       "github": {
         "repository": {
           "name": "blackduck-polaris-ghub-integration",
           "owner": {
             "name": "<userid or orgid>"
           },
           "branch": {
             "name": "main"
           }
         }
       }
     }
   }
   ```

   Run Bridge CLI:

   ```
   bridge-cli --stage polaris --input input.json
   ```

   **Environment variables**

   ```
   export BRIDGE_POLARIS_SERVERURL="https://polaris.example.com"
   export BRIDGE_POLARIS_ACCESSTOKEN="$POLARIS_ACCESS_TOKEN"
   export BRIDGE_POLARIS_APPLICATION_NAME="sample-polaris-application"
   export BRIDGE_POLARIS_PROJECT_NAME="sample-polaris-project"
   export BRIDGE_POLARIS_BRANCH_NAME="main"
   export BRIDGE_POLARIS_ASSESSMENT_TYPES="SCA"

   export BRIDGE_POLARIS_FIXPR_ENABLED="true"
   export BRIDGE_POLARIS_FIXPR_USEUPGRADEGUIDANCE="SHORT_TERM,LONG_TERM"
   export BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES="CRITICAL,HIGH"
   export BRIDGE_POLARIS_FIXPR_MAXCOUNT="3"

   export BRIDGE_GITHUB_REPOSITORY_NAME="repo"
   export BRIDGE_GITHUB_REPOSITORY_OWNER_NAME="userid_or orgid"
   export BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME="main"
   export BRIDGE_GITHUB_USER_TOKEN="<GITHUB_ACCESS_TOKEN_SECRET>"
   ```

   Run Bridge CLI:

   ```
   bridge-cli --stage polaris
   ```

   **Command line**

   ```
   bridge-cli \
     --stage polaris \
     polaris.serverUrl="https://polaris.example.com" \
     polaris.accessToken="$POLARIS_ACCESS_TOKEN" \
     polaris.application.name="sample-polaris-application" \
     polaris.project.name="sample-polaris-project" \
     polaris.branch.name="main" \
     polaris.assessment.types="SCA" \
     polaris.fixPR.enabled=true \
     polaris.fixPR.useUpgradeGuidance=SHORT_TERM,LONG_TERM \
     polaris.fixPR.filter.severities=CRITICAL,HIGH \
     polaris.fixPR.maxCount=3 \
     github.repository.name="repo" \
     github.repository.owner.name="userid_or_orgid" \
     github.repository.branch.name="main"
   ```

   The examples above use Bridge CLI  to enable Fix Pull Requests with the following preferences:
   - Upgrades are prioritized using the following order of preference for guidance:
   - 1. Short term
     2. Long term
   - Fix Pull requests are raised for Critical and High severity issues.
   - A maximum of 3 Fix Pull requests will be raised.
4. Review logs

   Bridge logs information about Fix Pull Request creation, including the number of Fix Pull Requests created and any dependencies that could not be updated.
5. Verify that new Fix Pull Requests were created that target the configured branch.

**Related information**  

- [Component Location Analysis](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/cee7c27eec87b30256f5416105092de1.topic)

**Target**  

- Fix pull requests (Fix PRs)
- Complete list of Bridge arguments
- Polaris prerequisites
