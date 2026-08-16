---
title: "Azure Tokens for SCM Bulk Integration and/or Monitoring"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/azure-tokens-for-scm-bulk-integration-and/or-monitoring.html"
content_id: "tz3K9xQqEHntCoaQ63wgLQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:15.170245+00:00"
content_hash: "e0d465d03ffd5825eed4f2f06bb60366b3157e85b58e96b6518043bf1286c5a8"
---

# Azure Tokens for SCM Bulk Integration and/or Monitoring

## Overview

How to create a token for bulk onboarding and monitoring features via SCM Integrations. Monitoring includes Synchronizing Polaris with your SCM Provider and Event-Based Test Automation in Polaris for SCM Integrations.

Note: Available for Azure Repos.

### Creating a personal access token

When integrating SCM repositories, you will need a personal access token you create in Azure DevOps.

Authentication between Azure Repos and Polaris is managed with a personal token that you create in Azure DevOps. If you haven't done so already, create an access token. For additional information: [Use personal access tokens > Create a PAT](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows#create-a-pat)

Important: Token must be created by an Azure DevOps **Organization Owner** or users with the "Manage organization webhooks" permission, who are authorized to manage organization webhooks. Although other Azure users may be able to select the scope requirements when creating a token, the token will not work due to permission requirements in Azure to manage organization webhooks.

1. From Settings pulldown, select Personal Access Token.
2. Click +New Token.
3. Enter a Name for the token.
4. Under Organization, select All accessible organizations.
5. Set the token's expiration date.
6. For scopes, select Custom defined.
   1. Under **Code**, select **Read & Write**.

      [image: azure scope a]
   2. Under **Project and Team**, select **Read & Write**.

      [image: azure scope b]

   Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

### Next Steps

Use this token to connect to Polaris:

- Connect a Polaris project to a repository in your SCM
- Connect Polaris to Multiple SCM Repositories

After the connection is established:

- Synchronizing Polaris with your SCM Provider
- Event-Based Test Automation in Polaris for SCM Integrations

You can also scan on demand (see [How to test from the web UI](how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](create-and-manage-policies/test-scheduling-policies.md)).

Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
