---
title: "Setting up projects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-projects.html"
content_id: "cwGq_Q~UiSIoWFZagshWzw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:59.558171+00:00"
---

# Setting up projects

When you create a project, you give it a name and description. You can also assign RBAC
roles to it. For more information about roles and the permissions that are associated
with those roles, see Roles and role-based access control.

**To set up a project:**

1. In the Projects & Streams menu, click +Project.
   Coverity Connect displays a dialog with a name
   similar to New Project 141 and a Description field.

   1. You can either use the default name or create a new name.

      Important: Project names are case-sensitive
      and must be 1 - 256 characters. Project names can NOT contain the
      following special characters:
      - `:` (colon)
      - `*` (asterisk)
      - `/` (forward slash)
      - `\` (back slash)
      - `` ` `` (backtick)
      - `'` (single quote)
      - `"` (double quote)
   2. Select the Analysis License File, if necessary.
   3. Click Create.
2. Select the project, and in the Roles tab, select one or
   more groups.

   Note: Make sure that the roles assigned to that group are appropriate for the
   project. Click Edit to change the assigned roles. For
   guidance, see Assigning roles per project or stream.
3. If necessary, assign one or more streams to your project.

   From the Projects & Streams menu, select and drag one or more
   streams to the project.

   If you need to assign a new stream, see Setting up streams.
4. Click Done to save your changes and exit. If you need to
   change any of the information, click Edit in
   Project Details.

Note: To use local analysis, Coverity Desktop requires special projects to be created. For
more information, see Configuring Coverity Desktop and shared files through the Downloads page.
