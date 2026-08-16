---
title: "Bitbucket Tokens for SCM Bulk Integration and/or Monitoring"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/bitbucket-tokens-for-scm-bulk-integration-and/or-monitoring.html"
content_id: "TMT1Dh3XyS3AW1qqGZsV~A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:16.060829+00:00"
content_hash: "c824dca5885a1aacdd85512e3326afd386b036ffae339ae846ba3335598959bb"
---

# Bitbucket Tokens for SCM Bulk Integration and/or Monitoring

## Overview

How to create a token for bulk onboarding and monitoring features via SCM Integrations. Monitoring includes Synchronizing Polaris with your SCM Provider and Event-Based Test Automation in Polaris for SCM Integrations.

Note: Available only for Bitbucket Cloud (Premium).

### Creating an API token

When integrating SCM repositories, you will need an API token you create in Bitbucket Cloud (Premium).

Authentication between Bitbucket Cloud and Polaris is managed with an API token that you create in Bitbucket Cloud. For additional information: [Create an API token](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/).

Important: Must be created in Bitbucket Cloud (Premium). Standard and Free versions does not allow users to create webhooks.

Important: Token must be created by a Bitbucket Cloud **Organization Owner** or users with the "Manage organization webhooks" permission, who are authorized to manage organization webhooks. Although other Bitbucket Cloud users may be able to select the scope requirements when creating a token, the token will not work due to permission requirements in Bitbucket to manage organization webhooks.

Note: App passwords have been deprecated for Bitbucket Cloud. Existing projects integrated using App Password will continue to work until the password expires or Atlassian ends support. After your App Password stops working or if creating a new integration, use API tokens.

1. Select the Settings gear icon in the upper-right corner of the top navigation bar.
2. Under Personal settings, select Atlassian account settings.
3. From the Atlassian Account page, select the Security tab on the top navigation bar.
4. Select Create and manage API tokens.
5. Select Create API token with scopes.
6. Give the API token a name and an expiry date. 365 days is recommended, select Next.
7. Select Bitbucket as the app and select Next.
8. Select the scopes:

   - `read:user:bitbucket`
   - `read:webhook:bitbucket`
   - `read:workspace:bitbucket`
   - `read:project:bitbucket`
   - `read:repository:bitbucket`
   - `read:pullrequest:bitbucket`
   - `write:pullrequest:bitbucket`
   - `write:webhook:bitbucket`  
    [image: bb scope bulk]
9. Select Next.
10. Select the Create token button.

    The page will display the New API token.
11. Copy the generated API token and store it in a secure location.

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
