---
title: "Java compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-compilers.html"
content_id: "FEV7Lz4y400ZoqgtCEI8fA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:13.888455+00:00"
---

# Java compilers

Coverity Analysis for Java supports the analysis of Java code that is built in two
ways:

- **[Recommended]** Using `cov-build`. For information about this
  build mode, see the section "Build capture (for compiled languages)" in the Coverity Analysis 2026.6.0 User and Administrator Guide, and see the `cov-build`
  command documentation in the Coverity 2026.6.0 Command Reference.
- Using buildless or filesystem capture. For information about these build modes, see
  the section "The capture" in the
  Coverity Analysis 2026.6.0 User and Administrator Guide, and see
  the `cov-emit-java`
  command documentation in the Coverity 2026.6.0 Command Reference.

Important: Java preview features are not guaranteed to be fully backwards
compatible.

Important: Coverity does not support Java compilations with a target (via the
--release argument) less than 8.

Table 1. Supported Java compilers for static analysis

| Host OS | Compiler | Compiler version | Notes |
| --- | --- | --- | --- |
| Linux (64-bit)/Linux ARM64/Windows (64-bit) | OpenJDK | 1.8, 17, 21, 25, 26 | **Deprecation notice:** Support for OpenJDK 17 is deprecated as of 2026.6.0 and support for it will be removed in a future release. |
| macOS/Linux (64-bit)/Windows (64-bit) | Oracle JDK | macOS on Intel: To ensure a complete capture, version 12-16 of Xcode (with command line tools) must be installed. Also, ensure that `xcodebuild -version` runs without error; Coverity uses this command to check the Xcode version.  macOS on Apple silicon: Build capture requires both Rosetta 2 and Xcode (*with command line tools*) 12 - 16 in order to function. Please ensure `xcodebuild -version` runs without error.  **Deprecation notice:** Support for Oracle JDK 17 is deprecated as of 2026.6.0 and support for it will be removed in a future release. |
