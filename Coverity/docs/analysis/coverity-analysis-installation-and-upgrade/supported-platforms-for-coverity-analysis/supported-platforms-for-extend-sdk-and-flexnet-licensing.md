---
title: "Supported platforms for Extend SDK and FlexNet licensing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/supported-platforms-for-extend-sdk-and-flexnet-licensing.html"
content_id: "WdDiLba3Gz6Sy8eBg3sgNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:00.466907+00:00"
---

# Supported platforms for Extend SDK and FlexNet licensing

This section describes Extend SDK and FlexNet Licensing support per platform. The
following table lists all platforms and versions on which Extend SDK and/or FlexNet
Licensing is supported.

Virtual machine (VM) implementations of the supported platforms are also supported if you
use FlexNet licensing or a default license that is not node-locked to a particular host
machine.

Table 1. Extend SDK and FlexNet licensing platform support

| OS | Platform | Extend SDK | FlexNet licensing | Notes |
| --- | --- | --- | --- | --- |
| Linux | Linux Kernel 2.6.32+ (32-bit) with glibc 2.18-2.27 (32-bit) on x86 | Yes | Yes |  |
| Linux Kernel 2.6.32+ (64-bit) with glibc 2.18-2.27 (64-bit) on x86_64 |
| Linux Kernel 2.6.32+ (64-bit) with glibc 2.18-2.27 (64-bit) on arm64 |  |
| macOS | 15 on Intel |  | Yes | *To avoid "bad message command" errors, the FlexNet server (`lmgrd`) must also be on Apple silicon.  **Deprecation notice:** Support for macOS on Intel (`macosx`) is deprecated as of 2025.12.0 and will be removed in 2026.12.0.  **Deprecation notice:** Support for macOS 14 is deprecated as of 2026.6.0 and will be removed in a future release. |
| 15 on Apple silicon | Yes* |
| 16 on Intel | Yes |
| 16 on Apple silicon | Yes* |
| 26 on Intel | Yes |
| 26 on Apple silicon | Yes* |
| Solaris | 11.4 (64-bit) on x86_64 | Yes | Yes | Extend SDK requires the `libiconv` library, and you must configure the system dynamic loader (`ld.so.1`) to locate it. On Solaris SPARC hosts, the FlexNet Publisher license manager daemon (`lmgrd`) is supported only when installed on the global zone. |
| 11.4 (64-bit) on SPARC |  |
| Windows | Windows 64-bit workstation releases Windows 11 | Yes | Yes |  |
| Windows 64-bit server releases Windows Server 2022 |
