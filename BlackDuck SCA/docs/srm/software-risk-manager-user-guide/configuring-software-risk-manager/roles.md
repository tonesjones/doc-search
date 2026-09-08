---
title: "Roles"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/roles.html"
content_id: "XSNeBk2NqXczktZmfWztdA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:04.353817+00:00"
content_hash: "d8912894b1a3209ded812842fd7939d0e131a14dc8969750260f4306aa7714e1"
---

# Roles

Roles enable users to interact with SRM in ways permitted by the set of permissions
included in their definition. Role definitions can be viewed, edited, and created on the
Roles page.

Click the Settings icon in the navigation bar and select Roles from the left menu to open the
Roles page.

[image: image]

This page displays both Global Roles and Project Roles. SRM comes preconfigured with a
collection of built-in roles, each of which is denoted by a padlock symbol next to its
name.

Built-in roles can only be viewed, while all other roles can be edited, deleted, and
replaced. Only custom project roles can be created.

## View Role

A built-in role's name and its set of associated permissions can be viewed on the
Roles page.

**To view a role's definition:**

1. Click the Settings icon in the navigation bar and select Roles from the left
   menu.
2. Open the context menu for the role and select the View Role option.

   [image: image]

   This opens the View Role window.

   [image: image]
3. Review the role's name and its set of associated permissions.
4. Click Done.

## Edit Role

A custom project role's name and its associated set of permissions can be edited on
the Roles page.

**To edit a custom project role's definition:**

1. Click the Settings icon in the navigation bar and select Roles from the left
   menu.
2. Open the context menu for the role and select the Edit Role option.

   [image: image]

   This opens the 'Edit Role' window.

   [image: image]
3. Review the role's name and set of associated permissions and make changes as
   necessary.

   Note: Role names are unique. An error will be presented in the
   event that a role's name is changed to one that already
   exists.
4. To save the changes made, click Save, otherwise click Cancel to discard
   them.

## Delete Role

Custom project roles can be deleted on the Roles page.

**To delete a custom project role:**

1. Click the Settings icon in the navigation bar and select Roles from the left
   menu.
2. Open the context menu for the role and select the Delete Role option.

   [image: image]

   This opens the Delete Role window.

   [image: image]
3. If the role to be deleted has been assigned to users or user groups, a
   replacement can be selected by checking the "Reassign all..." checkbox and
   then selecting a replacement role.

   [image: image]
4. To delete the role, click Delete, otherwise click Cancel.

## Replace Role Assignments

On the Roles page, users and user groups who have been assigned a role can have their
assignment replaced with a different role.

**To reassign users and user groups who have been assigned a role with a different role:**

1. Click the Settings icon in the navigation bar and select Roles from the left
   menu.
2. Open the context menu for the role and select the "Reassign Users and User
   Groups to Another Role."

   Note: The "Reassign Users and User Groups to
   Another Role" context menu option will be disabled if the role is not
   assigned to an users or user groups.

   [image: image]

   This opens the Replace Role window.

   [image: image]
3. Select a replacement role.
4. To reassign users and user groups to the selected replacement role, click
   Replace, otherwise click Cancel.

## Create Custom Project Roles

Custom project roles can be created on the Roles page.

**To create a custom project role:**

1. Click the Settings icon in the navigation bar and select Roles from the left
   menu.
2. Click on the New Custom Role button in the Project Roles section of the
   Roles page and choose to base the new role on an existing one or to build
   the new role from scratch.

   [image: image]

   This opens the New Custom Role window.

   [image: image]
3. Name the custom role and select any number of permissions.

   Note: Role names
   are unique. An error will be presented in the event that a role is
   attempted to be created with a name that already exists.
4. To create the new custom role, click Save, otherwise click Cancel.

For more information on how to assign roles, see the following topics:

- Configuring a User
  Profile
- Configuring User
  Group Roles
