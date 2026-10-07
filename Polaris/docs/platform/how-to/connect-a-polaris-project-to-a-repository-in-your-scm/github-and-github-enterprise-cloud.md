---
title: "GitHub, GitHub Enterprise, and GitHub Enterprise with data residency"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/github-github-enterprise-and-github-enterprise-with-data-residency.html"
content_id: "7zCqxPvjbXHSNhNCLapPBQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:20.857114+00:00"
content_hash: "bf19f2931ab2b8da101d9302bff8e7332c799149841928c337b5fb5deaca5f89"
---

# GitHub, GitHub Enterprise, and GitHub Enterprise with data residency

How to connect a Polaris project to a repository in GitHub, GitHub Enterprise, or GitHub Enterprise with data residency.

Note: Follow the steps on this page to connect a single project to a single GitHub repository. Alternatively, GitHub repositories can be imported into Polaris in bulk. For more information, see [Connect Polaris to Multiple SCM Repositories](../connect-polaris-to-multiple-scm-repositories.md).

## Prerequisites

### Create a personal access token

Authentication between GitHub and Polaris is managed with a personal access token (PAT) that you create in GitHub. If you haven't done so already, follow the instructions in the GitHub documentation to create an access token: [GitHub > Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Important: To use Event-Based Test Automation in Polaris for SCM Integrations and Synchronizing Polaris with your SCM Provider, the token you use has different requirements, see [GitHub Tokens for SCM Bulk Integration and/or Monitoring](../github-tokens-for-scm-bulk-integration-and-or-monitoring.md).

When creating an access token:

- Set the token's expiration date. To avoid issues, we recommend No expiration.   
   [image: git expiration]
- Under Select scopes, access to repo is required.   
   [image: git select scope]

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

## Connect to a repository hosted in GitHub or GitHub Enterprise

To connect a project in Polaris to a repository in GitHub, GitHub Enterprise, or GitHub Enterprise with data residency, follow these steps:

1. In Polaris, open the project you wish to connect to a repository (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Cloud-hosted.
4. Select the source of your repository: GitHub, GitHub Enterprise, or GitHub Enterprise (with data residency).
5. Enter the Repository URL.

   To obtain the repository's URL, open the GitHub repository in a browser and select Code. Copy the HTTPS URL (SSH is not supported).   
    [image: git code clone]
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
