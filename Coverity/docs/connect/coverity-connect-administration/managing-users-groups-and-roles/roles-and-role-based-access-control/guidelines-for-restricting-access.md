---
title: "Guidelines for restricting access"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/guidelines-for-restricting-access.html"
content_id: "FOaX1jUKkbWUhuNVschVcQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:55.564586+00:00"
---

# Guidelines for restricting access

Often it is necessary to restrict visibility of source and defects to specific users or
groups of users. RBAC can be configured to allow access to specific projects,
components, triage stores, or component maps. Usually, the simplest approach is to
choose one way to control access, and remove restrictions on other ways:

- If you choose to control access by project, then remove restrictions on
  access by components and triage stores.
- If you control access by components, then remove restrictions by projects and
  triage stores.
- If you control access by triage stores, then remove restrictions by projects
  and components.

Listed below are steps to control access by project. These steps are similar to
those for controlling access by components or triage stores.

1. Assign the Visitor role to the
   Users group at the Global level. This allows all
   users to login, but does not allow access to any projects, components, or
   triage stores.
2. Assign the Developer role to the
   Users group for every component and triage store.
   This removes restrictions on access by components and triage
   stores.
3. For each project, assign the roles to each specific user and group that needs
   access to the project. Depending on the access the user or group needs, you
   may assign the Developer role and/or other roles.
   This grants only the specific user or group access to the project.
