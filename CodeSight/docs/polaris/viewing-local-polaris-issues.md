---
title: "Viewing local Polaris issues"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/viewing-local-polaris-issues.html"
content_id: "588L8w3QAH5z4086FoT72w"
version: "2026.9.0"
section: "Polaris with Code Sight"
scraped_at: "2026-10-06T23:39:54.997378+00:00"
---

# Viewing local Polaris issues

Locally detected issues display in Local View.

Polaris can also run SAST scans for local projects in
your development environment.

Figure 1. List of local SAST issues in VS Code
  
 [image: Local SAST issues in VS Code]

In JetBrains IDEs, Visual Studio, and VS Code, Polaris
can also run Black Duck SCA scans for local projects.

Figure 2. List of local SCA issues in VS Code
  
 [image: Local SCA issues in VS Code]

## Scan mode

See Scan mode.

## The Issues list

Lists Code Analysis issues that Polaris has found.

In JetBrains (including IntelliJ) and in Visual Studio, but *not* in VS Code,
the list of issues is organized into the following columns (VS Code does display
severities):

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

Code Sight displays issue details when you click to highlight an
issue in the Issues list. The Issue Details panel also gives you access to a view
titled Contributing Details.

Please see Issue
Details: Coverity (SAST), Contributing
Details: Coverity (SAST), and Issue Details: Rapid Scan Static.
