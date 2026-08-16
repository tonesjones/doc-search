---
title: "Azure Repos"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/azure-repos.html"
content_id: "CJ_F_cSVpXpUgaQnCykTeg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:19.470658+00:00"
content_hash: "0ab8c119728845f8e4cdf82378d0a93f056c000660b0304c17028832420152ff"
---

# Azure Repos

How to connect a Polaris project to a repository in Azure DevOps.

## Prerequisites

### Create a personal access token

Authentication between Azure Repos and Polaris is managed with a personal access token (PAT) that you create in Azure DevOps. If you haven't done so already, follow the instructions in the Azure DevOps documentation to create an access token: [Use personal access tokens > Create a PAT](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows#create-a-pat).

Important: To use Event-Based Test Automation in Polaris for SCM Integrations and Synchronizing Polaris with your SCM Provider, the token you use has different requirements, see [Azure Tokens for SCM Bulk Integration and/or Monitoring](../azure-tokens-for-scm-bulk-integration-and-or-monitoring.md).

When creating an access token:

- From Settings pulldown, select **Personal Access Token**.
- Click **+New Token**.
- Enter a Name for the token and select your Organization.
- Set the token's expiration date.
- Enable the Read scope (under Code).   
   [image: azure create token]

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

### Naming imported repositories

Important: When you import a Git repository from a third-party SCM provider into your Azure DevOps project, Azure DevOps may append ".git" to the end of the repository's name. When this occurs, Polaris will not accept the repository's URL.

To rename an imported repository, follow these steps:

1. In Azure DevOps, go to Project settings > Repositories.
2. Select the repository you wish to rename.
3. Select Rename.
4. Remove ".git" from the repository's name and select Rename.

   [image: scm integ azure rename repo]
5. Click Import.

## Connect to a repository in Azure Repos

To connect a project in Polaris to a repository in Azure Repos, follow these steps:

1. In Polaris, open the project you wish to connect to a repository (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Cloud-hosted.
4. Select the source of your repository: Azure Repos.
5. Enter the Repository URL.

   To obtain the repository's URL, open the repository in a browser and select Clone. Copy the HTTPS URL (SSH is not supported).   
    [image: azure clone]
6. Enter the Repository Access Token.
7. Click Test your Connection. A spinning circle indicates the test is in progress.
8. If your connection is successful, click Save.

   If your connection test is unsuccessful, check the following and retry:

   1. Your network connection is stable.
   2. Check the Repository URL and Access Token to make sure they are accurate.
   3. Check that the Repository Access Token is still valid and has not expired.
   4. Check that you selected the correct provider for your source repository.

## Next steps

Now, you can scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
