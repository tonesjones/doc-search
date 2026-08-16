---
title: "Running a local analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-a-local-analysis.html"
content_id: "nOcYlBjaKbymRwCr5PaTlg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:30.168898+00:00"
---

# Running a local analysis

Local analysis allows you to locate new defects for code that you have changed before
checking it into your central code repository. This short tutorial will guide you
through the necessary steps.

In order for local analysis to return the most accurate results, you must connect to a relevant
stream on the Coverity Connect server. This will provide necessary
interprocedural analysis summary information for fast, accurate analysis results. This
will also allow issue triage information to be shared between Coverity Desktop and Coverity Connect. See Analysis Configurations... dialog for additional information.

Note: This tutorial assumes that you have a Java project open within the IDE.

Ensure that the source file you want to analyze is open in the main
Editor pane.

1. Select Analyze Current Editor File from the Tools > Coverity menu, or simply click the shortcut icon ( [image: image] ) on the toolbar.

   Note: You can
   also analyze multiple files in the same local analysis. To do so:
   1. Highlight each of the files, packages, and/or projects you wish
      to analyze in the package explorer.
   2. Right-click the selection to open the context menu.
   3. Click Analyze Selected File(s).

   Figure 1. Context menu
   [image: image]

   Note that if your project uses a gradle build, any source files that have not been previously
   captured by Coverity Desktop may not be available for
   analysis. When you attempt to run local analysis on one of these files, you will
   be prompted with several options in the Uncaptured Source
   Files dialog. To proceed with analysis, select
   Capture Build and Analyze. This will capture a build
   of any uncaptured files, and then run the local analysis as requested.
2. Once the analysis is complete, the Issues view will be
   updated to reflect any issues in the code you've selected. Double-click on a CID
   to view and triage the issue from within the IDE.

See Analysis scope options for additional analysis
options.
