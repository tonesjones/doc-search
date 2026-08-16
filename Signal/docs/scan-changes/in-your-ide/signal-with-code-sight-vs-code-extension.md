---
title: "Signal with Code Sight VS Code Extension"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-with-code-sight-vs-code-extension.html"
content_id: "fPSXTYIaVYKVGJI3EoHgUQ"
version: "latest"
section: "Scan your code changes"
scraped_at: "2026-08-13T00:04:53.211523+00:00"
---

# Signal with Code Sight VS Code Extension

The Code Sight VS Code extension features [Signal](https://documentation.blackduck.com/bundle/signal/page/Signal_docs/topics/c_signal_overview.html), an advanced agentic
scanning capability within Incremental Scan mode. This enhancement allows developers to scan
active files and code changes using improved analysis options, including dataflow detection
and removing invalid or redundant findings, reducing the incidence of false
positives.

## Signal Support

- **Agentic Code Analysis:**
  Signal offers advanced, context-aware
  analysis that evaluates both active files and code changes. This feature
  helps developers identify potential issues in real-time as they code,
  ensuring that problems are caught early in the development process.
- **Dataflow Detection:** This capability focuses on identifying issues
  related to dataflow across function or method boundaries. By analyzing how
  data moves through the code, Signal can
  highlight potential vulnerabilities or inefficiencies that may arise from
  improper data handling, allowing developers to make informed decisions about
  their code structure.
- **Oversight:**
  Signal includes an intelligent oversight
  system that automatically filters out non-critical findings. By minimizing
  false positives, this feature helps developers prioritize their efforts on
  significant issues that could impact the application’s security or
  performance, streamlining the debugging process.

## Prerequisites

- **Black Duck LLM Key:** This key is essential for
  accessing Signal’s capabilities. You can obtain your Black Duck LLM Key from your Black Duck fulfillment team. Ensure you have this key ready for configuration within the
  VS Code Code Sight extension.
- **VS Code Code Sight Extension:** The Signal functionality is integrated within the
  VS Code Code Sight extension. Make sure you have the latest
  version of the extension installed to take full advantage of Signal's features.
- **Git Repository for Code Changes Scanning:** For the Code Changes Scanning
  feature to function correctly, the project must be a Git repository.
  Additionally, Git must be available in the system PATH to facilitate the
  tracking of changes and ensure accurate scanning.

## Enabling Signal in Code Sight

1. Navigate to the **Products and License** page.
2. In the **Signal** tile, enter your LLM
   Key provided by Black Duck.
3. Signal features are accessible in
   Incremental Scan mode once enabled.

## Scanning Scopes

Scanning scopes define the specific sets of files that will be included in the scan
process. The following scopes are available for users to enhance their scanning
experience:

- **Active File Scanning**

  This scope allows users to scan the currently active file using [Signal's AI
  Scan](https://documentation.blackduck.com/bundle/signal/page/Signal_docs/topics/c_signal_overview.html) or Rapid Scan Static, focusing solely on the file that is open in the development environment.

  By default, Active File Scanning utilizes Rapid Scan Static. However, users can switch to AI Scan by clicking the **Enable AI**
  button in the **Local View** panel.
- **Code Changes Scanning** (Default)

  The Code Changes scope enables users to scan tracked files within their Git
  repository. To be eligible for scanning, new files must be staged. By
  default, Signal scans the diff-patches of
  uncommitted changes to identify relevant results. Users also have the option
  to configure the scan to include all uncommitted files, as well as commits
  that are ahead of the reference branch. Scanning Git submodules is not yet
  supported.

## Initiating Scans

There are two ways to initiate the scan:

- **AI Scan**

  - **Manual scan**: Trigger a scan by clicking the **Refresh** button
    in the **Local View** panel.
  - **Auto scan**: Enable auto-scan to run in the background every 24
    hours.
- **Rapid Static Scan**

  - **Manual scan**: Trigger a scan by clicking the **Refresh** button
    in the **Local View** panel.
  - **Auto scan**: For the Active File, scans run on file open and file
    save. For Code Changes, scans run on file save.

## Viewing Scan Results

After running a scan, the results in **Local View** are organized into two
categories: **Secrets** and **Vulnerabilities**.

- **Secrets**: This category includes all static scan (SAST) issues related to
  hardcoded secrets found in the codebase.
- **Vulnerabilities**: This category contains static scan (SAST) issues related
  to security weaknesses in the codebase, excluding hardcoded secrets.

## Configuring AI Scans

The following configuration options are available for AI Scan in both Active File and
Code Changes scopes:

| Option | Description |
| --- | --- |
| **Dataflow Agent** | Detect dataflow issues across function and method boundaries. |
| **Oversight Agent** | Reduces false positives by removing invalid or redundant findings. |
| **Auto Scan** | Automatically performs a scan every 24 hours. |
| **Code Changes: What to scan?** | Scans Git diff‑patches for relevant results **or** scans entire changed files. |
| **Code Changes: Scan scope** | Scans all uncommitted tracked files **or** all uncommitted tracked files + changes ahead of the reference branch. New files must be staged (git add) to be included. |
