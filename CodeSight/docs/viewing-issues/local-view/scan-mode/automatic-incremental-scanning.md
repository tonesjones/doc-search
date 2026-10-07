---
title: "Automatic / Incremental scanning"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/automatic/incremental-scanning.html"
content_id: "IoVW14d_q_7~4LV~4GK3tw"
version: "2026.9.0"
section: "Viewing Issues in Code Sight"
scraped_at: "2026-10-06T23:39:51.691375+00:00"
---

# Automatic / Incremental scanning

In Local
View, when Automatic (or **Incremental** in VS Code) is the active scan mode,
Code Sight launches a scan for an individual
file whenever you open or save that file.

## Scanning Tools

An Automatic or Incremental scan can run one of the following
tools:

- Rapid Scan Static

  The Rapid Scan Static engine (also known as *Sigma)* must have been installed on your
  system. Rapid Scan Static is available if you have authenticated Coverity, Polaris, or the Code Sight Standard Edition.
- Signal (available only in VS Code)

  An advanced agentic scanning capability allowing
  developers to scan active files and code changes using improved analysis
  options, including dataflow detection and removing invalid or redundant
  findings, reducing the incidence of false positives.
- Snippet Analysis (available only in VS
  Code)

  Auto-scan can also run Snippet Analysis. You must first
  have enabled Snippet Analysis: See Snippet Analysis.

## Viewing Automatic or Incremental Scan Results

In VS Code, after running an Incremental Scan the results in
LOCAL VIEW are grouped into the following categories:

- **Secrets**: This category includes all static scan (SAST) issues
  related to hardcoded secrets found in the codebase.
- **Vulnerabilities**: This category contains static scan (SAST) issues
  related to security weaknesses in the codebase, excluding hardcoded
  secrets.
- **Licenses** (Not available with Signal
  AI Scans): This category lists issues identified through Source Code Analysis
  (SCA) related to licensing.

Figure 1. VS Code LOCAL VIEW after an Incremental Scan
  
 [image: VS Code LOCAL VIEW after an Incremental Scan sorts issues to categorize them as either Secrets or Vulnerabilities]

## See also

Analyze while you type

Incremental Scan Configuration tab for VS Code
