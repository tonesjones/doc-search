---
title: "GitHub and GitHub Enterprise"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/github-and-github-enterprise.html"
content_id: "v5NFypuxAG_Tssy4Sjl_~A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:10.161463+00:00"
content_hash: "5af567d9f344ff7abc86baa5d8e7d8727bbf22ed68ef1d87cc1f003dfaff50a5"
---

# GitHub and GitHub Enterprise

## Prerequisites

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

## SCM bulk onboard to create applications and projects

See General Prerequisites before starting.

1. On the Portfolio page, select + Create > New Application(s) with SCM.
2. Connect to your SCM:
   1. Select the type of server that is hosting your repository: Cloud-hosted.
   2. Select GitHub or GitHub Enterprise.
   3. Enter the personal access token created in GitHub (see Prerequisites ) under Repository Access Token.

      Note: The personal access token provided here will be used to complete the onboarding process and will be subject to rate limits enforced by GitHub.
   4. Click Connect.

      You should receive a Connection Successful message and the Quick Start options should be visible. If your connection test is unsuccessful, check the following:

      - Your network connection is stable.
      - Check the Repository Access Token to make sure it is accurate.
      - Check that the Repository Access Token is still valid and has not expired.
      - Check that you selected the correct provider for your source repository.
      - Check that your organization allows use of personal access token (classic).
      - Check that you have authorized use of access token outside SSO (if applicable).
3. Under Quick Start, Select method: (Repository Mapping is different depending on the selection).

   - Matching Organization Names (Automatic)
   - Mapping Repositories (Custom)
4. Repository Mapping: This will be different according to which method is selected.

   1. Automatic Mapping: Lists the matching organization names as applications and projects. You can view repositories to be imported by using the pulldowns (read only).
   2. Custom Mapping: Select New (type application name) or Existing (select application from pulldown), then select repositories from pulldowns under Projects. If an arrow is next to a name, you can click to select repositories within it. Click Add More to map repositories to multiple applications.

   Note:
   - GitHub organization maps to a Polaris application
   - GitHub repo maps to a Polaris project
   - GitHub branch maps to a Polaris branch

   Application and project names match organization and repository names from GitHub, respectively.

## Customizing onboarding (optional)

1. Assign Application Role: Grant users access to all of the applications and projects you create with an application level role (administrator, contributor, member, observer, or custom roles).

   - The application level roles you select are applied to all of the applications that are being created.
   - Double-check that the user being assigned has access to the repositories in your SCM provider.
2. Under Integrations: Allows you to sync your SCM provider with Polaris and include non-default branches in your onboarding and sync. After onboarding is complete, you can manage these setting on the application level. See [Synchronizing Polaris with your SCM Provider](../synchronizing-polaris-with-your-scm-provider.md).

   1. Keep repositories and branches synchronized with SCM: Polaris will actively monitor repository updates, deletions, renames, and branch modifications, including updates, deletions, and renames, on the SCM provider. It will then implement the necessary changes to the corresponding Projects and Branches.

      Note: If this is selected without the additional branches option below, this will apply only to default branches.

      Note: Monitoring and updates for renaming is not supported for GitLab.
   2. Continue to import new repositories for above organization. For example, if you create a new repo in GitHub, Polaris will create a new project in Polaris. This is not available when you use custom matching during bulk onboarding.
   3. Import additional branches matching substrings. Default branches are automatically imported but this allows you to import/sync non-default branches.

      1. When selected, a new input field will appear. Enter substrings separated by commas (i.e. -release, -demo)
      2. When selected, a checkbox is available if you want to Continue to import new branches matching substrings after the initial integration. Polaris will monitor for branch creation events on all the repos under the organization/application that match the specified substrings.
3. Click Import Repositories.
4. On your Portfolio page, a progress bar with a percentage done will track your progress.   
    [image: bulk progress bar]   

   If the onboarding fails, an email notification will be sent to the user who initiated the onboarding. Organization Admins can monitor activity in audit logs (My Organization > Audit Logs).

   Click Cancel to cancel the import. Any repository in the process of being imported at the time of cancellation will complete in the background after the cancel is accepted. Then all onboarding will be stopped immediately. For example, if you import ten repositories and cancel at 50%, five repositories would be imported and five repositories would not.
5. You can now set up event-based test automation. See [Event-Based Test Automation in Polaris for SCM Integrations](../event-based-test-automation-in-polaris-for-scm-integrations.md).

   Note: To enable Fix Pull Requests for all onboarded applications, create a component policy (see [Component policies](../create-and-manage-policies/component-policies.md)) and assign it to the applications after onboarding. See [Fix Pull Requests (Fix PR)](../fix-pull-requests-fix-pr.md).

## SCM bulk onboarding projects into an application

See General Prerequisites before starting.

1. On the Portfolio page, select an application by clicking on its name.
2. On the Application page, select + Create > New Project(s) with SCM.
3. Connect to your SCM:
   1. Select the type of server that is hosting your repository: Cloud-hosted.
   2. Select GitHub or GitHub Enterprise.
   3. Enter the personal access token created in GitHub (see Prerequisites ) under Repository Access Token.

      Note: The personal access token provided here will be used to complete the onboarding process and will be subject to rate limits enforced by GitHub.
   4. Click Connect.

      You should receive a Connection Successful message. If your connection test is unsuccessful, check the following:

      - Your network connection is stable.
      - Check the Repository Access Token to make sure it is accurate.
      - Check that the Repository Access Token is still valid and has not expired.
      - Check that you selected the correct provider for your source repository.
      - Check that your organization allows use of personal access token (classic).
      - Check that you have authorized use of access token outside SSO (if applicable).
4. Repository Mapping: Select repositories to import as new projects from pulldowns. If an arrow is next to a name, you can click to select repositories within it.
5. Click Import Repositories.

## Next Steps

- Organization Admins can monitor activity in audit logs (My Organization > Audit Logs).
- Change settings or add:
  - Synchronizing Polaris with your SCM Provider
  - Event-Based Test Automation in Polaris for SCM Integrations
- You can also scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

  Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
