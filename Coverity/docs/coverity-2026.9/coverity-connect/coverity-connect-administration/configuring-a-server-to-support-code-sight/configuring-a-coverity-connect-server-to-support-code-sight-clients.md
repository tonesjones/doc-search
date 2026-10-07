---
title: "Configuring a Coverity Connect server to support Code Sight clients"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-a-coverity-connect-server-to-support-code-sight-clients.html"
content_id: "XzKflii9WnpGABZgHzAPPw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:13.318331+00:00"
---

# Configuring a Coverity Connect server to support Code Sight clients

The Coverity Connect server needs to deploy both the installer for
Coverity® Analysis, and the customer's license.dat
file.

- The server administer must ensure that both the installer for
  Coverity® Analysis and the license.dat file are
  located in a directory named as follows:
  <server-install-dir>/server/base/webapps/downloads.

  These are the specific file names:

  - license.dat
  - cov-analysis-win64-2026.9.exe
  - cov-analysis-linux64-2026.9.sh
  - cov-analysis-macosx-2026.9.sh
