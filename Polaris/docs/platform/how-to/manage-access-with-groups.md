---
title: "Manage access with groups"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/manage-access-with-groups.html"
content_id: "MYzZi_m~ecRMsd30nYGZSw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:03.546753+00:00"
content_hash: "e6d95e832a3838e36533a1aaaace8835a4878f2acd8cd720eb5dfa08cbf3811f"
---

# Manage access with groups

Use groups to manage access to your organization's applications and simplify user administration.

## Overview

A group can grant members:

- A global role for Polaris (organization administrator or organization application manager).
- Access to one or more applications, with an application-level role for each (application administrator, application contributor, application member, application observer, or a custom role).

Multiple applications and users can be assigned to each group. Each user or application can be a member of multiple groups.

Group management permissions are tightly controlled.

- Only organization administrators can create groups, add users to groups, and assign organization-level roles to groups.

  Note: Organization administrators can create custom roles. See [Manage permissions with custom roles](manage-permissions-with-custom-roles.md) for more information.
- Organization administrators, organization application managers, application administrators, and other users with permissions to manage application settings can grant groups access to applications, and assign application-level roles to groups.

Note: For more information on roles and permissions, see [Roles and permissions](../reference/roles-and-permissions.md).

### Tutorial: Creating groups in Polaris

Note: Interactive tutorials are updated periodically and may change without notice.

Figure 1. Tutorial: Creating groups. *This interactive tutorial demonstrates how to create and manage groups in Polaris.* [Open in new tab.](https://www.iorad.com/player/2544190/Polaris--Creating-groups)

### Permission overlap

When more than one group grants a user different levels of access to Polaris or an application, the more permissive role is used. For example:

- If one group grants a user a global role, and another group grants them an application-level role, the global role is used.
- If one group grants a user application administrator access to an application, and a different group grants them contributor access to the same application, the application administrator role is used.

Important: Polaris users inherit permissions from group membership, application membership, and the global role assigned to their account (if set). This means you can assign a global role to each user directly and manage application members and application-level roles without groups.

### Manage group membership with your identity provider

When you set up single sign-on (using SAML 2.0), you can synchronize groups in your identity provider (IDP) with Polaris. Once a group is synchronized, it's user membership cannot be modified in Polaris (and can only be modified in your IDP).

Note: See [Set up single sign-on (with SAML 2.0)](set-up-single-sign-on-with-saml-2-0.md) and Manage Polaris groups through your identity provider for more information.

### Audit logs

Events appear on the Audit Logs page when:

- A group is created, updated, or deleted.
- Users are added to or removed from a group.
- Applications are added to or removed from a group.

## Create a group

To create a group, follow these steps:

Note: Only organization administrators can create groups.

1. Go to My Organization > Groups.
2. Select Add Group.
3. Enter a name in the Group Name field.

   Note: The names of groups you create in Polaris must be unique, 3-255 characters long, and can include spaces. Polaris converts all uppercase characters you enter in a group name to lowercase automatically.
4. (Optional) Assign a global role (Organization Administrator or Application Manager) to the group.
5. Select Save.
6. (Optional) Give the group access to applications:
   1. Select the applications group members can access using the Select applications dropdown menu.
   2. Select Add.
   3. Select the application-level role group members will have when they access each application using dropdown menus in the Group's Role in Application column.
7. (Optional) Add users to the group:
   1. Open the Users tab.
   2. Select group members with the Select users dropdown menu and then select Add.

## Edit a group

To modify a group (including changing a group's name, access to applications, or user membership), follow these steps:

Note: Only organization administrators can edit groups.

1. Go to My Organization > Groups.
2. Select a group to modify.
3. If necessary, modify the group's access to applications, or membership.

   Note: If a group is synchronized with your IDP, you cannot change its user membership in Polaris.
4. To change the group's name or global role:
   1. Select Edit.
   2. Change the group's name or global role.

      Note: If a group is synchronized with your IDP, you cannot change its name in Polaris.
   3. Select Save.

## Delete a group

To delete a group, follow these steps:

Note: Only organization administrators can delete groups.

1. Go to My Organization > Groups.
2. Select Delete next to the group you wish to delete.

   Note: If a group is synchronized with your IDP, you cannot delete it until:
   - You revoke the group's access to Polaris in your IDP, or
   - You remove all users with access to Polaris from the group in your IDP
3. Select CONFIRM DELETE.

## Find the groups you belong to

Find a list of groups you belong to on the Account tab of the User Profile page. To open the account page, select Account [image: icon account] > Account.

A list of groups you belong to appears under Group Membership.

## Add multiple groups to an application

After you open an application's Members page (Portfolio > select an application > Settings > Members), you can grant multiple groups access to the application.

Note: Organization administrators, organization application managers, and application administrators can add new groups to an application. For more information, see Add users and groups to an application.
