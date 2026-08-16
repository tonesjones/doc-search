---
title: "Installing Coverity Desktop from your local desktop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-desktop-from-your-local-desktop.html"
content_id: "9nS4IKceG8f9LJ1YsN~ajA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:54.023221+00:00"
---

# Installing Coverity Desktop from your local desktop

1. Under the Coverity Connect Help menu, select
   Downloads.
2. Use the pull-down menu to select your IDE.
3. Download and extract your preferred package:

   For Eclipse
   :   cov-desktop-eclipse-2026.6.0.zip

   For Workbench
   :   cov-desktop-windriver-2026.6.0.zip

   For QNX Momentics
   :   cov-desktop-qnx-2026.6.0.zip

   For IBM RTC
   :   cov-desktop-ibmrtc-2026.6.0.zip
4. From the IDE, select Help > Install New Software.

   Note: For Wind River Workbench, you must go to the Device
   Debug perspective to make sure that the Install New
   Software... is present in the Help menu.

   Additionally, do not
   use the Help > Install into Eclipse... option. This option does not install the Coverity
   plug-in.
5. Click the Add... button.
6. Click Local and browse to your Coverity Desktop package
   directory:
   - <CD_package_dir>/cov-desktop-eclipse-2026.6.0
   - <CD_package_dir>/cov-desktop-windriver-2026.6.0
   - <CD_package_dir>/cov-desktop-qnx-2026.6.0
   - <CD_package_dir>/cov-desktop-ibmrtc-2026.6.0
7. Click OK for the Browse For Folder dialog.
8. Click OK for the Add Site dialog. In Eclipse 3.6, click
   OK for the Add Repository dialog.
9. Select Coverity DesktopC/C++ Analysis and Java Analysis (Eclipse only).
   - Coverity Desktop Java Analysis and C/C++ Analysis each allow you to view and
     triage Coverity issues in your project through central analysis.
   - Coverity Desktop Java Analysis allows you to run local analysis for Java
     Quality Defects and Security Risks.
   - Coverity Desktop C/C++ Analysis allows you to run local analysis for C/C++
     Quality Defects.
10. Click Next and review the Coverity Product License
    Agreement.
11. Select the I accept the terms of the license agreement radio
    button.
12. Click Finish.

    Note: The installation process might take a long
    time to complete because Eclipse checks for updates for all of the selected
    update sites installed on your environment. To speed up the installation, you
    can go to Help > Software Updates > Available Software > Manage Sites. Uncheck all of the update sites except for
    cov-desktop-eclipse-*. When you want to update other
    components, go to Manage Sites and select them again.
13. Click Restart Now to restart the IDE.
14. Set up your workspace preferences.

    For information about configuring Coverity
    Desktop, see the Coverity Desktop online help, or Coverity 2026.6.0 for Eclipse, Wind River Workbench, and QNX Momentics: User Guide.

    To access the help, select Help > Help Topics. In the Contents pane, select Coverity Desktop for use
    with Eclipse.
