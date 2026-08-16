---
title: "GitLab SaaS"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-saas.html"
content_id: "0TnK6iPnWQY44~W6Pz~s0Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:23.765282+00:00"
content_hash: "c6e64147035496cd00875492ccee241e5e6204d6ef3c36fa24eb8bdc5c426e36"
---

# GitLab SaaS

How to connect a Polaris project to a repository in GitLab SaaS.

## Prerequisites

### Create an access token

Authentication between GitLab and Polaris is managed with an access token that you create in GitLab. If you haven't done so already, follow the instructions in the GitLab documentation to create an access token: [GitLab Docs > GitLab token overview](https://docs.gitlab.com/security/tokens/).

Important: To use Event-Based Test Automation in Polaris for SCM Integrations and Synchronizing Polaris with your SCM Provider, the token you use has different requirements, see [GitLab Tokens for SCM Bulk Integration and/or Monitoring](../gitlab-tokens-for-scm-bulk-integration-and-or-monitoring.md).

When creating an access token:

- Select your avatar.
- Select **Edit profile**.
- On the left sidebar, select **Access tokens**.
- Select **Add new token**.
- Set the token's expiration date. We recommend setting a maximum expiration period, to avoid issues.
- Select the role (for Project/Group Access Tokens). Select any role above “Guest”.
- Under Select scopes, select read\_repository and read\_api.   
   [image: gitlab select scopes]

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

## Connect to a repository in GitLab SaaS

To connect a project in Polaris to a repository in GitLab SaaS, follow these steps:

1. In Polaris, open the project you wish to connect to a repository (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Cloud-hosted.
4. Select the source of your repository: GitLab.
5. Enter the Repository URL.

   To obtain the repository's URL, open the GitLab repository in a browser and select Clone. Copy the HTTPS URL (SSH is not supported).   
    [image: gitlab clone]
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
