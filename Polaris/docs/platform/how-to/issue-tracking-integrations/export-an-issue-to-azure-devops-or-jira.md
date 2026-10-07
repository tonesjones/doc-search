---
title: "Export an issue to an issue tracking instance"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/export-an-issue-to-an-issue-tracking-instance.html"
content_id: "wYmexZHmWc5xs1ZJyzvsNA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:21.342905+00:00"
content_hash: "1ccd6467d71d35fba0f4b8c62d496c06cf9666516a18662c983850e3476b9592"
---

# Export an issue to an issue tracking instance

After you connect a project with an external issue tracking integration, you can manually export individual DAST, SAST, and SCA issues from Polaris to an issue tracking instance.

## Prerequisites

Before you can export issues to an external issue tracking instance:

- An Organization Administrator must do one of the following:
  - Connect to an Azure DevOps instance
  - Connect to a Jira instance
  - Connect to a ServiceNow instance
  - Connect to GitHub Issues via SCM import (Organization Application Managers can also complete this)
  - Connect to GitLab Issues via SCM import (Organization Application Managers can also complete this)
- A user with permissions to manage project settings must do one of the following:
  - Connect the Polaris project to Azure DevOps
  - Connect the Polaris project to Jira
  - Connect the Polaris project to ServiceNow
  - Connect the Polaris project to GitHub Issues
  - Connect the Polaris project to GitLab Issues

Important: For GitHub Issues and GitLab Issues integrations, only SAST and SCA issue export is supported. DAST export is not supported at this time.

## Export a single issue to an issue tracking instance

You can export individual DAST, SAST, and SCA issues from the Issues tab. The selected issue is exported to the issue tracking instance that is associated with your Polaris project and the issue type you selected in your Polaris settings.

1. From the Issues tab in Polaris, select the issue you wish to export, and then select Export 1 Selected.

   [image: A screenshot of the Export Selected Issue panel.]

   Important: If the issue you selected is already linked to a ticket (indicated by a link in the Bug Tracking column), the export will be disabled. To export an issue that is already linked, you must first unlink it. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

   Tip: To quickly identify issues that are already linked to tickets, sort the Issues view by the Bug Tracking column.
2. In the Export Selected Issue panel, select External Bug Tracker.

   Tip: Hover over the question mark icon [image: export to tracker icon] to view the URL/instance the issue will be exported to.
3. Click Export 1 Issue.

   After you refresh the page, a link to the ticket appears in the Bug Tracking column.

## Export multiple issues to an issue tracking instance

You can export multiple DAST, SAST, and SCA issues at once from the Issues tab. When exporting multiple issues, you can choose to create one ticket for all selected issues (bundled) or create one ticket for each issue.

1. From the Issues tab in Polaris, select the issues you wish to export, and then select Export Selected.

   [image: A screenshot of the Export Selected Issues panel.]

   Important: If any of the issues you selected are already linked to a ticket (indicated by a link in the Bug Tracking column), the export will be disabled. To export issues that are already linked, you must first unlink them. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

   Tip: To quickly identify issues that are already linked to tickets, sort the Issues view by the Bug Tracking column.
2. In the Export Selected Issues panel, select External Bug Tracker.

   Tip: Hover over the question mark icon [image: export to tracker icon] to view the URL/instance the issue will be exported to.
3. Choose how you want to export the selected issues:
   - Create 1 ticket for all issues (bundle): Create one ticket that is linked to all selected issues. The ticket includes a table that lists all linked issues, remediation guidance for each issue, and links you can use to view the issues in Polaris.
   - Create 1 ticket per issue: Create a separate ticket for each selected issue. Each ticket includes remediation guidance for the issue, and links you can use to view the issue in Polaris.
4. Click Export Issues.

   After you refresh the page, links to the ticket (or tickets) appear in the Bug Tracking column.
