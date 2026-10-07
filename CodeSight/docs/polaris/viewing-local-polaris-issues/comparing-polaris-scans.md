---
title: "Comparing Polaris scans"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/comparing-polaris-scans.html"
content_id: "iwFL1pWLyF_Xy3mhYKgNdQ"
version: "2026.9.0"
section: "Polaris with Code Sight"
scraped_at: "2026-10-06T23:39:55.044996+00:00"
---

# Comparing Polaris scans

With Local View in JetBrains IDEs (including IntelliJ),
Visual Studio, and VS Code, you can compare the results of different Polaris scans.
For example, you might want to compare the issues found locally with those found on a server.

After you run a Polaris scan, Local View displays an entry above the issues list that reads
“Compare with: [configure]” in IntelliJ and Visual Studio, or “Compare with: [Not Configured]” in VS Code.

Figure 1. Polaris comparison not yet configured (IntelliJ)
  
 [image: The "Configure" field before choosing a scan to compare]

Click the “[configure]”/“[Not Configured]” field to display a drop-down menu of other local Polaris scans
that have already been run.

Figure 2. “Compare with” entry for Polaris scans in Local View
  
 [image: Comparison control for local Polaris scans]

Once you have chosen another Polaris scan for comparison.
In IntelliJ and Visual Studio, the choices appear on three buttons.

Figure 3. Buttons for filtering Polaris comparisons in IntelliJ
  
 [image: Choosing which comparison results to display in IntelliJ]

In VS Code, the choices appear in three icons that display
on a line labeled “Show”, which appears below the “Compare with” line.

[image: image]  Show All results shows all issues found by the local scan.

[image: image]  Show Absent results only shows issues that are absent in the
local scan but were found by the Compare With scan.

[image: image]  Show New results only shows issues that are present in the local scan but
absent in the Compare With scan.
