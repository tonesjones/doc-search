---
title: "Managing Project Groups"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-project-groups.html"
content_id: "x6HZbensNSE90CmM~pNQww"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:17.858380+00:00"
---

# Managing Project Groups

Black Duck provides the ability to logically group all your projects in the Hub, allowing
you to organize which projects belong to which business unit making it easier for you to
view risk across the organization. Project groups can contain both projects and other
project groups to provide a multi-level hierarchy.

To manage project groups:

1. Log in to Black Duck SCA.
2. Click [image: image] and select **Project
   Groups**.

From the Project Group Management page, you will see the root project group for all
projects and groups.

  
 [image: image]

## Project Group Hierarchy

The top level of the hierarchy, or the root level, is the main level for all
subsequent projects and project groups for your organization. By default, it is
named "Black Duck Project Groups", but can be changed at any time.

  
 [image: image]

### Ancestor, Parent, and Child Projects and Project Groups

In the example above, you can see a number of levels which may act as individual
projects or other project groups. Projects 1, 2, and 3 are considered children
of the root level project group. The same can be said for Project 4 and Project
5 in relation to Project 3. Project 5 is also a child of Project 4.

The inverse relationship is called a parent. For example, Project 4's parent is
Project 3 and Project 5's parent is Project 4.

An ancestor is any project group existing above the parent for that project
group. Project 3 is an ancestor of Project 5.

### Members and User Groups

The relationship between projects and project groups matters when assigning
members and user groups to project groups. Members and user groups can be
assigned to project groups with any number of roles. That assignment will give
those users access to the project or project group they are directly assigned to
(Direct Access), and to all child projects and project groups of that group with
the specified roles unless that assignment is explicitly overridden at the lower
levels (Indirect Access). This concept allows for setting users with default
access to projects that haven't been created yet. For more details regarding
user roles, see Understanding roles.

  
 [image: image]   

In the example above, users Bom and Copyright have been added as members with
Direct Access. The sysadmin user is a member of the root level project group,
therefore has Indirect Access to all child projects and project groups,
including Project 3.

  
 [image: image]   

As a result, users Bom and Copyright now have Indirect Access to Project 4 as
seen above. This extends to all children of Project 3. They will hold the same
role for all child projects and project groups of Project 3.
