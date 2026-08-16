---
title: "Scenario: Managing roles through primary projects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-managing-roles-through-primary-projects.html"
content_id: "d39ub16FiVcgUpbnBn~Msg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:53.060933+00:00"
---

# Scenario: Managing roles through primary projects

**Goal:** To manage multiple projects that have the same access control restrictions
to avoid having to replicate access control settings on each project.

**Scenario assumptions:**

- SysAdmin is a user that exists in the system. This user
  has the Create projects and Manage users
  and groups permissions.
- ProductManager creates the following projects and
  associated streams:   
   [image: image]
- Multiple users exist on the system and will have access to one (or more) of
  the streams. (Users could alternatively be members of separate
  groups).

1. ProductManager creates a separate project called
   Primary Project that will manage all
   permissions.
2. ProductManager assigns all of the users a global role that
   includes the View project permission, but no stream
   permissions. (For example, Visitor).
3. ProductManager associates all of the streams with
   Primary Project and lists it as their primary parent.
   The streams now inherit access control settings from Primary
   Project and are associated with the other projects as stream
   links.
4. ProductManager assigns the appropriate roles for the users
   (or groups) on the Primary Project.
5. Because the role assignments in Primary Project cascade down
   to the streams, ProductManager does not need to manage
   stream permissions on ProjectA,
   ProjectB, or ProjectC.
