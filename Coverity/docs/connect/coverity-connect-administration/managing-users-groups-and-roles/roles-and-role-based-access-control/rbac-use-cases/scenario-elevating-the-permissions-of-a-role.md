---
title: "Scenario: Elevating the permissions of a role"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-elevating-the-permissions-of-a-role.html"
content_id: "GAebLpiUiZm1GJbagwK3Tw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:54.957327+00:00"
---

# Scenario: Elevating the permissions of a role

**Goal:** To use newly granted mid-level administrator privileges to assign Developer and
Committer roles to a user and to members of an LDAP group.

Note: This scenario's assumptions are not supported by Coverity releases older than
2021.06.

**Scenario assumptions:**

Portal server User A, a member of the Administrators group, has created a new global
role, *User Creator*. User A then created a (local) User B, and assigned the new
global User Creator role to this new user. User A also assigned the roles Project Admin
and Stream Admin to User B. These permissions have enabled User B to accomplish
mid-level administration tasks.

**Scenario procedures:**

1. User B creates local User C.
2. User B then creates Group G by importing an LDAP group. User B also imports
   Users L1 and L2, who are members of that LDAP group.
3. User B creates streams, a project, and a triage store for the software
   project.
4. User B gives Group G the Developer and Committer role on those
   objects.
5. User B gives User C the Developer and Committer role on those
   objects.
6. Now Users L1 and L2 can commit and triage defects in the new stream. So can
   User C.
