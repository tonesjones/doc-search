---
title: "Built-in groups"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/built-in-groups.html"
content_id: "9JyoEckfTeIzXz0iJEXMXw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:40.384815+00:00"
---

# Built-in groups

By default, built-in groups are assigned specific roles that allow each group to perform
functions:

Administrators
:   By default, members of this group have the Server
    Admin role at the Global level, which
    provides them system-wide access to Coverity Connect.

Configuration Managers
:   By default, members of this group have the Project
    Admin and Project Owner roles, which
    allow them to configure projects, streams, components, and
    attributes.

Users
:   By default, members of this group have
    Committer and Developer
    roles at the Global level, and they have the
    Developer role at the
    Component level. Every user that is created is,
    by default, a member of this group.

Note that you can customize access control permissions by changing roles for these and
other groups. For more information, see Managing roles for a group. For
additional details about these roles, see Figure 1.

Note: For user administration and system management tasks, rather than using the default
Administrator account, it is recommended that an alternative
administrator account be created. Follow the procedures in Managing users, groups, and roles to create a new user account and assign
it to the Administrators group. That user account will have all
of the permissions of the Server Admin role.
