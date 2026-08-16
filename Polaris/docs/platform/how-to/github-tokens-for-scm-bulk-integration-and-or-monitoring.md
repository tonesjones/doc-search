---
title: "GitHub Tokens for SCM Bulk Integration and/or Monitoring"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/github-tokens-for-scm-bulk-integration-and/or-monitoring.html"
content_id: "2CI8mQhgGXzHBkAJK4fnqA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:17.013912+00:00"
content_hash: "577e3e18aa61bc2805ff5086c114cf547a3c9a1b7e323fb199a96a7d6a767830"
---

# GitHub Tokens for SCM Bulk Integration and/or Monitoring

## Overview

How to create a GitHub Personal Access Tokens (classic) for bulk onboarding and SCM monitoring features via SCM Integrations. Monitoring includes Synchronizing Polaris with your SCM Provider and Event-Based Test Automation in Polaris for SCM Integrations.

Note: Available only for GitHub and GitHub Enterprise Cloud.

### Creating a personal access token

Authentication between GitHub and Polaris is managed with a personal access token that you create in GitHub. If you haven't done so already, create an access token. For additional information: [GitHub > Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Important: Token must be created by a GitHub **Organization Owner** or users with the "Manage organization webhooks" permission, who are authorized to manage organization webhooks. Although other GitHub users may be able to select the admin scope requirements when creating a token, the token will not work due to permission requirements in GitHub to manage organization webhooks.

1. Sign in to GitHub.
2. In the upper-right corner of any page, click your profile photo, then click Settings.
3. In the left sidebar, click Developer settings.
4. In the left sidebar, under Personal access tokens, click Tokens (classic).
5. Select Generate new token, then click Generate new token (classic).
6. Name your token.
7. Set the token's expiration date. To avoid issues, we recommend No expiration.  
    [image: git expiration]
8. Under Select scopes, select repo (all), read:org (under admin:org), and admin:org\_hook.   
    [image: bulk scopes]
9. Click Generate Token.
10. (Optional) Select the copy icon to copy the token.   
     [image: copy pat]
11. To use your token to access resources owned by an organization that uses SAML single sign-on, authorize the token via Configure SSO. For more information, see [Authorizing a personal access token for use with SAML single sign-on](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on) in the GitHub Enterprise Cloud documentation.

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
