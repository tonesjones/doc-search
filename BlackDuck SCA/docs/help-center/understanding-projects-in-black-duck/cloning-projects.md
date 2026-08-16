---
title: "Cloning projects"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/cloning-projects.html"
content_id: "~CgO0zH65UNdOtSGL2slOg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:01.942961+00:00"
---

# Cloning projects

Use project cloning to fork an existing project to a new project. Cloning helps reduce
your workload by using the data, analysis, and resolutions you defined in an existing
project as a baseline for a new project.

Users who can create projects can clone projects. For each project, select the versions
you wish to clone and the project's attributes, such as the project's settings or
project members and groups. Note that the attributes cloned for each project version
depend on the project
version cloning settings you selected, as shown in the **Cloning** section
in the **Project Details** section of the **Settings** tab:

  
 [image: Cloning Project Version Attributes]   

Note that unlike persistent edits which synchronizes edits made in one version to all
other versions of that project, edits made to the baseline project do not propagate to
the cloned project or its cloned versions. This gives you the ability to experiment with
the cloned project while keeping the original version intact.

To successfully use cloning:

1. Enable cloning, as described below.
2. Run a scan to the new project.

Cloned information appears in the cloned project versions for components that are the
*same* as in the original project version for this project. A scan will need to
be performed to replicate the components of the base project to the cloned project. If a
component is not included in the newly scanned files, then that component *will
not* be included in the new cloned project version. Cloned information
*will* appear in the cloned project version for components that were manually
added in the original project version.

## Enabling cloning

To clone a project:

1. Open the *Project Name*
   **Settings** tab for the project you wish to clone.
2. Click **Clone Project** in the **Clone Project** section.

   The Clone Project dialog box appears.

     
    [image: Clone Project Dialog Box]
3. Do the following:
   - Enter a name for this clone.
   - Select the versions you wish cloned.
   - Select what you would like to clone:
     - Additional Fields.
     - Application ID.
     - Members and Groups.
     - Settings. This option is selected by default. This includes
       the values of all attributes, excluding the project name,
       shown in the **Settings** section in the **Project
       Details** tab for this project.
4. Click **Clone**.
