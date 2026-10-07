---
title: "Bridge support matrix"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-support-matrix.html"
content_id: "JLcDtzhRetUzUofAxL8hAQ"
version: "latest"
section: "Bridge support matrix"
scraped_at: "2026-10-04T23:28:32.084653+00:00"
content_hash: "3c7ba18620069183d9ab26a4000932cf0997641730df8e97eb10f6d6e13dac5a"
---

# Bridge support matrix

## Supported tools

**Tools** supported by Bridge CLI.

| Tool | Notes |
| --- | --- |
| Polaris | Polaris users can use the Bridge CLI to automate SAST and/or SCA scans in their CI pipeline. For more SAST information, see [System Requirements](https://docs.blackduck.com/access?ft:originId=f720d35c853c162f322ebf99909fe7c9/3cf3ec7339817e1950a3dc5f223e174f.topic). |
| Black Duck® SCA | Black Duck® SCA users can use the Bridge CLI to automate SCA scans in their CI pipeline. |
| Coverity Connect | Coverity users can use the Bridge CLI to automate SAST scans in their CI pipeline. The Bridge CLI can be used with both on-prem Coverity Connect as well as Coverity cloud deployment. For more information, see [System Requirements](https://docs.blackduck.com/access?ft:originId=f720d35c853c162f322ebf99909fe7c9/6c2ec9e5ca6406fb68729cff01333f2c.topic). |
| Software Risk Manager (SRM) | SRM users can use the Bridge CLI to automate SCA and SAST scanning in their CI pipeline. |

## Operating systems

**Bridge CLI** runs on the following operating systems.

| OS | System requirements | Notes |
| --- | --- | --- |
| Linux | 64-bit kernel, version 2.6.32+.  - **x86_64**   - Bridge 4.2.1 and later (recommended) do not require glibc.   - Bridge 4.2.0: glibc 2.34.   - Bridge versions earlier than 4.2.0: glibc 2.32. - **arm64**    - No glibc dependency. | Debian GNU is *not* supported.  Compatible with Linux ARM64 (aarch64). |
| macOS | macOS 11, 12, 13 | macOS 11, 12 and 13 on Intel is supported. M1 and M2 based Macs *are* supported as well. |
| Windows | x86_64, Version 10 and 11 and Windows Server 2019 and 2022 | Server Core is *not* supported. The Polaris Secure Tunnel feature does not run on Windows at this time due to a limitation of the underlying `teleport` Daemon. |
