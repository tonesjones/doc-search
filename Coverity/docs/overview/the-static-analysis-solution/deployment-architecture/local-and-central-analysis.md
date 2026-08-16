---
title: "Local and central analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/local-and-central-analysis.html"
content_id: "VpXb7_teWScJofhwDgxRJQ"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:15.298189+00:00"
---

# Local and central analysis

In the deployment example just described, all code analysis is performed centrally on the
build server. The following deployment example augments the previous example by adding
Coverity Analysis to the developer's machine. This deployment supports a workflow like
the following:

1. Coverity Analysis is installed on a build server where the artifacts of the build
   are analyzed.
2. At the conclusion of each build-and-analysis run, which happens daily or whenever
   code is checked in, code issues that have been discovered are committed to Coverity
   Connect as *issues*.

   Developers use their clients to
   browse the Connect server and review issues that have been assigned to
   them.
3. The developer performs analysis locally, and resolves issues.
4. The developer checks in fixed code.
5. The central build also runs an analysis to discover issues that arise from the
   code's interaction with other checked-in code.
6. The developer resolves any additional issues discovered in the central analysis and
   checks in code again.

To support this model, the Code Sight or Coverity Desktop plug-in is installed in the
developer's IDE, allowing the developer to find, examine, fix, and analyze code directly
in the IDE.

Figure 1. Combined Analysis
[image: image]
