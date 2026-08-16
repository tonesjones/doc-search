---
title: "GitHub Enterprise Server"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/github-enterprise-server.html"
content_id: "2yXDEtUf_fmc~Bo_QFPe9A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:10.890339+00:00"
content_hash: "13fd360882f3c1d61551d5bd683c348f7e409efaaaf81543bcf1c046235e755a"
---

# GitHub Enterprise Server

**Create a Secure Tunnel for GitHub Enterprise Server**

See Creating a Secure Tunnel for GitHub Enterprise Server.

**Create a personal access token**

Authentication between GitHub and Polaris is managed with a personal access token that you create in GitHub. If you haven't done so already, create an access token. For more information, see [GitHub: Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Important: The token must be created by a GitHub **Organization Owner** or a user with the "Manage organization webhooks" permission. Although other GitHub users may be able to select the required admin scopes when creating a token, the token will not work without the necessary organization-level permissions to manage organization webhooks.

1. Sign in to GitHub.
2. In the upper-right corner of any page, click your profile photo, then click Settings.
3. In the left sidebar, click Developer settings.
4. In the left sidebar, under Personal access tokens, click Tokens (classic).
5. Select Generate new token, then click Generate new token (classic).
6. Enter a name for your token.
7. Set the token's expiration date. To avoid issues, we recommend No expiration.
8. Under Select scopes, select repo (all), read:org (under admin:org), and admin:org\_hook.
9. Click Generate Token.
10. (Optional) Select the copy icon to copy the token.
11. To use your token to access resources owned by an organization that uses SAML single sign-on, authorize the token via Configure SSO. For more information, see [Authorizing a personal access token for use with SAML single sign-on](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on) in the GitHub Enterprise Cloud documentation.

    Important: Store your token in a secure location. Each time you modify a project's SCM integration, you'll need to reenter the token to save your changes.

## SCM bulk onboard to create applications and projects

See General Prerequisites before starting.

1. On the Portfolio page, select + Create > New Application(s) with SCM.
2. Connect to your SCM:
   1. Select Self-hosted.
   2. Select GitHub (Supported versions).
   3. Enter your private SCM URL.
   4. Select URL is in a private network, then select a Secure Tunnel from the pull-down (see Prerequisites).
   5. Under Repository Access Token, enter the personal access token you created in GitHub (see Prerequisites).

      Note: The personal access token provided here will be used to complete the onboarding process and will be subject to rate limits enforced by GitHub.
   6. Click Test Connect.

      You should receive a Connection Successful message and the Quick Start options should be visible. If your connection test is unsuccessful, check the following:

      - Verify that your network connection is stable.
      - Verify that the Repository Access Token is accurate.
      - Check that the Repository Access Token is still valid and has not expired.
      - Check that you selected the correct provider for your source repository.
      - Check that your organization allows the use of a personal access token (classic).
      - Check that you have authorized the access token for use outside SSO (if applicable).
      - Verify that the teleport agent (for example, Bridge) in the private network is running and pointing at the secure tunnel. See Creating a Secure Tunnel for GitHub Enterprise Server.
3. Under Quick Start, select a Select method option:

   - Matching Organization Names (Automatic)
   - Mapping Repositories (Custom)
4. Complete the **Repository Mapping** based on the selected method:

   - **Automatic Mapping**: Lists matching organization names as applications and projects. You can view repositories to be imported by using the pull-downs (read only).
   - **Custom Mapping**: Select New (type application name) or Existing (select application from pull-down), then select repositories from pull-downs under Projects. If an arrow is next to a name, you can click to select repositories within it. Click Add More to map repositories to multiple applications.

   Note:
   - GitHub organization maps to a Polaris application
   - GitHub repository maps to a Polaris project
   - GitHub branch maps to a Polaris branch

   Application and project names match organization and repository names from GitHub, respectively.

### Customizing onboarding (optional)

1. (Optional) Assign an application-level role to grant users access to the applications and projects being created.

   Choose administrator, contributor, member, observer, or a custom role. The role you select is applied to all applications being created.

   Note: Verify that the user being assigned has access to the repositories in your SCM provider.
2. (Optional) Configure synchronization settings under Integrations.

   These settings allow you to sync your SCM provider with Polaris and include non-default branches in your onboarding and ongoing synchronization. After onboarding is complete, you can manage these settings at the application level. See [Synchronizing Polaris with your SCM Provider](../synchronizing-polaris-with-your-scm-provider.md).

   1. Select Keep repositories and branches synchronized with SCM to have Polaris actively monitor repository updates, deletions, renames, and branch modifications and implement the necessary changes to the corresponding projects and branches.

      Note: If selected without the additional branches option below, this applies only to default branches.
   2. Select Continue to import new repositories for the selected organization to automatically create a new project in Polaris when a new repository is added in GitHub.

      Note: This option is not available when you use custom matching during bulk onboarding.
   3. Select Import additional branches matching substrings to import and synchronize non-default branches.

      After selecting this option, enter substrings separated by commas in the field that appears (for example, -release, -demo).

      Select Continue to import new branches matching substrings if you want Polaris to continue monitoring for branch creation events after the initial integration. Polaris will monitor for new branches matching the specified substrings across all repositories in the organization or application.
3. Click Import Repositories.

   On your Portfolio page, a progress bar will track the percentage of completion.

   If the onboarding fails, an email notification will be sent to the user who initiated the onboarding. Organization admins can monitor activity in audit logs (My Organization > Audit Logs).

   Click Cancel to cancel the import. Any repository already in progress at the time of cancellation will finish in the background. All remaining pending repositories will not be imported. For example, if you import ten repositories and cancel at 50%, five repositories will complete and five will not.
4. (Optional) Set up event-based test automation.

   See [Event-Based Test Automation in Polaris for SCM Integrations](../event-based-test-automation-in-polaris-for-scm-integrations.md).

## SCM bulk onboard projects into an application

See General Prerequisites before starting.

1. On the Portfolio page, select an application by clicking on its name.
2. On the Application page, select + Create > New Project(s) with SCM.
3. Connect to your SCM:
   1. Select Self-hosted.
   2. Select GitHub (Supported versions).
   3. Enter your private SCM URL.
   4. Select URL is in a private network, then select a Secure Tunnel from the pull-down (see Prerequisites).
   5. Under Repository Access Token, enter the personal access token you created in GitHub (see Prerequisites).

      Note: The personal access token provided here will be used to complete the onboarding process and will be subject to rate limits enforced by GitHub.
   6. Click Connect.

      You should receive a Connection Successful message. If your connection test is unsuccessful, check the following:

      - Verify that your network connection is stable.
      - Verify that the Repository Access Token is accurate.
      - Check that the Repository Access Token is still valid and has not expired.
      - Check that you selected the correct provider for your source repository.
      - Check that your organization allows the use of a personal access token (classic).
      - Check that you have authorized the access token for use outside SSO (if applicable).
      - Verify that the teleport agent (for example, Bridge) in the private network is running and pointing at the secure tunnel. See Creating a Secure Tunnel for GitHub Enterprise Server.
4. Under **Repository Mapping**, select repositories to import as new projects from the pull-downs.

   If an arrow is next to a name, you can click to select repositories within it.
5. Click Import Repositories.

- Organization admins can monitor activity in audit logs (My Organization > Audit Logs).
- After onboarding, you can change settings or add the following:
  - Synchronizing Polaris with your SCM Provider
  - Event-Based Test Automation in Polaris for SCM Integrations
- You can also scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

  Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
- To scan from a CI/CD pipeline or local machine, add Bridge CLI to your build process. For posting results back to an on-premises SCM, the CI environment or local machine requires `HTTPS_PROXY` or `HTTP_PROXY` to be configured to route traffic through the tunnel. See Using Bridge CLI with Polaris.
