---
title: "Scenario: Restricting project access for Coverity Desktop users"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-restricting-project-access-for-coverity-desktop-users.html"
content_id: "bXEWrMJ0_x_W5Mm1xcnVkw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:54.325831+00:00"
---

# Scenario: Restricting project access for Coverity Desktop users

**Goal:** To grant Coverity Desktop users access only to the Coverity Connect projects
to which they are assigned.

**Scenario assumptions:**

- ProjectManager exists on the system and has a role with
  the Manage project and Create
  project permissions.
- Multiple Coverity Desktop users exist on the system.

1. In the Roles tab, ProjectManager
   creates a new role, Desktop Developer, selects the same
   permissions that are assigned to the Developer role, and
   adds the Create Triage Stores permission.
2. ProjectManager creates a new Group,
   Group1, and adds the Coverity Desktop developers to the
   list of members.
3. In the Projects & Streams menu,
   ProjectManager creates a new Project,
   Project1, and adds Group1 with the
   Committer, Desktop Developer, and
   Triage Store Owner roles assigned.
4. In the Triage Stores menu,
   ProjectManager creates a Triage Store,
   TriageStore1, and adds Group1 with
   the Desktop Developer, and Triage Store
   Owner roles assigned.
5. In the Triage Stores menu,
   ProjectManager adds Group1, to the
   Default Triage Store and Empty Triage
   Store, with the Desktop Developer, and
   Triage Store Owner roles assigned.
6. In the Component Maps menu,
   ProjectManager creates a Component Map,
   CompMap1, and adds Group1 with the
   Committer, Desktop Developer, and
   Triage Store Owner roles assigned.
7. In the Component Maps menu,
   ProjectManager adds Group1, to the
   Default component map with the Desktop
   Developer and Triage Store Owner roles
   assigned.
