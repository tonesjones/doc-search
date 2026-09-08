---
title: "API Keys Administration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/api-keys-administration.html"
content_id: "JgcBQrdHVzjVVMdLtsi20w"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:54.411910+00:00"
content_hash: "8f2e73d805bca0c8b752cb2fcc0fd3a6e4be0d32013d617ee0484a1a55f112e4"
---

# API Keys Administration

API Keys can be generated for use with the Software Risk Manager API. Typically one key
would be generated for a specific purpose, such as integrating with a specific tool or
plugin. This would allow for fine-grained control over each API key’s active/inactive
state, as well as setting specific user roles for each key. In addition, API keys can be
subject to expiration (default is 90 days).

Click the Settings icon in the navigation bar and select API Keys from the top menu to
open the API Keys page.

[image: image]

This page lists the currently assigned API keys, shows when they were last active, and if
they are currently active.

Note: For more information on Software
Risk Manager API capabilities, please refer to the *Software Risk Manager API
Guide*.

For more information on administering API keys, see the following topics:

- Viewing existing API keys
- Creating an API key
- Editing an API key
- Regenerating an API key
- Deleting an API key

## Viewing Existing API Keys

**To view a list of existing API keys:**

1. Click the Settings icon in the navigation bar and select API Keys from the
   left menu.

   [image: image]

   This page a list of existing API keys, the date of the most recent
   activity, and whether the key is active.
2. Use the filter field to search for a specific API key or click the column
   headings to re-sort the list.

## Creating an API Key

**To create an API key:**

1. Click the Settings icon in the navigation bar and select API Keys from the
   left menu.

   [image: image]
2. Click Create New Key.

   [image: image]
3. Enter a name for the new API Key.
4. Select an expiration. (The default is 90 days.)
5. Configure global permissions and project roles as needed.

   Click on a role
   to select it. Click Clear to remove all selections.

   **Global
   Permissions.** Select global permissions for the new user.
   - **Administrator.** Grants user admin privileges. Admin users
     inherit all roles.
   - **Project Administrator.** Allows the user to create a new
     project.
   - **Integrations Administrator.** Allows user to manage
     centralized project configuration.
   - **Integrations User.** Allows user to create centralized
     project configuration. One user cannot see another user's
     connection configurations.
   - **Policy Administrator.** Allows user to create polices.
   - **API Key Administrator.** Allows user to manage API
     Keys.
   - **Project Viewer.** Allows user to view all projects.

   **Project Roles.** Select permissions for individual projects.
   - **Read**. The user or user group can see the specified
     project and all of its contents. If a user doesn't have the
     *Read* role for a particular project, that project will
     not appear in the *Project List* page for that user.
   - **Update**. The user or user group can change the finding
     status and comment on findings for the specified project.
   - **Create**. The user or user group can create new analyses
     for the specified project
   - **Manage**. The user or user group can manage the specified
     project's configuration (e.g., Git, Issue tracker, etc.). The
     *Manage* role also allows the user to delete the
     specified project.
6. Click Create API Key.

## Editing an API Key

**To edit an API key:**

Note: The API token expiration cannot be edited; however, regenerating an API key
allows you to set a new expiration.

1. Click the Settings icon in the navigation bar and select API Keys from the
   left menu.

   [image: image]
2. Click the dropdown configuration icon and select Edit API Key.

   [image: image]

   This opens the "Edit API Key" window.

   [image: image]
3. Configure global permissions and project roles as needed.

   Click on a role
   to select it. Click Clear to remove all selections.

   **Global
   Permissions.** Select global permissions for the new user.
   - **Administrator.** Grants user admin privileges. Admin users
     inherit all roles.
   - **Project Administrator.** Allows the user to create a new
     project.
   - **Integrations Administrator.** Allows user to manage
     centralized project configuration.
   - **Integrations User.** Allows user to create centralized
     project configuration. One user cannot see another user's
     connection configurations.
   - **Policy Administrator.** Allows user to create polices.
   - **API Key Administrator.** Allows user to manage API Keys.
   - **Project Viewer.** Allows user to view all projects.

   **Project Roles.** Select permissions for individual projects.
   - **Read**. The user or user group can see the specified
     project and all of its contents. If a user doesn't have the
     *Read* role for a particular project, that project will
     not appear in the Projects page for that user.
   - **Update**. The user or user group can change the finding
     status and comment on findings for the specified project.
   - **Create**. The user or user group can create new analyses
     for the specified project
   - **Manage**. The user or user group can manage the specified
     project's configuration (e.g., Git, Issue tracker, etc.). The
     *Manage* role also allows the user to delete the
     specified project.
4. Click Save.

## Regenerating an API Key

**To regenerate an API key:**

1. Click the Settings icon in the navigation bar and select API Keys from the
   left menu.

   [image: image]
2. Click the dropdown configuration icon and select Regenerate API Key.

   [image: image]

   This opens the "Regenerate Key" window.

   [image: image]
3. Select an expiration period and click Regenerate API Key. (The default is 90
   days.)
4. Copy and save the new API key and click Close.

## Deleting an API Key

**To delete an API key:**

1. Click the Settings icon in the navigation bar and select API Keys from the
   left menu.

   [image: image]
2. Click the dropdown configuration icon and select Delete API Key.

   [image: image]
3. Click Delete to confirm.
