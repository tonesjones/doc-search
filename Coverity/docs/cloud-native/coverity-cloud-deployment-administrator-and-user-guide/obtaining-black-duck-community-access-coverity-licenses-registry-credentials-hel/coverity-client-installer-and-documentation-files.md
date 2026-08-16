---
title: "Coverity client installer and documentation files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-client-installer-and-documentation-files.html"
content_id: "V41k3ijAhFKWkPetCOWabg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:33.877531+00:00"
---

# Coverity client installer and documentation files

This section identifies the following files that you can download from the Black Duck private Docker registry using the
`curl` command.

- Coverity toolkit installer files which include the Thin Client.
- Full Coverity Analysis client installer files.
- Host ID generate files.
- Platform files.
- Documentation files.

The Black Duck private repository which contains client
installer and documentation files is located here:

- `https://repo.blackduck.com/coverity-releases/2026.6.0/`

You can download files from the Black Duck private Docker registry using the
`curl` command, which enables you to download automatically from
within a script. For a download example, see the next section, Downloading a full analysis client file from the Black Duck repository.

Table 1. Coverity client installer and documentation files

| Category | File |
| --- | --- |
| Coverity Tools (includes Thin Client) | Important: If you are deploying Scan Service, you must download a `coverity-all-platforms...` file. Each of these files contains:   - Thin Client installers files. The administrator must   provide these files as needed through the Connect UI.   End users will download and install client software on   their client systems to interface with the cloud and be   able to run scans in Scan Service within the Kubernetes   container environment. - Analysis software that runs in its own pod within the Scan   Service node, and performs analyses for Scan Service. - Related client tools needed to setup and run scans.  `coverity-all-platforms-2026.6.0.tar.gz`  `coverity-all-platforms-2026.3.1.tar.gz`  `coverity-all-platforms-2026.3.0.tar.gz`  `coverity-all-platforms-2025.12.2.tar.gz`  `coverity-all-platforms-2025.12.1.tar.gz`  `coverity-all-platforms-2025.12.0.tar.gz`  `coverity-all-platforms-2025.9.3.tar.gz`  `coverity-all-platforms-2025.9.2.tar.gz`  `coverity-all-platforms-2025.9.0.tar.gz`  `coverity-all-platforms-2025.6.4.tar.gz`  `coverity-all-platforms-2025.6.2.tar.gz`  `coverity-all-platforms-2025.6.0.tar.gz`  `coverity-all-platforms-2025.3.2.tar.gz`  `coverity-all-platforms-2025.3.1.tar.gz`  `coverity-all-platforms-2025.3.0.tar.gz`  `coverity-all-platforms-2024.12.2.tar.gz`  `coverity-all-platforms-2024.12.1.tar.gz`  `coverity-all-platforms-2024.12.0.tar.gz` |
| Full Analysis client | Important: If you are not deploying Scan Service, you must download one of the following full analysis client installer files, `cov-analysis-platform-version`.  `cov-analysis-linux-2026.6.0.sh`  `cov-analysis-linux-2026.6.0.tar.gz`  `cov-analysis-linux64-2026.6.0.sh`  `cov-analysis-linux64-2026.6.0.tar.gz`  `cov-analysis-linux-arm64-2026.6.0.sh`  `cov-analysis-linux-arm64-2026.6.0.tar.gz`  `cov-analysis-macos-arm-2026.6.0.dmg`  `cov-analysis-macos-arm-2026.6.0.sh`  `cov-analysis-macos-arm-2026.6.0.tar.gz`  `cov-analysis-macosx-2026.6.0.dmg`  `cov-analysis-macosx-2026.6.0.sh`  `cov-analysis-macosx-2026.6.0.tar.gz`  `cov-analysis-win32-2026.6.0.exe`  `cov-analysis-win32-2026.6.0.zip`  `cov-analysis-win64-2026.6.0.exe`  `cov-analysis-win64-2026.6.0.zip` |
| Host ID generate | `cov-generate-hostid-linux-2026.6.0`  `cov-generate-hostid-linux64-2026.6.0`  `cov-generate-hostid-macos-arm-2026.6.0.dmg`  `cov-generate-hostid-macosx-2026.6.0.dmg`  `cov-generate-hostid-win32-2026.6.0.exe`  `cov-generate-hostid-win64-2026.6.0.exe` |
| Platform | `cov-platform-linux64-2026.6.0.sh`  `cov-platform-win64-2026.6.0.exe` |
| Documentation | `doc_en.zip`  `doc_install_en.zip`  `doc_install_ja.zip`  `doc_install_ko.zip`  `doc_install_zh-cn.zip`  `doc_ja.zip`  `doc_ko.zip`  `doc_zh-cn.zip` |
