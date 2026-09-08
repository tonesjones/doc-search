---
title: "Automatic Issue Creation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/automatic-issue-creation.html"
content_id: "RIksmDxd4YugwZGc1wfNow"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:19.925872+00:00"
content_hash: "5f1911e9dc663aceebb6453718784a2e0dedcaee0bcb1e329119d88daacbf06a"
---

# Automatic Issue Creation

Software Risk Manager can be configured to automatically create issues or work items
based on a number of different criteria. This is configurable on the "Auto Create" tab
of the Issue Tracker Configuration screen.

By default, Auto Create is disabled. To enable Auto Create, Jira, GitHub and GitLab users should
check the box labeled "Automatically create issues for findings," Azure DevOps users
should check the box labeled "Automatically create work items for findings," and
ServiceNow users should check the box labeled "Automatically create incidents for
findings."

After enabling Auto Create, the rest of the form will be enabled and further
configuration options are available.

## Issue Configuration

[image: image]

The following configuration settings are also available:

- **Create new issues instead of reopening closed issues.** Whether Software Risk Manager
  should create new issues for findings returning from Gone finding status instead of reopening
  closed ones. This is useful for workflows where closed/done issues cannot be reopened.
- **Branches.** What branches Software Risk Manager will use when
  creating issues or work items. If left blank, all branches will be used.
- **Issue Type.** What "Issue Type" Software Risk Manager will use when
  creating issues or work items.
- **Issue Assignee.** The user Software Risk Manager will assign these
  issues to (Jira and ServiceNow only; Azure DevOps, GitHub and GitLab users can
  configure this on the "SRM -> *" tab).
- **Finding Grouping.** How Software Risk Manager should group findings (or
  not) when creating issues or work items.
- **Ticket Summary Template.** The summary or title Software Risk Manager
  will provide when creating issues or work items.

## Finding Grouping

The "Finding Grouping" section allows users to either have Software Risk Manager
create one issue or work item per finding, or group multiple findings together per
single issue or work item. If *Multiple findings per ticket, grouped by...* is
selected, the dropdown menu will be populated.

[image: image]

The selection(s) made here determines how findings are grouped. Multiple selections
are allowed, but the order of the selections matters. For example, if "Location" is
selected first, and "Severity" is selected second, Software Risk Manager will first
group findings by their Location and then by their Severity. Therefore, if you had
two findings at the same location but with different severities, these findings
would be associated to different issues or work items.

## Ticket Summary

The *Ticket Summary - Template* field determines what Software Risk Manager uses
for the summary or title when issues or work items are created. This field supports
the same templates used on the field mappings tab (i.e., "SRM -> *" tab). For
example, if you want Software Risk Manager to create issues or work items and have
the summary display the finding's location and severity, you could configure a
Ticket (Work Item) Summary as
follows:

```
{{finding.location.path.path}} {{finding.severity.name}}
```

The *Insert placeholder...* control under the input will help in determining
what kind of template expression to use.

## Use Policy Rules or Filtering

[image: image]

The option to "Use Policy" or "Use Filters" to create issues allows users to choose
to either use configured Policy rules or the following filter options to determine
which findings should have an issue automatically created.

Note: By default, "Use Policy to create issues" is selected. Users must assign a policy
to this project, and that policy must have a rule where the action is "Create
Ticket(s)." See Configuring
Polices for more information.

## Filtering

SRM provides a number of options you can use to filter which findings should have
issues automatically created.

[image: image]

These filters include the following:

- **Only create tickets or work items for New findings.** If this is checked,
  only findings with a status of "New" will have issues or work items created for
  them.
- **Rule.** Select any number of Rules and only findings that match the
  selected Rules will have issues or work items created for them.
- **Tool.** Select any number of Tools and only findings that match the
  selected Tools will have issues or work items created for them.
- **Severity.** Check any number of Severities and only findings that match the
  checked Severities will have issues or work items created for them.
- **Tool Overlaps.** Select a number range and only findings that are in the
  selected Tool Overlap range will have issues or work items created for
  them.
- **Detection Method.** Check any number of Detection Methods and only findings
  that match the checked Detection Methods will have issues or work items created
  for them.
- **CWE.** Select any number of CWEs and only findings that match the selected
  CWEs will have issues or work items created for them.
- **Standard.** Select any number of Standards and only findings that match the
  selected Standards will have issues or work items created for them.

If a filter is left blank, that filter will not be used and all findings will be
considered. For example, if you leave the Severity filter blank (i.e., nothing is
checked), all severities will be considered.
