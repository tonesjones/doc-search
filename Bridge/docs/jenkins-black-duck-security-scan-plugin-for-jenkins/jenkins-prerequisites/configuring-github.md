---
title: "Configuring GitHub"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/configuring-github.html"
content_id: "_s3hCdcRFHJdV_Jf6jO1tA"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:33.399842+00:00"
---

# Configuring GitHub

## Configure GitHub access tokens

The `github_token` variable is required to configure jobs and to submit PR comments.

## Generate a GitHub token

To generate a GitHub token:

1. Click your Profile photo, then select **Settings > Password and authentication > Developer settings > Personal access tokens > Tokens (classic) > Generate new token > Generate new token (classic)**.
2. Enter a name for the token in the Note field.
3. Select an expiration for the token.
4. Select **repo** (under the Select scopes section).

   This is the minimum permission needed to run the scan.
5. Click **Generate token.**
6. Store the token.

   Remember to store the token after making it, because GitHub will not save the token for you.

Note:

In the **Jenkinsfile**, you will need to pass the `github_token` as pipeline input. Or, you can configure it in the global configuration. (Navigate to **Dashboard > Manage Jenkins > System**, then scroll to the **Black Duck Security Scan** section. There you will find the field **Github Token**.)

If `github_token` is set from both sides, then the pipeline input (Jenkinsfile) values will take precedence.

## Webhook creation and configuration for GitHub

For instructions on how to create and configure the webhook for GitHub, click [here](https://docs.github.com/en/webhooks).
