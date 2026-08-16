---
title: "Preparing to initiate Scan Service analyses from the full client"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-to-initiate-scan-service-analyses-from-the-full-client.html"
content_id: "500FgoAbpe_31kFK574SIg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:37.654831+00:00"
---

# Preparing to initiate Scan Service analyses from the full client

If you installed both Scan Service and the full Coverity client, you can
direct Coverity to perform an analysis using the Coverity
Scan Service. To do this, you can either manually modify the configuration file to
change the analysis location to `connect`, or use the command line as
described in Initiating a scan in the cloud and Using the Coverity CLI to override configuration defaults.

Note: If you scan your project in a CI/CD pipeline, you might want to
check-in a modified configuration file when you check-in the code to the SCM
system.

For information on available configuration settings, see "Options reference"
in the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.
