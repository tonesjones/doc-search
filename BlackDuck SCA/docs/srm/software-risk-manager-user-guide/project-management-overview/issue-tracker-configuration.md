---
title: "Issue Tracker Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/issue-tracker-configuration.html"
content_id: "OqGrWlZowqxUCjWTVLChkg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:14.615922+00:00"
content_hash: "2c9210ad5de2012cee9fb01bdde03890507d94b1b151d5844de09d4d49b0d923"
---

# Issue Tracker Configuration

Software Risk Manager allows you to associate findings with issues or work items in an
issue tracker, either by creating a new issue or work item, or by identifying an
existing issue or work item.

Software Risk Manager currently supports the following issue trackers:

- Azure DevOps (requires "Read" permission for "Graph" and "Project & Team"
  scopes, and "Read, Write, Manage" permissions for "Work Items" scope)
- GitLab (requires "api" access token scope)
- Jira (requires "Browse projects" project permission, "issue-level security"
  permission if issue-level security is configured, and the "read:jira-work" OAuth
  scope if using OAuth)
- ServiceNow (requires admin role or custom ACL rules granting access to the
  following ServiceNow tables - `incident`, `sys_user`,
  `sys_user_group`, `sys_choice` and
  `sys_dictionary`)
- GitHub and GitHub Enterprise (requires "repo" access token scope)

## Configuring an Issue Tracker

**To configure an Issue Tracker for a project:**

1. Click the Projects icon in the navigation bar to open the Projects
   page.
2. Click the project's dropdown configuration icon and select Issue Tracker
   Config.

   [image: image]
3. Enter the URL for your Issue Tracker server (including the "http://" or
   "https://"—even if you're using an IP address) as well as the credentials
   required for the user in whose name the issues or work items will be
   created.
4. Click Verify.

   Software Risk Manager will connect with the server and
   retrieve a list of projects the user can access.
5. Select the project you want to use from the dropdown menu.

   Software Risk Manager
   will periodically query the issue tracker server to refresh the status
   for all of the issues or work items associated with a given project. The
   Refresh Interval specifies the number of minutes between refreshes (the
   default is 60 minutes).
6. Click OK to save your configuration.

   If you delete the issue tracker
   configuration for a given project, all of the issue or work item
   associations tied to the findings in that project will be deleted.
   However, none of the issues or work items on the issue tracker server
   itself will be affected.

## Additional Configuration Options

To perform additional configuration options, see the following sections:

- Advanced Field
  Configuration
- Issue Tracker Two-Way
  Sync
- Automatic Status
  Updating
- Automatic Issue Creation
