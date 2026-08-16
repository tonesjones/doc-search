---
title: "Running a local analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-a-local-analysis.html"
content_id: "5tkx7d18YNTmm2i7tgwyOA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:10.820172+00:00"
---

# Running a local analysis

Local analysis allows you to locate new and existing issues for code that you have
changed before checking it into your central code repository. This short tutorial will
guide you through the necessary steps.

In order for local analysis to return the most accurate results, you must connect to a relevant
stream on the Coverity Connect server. This will provide necessary
interprocedural analysis summary information for fast, accurate analysis results. This
will also allow issue triage information to be shared between Coverity Desktop and Coverity Connect. See Streams for additional information.

Note: This tutorial assumes that you have a project open within the IDE in one
of the supported languages: C/C++, C#, JavaScript, Node.js, PHP, Ruby, and
Python.

1. Ensure that the source file you want to analyze is open in the main
   Editor pane.

   CAUTION:

   Coverity Desktop requires you to analyze a
   Project or Solution. If you open your code at the folder level, Coverity capture
   and analysis will not succeed.
2. Select Analyze Current Editor File from the 
   Coverity menu, or simply click the shortcut icon ( [image: image] ) on the toolbar. This will save
   the current editor file if it has any unsaved changes.

   Note: You can also
   analyze multiple files in the same local analysis. To do so, use the
   Analyze Modified Files (SCM) option, via the
    Coverity menu or the toolbar shortcut. If you
   have configured your SCM for use with Coverity Desktop,
   this will analyze all source files that are new or modified since your
   latest checkout.

   If you have not configured your SCM, you can simply
   select multiple files manually:
   1. Highlight each of the files and/or packages you wish to
      analyze in the solution explorer.
   2. Right-click the selection to open the context menu.
   3. Click Analyze Selected File(s) with
      Coverity.

   Figure 1. Context menu
   [image: image]

   Note that any source files that have not been previously captured in a build by Coverity Desktop will not be available for analysis. When you
   attempt to run local analysis on one of these files, you will be prompted with
   several options in the Uncaptured Source Files dialog. To
   proceed with analysis, select Capture Build and Analyze.
   This will capture a build of the entire solution, and then
   run the local analysis as requested.
3. Once the analysis is complete, the Issues view will be
   updated to reflect any issues in the code you've selected. Double-click on an
   issue to view and triage the issue from within the IDE.

Analyzing different Solution/Platform Configurations
:   You can associate different Solution/Platform Configurations to specific
    analysis settings by creating a unique Analysis Configuration for each unique Solution/Platform
    Configuration you want to analyze.

    If the Solution/Platform Configuration needs to be associated with a specific Coverity Connect stream, make sure that you have selected the
    appropriate active Analysis Configuration, or create a new one with the
    correct stream setting configured. The current Solution/Platform
    Configuration build will always be analyzed using the currently active
    Analysis Configuration.

See Analysis scope options for additional analysis
options.
