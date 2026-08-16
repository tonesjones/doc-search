---
title: "Prerequisites"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/prerequisites.html"
content_id: "Gn5QwMcElmyyxUX0eaANuQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:44.464512+00:00"
---

# Prerequisites

Before you do anything else, verify that the prerequisites for performing a Coverity Analysis have been met.

This is a step you probably need to perform only once.

- To run an analysis, you must have a valid license to Coverity Analysis.

  If you have not yet set up licensing (for example, during the installation process), you can refer to
  "Coverity Analysis license options" in the
  Coverity 2026.6.0 Installation and Upgrade Guide.
- You need to know your Coverity Connect username, password, and the Coverity Connect host or data port.

  For example, see The commit.

  Note:
  When the target Coverity Connect instance is configured to support Single Sign-on (SSO),
  you can use that method to sign in.

  For more information about Single Sign-on, see
  "Configuring Coverity Connect to use SAML" in
  the Coverity Platform 2026.6.0 User and Administrator Guide.
- You also need to have access to a Coverity Connect
  stream to which you can send your analysis results.

  Typically, a Coverity Connect administrator is responsible for setting up the stream, giving you permission to commit
  issues to it, and providing the other information you need.
  If you need set up your own stream, you can refer to
  "Working with projects and streams" in the
  Coverity Platform 2026.6.0 User and Administrator Guide.
- Make sure that you have adequate memory for the analysis.

  For details, see
  "Hardware and network recommendations and requirements"
  in the Coverity 2026.6.0 Installation and Upgrade Guide.

CAUTION:

In accordance with proper security practices, we do not advise installing Coverity Analysis as a root user.

See "Coverity Analysis commands"
in the Coverity 2026.6.0 Command Reference for a list of all the
Coverity Analysis commands that are available to you.
