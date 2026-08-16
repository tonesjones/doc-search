---
title: "Roles and permissions"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/roles-and-permissions.html"
content_id: "px4H6Xj8K9wJmlNa5lPcvw"
product_key: "polaris-platform-latest"
section: "Reference"
scraped_at: "2026-08-12T19:57:58.571931+00:00"
content_hash: "74703e92229cf3197b9887de32d7eb61b74d834a30bc227e3e88de0ac7178d79"
---

# Roles and permissions

Roles in your organization are divided into two levels: organization-level roles and application-level roles. This page describes all the roles, and what each role can do.

## Organization-level roles

- Organization Admin: Sets up your organization's Polaris account and manages users and groups within it. Each organization has at least one Organization Admin.
- Organization Application Manager: Has full access to all applications within the organization.

Note: You can assign organization-level roles to users or groups. Most users don't have organization-level permissions, but receive application-level permissions from an Application Admin. No Global Role refers to users who don't have organization-level permissions.

## Application-level roles

- Application Admin: The owner of one or more applications.
- Contributor: A user with access to an application who can create and manage projects, run test, and triage issues.
- Member: A user with access to an application who can do everything a contributor can do, except create, update, or delete projects.
- Observer: A user with access to an application who can view projects, test results, and issues, but cannot run tests or triage issues.

Note: Organization Administrators can create custom application-level roles on the Roles tab (My Organization > Roles). For more information, see [Manage permissions with custom roles](../how-to/manage-permissions-with-custom-roles.md).

After you add a user or group to an application, you can set the user or group's application-level role. For more information, see Add users and groups to an application.

## Roles and permissions tables

Table 1. Roles and permissions

|  | Organization-Level Roles | | Application-Level Roles | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Organization Admin | Organization Application Manager | Application Admin | Application Contributor | Application Member | Application Observer |
| **Entitlements** (**controlled at the Application level**) | | | | | | |
| View entitlements | Yes | Yes | Yes | Yes | Yes | Yes |
| Allocate entitlements to the application | Yes | Yes | Yes | No | No | No |
| **Application** | | | | | | |
| Create applications | Yes | Yes | No | No | No | No |
| View applications | Yes | Yes | Yes | Yes | Yes | Yes |
| Update applications | Yes | Yes | No | No | No | No |
| Delete applications | Yes | Yes | No | No | No | No |
| **Project** | | | | | | |
| Create projects | Yes | Yes | Yes | Yes | No | No |
| View projects | Yes | Yes | Yes | Yes | Yes | Yes |
| Update projects | Yes | Yes | Yes | Yes | No | No |
| Delete projects | Yes | Yes | Yes | Yes | No | No |
| Move projects between applications | Yes | Yes | Yes | No | No | No |
| **Branch** | | | | | | |
| Create branch | Yes | Yes | Yes | Yes | Yes | No |
| View branch | Yes | Yes | Yes | Yes | Yes | Yes |
| Update branch | Yes | Yes | Yes | Yes | Yes | No |
| Delete branch | Yes | Yes | Yes | Yes | Yes | No |
| **Labels** | | | | | | |
| Create labels | Yes | No | No | No | No | No |
| Create labels (if allowed by the Organization Administrator) | Yes | Yes | Yes | Yes | No | No |
| View all labels in the portfolio | Yes | Yes | No | No | No | No |
| Edit and delete labels | Yes | No | No | No | No | No |
| Apply labels to applications | Yes | Yes | Yes | No | No | No |
| Apply labels to projects | Yes | Yes | Yes | Yes | No | No |
| Apply labels to branches | Yes | Yes | Yes | Yes | No | No |
| **User Management** | | | | | | |
| Add users | Yes | No | No | No | No | No |
| Assign users to specific applications | Yes | Yes | No | No | No | No |
| Reset two-factor authentication for user | Yes | No | No | No | No | No |
| View users assigned to application-level roles | Yes | Yes | Yes | No | No | No |
| Assign/unassign other users to application-level roles | Yes | Yes | Yes | No | No | No |
| View list of application roles | Yes | Yes | Yes | No | No | No |
| **Service Account Management** | | | | | | |
| View service accounts | Yes | No | No | No | No | No |
| Create service accounts | Yes | No | No | No | No | No |
| Delete service accounts | Yes | No | No | No | No | No |
| **Role Management** | | | | | | |
| Create roles | Yes | No | No | No | No | No |
| View a list of all roles | Yes | No | No | No | No | No |
| Update roles | Yes | No | No | No | No | No |
| Delete roles | Yes | No | No | No | No | No |
| **Group Management** | | | | | | |
| Create groups | Yes | No | No | No | No | No |
| View a list of all groups | Yes | Yes | Yes | No | No | No |
| View groups you belong to | Yes | Yes | Yes | Yes | Yes | Yes |
| View a group's members | Yes | No | No | No | No | No |
| View a group's organization-level role | Yes | No | No | No | No | No |
| View a group's application-level role | Yes | Yes | Yes | No | No | No |
| Update a group's name | Yes | No | No | No | No | No |
| Update a group's organization-level role | Yes | No | No | No | No | No |
| Update a group's application-level role | Yes | Yes | Yes | No | No | No |
| Add or remove group members | Yes | No | No | No | No | No |
| Delete groups | Yes | No | No | No | No | No |
| **Risk Scoring** | | | | | | |
| Enable risk scoring | Yes | No | No | No | No | No |
| Create risk factor | Yes | No | No | No | No | No |
| Update risk factor | Yes | No | No | No | No | No |
| Delete risk factor | Yes | No | No | No | No | No |
| Update risk factor weights | Yes | No | No | No | No | No |
| Edit risk factors | Yes | Yes | No | No | No | No |
| View risk scores | Yes | Yes | Yes | Yes | Yes | Yes |
| **Scanning/Test Management** | | | | | | |
| Start scan | Yes | Yes | Yes | Yes | Yes | No |
| View scan | Yes | Yes | Yes | Yes | Yes | Yes |
| Pause scan (update) | Yes | Yes | Yes | Yes | Yes | No |
| Cancel scan (delete) | Yes | Yes | Yes | Yes | Yes | No |
| Download test artifacts | Yes | Yes | Yes | Yes | Yes | Yes |
| **Secure Tunnels** | | | | | | |
| Add a secure tunnel to the Polaris UI | Yes | No | No | No | No | No |
| **SAST tool version customization** | | | | | | |
| Audit SAST tool versions | Yes | No | No | No | No | No |
| Update organization-level SAST tool version | Yes | No | No | No | No | No |
| View application-level SAST tool version | Yes | Yes | Yes | Yes | Yes | Yes |
| Update application-level SAST tool version | Yes | Yes | No | No | No | No |
| View project-level SAST tool version | Yes | Yes | Yes | Yes | Yes | Yes |
| Update project-level SAST tool version | Yes | Yes | Yes | Yes | No | No |
| View branch-level SAST tool version | Yes | Yes | Yes | Yes | Yes | Yes |
| Update branch-level SAST tool version | Yes | Yes | Yes | Yes | Yes | No |
| **File and Folder Exclusion** | | | | | | |
| View organization-level exclusion rules | Yes | No | No | No | No | No |
| Update organization-level exclusion rules | Yes | No | No | No | No | No |
| View application-level exclusion rules | Yes | Yes | Yes | Yes | Yes | Yes |
| Update application-level exclusion rules | Yes | Yes | No | No | No | No |
| View project-level exclusion rules | Yes | Yes | Yes | Yes | Yes | Yes |
| Update project-level exclusion rules | Yes | Yes | Yes | Yes | No | No |
| **Triage approval workflows** | | | | | | |
| View organization-level triage approval workflow | Yes | No | No | No | No | No |
| Update organization-level triage approval workflow | Yes | No | No | No | No | No |
| View application-level triage approval workflow | Yes | Yes | Yes | Yes | Yes | Yes |
| Update application-level triage approval workflow | Yes | Yes | No | No | No | No |
| View project-level triage approval workflow | Yes | Yes | Yes | Yes | Yes | Yes |
| Update project-level triage approval workflow | Yes | Yes | Yes | Yes | No | No |
| **Issue** | | | | | | |
| Update issue (not triaged/to be fixed) | Yes | Yes | Yes | Yes | Yes | No |
| Delete issue (dismiss) | Yes | Yes | Yes | Yes | Yes | No |
| View issue history | Yes | Yes | Yes | Yes | Yes | Yes |
| Approve or reject issue triage request | Yes | Yes | Yes | No | No | No |
| **Black Duck Assist** | | | | | | |
| Enable/disable Black Duck Assist | Yes | No | No | No | No | No |
| Use Black Duck Assist | Yes | Yes | Yes | Yes | Yes | Yes |
| **Issue tracking integrations** | | | | | | |
| Create organization-level issue tracking connections | Yes | No | No | No | No | No |
| View organization-level issue tracking connections | Yes | No | No | No | No | No |
| Update organization-level issue tracking connections | Yes | No | No | No | No | No |
| Create issue tracking integration options | Yes | No | No | No | No | No |
| Update issue tracking integration options | Yes | No | No | No | No | No |
| Delete issue tracking integration options | Yes | No | No | No | No | No |
| Delete organization-level issue tracking connections | Yes | No | No | No | No | No |
| Create project-level issue tracking connection | Yes | Yes | Yes | No | No | No |
| View project-level issue tracking connection | Yes | Yes | Yes | Yes | Yes | Yes |
| Update project-level issue tracking connection | Yes | Yes | Yes | No | No | No |
| Export issues to Azure DevOps/Jira | Yes | Yes | Yes | Yes | Yes | No |
| View links to exported issues | Yes | Yes | Yes | Yes | Yes | Yes |
| **Secure Code Warrior Integration** | | | | | | |
| Enable/disable integration | Yes | No | No | No | No | No |
| **Dashboard** | | | | | | |
| View dashboard | Yes | Yes | Yes | Yes | Yes | Yes |
| Manage default filters | Yes | Yes | Yes | Yes | Yes | Yes |
| Create and manage saved filters | Yes | Yes | Yes | Yes | Yes | Yes |
| **Reporting** | | | | | | |
| Create and download report | Yes | Yes | Yes | Yes | Yes | No |
| Delete report | Yes | Yes | Yes | Yes | Yes | No |
| Create report configuration | Yes | Yes | Yes | Yes | Yes | No |
| Update report configuration | Yes | Yes | Yes | Yes | Yes | No |
| Delete report configuration | Yes | Yes | Yes | Yes | Yes | No |
| **Audit** | | | | | | |
| View audit log | Yes | No | No | No | No | No |
| Download audit log | Yes | No | No | No | No | No |
| **Policy** | | | | | | |
| Create policy | Yes | Yes | No | No | No | No |
| Update policy | Yes | Yes | No | No | No | No |
| Delete policy | Yes | Yes | No | No | No | No |
| Assign/unassign policy to organization | Yes | No | No | No | No | No |
| Assign/unassign policy to application | Yes | Yes | Yes | No | No | No |
| Assign/unassign policy to project | Yes | Yes | Yes | No | No | No |
| Assign/unassign policy to branch | Yes | Yes | Yes | No | No | No |
| Manage default policy values for new branches | Yes | No | No | No | No | No |
| View policy applied to application, project, or branch | Yes | Yes | Yes | Yes | Yes | Yes |
| Receive policy notifications | Yes | No | No | No | No | No |
| **Notifications** | | | | | | |
| Manage global notification settings | Yes | No | No | No | No | No |
| **SCM Repository Configuration** | | | | | | |
| Create SCM repository connection | Yes | Yes | Yes | No | No | No |
| Bulk onboard applications and projects | Yes | Yes | No | No | No | No |
| Integrate individual repositories/bulk onboarding projects into application | Yes | Yes | Yes | No | No | No |
| Synchronize Polaris with SCM provider | Yes | Yes | Yes | No | No | No |
| Manage organization-level event-based test automation settings | Yes | No | No | No | No | No |
| Manage application-level event-based test automation settings | Yes | Yes | Yes | No | No | No |
| Manage project-level event-based test automation settings | Yes | Yes | Yes | No | No | No |
| Manage branch-level event-based test automation settings | Yes | Yes | Yes | No | No | No |
| View SCM repository connection | Yes | Yes | Yes | Yes | Yes | Yes |
| Update SCM repository connection | Yes | Yes | Yes | No | No | No |
| Test SCM repository connection | Yes | Yes | Yes | Yes | Yes | No |
| Cancel bulk onboarding of applications and projects | Yes | Yes | No | No | No | No |
| Cancel bulk onboarding of projects into applications | Yes | Yes | Yes | No | No | No |
| **Component** | | | | | | |
| View component | Yes | Yes | Yes | Yes | Yes | Yes |
| Update component triage status | Yes | Yes | Yes | Yes | Yes | No |
| Approve or reject component triage request | Yes | Yes | Yes | No | No | No |
| Manually add component | Yes | Yes | Yes | Yes | Yes | No |
| Update component | Yes | Yes | Yes | Yes | Yes | No |
| Delete a manually-added component | Yes | Yes | Yes | Yes | Yes | No |
| Export SBOM (report) | Yes | Yes | Yes | Yes | Yes | No |
| **License** | | | | | | |
| View license | Yes | Yes | Yes | Yes | Yes | Yes |
| Update License (Pick license) | Yes | Yes | Yes | Yes | Yes | No |
