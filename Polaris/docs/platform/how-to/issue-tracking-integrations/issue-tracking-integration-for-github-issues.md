---
title: "Issue tracking integration for GitHub Issues"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integration-for-github-issues.html"
content_id: "gokC4ZSU4bI1ZrfWIVHQdQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.981824+00:00"
content_hash: "97b30d40128f8ce971d17cd329c261390bf407665f8d2ad6af6138a99785c29d"
---

# Issue tracking integration for GitHub Issues

Connect Polaris to GitHub Issues via SCM integration to export issues captured in SAST and SCA tests as GitHub Issues bug tickets.

Note: DAST issue export to GitHub Issues is not supported at this time.

## Prerequisites and technical requirements

The issue tracking integration for GitHub Issues requires:

- A cloud-hosted GitHub Standard, GitHub Enterprise, or GitHub Enterprise with data residency repository with the Issues feature enabled.

  Note: GitHub Enterprise Server is not supported at this time.

  To enable the Issues feature, go to Settings > General, and under the Features heading, select the Issues checkbox.

    
   [image: A screenshot of the GitHub Features settings.]
- A Personal Access Token (PAT) with the following classic token scopes:
  - `repo`
  - `security_events`
  - `read:org`
  - `admin:org_hook` if you are linking an organization repository.
  - `admin:repo_hook` if you are linking a personal repository.

  See [GitHub Tokens for SCM Bulk Integration and/or Monitoring](../github-tokens-for-scm-bulk-integration-and-or-monitoring.md) for more information.

  CAUTION:

  If the PAT is under-scoped, the SCM connection test still passes and a scope error will surface at issue export time.
- A Polaris Organization Administrator or Organization Application Manager who is also a GitHub Organization Owner or user with the Manage organization webhooks permission.

  Note: A Polaris Application Administrator cannot bulk onboard applications with an SCM integration, but can still manage SCM repository connections and issue tracking integration options. See [Roles and permissions](../../reference/roles-and-permissions.md) for more information.

## Issue fields

Polaris creates issues in GitHub Issues with the Bug type. Each issue includes the following fields:

- Title: the format of titles varies, depending on how the ticket was created:
  - Tickets for individual issues you export manually (single export):

    ```
    Polaris - '<Application name>' / '<Project name>' / '<Branch name>' contains issue '<Issue type>'
    ```
  - Tickets created for policy violations:

    ```
    Polaris - '<Application name>' / '<Project name>' / '<Branch name>' issues violating policy '<Policy name>'
    ```
  - Tickets for multiple issues you export manually (bulk export):

    ```
    Polaris - '<Application name>' / '<Project name>' / '<Branch name>' vulnerabilities ('<Number of issues>' issues)
    ```
- Description: the format of descriptions varies, depending on how the ticket was created:
  - Tickets for issues you export manually: detailed information about the issue, remediation guidance, and a link to the issue in Polaris.
  - Tickets created for policy violations: the name of the violated policy, the names of any violated rules, and links you can use to view violating issues in Polaris.
- Issue Author: the user associated with the personal access token used for the integration.
- State: the status of the GitHub Issues ticket depends on the status of the Polaris issues:
  - `open` when a GitHub Issues ticket is created by issue export or policy violation in Polaris.
  - `closed` and `state_reason=completed` when status synchronization is enabled in Polaris and the linked Polaris issue(s) are dismissed or absent.

Note: For bundled tickets (bulk issue export to a single ticket or policy violation tickets), two-way status mapping is not supported at this time. However, these tickets can still be automatically closed when all of the linked issues become absent or are dismissed in Polaris.

Important: Only the Bug issue type is supported at this time.

## Connect a Polaris application to GitHub Issues via SCM bulk onboarding

Issue tracking integration with GitHub can be configured at the application level during SCM onboarding. To configure GitHub issue tracking integration with a Polaris application, follow these steps:

1. In Polaris, go to Portfolio > + Create > New Application(s) with SCM.

   The New Application(s) from SCM Import page appears.
2. Select Cloud-hosted as the type of server that is hosting your repository.
3. Select either GitHub, GitHub Enterprise, or GitHub Enterprise (with data residency) as the source of your organization connection.
4. If you selected GitHub Enterprise (with data residency), enter your tenant's SCM URL (for example, `https://<company>.ghe.com`).

   Note: The SCM URL field only appears when you select GitHub Enterprise (with data residency).
5. Enter the personal access token in the Repository Access Token field and click the Test Connection button.

   A green confirmation message ✓ Connection successful appears.
6. Select a Quick Start method from the dropdown menu:

   - Automatically create Polaris Applications from GitHub organizations allows Polaris to create a new application using the name of your GitHub organization and automatically maps the organization repositories to new Polaris projects within this application.
   - Manually map GitHub repositories to Polaris Applications allows you to choose between creating a new application or selecting an existing application for SCM onboarding. If a new application is selected, you can enter a name for the application in the Application field. You can also customize which repositories are imported and mapped to new Polaris projects by selecting any number of available repositories in the Projects > Select Repositories dropdown menu. Optionally, you can click the Add More + button to map repositories to multiple new or existing Polaris Applications.
7. (Optional) Under the Assign Application Role heading, assign Polaris application roles to specific users by using the Application Role and Assign Users dropdown menus.
8. Under the Auto-configure Bug Tracking System heading, select Use SCM Configuration.
9. (Optional) Select the Automatically sync GitHub/GitHub Enterprise and Polaris issue status when either is opened, closed, or dismissed (in all configured branches) checkbox to enable issue status synchronization. You can then choose the synchronization direction by selecting one of three radio buttons: Bi-Directional (both directions), Polaris to GitHub/GitHub Enterprise, or GitHub/GitHub Enterprise to Polaris.

   Important: Triage status changes triggered by two-way (Bi-Directional) synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. If you require approval for every triage status change, configure one-way synchronization (Polaris to GitHub Issues) instead.
10. (Optional) Under the Integrations heading, select any of the checkbox options, which include Keep repositories and branches synchronized with SCM, Import additional branches matching substrings, and Continue to import branches matching substrings.

    Note: Default branches are automatically imported.
11. Click the Import Repositories button to finalize the SCM onboarding and issue tracking integration with your application.

    An example of a completed New Application(s) from SCM Import form is shown below.

      
     [image: A screenshot of a completed New Application form configured with GitHub SCM and issue tracking.]

Polaris returns to the Portfolio page with a loading bar at the top of the screen to indicate the progress of the SCM onboarding. The Portfolio page refreshes again once importing is finished.

### Manage GitHub Issues settings for Polaris applications

Issue tracking integration with GitHub can be configured for existing Polaris applications through the application's settings. To do so, follow these steps:

1. In Polaris, go to Portfolio and select the application you want to configure the GitHub issue tracking integration for.
2. Select Settings > Integrations.
3. Click the pencil [image: A small user interface icon denoted by a pencil.] icon next to Connected SCM to edit the SCM integration for this application.
4. Select Cloud-hosted as the type of server that is hosting your repository.
5. Select either GitHub, GitHub Enterprise, or GitHub Enterprise (with data residency) as the source of your organization connection.
6. Enter your organization's GitHub URL in the SCM URL field.
7. Enter the personal access token in the Repository Access Token field and click the Test Connection button.

   A green confirmation message ✓ Connection successful appears.
8. Click the Save button.
9. (Optional) Under the Repository and Branch Monitoring heading, click the pencil [image: A small user interface icon denoted by a pencil.] icon to edit or select any checkbox options, which include Keep repositories and branches synchronized with SCM, Continue to import new repositories for above organizations, Import additional branches matching substrings, and Continue to import branches matching substrings. Click the Save button to save these settings.
10. Under the Issue Tracker heading, click the pencil [image: A small user interface icon denoted by a pencil.] icon and then select Use SCM Configuration.
11. (Optional) Select the Automatically sync GitHub/GitHub Enterprise and Polaris issue status when either is opened, closed, or dismissed (in all configured branches) checkbox to enable issue status synchronization. You can then choose the synchronization direction by selecting one of three radio buttons: Bi-Directional (both directions), Polaris to GitHub/GitHub Enterprise, or GitHub/GitHub Enterprise to Polaris. Click the Save button to save these settings.

    Important: Triage status changes triggered by two-way (Bi-Directional) synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. If you require approval for every triage status change, configure one-way synchronization (Polaris to GitHub Issues) instead.

    An example of an application configured with GitHub issue tracking and status synchronization is shown below.

      
     [image: A screenshot of the Polaris application settings screen with a GitHub SCM connected.]

The Polaris application is now configured with GitHub issue tracking integration.

Note: If the Keep repositories and branches synchronized with SCM and Continue to import new repositories for above organizations checkboxes are enabled, Polaris automatically creates projects from the synchronized repositories. If these settings are not enabled, you must create the Polaris projects manually.

## Connect a Polaris project to GitHub Issues from SCM import

Issue tracking integration with GitHub can be configured at the project level during SCM import. To create a new Polaris project with a GitHub issue tracking integration, follow these steps:

Important: If a GitHub instance has already been connected to your Polaris application, all projects within that application automatically inherit the SCM synchronization and issue tracking integration settings from the application. If you change any settings at the project level, they overwrite the application-level inherited settings.

1. In Polaris, go to Portfolio > <Application name> > + Create > New Project(s) with SCM.

   The New Project(s) from SCM Import page appears.
2. Select Cloud-hosted as the type of server that is hosting your repository.
3. Select either GitHub, GitHub Enterprise, or GitHub Enterprise (with data residency) as the source of your organization connection.
4. If you selected GitHub Enterprise (with data residency), enter your tenant's SCM URL (for example, `https://<company>.ghe.com`).

   Note: The SCM URL field only appears when you select GitHub Enterprise (with data residency).
5. Enter the personal access token in the Repository Access Token field and click the Test Connection button.

   A green confirmation message ✓ Connection successful appears.
6. Select any number of available repositories to import from the Repository Map dropdown menu. Polaris automatically creates and maps the selected repositories to new projects.
7. Click the Import Repositories button to finalize the SCM connection.

   An example of a completed New Project(s) from SCM Import form is shown below.

     
    [image: A screenshot of a completed New Project form configured with GitHub SCM.]

Polaris returns to the application's Projects page with a loading bar at the top of the screen to indicate the progress of the SCM onboarding. This page refreshes again once importing is finished. Issue tracking settings can be configured by following Manage GitHub Issues settings for Polaris projects.

### Manage GitHub Issues settings for Polaris projects

Issue tracking integration with GitHub can be configured for individual Polaris projects through the project's settings. To do so, follow these steps:

Important: If a GitHub instance has already been connected to your Polaris application, all projects within that application automatically inherit the SCM synchronization and issue tracking integration settings from the application. If you change any settings at the project level, they overwrite the application-level inherited settings.

1. In Polaris, go to Portfolio > <Application name> and select the project you want to configure the GitHub issue tracking integration for.
2. Select Settings > Integrations.
3. Click the pencil [image: A small user interface icon denoted by a pencil.] icon next to Connected SCM to edit the SCM integration for this project.
4. Select Cloud-hosted as the type of server that is hosting your repository.
5. Select either GitHub, GitHub Enterprise, or GitHub Enterprise (with data residency) as the source of your organization connection.
6. Enter the repository's URL in the Repository URL field.
7. Enter the personal access token in the Repository Access Token field and click the Test Connection button.

   A green confirmation message ✓ Connection successful appears.
8. Click the Save button.
9. Under the Issue Tracker heading, click the pencil [image: A small user interface icon denoted by a pencil.] icon and then select Use SCM Configuration.
10. (Optional) Select the Automatically sync GitHub/GitHub Enterprise and Polaris issue status when either is opened, closed, or dismissed (in all configured branches) checkbox to enable issue status synchronization. You can then choose the synchronization direction by selecting one of three radio buttons: Bi-Directional (both directions), Polaris to GitHub/GitHub Enterprise, or GitHub/GitHub Enterprise to Polaris. Click the Save button to save these settings.

    Important: Triage status changes triggered by two-way (Bi-Directional) synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. If you require approval for every triage status change, configure one-way synchronization (Polaris to GitHub Issues) instead.

    An example of a project configured with GitHub issue tracking and status synchronization is shown below.

      
     [image: A screenshot of the Polaris project settings screen with a GitHub SCM connected.]   

    Note: If the Issue Tracker settings at the project level have been modified from the inherited application settings, the inherited label for the Issue Tracker section changes to modified. A reset button appears here that can be used to restore the inherited settings.

The Polaris project is now configured with GitHub issue tracking integration.

## Enable issue tracking for individual branches

After connecting a project in Polaris to an issue tracking instance, you can configure issue tracking synchronization (including auto-close) for individual branches.

Before you can enable issue tracking synchronization at the branch level, the project must be configured with a GitHub issue tracking integration via one of the following methods:

- Connect a Polaris application to GitHub Issues via SCM bulk onboarding
- Manage GitHub Issues settings for Polaris applications
- Connect a Polaris project to GitHub Issues from SCM import
- Manage GitHub Issues settings for Polaris projects

Note: If the GitHub issue tracking integration is configured at the application level, all projects within that application automatically inherit the application's SCM synchronization and issue tracking settings by default.

By default, issue tracking synchronization is only enabled on the project's default branch. You can enable or disable this setting for individual branches to control which branches participate in issue tracking synchronization. This is useful when you want to track issue resolution across multiple branches (such as feature branches or release branches) or exclude certain branches from the auto-close behavior.

Note: An exported issue must be dismissed or absent across all participating branches before the associated ticket is closed.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Select the Branches tab.
4. Select the branch you want to configure.

   The Edit Branch window opens.
5. Under Issue Tracker, select Include this branch in issue tracking synchronization (i.e. auto-close).

   When this option is enabled, Polaris includes this branch when determining whether issues are absent or dismissed across all synchronized branches.
6. Select Save.
7. (Optional) Repeat this process for other branches you want to include in issue tracking synchronization.

The branch is now included in issue tracking synchronization. When issues linked to GitHub Issues bug tickets become absent or are dismissed across all synchronized branches, Polaris automatically closes the associated ticket.

Note: If an auto-closed issue reappears in a subsequent scan, Polaris does not reopen the closed ticket. If the issue is flagged by a policy, the policy creates a new GitHub Issues bug ticket automatically. Otherwise, you must manually export or link a new ticket to the issue. See [Export an issue to an issue tracking instance](export-an-issue-to-azure-devops-or-jira.md) for more information.
