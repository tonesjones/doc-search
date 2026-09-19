---
title: "Setting up Black Duck Security Scan Pipe"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/setting-up-black-duck-security-scan-pipe.html"
content_id: "cirZ13ZsgavAgCq7gxzp3w"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:48:59.402730+00:00"
---

# Setting up Black Duck Security Scan Pipe

Before configuring Black Duck Security Scan Pipe for Bitbucket into your workflow, you must meet the following prerequisites:

## Compatibility & requirements

- Linux ARM architectures are supported, with Bridge version 3.5.1 or later. Linux ARM is supported for Coverity scans only.
- ARM-based pipelines must use a Docker image that supports ARM architecture For example, you may use `atlassian/default-image:4` or a later version. More details can be found at the Atlassian blog here: <https://www.atlassian.com/blog/bitbucket/announcing-support-for-linux-arm-runners-in-bitbucket-pipelines>
- The integration supports both public and private docker images from Docker Hub and internal Docker registries. Ensure proper authentication is configured for private images. For authentication, use `DOCKER_USERNAME`, `DOCKER_PASSWORD` and `DOCKER_REGISTRY` as per your requirement.

## Setup Bitbucket pipeline

To setup a Bitbucket pipeline the **Pipelines** feature should be enabled within the repository:

1. **Enable Pipelines**: From the left navigation sidebar of a repository select Repository settings > Settings > Turn on Enable Pipelines.
2. **Add bitbucket-pipelines.yml**: Add a `bitbucket-pipelines.yml` file to the root of the repository.
3. **Push changes**: Push the bitbucket-pipelines.yml file and a Bitbucket runner will pick up the job and initiate the pipeline.

If access to Bitbucket Cloud is restricted due to corporate firewall rules or network policies, e.g. requiring VPN access to internal resources, a self-hosted runner may be necessary. Self-hosted runners can be configured either as **Workspace Runners** or **Repository Runners**:

| Type | Scope | Use case |
| --- | --- | --- |
| **Repository** | Single repository | Isolate builds to a single repository, e.g., handle sensitive credentials or unique build requirements. |
| **Workspace** | All repositories within a workspace | Centralize and reuse build environments across repositories that share infrastructure, reducing setup, duplication and maintenance overhead. |

See [Adding a new runner in Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/adding-a-new-runner-in-bitbucket/) for further details.

Note: Black Duck Security Scan Pipe for Bitbucket requires a **Linux** self-hosted runner, or the default **Cloud** runner, to provide the functionality for executing the pipe.

## Configure Bitbucket API token

The `BRIDGE_BITBUCKET_API_TOKEN` parameter is required to enable the features listed in the table below.

Table 1. Features that require BRIDGE_BITBUCKET_API_TOKEN parameter

| Platform | Pull Requests | | SARIF Upload |
| --- | --- | --- | --- |
| Comments | Fixes |
| Black Duck® SCA | ✅ | ✅ | ✅ |
| Coverity | ✅ | ❌ | ❌ |
| Polaris | ✅ | ✅ | ✅ |
| Software Risk Manager | ❌ | ❌ | ❌ |

The `BRIDGE_BITBUCKET_API_TOKEN` parameter accepts two types of Bitbucket access tokens:

- **Access tokens**: Repository, project or workspace-scoped tokens that provide controlled access. Requires `pullrequest:write` scope.
- **API tokens (user level access)**: Single purpose access tokens, for example CI/CD tools, for use with Bitbucket Cloud.

Table 2. Supported Bitbucket access tokens

| Access Token | Recommended Use |
| --- | --- |
| **[Repository access token](https://support.atlassian.com/bitbucket-cloud/docs/repository-access-tokens/)** | Access required to a single repository |
| [**Project access token (Bitbucket Premium)**](https://support.atlassian.com/bitbucket-cloud/docs/project-access-tokens/) | Access required to all repositories within a project |
| [**Workspace access token (Bitbucket Premium)**](https://support.atlassian.com/bitbucket-cloud/docs/workspace-access-tokens/) | Access required to all projects and repositories in a workspace |

Table 3. Supported API tokens (user level access)

| Token Type | Notes |
| --- | --- |
| [**API Token (Recommended)**](https://support.atlassian.com/bitbucket-cloud/docs/using-api-tokens/) | - Requires `BRIDGE_BITBUCKET_API_USER_NAME` set to Bitbucket email address - Recommended for new integrations |
| [**App Password (Deprecated)**](https://www.atlassian.com/blog/bitbucket/bitbucket-cloud-transitions-to-api-tokens-enhancing-security-with-app-password-deprecation) | - Requires `BRIDGE_BITBUCKET_API_USER_NAME` set to Bitbucket username - Switch to API tokens before June 9th, 2026 |

**App Password deprecation timeline:**

- New Bitbucket app passwords cannot be created after September 9th, 2025.
- Existing app passwords will continue to work until June 9th, 2026.
- All integrations must switch to API tokens before June 9th, 2026 to avoid disruption.
