---
title: "Installing Coverity Analysis for local analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-analysis-for-local-analysis.html"
content_id: "wsh6QftgASsjh7unr2o6bQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:58.545848+00:00"
---

# Installing Coverity Analysis for local analysis

Coverity Analysis is used to run a local analysis. If the Coverity Connect system administrator
has configured the Downloads page to include the Coverity
Analysis installer, you can download it (and optionally the
license.dat license file) to your system. (For information on
how to configure the Downloads page to include the Coverity
Analysis installer, refer to the section "Adding
Coverity Analysis to the Downloads page" in the Coverity Platform 2026.6.0 User and Administrator Guide.)

To download Coverity Analysis from the Coverity Connect Downloads
page:

1. In the Downloads page, download the Coverity Analysis package
   (if available).
2. If available, download the license file.
3. Run the Coverity Analysis installer. It is required that you provide the location of
   the license.dat file during installation.

   Note: In the case
   where Coverity Analysis uses a FlexNet license, you will find a
   license.config file in 
   SA_install_dir/bin.
4. When you configure Coverity Desktop for local analysis, you can point the
   configuration to your local Coverity Analysis instance.
