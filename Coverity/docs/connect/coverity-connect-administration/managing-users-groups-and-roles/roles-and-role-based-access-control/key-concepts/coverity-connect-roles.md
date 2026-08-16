---
title: "Coverity Connect roles"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-roles.html"
content_id: "77Hmz35AN8SPhpRz9iowbw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:47.063289+00:00"
---

# Coverity Connect roles

Roles are entities that contain any number of permissions to grant or restrict access to
a specific "type" of Coverity Connect user. For example, an administrator will most
likely only need to access certain parts of Coverity Connect for configuring the system,
while a developer does not need to access system configuration screens, but does need to
view and triage issues.

Note: The System Report Generator is a specialized role that is
specifically assigned to a unique type of user in Coverity Connect, the
reporter user. The reporter is a
process (rather than a person) that is automatically created by Coverity Connect. For
details about the role of this user, see Built-in users.

Roles can be assigned to both users and groups. For more information, see Understanding how Coverity Connect applies roles.

Coverity Connect has the following types of roles:

- Built-in roles. For details, see "Managing built-in roles."
- Custom roles. For details, see "Creating new roles."

## Managing built-in roles

Built-in roles are pre-defined roles that you cannot edit or delete. You can,
however, copy a built-in role and edit the name and permissions of the copy.

The following table lists the permissions that are assigned for each built-in
role:

Figure 1. Built-in roles
  
 [image: image]

Permissions marked with an asterisk (*****) also belong to the component level.
For more information, see Understanding how Coverity Connect applies roles.

Permissions marked with two asterisks (******) also belong to the component level
and triage store levels. For more information, see Understanding how Coverity Connect applies roles.

Note: As of release 2018.06 the new permission category, Classify Issues, is available
by default to all users. See Stream permissions.

To copy and edit a built-in role:

1. Select the name of the role that you want to copy.
2. Click Duplicate.

   A dialog with the copied role name followed by a number (for example,
   Project Owner 73) appears.
3. Change the name and description of the role, as needed.
4. Select or remove any permissions that you want included or excluded in the
   role.
5. Click Create to finalize your changes and exit the
   dialog.

## Managing custom roles

Custom roles are pre-configured roles that you can edit by adding or removing
permissions to match your requirements. The following table lists the permissions
that are assigned for default roles:

Figure 2. Custom roles
  
 [image: image]

Permissions marked with an asterisk (*****) also belong to the component level.
For more information, see Understanding how Coverity Connect applies roles.

Permissions marked with two asterisks (******) also belong to the component level
and triage store levels. For more information, see Understanding how Coverity Connect applies roles.

To edit a custom role:

1. Select the name of the role.
2. In Role Details, click
   Edit.
3. Change the name or description of the role, if desired. Select or remove any
   permissions that you want included or excluded from the role.
4. Click OK to finalize your changes and exit the
   dialog.

## Creating new roles

Coverity Connect allows you to create your own, custom sets of access permissions for
specific types of users or groups in your organization. In general, you need to
create a new role if one or more of the built-in or default roles does not apply the
permissions you need for a given user or group.

Note: You cannot assign administrative privilege to another user unless you yourself
have an administrative privilege such as Manage users and
groups or Manage role definitions.

To create a new role:

1. Click Add.

   A dialog appears with the Name set to New Role
   followed by a number (for example, New Role 47).
2. Change the name and description of the role.
3. Select any of the permissions that you want included in the role.
4. Click Create to finalize your changes and exit the
   screen.

   You can now apply the role to users and groups.

Note: **Deleting roles**

To delete one or more roles, select the
name of each role to delete, and click Delete. In the
confirmation dialog, click Delete again.
