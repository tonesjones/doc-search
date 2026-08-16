---
title: "Work with dashboards"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/work-with-dashboards.html"
content_id: "v4XJ9XEZEsiuKdX7WRE4Wg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:35.626053+00:00"
content_hash: "14d475852e52d6b11f7a5d38b1204cdabbd107782cd9de1765c2b119ae09b0e5"
---

# Work with dashboards

Use the Dashboards page to analyze and visualize SAST, SCA, and DAST test and issue data from your applications and projects.

## Overview

The Dashboards page provides access to interactive charts and other representations of your test and issue data. It's available for all Polaris users, and only displays data from the applications they have access to. You can navigate between available dashboards using the drop-down menu in the top-left corner of the page.

Dismissed issues and excluded components are typically hidden on dashboards that show issues and components, but adjusting filters may allow you to see them. Issues you import from third-party tools appear in dashboards, but the components and licenses associated with issues you import do not.

Note: See [Roles and permissions](../reference/roles-and-permissions.md) for more information on roles and permissions.

Switch between dashboards using the dropdown menu near the top of the page. Some dashboards have information spread across multiple tabs.

### Tutorial: Dashboards in Polaris

Note: Interactive tutorials are updated periodically and may change without notice.

Figure 1. Tutorial: Polaris: Insights. *This interactive tutorial covers the basics of working with Dashboards.* [Open in new tab.](https://www.iorad.com/player/2202769/Polaris--Insights)

### Interact with charts

Each dashboard is a collection of interactive widgets, charts, and tables that provide information about your applications, projects, and Polaris usage.

You can:

- Hover your mouse over chart segments to see additional information.
- Select chart segments to quickly apply filters.
- Select an item in a chart's legend to hide or show data.

### Filters

The Dashboards interface contains multiple options for filtering available data, giving you precise control over the information displayed in graphs and reports.

Note: The filter options available vary depending on which dashboard is selected.

To get started with filters, use the various fields on the left-hand side of the page to choose values relevant to the scope of data that you need. To reset the filter values back to their defaults, select CLEAR ALL. The current dashboard won't update while you're making changes, so when you're ready to see the filtered data, select APPLY FILTERS.

Note: After filtering a dashboard you can save the current view, letting you reapply the same filter criteria quickly and easily in future. See Create and manage saved filters for more information.

You can apply a saved filter using the Saved Filters drop-down menu near the top of the page. You can deselect the currently applied filter by pressing the X icon next to its name. To revert the current dashboard to its default view, select Reset filters.

Saved filters are unique to individual users. If you create one, only you have access to it, but you can share a copy of it with users and groups within your organization.

Important: Most users can only share saved filters with people and groups that have the same set of applications as themselves. Org admins can share with any user or group, but doing this will allow the recipients to see all settings in the shared filter, even if they don't have access to the applications mentioned. The admin will be warned of this before the filter is shared.

Shared copies of saved filters have the following characteristics:

- Distinct from the original filter, so making changes to a saved filter won't affect anyone else who has a copy of it.
- Filter name includes the name of the person who shared it. Also, if the shared filter has the same name as one of your existing saved filters, the end of its name will get a distinguishing instance number. For example, the shared filter might be named `DAST data for July - shared by Bob Slydell - 2`.
- Initially appear at the end of the recipient's Saved Filters list, but can be reordered like any other saved filters.

Important: For each user, the maximum number of saved filters per dashboard (including copies) is 100. If someone tries to share a saved filter with you when you already have the maximum number, you won't receive it and neither person will be notified.

### Refresh rate

Dashboards represent a snapshot of your Polaris data. It can take up to 60 minutes for the following changes to be reflected in the active snapshot:

- New issue data from a test.
- Issue and component triage actions.

  Note: Dismissed issues and excluded components (via issue and component triage) are typically hidden on dashboards that show issues and components; customizing filters may allow you to see them. Issue and component triage actions only affect dashboards after changes are approved.
- Components you add, edit, or delete.
- Changes made to application, project, or branch settings (including changes to labels).
- Changes made to file and folder exclusion rules.

The page does not automatically refresh over time, but you can manually pull the latest snapshot using one of the following methods:

- To refresh the whole dashboard, select options [image: dashboard options button] > Refresh dashboard
- To refresh a single chart or widget, select options [image: dashboard options icon] > Force refresh

Important: Manually refreshing a dashboard, chart, or widget has no effect on when the underlying data snapshot is updated.

### Dashboard reference

The following table includes short descriptions of the dashboards included with Polaris:

Table 1. Dashboard reference

| Dashboard name | Summary |
| --- | --- |
| Component Management Dashboard | Provides an overview of component and license usage in your portfolio. Includes charts that show the quantity of components grouped by security risk, and the quantity of licenses grouped by license type. Tables show how common different components are throughout your portfolio, how many versions of a component are captured in your portfolio, and the relative risk of different applications and projects in your portfolio. While the default (out-of-the-box) filters are active, the dashboard includes all component security risks and license types. Tip: Use the Component and Component Version filters to assess the prevalence of specific components in your portfolio. |
| Executive Overview Dashboard | Provides an overview of application security and policy compliance in your organization. Includes charts that show open, introduced, and absent issues in your portfolio over time. While the default (out-of-the-box) filters are active, the dashboard includes results from the past year. |
| Issue Summary Dashboard | Visualize your organization's security profile across applications and projects. While the default (out-of-the-box) filters are active, dismissed issues are ignored. Open the Issue List tab (near the top of the dashboard) to view issue data in a sortable table. Columns include Application, Project, Issue Type, Severity, Test Type, CWE ID, Vulnerability Id, Location Vulnerability id, CISA KEV, Fix By, Fix By Status, Owner, First Detected Date, Triage Status, Owner, Link (a direct link to each issue's details in Polaris), etc. Tip:  - Apply a Standard filter to populate the Standard Categories By Total Issues chart. - Apply an Exposure (matches SCA only) filter to view reachability and/or undetermined component vulnerabilities. |
| Onboarding Dashboard | View the quantity of applications and projects created in a time period, and how many of the applications and projects were tested. Includes trend charts for applications and projects created, and a table with the total number of tests run per project. |
| Polaris Risk Dashboard | View the risk scores of applications in your portfolio, the average risk score of applications in your portfolio, and 10 applications with the highest risk scores in your organization. Note: Risk scoring data is only available while the risk scoring feature is enabled. See [Risk scoring in Polaris](risk-scoring-in-polaris.md) for more information. |
| Policy Overview Dashboard | View the quantity of issues in your portfolio that violate your organization's policies. Includes charts that show applications and projects with the most policy violations, and widgets that show the quantity of applications and projects using your organization's default policies. Tip: Apply the Policy Name filter to limit results to issues that violate specific policies. |
| Portfolio ROI Dashboard | View the impact of Polaris on your portfolio's security profile over time. Includes charts that show open, detected, reintroduced, and absent issues in your portfolio over time. It includes an exposure filter to view reachability and/or undetermined component vulnerabilities found in SCA testing. By default, results are limited to issues first detected in the last 12 months. You can extend or shorten this duration with the Issues First Detected in filter. |
| Remediation Dashboard | Shows the average time (in days) it takes to remediate issues (that is, from the time an issue is detected, the time it takes for the issue to be triaged and dismissed *or* no longer detected in tests) in your portfolio. Includes charts that show the 10 applications with the longest/shortest average remediation times in your portfolio, along with tables that show per-application, per-issue-type, and per-issue-severity remediation times. While the default (out-of-the-box) filters are active, the dashboard includes data from all the applications you have access to, and all issue severities. |
| Table - Component Search | View all the components used in your organization's applications and projects, along with the license each component is subject to. It includes an exposure filter to view reachability and/or undetermined component vulnerabilities found in SCA testing. |
| Table - License Search | View all the licenses your organization's applications and projects are subject to, along with a description of each license, and each license's family. |
| Test Summary | Visualize the quantity of tests run against applications and projects in your organization. Note: To include DAST test results, the Display Default Branch filter must be set to Include all (default) or true. |
| Triage Approval Overview Dashboard | Provides a centralized view of triage approval requests across applications and projects. Includes widgets that show the total number of pending, approved, and rejected triage requests, along with a detailed table of individual triage approval requests. While the default (out-of-the-box) filters are active, the dashboard includes data from all applications you have access to. Tip: Use the Triage Status filter to view requests by their approval state (Pending, Approved, or Rejected). Use the Approver filter to view requests assigned to specific approvers. |

Tip: Apply the Application Label, Project Label, and Branch Label filters (available on most dashboards) to limit data to applications, projects, and branches with particular labels.

## Save a dashboard (PDF, image)

To save a dashboard as an image or PDF, follow these steps:

1. (Optional) Apply filters and customize the dashboard, as required.
2. Select the options [image: dashboard options button] button near the top of the page, select Download, and select a format (Export to PDF or Download as Image).

   Note: Saving a dashboard as an image is not supported in Firefox.

## Export issue metadata (CSV, Excel, image)

You can export issue metadata to CSV, Excel, or an image using the Issue Summary Dashboard.

Tip: We strongly recommend you use the issue export functions available on the Portfolio Project page instead. See [How to export issues to CSV or JSON](how-to-export-issues-to-csv-or-json.md) for more information.

To export issue metadata, follow these steps:

1. After you open the Issue Summary Dashboard, open the Issue List tab.
2. (Optional) Adjust filters, as required.

   Note: Exports are limited to 100,000 issues at a time.
3. Select Options [image: dashboard options icon] > Download, and select a format (Export to .CSV, Export to Excel, Download as image).

   [image: dashboard issue export]

## Create and manage saved filters

Saving the active filter lets you quick reapply it later to get consistent insights into your Polaris data.

Saved filters are:

- **User-specific:** They are unique to the user who created them, but can be shared as copies with other users and groups.
- **Dashboard-specific:** Each saved filter is associated exclusively with the dashboard for which it was created, and cannot be transferred between dashboards.

### Create a saved filter

Follow these steps to create a saved filter:

1. Open the dashboard you wish to create a saved filter for.
2. Use the options in the Filters panel to adjust the scope of the dashboard, as required.
3. Select APPLY FILTERS, near the bottom of the Filters panel.
4. Select Save filter (or Save filter > Save as... if you already have a saved filter applied).

   The New Saved Filter window appears.
5. Enter a Filter name.

   Saved filter names can be up to 80 characters long, and can include spaces and special characters.
6. Select Save.

You can apply the new saved filter using the Saved Filters drop-down menu near the top of the page.

### Edit a saved filter

Follow these steps to edit a saved filter:

1. Open a dashboard and use the Saved Filters drop-down menu to select the saved filter you wish to modify.
2. Use the options in the Filters panel to adjust the scope of the dashboard, as required.

   Note: To revert any changes you've made to the current filter since it was applied or last saved, select Undo changes.
3. Select APPLY FILTERS, near the bottom of the Filters panel.
4. Select Save filter > Save changes.

### Rename a saved filter

Follow these steps to change the name of a saved filter:

1. Open the dashboard linked to the saved filters you wish to rename.
2. Select the Saved Filters drop-down menu, and then select Manage Saved Filters.

   The Manage Saved Filters window opens.
3. Rename the filter, as required.
4. Select Save.

### Share a copy of a saved filter

Follow these steps to send a copy of a saved filter to one or more users or groups in your organization:

1. Open the dashboard linked to the saved filter you wish to share.
2. If the intended filter is not already applied, select the Saved Filters dropdown menu, and then select the name of that filter.
3. Select the share [image: dashboard share button] button near the saved filters list.

   The Send a Copy of Saved Filter dialog opens.
4. Select the Select Users or Groups field.

   The Users and Groups tabs appear.

   Note: You must select at least one user or group to share the saved filter with.

   Important: Unless you're an admin for your organization, you can only select users or groups who have access to all applications mentioned in the saved filter. If you are an organization admin, sharing with people who can't already access the relevant applications will allow recipients to see the filter values, so you'll be warned of this before confirming the share action.
5. To add users, select the Users tab and use the Search field to locate them based on their name or email address, then select them.
6. To add groups, select the Groups tab and use the Search field to locate them based on their name, then select them.

   Note: Changes made to a group after sharing a filter with it won't affect who has access to the filter; people added to the group won't automatically receive a copy of the filter, and people removed from the group won't lose their copy.
7. Select Send.

### Reorder saved filters

Follow these steps to change the order of filters in the Saved Filters drop-down menu:

1. Open the dashboard linked to the saved filters you wish to sort.
2. Select the Saved Filters dropdown menu, and then select Manage Saved Filters.

   The Manage Saved Filters window opens.
3. Drag and drop saved filters using the [image: dashboards sort filter icon] icon, as required.
4. Select Save.

### Delete a saved filter

Follow these steps to delete a saved filter:

1. Open the dashboard linked to the saved filter you wish to delete.
2. Select the Saved Filters dropdown menu, and then select Manage Saved Filters.

   The Manage Saved Filters window opens.
3. Select the delete [image: dashboards delete filter icon] icon next to the saved filter you wish to delete.
4. Select Save.

## Restore a dashboard's default filters

To restore a dashboard's default (out-of-the-box) filters, select Reset Filters near the top of the page.
