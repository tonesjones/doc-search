---
title: "Preliminaries: Server-side configuration for Coverity Connect"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/preliminaries-server-side-configuration-for-coverity-connect.html"
content_id: "~QSgTTSQ0juSo~YGV2lesg"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.615375+00:00"
---

# Preliminaries: Server-side configuration for Coverity Connect

Installers for Coverity Analysis, and a license.dat file, must be present
on the Coverity Connect server so they are available for downloading to Code Sight users who wish to
install and run Coverity Analysis.

This is a necessary first step for a Coverity Connect server to support Code Sight clients.
The server administrators should follow these steps before any client system attempts to download
Coverity Analysis.

The server administrator must ensure that both the installers for Coverity Analysis and the license.dat file
be located in a directory named <server-install-dir>/server/base/webapps/downloads.

These are the specific file names:

- license.dat
- cov-analysis-win64-<versionNumber>.exe
- cov-analysis-linux64-<versionNumber>.sh
- cov-analysis-macosx-<versionNumberr>.sh
- cov-analysis-macos-arm-<versionNumber>.sh

It is also possible to upload the Coverity Analysis files in compressed format:
.zip for Windows, .tar.gz for Linux or macOS.
