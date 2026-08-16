---
title: "Navigation and features"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/navigation-and-features.html"
content_id: "tgDrNZagN07Dy_FtQ7OMOA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:08.139014+00:00"
---

# Navigation and features

The modern UI provides a consistent layout across all pages. A left sidebar contains
primary navigation, and the main content area displays page-specific information and
controls.

## Sidebar

The sidebar appears on the left side of every page and contains the following
elements:

- **Black Duck Coverity** — Displays the product name and the current snapshot
  context.
- **Projects & hierarchies** — Expands to show the
  Projects link, which opens the Projects page.
- **Help & support** — Expands to show help and support resources.
- **Search CIDs** — A search box at the bottom of the sidebar that allows you
  to search for issues by CID number.
- **User information** — Displays the signed-in user name and email address at
  the bottom of the sidebar.

## Projects

The Projects page is the landing page of the modern UI. It displays all projects that
you have access to.

The Projects page is currently in beta and subject to change.

Figure 1. Projects page in the modern UI
  
 [image: Screenshot of the Projects page showing the project list.]

**Toolbar**

The toolbar above the projects table provides the following controls:

- View | All Projects — A dropdown that allows you to
  select a predefined or custom view to filter the projects list.
- Add filters — Opens a dropdown to add filters that narrow
  the list of displayed projects.
- **Save** — Allows you to save the current view.
- **Save As** — Allows you to save the current view under a new name.
- **Search** — Searches the projects table.
- **Column settings** — Configures which columns appear in the table.
- **Export** — Exports the projects list as CSV or XML.

**Projects table**

The table displays projects with the following sortable columns by default:

- **Project** — The project name, displayed as a link. Click a project name to
  view its issues.
- **Description** — A summary of the project.
- **Last Commit** — The date and time of the most recent commit to the
  project.

To view issues, click a project name.

Each column allows you to sort in ascending or descending order, and clear the
sort.

You may click a column header and drag the column if reordering is needed.

Each row includes action icons to copy or delete the project.

The bottom of the table displays the total number of projects and a control to set
the number of projects shown per page.

## Issues

The Issues page appears when you click a project name on the Projects page. It
displays all issues detected in the selected project.

A breadcrumb at the top of the page shows Projects >
*project name*, allowing you to navigate back to the Projects page. You can
use the dropdown next to the project name to switch to a different project.

**Issues tab toolbar**

The toolbar above the issues table provides the following controls:

- View | Select view — A dropdown that allows you to select
  a predefined or custom view to filter the issues list. If the view has been
  modified, the label displays Select view (modified).

  Note: You can mark a view as a favorite to display it at the top of the view
  list for quick access.
- **Save** — Saves the current view.
- **Save As** — Saves the current view under a new name.
- **Reset** — Returns table to previous state.
- **Share** — Allows you to select the users and groups that will have access
  to the current view. (This control is not available in the current release but
  will be added to a later release.)
- Add filters — Opens a dropdown to add filters that narrow the list of
  displayed issues. Filters may be added without saving the current view.

  Note: Filter names used to customize the view are currently
  only available in English.
- **Export** — Exports the issues list as CSV or XML.
- **Column settings** — Configures which columns appear in the table.

If AI-assisted triage is available
for the project, a banner displays Let AI assist with triaging
issues! with a Learn More link.

**Issues table**

The table displays issues with the following sortable columns by default:

- **Impact** — The impact level of the issue.
- **CID** — The Coverity issue identifier. Click a CID to view the issue
  details.
- **Checker** — The checker that detected the issue.
- **Category** — The issue category and subcategory.
- **Status** — The current status (for example, New, Triaged, Dismissed).
- **Classification** — The triage classification (for example, Unclassified,
  Bug, False Positive).
- **File** — The file where the issue was detected, and the component if
  defined.

More columns are available in Columns settings.

Each row includes a checkbox for selecting issues for bulk triage. After selecting
one or more issues, click the Triage button that appears to
open the triage controls. Click a CID to open the issue detail view.

Each column allows you to sort in ascending or descending order, and clear the sort.
You may click a column header and drag the column if reordering is needed.

The bottom of the table displays pagination controls, including page numbers and a
control to set the number of issues shown per page.

## Issue detail view

The issue detail view appears when you click a CID on the Issues page. It displays
the source code and triage controls for the selected issue in a split-pane layout.
Unlike the classic interface, where issue details appear in panels alongside the
issues list, the modern UI opens a full dedicated page for each issue.

**Navigation**

Navigation controls appear above the issue detail area:

- Previous issue — Navigates to the previous issue in the
  filtered list.
- Next issue — Navigates to the next issue in the filtered
  list.
- Back to Issues — Returns to the issues list.

**Issue summary**

A summary card displays the CID number, the issue type (displayed as a link), a
description of the issue, the function where it occurs, and a CWE identifier
link.

**Source code pane**

The source code pane displays the source file with issue event markers. The pane
includes the following controls and features:

- **File selector** — A dropdown at the top of the pane that displays the
  current file name. Click the dropdown to search for and switch between files
  related to the issue.
- **Source code gutter settings** — A menu that controls what information
  appears in the source code gutter. Options include:
  - Line Numbers — Shows or hides line numbers.
  - Issue Events — Shows or hides issue event markers
    in the gutter.
  - SCM Author — Shows or hides the author of each
    line from source control.
  - SCM Modification Date — Shows or hides the
    modification date from source control.
  - SCM Revision — Shows or hides the revision
    identifier from source control.
- **Fullscreen** — Expands the source code pane to fill the viewport.
- **File tree** — Toggles a file tree panel on the left side of the source code
  pane, showing the directory structure of the project files.

Issue event markers appear as colored icons in the source code. Each marker indicates where an
event in the issue path occurs. Click an event marker to see the CID, issue type,
checker name, and event description.

Note: In a future version,
other issues in the source file will appear with "select issue" links that will
allow you to switch to that issue.

**Triage pane**

The triage pane appears on the right side of the issue detail view. It contains
collapsible sections for triaging the issue and viewing related information.

The **Triage** section provides the following controls:

- **Classification** — A dropdown to categorize the issue (for example,
  Unclassified, Bug, False Positive, Intentional).
- **Severity** — A dropdown to set the severity level (for example,
  Unspecified, Major, Minor).
- **Action** — A dropdown to specify the required action (for example,
  Undecided, Fix Required, Ignore, Modeling Required).
- **Owner** — A dropdown to assign the issue to a user or leave as
  Unassigned.
- **Comments** — A text field to add notes about the issue or triage decision.
  Previous comments appear in the Triage History section.

Note: The modern UI does not include the option to Select Stores.
This feature will be added in a future release. To apply triage to a subset of
triage stores, the classic UI must be used.

Two buttons appear at the bottom of the Triage section:

- Apply + Next — Saves the triage changes and navigates to
  the next issue.
- Apply — Saves the triage changes and remains on the
  current issue.

The **Projects & Streams** section lists the streams in the current project
where the issue occurs.

The **Detection History** section shows the date and time the issue was detected
in the latest snapshot and the stream where it was last detected.

The **Triage History** section lists all previous changes to triage attributes
with timestamps and user names. If no changes have been made, it displays "-- No
Change --".

The **Occurrences** section shows the events contributing to the issue. It
includes a stream selector dropdown and Expand All /
Collapse All controls. Each event displays a sequence
number, tag, file name, and line number.

The **Standard Attributes** section displays any standard attributes associated
with the issue. If none are defined, it displays "None".
