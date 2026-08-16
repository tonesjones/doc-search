---
title: "Kotlin compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/kotlin-compilers.html"
content_id: "lXGt4baHtfjUX4AT2vzSQA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:14.548470+00:00"
---

# Kotlin compilers

Coverity Analysis for Kotlin supports the analysis of Kotlin code that is built using the
`cov-build` command. For information about this build mode, see the
section "Build capture (for compiled languages)" in the Coverity Analysis 2026.6.0 User and Administrator Guide, and see the `cov-build`
command documentation in the Coverity 2026.6.0 Command Reference.

Table 1. Supported compilers: Coverity Analysis for Kotlin

| Compiler | Compiler version | Host OS | Notes |
| --- | --- | --- | --- |
| Kotlin | 2.0.0-2.0.21, 2.1.0-2.1.10 | Linux (64-bit) | Coverity only supports Kotlin projects that are targeted to JVM or Android, not other platforms. For multiplatform projects, Coverity only captures Kotlin source files that are targeted to the supported platforms.  Coverity does not support Kotlin on Linux ARM64.  macOS on Intel: To ensure a complete capture, version 12-16 of Xcode (with command line tools) must be installed. Also, ensure that `xcodebuild -version` runs without error; Coverity uses this command to check the Xcode version.  macOS on Apple silicon: Build capture requires both Rosetta 2 and Xcode (*with command line tools*) 12 - 16 in order to function. Please ensure `xcodebuild -version` runs without error.  **Deprecation notice:** Support for Kotlin 2.0.x is deprecated as of 2025.3.0 and will be removed in a future release.  Coverity capture and some Coverity checkers will have degraded results on code that uses Kotlin 2.1.0 preview language features, or language features introduced in Kotlin 2.2 or later. This is a known issue that will be fixed in a future release. |
| macOS |
| Windows (64-bit) |
