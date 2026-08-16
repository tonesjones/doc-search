---
title: "Workflows"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/workflows.html"
content_id: "vceeunkOjKKW8sfTRVCckQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:39.439405+00:00"
---

# Workflows

Coverity Compliance Filtering incorporates two workflows⁠—a developer workflow and an
architect/quality manager workflow. These are the basic steps in the developer
workflow:

- Run the `cov-build` and `cov-analyze` commands to
  discover findings.
- Upload the analysis results to Coverity Connect using the
  `cov-commit-defects` command.
- Fix issues.

The developer iterates through this workflow on a frequent basis, as shown:

  
 [image: image]   

Coverity Compliance Filtering adds a separate workflow for the architect/quality
manager:

- Run the `cov-build` and `cov-analyze` commands to
  discover findings.
- Run the `cov-manage-findings` command to generate a findings
  report.
- View the findings report, analyze findings distribution, and create filtering
  policies that implement your prioritization decisions.
- Upload your filtering policies to Coverity Connect.

You execute the architect/quality manager workflow infrequently—generally only to set up
filtering policies or to adjust them. The following diagram illustrates this workflow:

  
 [image: image]   

The `cov-commit-defects` command now uploads filtered analysis results
without additional steps. And although the developer's basic workflow is unmodified, the
developer can now use issue scores to prioritize development work (see Using scores to prioritize development tasks). The architect/quality
manager workflow feeds into the developer workflow as shown:

  
 [image: image]
