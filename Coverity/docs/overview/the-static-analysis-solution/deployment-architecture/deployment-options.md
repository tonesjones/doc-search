---
title: "Deployment options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deployment-options.html"
content_id: "nuCHRGSJtzH3gHDefKlvkg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:16.582170+00:00"
---

# Deployment options

Coverity supports many deployment options. Basic options involve the following:

- Using the embedded PostgreSQL database or configuring Coverity Connect to use your
  own external PostgreSQL database.
- Deploying Coverity Connect as either a stand-alone application or along with
  multiple Connect instances in a coordinator-and-subscriber arrangement.
- Configuring multiple Coverity Analysis instances to commit issues to the Coverity
  Connect server.
- Deploying Analysis in an SCM pipeline (in GitHub, GitLab, Azure, Bitbucket or
  Jenkins) and surfacing issues as pull request comments when developers are working
  on a feature branch, then as issues in the Coverity Connect portal after the branch
  is merged.
- Deploying Coverity Connect in your private cloud server on Kubernetes, using an
  external PostgreSQL database to save scan results.
