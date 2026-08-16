---
title: "Manage permissions with custom roles"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/manage-permissions-with-custom-roles.html"
content_id: "AUW9syQP3nM7lXYbWFxf3A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:04.394820+00:00"
content_hash: "629fc26faf420b5cbf0ee18df90d33a0e34ddfd3417ad1305bead02c8ba074b8"
---

# Manage permissions with custom roles

Create custom application-level roles to manage what different users or groups in your organization can do in the applications they have access to.

## Overview

Organization administrators can create custom application-level roles to control what different users and groups can do in the applications they have access to. Custom roles can also be assigned to Polaris service accounts.

Note: Only organization administrators can create and manage custom roles. The default application-level roles (Administrator, Contributor, Member, and Observer) cannot be modified.

### Tutorial: Creating custom roles in Polaris

Note: Interactive tutorials are updated periodically and may change without notice.

Figure 1. Tutorial: Creating custom roles. *This interactive tutorial demonstrates how to create and manage custom roles in Polaris.* [Open in new tab.](https://www.iorad.com/player/2544228/Polaris--Creating-custom-roles)

### Permission reference

All of the permissions you can assign to custom roles are listed in the table below:

Table 1. Available permissions for custom roles

| Category | Permission | Allows users to... |
| --- | --- | --- |
| Components | Approve component triage requests | - Approve triage requests for components - Reject triage requests for components |
| Delete components | - Delete manually-added components |
| Triage components | - Update component triage status |
| Write components | - Add components and component origins - Edit components - Reset edited components |
| Create and manage Fix Pull Requests | - Create automatic and manual Fix PRs - Customize maximum number of Fix PRs per branch and upgrade guidance |
| Issues | Approve issue triage requests | - Approve triage requests for issues - Reject triage requests for issues |
| Bug tracking system export | - Export an issue via issue tracking integration |
| Triage issue | - Update issue (not triaged/to be fixed) triage status - Delete issue (dismissed) - Change other issue properties |
| Reports | Create and manage reports | - Create and download reports |
| Labels | Create and manage labels | - Create labels - Update labels |
| View labels | - View labels |
| Tests | Create and manage tests | - Start scan - Pause scan (update) - Cancel scan (delete) |
| Branches | Create branches and manage branch settings | - Create branches - Update branches |
| Delete branches | - Delete branches |
| Projects | Create projects and manage project settings | - Create projects - Update projects - Create project-level tracking connection - Update project-level issue tracking connection - Create SCM repository connection - Update SCM repository connection - Test SCM repository connection - Cancel bulk onboarding of applications and projects - Cancel bulk onboarding of projects into applications - Manage project file and folder exclusion rules - Manage project-level triaging issue severity setting - Manage project-level triage approval workflow |
| Delete projects | - Delete projects |
| Move projects | - Move SAST & SCA projects between applications with team member (concurrent) subscriptions |
| Application | Manage application settings | - Allocate entitlements to the application - View users assigned to application-level roles - Assign/unassign other users to application-level roles - View list of application roles - View a group's members - View a group's application level role - Update a group's application level role - Assign/unassign policy to a project - Manage application file and folder exclusion rules - Manage application-level triaging issue severity setting - Manage project-level triage approval workflow |
| Licenses | Manage licenses | - Update license (pick license) |

### Audit logs

Events appear on the Audit Logs page when a role is created, updated, or deleted.

## Create a role

To create a role, follow these steps:

Note: Only organization administrators can create roles.

1. Go to My Organization > Roles.
2. Select Create Role.
3. Enter a name in the Role Name field.

   [image: roles custom create]

   Note: Role names in Polaris must be unique, 3–50 characters long, and can include spaces and special characters.
4. (Optional) Enter a description in the Description field.
5. (Optional) Use the checkboxes to grant the role permissions. You can search for permissions using the search box.
6. Select Create Application Role.

## Duplicate a role

To duplicate a role, follow these steps:

Note: Only organization administrators can duplicate roles.

1. Go to My Organization > Roles.
2. After you find the role you want to duplicate, select the options [image: icon polaris options] icon at the end of the role's row and select Duplicate Role.

## Edit a custom role

To modify a custom role (including changing a role's name, description, or permissions), follow these steps:

Note: You can only modify custom roles; the default roles (Administrator, Contributor, Member, and Observer) cannot be modified. Only organization administrators can modify custom roles.

1. Go to My Organization > Roles.
2. Select a custom role to modify.
3. Modify the role, as required.
4. Select Save Changes.

   Note: A warning appears if you edit a custom role that's currently assigned to one or more service accounts.

## Delete a role

To delete a role, follow these steps:

Note: You can only delete custom roles; the default roles (Administrator, Contributor, Member, and Observer) cannot be deleted. Only organization administrators can delete roles.

1. Go to My Organization > Roles.
2. Select the options [image: icon polaris options] icon at the end of the role's row and select Delete Role.

   A confirmation appears.
3. Select DELETE ROLE.

   CAUTION:

   When you delete a role, all members may immediately lose access to the applications and features associated with it. Roles you delete cannot be recovered.

## Assign roles to users and groups

Organization administrators, organization application managers, application administrators, and other users with permissions to manage application settings can add users and groups to an application, and assign roles to different groups and users. For more information, see Add users and groups to an application.
