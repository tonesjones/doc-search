---
title: "To install the Code Sight plug-in in Eclipse"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-install-the-code-sight-plug-in-in-eclipse.html"
content_id: "0zEF4Jj0dR8mnjhm_NHJnA"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:49.738462+00:00"
---

# To install the Code Sight plug-in in Eclipse

You can install the Code Sight plug-in for Eclipse via the web.

Make sure you have installed Eclipse, along with a code project to analyze.

Note:
You can read through this page, or you can watch a brief
[interactive lesson](https://www.iorad.com/player/1732258)
about how to install Code Sight in Eclipse.

1. Launch the Eclipse IDE.
2. Choose Help → Eclipse Marketplace.

   The Eclipse Marketplace dialog appears.
3. In the search field, enter `code sight (security)` and then click Go.
4. If the Black Duck Code Sight plug-in does not appear in this dialog, click Browse for more solutions.

   Eclipse opens a browser window. Scroll down in this window to see the Code Sight (Security) entry.

   Tip:
   You can find the Code Sight plug-in by searching the Eclipse Marketplace,
   <https://marketplace.eclipse.org>.
   The direct link to the Code Sight plug-in is <https://marketplace.eclipse.org/content/code-sight-security>.
5. Move your mouse over the Install widget. As the tooltips instruct you, drag the widget over a different Eclipse window,
   and then release the mouse button.

   Code Sight installs.
6. When Code Sight has finished loading, click Finish.

   Note:
   In certain releases, the Install dialog retains the Next button, and
   after you click Next, Eclipse displays the Install dialog’s Review Licenses panel.
   Accept the license agreement, and then click Finish.
7. At this point, Eclipse might display a Trust dialog that asks you to verify the unsigned content that you are installing.

   You can click Select All and then Trust Selected
   to proceed with the installation.

   Tip:
   In general, software obtained from the Eclipse web site is considered trustworthy, but you can
   set up Eclipse so that it skips this step. See the workaround described on the
   Code Sight Known Issues page (look for issue UD-11164 or UD-11467).
8. A dialog prompts you to restart the application. Click Restart Now.

   Figure 1. The Restart Now button
     
    [image: Restart Now to finish installation]

   After the IDE starts again, the Code Sight interface appears within it.
   To use Black Duck scan engines in Code Sight, you will need to
   authenticate yourself.
