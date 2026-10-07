---
title: "Viewing Open Source Analysis issues"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/viewing-open-source-analysis-issues.html"
content_id: "g8NRttHbKqUCYn2fkGSd8w"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.437571+00:00"
---

# Viewing Open Source Analysis issues

Open Source Analysis (software composition analysis) issues display in the
Local View tab within Code Sight.

Figure 1. List of SCA issues in Local View in IntelliJ
  
 [image: Open Source Analysis issues in IntelliJ]

Figure 2. SCA issues in LOCAL VIEW in VS Code
  
 [image: LOCAL VIEW: VS Code display of SCA issues]

## Scan mode

See Scan mode.

## The Issues list

Lists issues that Code Sight has found.

In most supported development environments (but not in VS Code), the list of issues is organized into the following columns:

Severity
:   Icons in this column indicate the severity level of the issue:

    [image: image]  Low

    [image: image]  Medium

    [image: image]  High

    [image: image]  Critical

Component
:   The name of the source file where the issue was detected.

Location
:   The name of the project file where the issue was found.

First Detected
:   Indicates how long ago the issue was first detected.

## Issue Details

Code Sight displays issue details when you click to highlight an issue in the Issues list.
The Issue Details panel also gives you access to a dependency-tree view titled Contributing Details.

Please see Issue details: Black Duck SCA and
View dependencies: Black Duck SCA.
