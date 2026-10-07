---
title: "To install the Code Sight plug-in on an IntelliJ system not connected to the Internet"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-install-the-code-sight-plug-in-on-an-intellij-system-not-connected-to-the-internet.html"
content_id: "zqDhRpSSO~6FApGaPSTvZQ"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.160148+00:00"
---

# To install the Code Sight plug-in on an IntelliJ system not connected to the Internet

If the system on which you want to run the Code Sight plug-in is not connected to the Internet—or in other words, is
*air-gapped*—then the steps to install it are a bit different from the standard steps.

Make sure you have installed your IDE, along with a code project to analyze.

1. On a system that *is* connected to the Net,
   navigate to the IntelliJ (JetBrains) Marketplace, and download the ZIP file of the Code Sight plug-in to
   a portable storage device: for example, a thumb drive will do.

   This file is named code-sight-intellij-<version number>.zip.
2. On the air-gapped system, save the ZIP file to a location you will remember.

   The Downloads/ directory is one possibility.

   Attention:
   You don’t have to unzip the ZIP file:
   The JetBrains IDEs can load the plug-in in its compressed form.
3. Start the IDE, then go to plug-in installation for the platform you are using.

   On Windows® or Linux® systems, the menu choice is
   File → Settings | Preferences → Plugins;
   on Mac® systems, the menu choice is
   IntelliJ IDEA → Preferences → Plugins.
4. In the Preferences dialog, go to the Plugins panel.
5. [image: Utilities icon]
    At the top of the Plugins panel, click the Utilities icon,
   then from the drop-down menu choose Install Plugin from Disk.

   The IDE displays a regular file dialog.
6. In the file dialog, navigate to the directory that contains the
   Code Sight ZIP file you saved. Click to highlight the ZIP file, and then click
   Open. 

   The IDE adds a “Code Sight (Security)” entry to the Plugins
   panel.
7. Both the plug-in entry and its information page include a button that says
   Restart IDE.
   Click one of those buttons.

   A dialog prompts you to confirm the restart.

   After the IDE starts again, the Code Sight interface appears within it.
   To use Black Duck scan engines in Code Sight, you will need to
   authenticate yourself.
