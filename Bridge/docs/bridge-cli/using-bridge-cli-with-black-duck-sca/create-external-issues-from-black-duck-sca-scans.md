---
title: "Create external issues from Black Duck SCA scans"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-external-issues-from-black-duck-sca-scans.html"
content_id: "kY8KPhxWve~9AOxaEIMAng"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:16.759833+00:00"
---

# Create external issues from Black Duck SCA scans

Configure Bridge CLI to create and manage repository issues from Black Duck® SCA scan findings. Development teams can quickly identify, track and remediate security issues directly within existing workflow tools.

External issues are automatically created from Black Duck® SCA scan findings based on configurable parameters. Issues can be generated from scan findings by specifying severity levels (such as `Critical` and `High`) and the maximum number of issues to create per scan.

Important: The feature currently supports creating issues in GitHub source code repositories.

Issues can optionally be grouped by component-version pair, allowing multiple related vulnerabilities affecting the same component to be tracked in a single issue rather than creating separate issues for each vulnerability.

## Prerequisites

- The following reading is recommended before starting:
  - External issues
  - Complete list of Black Duck® SCA Bridge commands
- Access to a Black Duck® SCA server with permission granted to create access tokens.
- A Black Duck® SCA access token to allow integration with a Black Duck® SCA server instance.
- Admin access to a GitHub source code repository.
- To enable Bridge CLI to create external source code repository issues an access token is required. Currently, issues can be created in GitHub repositories with support for GitHub Access Tokens:
  - Fine grained tokens require the `Issues` permission with `read/write` access.
  - GitHub classic tokens require the `repo` scope.

**List of parameters required for raising external issues from Black Duck® SCA scans**

| Parameter | Description | Required |
| --- | --- | --- |
| `--stage` | Use to specify that Bridge CLI integrates with Black Duck® SCA. | Mandatory |
| `blackducksca.url` | Black Duck® SCA server URL. | Mandatory |
| `blackducksca.externalIssues.create` | Set to `true` to enable creation of external repository issues from scan findings. Default is `false`. | Mandatory (set to `true` to enable creation of external issues ) |
| `blackducksca.externalIssues.severities` | List of severities for which repository issues should be created. Default: `["Critical", "High"]`. | Optional |
| `blackducksca.externalIssues.groupSCAIssues` | Set to `true` to group SCA issues by vulnerabilities of a component-version pair when creating repository issues. Set to `false` to create separate issues for each vulnerability. Default: `true`. | Optional |
| `blackducksca.externalIssues.maxCount` | Maximum number of repository issues to create per scan. Default: `10`. | Optional |
| `project.directory` | If `project.directory`  parameter is empty then Bridge will scan the source code in the current work directory (pwd) by default.  Use this parameter to specify the absolute path to the source code directory when the source is not available in the current working directory. | Optional |

**List of secrets required for raising external issues from Black Duck® SCA scans**

| Parameter | Description |
| --- | --- |
| `BRIDGE_BLACKDUCKSCA_TOKEN` | Black Duck® SCA access token to enable Bridge CLI to integrate with a Black Duck® SCA server. |
| `BRIDGE_GITHUB_USER_TOKEN` | Repository access token to allow Bridge CLI to create external repository issues. |

Bridge CLI provides configuration parameters for integration with external source code repositories. Support for creating external repository issues is provided for GitHub repositories.

## Instructions

1. Make the Black Duck® SCA access token available as an environment variable or secret.

   ```
   export BRIDGE_BLACKDUCKSCA_TOKEN=<BLACKDUCKSCA_TOKEN>
   ```

   Note: Use either a user access token (created in the Black Duck® SCA UI) or an API token with appropriate permissions.
2. Make a source code repository access token available as an environment variable or secret.

   ```
   export BRIDGE_GITHUB_USER_TOKEN=<GITHUB_ACCESSTOKEN>
   ```
3. Use Bridge CLI to run a scan with creation of external repository issues enabled.

   **JSON configuration**

   ```
   {
     "data": {
       "blackducksca": {
         "url": "https://blackduck.example.com",
         "externalIssues": {
           "create": true,
           "severities": [
             "Critical",
             "High"
           ],
           "groupSCAIssues": true,
           "maxCount": 20
         }
       },
       "github": {
         "repository": {
           "name": "repo",
           "owner": {
             "name": "userid_or_orgid"
           },
           "branch": {
             "name": "main"
           }
         }
       }
     }
   }

   # ensure that BRIDGE_BLACKDUCKSCA_TOKEN and BRIDGE_GITHUB_USER_TOKEN
   # secrets are set
   bridge --stage blackducksca --input input.json
   ```

   **Environment variables**

   ```
   export BRIDGE_BLACKDUCKSCA_TOKEN="<BLACKDUCKSCA_TOKEN>"
   export BRIDGE_BLACKDUCKSCA_URL="https://blackduck.example.com"
   export BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_CREATE=true
   export BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_SEVERITIES="Critical,High"
   export BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_GROUPSCAISSUES=true
   export BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_MAXCOUNT=20

   export BRIDGE_GITHUB_REPOSITORY_NAME="repo"
   export BRIDGE_GITHUB_OWNER_NAME="userid_or_orgid"
   export BRIDGE_GITHUB_BRANCH_NAME="main"
   export BRIDGE_GITHUB_USER_TOKEN="<GITHUB_ACCESS_TOKEN_SECRET>"

   bridge --stage blackducksca
   ```

   **Command-line**

   ```
   # ensure that BRIDGE_BLACKDUCKSCA_TOKEN and BRIDGE_GITHUB_USER_TOKEN
   # secrets are set

   bridge --stage blackducksca \
     blackducksca.url="https://blackduck.example.com" \
     blackducksca.externalIssues.create=true \
     blackducksca.externalIssues.severities=Critical,High \
     blackducksca.externalIssues.groupSCAIssues=true \
     blackducksca.externalIssues.maxCount=20 \
     github.repository.name="repo" \
     github.repository.owner.name="userid_or_orgid" \
     github.repository.branch.name="main"
   ```

   The examples above show how to configure Bridge CLI to create GitHub issues for `Critical` and `High` severity findings from SCA scans. SCA issues are grouped by component-version pair and a maximum of 20 issues will be created per scan.
4. Review the scan results.

   When the scan completes successfully, repository issues will be automatically created for SCA findings that meet your configured criteria. The issues will be available in the connected repository's issue tracker.
