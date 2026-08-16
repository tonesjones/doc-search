---
title: "Role ID (Built-in Roles: roleAssignmentDataObj.roleId)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/role-id-built-in-roles-roleassignmentdataobj.roleid-.html"
content_id: "~nxmRLtI3Hu0CTsmpdwXog"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:59.677768+00:00"
---

# Role ID (Built-in Roles: roleAssignmentDataObj.roleId)

| Attribute Type | **Coverity Connect Role** | Description |
| --- | --- | --- |
| committer | Committer | Editable and deletable. Supports committing analysis results to the database. Default permissions: commitToStream |
| desktopDeveloper | Desktop Developer | Editable and deletable. Supports permissions commonly needed by Coverity Desktop developers. Default permissions: triageDefects, accessWS, viewDefects, createStreams, manageProjects, viewSource, accessWebUI |
| developer | Developer | Editable and deletable. Supports permissions commonly needed by developers who use Coverity Connect. Default permissions: triageDefects, accessWS, viewDefects, viewSource, accessWebUI, viewProjectsHistoryAndTrends |
| hierarchyAdmin | Hierarchy Administrator | Not editable or deletable. Supports the creation of Policy Manager Hierarchies. Default permissions: accessWS, manageHierarchies, viewIntegrityControl, accessWebUI |
| icUser | Policy Manager User | Not editable or deletable. Supports end usage of Policy Manager, which includes creating, editing, and using charts and heatmaps. Default permissions: accessWS, accessWebUI, viewIntegrityControl |
| noAccess | No Access | Not editable or deletable. Prohibits access. No permissions are enabled. |
| observer | Observer | Editable and deletable. Default permissions: accessWS, viewDefects, viewSource, accessWebUI, viewProjectsHistoryAndTrends |
| projectAdmin | Project Admin | Editable and deletable. Supports permissions that are commonly needed by project administrators. Default permissions: accessWS, manageComponentMaps, createTriageStores, manageAttributes, createProjects, accessWebUI |
| projectOwner | Project Owner | Not editable or deletable. Supports permssions needed by project owners. Default permissions: triageDefects, commitToStream, accessWS, viewDefects, createStreams, manageProjects, viewSource, accessWebUI, manageStreams, viewProjectsHistoryAndTrends |
| reporter | System Report Generator | Not editable or deletable. Default permissions: viewDefects, viewSource |
| serverAdmin | Server Admin | Editable and deletable. Default permissions: accessWS, accessWebUI, manageRoleDefinitions, manageUsersGroups, manageServerParams |
| streamAdmin | Stream Admin | Editable and deletable. Default permissions: accessWS, createStreams, accessWebUI |
| streamOwner | Stream Owner | Not editable or deletable. Default permissions: triageDefects, commitToStream, accessWS, viewDefects, viewSource, accessWebUI, manageStreams |
| sysAdmin | System Admin | Not editable or deletable. Default permissions: *All permissions* |
| triageStoreOwner | Triage Store Owner | Not editable or deletable. Default permissions: accessWS, viewDefects, triageDefects, manageTriageStores, accessWebUI |
| visitor | Visitor | Not editable or deletable. . Default permissions: accessWS, accessWebUI |
| wsReporter | Web Service Reporter | Editable and deletable. Default permissions: accessWS, viewDefects |
