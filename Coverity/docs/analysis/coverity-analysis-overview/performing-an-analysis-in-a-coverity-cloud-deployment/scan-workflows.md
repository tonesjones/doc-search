---
title: "Scan workflows"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-workflows.html"
content_id: "z9vGBDi_fyuzsxLpHSYy2A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:34.966681+00:00"
---

# Scan workflows

With either the full Coverity Analysis client or the Thin Client, you can invoke
a scan using either the `coverity scan` command which performs the
capture, analysis, and commit with one command, or by issuing separate capture, analysis
and commit commands as follows:

1. Running `coverity capture` captures source files to be analyzed
   and saves them in an intermediate directory (idir) in the cloud.
2. Running `coverity analyze` performs the analysis in the cloud and
   writes the results to the idir.
3. Running `coverity commit` reads the analysis results from the idir
   and commits (pushes) the analysis results to Coverity Connect.
4. Developers and team leads can view analysis status as described in Managing and viewing the status of analyses performed in the cloud.

   Developers and team leads can view, manage, and fix software issues as described
   in the document, Coverity Platform 2026.6.0 User and Administrator Guide.

   Administrators can view performance metrics and logs to resolve issues with or
   fine tune Coverity, Kubernetes, and the cloud environment as described in the
   document, Coverity 2026.6.0 Cloud Deployment Administrator and User Guide.

Using multiple commands enables you to list and verify the captured files before starting
a potentially long-running analysis. These commands can be used with CI/CD.

With Coverity Scan Service deployed in the cloud, both workflows capture the
code on the your client system and save the code in the cloud. The cloud-based Scan
Service performs the analysis using cloud-based compute resources, assigns a unique
identifier for the scan, and provides a job status to the client. Coverity Connect, which is located in the cloud, saves the analysis
results in the PostgreSQL database.
