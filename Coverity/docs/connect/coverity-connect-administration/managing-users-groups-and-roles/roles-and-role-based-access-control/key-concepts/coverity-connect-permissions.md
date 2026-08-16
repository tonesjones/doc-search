---
title: "Coverity Connect permissions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-permissions.html"
content_id: "6AmZbFcqPvbSoY_DE8d48Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:46.077621+00:00"
---

# Coverity Connect permissions

Permissions are rules that can be added to a role to define access rights for a user.
Generally, similar types of rules are assigned to a role based on a person's
responsibilities within the organization.

Global permissions
:   System permissions are access rules that are intended primarily for
    administrative tasks, such as Coverity Connect server configuration, user and
    group creation and management, and so forth. The global permissions are
    described in the following table:

    | Permission | Description |
    | --- | --- |
    | Log in to Coverity Connect | Allows the user to sign in to Coverity Connect through the web interface, assuming that the user has proper authentication credentials. |
    | Access web services | Allows the user to access the Coverity Connect Web services API. |
    | Manage server parameters | Allows the user to access the Configuration > System menu and to edit the Coverity Connect server system settings. |
    | Manage users and groups | Allows the user to access the Configuration > Users & Groups menu, and to manage user and group settings. |
    | Create users and groups | Allows the user to access the Configuration > Users & Groups menu, and to create user and group settings. |
    | Manage role definitions | Allows the user to access the Configuration > Roles menu and to create roles and assign permissions. |
    | Manage attribute definitions | Allows the user to access the Configuration > Attributes menu and to create, configure, and delete Coverity Connect triage attributes and their values. |
    | Manage component maps | Allows the user to access the Configuration > Component Maps menu. The user can add components, add RBAC access rules, and so forth. |
    | Create component maps | Allows the user to create component maps. By default, this ability is restricted to the project administrator. |
    | View component maps | Allows the user to view component maps. |
    | View global dashboard | Allows the user to access the dashboard for the current project for Quality or Security results. The dashboards shows graphs and charts that provide an overview of status of all of the project. Test advisor results are no longer supported since Test Advisor is end-of-life and unavailable as of the 2021.9.0 release. |
    | Create projects | Allows the user to access the Configuration > Projects & Streams menu to create new projects and streams in the system. |
    | Create triage stores | Allows the user to create new triage stores in the system by accessing the Configuration > Triage Stores menu. |
    | View Policy Manager | Allows the user to access Coverity Policy Manager to view and create charts that are used for monitoring and reporting on the status of the code base. Note that Coverity Policy Manager might not be enabled by your Coverity Connect license. |
    | Manage Hierarchies | Allows the user to configure Coverity Policy Manager Hierarchies. Note that Coverity Policy Manager might not be enabled by your Coverity Connect license. |

Project permissions
:   Project permissions are access control rules that are applied at the project
    level. Users with project permissions can access items and features in the
    Projects screen. For example, your organization more
    than likely has project leads or project owners. Such users are typically
    assigned roles that contain these permissions. After the roles are assigned,
    users with project permissions can then assign roles or regulate access in the
    project to the developers that are assigned to it.

    Note: Having project
    permissions *does not* automatically give the user permission to delete
    a stream. This is intentional, because one stream can be shared by more than
    one project. For a user (or a group) to be able to delete a stream, that
    user (or group) must have been assigned stream
    permissions as well.

    The project permissions are
    described in the following table:

    | Permission | Description |
    | --- | --- |
    | Manage projects | Allows the user to edit and manage the project. This can include updating the project's name and description, assigning roles to users in the project, linking streams to the project, and setting trend-data calculation formulas. |
    | Create streams | Allows the user to create new streams within the project. Attention: Stream names are case sensitive. Coverity would treat `stream1` and `Stream1` as two distinct streams. |
    | View project history and dashboard | Allows the user to view the project trends and reports. |

Stream permissions
:   Stream permissions are access control rules that are applied to users at the stream level.
    Stream permissions are intended for users (typically, developers) who are
    examining and triaging issues in the code.

    Note: Stream permissions are
    independent of project
    permissions. Project permissions do not automatically grant
    stream permissions.

    The stream permissions are described in the
    following table:

    | Permission | Description |
    | --- | --- |
    | Manage streams | Allows the user to edit and manage the stream. This can include updating the stream's name and description, assigning roles for users in the stream, and so forth. |
    | View issues | Allows to the user to view, but not triage, issues that occur in the stream to which the user is assigned. |
    | View source | Allows the user to view issue occurrences in the Source browser. |
    | Commit to stream | Allows the user to commit analysis results to Coverity Connect using the `cov-commit-defects` command. |
    | Preview commits | Allows the user to preview commits to streams using the `--preview-report` option with the `cov-commit-defects` command. |
    | Triage issues | Allows the user to change and update triage states for issues that exist in the stream. Users who do not possess this permission cannot access the triage form in the Source tab. |
    | Classify issues | Allows the user to change and update classification states for issues that exist in a stream that is associated with a triage store. Users who do not possess this permission cannot access the triage form in the **Source** tab. |

Triage Store permissions
:   Triage Store permissions are access control rules that are applied to users at
    the triage store level. Triage store permissions are intended for users
    (typically, developers) who are examining and triaging issues in the code. The
    triage store permissions are described in the following table:

    | Permission | Description |
    | --- | --- |
    | Manage triage stores | Allows the user to edit and manage the triage store. This includes updating the name and description, branching the triage store, associating streams with the triage store, and assigning roles for groups and users in the triage store. |
    | Classify issues | Allows the user to change and update classification states for issues that exist in a stream that is associated with a triage store. Users who do not possess this permission cannot access the triage form in the **Source** tab. |
    | Triage issues | Allows the user to change and update triage states for issues that exist in a stream that is associated with a triage store. Users who do not possess this permission cannot access the triage form in the Source tab. |
    | View issues | Allows to the user to view, but not triage, issues that occur in the stream to which the user is assigned. |

Component permissions
:   Component permissions are access control rules that are applied to users at
    the component level. Component permissions are intended for users
    (typically, developers) who are examining and triaging issues in the code.
    The component permissions are described in the following table:

    | Permission | Description |
    | --- | --- |
    | View source | Allows the user to view issue occurrences in the Source browser. |
    | View issues | Allows the user to view, but not triage, issues that occur in the stream to which the user is assigned. |
    | Triage issues | Allows the user to change and update triage states for issues that exist in a stream that is associated with a triage store. Users who do not possess this permission cannot access the triage form in the Source tab. |

Component map permissions
:   Component map permissions are access control rules that are applied to users at
    the component map level. Component map permissions are intended for users
    (typically, project administrators) who are managing projects. The component map
    permissions are described in the following table:

    | Permission | Description |
    | --- | --- |
    | Manage component maps | Allows the user to edit and manage the component map. This can include updating the map's name and description, associating streams with the component map, and assigning roles for groups and users in the component map. |
    | View component maps | Allows the user to view component maps. |
