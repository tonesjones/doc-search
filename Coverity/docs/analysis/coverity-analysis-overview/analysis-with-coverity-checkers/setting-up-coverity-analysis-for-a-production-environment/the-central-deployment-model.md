---
title: "The central deployment model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-central-deployment-model.html"
content_id: "lHNIxhMjQlKIRsLyeAXW2w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:55.409886+00:00"
---

# The central deployment model

The central deployment model separates administrative tasks from the tasks that
developers perform.

- As an administrator, you check out the latest source to a platform that supports Coverity
  Analysis, analyze the source code, and commit the analysis results to Coverity
  Connect. To deploy Coverity Analysis based on this model, you need to write a script
  that automatically runs the Coverity Analysis commands needed to analyze a given
  code base (see Analysis with Coverity Checkers).

  You can integrate Coverity
  Analysis with the build process to provide Coverity Analysis consumers with
  analysis results from snapshots of the latest source code (for details, see
  Integrating Coverity Analysis into a build system).

  As mentioned in Setting up Coverity Analysis for a production environment,
  you can also combine this model with an IDE-based deployment model if your
  developers are using Coverity Desktop for Eclipse or Visual Studio.
- After using Coverity Connect to discover, prioritize, and understand the software issues that
  they own, developers check out the affected source code files from the source
  repository, fix one or more of the issues locally, and then check in their fixes to
  the source repository. Coverity Connect will reflect the fixes in the next round of
  analysis results (the next snapshot) of the code base that contained the
  issues.
