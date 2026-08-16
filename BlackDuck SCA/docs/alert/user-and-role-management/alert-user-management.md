---
title: "Alert User Management"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-user-management.html"
content_id: "LPvF835USZJpskiZtSNZ8Q"
version: "8.4.0"
section: "User and Role Management"
scraped_at: "2026-08-08T23:46:44.468546+00:00"
---

# Alert User Management

You manage users and user roles on the User Management page. You can change the username
and details for a user, specifically, you can change the user name for the Alert
administrator.

In addition to the default `sysadmin` user, there are two other default
users in Alert, which are the `jobmanager` and
`alertuser`.

- The `jobmanager` user has the `JOB_MANAGER` user role.
- The `alertuser` user has the `ALERT_USER` user role.

These default users are configured with the default password of `blackduck`. You cannot delete these user accounts.

You should change the default password for each user when Alert is first started. These
can be changed in the User Management screen.

Note: Alert admins can manage permissions for the jobs that users can create
or edit but they can't control which Black Duck SCA projects users can see and configure
in Alert.

## User Management Tasks Overview

Manage users and roles using the User Management page:

- To create new users, delete users, or edit users, click **User Management** on the left navigation pane and select the **Users**
  tab.
- To create, edit, or delete user roles, and manage the permissions for those
  roles, click **User Management** on the left navigation pane and select
  the **Roles** tab.

> For further information on Roles and Permissions see User and Role
> Management.

Tip: When you disable **Enable Auto-Refresh** on the **User
Management** screen a **Refresh** button appears, which enables you to
refresh the display.

Figure 1. User Management
[image: User management page]

## Managing users

To create, edit, or delete users, click **User Management** on the left navigation
pane and select the **Users** tab.

- To create a new user, click **+ New**, populate the fields and save.
- To delete a user, select the checkbox that represents the user and then click
  the **Delete** button.
- To edit a user, double-click the row for the user, or click the edit icon.

Note: You cannot delete the default user accounts.

### Copying a user or role attributes to create a new user or role

Both user names and role names must be unique, but you have the option of
creating new users and roles based on existing ones.

The table for users and the table for roles include an additional column
containing a copy button, located at the far right of each user, and role. This
enables you to copy the configuration of an existing user or role. By using the
copy functionality, you can easily configure multiple users or roles where only
a small number of fields differ between each one. Clicking the copy icon
displays the **User** or **Role** dialog box.
