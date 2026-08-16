---
title: "Third Party Integration Toolkit overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/third-party-integration-toolkit-overview.html"
content_id: "hFi_EhM2xn9v5mZNHbPu2Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:25.376951+00:00"
---

# Third Party Integration Toolkit overview

The Coverity Connect Third Party Integration Toolkit is a command line tool that imports
issues discovered by a third-party analysis tool and the source code files that contain
these issues. The issues are then displayed in Coverity Connect allowing you to examine
and manage the issues in the same way that you would manage an issue discovered by
Coverity Analysis.

For example, the Third Party Integration Toolkit can import results from an analysis run
by PMD and can then be viewed in Coverity Connect, alongside analysis results from
Coverity Analysis. PMD issues can then be triaged and annotated in Coverity Connect.

The Third Party Integration Toolkit imports your third-party issues through the
`cov-import-results` command. `cov-import-results`
accepts issue and source file information provided in a JSON import file. The import
file is typically created by a tool, such as a script, that you provide (it is not
provided by Coverity).

This book provides the following information:

- A tutorial
  describing the process of running the Third Party Integration Toolkit
- Sample JSON and
  source files that serve as the basis of the tutorial
- A reference of the JSON
  elements used in the import file
- Important capacity and
  performance information and recommendations
