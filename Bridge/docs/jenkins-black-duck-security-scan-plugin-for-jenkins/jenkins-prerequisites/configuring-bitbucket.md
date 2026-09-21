---
title: "Configuring Bitbucket"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/configuring-bitbucket.html"
content_id: "41WGODcOTgZI1ihz3o7aFQ"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:32.786593+00:00"
---

# Configuring Bitbucket

## Configure Bitbucket HTTP access tokens

The `bitbucket_token` variable is required to configure jobs and submit PR comments. Note that repository-level tokens do not behave in the same way as account-level tokens.

|  |  |  |
| --- | --- | --- |
|  | Account-level token | Repository-level token |
| Configure a job | Required | N/A |
| Submit PR comment | - Must hold project permissions such as "Project write" or "Project admin." - Token can be used on the project level and repository level. | - Must hold repository permissions such as "Repository write" or "Repository admin." - This token is used only when working at the repository level. |

## Generate an account-level Bitbucket token

Remember to store the token after making it, because Bitbucket will not save the token for you.

1. Click your Profile Photo, then Manage Account > HTTP Access Tokens > Create token.
2. Enter a Token name.

   Default settings are fine, or you can change the project and repository permissions, as needed.
3. Click the Create button. The token will be generated.
4. Store the token.

## Generate a repository-level Bitbucket token

Remember to store the token after making it, because Bitbucket will not save the token for you.

1. Navigate to your Bitbucket repository.
2. Click the Repository Settings icon.
3. Click the HTTP access tokens.
4. Click the Create token button.
5. Enter the token name.
6. Click the Create button to make the token.
7. Store the token.

## Webhook creation and configuration for Bitbucket

For instructions on how to create and configure the webhook for Bitbucket, click [here](https://confluence.atlassian.com/bitbucketserver/manage-webhooks-938025878.html).

## Configuring Bitbucket Cloud

To configure a job in Jenkins with Bitbucket Cloud, it is necessary to provide a Bitbucket API token created with scopes having Repositories and Pull Requests Read/Write permissions.

## Submitting PR comments in Bitbucket Cloud

The Black Duck Security Scan plugin provides a UI field to configure a Bitbucket Token / username and Password (Manage Jenkins > System > Black Duck Security Scan > Configure Source Code Management Token > Bitbucket).

This field provides a global configuration for all pipelines, accepting either secret text or a username with password credential.

Bitbucket Cloud provides several types of access tokens that can be configured using `bitbucket_username` and/or `bitbucket_token` parameters.

1. **Bitbucket access token**: For using **repository**, **workspace** and **project** access tokens, select the `Secret text` credential option to set the Bitbucket Token. Alternatively, provide a pipeline-specific token by setting the `bitbucket_token` parameter directly in the Jenkinsfile.
2. **Bitbucket API token**: Select the `Username with
   password` credential option. Set the username as the Bitbucket email and the password as the Bitbucket API Token. Alternatively, to provide a pipeline-specific Bitbucket API Token, set the `bitbucket_username` and `bitbucket_token` parameters in the Jenkinsfile.

   Important: The `bitbucket_username` parameter must be set to the Bitbucket email address when using a Bitbucket API Token.

   **Supported Bitbucket authentications**

   | Access token | Recommended use |
   | --- | --- |
   | [**Repository access token**](https://support.atlassian.com/bitbucket-cloud/docs/repository-access-tokens/) | - Access required to a single repository - Use `bitbucket_token` to set Repository Access Token |
   | [**Project access token (Bitbucket premium)**](https://support.atlassian.com/bitbucket-cloud/docs/project-access-tokens/) | - Access required to all repositories within a project - Use `bitbucket_token` to set Project Access Token |
   | [**Workspace access token (Bitbucket premium)**](https://support.atlassian.com/bitbucket-cloud/docs/workspace-access-tokens/) | - Access required to all projects and repositories in a workspace - Use `bitbucket_token` to set Workspace Access Token |
   | [**API Token (Recommended)**](https://support.atlassian.com/bitbucket-cloud/docs/using-api-tokens/) | - Requires `bitbucket_username` set to Bitbucket email address - Use `bitbucket_token` to set Bitbucket API Token - Recommended for new integrations |
   | [**App Password (Deprecated)**](https://www.atlassian.com/blog/bitbucket/bitbucket-cloud-transitions-to-api-tokens-enhancing-security-with-app-password-deprecation) | - Requires `bitbucket_username` set to Bitbucket username - Switch to API tokens before June 9th, 2026 |

   **App Password deprecation timeline**

   - New Bitbucket app passwords cannot be created after September 9th, 2025.
   - Existing app passwords will continue to work until June 9th, 2026.
   - All integrations must switch to API tokens before June 9th, 2026 to avoid disruption.
