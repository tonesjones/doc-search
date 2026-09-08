---
title: "Issue Tracker Two-way Sync"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/issue-tracker-two-way-sync.html"
content_id: "MhCFMxIneiMYmbnFuAMZUw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:18.496769+00:00"
content_hash: "13b067d8e7b321eae5192ecaa8d00a4bdd262020a1413a91c5c070d23b3f38c6"
---

# Issue Tracker Two-way Sync

Software Risk Manager can be configured to automatically update issue or work item fields
in response to any changes to a finding within Software Risk Manager. This is
configurable on the "SRM -> *" tab.

Each field listed on the "SRM -> *" tab will have a "Keep synced" checkbox located to the
right of the field's title. Enable this option to have Software Risk Manager push
updates to editable fields for issues when the issue or work item's associated Software
Risk Manager finding has changed. The values pushed to the issue tracker will be based
on the branch associated with the issue at the time of creation. Currently, issues
created via *Auto Create* can only be associated with a project's default
branch.

[image: image]

Software Risk Manager can also be configured to watch specific issue or work item fields
and update associated findings accordingly. This is configurable on the "* -> SRM" tab.
Currently, only single select dropdowns and radio button fields can be mapped to affect
Software Risk Manager finding Triage Status, Severity Override and/or Fix By Date1.
Note that these changes will only take effect on the issue's associated branch; findings on other
branches will be unaffected.

Note: 1. Only the Azure DevOps, GitLab, Jira and ServiceNow issue trackers support mapping
of Software Risk Manager finding Fix By Date.
