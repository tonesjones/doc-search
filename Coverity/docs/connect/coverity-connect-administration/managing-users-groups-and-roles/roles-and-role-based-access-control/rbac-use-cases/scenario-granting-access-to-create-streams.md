---
title: "Scenario: Granting access to create streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-granting-access-to-create-streams.html"
content_id: "xiOVC4yCTEJpqMguu7rHSw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:53.686400+00:00"
---

# Scenario: Granting access to create streams

**Goal:** To allow other users to create streams in a project.

**Scenario assumptions:**

- ProjectManager exists on the system and has a role with
  the Manage project and Create
  project permissions.
- user1 and user2 exist on the
  system, both with a global Visitor role.

1. ProjectManager creates
   Project1.
2. ProjectManager goes to Configuration > Projects & Streams and edits Project1.
3. In the Roles tab, ProjectManager adds
   user1 and user2 and assigns them a
   role that includes the create stream permission (for
   example, Stream Admin).
4. user1 and user2 each creates a stream,
   and the system grants them the Stream Owner role for each stream that they have created.

   Attention:
   Stream names are case sensitive. Coverity would treat `stream1` and `Stream1` as two distinct streams.
