---
title: "Adding Coverity Desktop updates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-coverity-desktop-updates.html"
content_id: "yAnxYx0KZnowiSyPrTVV~A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:58.452628+00:00"
---

# Adding Coverity Desktop updates

If an incremental release of the Coverity Desktop product becomes available, you can
update the central download page with the new packages by completing the following:

1. Go to the <install_dir>/server/base/webapps/
   directory.
2. Remove the following files:

   1. In the downloads directory, remove the following files:
      - cov-desktop-eclipse-2026.6.0.zip
      - cov-desktop-windriver-2026.6.0.zip
      - cov-desktop-qnx-2026.6.0.zip
      - cov-desktop-microsoft-visual-studio-2026.6.0.zip (for Visual Studio
        versions 2008-2010)
      - Coverity.Desktop.vsix (for Visual Studio
        2013-2017)
   2. Remove the following directories:
      - coverity-desktop-eclipse/update
      - coverity-desktop-windriver/update
      - coverity-desktop-qnx/update
      - coverity-desktop-visual-studio/gallery
3. Download updated Eclipse, Wind River WorkBench, QNX Momentics, and Visual Studio
   .zip packages.
4. For Eclipse, Wind River, QNX, and Visual Studio versions 2008-2010, save the
   .zip packages in the
   <install_dir>/server/base/webapps/downloads
   directory.

   For Visual Studio 2013-2017, extract the
   cov-desktop-microsoft-visual-studio-gallery-2026.6.0.zip file. Then copy
   Coverity.Desktop.vsix into the
   downloads directory.

   Note: Coverity.Desktop.vsix is found in the
   extracted .zip package, under
   coverity-desktop-vs/gallery.
5. For Eclipse, unpack cov-desktop-eclipse-2026.6.0.zip, then move the extracted directories to
   coverity-desktop-eclipse/update.

   For Wind River, unpack cov-desktop-windriver-2026.6.0.zip, then move the extracted directories to
   coverity-desktop-windriver/update.

   For QNX, unpack cov-desktop-qnx-2026.6.0.zip, then move the extracted directories to
   coverity-desktop-qnx/update.

   For Visual Studio 2013-2017, copy the extracted gallery
   directory to
   coverity-desktop-visual-studio/gallery.

The user can now download the new versions of the plug-in files and also point at a new
version of the Eclipse update or Visual Studio 2013-2017 gallery site.
