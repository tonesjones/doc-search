---
title: "Issue Tracker Integration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/issue-tracker-integration.html"
content_id: "jC0fmjEk9asye5j4yCMdRg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:09.798491+00:00"
content_hash: "c9a175904d205528fc78cee5eeb63b7ed48ff080de19eb4136fc7d6a0000eb36"
---

# Issue Tracker Integration

If a project has an Issue Tracker Configuration, the *Issue
Tracker* dropdown menu will be available, allowing users with the
`update`
role to interact with the configured issue
tracker. Software Risk Manager currently supports Jira, Azure DevOps, ServiceNow, GitHub and
GitLab. For Jira, GitHub and GitLab users, the options are create issue, associate with existing
issue, and remove association. For Azure DevOps users, the options are create work item,
associate with existing work item, and remove association. For ServiceNow users, the
options are create incident, associate with existing incident, and remove association.
The examples below assume Jira is the currently configured issue tracker.

## Creating New Issues

To create a new issue for a Finding based on your current branch view, click the *Jira*
dropdown menu and select the *Create issue...* option.

[image: image]

A dialog will open.

[image: image]

All of the fields are editable. Required fields will have a red asterisk by their
name.

Use the template expressions that were defined when configuring the issue tracker to
pre-populate the relevant fields with data from the active findings. Note that these
pre-populated values will be based on the current branch view where the issue is
created. Software Risk Manager provides default templates for the *Summary* and
*Description* fields.

The *Description* field will be pre-populated with a brief description for each
Finding. Jira descriptions can be set to allow for the use of [WikiMarkup](https://en.wikipedia.org/wiki/Help:Wiki_markup). Software Risk Manager takes advantage of
that to make the descriptions more readable from within Jira.

## Creating Associations with Existing Issues

For Jira users, associate a finding with an existing issue by clicking the *Jira* dropdown
menu and selecting the *Use existing issue* option. For Azure DevOps users,
associate a finding with an existing work item by clicking the *Azure DevOps*
dropdown menu and selecting the *Use existing work item* option. For
ServiceNow users, associate a finding with an existing incident by clicking the
*ServiceNow* dropdown menu and selecting the *Use existing incident* option. For GitLab users, associate a finding with an existing issue by
clicking the *GitLab* dropdown menu and selecting the *Use existing
issue* option. For GitHub users, associate a finding with an existing issue by
clicking the *GitHub* dropdown menu and selecting the *Use existing
issue* option.

Enter the issue key, work item, or incident number that you want to associate with
the finding(s). Clicking outside the textbox or pressing *Enter*will cause
Software Risk Manager to look up the issue, work item, or incident in question. If
SRM is able to find it, and if it's part of the same Jira, Azure DevOps, ServiceNow,
GitHub, or GitLab project you selected when you configured the issue tracker for this
project, or if the same ServiceNow instance configured for this Software Risk
Manager project, the issue or work item summary will be displayed, allowing you to
confirm that you've entered the issue or work item you want. Click OK to associate
the finding (or findings) with that issue or work item.

## Refreshing Issue Status

Software Risk Manager will regularly check the Issue Tracker server to refresh the status for all
of the issues, work items, or incidents associated with findings in a given project.
The interval at which the check is done is configurable in the Issue tracker
configuration. However, you can also manually trigger a refresh of all the issues,
work items, or incidents on the Findings page by clicking the *Refresh Issues*,
*Refresh Work Items*, or *Refresh Incidents* button.

## Removing Associations with Existing Issues

You can remove the issue, work item, or incident associations for all of the findings in the
current filter by using the *Jira*, *Azure DevOps*, *ServiceNow*, *GitHub*
or *GitLab* dropdown menu and selecting the *Remove association* option.
Note this only removes the association in Software Risk Manager; it doesn't change
the issue, work item, incident in the Issue Tracker.
