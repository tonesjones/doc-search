---
title: "Assigning roles to a component map"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assigning-roles-to-a-component-map.html"
content_id: "9PmpMcOjTaWpxFxL4tEcnQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:20.921790+00:00"
---

# Assigning roles to a component map

A user or a group can be assigned one or more roles that specify permissions regarding a
component map (or other features in the Coverity Connect UI).

- To add a component map, a user or group must have the Create Component
  Maps permission. The System Admin. and Project Admin. roles have
  this permission by default.
- To delete a component map, a user or group must have the Manage
  Component Maps permission. The System Admin. and Component Map
  Owner roles have this permission by default.
- To associate a stream with a component map, a user or group must have the
  Manage Streams permission for that particular stream.
  The user or group also must have one of the following permissions for the
  component map:

  - Manage Component Maps
  - View Component Maps
- To be able to associate a component map with a stream, a user (or a group to
  which the user belongs) requires View/Manage Component Maps permission at the
  global level (which gives View/Manage access to all component maps); or at a
  separate, lower level, to the specific component map.

  To use the permission at a lower level, you might add a user or group role to the
  component map, assigning View/Manage Component Maps permission to that new
  role.
- To make sure that a user designated as a Stream Owner can view the component map
  associated with the stream, make sure the user (or a group that includes the
  user) has View Component Maps permission for that component map.

For a visual summary of the built-in roles that have these permissions by default, see
Figure 1.
