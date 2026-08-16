---
title: "Enabling role-based access control over component maps"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-role-based-access-control-over-component-maps.html"
content_id: "fXobXnNHFd8DH4Auz29MSg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:56.189860+00:00"
---

# Enabling role-based access control over component maps

Just like projects, streams, triage stores, and components, customers can enforce
role-based access control (RBAC) over component maps.

Two permissions relate to component maps: View Component Maps and Manage Component Maps.
Anyone who has these permissions is given access to the Configuration > Component Maps menu. Giving a user or a group component map permissions at the global
level allows the user to see all component maps, excepting component maps for which the
user or group is assigned the No Access role at the component map level.

Customers who wish to only give component map View/Manage permissions on a per-map basis
will have to run the following one-time steps upon upgrade to Coverity Connect 2021.06
or a later version:

**To enable RBAC for component maps:**

1. At the user level, remove the role assignment that contains the Manage Component
   Maps permission.
2. For all non built-in roles that have Create Streams or Manage Streams permission,
   remove the View Component Maps permission.
3. For each Project Administrator, remove the Manage Component Maps
   permission.
4. For each user who needs to be able to create a component map, assign a global
   role that includes Create Component Maps among its permissions.

   For example, this might be the built-in Project Administrator role.
5. For each existing component map, use the following guidelines to update role
   assignments.

   For an imaginary Project X, you might set the roles as follows:

   - The manager of the team has a Component Map Owner role for each component
     map that the project uses.
   - Each member of the team has a Component Map Viewer role for each
     component map that the project uses.

   Each time you add a component map, update the role assignments in the same
   way.  For example, when you add a new map to the imaginary Project X, you
   might set the roles as follows:

   - Assign the manager of the team to be the Component Map Owner of the new
     component map.
   - Assign each member of the team to be a Component Map Viewer of the new
     component map.

To summarize, the following are the general guidelines to enforce RBAC on a per component
map basis:

**General guidelines for RBAC management of component maps:**

1. To prevent them from seeing all component maps, ensure no users or groups are
   given component map permissions at the global level.

   We recommend that you check any roles you are assigning at the global level to
   make sure they don't have component map permissions.
2. Go to Configuration > Component Maps, and select the component map for which you would like to control
   permissions.
3. On the right, select the Roles tab for your component
   map.
4. Add the user or group to which you would like to give component map access, and
   assign them an appropriate role.

   You can use the built-in Component Map Viewer role to give the permission to view
   component maps, or you can use the built-in Component Map Owner role to give the
   permission to manage component maps. Alternatively, you can create a custom role
   that has component map permissions, and use that.
