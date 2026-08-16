---
title: "Export an issue to Azure DevOps or Jira"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/export-an-issue-to-azure-devops-or-jira.html"
content_id: "wYmexZHmWc5xs1ZJyzvsNA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:32.305685+00:00"
content_hash: "d1dad2567e897a40a006d6fea3e00f1193688842775e872f4a2a79c905d964d4"
---

# Export an issue to Azure DevOps or Jira

After you connect a project to Azure DevOps or Jira, you can manually export individual DAST, SAST, and SCA issues from Polaris to Azure DevOps or Jira.

## Prerequisites

Before you can export issues to Azure DevOps or Jira:

- An organization administrator must Connect Polaris to Azure DevOps or Connect Polaris to a Jira instance.
- A user with permissions to manage project settings must Connect the Polaris project to Azure DevOps or Connect the Polaris project to Jira.

## Export an issue to Azure DevOps or Jira

You can export individual DAST, SAST, and SCA issues from the Issues tab. The selected issue is exported to the Azure DevOps or Jira project that is associated with your Polaris project and the issue type you selected in your Polaris settings.

1. From the Issues tab in Polaris, select the issue you wish to export, and then select Export 1 Selected.

   [image: A screenshot of the Export Selected Issue panel.]

   Important: If the issue you selected is already linked to a ticket (indicated by a link in the Bug Tracking column), the export will be disabled. To export an issue that is already linked, you must first unlink it. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

   Tip: To quickly identify issues that are already linked to tickets, sort the Issues view by the Bug Tracking column.
2. In the Export Selected Issue panel, select External Bug Tracker.

   Tip: Hover over the question mark icon [image: export to tracker icon] to view the Azure DevOps/Jira instance the issue will be exported to.
3. Click Export 1 Issue.

   After you refresh the page, a link to the ticket appears in the Bug Tracking column.

## Export multiple issues to Azure DevOps or Jira

You can export multiple DAST, SAST, and SCA issues at once from the Issues tab. When exporting multiple issues, you can choose to create one ticket for all selected issues (bundled) or create one ticket for each issue.

1. From the Issues tab in Polaris, select the issues you wish to export, and then select Export Selected.

   [image: A screenshot of the Export Selected Issues panel.]

   Important: If any of the issues you selected are already linked to a ticket (indicated by a link in the Bug Tracking column), the export will be disabled. To export issues that are already linked, you must first unlink them. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

   Tip: To quickly identify issues that are already linked to tickets, sort the Issues view by the Bug Tracking column.
2. In the Export Selected Issues panel, select External Bug Tracker.

   Tip: Hover over the question mark icon [image: export to tracker icon] to view the Azure DevOps/Jira instance the issue will be exported to.
3. Choose how you want to export the selected issues:
   - Create 1 ticket for all issues (bundle): Create one ticket that is linked to all selected issues. The ticket includes a table that lists all linked issues, remediation guidance for each issue, and links you can use to view the issues in Polaris.
   - Create 1 ticket per issue: Create a separate ticket for each selected issue. Each ticket includes remediation guidance for the issue, and links you can use to view the issue in Polaris.
4. Click Export Issues.

   After you refresh the page, links to the ticket (or tickets) appear in the Bug Tracking column.
