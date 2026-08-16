---
title: "Project Group Roles Reference"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-group-roles-reference.html"
content_id: "WvCy7fNsktjwWuvR1ScQ_Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:37.511773+00:00"
---

# Project Group Roles Reference

Project group roles provide the same permissions as their project-role counter parts,but
those permissions apply to every project within the assigned project group.

Project group roles simplify administration by allowing permissions to be assigned once
at the project group level instead of assigning users to individual projects.

## Available project group roles

| Project group role | Equivalent project role | Description |
| --- | --- | --- |
| Project Group Administrator | Project Administrator | Provides administrative access to projects within the assigned project group. |
| Project Manager | Project Manager | Manages projects, project versions, BOMs, and project membership within the assigned project group. |
| Project Code Scanner | Project Code Scanner | Manages scans and project versions for projects within the assigned project group. |
| BOM Manager | BOM Manager | Manages BOM data for projects within the assigned project group. |
| BOM Annotator | BOM Annotator | Adds comments and updates BOM component custom fields. |
| Security Manager | Security Manager | Manages vulnerability remediation activities. |
| Policy Violation Reviewer | Policy Violation Reviewer | Reviews and manages policy overrides. |
| Project Viewer | Project Viewer | Provides read-only access to projects within the assigned project group. |

## How project group roles work

Project group roles are inherited by all projects within the assigned project
group.

For example, assigning a user the **Project Manager** role at the project group
level grants that user Project Manager permissions for every project in that project
group.

Similarly, assigning a user the **Project Viewer** role at the project group level
grants read-only access to every project in that project group.

## Direct and indirect access

Users can receive access to projects in one of two ways:

| Access type | Description |
| --- | --- |
| Direct access | The user is assigned directly to a project. |
| Indirect access | The user gains access through a project group assignment or through membership in a user group associated with a project group. |

Indirect access allows administrators to manage permissions for multiple projects
through a single project group assignment.

## Related information

- Understanding roles
- Global roles reference
- Project roles reference
- Black Duck SCA user role
  matrix
