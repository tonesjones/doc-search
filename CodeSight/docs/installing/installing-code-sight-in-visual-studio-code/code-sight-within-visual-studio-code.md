---
title: "Code Sight within Visual Studio Code"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-within-visual-studio-code.html"
content_id: "4mYWxr2pl7~Mdi~biII9dQ"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.980151+00:00"
---

# Code Sight within Visual Studio Code

Once installed in Visual Studio Code, the Code Sight interface
appears in a tabular view.

  
 [image: Code Sight controls inside VS Code]   

- [image: image] To
  see the Code Sight controls, click the sidebar icon that shows the
  Black Duck logo.
- While the extension is active, the Code Sight panel appears at the
  left of the VS Code window. It displays various views that are described in more
  detail below:
  - LOCAL VIEW
  - TEAM VIEW
  - STATUS
  - HELP
- In the code editor, icons next to line numbers show Code Analysis (SAST) issues and
  other findings. A line of code that has an SAST issue is highlighted. When an SAST
  issue is highlighted, details about it display in their own editor tab.

## SAST issue details

In the Editor, when you hover your mouse over an issue’s line of code, Code Sight displays a drop-down panel with a summary of the issues that
were detected.

Figure 1. Details drop-down panel in Visual Studio Code
  
 [image: Details drop-down panel in the VS Code editor]

To see a more detailed description, click the issue’s entry in the LOCAL VIEW.
Code Sight displays an “Issue Details” tab with a full
description of the issue that was found.

Figure 2. Issue details for SAST issues in VS Code
  
 [image: View to show details of SAST issues in VS Code]

Figure 3. Issue details for SCA issues in VS Code
  
 [image: View to show details of SCA issues in VS Code]

## LOCAL VIEW

The LOCAL VIEW displays issues found by scan engines installed locally on your
system. You can use *scan configurations* to set up these scans: See Local View.

Figure 4. LOCAL VIEW in VS Code
[image: LOCAL VIEW in the Code Sight panel in VS Code]

When you hover over LOCAL VIEW, Code Sight displays some icons that
let you search and manage this view:

Figure 5. Search and management icons for LOCAL VIEW
  
 [image: In VS Code, for sorting SAST issues]

- [image: image]
  Click the Search Results icon to search items in this
  view’s list.
- [image: image] Click the Sort Results icon to display a drop-down
  menu that lets you choose other criteria for sorting or filtering issues.

  Figure 6. Drop-down menu to choose a criterion in LOCAL VIEW
    
   [image: LOCAL VIEW issue-sorting options]

  The sorting options don’t have a counterpart in the versions of
  Code Sight for other IDEs. You can use the search field
  at the top of this drop-down menu to find a sorting option quickly.
- [image: image] Click the Run Scan icon to run a new scan.
- [image: image] Click the Open Scan Configuration icon to create,
  delete, or otherwise manage scan configurations.

## TEAM VIEW

The TEAM VIEW displays issues found by scans that run on remote servers. Such scans
can include Coverity Connect / Coverity on
Polaris, Polaris,
and Software Risk Manager.

Figure 7. TEAM VIEW in VS Code
[image: TEAM VIEW in the Code Sight panel in VS Code]

When you hover over TEAM VIEW, Code Sight displays some icons that
let you search and manage this view:

- [image: image] Click the Refresh remote results icon to update the
  current issues list.
- [image: image] Click the Show Team View Filters icon to display issue
  filters for the currently active server.
- [image: image] Click the Sort Results icon to display a drop-down
  menu that lets you choose other criteria for sorting or filtering issues.

  Figure 8. Drop-down menu to choose a criterion in TEAM VIEW
    
   [image: TEAM VIEW issue-sorting options]

  The sorting options don’t have a counterpart in the versions of
  Code Sight for other IDEs. You can use the search field
  at the top of this drop-down menu to find a sorting option quickly.
- [image: image] Click the Open Team View Configuration icon to open
  the Team View Configuration tab.
- [image: image] Click the Collapse All icon to collapse all issue
  entries that might have been expanded.

## STATUS view

In the STATUS view in the left-hand side bar, shortcut icons help you view and
manage the Scan Status panel and the Authentication pages.

Figure 9. STATUS VIEW in VS Code
[image: STATUS VIEW in the Code Sight panel in VS Code]

- [image: Products & Licenses icon]
  Products and Licenses

  Click to configure Black Duck scan engines. See
  Authenticating and installing: Products and Licenses panel.
- [image: Code Sight Settings icon]
  Code Sight Settings

  Click to display the Settings tab.
- [image: Edit Server Settings icon]
  Edit Server Settings

  Appears to the right when you hover over one of the server entries below the
  Server Connections label in the STATUS view.
  Click it to display the Authentication page, where
  you can change the server being used, the current Code Sight
  user, or both.

## HELP view

The HELP view in the left-hand side bar provides a few useful links to web pages,
and an Export Logs option.

Figure 10. HELP view
  
 [image: HELP view: web links and an Export Logs control]

Export Logs
:   Click the **Export Logs** text to display an Export Logs page with an
    Export Logs button that you can click to save a
    zipped file of the current scan logs.

    Exporting logs can be helpful when
    you need to troubleshoot a problem by working with Black Duck Support. After export, you can attach the
    logs file to your Support request.
