---
title: "Installing and updating Coverity Desktop for Visual Studio using a gallery"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-and-updating-coverity-desktop-for-visual-studio-using-a-gallery.html"
content_id: "y6lhfmoZJrfAR18ZA8yoYg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:56.622414+00:00"
---

# Installing and updating Coverity Desktop for Visual Studio using a gallery

You can use a private gallery in Visual Studio (by providing its location) to install
Coverity Desktop. This allows automatic updates for the Coverity Desktop plug-in from
within Visual Studio, whenever a new version becomes available on the Coverity Connect
server.

**To use this feature, complete the following steps:**

1. From the Coverity Connect Help menu, select Downloads.
2. Select Visual Studio from the IDE drop-down and copy the
   generated Gallery link.
3. In Visual Studio, navigate to Tools > Options > Environment > Extensions (for Visual Studio versions 2019, 2022)
   or
   Tools > Options > Environment > Extensions and Updates (for Visual Studio versions 2015, 2017).
4. Click the Add button, enter a name for the extension, and
   paste the copied Gallery link in the URL field. Then click
   Apply to save.
5. Click OK to close the options window.
6. Navigate to Extensions > Manage Extensions > Online (for Visual Studio versions 2019, 2022) or Tools > Extensions and Updates > Online (for Visual Studio versions 2015, 2017) and select the name you chose
   for the Gallery.
7. Click Download to download the latest version of the
   plug-in.

For information about adding a private gallery to Extensions and Updates
in Visual Studio, see

- <http://msdn.microsoft.com/en-us/library/hh266746.aspx> (Visual Studio 2015)
- <https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2017/extensibility/private-galleries?view=vs-2017> (Visual Studio 2017)
- <https://learn.microsoft.com/en-us/visualstudio/extensibility/private-galleries?view=vs-2019> (Visual Studio 2019)
- <https://learn.microsoft.com/en-us/visualstudio/extensibility/private-galleries?view=vs-2022> (Visual Studio 2022)

For more information about managing a private gallery by using registry settings, see

- <http://msdn.microsoft.com/en-us/library/hh266735.aspx> (Visual Studio 2015)
- <https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2017/extensibility/how-to-manage-a-private-gallery-by-using-registry-settings?view=vs-2017> (Visual Studio 2017)
- <https://learn.microsoft.com/en-us/visualstudio/extensibility/how-to-manage-a-private-gallery-by-using-registry-settings?view=vs-2019> (Visual Studio 2019)
- <https://learn.microsoft.com/en-us/visualstudio/extensibility/how-to-manage-a-private-gallery-by-using-registry-settings?view=vs-2022> (Visual Studio 2022)

Note: You can also install the Visual Studio plug-in from your local desktop by downloading
and running the Coverity.Desktop.vsix file from the Coverity
Connect Help > Downloads menu.
