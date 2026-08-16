---
title: "Understanding how Coverity Connect applies roles"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/understanding-how-coverity-connect-applies-roles.html"
content_id: "T45nvgQfXMEs3LSE34a6Bw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:48.297076+00:00"
---

# Understanding how Coverity Connect applies roles

Coverity Connect allows you, as an administrator, to assign roles to specific users or
groups at a number of different levels. Role assignments at a more specific level
override role assignments at a more general level. This allows role assignments at a
specific level to grant a user (or group) additional permissions OR to remove
permissions within that level. The Coverity Connect RBAC implementation provides the
following levels:

- Global roles grant permissions to users throughout
  Coverity Connect, except when they are overridden by role assignments on a
  triage store, component, project or stream.
- Triage store roles grant permissions to users within the
  confines of a given triage store.
- Component roles grant permissions to users within the
  confines of a given component map.
- Project roles grant permissions to users within the
  confines of a given project, except when they are overridden by role assignments
  on a stream.
- Stream roles grant permissions to users within the
  confines of a given stream.
- Component map roles grant permissions to users within the
  confines of a given component map.

Some of the levels combine to form hierarchies by which Coverity Connect determines
access roles, as illustrated in the following diagram:

Figure 1. RBAC role hierarchy within Coverity Connect
  
 [image: image]

Coverity Connect enforces RBAC permissions by determining an "effective" role for the
user or group that is trying to perform some action. This effective role, in turn,
allows Coverity Connect to decide if the action is permitted or not.

Effective role
:   To determine the effective role, Coverity Connect examines the most specific
    level for the action that is being attempted. For example, if a user is
    attempting to triage an issue on a specific stream, Coverity Connect
    determines access rights by examining the role assignments on that stream.
    If Coverity Connect identifies one or more role at that level, it stops the
    evaluation at that level and does not continue to evaluate role definitions
    at "higher" levels. This is because the role permissions at the more
    specific level hide (or, override) any role permissions that exist at more
    general levels.

    Coverity Connect examines roles defined at a higher level only when the more
    specific level does not have any roles assigned to it. Therefore, a role
    assigned to a user or group at the global level can be overridden by
    assigning a role at a more specific level.

    When Coverity Connect finds a role at a given level, it gathers all role
    definitions at that level and combines them to form the effective role. The
    effective role contains all of the permissions that are assigned to the user
    at that level, so the user can use any permission defined in any role at
    that level. Furthermore, a user's role can vary depending on context. For
    example, a user could be assigned the Developer role on one stream, and the
    Observer role on another stream.

As an example of how Coverity Connect determines role access, consider the following:

- user1 has a global Developer role.
- user1 also has the No Access role assigned at the project
  level for projectA.

In this configuration, user1 has permission to view and triage issue
anywhere on the system, except for in projectA, which
user1 cannot see at all.

As an additional example:

- user2 has a global Visitor role.
- user2 has the Developer role defined at the project level
  for projectB.
- user2 has a role with the view issues
  permission to view issues, and the triage issues
  permission at the component and triage store level to triage issues.

In this configuration, user2 can log into the system, but can only
view and triage issues on projectB.

## Permissions for triaging issues

Most actions for which a user is allowed or denied permission take affect on a single
object. Because of this, these permissions take place in a single hierarchy. A few
common operations, however, require multiple objects and are therefore controlled by
permission settings of multiple hierarchies at one time.

One very common and important example of this is applying issue triage permissions.
This involves role settings at the triage store, component, and stream levels. The
user must be authorized at all three levels in order for the action to succeed. All
three effective roles must grant at least the Triage issues
permission in order for the triage action to be allowed. For an example, see Scenario: Granting triage permissions on a synchronized Coverity Connect enterprise cluster

The View issues permission is available for definition at the
triage store level, so a user must have this permission at the triage store,
component, and stream levels in order to view issues.

## Triaging workflows and classifying issues

By default all users have the right to triage as well as to classify an issue. If you
want to prevent certain users from being able to dismiss an issue, you can do so by
limiting their ability to classify an issue. You can apply the restriction to groups
of users as defined by their assigned role. In this way triaging may be done in two
steps: when a new issue is detected,

- A junior developer can triage the defect; then depending on the action
  needed
- A senior developer can determine the appropriate action; for example, by
  setting its classification to `False Positive` or
  `Intentional`

You can control which users can do further classification by enabling the **Classify
issues** checkbox when defining the user role.

If a user does not have the **Classify issues** permission, when triaging an issue
using the **Triage** pane, They may still specify the severity of the issue and
the action taken. If the user tries to classify an issue in some other way, for
example, through Web Services, an error is returned.

## Assigning roles to users and groups

All levels of roles can be assigned to users and groups in the Configuration > Users & Groups menu. When you assign a role to a group, all members of the group
possess the permission rules for each role. Assigning roles directly to users and
groups is typically performed by an administrator who must be assigned a role that
contains the Manage users and groups permission.

Roles assigned directly to the user take precedence over those assigned to the user
through group membership. If a user belongs to a group that is assigned a role with
permissions that are different than permissions that are assigned to the user,
Coverity Connect applies the permissions defined for the user and ignores the group
permissions.

For information about adding roles to users, see Managing roles for a user. For information about adding roles to
groups, see Managing roles for a group.

## Assigning roles to levels

Coverity Connect allows you to assign roles directly to users and groups at each of
the levels:

Adding roles at the triage store level
:   Specific users and groups can be assigned roles through Configuration > Triage Stores. In order to add users and group role assignments at this
    level, the granter must have the Manage triage
    stores permission. For more information, see Managing triage stores.

Adding roles at the component level
:   Specific users and groups can be assigned roles through Configuration > Component Maps. In order to add users and group role assignments at this
    level, the granter must have the Manage component
    maps permission. For more information, see Using components.

Adding roles at the project level
:   Specific users and groups can be assigned roles through Configuration > Projects & Streams. Users that are assigned roles through the project are
    granted permissions that apply only to the project. You must have a role
    with the Manage projects permission to add users
    and assign project-level roles. For more information, see Assigning roles per project or stream.

Adding roles at the stream level
:   Specific users and groups can be assigned roles at the stream level
    through Configuration > Projects & Streams. You must have a role with the Manage
    streams permission to authorize users and assign
    stream-level roles. For more information, see Assigning roles per project or stream.

Adding roles at the component map level
:   Specific users and groups can be assigned roles through Configuration > Component Maps. In order to add users and group role assignments at this
    level, the granter must have the Manage component
    maps permission. For more information, see Assigning roles to a component map.
