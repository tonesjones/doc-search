---
title: "Enabling management of license term conflicts"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/enabling-management-of-license-term-conflicts.html"
content_id: "7DvGH~nLdtiPU2r5IB6AHA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:08.801368+00:00"
---

# Enabling management of license term conflicts

BOM Managers, and other users with the appropriate role, can view conflicts for a
license term using the **License Conflicts** tab in the *Project Version's*
**Legal** tab.

By default, these tabs are disabled. To enable this feature:

1. Use the System Setting page to enable the feature for all *future*
   projects.
2. Once future projects are enabled, use a project's **Setting** tab to enable
   the feature for a *current* project.

To enable license conflicts for future projects:

Use the System Settings page to enable the **Legal** and **License Conflicts** tabs
for all future projects.

1. Log into Black Duck with the System Administrator role.
2. Click [image: Admin icon] .
3. Select **System Settings**.
4. Click **Legal**.
5. Set the toggle located in the **License Conflicts** section to *Setting is
   enabled* to display the **Legal** and **License Conflicts** tabs.
   Enabling the setting will not take effect immediately for existing projects.

     
    [image: image]   

   Set the toggle located in the **License Conflicts** section to *Setting is
   disabled* to remove the **Legal** and **License Conflicts** tabs.
   Note that if you select to enable license term fulfillment, the **Legal** tab
   will appear, but the **License Conflicts** tab will not appear.

     
    [image: image]

## Enabling or disabling license conflicts for a specific project

If the system setting is not enabled prior to the creation of the Black Duck project, then the
setting must be set at the project level.

To enable or disable license term conflicts:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the **Settings** tab.

     
    [image: Project page Settings tab]
3. Do one of the following:

   - Enable the **Apply License Conflicts Data to Bill of Materials**
     option in the **License Conflicts** section.
   - Clear the option to disable this feature for this project.
4. Click **Save**.
