---
title: "To install the Code Sight plug-in on an Eclipse system not connected to the Internet"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-install-the-code-sight-plug-in-on-an-eclipse-system-not-connected-to-the-internet.html"
content_id: "eG4NArTkuiJz4LciLP2nzQ"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:49.822267+00:00"
---

# To install the Code Sight plug-in on an Eclipse system not connected to the Internet

If the system on which you want to run the Code Sight plug-in is not connected to the Internet—or in other words, is
*air-gapped*—then the steps to install it are a bit different from the standard steps.

Make sure you have installed Eclipse, along with a code project to analyze.

**Important:**

Depending on which choices you make when you install it, Eclipse requires one or more of the following components:

- C/C++ Development Tools
- Java Development Tools
- JavaScript Development Tools

When connected to the Internet, Eclipse downloads these dependencies automatically, if they are not already present.
If Eclipse can't install them itself, due to the lack of an Internet connection, you must install them yourself *before you install* the Code Sight plug-in.
If you don't, Eclipse will fail when you try to install Code Sight.

To install the missing dependencies, use this download site: <https://download.eclipse.org/releases/>,
and click on the release number that matches the version of Eclipse you are using.

Search for missing dependencies and install them:

- Search for `C/C++ Development Tools` to find missing CDT dependencies such as org.eclipse.cdt.core.
- Search for `Java Development Tools` to find missing JDT dependencies such as org.eclipse.jdt.core.
- Search for `JavaScript Development Tools` to find missing JSDT dependencies such as org.eclipse.wst.jsdt.core.

Attention:
This URL is managed by the Eclipse Foundation, not by Black Duck. It might be *subject to change*.

1. On a system that *is* connected to the Net, navigate to the GitHub page,
   <https://github.com/coverity/Code-Sight-for-Eclipse/releases>.
   Download the compressed file for the Code Sight plug-in to a portable storage device: for
   example, a thumb drive will do.

   - For a Windows system, click Source code (zip).

     The GitHub page downloads Code-Sight-for-Eclipse-<version_number>.zip.
   - For a macOS or Linux system, click Source code (tar.gz).

     The GitHub page downloads Code-Sight-for-Eclipse-<version_number>.tar.gz.
2. On the air-gapped system, save the compressed file to a location you will remember.

   The Downloads/ directory is one possibility.
3. Double-click the entry for the compressed file to extract its contents.

   This creates a subdirectory that has the same name as the compressed file, without the
   filename extension.

   You can uncompress to the same directory where you saved the compressed file.
4. Launch the Eclipse IDE.
5. Choose Help → Install New Software.

   Eclipse displays the Install dialog.

   Figure 1. Install dialog
     
    [image: Eclipse Install dialog]
6. In the Install dialog, click Add.

   Eclipse displays the Add Repository dialog.

   Figure 2. Add Repository dialog
     
    [image: Eclipse Add Repository dialog]
7. In the Add Repository dialog, click Local.

   Eclipse displays a regular file dialog.
8. In the file dialog, navigate to the uncompressed directory.
   Click to highlight this directory, and then click
   Open.

   The Add Repository dialog appears again, this time with its
   Location field naming the Code Sight subdirectory.
   After you click Add, Eclipse returns to the Install dialog.
9. In the main window of the Install dialog, click to turn on the check box next to the
   “Black Duck Code Sight” entry, then choose whether to analyze C/C++ code, Java code, or both languages.
10. Click Next.

    Eclipse loads the plug-in, which takes a few moments.
11. When Code Sight has finished loading, click Finish.

    Note:
    In certain releases, the Install dialog retains the Next button, and
    after you click Next, Eclipse displays the Install dialog’s Review Licenses panel.
    Accept the license agreement, and then click Finish.
12. At this point, Eclipse might display a Trust dialog that asks you to verify the unsigned content that you are installing.

    You can click Select All and then Trust Selected
    to proceed with the installation.

    Tip:
    In general, software obtained from the Eclipse web site is considered trustworthy, but you can
    set up Eclipse so that it skips this step. See the workaround described on the
    Code Sight Known Issues page (look for issue UD-11164 or UD-11467).
13. A dialog prompts you to restart the application. Click Restart Now.

    Figure 3. The Restart Now button
      
     [image: Restart Now to finish installation]

    After the IDE starts again, the Code Sight interface appears within it.
    To use Black Duck scan engines in Code Sight, you will need to
    authenticate yourself.
