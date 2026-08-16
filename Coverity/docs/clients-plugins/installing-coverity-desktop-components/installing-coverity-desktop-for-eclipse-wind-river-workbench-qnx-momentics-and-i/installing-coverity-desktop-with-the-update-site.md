---
title: "Installing Coverity Desktop with the update site"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-desktop-with-the-update-site.html"
content_id: "QiOmwIeFtfnGgTt9v6IAVg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:53.364048+00:00"
---

# Installing Coverity Desktop with the update site

Through Coverity Connect you can set up an update site to install Coverity Desktop or
upgrade Coverity Desktop when the update site is updated with the new version.

1. Under the Coverity Connect Help menu, select
   Downloads.
2. Display the Classic Fast Desktop tab.
3. Use the IDE drop-down list to select your IDE.
4. Copy the URL associated with your IDE (Eclipse, QNX Momentics, Wind River, IBM RTC), or click
   the copy link icon.

   Note: This is the URL that your IDE will access to download
   Coverity plug-in updates. Ensure that it is accessible by your IDE. (It is not
   the same URL that the Coverity plug-in uses to communicate with Coverity
   Connect.)
5. In the IDE, go to Help > Install New Software...

   Note: For Wind River Workbench only, you must go to the Device
   Debug perspective to make sure that the Install New
   Software... is present in the Help menu.

   Additionally, do not
   use the Help > Install into Eclipse... option. This option does not install the Coverity
   plug-in.
6. Click the Add... button.
7. In the Location/Work with field, enter the update site URL
   and click OK.
8. Select Coverity DesktopC/C++ Analysis and Java Analysis (Eclipse only).
   - Coverity Desktop Java Analysis and C/C++ Analysis each allow you to view and
     triage Coverity issues in your project through central analysis.
   - Coverity Desktop Java Analysis allows you to run local analysis for Java
     Quality Defects and Security Risks.
   - Coverity Desktop C/C++ Analysis allows you to run local analysis for C/C++
     Quality Defects.
9. Click Next and review the Coverity Product License
   Agreement.

   Note: The installation step, "Calculating
   requirements and dependencies," can take a long time if there are invalid or
   slow URLs in the Available Software Sites list. To solve
   this, remove the offending URLs or uncheck the box labeled Contact
   all update sites during install to find required software.
10. Select the I accept the terms of the license agreement radio
    button.
11. Click Finish.

    Note: The installation process might take a long
    time to complete because Eclipse checks for updates for all of the selected
    update sites installed on your environment. To speed up the installation, you
    can go to Help > Software Updates > Available Software > Manage Sites. Uncheck all of the update sites except for
    cov-desktop-eclipse-2026.6.0.
    When you want to update other components, go to Manage Sites and select them
    again.
12. Click Restart Now to restart the IDE.
13. Set up your workspace preferences.

    For information about configuring Coverity
    Desktop, see the Coverity Desktop online help. To access the help, select Help > Coverity Help Center, then open Coverity 2026.6.0 for
    Eclipse, Wind River Workbench, and QNX Momentics: User
    Guide.
