---
title: "Ways to triage issues in Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/ways-to-triage-issues-in-polaris.html"
content_id: "VDpqzlQJabOCG04bXwvyvQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:48.509158+00:00"
content_hash: "6af4e8cf8803a6eed1ae306aca4ffeceb3d23d2e33e653adf57b95154610c6db"
---

# Ways to triage issues in Polaris

In the issue list you can triage issues in several ways:

- Triage individual issues
- Batch triage by manually selecting multiple issues
- Batch triage by filtering
- Triage all

You'll need to use all of these, so we explain each approach on this page.

Note the following when triaging issues:

- If the same issue is detected in multiple branches of a project, you only need to triage it once. Triage actions (which can include setting or changing fix-by dates) are automatically applied across branches in a project.

  Important: Duplicate SCA issues may appear in the issues table. This occurs when the same issue is captured in separate package manager and signature analysis tests of the same branch. Duplicate SCA issues must be triaged separately.
- Component triage (see [Ways to triage components in Polaris](ways-to-triage-components-in-polaris.md)) can affect your results.
  - When you exclude a component, any non-dismissed issues derived from the component are automatically dismissed.
  - When you include a component, any issues related to the component that has been previously dismissed automatically, are now set to the default state (not triaged).

    Note: View components excluded on the Issues page by going to Filters > Triage Status > Dismissed > Components Excluded.
- If your organization uses a triage approval workflow, certain changes may require approval to take effect. After you triage an issue, the pending approval [image: triage icon pending] icon appears next to changes that require approval. You can monitor triage approval requests on the Triage Approval Overview Dashboard.

  **Known issue**: Issue severity and fix-by date changes that are pending approval do not appear on the Triage Approval Overview dashboard. These changes only appear in the dashboard after they're approved.

  See [Set up triage approval workflows](set-up-triage-approval-workflows.md) and Work with dashboards for more information.
- Dismissed issues and excluded components (via issue and component triage) are not included in reports. Dismissed issues and excluded components are typically hidden on dashboards that show issues and components; adjusting filters may allow you to see them. After you triage an issue (and approve the change, if required), it can take up to 60 minutes for the change to affect reports and dashboards.
- When you dismiss an issue linked to a ticket in Azure DevOps or Jira, the ticket may close automatically. See Automatically close tickets and synchronize triage statuses for more information.

## Tutorial: Triage issues in Polaris

Note: Interactive tutorials are updated periodically and may change without notice.

Figure 1. Tutorial: Ways to Triage Issues. *This interactive tutorial covers triaging issues in Polaris.* [Open in new tab.](https://www.iorad.com/player/2200870/Polaris--Ways-to-Triage-Issues)

## Triage individual issues

You might decide to review an issue independently to decide whether to dismiss it. In such cases, you can triage a single issue from within the issue view.

1. Select an issue to triage with the checkbox on the left side of the list.
2. Click Triage Selected.

   The Triage Selected Issue panel opens.

   [image: Screenshot of Individual Issue Triage]

   1. (Optional) Use the Owner dropdown menu to assign the issue to yourself or another user with access to the project.
   2. (Optional) Choose a Triage Status from the dropdown menu.

      If you select Dismissed, the Reason for Dismissal dropdown menu appears. Select a dismissal reason.
   3. Enter a comment that describes the change you made in the Comment field.

      Note: Depending on your approval workflow, this may be optional. A comment is always required when you set Triage Status to Dismissed and Reason for Dismissal to Other.
   4. (Optional) To change the severity of the issue, select a severity level from the Severity dropdown menu. You cannot change an issue's severity to Not Specified or None.

      Note: The Severity option only appears when triaging issue severity is enabled in the active project.
   5. (Optional) Set, change, or clear the issue's fix-by date.

      - To change the issue's fix-by date, select Specific Date with the Fix-By Date dropdown menu, and then select a date.

        Note: When you manually set or change an issue's fix-by date, the fix-by time is set to 5:00 PM in your local timezone.
      - To clear the issue's fix-by date, select No Date with the Fix-By Date dropdown menu.
   6. (Optional) Update the Azure DevOps or Jira ticket the issue is linked to using the Bug Tracking ID field.

      Important: The Bug Tracking ID field only appears when triaging issues in a project connected to Azure DevOps or Jira. For more information, see [Issue tracking integrations](issue-tracking-integrations.md).

      To unlink the issue from the ticket, clear the Bug Tracking ID field. To change the ticket the issue is linked to, enter a new ticket ID or key in the field.
3. Click Save.

   Important: If your organization uses a triage approval workflow, certain changes may require approval to take effect. After you triage an issue, the pending approval [image: triage icon pending] icon appears next to changes that require approval. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.

## Batch triage by manually selecting multiple issues

You can triage multiple issues you select manually.

1. Select issues to triage with the checkboxes on the left side of the list.
2. Click Triage Selected.

   The Triage Selected Issues panel opens.

   [image: triage bulk]
3. Use the checkboxes to select the fields you wish to modify, and make changes, as required.
   1. (Optional) To reassign the issues, select Owner, and then select a user (yourself or another user with access to the project) from the dropdown.
   2. (Optional) To change the status of the issues, select Triage Status, and then select a triage status from the dropdown.

      If you select Dismissed, the Reason for Dismissal dropdown menu appears. Select a dismissal reason.
   3. (Optional) To change the severity of the issues, select Severity, and then select a severity level from the dropdown. You cannot change an issue's severity to Not Specified or None.

      Note: The Severity option only appears when triaging issue severity is enabled in the active project.
   4. (Optional) To change the issues' fix-by date, select Fix-By Date, and then select a date from the picker.

      Note: When you manually set or change an issue's fix-by date, the fix-by time is set to 5:00 PM in your local timezone.
   5. (Optional) To update the Azure DevOps or Jira ticket the issues are linked to, select Bug Tracking ID.

      Important: The Bug Tracking ID field only appears when triaging issues in a project connected to Azure DevOps or Jira. For more information, see [Issue tracking integrations](issue-tracking-integrations.md).

      To unlink the issues from the tickets they're linked to, select Clear all values. To link the issues to a single ticket, select Assign new value, and enter the ticket's key or ID in the field.
   6. Enter a comment that describes the change you made in the Comment field.

      Note: Depending on your approval workflow, this may be optional. A comment is always required when you set Triage Status to Dismissed and Reason for Dismissal to Other.
4. Click Save.

   The triage options you selected are applied to *all* the issues you selected.

   Important: If your organization uses a triage approval workflow, certain changes may require approval to take effect. After you triage an issue, the pending approval [image: triage icon pending] icon appears next to changes that require approval. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.

## Batch triage by filtering

You can triage multiple issues you select with filters.

1. Apply filters to identify issues to triage:
   1. Click the filter [image: A screenshot of the icon used to open the filter panel.] icon.

      The filters panel opens.

      [image: triage filter branch]
   2. Expand filter categories and use the checkboxes to apply filters, as required.

      Tip: The quantity of matching issues appears in parenthesis next to each filter.
2. Click Triage All.

   The Triage Selected Issues panel opens.

   [image: triage filter branch triage]
3. Use the checkboxes to select the fields you wish to modify, and make changes, as required.
   1. (Optional) To reassign the issues, select Owner, and then select a user (yourself or another user with access to the project) from the dropdown.
   2. (Optional) To change the status of the issues, select Triage Status, and then select a triage status from the dropdown.

      If you select Dismissed, the Reason for Dismissal dropdown menu appears. Select a dismissal reason.
   3. (Optional) To change the severity of the issues, select Severity, and then select a severity level from the dropdown. You cannot change an issue's severity to Not Specified or None.

      Note: The Severity option only appears when triaging issue severity is enabled in the active project.
   4. (Optional) To change the issues' fix-by date, select Fix-By Date, and then select a date from the picker.

      Note: When you manually set or change an issue's fix-by date, the fix-by time is set to 5:00 PM in your local timezone.
   5. (Optional) To update the Azure DevOps or Jira ticket the issues are linked to, select Bug Tracking ID.

      Important: The Bug Tracking ID field only appears when triaging issues in a project connected to Azure DevOps or Jira. For more information, see [Issue tracking integrations](issue-tracking-integrations.md).

      To unlink the issues from the tickets they're linked to, select Clear all values. To link the issues to a single ticket, select Assign new value, and enter the ticket's key or ID in the field.
   6. Enter a comment that describes the change you made in the Comment field.

      Note: Depending on your approval workflow, this may be optional. A comment is always required when you set Triage Status to Dismissed and Reason for Dismissal to Other.
4. Click Save.

   The triage options you selected are applied to *all* the issues you selected.

   Important: If your organization uses a triage approval workflow, certain changes may require approval to take effect. After you triage an issue, the pending approval [image: triage icon pending] icon appears next to changes that require approval. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.

## Find triage history

Triage events are saved, and can be reviewed later. See [View issue history](view-issue-history.md) for more information.
