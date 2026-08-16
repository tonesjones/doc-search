---
title: "Using SAST Fix PRs with Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-sast-fix-prs-with-bridge.html"
content_id: "gnkQZukNM96vB6kcuVRgTA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:02.985309+00:00"
---

# Using SAST Fix PRs with Bridge

Bridge can create SAST Fix Pull Requests (Fix PRs) from Polaris SAST scan results in CI workflows. Each Fix PR contains an AI-generated code fix for one static analysis vulnerability detected by a full baseline SAST scan on a monitored branch, such as `main`, `develop`, `staging`, or `release`.

When a full baseline SAST scan completes on a monitored branch, Bridge evaluates eligible SAST issues, applies the Fix PR severity and count filters, and creates Fix PRs in the configured SCM repository. Each Fix PR contains an AI-generated fix for one selected SAST vulnerability.

If both SAST and SCA Fix PRs are enabled, SAST issues are evaluated before SCA issues. The `polaris.fixPR.maxCount` value applies across both SAST and SCA assessment types.

When Fix PRs are enabled, Bridge selects issues in the following order:

1. SAST issues are evaluated before SCA issues.
2. Dismissed issues are excluded.
3. The `polaris.fixPR.filter.severities` allow list is applied.
4. Issues are sorted by severity in descending order.
5. Issues with earlier first-detected dates are selected before newer issues. Issues without first-detected dates are selected last.
6. The first issues up to `polaris.fixPR.maxCount` are selected.

## Prerequisites

- Bridge CLI 4.5.0 or newer.
- Read the related information links:
  - Commands for integrating Bridge to connect with Polaris and a Source Code Management system (SCM) to raise Fix Pull Requests
  - Polaris prerequisites
- Access to the SCM repository where Bridge Polaris will create Fix PRs.
- To enable Bridge CLI to create Fix PRs in an SCM repository, an access token is required. This can be an ephemeral build token if Bridge CLI is used directly in a CI pipeline or a Personal Access Token (PAT).
- The following secrets are required:

  | Secret | Description |
  | --- | --- |
  | `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token to enable Bridge CLI to integrate with a Polaris server. |
  | Access token | A Source Code Management system (SCM) ephemeral build token or Personal Access Token (PAT) that allows Bridge to raise Fix PRs. The token should be configured with permission to create pull requests in the target repository. Consult Complete list of Bridge arguments to determine the Bridge environment variable for the appropriate SCM system, for example, `BRIDGE_GITHUB_USER_TOKEN` for GitHub. |

## Required parameters

The following configuration parameters are required for Polaris SAST Fix PRs.

| Parameter | Description |
| --- | --- |
| `BRIDGE_POLARIS_ACCESSTOKEN` | Environment variable that provides the Polaris access token at runtime. This value can be stored as a CI secret. |
| `polaris.serverUrl` | URL of the Polaris server. |
| `polaris.application.name` | Name of the Polaris application. |
| `polaris.project.name` | Name of the Polaris project. The type of Polaris project should support SAST scanning of branches. |
| `polaris.branch.name` | Name of the monitored branch, such as `main`. Note: If a SAST Fix PR scan is run on a pull request, Bridge CLI logs a warning and does not create Fix PRs. |
| `polaris.assessment.types` | Must include `SAST`, for example `SAST` or `SAST,SCA`. |
| `polaris.fixPR.enabled` | Must be set to `true` to enable Fix PRs. |

## Optional parameters

The following parameters are optional.

| Parameter | Description |
| --- | --- |
| `polaris.fixPR.filter.severities` | By default, Fix PRs are raised for `CRITICAL` and `HIGH` severity issues. This applies to **both** SAST and SCA. The severity filter can include any combination of `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW`, such as `MEDIUM,LOW`. |
| `polaris.fixPR.maxCount` | By default, a maximum count of five Fix PRs can be raised across both SAST and SCA scans, with SAST evaluated first. Dismissed issues are excluded, then the `polaris.fixPR.filter.severities` allow list is applied. Issues are sorted by severity (descending) and first-detected date (ascending, with undated issues last), and only the first `maxCount` results are selected. |
| `polaris.test.sast.location` | Controls where SAST capture and analysis are performed for Fix PR workflows.    Valid values are:   - `HYBRID` (default): Capture is performed locally and analysis is performed in Polaris. - `REMOTE`: Source code is uploaded to Polaris, where capture and analysis are performed.   `LOCAL` is not supported for SAST Fix PRs. |

## Instructions

Perform the following steps to create SAST Fix PRs with Bridge and Polaris.

1. Make the Polaris access token available as an environment variable or secret.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESS_TOKEN>
   ```
2. Make a source code repository access token available as an environment variable or secret.

   ```
   export BRIDGE_GITHUB_USER_TOKEN=<GITHUB_ACCESS_TOKEN>
   ```
3. Use Bridge CLI to run a SAST scan with Fix PRs enabled.

   Note: Bridge can integrate with a variety of Source Code Management (SCM) systems, such as GitHub, GitLab, and others. The examples demonstrate how to integrate with a GitHub repository to raise Fix PRs. Consult Complete list of Bridge arguments to discover the equivalent Bridge commands to use for the Source Code Management system in use by your organization.

   **JSON**

   Save the following text to a JSON file and give the file an appropriate name, such as `input.json`.

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
           "types": [
             "SAST"
           ]
         },
         "test": {
           "sast": {
             "location": "HYBRID"
           }
         },
         "fixPR": {
           "enabled": true,
           "filter": {
             "severities": "CRITICAL,HIGH"
           },
           "maxCount": 3
         }
       },
       "github": {
         "repository": {
           "name": "sample-repository",
           "owner": {
             "name": "<userid_or_orgid>"
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
   export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESS_TOKEN>"
   export BRIDGE_GITHUB_USER_TOKEN="<GITHUB_ACCESS_TOKEN>"

   bridge-cli --stage polaris --input input.json
   ```

   **Environment variables**

   ```
   export BRIDGE_POLARIS_SERVERURL="https://polaris.example.com"
   export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESS_TOKEN>"
   export BRIDGE_POLARIS_APPLICATION_NAME="sample-polaris-application"
   export BRIDGE_POLARIS_PROJECT_NAME="sample-polaris-project"
   export BRIDGE_POLARIS_BRANCH_NAME="main"
   export BRIDGE_POLARIS_ASSESSMENT_TYPES="SAST"
   export BRIDGE_POLARIS_TEST_SAST_LOCATION="HYBRID"
   export BRIDGE_POLARIS_FIXPR_ENABLED="true"
   export BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES="CRITICAL,HIGH"
   export BRIDGE_POLARIS_FIXPR_MAXCOUNT="3"
   export BRIDGE_GITHUB_REPOSITORY_NAME="sample-repository"
   export BRIDGE_GITHUB_REPOSITORY_OWNER_NAME="userid_or_orgid"
   export BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME="main"
   export BRIDGE_GITHUB_USER_TOKEN="<GITHUB_ACCESS_TOKEN>"
   ```

   Run Bridge CLI:

   ```
   bridge-cli --stage polaris
   ```

   **Command line**

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESS_TOKEN>"
   export BRIDGE_GITHUB_USER_TOKEN="<GITHUB_ACCESS_TOKEN>"

   bridge-cli \
     --stage polaris \
     polaris.serverUrl="https://polaris.example.com" \
     polaris.application.name="sample-polaris-application" \
     polaris.project.name="sample-polaris-project" \
     polaris.branch.name="main" \
     polaris.assessment.types="SAST" \
     polaris.test.sast.location="HYBRID" \
     polaris.fixPR.enabled=true \
     polaris.fixPR.filter.severities="CRITICAL,HIGH" \
     polaris.fixPR.maxCount=3 \
     github.repository.name="sample-repository" \
     github.repository.owner.name="userid_or_orgid" \
     github.repository.branch.name="main"
   ```

   The examples above use Bridge CLI to enable SAST Fix PRs with the following settings:

   - Fix PRs are raised for `CRITICAL` and `HIGH` severity SAST issues.
   - A maximum of three Fix PRs will be raised.
   - Each Fix PR contains an AI-generated code fix targeting a single SAST vulnerability.
4. Review Bridge logs.

   Bridge logs information about Fix PR creation, including the number of Fix PRs created and any issues that could not be fixed.
5. Verify that new Fix PRs were created for the configured branch.

Bridge creates Fix PRs in the configured source code repository for eligible SAST issues on the monitored branch.
