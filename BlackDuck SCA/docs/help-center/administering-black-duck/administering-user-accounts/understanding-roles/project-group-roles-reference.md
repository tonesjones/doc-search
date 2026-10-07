---
title: "Project Group Roles Reference"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-group-roles-reference.html"
content_id: "xMeFdjqfMYix6sEX4HDv~A"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:18.872493+00:00"
content_hash: "12e573b0f72e6a7cdfb7bd881866c4e48434b610982384c1dae8c11bacc41e7c"
---

# Project Group Roles Reference

Project group roles provide the same permissions as their project-role counter parts,but those permissions apply to every project within the assigned project group.

Project group roles simplify administration by allowing permissions to be assigned once at the project group level instead of assigning users to individual projects.

## Available project group roles

| Project group role | Equivalent project role | Description |
| --- | --- | --- |
| Project Group Administrator | Project Administrator | Provides administrative access to projects within the assigned project group. |
| Project Manager | Project Manager / Project Owner | Manages projects, project versions, BOMs, and project membership within the assigned project group. Note that each project has exactly one Project Owner, who inherently possesses Project Manager capabilities for that project. |
| Project Code Scanner | Project Code Scanner | Manages scans and project versions for projects within the assigned project group. |
| BOM Manager | BOM Manager | Manages BOM data for projects within the assigned project group. |
| BOM Annotator | BOM Annotator | Adds comments and updates BOM component custom fields. |
| Security Manager | Security Manager | Manages vulnerability remediation activities. |
| Policy Violation Reviewer | Policy Violation Reviewer | Reviews and manages policy overrides. |
| Project Viewer | Project Viewer | Provides read-only access to projects within the assigned project group. |

Note: Each project has exactly one **Project Owner**. The Project Owner possesses the same functional capabilities as the **Project Manager** role for the owned project.

## How project group roles work

Project group roles are inherited by all projects within the assigned project group.

For example, assigning a user the **Project Manager** role at the project group level grants that user Project Manager permissions for every project in that project group.

Similarly, assigning a user the **Project Viewer** role at the project group level grants read-only access to every project in that project group.

## Direct and indirect access

Users can receive access to projects in one of two ways:

| Access type | Description |
| --- | --- |
| Direct access | The user is assigned directly to a project (for example, as a Project Owner or directly assigned a project role). |
| Indirect access | The user gains access through a project group assignment or through membership in a user group associated with a project group. |

Indirect access allows administrators to manage permissions for multiple projects through a single project group assignment.

Note: Project Owners and Project Managers can add users to a project, but cannot assign or administer user roles for project members. Users added to a project by a Project Owner or Project Manager default to read-only access (the **Project Viewer** role). To enable user role administration across projects within a project group, users must be assigned a project-group-scoped **Project Administrator** or **Project Group Administrator** role.

## Related information

- Understanding roles
- Global roles reference
- Project roles reference
- Black Duck SCA user role matrix
