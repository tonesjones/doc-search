---
title: "GitLab Self-Managed"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-self-managed.html"
content_id: "6_Yk_lzXG8xdYQyc9k1RRQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:20.958637+00:00"
content_hash: "64709aa77d332b2b7bb9cd25f9958931345faf5773f2c288aa2cb750f55ce038"
---

# GitLab Self-Managed

How to connect a Polaris project to a project in GitLab Self-Managed. This can be done either by creating a secure tunnel or by adding the Polaris integration IPs to your allow list.

Note: SCA Fix Pull Requests are supported for repositories hosted in GitLab Self-Managed. Polaris creates the merge request over the Secure Tunnel that connects it to your private network. See [SCA Fix Pull Requests](../fix-pull-requests-fix-pr.md).

Note: This page describes how to connect a single Polaris project to a single GitLab project. GitLab projects can also be imported into Polaris in bulk. For more information, see GitLab Self-Managed.

## Prerequisites

### Secure tunnel

If you plan to connect a Polaris project to GitLab Self-Managed using a secure tunnel, you'll need to create this tunnel in Polaris and then, when you're ready to connect, activate the tunnel using the Bridge CLI. See [Add and manage secure tunnels in the Polaris UI](../add-and-manage-secure-tunnels-in-the-polaris-ui.md) and [Create a secure tunnel using Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/539af6010b0ca8cbf87dbf421895141f.topic) for more information.

### Domains and IPs

If you're not using a secure tunnel, to connect a Polaris project to a project hosted in GitLab Self-Managed you must add the integration IPs for Polaris to your allow list. See the **Integrations** section of Polaris IP ranges for more information.

### Create an access token

Authentication between GitLab and Polaris is managed with an access token that you create in GitLab. If you haven't done so already, follow the instructions in the GitLab documentation to create an access token: [GitLab Docs > GitLab token overview](https://docs.gitlab.com/security/tokens/).

When creating an access token:

- Set the token's expiration date. To avoid issues, we recommend No expiration.
- Select the role (for Project/Group Access Tokens). Select any role above “Guest”.
- Under Select scopes, select read\_repository and read\_api.   
   [image: gitlab select scopes]

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

## Connect to a project hosted in GitLab Self-Managed

To connect a project in Polaris to a project in GitLab Self-Managed, follow these steps:

1. In Polaris, open the project you wish to connect to a GitLab project (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Under Connected SCM, select Edit.
4. Select Self-hosted.
5. Select the source of your project: GitLab.
6. Enter the Repository URL.

   To obtain the repository URL, open the GitLab project in a browser and select Clone. Copy the HTTPS URL (SSH is not supported).   
    [image: gitlab clone]
7. If using a secure tunnel, check URL is in a private network and select a secure tunnel from the pull-down menu.
8. Enter the Repository Access Token.
9. Click Test your Connection. A spinning circle indicates the test is in progress.
10. If your connection test is unsuccessful, check the following and retry:

    1. Your network connection is stable.
    2. Check the Repository URL and Access Token to make sure they are accurate.
    3. Check that the Repository Access Token is still valid and has not expired.
    4. If you're not using a secure tunnel, check that Polaris external IP addresses have been added to your firewall allow list.
    5. Check that you selected the correct provider for your source project (GitLab).
11. If your connection is successful, click Save.

## Next steps

Now, you can scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
