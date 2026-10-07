---
title: "To install the Code Sight extension in Visual Studio"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-install-the-code-sight-extension-in-visual-studio.html"
content_id: "1HlBt3FuuiNRmo2jVyvDZg"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.459510+00:00"
---

# To install the Code Sight extension in Visual Studio

You can install the Code Sight extension for Visual Studio via the web.

Make sure you have installed Microsoft Visual Studio, along with a code project to analyze.

Attention: The steps to install Code Sight as an extension to Visual Studio are
*not the same* as the steps to install the Code Sight extension within Visual Studio Code.

Note:
You can read through this page, or you can watch a brief
[interactive lesson](https://www.iorad.com/player/1711416)
about how to install Code Sight in Visual Studio.

1. Start Visual Studio.
2. Choose Extensions → Manage Extensions.
   (In versions of Visual Studio prior to Visual Studio 2019, this command appears as Tools → Extensions and Updates.)
3. In the left-hand column of the Extensions and Updates dialog, click Online.
   Make sure that Visual Studio Marketplace is active; click its entry if you need to.
4. In the search field, enter `Code Sight (Security)` to locate Black Duck Software, Inc. extensions.

   Important:
   The Marketplace page can show one of three entries, depending on which release of Visual Studio you run:
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

   Tip:
   You can find the Code Sight extension for Visual Studio by searching the
   Visual Studio Marketplace,
   <https://marketplace.visualstudio.com>.
5. Click the appropriate Black Duck Code Sight entry to highlight it, and then click Download.

   A notice confirms the download.

   Figure 1. Download confirmation
     
    [image: Notice to close Visual Studio so update can complete]
6. Click Close to exit the Extensions and Updates dialog.
7. Close Visual Studio.

   Now a VSIX installer icon appears on the taskbar.

   Figure 2. VSIX installer icon on the taskbar
     
    [image: VSIX installer icon on the taskbar]

   A VSIX Installer dialog opens shortly after that.

   Figure 3. VSIX Installer dialog
     
    [image: VSIX Installer dialog for Code Sight]
8. In the VSIX Installer dialog, click Install.

   The VSIX Installer installs the extension.
9. In the VSIX Installer dialog, click Close.
10. Start Visual Studio once again.

    After the IDE starts again, the Code Sight interface appears within it.
    To use Black Duck scan engines in Code Sight, you will need to
    authenticate yourself.
