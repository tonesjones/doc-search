---
title: "Black Duck SCA User Role Matrix"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-sca-user-role-matrix.html"
content_id: "1KDhz_ItFDMnkSPMav17gw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:38.279698+00:00"
---

# Black Duck SCA User Role Matrix

The roles assigned to a user or group determine the tasks that can be performed. You can
assign multiple roles (or no roles) to a user or group.

Roles are also assigned to a user when a user is assigned as a member of a project or a
project group.

## Global roles by task

| Task | Roles (details or restrictions) |
| --- | --- |
| Manage code scans/Protex BOM files:   - Scan code - Upload scans to Black Duck SCA. - Map or unmap scans to projects - Delete scans | - Global Project Administrator (Map/unmap/delete scans only) - Global Project Manager (Map/unmap/delete scans only) - Global Code Scanner |
| Create, edit, delete projects | - Global Project Administrator - Global Project Manager - Project Creator (edit/delete solely the project created by the corresponding user) |
| Add or remove users from a project | - Global Project Administrator (add users with a defined   role) - Global Project Manager (Add users but cannot define their   roles. Users added to projects by a global project   manager will have read only access to the projects and   will not be able to edit or modify the BOM.) - User Administrator (add users with a defined role) - Global Project Group Administrator (add users with a   defined role)   Note: If the appropriate Role setting is not enabled, additional restrictions may apply to role assignment. |
| Manage projects versions:   - Create, edit, delete project versions - Edit project or version settings, including tags | - Global Project Administrator - Global Project Manager - Global Release Creator (Create permission only) - Project Creator (See Project Manager role for permissions   obtained when creating a project) |
| Manage custom components | - Component Manager - Global Project Administrator - Global Project Manager |
| Manage licenses:   - Create, edit, delete custom licenses - Manage KnowledgeBase licenses - Create, edit, delete custom license families - Manage KB and custom license terms | - License Manager |
| View BOMs:   - View BOM - Add/edit/view comments - Print BOM - Compare BOMs | - Global Project Administrator (Cannot edit comments   created by other users) - Global Project Manager - Global Project Viewer (View all projects only)  Important: Users with only the **Global Project Viewer** role cannot view   SCM project BOMs. To create, view, and manage SCM   projects, users must have either the **Lite Global   Project Manager** role or the **Integration   Manager** role. - Any other user assigned to the project |
| Manage BOMs:   - Manually add components; delete manually added   components - Ignore components - Review components - Remediate security vulnerabilities - Override policy violations - Remove override of policy violations - Edit licenses, including excluding license from Notices   File report, adding an attribution statement, or   selecting a different license for a component   version - Indicate license term fulfillment status - Manage deep license data - View license conflicts | - Global Project Manager |
| Manage policy rules | - Policy Manager (can create global policy rules, as well as edit and delete group-scoped   policy rules) - Global Project Admin + Policy Manager (can create global or project group scoped policy   rules for any project groups) - Project Group Admin + Global Policy Manager (can create global or project group-scoped   policy rules for their project groups) |
| Update Additional (Custom, SBOM) fields | - Component Manager (Can only update Component and   Component Version custom fields) - Custom Fields Administrator (Can only create, edit,   delete Custom Fields) - Global Project Administrator (Update custom field values   for project, project version, and BOM) |
| Create, edit, or delete global remediation statuses | - Global Project Administrator - Global Project Manager - Global Security Manager (Must be assigned to a project to   view data) |
| Run project vulnerability reports from the Reports menu | The following roles can create a project vulnerability report for any project:  - Global Project Manager - Global Project Administrator - Global Project Viewer  The following roles must be assigned to a project to create a project vulnerability report:   - Component Manager - Copyright Editor - Custom Fields Administrator - Global Code Scanner - Global Project Group Administrator - Global Release Creator - Global Security Manager - License Manager - Policy Manager - Project Creator - System Administrator - User Administrator |
| Create and modify copyright statements | - Copyright Editor (Must be assigned to a project to view   data) |
| Run Project version reports:   - Version Details report - Vulnerability report - Notices File report - Software Bill of Materials (SBOM) report | The following roles can create a project version report for any project:   - Global Project Manager - Global Project Administrator     The following roles must be assigned to a project to create a project version report:   - Component Manager - Copyright Editor - Custom Fields Administrator - Global Code Scanner - Global Project Group Administrator - Global Project Viewer - Global Release Creator - Global Security Manager - License Manager - Policy Manager - Project Creator - System Administrator - User Administrator |
| Delete Project version reports | The following roles can delete a project version report for any project:   - Global Project Manager - Global Project Administrator     The following roles can only delete project version reports created by themselves:   - Component Manager - Copyright Editor - Custom Fields Administrator - Global Code Scanner - Global Project Group Administrator - Global Project Viewer - Global Release Creator - Global Security Manager - License Manager - Policy Manager - Project Creator - System Administrator - User Administrator |
| View information in Dashboard pages | The following roles can view any project from the Dashboard page:   - Global Project Manager - Global Project Administrator     The following roles can only view any projects to which they are associated on the Dashboard page:   - Component Manager - Copyright Editor - Custom Fields Administrator - Global Code Scanner - Global Project Group Administrator - Global Project Viewer - Global Release Creator - Global Security Manager - License Manager - Policy Manager - Project Creator - System Administrator - User Administrator |
| Access the Tools page:   - Download the scanner - Access links to the Community and Customer Education | All roles |
| Use the Search function | All roles |
| Administer Black Duck SCA. Use the Admin menu to:   - View jobs - Register Black Duck SCA. - Configure LDAP - Configure SAML - Manage system settings - Manage system announcements - Configure password requirements | - System Administrator |
| Administer users and groups. Use the Admin menu to:   - Manage users, including resetting passwords - Manage groups | - User Administrator |
| Manage snippets | - Global Project Manager - Global Project Administrator |
| View issues | - Global Project Manager - Global Project Administrator |
| Manage project groups:   - Create/Edit/Delete project groups - Add/Remove members and user groups from project   groups | - Global Project Group Administrator |
| Manage Access Tokens | - User Administrator |
| View notifications | - Global Notification Viewer (View notifications for all   projects and receives all system notifications regardless of   user preferences) |
| Download the heatmap CSV report | - System Administrator |
| View the scan heatmap | - Global Project Administrator - Global Project Manager - Global Notification Viewer - Global Project Viewer - Global Code Scanner |
| Manage integration servers | - Integration Manager |
| Manage lightweight BOMs | - Lite Global Project Manager |
| Convert project versions to LTS | - Global Project Administrator - Global Project Manager |
| Enable/disable Multi-Factor Authentication (MFA) | - User Administrator |

## Project and Project Group roles

| Task | Roles (details or restrictions) |
| --- | --- |
| Manage project groups:   - Create/Edit/Delete project groups - Add/Remove members and user groups from project   groups | - Project Group Administrator (below parent group) |
| Manage code scans/Protex BOM files:   - Scan code - Upload scans to Black Duck SCA. - Map or unmap scans to projects - Delete scans | - Project Manager (Can unmap/delete scans from their   projects) - Project Group Manager (Can unmap/delete scans from their   projects) - Project Code Scanner (Can map/unmap/delete a code scan   to/from projects for which they have access) - Project Group Code Scanner |
| Create, edit, delete projects | - Project Administrator (Delete/Edit only) - Project Group Administrator (must already have access to these projects) - Project Manager (cannot create projects but can delete projects to which they are   associated) |
| Manage projects:   - Create, edit, delete project versions - Edit project or version settings, including tags | - Project Administrator - Project Manager (Only projects they manage) - Project Group Administrator (must already have access to   these projects) - Project Code Scanner (Can only create project   versions) |
| Add or remove users or groups to projects | - Project Administrator (add users with a defined role on   projects they administer) - Project Manager (Add users but cannot define their roles   on projects they administer. Users added to projects by   a project manager will have read only access to the   projects and will not be able to edit or modify the   BOM.) - Project Group Administrator (must already have access to   these projects)   Note: If the appropriate Role setting is not enabled, Project Managers and Project Group Administrators cannot assign the Security Manager role at the project level. |
| Manage custom licenses:   - Create, edit, delete custom licenses | - BOM Manager |
| View BOMs:   - View BOM - View notifications - Add/edit/view comments - Print BOM - Compare BOMs | - All roles |
| Manage BOMs:   - Manually add components; delete manually added   components - Ignore components - Review components - Edit licenses, including excluding license from Notices   File report, adding an attribution statement, or   selecting a different license for a component   version - Indicate license term fulfillment status - Manage deep license data - Update custom field information - View license conflicts | - Project Administrator (Update Project and Project Version   custom fields, view BOM custom fields) - Project Manager - Project Group Administrator (must already have access to   these projects, Update Project and Project Version   custom fields, view BOM custom fields). - BOM Manager |
| Manage policy violations:   - Override policy violations - Remove override of policy violations | - Project Manager (Can only manage policy violations if   enabled by the system administrator>) - Policy Violation Reviewer |
| Remediate security vulnerabilities | - Project Manager (Can only remediate security   vulnerabilities if enabled by the system administrator) - Security Manager (Can only modify remediation for   vulnerabilities associated with components) |
| Update custom field values | - Project Manager (Can only update BOM Component, Project,   and Project Version custom fields) - BOM Annotator (Can only update BOM Component custom   field) - BOM Manager (Can only update BOM Component custom   field) |
| Manage policy rules:   - Create, edit, or delete policy rules | - No project or project group level role can perform this   task |
| Run project vulnerability reports from the Report menu:   - Vulnerability Remediation Report - Vulnerability Status Report - Vulnerability Update Report | - All roles |
| Run Project version reports:   - Version Details report - Vulnerability report - Notices File report - Software Bill of Materials (SBOM) report | - All roles |
| Delete project version reports | The following roles can delete all reports:   - Project Administrator - Project Manager - Project Group Administrator (must already have access to these projects)   The following roles can delete reports generated by themselves:   - All roles |
| View information in Dashboard pages | - All roles |
| Access the Tools page from which user can:   - Download the scanner - Access API documentation | - All roles |
| Search | - All roles |
| Manage snippets | - Project Administrator - Project Manager - BOM Manager |
| Convert project versions to LTS | - Project Administrator - Project Manager |
