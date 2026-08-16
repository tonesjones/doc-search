---
title: "Bitbucket Data Center"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/bitbucket-data-center.html"
content_id: "vlkXwozD00XAQMzLPlNk2w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:21.070970+00:00"
content_hash: "f814c07769002b4bcdc7232a5a77dc0bd875892852e8416e193f5bb38c61a986"
---

# Bitbucket Data Center

How to connect a Polaris project to a repository in Bitbucket Data Center.

## Prerequisites

### Domains and IPs

To connect a project to a repository hosted in Bitbucket Data Center, you must add the integration IPs for Polaris to your allow list. See Integrations for more information.

### Create an HTTP access token

Authentication between Bitbucket Data Center and Polaris is managed with an HTTP access token that you create in Bitbucket. If you haven't done so already, follow the instructions in the Bitbucket Data Center documentation to create an access token: [HTTP access tokens > Create HTTP access tokens](https://confluence.atlassian.com/bitbucketserver0819/http-access-tokens-1416825778.html).

When creating an access token:

- Login to Bitbucket Data Center.
- Select the profile icon (near the upper-right corner of the screen) and open Manage account.
- On the left tab, click on HTTP access tokens and click the create token button.
- Name your token.
- Set Project permissions to Project read.
- Set Repository permissions to Repository read.
- Set the token's expiration date. To avoid issues, we recommend Do not expire.
- .

Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

## Connect to a repository hosted in Bitbucket Data Center

To connect a project in Polaris to a repository in Bitbucket Data Center, follow these steps:

1. In Polaris, open the project you wish to connect to a repository (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Self-hosted.
4. Select the source of your repository: Bitbucket.
5. Enter the Repository URL.

   To obtain the repository's URL, open your Bitbucket project and select Clone. Copy the HTTPS URL (SSH is not supported) starting at `https`.

   [image: BB Clone URL]
6. Enter the Repository Access Token.
7. Click Test your Connection. A spinning circle indicates the test is in progress.
8. If your connection is successful, click Save.

   If your connection test is unsuccessful, check the following and retry:

   1. Your network connection is stable.
   2. Check the Repository URL and Access Token to make sure they are accurate.
   3. Check that the Repository Access Token is still valid and has not expired.
   4. Check that Polaris external IP addresses have been added to your firewall allow list.
   5. Check that you selected the correct provider for your source repository.

## Next steps

Now, you can scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
