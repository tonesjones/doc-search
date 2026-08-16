---
title: "Issue tracking integrations"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integrations.html"
content_id: "kHbU8EYkPHhMK2qTu_ukSQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:29.320626+00:00"
content_hash: "5e3ce3938d120e959a766d5568f812938255c7e725ea3bce06a64bb975413775"
---

# Issue tracking integrations

Set up an issue tracking integration to send issues captured in Polaris to Azure DevOps or Jira.

After you set up an issue tracking integration, you can export DAST, SAST, and SCA issues in your Polaris projects to Azure DevOps or Jira. You can export a single issue or multiple issues at once. When exporting multiple issues, you can create one ticket for all selected issues (bundled) or create individual tickets for each issue. Polaris creates tickets (work items, or Jira issues) that include detailed information about the issue, remediation guidance, and helpful links. DAST issues also include evidence of the issue found; for example, the API endpoint. You can select the type of ticket Polaris creates when you set up the integration. See [Export an issue to Azure DevOps or Jira](issue-tracking-integrations/export-an-issue-to-azure-devops-or-jira.md) for more information.

Additionally, setting up an issue tracking integration allows you to create tickets using issue policies (with the Create and bundle to 1 external issue tracker ticket action). When violations are captured in a test of a project's default branch, Polaris creates a single ticket linked to all of the violating issues. The ticket includes the name of the violated policy, the names of violated rules, and links you can use to view issues that violate different rules in Polaris. See [Issue policies](create-and-manage-policies/issue-policies.md) for more information.

Find links to the tickets Polaris creates on the Issues tab (in the Bug Tracking column), and the Issue Details panel (under Bug Tracking).

Note: You can add multiple instances of Azure DevOps and Jira to your organization, but each Polaris project can only be connected to one Azure DevOps or Jira project.

## Automatically close tickets and synchronize triage statuses

Optionally, configure Polaris to automatically close tickets in Azure DevOps or Jira when issues are absent or dismissed. For Jira Cloud, you can also configure two-way synchronization of Polaris triage statuses and Jira ticket statuses.

Auto-close is optional and configurable for both Azure DevOps and Jira Cloud integrations. When enabled, Polaris automatically closes tickets when the linked issue is dismissed (any reason) or absent in subsequent scans. It applies to all issue types (SAST, SCA, DAST).

For Jira Cloud integrations, you can also configure triage status sync. When configured:

- Triage state changes in Polaris automatically update the status of linked Jira tickets.
- Ticket status changes in Jira automatically update the triage status of linked Polaris issues.
- Optionally, fix-by dates in Polaris and due dates in Jira are kept in sync.

Important: Triage state sync is supported for Jira Cloud only. Jira Data Center is not supported.

Please note:

- Tickets created for policy violations (bundled tickets) are not supported for auto-close or triage status sync. Both features only work for individually exported issues with a 1:1 link between a Polaris issue and a ticket.
- Polaris does not re-open tickets once they are closed due to auto-close, even if the linked issue is detected again in a subsequent scan. When a previously absent issue is re-detected, the original ticket remains closed and no new ticket is created automatically.
- By default, after you set up an issue tracking integration (that includes the auto-close integration option), auto-close is only enabled on the project's default branch.

For Jira Cloud triage status sync, also note:

- If a Jira workflow blocks a status transition, Polaris reverts the triage status to its previous value and logs the error in the issue's triage history.
- If the Jira token expires, triage changes in Polaris still succeed, but are not reflected in Jira until the token is renewed. The error is logged in the issue's triage history and shown in the integration's configuration.
- Triage state changes triggered by Jira sync do not require approval, even if triage approval workflows are configured.
- Jira ticket statuses that have no configured mapping in Polaris do not trigger a triage status change in Polaris.
- Issue counts in portfolio summary views, dashboards, and reports reflect triage status changes triggered by Jira sync, but these counts can take up to 60 minutes to update.

To use these features, create integration options that define the status mappings and auto-close behavior, then enable those options at the project level. See Create integration options for Azure DevOps and Create integration options for Jira for more information.

## Edit links between issues and tickets

After you set up an issue tracking integration, you can update the links between issues in Polaris and tickets in Azure DevOps or Jira. This allows you to:

- Link issues to a ticket that already exists in Azure DevOps or Jira.
- Change the ticket issues are linked to.
- Delete links to tickets.

Please note:

- Like other triage actions, ticket links are shared across branches in a project. If the same issue is detected on multiple branches and you link it to a ticket on one branch, that ticket link applies to the issue across all branches.
- When you manually link an issue to a ticket (or change the ticket an issue is linked to), the ticket you specify must:
  - Exist in the Azure DevOps or Jira project you connected your Polaris project to.
  - Match the ticket type configured in your Polaris project's issue tracking integration. For example, if a Polaris project's issue tracking integration is configured to create tasks in Azure DevOps or Jira, you cannot create links to epics.
- When you change links manually (including creating, updating, or deleting links), the ticket's description doesn't change. Changing or removing ticket links in Polaris does not alter, update, or close the tickets in Azure DevOps or Jira.
- Similarly, modifying or deleting a ticket in Azure DevOps or Jira won't affect issues in Polaris.
- All link updates (including creating, updating, or deleting links) are tracked as triage events, and appear in the issue's triage history. See [View issue history](view-issue-history.md) for more information.

You can edit ticket links using the Bug Tracking ID field in the triage panel. See [Ways to triage issues in Polaris](ways-to-triage-issues-in-polaris.md) for more information.

## Set up an issue tracking integration

To set up an issue tracking integration, you'll need to perform the following tasks:

1. Ensure you meet the prerequisites for the integration, which vary from platform to platform:
   - Prerequisites and technical requirements for Azure DevOps
   - Prerequisites and technical requirements for Jira
2. Set up the connection between Polaris and Azure DevOps or Jira:
   - Connect Polaris to Azure DevOps
   - Connect Polaris to a Jira instance
3. (Optional) Create integration options to configure auto-close and, for Jira Cloud, triage status sync:
   - Create integration options for Azure DevOps
   - Create integration options for Jira
4. Connect a project in Polaris to a project in Azure DevOps or Jira:
   - Connect a Polaris project to Azure DevOps
   - Connect a Polaris project to Jira
