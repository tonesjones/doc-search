---
title: "Managing users"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-users.html"
content_id: "_3YmE670hwy_nEaSJ7ZOvA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:29.712453+00:00"
---

# Managing users

You manage users in Configuration > Users & Groups. If your user role has permission to manage users and groups, you can
add, delete, copy, import, and edit users. When adding and editing a user, you can
assign the user to a group and set one or more roles for the user.

Note: **Built-in users**

Coverity Connect automatically creates the
following users during the installation process:

- The admin user is the overall
  administrator for the system. This user cannot be deleted. Also, this user
  is outside of the scope of the RBAC feature.
- The reporter user is a specialized
  process (as opposed to an actual person) in the Coverity Connect system that
  collects nightly trend and metrics data.

  The reporter is assigned the System Report
  Generator role to streamline the trend data collection
  process. By default, the role assignment is global, meaning that the
  reporter collects data for all components,
  projects, and streams on your system. To change this default behavior, see
  Limiting the scope of data collection.
