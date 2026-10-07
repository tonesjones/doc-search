---
title: "Manual scanning workflow"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/manual-scanning-workflow.html"
content_id: "mYczEvSwATcrog1NH9IJYg"
version: "2026.9.0"
section: "Viewing Issues in Code Sight"
scraped_at: "2026-10-06T23:39:52.002513+00:00"
---

# Manual scanning workflow

## Workflow in JetBrains IDEs, Eclipse, and Visual Studio

If no scan configuration yet exists when you start IntelliJ or another JetBrains
IDE, Eclipse, or Visual Studio, Local View shows an
Edit configurations button in the bar at top.

Click Edit configurations to open a Scan Configurations dialog where you can create new configurations.

Once you have created at least one scan configuration, the control that displayed Edit configurations changes to
a drop-down menu. When not expanded, it displays the currently active configuration. When expanded, it displays configurations to choose from.
Edit configurations remains a choice.

Figure 1. Scan configurations drop-down menu
  
 [image: Scan configuration choices in IntelliJ]

- [image: image] When you have chosen a scan configuration, click the
  Run Scan icon to run a scan.
- [image: image] When you have run more than one type of scan,
  you can click the “clock face” icon to choose which set of previous scan results you want to view.

  Figure 2. Scan results drop-down menu
    
   [image: Scan results choices in IntelliJ]

  Attention:
  A blinking orange dot can appear on the clock face icon. This
  indicates that new results are available for a scan that you are not currently
  looking at—in other words, for a scan that has been running in the
  background.

  If you move your mouse to hover over the icon, a tooltip will
  mention this, and if you click to open the drop-down clock menu, the entry for
  the new scan will be prefixed with ‘(new)’.

## Workflow in VS Code

- [image: image] In Local View,
  the first time you click Run Scan, Code Sight displays a drop-down menu
  that prompts you to create a scan configuration.

Figure 3. Menu for a new scan configuration
  
 [image: Drop-down menu in VS Code prompts to create a new scan configuration]

Click Configure scan to open a Scan Configuration tab that lets you
create a configuration.

Once you have created scan configurations, they appear in the Scan Configuration controls and also in the drop-down menu.

Figure 4. VS Code menu with scan configurations to choose
  
 [image: Menu showing configured scans in VS Code]

Click the name of a scan configuration to run that particular scan. Issues found by the scan appear in the Local View list.
When you click an issue in Local View, VS Code displays the code location and issue details as it did in the views from
older Code Sight versions.
