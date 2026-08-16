---
title: "GitHub Enterprise Server"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/github-enterprise-server.html"
content_id: "fKp8SWVkBXUJOHwDGDCrqA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:22.879898+00:00"
content_hash: "3081b3a24f7c8d777206d3aa4ae9e3f7b6b9302e74ee4bd51984ee46df86fbdd"
---

# GitHub Enterprise Server

How to connect a Polaris project to a repository in GitHub Enterprise Server.

Note: Follow the steps on this page to connect a single project to a single GitHub repository. Alternatively, GitHub repositories can be imported into Polaris in bulk. For more information, see [Connect Polaris to Multiple SCM Repositories](../connect-polaris-to-multiple-scm-repositories.md).

## Prerequisites

### Domains and IPs

To connect a project to a repository hosted in GitHub Enterprise Server, you must add the integration IPs for Polaris to your allow list. See Integrations for more information.

### Create a personal access token

Authentication between GitHub and Polaris is managed with a personal access token (PAT) that you create in GitHub. If you haven't done so already, follow the instructions in the GitHub documentation to create an access token: [GitHub Enterprise Docs > Creating a personal access token](https://docs.github.com/en/enterprise-server@3.8/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token).

When creating an access token:

- Set the token's expiration date. To avoid issues, we recommend No expiration.   
   [image: git expiration]
- Under Select scopes, access to repo is required.   
   [image: git select scope]

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

Important: To use the event-based test automation feature or synchronize the repository with Polaris, the token you use requires additional scopes (read:org (under admin:org), and admin:org\_hook). See [Event-Based Test Automation in Polaris for SCM Integrations](../event-based-test-automation-in-polaris-for-scm-integrations.md) and Synchronizing Polaris with your SCM Provider for more information.

## Connect to a repository hosted in GitHub Enterprise Server

To connect a project in Polaris to a repository in GitHub Enterprise Server, follow these steps:

1. In Polaris, open the project you wish to connect to a repository (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Self-hosted.
4. Select the source of your repository: GitHub.
5. Enter the private Repository URL.

   To obtain the repository's URL, open the GitHub repository in a browser and select Code. Copy the HTTPS URL (SSH is not supported).   
    [image: git code clone]
6. If using a secure tunnel, check URL is in a private network and select a secure tunnel from pull-down menu.
7. Enter the Repository Access Token.
8. Click Test your Connection. A spinning circle indicates the test is in progress.
9. If your connection is successful, click Save.

   If your connection test is unsuccessful, check the following and retry:

   1. Your network connection is stable.
   2. Check the Repository URL and Access Token to make sure they are accurate.
   3. Check that the Repository Access Token is still valid and has not expired.
   4. Check that Polaris external IP addresses have been added to your firewall allow list.
   5. Check that you selected the correct provider for your source repository.

## Next steps

Now, you can scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
