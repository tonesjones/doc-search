---
title: "The My Organization page"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/the-my-organization-page.html"
content_id: "cRmrJcYvlgLAIe6QJ4FsEw"
product_key: "polaris-platform-latest"
section: "The Polaris web UI"
scraped_at: "2026-08-12T19:55:49.964600+00:00"
content_hash: "fa39d56cea0c8c75b4cb4720d1299c60cb0e597dcbd0661687f0a0595fdadab0"
---

# The My Organization page

Allows administrators to manage Polaris for the entire organization, including adding users, viewing audits, adding subscriptions, managing issue tracking integrations, and managing notifications.

Table 1. My Organization Page Interface

|  |  |
| --- | --- |
| [image: my org] | |
| General | Here, you can:  - Find your organization (tenant) name and ID. - Enable/disable assessment center access to published issues (enabled by default). - Select how the copyright information is displayed. - Enable/disable email notifications for all users (enabled by default). Note: To change your personal notification settings, go to Account [image: icon account]  > Account > Notifications. |
| Users | Add new users to Polaris and manage the users in your organization (including deactivating or deleting users, updating a user's information or global role, resetting a user's password or two-factor authentication). |
| Groups | Create and manage groups in Polaris (including managing group membership, group application assignments, global and application-level roles, and deleting groups). |
| Service Accounts | Create and manage service accounts in Polaris. See [Service accounts for Polaris](../how-to/service-accounts-for-polaris.md) for more information. |
| Roles | Create and manage application-level roles in Polaris. |
| Audit Logs | See system changes from the user interface and API. Users can filter results by date, event type, etc., see activity details such as changes in issue policies names or rules, and export the audit log. |
| Subscriptions | View subscriptions and see active status for all of Polaris. |
| Integrations | **SCM Integrations**: Integrate Polaris with Azure DevOps, Jira, and Secure Code Warrior. See [Issue tracking integrations](../how-to/issue-tracking-integrations.md) and Integrate Secure Code Warrior with Polaris for more information.  **Black Duck SCA**: Set up a connection to sync vulnerabilities from your Black Duck Black Duck® SCA instance to Polaris, either daily or on demand. Black Duck® SCA projects and versions are automatically mapped to Polaris. Requires a subscription that permits external analysis tests. See [Import issues from Black Duck SCA](../how-to/import-issues-from-black-duck-sca.md) for more information.  Manage your Fix Pull Request settings for your organization. See [Fix Pull Requests (Fix PR)](../how-to/fix-pull-requests-fix-pr.md) for more information. |
| Licenses | Enable or disable on an organization-level:  - Normalize copyright entries - Deep License |
| Authentication | Set up your organization's multi-factor authentication method (two-factor authentication, or single sign-on with SAML 2.0). |
| Labels | Define a set of labels to categorize applications, projects, and branches in ways that make sense to your organization. See [Create and manage labels](../how-to/create-and-manage-labels.md) for more information. |
| Analysis | - Manage your organization's event-based test automation settings including Fail PRs. See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md). - Default file and folder exclusion rules. See [Exclude files and folders from tests](../how-to/exclude-files-and-folders-from-tests.md) for more information. |
| Black Duck Assist | Enable/disable Black Duck Assist features (disabled by default). Features include:  - AI insight - AI chatbot (beta) |
| Risk Scoring | Enable risk scoring in your organization, and set up your organization's application and issue risk factors. See [Risk scoring in Polaris](../how-to/risk-scoring-in-polaris.md) for more information. |
| Triage | Here, you can:  - Enable/disable triaging issue severity. This allows users (with triage permissions) to change issue severity during triage. Leave the Allow triaging issue severity setting unlocked to allow Organization Application Managers, Application Administrators, and other users with permissions to modify it for their applications and projects. Lock the setting to only allow Organization Administrators to manage this setting for all applications and projects. See [Triaging issue severity](../how-to/triaging-issue-severity.md) and Ways to triage issues in Polaris for more information. - Manage your organization's default approval workflow—see [Set up triage approval workflows](../how-to/set-up-triage-approval-workflows.md) for more information. |
| Policies | Set your organization's default policies and control policy inheritance. Here, you can:  - Set the default policies applied to new applications, projects, and branches. - Apply default policies to all of the applications, projects, or branches in your portfolio. - Control whether default policies are automatically applied to default branches and non-default branches.   See [Manage your default policies](../how-to/create-and-manage-policies/manage-your-default-policies.md) for more information. |
| Dashboards | Select which dashboards are available to users in your organization. Choose from two dashboard sets:  - Polaris (default): Enable the default set of Polaris dashboards (all dashboards). - Black Duck SCA: Enable the Table - Component Search and Table - License Search dashboards. |
