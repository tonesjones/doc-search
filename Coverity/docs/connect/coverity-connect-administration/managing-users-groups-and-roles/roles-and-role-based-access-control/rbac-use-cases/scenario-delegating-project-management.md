---
title: "Scenario: Delegating project management"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-delegating-project-management.html"
content_id: "9SkZo~gv0MFFDee7nJFb3g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:51.701282+00:00"
---

# Scenario: Delegating project management

**Goal:** To delegate management of a project to that project's owner.

**Scenario assumptions:**

- ProjectManager exists on the system with a role that
  includes the Manage projects permission.
- user1 exists on the system.
- Project A exists on the system.

1. ProjectManager goes to Configuration > Projects & Streams.
2. ProjectManager edits ProjectA.
3. ProjectManager adds user1 to the
   project's Roles.
4. ProjectManager assigns the Project
   Owner role to user1 so that he/she is
   allowed to administer the project.

   Note: Roles can also be assigned to a user group that represents users that are the
   project's owners.
5. user1 logs into Coverity Connect and can create streams in
   ProjectA and assign roles to other users and groups in
   their respective projects.

Stream ownership can be delegated similarly to this procedure by assigning the Stream
Owner role.
