---
title: "Create external issues from Polaris scans"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-external-issues-from-polaris-scans.html"
content_id: "R07wexfykgJYgFGVVbHYsQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:08.773319+00:00"
---

# Create external issues from Polaris scans

Configure Bridge CLI to create and manage repository issues from Polaris SAST and SCA findings. Development teams can quickly identify, track and remediate security issues directly within existing workflow tools.

External issues are automatically created from Polaris scan findings based on configurable parameters. Issues can be generated from scan findings by specifying severity levels (such as `Critical` and `High`), assessment types (`SAST`, `SCA` or both) and the maximum number of issues to create per scan.

Important: External issues are supported for GitHub source code repositories.

For SCA findings, issues can optionally be grouped by component-version pair, allowing multiple related vulnerabilities affecting the same component to be tracked in a single issue rather than creating separate issues for each vulnerability.

## Prerequisites

- The following reading is recommended before starting:
  - External issues
  - Complete list of Polaris Bridge commands
- Access to a Polaris server with permission granted to create access tokens and projects.
- Access to a source code repository.
- A [Polaris access token](hhttps://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0d97d272fb42796be0f9f52928a17d57.topic) or [service account token](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ae0e60062f785563c1907b533597e5dd.topic) to allow integration with a Polaris server instance.
- Admin access to a GitHub source code repository.
- To enable Bridge CLI to create external source code repository issues an access token is required. Currently, issues can be created in GitHub repositories with support for GitHub Access Tokens:
  - Fine grained tokens require the `Issues` permission with `read/write` access.
  - GitHub classic tokens require the `repo` scope.
- Use the tables below to identify the parameters and secrets required for raising external issues from Polaris scans.

**List of parameters for raising external issues from Polaris scans**

| Parameter | Description | Required |
| --- | --- | --- |
| --stage | Use to specify that Bridge CLI integrates with Polaris. | Mandatory |
| polaris.serverurl | Polaris server URL. | Mandatory |
| polaris.application.name | Name for Polaris application. The specified application must exist on Polaris with appropriate entitlements. | Mandatory |
| polaris.assessment.types | List of Polaris test assessment types:  - `SAST` - `SCA` - `SAST, SCA` | Mandatory |
| polaris.project.name | Name for Polaris project. If the project doesn't exist it will be created. | Mandatory |
| polaris.branch.name | Branch name in the Polaris server. If the branch doesn't exist it will be created. | Mandatory |
| polaris.externalIssues.create | Set to `true` to enable creation of external repository issues from scan findings. Default is `false`. | Mandatory (set to `true` to enable creation of external issues ) |
| polaris.externalIssues.severities | List of severities for which repository issues should be created. Default: `["Critical", "High"]`. | Optional |
| polaris.externalIssues.types | List of assessment types for which repository issues should be created. Acceptable values: `SAST`, `SCA`. | Optional |
| polaris.externalIssues.groupSCAIssues | Set to `true` to group SCA issues by vulnerabilities of a component-version pair when creating repository issues. Set to `false` to create separate issues for each vulnerability. Default: `true`. | Optional |
| polaris.externalIssues.maxCount | Maximum number of repository issues to create per scan. Default: `10`. | Optional |
| project.directory | If `project.directory`  parameter is empty then Bridge will scan the source code in the current work directory (pwd) by default.  Use this parameter to specify the absolute path to the source code directory when the source is not available in the current working directory. | Optional |

**List of secrets required for raising external issues from Polaris scans**

|  | Description |
| --- | --- |
| `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token to enable Bridge CLI to integrate with a Polaris server. |
| `BRIDGE_GITHUB_USER_TOKEN` | Repository access token to allow Bridge CLI to create external repository issues. |

Bridge CLI provides configuration parameters for integration with external source code repositories. Support for creating external repository issues is provided for GitHub repositories.

## Instructions

1. Make the Polaris access token available as an environment variable or secret.

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
   ```

   Note: Use either a user access token (created in the Polaris UI) or a service account token.
2. Make a source code repository access token available as an environment variable or secret.

   ```
   export BRIDGE_GITHUB_USER_TOKEN=<GITHUB_ACCESSTOKEN>
   ```
3. Use Bridge CLI to run a scan with creation of external repository issues enabled.

   **JSON configuration**

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
           "types": "SAST,SCA"
         },
         "externalIssues": {
           "create": true,
           "severities": [
             "Critical",
             "High"
           ],
           "types": [
             "SAST",
             "SCA"
           ],
           "groupSCAIssues": true,
           "maxCount": 20
         }
       },
       "github": {
         "repository": {
           "name": "blackduck-polaris-ghub-integration",
           "owner": {
             "name": "sppears"
           },
           "branch": {
             "name": "main"
           }
         }
       }
     }
   }

   # ensure that BRIDGE_POLARIS_ACCESSTOKEN and BRIDGE_GITHUB_USER_TOKEN
   # secrets are set
   bridge --stage polaris --input input.json
   ```

   **Environment variables**

   ```
   export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESS_TOKEN_SECRET>"
   export BRIDGE_POLARIS_SERVERURL="https://polaris.example.com"
   export BRIDGE_POLARIS_APPLICATION_NAME="sample-polaris-application"
   export BRIDGE_POLARIS_PROJECT_NAME="sample-polaris-project"
   export BRIDGE_POLARIS_BRANCH_NAME="main"
   export BRIDGE_POLARIS_ASSESSMENT_TYPES="SAST,SCA"
   export BRIDGE_POLARIS_EXTERNAL_ISSUES_CREATE="true"
   export BRIDGE_POLARIS_EXTERNAL_ISSUES_SEVERITIES="Critical,High"
   export BRIDGE_POLARIS_EXTERNAL_ISSUES_TYPES="SAST,SCA"
   export BRIDGE_POLARIS_EXTERNAL_ISSUES_GROUPSCAISSUES="true"
   export BRIDGE_POLARIS_EXTERNAL_ISSUES_MAX_COUNT="20"
   export BRIDGE_GITHUB_REPOSITORY_NAME="repo"
   export BRIDGE_GITHUB_REPOSITORY_OWNER_NAME="userid_or_orgid"
   export BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME="main"
   export BRIDGE_GITHUB_USER_TOKEN="<GITHUB_ACCESS_TOKEN_SECRET>"

   bridge --stage polaris
   ```

   **Command-line**

   ```
   # ensure that BRIDGE_POLARIS_ACCESSTOKEN and BRIDGE_GITHUB_USER_TOKEN
   # secrets are set

   bridge --stage polaris \
     polaris.serverUrl="https://polaris.example.com" \
     polaris.application.name="sample-polaris-application" \
     polaris.project.name="sample-polaris-project" \
     polaris.branch.name="main" \
     polaris.assessment.types="SAST,SCA" \
     polaris.externalIssues.create=true \
     polaris.externalIssues.severities=Critical,High \
     polaris.externalIssues.types=SAST,SCA \
     polaris.externalIssues.groupSCAIssues=true \
     polaris.externalIssues.maxCount=20 \
     github.repository.name="repo" \
     github.repository.owner.name="userid_or_orgid" \
     github.repository.branch.name="main"
   ```

   The examples above show how to configure Bridge CLI to create GitHub issues for `Critical` and `High` severity findings from both `SAST` and `SCA` scans. SCA issues are grouped by component-version pair and a maximum of 20 issues will be created per scan. These settings can be adjusted based on organization workflow and preferences.
4. Review the scan results.

   When the scan completes successfully, repository issues will be automatically created for findings that meet your configured criteria. The issues will be available in the connected repository's issue tracker.
