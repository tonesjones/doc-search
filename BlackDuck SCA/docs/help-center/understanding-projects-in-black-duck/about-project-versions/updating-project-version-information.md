---
title: "Updating project version information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/updating-project-version-information.html"
content_id: "NsTUIvKQMsuxMM0xmpCk6Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:13.927044+00:00"
---

# Updating project version information

You can rename a project version and update the following information:

- Version
- License
- SCM Repository Branch

  Note: The SCM Repository Branch field is visible only if this feature is enabled in
  your environment. Manually changing the SCM branch name could break existing
  scans.
- Notes
- Nickname
- Release Date
- Phase
- Distribution
- Scan Retention
- Data Retention

  Note: This option is displayed only if the respective flag is set in your
  environment.

To update project version information:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name of the project that you want to manage.

   The **Components** tab
   for the version opens.

     
    [image: BOM page]
4. Select the **Settings** tab and select **Version Details** to update the
   version information.

   Note: The ability to delete a version is also available in the **Version
   Details** section, if there is more than one version of a project. You
   cannot delete a project version if that version is a subproject in a
   BOM: you must remove the project version from all BOMs before you can
   delete it. Select the **Details** tab to view where this project version is
   used as a subproject.
5. Click **Save**.

   Black Duck saves the project
   version information.
