---
title: "GitLab Self-Managed"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/gitlab-self-managed.html"
content_id: "WmSBBryUar1AJmU1fGy6SQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.674803+00:00"
content_hash: "2ee52b94858752b0bbd01c9df7d2ea83ccf0423238b70d43595f190d80ce930a"
---

# GitLab Self-Managed

How to connect one or more of your GitLab Self-Managed projects to new or existing applications in Polaris. This can be done either by using a secure tunnel or by adding the Polaris integration IPs to your allow list.

Note: This page describes how to connect one or more GitLab projects to new or existing Polaris applications, resulting in the creation of new, mapped Polaris projects. Alternatively, you can connect a GitLab project to an existing Polaris project. For more information, see GitLab Self-Managed.

**Connect Polaris to GitLab Self-Managed**

Use one of the following methods depending on your network configuration:

- **IP allowlisting** - For internet-accessible instances, add the Polaris integration IP ranges to your allow list. See the **Integrations** section of Polaris IP ranges.
- **Polaris Secure Tunnel** - For instances on a private network, create a secure tunnel for GitLab Self-Managed first. See [Add and manage secure tunnels in the Polaris UI](../add-and-manage-secure-tunnels-in-the-polaris-ui.md) and [Create a secure tunnel using Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/539af6010b0ca8cbf87dbf421895141f.topic).

Important: Group-level webhooks, which enable automatic detection of new repositories across a group, require GitLab Premium or Ultimate (Self-Managed or SaaS). Project-level webhooks, which enable event monitoring and MR comment decoration for individually onboarded projects, are supported on all GitLab editions, including Free Edition.

## Creating an access token

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

## Onboard to Polaris applications and projects

This procedure describes how to onboard one or more GitLab projects to new or existing Polaris applications. During this process, you'll have the option of importing all GitLab projects in your SCM instance or choosing specific projects to import.

The import mappings are as follows:

- (Automatic import only) GitLab groups are mapped to Polaris applications
- GitLab projects are mapped to Polaris projects
- GitLab branches are mapped to Polaris branches

The names of new Polaris applications and projects will match your GitLab group and project names, respectively.

See General Prerequisites before starting.

1. On the Portfolio page, select + Create > New Application(s) with SCM.
2. Connect to your SCM:
   1. Select Self-hosted.
   2. Select GitLab.
   3. Enter your private SCM URL.
   4. If using a secure tunnel, check URL is in a private network and select a secure tunnel from the pull-down menu (see Prerequisites).
   5. Under Repository Access Token, enter the personal access token you created in GitLab (see Prerequisites).

      Note: The personal access token provided here will be used to complete the onboarding process and will be subject to rate limits enforced by GitLab.
   6. Click Test Connection.

      You should receive a Connection Successful message and the Quick Start options should become visible. If your connection test is unsuccessful, check the following:

      - Verify that your network connection is stable.
      - Verify that the Repository Access Token is accurate.
      - Check that the Repository Access Token is still valid and has not expired.
      - Check that you selected the correct provider for your SCM.
      - Check that your group allows the use of a personal access token.
      - Check that you have authorized the access token for use outside SSO (if applicable).
      - Verify that the teleport agent (for example, Bridge) in the private network is running and pointing at the secure tunnel. See [Add and manage secure tunnels in the Polaris UI](../add-and-manage-secure-tunnels-in-the-polaris-ui.md).
3. If your connection is successful, use the Select Method dropdown menu to select one of the following:

   - Automatically create Polaris Applications from GitLab groups.

     Important: This first option will onboard every single project in your GitLab Self-Managed instance, with each group mapped to a new Polaris application and the projects within them mapped to new Polaris projects. Depending on the number of projects you have, this could take a significant amount of time and result in many unwanted projects. We recommend you choose the second option in most circumstances, especially when first testing this feature.
   - Manually map GitLab Self-Managed projects to Polaris Applications.

   If you selected the first option, skip ahead to step 7.
4. Under the Projects heading, use the pull-down menu to browse and select one or more of the projects in your GitLab Self-Managed instance.

   Important: You'll be mapping the selected projects to a single Polaris application. If you want to add some projects to a different application, deselect them for now.
5. Using the radio buttons under the Application heading, choose whether you want to use a New or Existing Polaris application for the selected GitLab projects.

   - New - enter a unique, suitable name for the new application in the text field provided.
   - Existing - use the dropdown menu to select the intended application.

   Note: Each selected GitLab project will be mapped to a new Polaris project within the chosen application.
6. If you want to assign other GitLab projects to a different application, select Add More and repeat steps 4-6 until you have all of the mappings you need.
7. If you want to assign specific roles to users for the applications you specified in the preceding steps, use the Assign Application Role table to specify each role and the users you want to have it. Select Add More to add as many role assignments as you need.

   Important: Verify that each user has access to the relevant repositories in your SCM instance.
8. If you want to use the SCM server and project for issue tracking, select Use SCM Configuration. Otherwise, make sure No issue tracker is selected.
9. (Optional) Configure synchronization settings under Integrations.

   These settings allow you to sync your SCM provider with Polaris and include non-default branches in your onboarding and ongoing synchronization. After onboarding is complete, you can manage these settings at the application level. See [Synchronizing Polaris with your SCM Provider](../synchronizing-polaris-with-your-scm-provider.md).

   1. Select Keep repositories and branches synchronized with SCM to have Polaris actively monitor GitLab project updates, deletions, and branch modifications and implement the necessary changes to the corresponding Polaris projects and branches.

      Note: If selected without the additional branches option below, this applies only to default branches.

      Note: Monitoring and updates for renaming is not supported for GitLab.
   2. Select Continue to import new repositories for above organizations to automatically create a new project in Polaris when a new project is added in GitLab.

      Note: This option is only available if you selected the automatic import method in step 3.
   3. Select Import additional branches matching substrings to import and synchronize non-default branches whose names include specific text.

      After selecting this option, enter a comma-separated list of the text substrings you want to match against (for example, `-release`, `-demo`, and so on).

      If you want Polaris to continue monitoring for branch creation events after the initial integration, select Continue to import new branches matching substrings. Polaris will monitor for new branches matching the specified substrings across all repositories in the group or application.
10. Click Import Repositories.

    On your Portfolio page, a progress bar will track the percentage of completion.

    If the onboarding fails, an email notification will be sent to the user who initiated the onboarding. Organization admins can monitor activity in audit logs (My Organization > Audit Logs).

    Click Cancel to cancel the import. Any repository already in progress at the time of cancellation will finish in the background. All remaining pending repositories will not be imported. For example, if you import ten repositories and cancel at 50%, five repositories will complete and five will not.
11. (Optional) Set up event-based test automation.

    See [Event-Based Test Automation in Polaris for SCM Integrations](../event-based-test-automation-in-polaris-for-scm-integrations.md).

## Onboard GitLab projects into an application

This procedure describes how to onboard one or more GitLab projects to a single existing Polaris application. Each GitLab project you select is mapped to a new Polaris project within that application.

See General Prerequisites before starting.

1. On the Portfolio page, select an application by clicking on its name.
2. On the Application page, select + Create > New Project(s) with SCM.
3. Connect to your SCM:
   1. Select Self-hosted.
   2. Select GitLab.
   3. Enter your private SCM URL.
   4. If using a secure tunnel, check URL is in a private network and select a secure tunnel from pull-down menu (see Prerequisites).
   5. Under Repository Access Token, enter the personal access token you created in GitLab (see Prerequisites).

      Note: The personal access token provided here will be used to complete the onboarding process and will be subject to rate limits enforced by GitLab.
   6. Click Test Connection.

      You should receive a Connection Successful message. If your connection test is unsuccessful, check the following:

      - Verify that your network connection is stable.
      - Verify that the Repository Access Token is accurate.
      - Check that the Repository Access Token is still valid and has not expired.
      - Check that you selected the correct provider for your SCM.
      - Check that your group allows the use of a personal access token.
      - Check that you have authorized the access token for use outside SSO (if applicable).
      - Verify that the teleport agent (for example, Bridge) in the private network is running and pointing at the secure tunnel. See [Add and manage secure tunnels in the Polaris UI](../add-and-manage-secure-tunnels-in-the-polaris-ui.md).
4. Under the Repository Mapping heading, use the pull-down menu to browse and select one or more of the projects in your GitLab Self-Managed instance. If an arrow appears next to a name, click it to expand the group and browse its contents.

   Note: Each selected GitLab project will be mapped to a new Polaris project within the application.
5. Click Import Repositories.

**Next steps**

- Organization admins can monitor activity in audit logs (My Organization > Audit Logs).
- After onboarding, you can change settings or add the following:
  - Synchronizing Polaris with your SCM Provider
  - Event-Based Test Automation in Polaris for SCM Integrations
- You can also scan on demand (see [How to test from the web UI](../how-to-test-from-the-web-ui.md)) or schedule automatic testing on a daily or weekly basis (see [Test scheduling policies](../create-and-manage-policies/test-scheduling-policies.md)).

  Note: From the Tests screen, before beginning a test manually, make sure to test the connection.
- To scan from a CI/CD pipeline or local machine, add Bridge CLI to your build process. For posting merge request comments to an on-premises GitLab instance, the CI environment or local machine requires `HTTPS_PROXY` or `HTTP_PROXY` configured to route traffic through the tunnel. See [Using Bridge CLI with Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic).
