---
title: "Managing User Groups"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/managing-user-groups.html"
content_id: "e_GLdAlWgSj3zTolo8VhuA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:55.412370+00:00"
content_hash: "e54121513a0f3ecb4f0ca7ef861a2a28cd998719b2375f1cb64aad5d133c500a"
---

# Managing User Groups

To simplify user administration, users can be managed as groups. Roles and permissions
assigned to a group will apply to every member of that group. Admins can set up multiple
groups with multiple permissions, including nested groups.

Click the Settings icon in the navigation bar and select User Groups from the left menu
to open the User Groups page.

[image: image]

The User Groups page shows a list of existing groups and the number of members in each.
Clicking the column headers will re-sort the list.

For more information on managing user groups, see the following topics.

- Viewing existing user groups
- Creating a user group
- Configuring user group roles
- Editing user group settings
- Deleting a user group

## Viewing Existing User Groups

**To view a list of existing user groups:**

1. Click the Settings icon in the navigation bar and select User Groups from
   the left menu.

   [image: image]

   This page shows a list of existing groups and the number of members
   in each.
2. Use the filter field to search for a specific user group or click the column
   header to re-sort the list.

## Creating a User Group

In addition to single groups, groups can be nested ("parent" group).

**To create a user group:**

1. Click the Settings icon in the navigation bar and select User Groups from
   the left menu.

   [image: image]
2. Click Create Group.

   [image: image]
3. Enter a group name and select group members from the list.
4. (Optional) Select a "Parent Group" to create a nested group.
5. Click Save.

## Configuring User Group Roles

Assigning roles to a group will apply those roles to every member of that group.
However, roles assigned to members in the group will not replace or overwrite the
roles assigned individually to a user.

**To configure group roles:**

1. Click the Settings icon in the navigation bar and select User Groups from
   the left menu.

   [image: image]
2. Click the dropdown configuration icon and select Configure Roles.

   [image: image]

   This opens the Configure Roles window.

   [image: image]
3. Make the necessary configuration changes.
4. Click Done.

## Editing User Group Settings

Editing group settings includes changing the group name, reassigning the parent
group, and adding or removing users.

**To edit group settings:**

1. Click the Settings icon in the navigation bar and select User Groups from
   the left menu.

   [image: image]
2. Click the dropdown configuration icon and select Edit Group Settings.

   [image: image]

   This opens the Edit User Group window.

   [image: image]
3. Make the necessary changes.

   Use the filter field to search for individual
   users or click the column headers to re-sort the list.
4. Click Save.

## Deleting a User Group

Deleting a user group will not delete individual users or remove any roles previously
assigned to a user individually

**To delete a user group:**

1. Click the Settings icon in the navigation bar and select User Groups from
   the left menu.

   [image: image]
2. Click the dropdown configuration icon and select Delete Group.

   [image: image]

   This opens the Confirm Delete window.

   [image: image]
3. Click Delete to confirm.

## Configuring LDAP for User Groups

Note: To take advantage of LDAP with User Groups, there must be a valid LDAP
configuration in the Software Risk Manager properties file. For more information,
see the *SRM
Install Guide*.

This feature may be presented when LDAP is configured but is only compatible with
providers that create a user attribute containing group membership for SRM to check,
such as Active Directory.

To manage mapping of LDAP groups to SRM user groups, pick the LDAP Config option from
the group's config menu.

[image: image]

From here, you can enter a comma-separated list of LDAP group names.

[image: image]

The names for your LDAP groups are pulled from the DN path attribute specified in the
SRM properties file. For more information, see LDAP group mapping in the *SRM Install Guide.*

When an LDAP user signs in, their LDAP groups will be checked against your mappings
configured on this page. The user will be added to the SRM group if they are a
member of any of the listed LDAP groups; otherwise, they will be removed.

If users are added or removed from an LDAP group, their membership will not be
updated until they sign out and back in. You can force a manual refresh of all
group's LDAP members by clicking the "Refresh" button on this page.

Note: If the LDAP Group Names textbox is empty, a membership refresh will have no effect
on that group.
