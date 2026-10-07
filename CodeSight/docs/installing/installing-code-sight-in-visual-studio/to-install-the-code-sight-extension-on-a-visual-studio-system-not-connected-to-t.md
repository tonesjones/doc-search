---
title: "To install the Code Sight extension on a Visual Studio system not connected to the Internet"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-install-the-code-sight-extension-on-a-visual-studio-system-not-connected-to-the-internet.html"
content_id: "WjpDsNUUQzXN69UMeyanCg"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.512822+00:00"
---

# To install the Code Sight extension on a Visual Studio system not connected to the Internet

If the system on which you want to run the Code Sight extension is not connected to the Internet—or in other words, is
*air-gapped*—then the steps to install it are a bit different from the standard steps.

Make sure you have installed Visual Studio, along with a code project to analyze.

1. On a system that *is* connected to the Net,
   navigate to the correct Visual Studio Marketplace site (see below), and download the VSIX installer for the Code Sight extension.
   Save this file to a portable storage device: For example, a thumb drive will do.

   Important:
   The Marketplace page shows one of three entries, depending on which release of Visual Studio you run:
   - If you run Visual Studio 2017, choose the installer for this version.
     In the Marketplace, this appears as Code Sight for VS 2017 (Security).
     *Visual Studio 2017 no longer updates Code Sight automatically:* You need to download the new VSIX file.

     This installer is named code-sight-vs2017-<Code Sight version number>.vsix.
     The direct link to the Marketplace page for these versions of Code Sight is <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vs2017>.

     Attention:
     Support for Visual Studio 2017 has been deprecated, and will be discontinued in a future release of Code Sight.
   - If you run Visual Studio 2019, choose the installer for this version.
     In the Marketplace, this appears as Code Sight for VS 2019 (Security).

     This installer is named code-sight-vs2019-<Code Sight version number>.vsix.
     The direct link to the Marketplace page for these versions of Code Sight is <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vs2019>.
   - If you run Visual Studio 2022, choose the installer for this more recent version.
     In the Marketplace, this appears as Code Sight for VS 2022 (Security) .

     This installer is named simply code-sight-vs2022-<Code Sight version number>.vsix.
     The direct link to the Marketplace page for the VS 2022 version of Code Sight is <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vs2022>.

   **Be careful:** The system might attempt to download this file
   as a zipped folder, without the .vsix filename extension.
   If it is not saved as a VSIX file, the installer will not run (and simply changing the file name will not work).
   To download correctly, right-click the download link, choose Save Target As,
   and then in the file dialog, type `.vsix` at the end of the folder name.
2. On the air-gapped system, save the VSIX file to a location you will remember.

   The Desktop/ folder is the most convenient location.

   Figure 1. Icon for installing the Code Sight extension
     
    [image: extension installer icon]
3. Make sure that Visual Studio *is not* running,
   and then double-click the installer icon.

   A VSIX Installer dialog appears.

   Figure 2. Installer dialog
     
    [image: VSIX Installer dialog]
4. Click Install.

   The VSIX Installer installs the extension.
5. Start Visual Studio.

   After the IDE starts again, the Code Sight interface appears within it.
   To use Black Duck scan engines in Code Sight, you will need to
   authenticate yourself.
