---
title: "Alert Users and Roles"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-users-and-roles.html"
content_id: "IlITWQh8yDw_BJYD559A6Q"
version: "8.4.0"
section: "User and Role Management"
scraped_at: "2026-08-08T23:46:43.645644+00:00"
---

# Alert Users and Roles

This page describes users and roles in Black Duck Alert. For information on creating
users and groups see the User
Management page

## Alert Users

Alert users include default users, users added by an administrator, and users managed
by external systems such as `LDAP` or `SAML`.

There are three default users in Alert:

`sysadmin` - full system configuration access.

`jobmanager` - full access to distribution jobs and read permissions
for other operational functions.

`alertuser` - read access for distribution jobs only.

Only an administrator can manage and assign roles to users that are managed by
external systems such as LDAP or SAML.

## Alert Roles

By default, the following user roles are defined in Alert and their use is
recommended. You can create additional custom roles within the UI however care must
be taken to ensure you assign sufficient permisisons on the roles to accomplish the
desired tasks.

| Role Name | Description | Notes |
| --- | --- | --- |
| ALERT_ADMIN | Provides full user privileges, and full access to Alert's configuration. The system administrator (sysadmin) default user has this role. | This role cannot be changed. |
| ALERT_JOB_MANAGER | Allows a user to read the provider and channel global configuration, and to test the configuration. This user has full access to distribution jobs and read access to the Audit page and Scheduling page. | The user has read-only access to scheduling. The user cannot view or change the system settings as these are removed from their navigation panel on the left side of Alert. |
| ALERT_USER | Read-only access to distribution jobs to view configuration. | The user cannot view or read data for providers, the global channel settings, scheduling, or system settings. These items are removed from the left side navigation panel. |

## Managing roles

On the Roles tab of the **User Management** screen, you can create, edit, or
delete roles, and manage the permissions for those roles.

Click **User Management** > **Roles** to open the Roles screen.

### Adding a new role:

1. Click **+ Create Role**. [image: "Create Role"]
2. Type a name for the new role in the **Role Name**
   field. [image: "Role Name"]
3. Select a value from the dropdown menu in the **Descriptor Name**
   field. [image: "Role Descriptor"]
4. Select a value of either Global, or Distribution for the context in the
   **Context** field. [image: "Role Context"]
5. Select any permission checkboxes for permissions that you want to
   associate with this role. [image: "Role Configuration"]
6. Click **+ Add Permission** to add the permission to the
   role. [image: "Role Permissions"]
7. Click **Save** to save this role.

Tip: The `Execute` permission allows a user to test
configurations by selecting a test button that is only available to users
assigned a role associated with this permission.

### Copying an existing role

1. Click the **Copy** icon in the same row for the user role that you
   want to copy.
2. In the Role Name field on the Role screen, you can change the role name
   and click Save to create a new role with the same permissions.
3. Use the Add, Remove, or Edit functions to change permissions for your new
   role.

### Adding or removing permissions for an existing role

1. Click the Edit icon or double-click the row that corresponds with the
   role name.
2. On the Role screen, click **+ Add** to add new role
   permissions.
3. To edit a Descriptor, double-click the row or click the **Edit** icon
   to open the role permissions.
4. To remove a role Descriptor, for example, Black Duck, select the row and
   click **Remove**.
5. Click **Save** to save your changes.

### About permissions

- All **Descriptors** can be assigned a GLOBAL Context.
- For all Channel (`Slack`, `MS Teams`,
  `Email`, `Jira Server`, `Jira
  Cloud`, `Azure Boards`) combinations where
  **Context** equals *DISTRIBUTION*, you must also add a
  **Descriptor** for Black Duck and a Context set to
  *DISTRIBUTION*.

Note: All other non-channel **Descriptor** combinations with
**Context** set to *DISTRIBUTION* are not valid combinations,
such as Authentication, Settings, or User Management with
*DISTRIBUTION*.

### Deleting an existing role

1. Select the checkbox for the role that you want to delete.
2. Click the **Delete** button and follow prompts to delete the selected
   role.

## LDAP Groups and Roles

If you configure `LDAP` you can assign additional roles.

Your LDAP server administrator needs to create the following groups and assign them
to user accounts

| Role Name | Description |
| --- | --- |
| ROLE_ALERT_ADMIN | Users assigned to this group have the ALERT_ADMIN role. |
| ROLE_ALERT_JOB_MANAGER | Users assigned to this group have the ALERT_JOB_MANAGER role. |
| ROLE_ALERT_USER | Users assigned to this group have the ALERT_USER role |

Note: LDAP and SAML users that login into Alert have the ALERT_USER role
assigned to them on first login, by default.

## SAML Groups and Roles

If you configure `SAML` you can assign additional roles.

For SAML, you must add an attribute to your application to define the roles.
Therefore, you might need to create a different application per role to restrict
access to Alert.

For example, an Alert Administrators application is created that sets the
`AlertRoles` attribute with the ROLE_ALERT_ADMIN as the
value.

The administrator:

1. Sets an application attribute called `AlertRoles`
2. Assigns `ROLE_ALERT_ADMIN`,
   `ROLE_ALERT_JOB_MANAGER`, or
   `ROLE_ALERT_USER` to the attribute to define the
   appropriate roles for the application. For each role, the administrator
   should create a separate application with the `AlertRoles`
   attribute set with the corresponding role.
3. Assigns the application to the users requiring that level of access to
   Alert.

Tip: It is recommended that only Alert administrators have the attribute
for the `ALERT_ADMIN` role set. All other users should have their
roles managed on the Alert User Management page.

## Alert Error Messaging

The following denote error messages that relate to authentication, which might be
displayed in response to user actions:

| Error | Description |
| --- | --- |
| *You are not permitted to view this information.* | The user does not have read access to the data. |
| *You are not permitted to perform this action* | The user does not have permission to create, delete, or execute depending on the attempted action in the user interface. |
| *User not authorized to perform the request* | Pertains to the Global channel configurations such as Email, Jira Cloud, Jira Server, if the user does not have permission to save, delete, or test a configuration. |
