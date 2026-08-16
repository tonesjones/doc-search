---
title: "Understanding roles"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-roles.html"
content_id: "ns0Bc~AESKel_ZtEYkWbFA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:35.747973+00:00"
---

# Understanding roles

Black Duck SCA uses roles to control what users can view and manage.
Roles define the actions users can perform and the information they can access. Users
can be assigned roles individually or through group membership. Permissions from
multiple roles are combined.

If no roles are assigned, users have read-only access to Black Duck and to the projects
to which they are assigned.

## Role types

Black Duck provides three types of roles:

- **Global roles**

  Global roles grant permissions across the entire Black Duck SCA environment.
  These roles are typically assigned to users who perform administrative,
  security, compliance, reporting, or system-wide management tasks.

  Common global roles include:

  | Role | Purpose |
  | --- | --- |
  | System Administrator | Configure and administer Black Duck |
  | User Administrator | Manage users, groups, and access |
  | Global Project Administrator | Manage projects and project versions across the system |
  | Global Project Manager | Manage projects, project versions, and BOMs across the system |
  | Global Project Viewer | View all projects and BOMs |
  | Global Code Scanner | Manage scans across all projects |
  | Component Manager | Manage custom components |
  | License Manager | Manage licenses and license data |
  | Policy Manager | Manage policy rules |
  | Global Security Manager | Manage remediation statuses |
  | Integration Manager | Manage integrations |

  For detailed role capabilities, see **Global roles
  reference**
- **Project roles**

  Project roles apply only to the projects to which a user has been assigned.
  Use project roles when users need access to specific projects without
  receiving broader system-wide permissions.

  Common project roles include:

  | Role | Purpose |
  | --- | --- |
  | Project Administrator | Manage project settings and membership |
  | Project Manager | Manage project versions, BOMs, and project membership |
  | BOM Manager | Manage BOM data |
  | BOM Annotator | Add comments and update BOM component custom fields |
  | Project Code Scanner | Manage scans for assigned projects |
  | Security Manager | Remediate vulnerabilities |
  | Policy Violation Reviewer | Manage policy overrides |
  | Project Viewer | View project information and reports |

  For detailed role capabilities, see **Project
  roles reference**.
- **Project group roles**

  Project group roles provide the same capabilities as their project-role
  counterparts but apply to every project within an assigned project group.
  They help administrators manage permissions consistently across multiple
  related projects.

  Examples include:

  - Project Group Administrator
  - Project Manager
  - Project Code Scanner
  - BOM Manager
  - BOM Annotator
  - Security Manager
  - Policy Violation Reviewer
  - Project Viewer

  For detailed role capabilities, see **Project group roles reference**.

## Assigning roles

Roles can be assigned directly to users or to groups. When a role is assigned to a group, all
group members inherit that role and its permissions.

Users can also receive project-level permissions when they are assigned a role within
a project or project group.

## How permissions are combined

Users can have multiple roles. A user's effective permissions are the combination of
all assigned global, project, and project group roles.

For example, a user might:

- Have a global role that allows project administration.
- Have a project role that allows BOM management.
- Have a project group role that provides access to multiple projects.

Together, these roles determine the user's available actions within Black Duck SCA.

## Direct and indirect access

Project groups introduce two methods of access:

**Direct access**

The user is assigned directly to a project.

**Indirect access**

The user gains access through a project group assignment or through membership in a user group
that is associated with a project group.

Project group roles allow permissions to be applied consistently across multiple
projects without assigning users to each project individually.

## Choosing the appropriate role type

| If the user needs to... | Assign... |
| --- | --- |
| Administer Black Duck SCA or manage resources across all projects | A global role |
| Work within specific projects only | A project role |
| Work across multiple projects in the same project group | A project group role |

## Related information

- Global roles reference
- Project roles reference
- Project group roles reference
- Black Duck SCA user role
  matrix
