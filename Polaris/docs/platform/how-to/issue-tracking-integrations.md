---
title: "Issue tracking integrations"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integrations.html"
content_id: "kHbU8EYkPHhMK2qTu_ukSQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:21.116933+00:00"
content_hash: "17ea429f962c9f1d420208dbebbba215b4b034a18b87fcad21e0f4e989dff185"
---

# Issue tracking integrations

Set up an issue tracking integration to export issues captured in Polaris to an external issue tracking platform.

Supported issue tracking integration platforms:

- Azure DevOps
- Jira (Cloud and Data Center)
- ServiceNow
- GitHub Issues (via SCM import)
- GitLab Issues (via SCM import)

After you set up an issue tracking integration, you can export DAST, SAST, and SCA issues in your Polaris projects to an external issue tracking platform. You can export a single issue or multiple issues at once. When exporting multiple issues, you can create one ticket for all selected issues (bundled) or create individual tickets for each issue. Polaris creates tickets that include detailed information about the issue, remediation guidance, and helpful links. DAST issues also include evidence of the issue found; for example, the API endpoint. You can select the type of ticket Polaris creates when you set up the integration. See [Export an issue to an issue tracking instance](issue-tracking-integrations/export-an-issue-to-azure-devops-or-jira.md) for more information.

Important: For GitHub Issues and GitLab Issues, DAST issue export is not supported at this time.

Additionally, setting up an issue tracking integration allows you to create tickets using issue policies (with the Create and bundle to 1 external issue tracker ticket action). When policy violations are detected in a scan of a project's default branch, Polaris creates a single ticket linked to all of the violating issues. The ticket includes the name of the violated policy, the names of violated rules, and links you can use to view issues that violate different rules in Polaris. See [Issue policies](create-and-manage-policies/issue-policies.md) for more information.

Ticket links appear on the Issues tab (in the Bug Tracking column) and in the Issue Details panel (under Bug Tracking).

Note: You can add multiple instances of issue tracking integrations to your organization, but each Polaris project can only be connected to one instance.

## Automatically close tickets and synchronize triage statuses

Optionally, configure Polaris to automatically close (auto-close) tickets in an integrated issue tracking platform when issues are absent or dismissed. You can also configure two-way synchronization of Polaris triage statuses and external ticket statuses.

Auto-close is available for all issue tracking integrations. When enabled, Polaris automatically closes tickets when the linked issue is dismissed (any reason) or absent in subsequent scans. Auto-close applies to all issue types (SAST, SCA, DAST). This feature helps reduce manual ticket management by automatically synchronizing external tickets with the issues they are linked to in Polaris.

You can also configure two-way status synchronization. When configured:

- Triage status changes in Polaris automatically update the status of linked issue tracker tickets.
- Ticket status changes automatically update the triage status of linked Polaris issues.
- Optionally, you can synchronize fix-by dates in Polaris with Azure DevOps, Jira, or ServiceNow ticket due dates. This feature is not available for GitHub Issues or GitLab Issues.

Note the following:

- Triage status changes triggered by two-way synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. The status update is still logged in the triage history panel. If you require approval for every triage status change, configure one-way synchronization (Polaris to the issue tracker) instead. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.
- Bundled tickets created from policy violations or bulk export of several issues to one ticket are not supported for two-way synchronization. This feature only works for individually exported issues with a 1:1 link between a Polaris issue and an external ticket. Bundled tickets can still participate in one-way auto-close, which is triggered when all issues linked to the ticket are dismissed or absent in Polaris.
- Polaris does not reopen tickets that were automatically closed. When a previously absent issue is re-detected, the original ticket remains closed. If the issue is flagged by a policy, the policy creates a new ticket automatically. Otherwise, you must manually export or link a new ticket.
- By default, auto-close is only enabled on the project's default branch.
- If an issue tracking instance's API token expires, triage status changes in Polaris are still saved, but are not reflected in the issue tracker until the token is renewed. The error is logged in the issue's triage history and shown in the integration's configuration.
- Ticket statuses that have no configured mapping in Polaris do not trigger a triage status change in Polaris.
- Issue counts in portfolio summary views, dashboards, and reports reflect triage status changes triggered by two-way synchronization, but these counts can take up to 60 minutes to update.

For Azure DevOps two-way synchronization, also note:

- For Agile templates, `Microsoft.VSTS.Scheduling.DueDate` is used. For Scrum, Basic, or CMMI templates, `Microsoft.VSTS.Scheduling.TargetDate` is used. `FinishDate` is also supported. Verify that one of these fields exists in your Azure DevOps project before configuring fix-by date synchronization.
- If an Azure DevOps workflow requires mandatory fields during a status transition that Polaris does not populate, the sync fails and the error is logged in the issue's triage history.
- Webhooks are registered at the Azure project level, and all work item changes within that Azure project are processed. Polaris automatically registers and manages webhooks in Azure when a two-way sync configuration is saved or deleted. No manual webhook setup in Azure is required.

For Jira two-way synchronization, also note:

- If a Jira workflow blocks a status transition, Polaris reverts the triage status to its previous value and logs the error in the issue's triage history.

For ServiceNow two-way synchronization, also note:

- If the ServiceNow incident workflow requires mandatory custom fields, issue export and status synchronization fail. Polaris does not change the triage status or incident ticket status and logs the error in the issue's triage history.

For GitHub Issues and GitLab Issues two-way synchronization, also note:

- Unlike Azure DevOps, Jira, and ServiceNow, which are configured at the organization level, GitHub Issues and GitLab Issues are configured at the application or project level through SCM import. Two-way synchronization is controlled by a checkbox under the Issue Tracker section of the application or project integrations settings. Polaris projects automatically inherit the issue tracking and synchronization settings of the parent application.

To use these features, create integration options that define the status mappings and auto-close behavior, then enable those options at the project level. See Create integration options for Azure DevOps, Create integration options for Jira Cloud, Create integration options for Jira Data Center, Create integration options for ServiceNow, Manage GitHub Issues settings for Polaris applications, or Manage GitLab Issues settings for Polaris applications for more information.

## Edit links between issues and tickets

After you set up an issue tracking integration, you can update the links between issues in Polaris and tickets in the issue tracking instance.

Polaris issue tracking link updates allow you to:

- Link issues to an external ticket that already exists.
- Change the ticket that issues are linked to.
- Delete links to tickets.

Note the following:

- Like other triage actions, ticket links are shared across branches in a project. If the same issue is detected on multiple branches and you link it to a ticket on one branch, that ticket link applies to the issue across all branches.
- When you manually link an issue to a ticket (or change the ticket an issue is linked to), the ticket you specify must:
  - Exist in the issue tracking instance you connected your Polaris project to.
  - Match the ticket type configured in your Polaris project's issue tracking integration. For example, if a Polaris project's issue tracking integration is configured to create tasks in Azure DevOps or Jira, you cannot create links to epics.
- When you change links manually (including creating, updating, or deleting links), the ticket's description does not change. Changing or removing ticket links in Polaris does not alter, update, or close the tickets in the connected issue tracking instance. The link change action is recorded in the triage history for that issue.
- Similarly, modifying or deleting a ticket in a connected issue tracking instance will not affect issues in Polaris.
- All link updates (including creating, updating, or deleting links) are tracked as triage events, and appear in the issue's triage history. See [View issue history](view-issue-history.md) for more information.

You can edit ticket links using the Bug Tracking ID field in the triage panel. See [Ways to triage issues in Polaris](ways-to-triage-issues-in-polaris.md) for more information.

## Set up an issue tracking integration

To set up an issue tracking integration, follow these steps:

1. Ensure you meet the prerequisites for the integration, which vary from platform to platform:
   - Prerequisites and technical requirements for Azure DevOps
   - Prerequisites and technical requirements for Jira Cloud
   - Prerequisites and technical requirements for Jira Data Center
   - Prerequisites and technical requirements for ServiceNow
   - Prerequisites and technical requirements for GitHub Issues
   - Prerequisites and technical requirements for GitLab Issues
2. Set up the connection between Polaris and the issue tracking platform:
   - Connect Polaris to Azure DevOps
   - Connect to Jira Cloud
   - Connect to Jira Data Center
   - Connect Polaris to ServiceNow
   - Connect to GitHub Issues
   - Connect to GitLab Issues
3. (Optional) Create integration options to configure auto-close and two-way synchronization:
   - Create integration options for Azure DevOps
   - Create integration options for Jira Cloud
   - Create integration options for Jira Data Center
   - Create integration options for ServiceNow
   - Manage GitHub Issues settings for Polaris applications
   - Manage GitLab Issues settings for Polaris applications
4. Connect a project in Polaris to an issue tracking instance:
   - Connect a Polaris project to Azure DevOps
   - Connect a Polaris project to Jira Cloud
   - Connect a Polaris project to Jira Data Center
   - Connect a Polaris project to ServiceNow
   - Connect a project to GitHub Issues
   - Connect a project to GitLab Issues
