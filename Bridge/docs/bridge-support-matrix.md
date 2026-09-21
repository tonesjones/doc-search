---
title: "Bridge support matrix"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-support-matrix.html"
content_id: "JLcDtzhRetUzUofAxL8hAQ"
version: "latest"
section: "Bridge support matrix"
scraped_at: "2026-08-08T23:49:10.272475+00:00"
---

# Bridge support matrix

## Supported tools

**Tools** supported by Bridge CLI.

| Tool | Notes |
| --- | --- |
| Polaris | Polaris users can use the Bridge CLI to automate SAST and/or SCA scans in their CI pipeline. For more SAST information, see [System Requirements](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/deploy-install-guide/topics/coverity_analysis_hardware-1.html). |
| Black Duck® SCA | Black Duck® SCA users can use the Bridge CLI to automate SCA scans in their CI pipeline. |
| Coverity Connect | Coverity users can use the Bridge CLI to automate SAST scans in their CI pipeline. The Bridge CLI can be used with both on-prem Coverity Connect as well as Coverity cloud deployment. For more information, see [System Requirements](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/deploy-install-guide/topics/coverity_connect_network_connectivity_requirements.html). |
| Software Risk Manager (SRM) | SRM users can use the Bridge CLI to automate SCA and SAST scanning in their CI pipeline. |

## Operating systems

**Bridge CLI** runs on the following operating systems.

| OS | System requirements | Notes |
| --- | --- | --- |
| Linux | 64-bit kernel, version 2.6.32+ with glibc 2.18 or later | Debian GNU is *not* supported.  Compatible with Linux ARM architectures, including both ARM32 (armv7) and ARM64 (aarch64). |
| macOS | macOS 11, 12, 13 | macOS 11, 12 and 13 on Intel is supported. M1 and M2 based Macs *are* supported as well. |
| Windows | x86_64, Version 10 and 11 and Windows Server 2019 and 2022 | Server Core is *not* supported. The Polaris Secure Tunnel feature does not run on Windows at this time due to a limitation of the underlying `teleport` Daemon. |
