---
title: "Issue Tracker Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/issue-tracker-configuration.html"
content_id: "HJNseBGBel~9hkSaNJJIUg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:34.853175+00:00"
content_hash: "5303266f0e5c0d7c14db0a53e071a2d1949ff65b6d1ded770688ef949f863642"
---

# Issue Tracker Configuration

To support issue tracker integrations, Software Risk Manager will make requests to the
issue tracker server periodically in order to create, update, and read issues. Due to
the volume of requests that can be made in quick succession, issue tracker servers may
begin to deny requests to prevent the server from being overloaded.

The following properties will affect how Software Risk Manager makes requests.

- `azure.auto-create-delay` [default: 50] - sets the delay (in ms)
  between subsequent work item creation requests made during an auto create
  job.
- `gitlab.auto-create-delay` [default: 60] - sets the delay (in ms)
  between subsequent requests made during auto create jobs and bulk update
  jobs.
- `jira.auto-create-delay` [default: 50 - sets the delay (in ms)
  between subsequent issue creation requests made during an auto create
  job.
- `servicenow.request-delay` [default: 750] - sets the delay (in ms)
  between subsequent requests made during auto create jobs and bulk update
  jobs.

It is also possible to configure result and finding level data that SRM includes
when querying issue tracker data and in the issue tracker sync process.

The following properties will affect what data Software Risk Manager includes when querying
issue tracker data.

- `issuetracker.include-archived-results` [default: true] - if false,
  result data will not include archived results.
- `issuetracker.include-gone-in-active-findings-group` [default: true] -
  if false, result data will not include Gone findings if an active version of the
  same finding also exists. If all findings in a group linked to an issue are Gone
  however, the group will be considered Gone and all the Gone findings included. This
  property only ignores Gone findings when *at least one* non-Gone finding is
  present in the group.
- `issuetracker.skip-issue-update-for-gone-findings` [default: false] -
  if true, SRM -> issue tracker updates will be skipped for Gone findings
  *when the associated issue is already closed/done*. If the issue is still open,
  SRM will still push the update needed to close it. This is useful for workflows
  where closed/done issues cannot be edited.
- `issuetracker.closed-issue-status-names` [default: ""] - comma-separated
  list of additional issue status names to treat as closed/done (case-insensitive),
  checked in addition to the built-in "done", "closed", and "resolved" fallbacks.
- `codedx.issuetracker.comment.enabled` [default: false] - if true,
  enables comment sync for all projects by default. When false, comment sync must
  be enabled on a per-project basis from the Issue Tracker Configuration modal in the UI.
- `codedx.issuetracker.closing.comment` [default: "This ticket was
  closed by SRM since the associated finding(s) were resolved"] - the comment
  posted to the issue tracker ticket when Software Risk Manager triggers a status
  transition (for example, when associated findings are resolved or marked as
  Gone). This value can be overridden per deployment to match your
  organization's preferred language.
