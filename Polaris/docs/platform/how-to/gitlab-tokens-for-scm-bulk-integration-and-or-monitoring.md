---
title: "GitLab Tokens for SCM Bulk Integration and/or Monitoring"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-tokens-for-scm-bulk-integration-and/or-monitoring.html"
content_id: "ey7ptJSFXDj1OvTNfE8Geg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:20.697284+00:00"
content_hash: "c4de7d8c6d07aa1f70976c47ff4360066eecc6a2a8f1508aeda16c248d1dcb46"
---

# GitLab Tokens for SCM Bulk Integration and/or Monitoring

## Overview

How to create a token for bulk onboarding and monitor features via SCM Integrations. Monitoring includes Synchronizing Polaris with your SCM Provider and Event-Based Test Automation in Polaris for SCM Integrations.

Note: Group-level webhooks, required for auto-onboarding of new repositories, require GitLab Premium or Ultimate on both SaaS and Self-Managed. Project-level webhooks are supported on all GitLab editions, including Free Edition on Self-Managed.

### Creating an access token

When integrating SCM repositories, you will need an access token you create in GitLab.

Authentication between GitLab and Polaris is managed with an access token that you create in GitLab. If you haven't done so already, create an access token. For additional information: [GitLab Docs > GitLab token overview.](https://docs.gitlab.com/security/tokens/)

Important: Premium or Ultimate is required for group-level webhooks (auto-onboarding of new repositories). All editions, including Free, are supported for project-level webhooks (individual project integrations).

Important: Token must be created by a GitLab **Group Owner** or someone with equivalent webhook-management rights. Although other GitLab users may be able to select the scope requirements when creating a token, the token will not work due to permission requirements in GitLab to manage organization webhooks.

When creating an access token:

- Select your avatar.
- Select **Edit profile**.
- On the left sidebar, select **Access tokens**.
- Select **Add new token**.
- Set the token's expiration date. We recommend setting a maximum expiration period, to avoid issues.
- Select the role (for Project/Group Access Tokens). Select any role above “Guest”.
- Under Select scopes, select read\_repository, read\_api, write\_repository and api.   
   [image: bulk scopes gitlab]

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
