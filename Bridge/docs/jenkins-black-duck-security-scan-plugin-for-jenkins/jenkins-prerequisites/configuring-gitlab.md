---
title: "Configuring GitLab"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/configuring-gitlab.html"
content_id: "OMwtry3pg7r_hQuxgno82w"
version: "latest"
section: "Jenkins Integrations"
scraped_at: "2026-10-04T23:28:30.324513+00:00"
content_hash: "31147db677bb0383575a6e2ac3f3cb33fa9db5a4c40ee8b9c904d0cf8dd0f35e"
---

# Configuring GitLab

## Configure GitLab access tokens

The `gitlab_token` variable is required to configure jobs and to submit PR comments.

## Generate a GitLab token

To generate a GitLab token:

1. Click your repository under the Projects section.
2. Select **Settings > Access Tokens > Add new token.**
3. Enter a name for the token in the Note field.
4. Select an expiration for the token.
5. Select a role.
6. Select **api** (under the Select scopes section).

   This is the minimum permission needed to run the scan.
7. Click **Create project access token**.
8. Store the token.

   Remember to store the token after making it, because GitLab will not save the token for you.

Note:

In the **Jenkinsfile**, you will need to pass `gitlab_token` as pipeline input. Or, you can configure it in the global configuration. (Navigate to **Dashboard > Manage Jenkins > System**, then scroll to the **Black Duck Security Scan** section. There you will find the field **Gitlab Token**.)

If `gitlab_token` is set from both sides, then the pipeline input (Jenkinsfile) values will take precedence.

## Webhook creation and configuration for GitLab

For instructions on how to create and configure the webhook for GitLab, click [here](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html).
