---
title: "GitLab Self-Managed"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-self-managed.html"
content_id: "6_Yk_lzXG8xdYQyc9k1RRQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:24.672142+00:00"
content_hash: "4c650339c2add24129c17da31594c98de9a2be916cadd1d2f418f21c133de842"
---

# GitLab Self-Managed

How to connect a Polaris project to a repository in GitLab Self-Managed.

## Prerequisites

### Domains and IPs

To connect a project to a repository hosted in GitLab Self-Managed, you must add the integration IPs for Polaris to your allow list. See Integrations for more information.

### Create an access token

Authentication between GitLab and Polaris is managed with an access token that you create in GitLab. If you haven't done so already, follow the instructions in the GitLab documentation to create an access token: [GitLab Docs > GitLab token overview](https://docs.gitlab.com/security/tokens/).

When creating an access token:

- Set the token's expiration date. To avoid issues, we recommend No expiration.
- Select the role (for Project/Group Access Tokens). Select any role above “Guest”.
- Under Select scopes, select read\_repository and read\_api.   
   [image: gitlab select scopes]

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

## Connect to a repository hosted in GitLab self-managed

To connect a project in Polaris to a repository in GitLab self-managed, follow these steps:

1. In Polaris, open the project you wish to connect to a repository (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Self-hosted.
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
