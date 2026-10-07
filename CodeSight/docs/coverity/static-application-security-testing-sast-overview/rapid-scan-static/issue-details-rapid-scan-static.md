---
title: "Issue details: Rapid Scan Static"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/issue-details-rapid-scan-static.html"
content_id: "mpxmqhUiR9K2BP9Cst9Gsw"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.700307+00:00"
---

# Issue details: Rapid Scan Static

The display of Rapid Scan Static issues is similar to that for Coverity
issues.

When you hover over an issue line that is highlighted in the Editor, a drop-down panel displays a summary of the issue that was found.

Figure 1. Drop-down panel for an SAST issue
  
 [image: Drop-down summary of an SAST issue in the VS Code editor]

Figure 2. Details drop-down panel for a Rapid Scan Static issue in the IntelliJ editor
[image: Drop=down summary for a Rapid Scan SAST issue in the IntelliJ editor]

To see a panel that shows further details about the issue, click the issue’s entry in the issues list.
The Issue Details panel includes the name of the checker that detected the issue.

Figure 3. Issue details for SAST issues in VS Code
  
 [image: View to show details of SAST issues in VS Code]

## Range highlighting

When Coverity (in-depth SAST) detects an issue, it simply highlights the line of code where the issue was first detected.

Rapid Scan SAST provides a more fine-grained display.
If the issue is confined to a single line, then in the editor Rapid Scan SAST highlights only that portion
of code that contains the issue.
On the other hand, if the issue spans several lines of code, Rapid Scan SAST highlights all the lines that
contribute to the issue.

Figure 4. Rapid Scan SAST highlights only part of a line
  
 [image: Rapid Scan SAST in VS Code editor: Only the value 'true' is highlighted.]

In the case above, only the value `true` is at issue.

Figure 5. Rapid Scan SAST highlights several lines
  
 [image: Rapid Scan SAST in VS Code editor: Several lines are highlighted]

The case above is a similar issue, but it involves a multiline field. All lines in the field are highlighted.

Figure 6. Multiline highlight in the IntelliJ editor
  
 [image: Rapid Scan SAST issue in IntelliJ editor: Several lines are highlighted]
