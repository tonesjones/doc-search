---
title: "Retrieve all roles"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-roles.html"
content_id: "7RSERcMqGd66I1YAByEjrg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:36.040974+00:00"
---

# Retrieve all roles

Example GET request to retrieve all roles.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/roles" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "roles": [
    {
      "name": "componentMapOwner",
      "displayName": "Component Map Owner",
      "description": "componentMapOwner",
      "displayDescription": "Manage component maps",
      "deletable": false,
      "editable": false,
      "permissions": [
        "accessWebUI",
        "manageComponentMaps",
        "viewComponentMaps",
        "accessWS"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "manageComponentMaps",
          "displayName": "Manage component maps"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        }
      ]
    },
    {
      "name": "componentMapViewer",
      "displayName": "Component Map Viewer",
      "description": "componentMapViewer",
      "displayDescription": "View component maps",
      "deletable": false,
      "editable": false,
      "permissions": [
        "accessWebUI",
        "viewComponentMaps",
        "accessWS"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        }
      ]
    },
    {
      "name": "hierarchyAdmin",
      "displayName": "Hierarchy Administrator",
      "description": "hierarchyAdmin",
      "displayDescription": "Manage hierarchies, view Policy Manager",
      "deletable": false,
      "editable": false,
      "permissions": [
        "manageHierarchies",
        "accessWebUI",
        "accessWS",
        "viewIntegrityControl"
      ],
      "displayPermissions": [
        {
          "name": "manageHierarchies",
          "displayName": "Manage Hierarchies"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "viewIntegrityControl",
          "displayName": "View Policy Manager"
        }
      ]
    },
    {
      "name": "icUser",
      "displayName": "Policy Manager User",
      "description": "icUser",
      "displayDescription": "View Policy Manager",
      "deletable": false,
      "editable": false,
      "permissions": [
        "accessWebUI",
        "accessWS",
        "viewIntegrityControl"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "viewIntegrityControl",
          "displayName": "View Policy Manager"
        }
      ]
    },
    {
      "name": "noAccess",
      "displayName": "No Access",
      "description": "noAccess",
      "displayDescription": "Denied all access",
      "deletable": false,
      "editable": false,
      "permissions": [],
      "displayPermissions": []
    },
    {
      "name": "projectOwner",
      "displayName": "Project Owner",
      "description": "projectOwner",
      "displayDescription": "Manage projects",
      "deletable": false,
      "editable": false,
      "permissions": [
        "viewDefects",
        "manageProjects",
        "accessWebUI",
        "viewSource",
        "commitToStream",
        "viewComponentMaps",
        "accessWS",
        "classifyIssues",
        "createStreams",
        "manageStreams",
        "viewProjectsHistoryAndTrends",
        "triageDefects"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "manageProjects",
          "displayName": "Manage projects"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "commitToStream",
          "displayName": "Commit to a stream"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "classifyIssues",
          "displayName": "Classify Issues"
        },
        {
          "name": "createStreams",
          "displayName": "Create streams"
        },
        {
          "name": "manageStreams",
          "displayName": "Manage streams"
        },
        {
          "name": "viewProjectsHistoryAndTrends",
          "displayName": "View project history and dashboard"
        },
        {
          "name": "triageDefects",
          "displayName": "Triage issues"
        }
      ]
    },
    {
      "name": "reporter",
      "displayName": "System Report Generator",
      "description": "reporter",
      "displayDescription": "Automatic process that creates trend data",
      "deletable": false,
      "editable": false,
      "permissions": [
        "viewDefects",
        "viewSource"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        }
      ]
    },
    {
      "name": "streamOwner",
      "displayName": "Stream Owner",
      "description": "streamOwner",
      "displayDescription": "Manage streams",
      "deletable": false,
      "editable": false,
      "permissions": [
        "viewDefects",
        "accessWebUI",
        "viewSource",
        "commitToStream",
        "viewComponentMaps",
        "previewCommit",
        "accessWS",
        "classifyIssues",
        "manageStreams",
        "triageDefects"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "commitToStream",
          "displayName": "Commit to a stream"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "previewCommit",
          "displayName": "Preview Commit"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "classifyIssues",
          "displayName": "Classify Issues"
        },
        {
          "name": "manageStreams",
          "displayName": "Manage streams"
        },
        {
          "name": "triageDefects",
          "displayName": "Triage issues"
        }
      ]
    },
    {
      "name": "sysAdmin",
      "displayName": "System Admin",
      "description": "sysAdmin",
      "displayDescription": "Unrestricted access",
      "deletable": false,
      "editable": false,
      "permissions": [
        "createTriageStores",
        "accessWS",
        "classifyIssues",
        "createStreams",
        "manageServerParams",
        "manageHierarchies",
        "viewSource",
        "commitToStream",
        "createComponentMaps",
        "createUsersGroups",
        "viewIntegrityControl",
        "viewProjectsHistoryAndTrends",
        "triageDefects",
        "viewDefects",
        "manageProjects",
        "accessWebUI",
        "createProjects",
        "viewComponentMaps",
        "previewCommit",
        "manageUsersGroups",
        "manageRoleDefinitions",
        "manageAttributes",
        "manageStreams",
        "manageTriageStores",
        "manageComponentMaps",
        "viewGlobalDashboard"
      ],
      "displayPermissions": [
        {
          "name": "createTriageStores",
          "displayName": "Create Triage Stores"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "classifyIssues",
          "displayName": "Classify Issues"
        },
        {
          "name": "createStreams",
          "displayName": "Create streams"
        },
        {
          "name": "manageServerParams",
          "displayName": "Manage server parameters"
        },
        {
          "name": "manageHierarchies",
          "displayName": "Manage Hierarchies"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "commitToStream",
          "displayName": "Commit to a stream"
        },
        {
          "name": "createComponentMaps",
          "displayName": "Create component maps"
        },
        {
          "name": "createUsersGroups",
          "displayName": "Create users and groups"
        },
        {
          "name": "viewIntegrityControl",
          "displayName": "View Policy Manager"
        },
        {
          "name": "viewProjectsHistoryAndTrends",
          "displayName": "View project history and dashboard"
        },
        {
          "name": "triageDefects",
          "displayName": "Triage issues"
        },
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "manageProjects",
          "displayName": "Manage projects"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "createProjects",
          "displayName": "Create projects"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "previewCommit",
          "displayName": "Preview Commit"
        },
        {
          "name": "manageUsersGroups",
          "displayName": "Manage users and groups*"
        },
        {
          "name": "manageRoleDefinitions",
          "displayName": "Manage role definitions*"
        },
        {
          "name": "manageAttributes",
          "displayName": "Manage attributes"
        },
        {
          "name": "manageStreams",
          "displayName": "Manage streams"
        },
        {
          "name": "manageTriageStores",
          "displayName": "Manage Triage Stores"
        },
        {
          "name": "manageComponentMaps",
          "displayName": "Manage component maps"
        },
        {
          "name": "viewGlobalDashboard",
          "displayName": "View global dashboard"
        }
      ]
    },
    {
      "name": "triageStoreOwner",
      "displayName": "Triage Store Owner",
      "description": "triageStoreOwner",
      "displayDescription": "Manage triage stores",
      "deletable": false,
      "editable": false,
      "permissions": [
        "viewDefects",
        "accessWebUI",
        "accessWS",
        "classifyIssues",
        "manageTriageStores",
        "triageDefects"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "classifyIssues",
          "displayName": "Classify Issues"
        },
        {
          "name": "manageTriageStores",
          "displayName": "Manage Triage Stores"
        },
        {
          "name": "triageDefects",
          "displayName": "Triage issues"
        }
      ]
    },
    {
      "name": "visitor",
      "displayName": "Visitor",
      "description": "visitor",
      "displayDescription": "Log in with no project access",
      "deletable": false,
      "editable": false,
      "permissions": [
        "accessWebUI",
        "accessWS"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        }
      ]
    },
    {
      "name": "abc",
      "displayName": "abc",
      "description": null,
      "displayDescription": null,
      "deletable": true,
      "editable": true,
      "permissions": [
        "manageProjects",
        "accessWS"
      ],
      "displayPermissions": [
        {
          "name": "manageProjects",
          "displayName": "Manage projects"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        }
      ]
    },
    {
      "name": "committer",
      "displayName": "Committer",
      "description": "committer",
      "displayDescription": "Commit issues",
      "deletable": true,
      "editable": true,
      "permissions": [
        "viewDefects",
        "viewSource",
        "commitToStream",
        "previewCommit"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "commitToStream",
          "displayName": "Commit to a stream"
        },
        {
          "name": "previewCommit",
          "displayName": "Preview Commit"
        }
      ]
    },
    {
      "name": "developer",
      "displayName": "Developer",
      "description": "developer",
      "displayDescription": "Manage issues",
      "deletable": true,
      "editable": true,
      "permissions": [
        "viewDefects",
        "accessWebUI",
        "viewSource",
        "previewCommit",
        "accessWS",
        "classifyIssues",
        "viewProjectsHistoryAndTrends",
        "triageDefects"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "previewCommit",
          "displayName": "Preview Commit"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "classifyIssues",
          "displayName": "Classify Issues"
        },
        {
          "name": "viewProjectsHistoryAndTrends",
          "displayName": "View project history and dashboard"
        },
        {
          "name": "triageDefects",
          "displayName": "Triage issues"
        }
      ]
    },
    {
      "name": "observer",
      "displayName": "Observer",
      "description": "observer",
      "displayDescription": "View issues",
      "deletable": true,
      "editable": true,
      "permissions": [
        "viewDefects",
        "accessWebUI",
        "viewSource",
        "accessWS",
        "viewProjectsHistoryAndTrends"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "viewProjectsHistoryAndTrends",
          "displayName": "View project history and dashboard"
        }
      ]
    },
    {
      "name": "projectAdmin",
      "displayName": "Project Admin",
      "description": "projectAdmin",
      "displayDescription": "Create Projects, Component Maps & Triage Stores, Manage Attributes & Components",
      "deletable": true,
      "editable": true,
      "permissions": [
        "accessWebUI",
        "manageComponentMaps",
        "createProjects",
        "createComponentMaps",
        "createTriageStores",
        "accessWS",
        "manageAttributes"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "manageComponentMaps",
          "displayName": "Manage component maps"
        },
        {
          "name": "createProjects",
          "displayName": "Create projects"
        },
        {
          "name": "createComponentMaps",
          "displayName": "Create component maps"
        },
        {
          "name": "createTriageStores",
          "displayName": "Create Triage Stores"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "manageAttributes",
          "displayName": "Manage attributes"
        }
      ]
    },
    {
      "name": "serverAdmin",
      "displayName": "Server Admin",
      "description": "serverAdmin",
      "displayDescription": "Manage server settings",
      "deletable": true,
      "editable": true,
      "permissions": [
        "accessWebUI",
        "createUsersGroups",
        "accessWS",
        "manageUsersGroups",
        "manageRoleDefinitions",
        "manageServerParams"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "createUsersGroups",
          "displayName": "Create users and groups"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "manageUsersGroups",
          "displayName": "Manage users and groups*"
        },
        {
          "name": "manageRoleDefinitions",
          "displayName": "Manage role definitions*"
        },
        {
          "name": "manageServerParams",
          "displayName": "Manage server parameters"
        }
      ]
    },
    {
      "name": "streamAdmin",
      "displayName": "Stream Admin",
      "description": "streamAdmin",
      "displayDescription": "Create streams",
      "deletable": true,
      "editable": true,
      "permissions": [
        "accessWebUI",
        "viewComponentMaps",
        "accessWS",
        "createStreams"
      ],
      "displayPermissions": [
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "createStreams",
          "displayName": "Create streams"
        }
      ]
    },
    {
      "name": "testaaa",
      "displayName": "testaaa",
      "description": "aaaddd",
      "displayDescription": "aaaddd",
      "deletable": true,
      "editable": true,
      "permissions": [
        "createTriageStores",
        "accessWS",
        "classifyIssues",
        "createStreams",
        "manageServerParams",
        "manageHierarchies",
        "viewSource",
        "commitToStream",
        "createComponentMaps",
        "createUsersGroups",
        "viewIntegrityControl",
        "viewProjectsHistoryAndTrends",
        "triageDefects",
        "viewDefects",
        "manageProjects",
        "accessWebUI",
        "createProjects",
        "viewComponentMaps",
        "previewCommit",
        "manageUsersGroups",
        "manageRoleDefinitions",
        "manageAttributes",
        "manageStreams",
        "manageTriageStores",
        "manageComponentMaps",
        "viewGlobalDashboard"
      ],
      "displayPermissions": [
        {
          "name": "createTriageStores",
          "displayName": "Create Triage Stores"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        },
        {
          "name": "classifyIssues",
          "displayName": "Classify Issues"
        },
        {
          "name": "createStreams",
          "displayName": "Create streams"
        },
        {
          "name": "manageServerParams",
          "displayName": "Manage server parameters"
        },
        {
          "name": "manageHierarchies",
          "displayName": "Manage Hierarchies"
        },
        {
          "name": "viewSource",
          "displayName": "View source"
        },
        {
          "name": "commitToStream",
          "displayName": "Commit to a stream"
        },
        {
          "name": "createComponentMaps",
          "displayName": "Create component maps"
        },
        {
          "name": "createUsersGroups",
          "displayName": "Create users and groups"
        },
        {
          "name": "viewIntegrityControl",
          "displayName": "View Policy Manager"
        },
        {
          "name": "viewProjectsHistoryAndTrends",
          "displayName": "View project history and dashboard"
        },
        {
          "name": "triageDefects",
          "displayName": "Triage issues"
        },
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "manageProjects",
          "displayName": "Manage projects"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "createProjects",
          "displayName": "Create projects"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "previewCommit",
          "displayName": "Preview Commit"
        },
        {
          "name": "manageUsersGroups",
          "displayName": "Manage users and groups*"
        },
        {
          "name": "manageRoleDefinitions",
          "displayName": "Manage role definitions*"
        },
        {
          "name": "manageAttributes",
          "displayName": "Manage attributes"
        },
        {
          "name": "manageStreams",
          "displayName": "Manage streams"
        },
        {
          "name": "manageTriageStores",
          "displayName": "Manage Triage Stores"
        },
        {
          "name": "manageComponentMaps",
          "displayName": "Manage component maps"
        },
        {
          "name": "viewGlobalDashboard",
          "displayName": "View global dashboard"
        }
      ]
    },
    {
      "name": "wsReporter",
      "displayName": "Web Service Reporter",
      "description": "wsReporter",
      "displayDescription": "View issues, invoke web services",
      "deletable": true,
      "editable": true,
      "permissions": [
        "viewDefects",
        "accessWS"
      ],
      "displayPermissions": [
        {
          "name": "viewDefects",
          "displayName": "View issues"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        }
      ]
    }
  ],
  "code": null,
  "message": null
}
```
