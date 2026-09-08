---
title: "Automatic Status Updating"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/automatic-status-updating.html"
content_id: "sey2skbI0QWq6NUj_jkLyg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:19.090435+00:00"
content_hash: "e3dd49d2ea5443243249d3097d2d41c9f9c8dcfdbe4f2717c2ce0a3672823984"
---

# Automatic Status Updating

Note: This section is only applicable to Software Risk Manager users who are configuring
a Jira integration.

Software Risk Manager can be configured to automatically update Jira issue statuses in
response to status changes within Software Risk Manager. This is configurable on the
"Status Mapping" tab.

Click the Projects icon in the navigation bar to open the Projects page, then select
Issue Tracker Config from the project's dropdown configuration options.

When automatic status updating is enabled, a list of Software Risk Manager triage
statuses will be shown, along with a dropdown list to pick the associated Jira status.
These mappings are optional: if one is not selected, then no action will be taken on
findings with that status.

After configuring status mappings, any time the status of a finding on the issue's
associated branch is updated, the associated Jira issue will be updated according to the
mapping (if applicable). If a transition is not available, then no action will be taken.
If a transition requires some input for a field, Software Risk Manager will attempt to
use any defined mappings in the "SRM -> Jira" tab that are marked "Keep synced" to
satisfy those requirements. If multiple findings are associated with the same Jira
issue, the Jira status will only be updated if all findings map to the same status.

When Software Risk Manager triggers a status transition with the "Include comments and
keep synced" option enabled in the Issue Tracker Configuration modal, the closing comment
is included as part of the transition request. The same applies when the transition
itself requires a comment field. The default comment text is
*"This ticket was closed by SRM since the associated finding(s) were
resolved"*. This text can be customized by setting the
`codedx.issuetracker.closing.comment` property in
`codedx.props`. See Issue Tracker
Configuration for details.
