---
title: "Navigating the Users & Groups page"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/navigating-the-users-groups-page.html"
content_id: "CYZyt7sS_V20z3~I1o475g"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:34.293853+00:00"
---

# Navigating the Users & Groups page

The **Users & Groups** page provides a comprehensive view of user details, including
roles, status, and group memberships. This allows administrators to quickly review
access permissions and ensure users have the appropriate privileges within Black Duck.

To view the Users and Groups page:

1. Log in to Black Duck SCA.
2. Click [image: Administration icon] → **Users** to view the list of users or → **Groups** to view the
   list of groups.

     
    [image: The Users tab of the Users & Groups page]   

   [image: The Groups tab of the Users & Groups page]

## Understanding the Users & Groups tables

The **Users & Groups** page contains two tabs—**Users** and **Groups**— each
displaying a table providing an overview of users or groups within Black Duck. These
tables help administrators efficiently manage access and permissions in Black Duck.

The **Users** tab table lists all registered users and their key attributes, including:

- **Username**: The unique identifier for the user.
- **First Name** / **Last Name**: The user's full name.
- **Email**: The email address associated with the account.
- **Global Roles**: Displays the user's global roles. Project-level roles are
  not shown in this column.
- **Status**: Indicates if the user accounts is active or inactive.

The **Groups** tab table displays all user groups and their details, including:

- **Group Name**: The name of the user group.
- **Source**: Indicates where the group originates from:

  - **Local**: A group manually created within Black Duck.
  - **External**: A group synchronized from an external authentication provider (LDAP or
    SAML).
- **Status**: Indicates if the user group is active or inactive.

## Managing users and groups

The **Users & Groups** page allows administrators to manage individual users and user
groups directly from their respective tabs.

In the **Users** tab, you can click the username or the [image: Options button] button to manage the following:

- **User Details**: View and edit the
  user's full profile, including email, status, and authentication source. You
  can also inactivate a user from
  here.
- **Global Roles**: Review and modify the user's assigned global roles (project-level roles
  are not displayed here).
- **Project Groups**: The Projects Groups page lists the project groups to which this user
  belongs. In this section, you can select a group name to view the *Group
  Name* page from which you can manage group information, group
  roles, and group membership by adding or removing this user from one or more groups.
- **Project**: View a list of projects where the user has assigned roles.
- **User Groups**: The User Groups page lists the user groups to which this user belongs.
  In this section, you can select a group name to view the *Group Name*
  page from which you can manage
  group information, group roles
  and group
  membership.

  Users can view the
  user groups that they belong to by using the Profile page.

In the **Groups** tab, administrators can view and manage groups, including:

- **Edit group**: Click the group name to view and edit the project group details, associated roles, related projects and groups, and group
  membership by adding or removing users.
- **Delete group**: Delete the desired user group.

## Exporting to CSV

You can export the list of users or groups to CSV which converts the individual rows to
tabular data. To do so, click either the **Users** or **Groups** tab on the
top right, click the [image: Export CSV button] button, and select CSV.
