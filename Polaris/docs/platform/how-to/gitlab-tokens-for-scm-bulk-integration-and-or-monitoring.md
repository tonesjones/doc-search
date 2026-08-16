---
title: "GitLab Tokens for SCM Bulk Integration and/or Monitoring"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-tokens-for-scm-bulk-integration-and/or-monitoring.html"
content_id: "ey7ptJSFXDj1OvTNfE8Geg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:17.899047+00:00"
content_hash: "ae4b53845a2173608d9dc1db3afc95588d1a3525be139923167fb848a0ef4445"
---

# GitLab Tokens for SCM Bulk Integration and/or Monitoring

## Overview

How to create a token for bulk onboarding and monitor features via SCM Integrations. Monitoring includes Synchronizing Polaris with your SCM Provider and Event-Based Test Automation in Polaris for SCM Integrations.

Note: Available only for GitLab SaaS (Premium and Ultimate).

### Creating an access token

When integrating SCM repositories, you will need an access token you create in GitLab.

Authentication between GitLab and Polaris is managed with an access token that you create in GitLab. If you haven't done so already, create an access token. For additional information: [GitLab Docs > GitLab token overview.](https://docs.gitlab.com/security/tokens/)

Important: Must be created in GitLab SaaS (Premium or Ultimate). Free version does not allow users to create webhooks.

Important: Token must be created by a GitLab **Organization Owner** or users with the "Manage organization webhooks" permission, who are authorized to manage organization webhooks. Although other GitLab users may be able to select the scope requirements when creating a token, the token will not work due to permission requirements in GitLab to manage organization webhooks.

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
