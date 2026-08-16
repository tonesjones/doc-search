---
title: "Bazel"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/bazel.html"
content_id: "2sGxbfdqFY0BAUhRq7iWlA"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:56.980679+00:00"
---

# Bazel

Bazel is supported in Coverity starting in versions 2022.3.0+ and Black Duck C/CPP in
versions 1.0.13+.

## Prerequisites

Please visit [Bazel Tutorial: Build a C++ Project](https://bazel.build/start/cpp) for more information
on how to get started with Bazel in your environment.

Bazel builds can be captured on the x86_64 versions of Windows, Linux, and macOS that
are supported by Coverity Analysis. Please visit <https://bazel.build/install> for more
information on how to install and configure Bazel for your environment.

## How to enable Bazel in your scan

Before enabling Bazel in your Black Duck C/CPP tool scan, you must first configure it in Coverity. Once configuration is
complete, use the `--bazel` argument in the command line or set
`bazel: True` in your yaml
configuration file.

## Compilers

Compilers for Coverity Analysis are supported, but all compilers must be accessible
and runnable on the host system: Remote cross-platform builds are not supported.

Supported compilers for C/C++ on x86_64 are as follows:

Table 1. Coverity 2023.9.x

| Compiler | Version | Host OS |
| --- | --- | --- |
| Clang | Android NDK Clang 9.0.9–14.0.6 (NDK revisions r21e–r25b) | Windows, Linux, macOS |
| LLVM Clang 7.0–16.0 | Windows, Linux, macOS, FreeBSD |
| Rynda Clang |
| clang-cl | 7.0–16.0 | Windows |
| Embarcadero (formerly Borland) C++ | 7.60 | Windows |
| GNU GCC and G++ | GNU gcc and g++ versions 4.1.0–13.1 | Windows, Linux, Linux ARM64, macOS on Intel, FreeBSD, Solaris |
| Intel C++ | 17.0.0 | Linux |
| 17.0.0–19.1.0 | Windows |
| Intel oneAPI DPC++/C++ | 2022.1.0 | Windows, Linux |
| Microsoft Visual C++ | 2019–2022 | Windows |
| Xcode (with Clang compiler) | Apple Clang 12.0 (Xcode 12.0–12.5) | macOS |
| Apple Clang 13.3 (Xcode 13.3) |
| Apple Clang 14.0 (Xcode 14.0–14.3) |

Table 2. Coverity 2023.6.x

| Compiler | Version | Host OS |
| --- | --- | --- |
| Clang | Android NDK Clang 9.0.9–14.0.6 (NDK revisions r21e–r25b) | Windows, Linux, macOS |
| LLVM Clang 7.0–16.0 | Windows, Linux, macOS, FreeBSD |
| Rynda Clang |
| clang-cl | 7.0–16.0 | Windows |
| Embarcadero (formerly Borland) C++ | 7.60 | Windows |
| GNU GCC and G++ | GNU gcc and g++ versions 4.1.0–12.1 | Windows, Linux, Linux ARM64, macOS on Intel, FreeBSD, Solaris |
| Intel C++ | 17.0.0 | Linux |
| 17.0.0–19.1.0 | Windows |
| Intel oneAPI DPC++/C++ | 2022.1.0 | Windows, Linux |
| Microsoft Visual C++ | 2019–2022 | Windows |
| Xcode (with Clang compiler) | Apple Clang 12.0 (Xcode 12.0–12.5) | macOS |
| Apple Clang 13.3 (Xcode 13.3) |
| Apple Clang 14.0 (Xcode 14.0–14.3) |

Table 3. Coverity 2023.3.x

| Compiler | Version | Host OS |
| --- | --- | --- |
| Clang | Android NDK Clang 9.0.9–14.0.6 (NDK revisions r21e–r25b) | Windows, Linux, macOS |
| LLVM Clang 6.0–15.0 | Windows, Linux, macOS, FreeBSD |
| Rynda Clang |
| clang-cl | 7.0–13.0 | Windows |
| Embarcadero (formerly Borland) C++ | 7.60 | Windows |
| GNU GCC and G++ | GNU gcc and g++ versions 4.0–12.1 | Windows, Linux, Linux ARM64, macOS on Intel, FreeBSD, Solaris |
| Intel C++ | 17.0.0 | Linux |
| 17.0.0–19.1.0 | Windows |
| Intel oneAPI DPC++/C++ | 2022.1.0 | Windows, Linux |
| Microsoft Visual C++ | 2019–2022 | Windows |
| Xcode (with Clang compiler) | Apple Clang 11.0 (Xcode 11.0–11.4) | macOS |
| Apple Clang 12.0 (Xcode 12.0–12.5) |
| Apple Clang 13.3 (Xcode 13.3) |
| Apple Clang 14.0 (Xcode 14.0–14.1) |

Table 4. Coverity 2022.12.x

| Compiler | Version | Host OS |
| --- | --- | --- |
| Clang | Android NDK Clang 3.1–3.4 (NDK revisions r8c–r9d) | Windows, Linux, macOS on Intel, FreeBSD |
| Android NDK Clang 9.0.9–14.0.6 (NDK revisions r21e–r25b) | Windows, Linux, macOS |
| LLVM Clang 6.0–15.0 | Windows, Linux, macOS, FreeBSD |
| Rynda Clang |
| clang-cl | 7.0–13.0 | Windows |
| GNU GCC and G++ | GNU gcc and g++ versions 4.0–12.1 | Windows, Linux, Linux ARM64, macOS on Intel, FreeBSD, Solaris |
| Intel C++ | 17.0.0 | Linux |
| 17.0.0–19.1.0 | Windows |
| Intel oneAPI DPC++/C++ | 2022.1.0 | Windows, Linux |
| Microsoft Visual C++ | 2017–2022 | Windows |
| Xcode (with Clang compiler) | Apple Clang 11.0 (Xcode 11.0–11.4) | macOS |
| Apple Clang 12.0 (Xcode 12.0–12.5) |
| Apple Clang 13.3 (Xcode 13.3) |
| Apple Clang 14.0 (Xcode 14.0–14.1) |
