---
title: "Scenario: Limiting access for project and stream administration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-limiting-access-for-project-and-stream-administration.html"
content_id: "Dp6NP0zJartxA5QeKdPcxg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:52.321307+00:00"
---

# Scenario: Limiting access for project and stream administration

**Goal:** To allow project owners to create and configure their own projects/streams,
but to not be able to access other owner's projects/streams.

**Scenario assumptions:**

- Admin exists on the system with a role that includes the
  Manage users and groups permission.
- user1 and user2 exist in the system
  and are designated to be project owners.

1. Admin assigns user1 and
   user2 the Project Admin role at the global level.

   This role has a Create projects global permission, but no
   project or stream-level permissions.
2. user1 creates a ProjectA and is given
   the Project Owner role on that project by the system.
3. user2 creates a ProjectB and is given
   the Project Owner role on that project by the system.
4. user1 creates several streams, adds users to
   ProjectA, and assigns them the Stream Owner role on
   those streams.
5. user2 also creates several streams, adds users to
   ProjectB, and assigns them the Stream Owner role on
   those streams.
6. user1 cannot add any streams that exist in
   ProjectB, because user1 does not
   have the Manage stream for those streams.

   The same is true for user2 regarding the streams in
   ProjectA.
7. The users in each project cannot add streams to their respective projects,
   because they do not have the Manage project or
   Create streams permissions.
