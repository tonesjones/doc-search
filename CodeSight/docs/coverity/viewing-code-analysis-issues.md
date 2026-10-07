---
title: "Viewing Code Analysis Issues"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/viewing-code-analysis-issues.html"
content_id: "Cim8FssSr73SmQjx7mTzyw"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.394837+00:00"
---

# Viewing Code Analysis Issues

This document outlines how to view both local and remote Code Analysis issues detected by Code Sight. Users can utilize the **Local View** tab for local issues and the **Team View** for remote issues.

## Viewing Local Code Analysis Issues

Local Code Analysis issues are displayed in the **Local View** tab, allowing users to efficiently review and address issues found in their code. The Scan mode determines how these issues are analyzed and reported.

Figure 1. Local View showing Code Analysis issues  
 [image: Code Analysis issues in Visual Studio]

(Example from Visual Studio)

Figure 2. Local view showing Code Analysis issues  
 [image: Code Analysis issues in VS Code]

(Example from VS Code)

## Viewing Remote Code Analysis Issues

Remote Code Analysis issues are displayed in the Team View tab. In IntelliJ and Visual Studio Code, you can filter the issues displayed by the Coverity Connect server. In Visual Studio, highlighting a remote issue in Team View opens the Code Sight Triage panel for issue triage.

Figure 3. Issues detected by a Coverity server displayed in Team View  
 [image: Team view displaying remote Coverity issues]

**“Issues from” drop-down list**
:   Select a source server from the configured sources. To add a new source, choose Configure sources to access the Sources panel.

[image: image]
:   Click the Refresh icon to update the current issues list. Issues do not refresh automatically and can be updated by clicking the icon or selecting a different software-integrity product.

## Local View and Team View Issues List

The Issues list displays Code Analysis issues that Code Sight has found.

In Eclipse, IntelliJ, and Visual Studio (but not in VS Code), the list of issues is organized into the following columns (VS Code does display severities):

Severity
:   Icons in this column indicate the severity level of the issue:

    [image: image]  Audit

    [image: image]  Low

    [image: image]  Medium

    [image: image]  High

    [image: image]  Critical

Issue Type
:   A brief description of the issue that was found

Location
:   The name of the file and the line number where the issue was found.

First Detected
:   Indicates how long ago the issue was first detected.

## Issue Details

Code Sight displays issue details when you click to highlight an issue in the Issues list. The Issue Details panel also gives you access to a view titled Contributing Details.

When using Coverity Connect as your server, relevant links to Secure Code Warrior web pages can be displayed in the Team View, provided Secure Code Warrior is enabled on the server and you are running Coverity version 2023.12.0 or later.

Please see Issue Details: Coverity (SAST), Contributing Details: Coverity (SAST), and Issue Details: Rapid Scan Static.

## Code Sight Icons in the Editor

[image: image]  A diamond-shaped icon indicates the line where the issue was detected.

[image: image]  When the issue is selected, the diamond is a solid color.

[image: image]  A double diamond indicates that multiple issues (or events) appear on the same line of code.

[image: image]  A circular icon indicates a line that contains an event that contributed to an issue.
