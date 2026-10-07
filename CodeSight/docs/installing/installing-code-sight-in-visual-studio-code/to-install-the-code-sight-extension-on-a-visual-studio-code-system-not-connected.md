---
title: "To install the Code Sight extension on a Visual Studio Code system not connected to the Internet"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-install-the-code-sight-extension-on-a-visual-studio-code-system-not-connected-to-the-internet.html"
content_id: "h0je3r230nGOlQ1G43Uk4A"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.907718+00:00"
---

# To install the Code Sight extension on a Visual Studio Code system not connected to the Internet

If the system on which you want to run the Code Sight extension is not connected to the Internet—or in other words, is
*air-gapped*—then the steps to install it are a bit different from the standard steps.

Make sure you have installed Visual Studio Code, along with a code project to analyze.

1. On a system that *is* connected to the Net,
   navigate to <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vscode>,
   and download the VSIX installer for the Code Sight plug-in.
   Save this file to a portable storage device: for example, a thumb drive will do.

   This installer is named blackduck.code-sight-vscode-<Code Sight version>.vsix.

   **Be careful:** The system might attempt to download this file
   as a zipped folder, without the .vsix filename extension.
   If it is not saved as a VSIX file, the installer will not run (and simply changing the file name will not work).
   To download correctly, right-click the download link, choose Save Target As,
   and then in the file dialog, type `.vsix` at the end of the folder name.
2. On the air-gapped system, save the VSIX file to a location you will remember.

   The Desktop/ folder is the most convenient location.
3. If it is not already running, start Visual Studio Code.
4. In the activity bar at the left of the VS Code window, click the Extensions button.

   Figure 1. Extensions button
     
    [image: VS Code Extensions button]
5. At the top of the EXTENSIONS view, click Views and More Actions (the ... icon),
   and choose Install from VSIX... from the drop-down menu.

   VS Code opens a standard file dialog.
6. In the file dialog, click to highlight the VSIX installer, and then click Install.

   The VSIX installer installs the extension.
7. [image: image] In the left-hand sidebar, click the icon with the Black Duck logo
   to see the Code Sight controls and begin scanning your code.
