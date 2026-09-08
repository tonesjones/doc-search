---
title: "Issue Tracker"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/issue-tracker.html"
content_id: "TURY1i4xP61daZ7N_i6iXQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:28.160252+00:00"
content_hash: "c5b690ddbdcdccf357636c47e981e2312cc88b61809f97c4c4bbc5d801714b8e"
---

# Issue Tracker

If a project has an Issue Tracker Configuration, the *Create issue* and *Use existing
issue* buttons will be shown for Jira, GitHub and GitLab users, *Create work item*
and *Use existing work item* for Azure DevOps users, and *Create incident* and
*Use existing incident* for ServiceNow users. Users with the
`update`
role are allowed to interact with the
configured issue tracker.

## Creating an Issue

You can click the *Create issue*, *Create work item*, or *Create incident* button,
which will open a dialog.

[image: image]

The dialog functions the same way as the dialog opened from the Bulk Operations area
of the *Findings Table*, except the *Description* field will be
pre-populated with information about this finding. When manually creating an issue
in this way, the issue will be associated with the current branch view and will
reference that finding's branch-specific data (e.g., *Severity* and
*Status*).

Note: In contrast to manual issue creation, *Auto Create* currently only
supports associating issues with a project's default branch.

## Associating a Finding with an Existing Issue

Click the *Use existing Issue*, *Use existing work item*, or *Use exiting
incident* button to associate this finding with an existing issue, work item,
or incident. A dialog will open.

[image: image]

## Refreshing Issue Status

Select the refresh icon to manually trigger a refresh of the issue or work item.

## Removing Associations

Clicking the trash icon removes the association between the finding and its related issue or work
item. Note: This only removes the association; it doesn't touch the issue or work
item itself.
