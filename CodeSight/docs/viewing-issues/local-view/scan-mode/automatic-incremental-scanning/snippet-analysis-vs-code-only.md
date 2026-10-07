---
title: "Snippet Analysis (VS Code only)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/snippet-analysis-vs-code-only-.html"
content_id: "2ZPfaKy8pcAuVQrTU7SbfA"
version: "2026.9.0"
section: "Viewing Issues in Code Sight"
scraped_at: "2026-10-06T23:39:51.739439+00:00"
---

# Snippet Analysis (VS Code only)

Snippet matching can help you manage legal risk and detect possible license infringements.
A snippet match occurs when a portion of code in your source file matches code in one or more
KnowledgeBase files.

Snippets are small reusable pieces of computer code. A snippet of open-source
software can easily find its way into your proprietary files. For example, a
developer might find a useful function from an open-source program and copy and
paste that code into their program.

Because the use of open-source software is managed through licenses that allow you
to use, modify, and share the software under defined terms and conditions, it is important
to identify the open-source software used in your proprietary code so that you can manage the
legal risk and detect possible license infringement.

Your proprietary code might include only a portion of open-source software, but you still
must comply with the license associated with that particular open-source software.

## Conditions for running Snippet Analysis

These conditions apply to running Snippet Analysis:

- Snippet Analysis is available only within VS Code.
- You must be connected to a Black Duck SCA server whose version is 2024.10 or greater,
  and that has a license for Generative AI Compliance,

  *OR ...*
- You must have an active license for the Code Sight Standard Edition (CSSE).

## To view the results of Snippet Analysis

1. In LOCAL VIEW, make sure the scan mode is Automatic.
2. [image: image] In
   the LOCAL VIEW title bar, click the settings icon.

   This displays the Code Sight Automatic Scan Configuration tab.
3. On the configuration tab, click to turn on the Snippet Analysis toggle.

   [image: Tab to configure Sigma scans and snippet analysis]
4. Use the two check boxes to choose when you want VS Code to scan the source files.

When it has scanned the source, VS Code displays the names of detected open-source snippets
in the LOCAL VIEW.

[image: LOCAL VIEW showing results of a snippet scan]
