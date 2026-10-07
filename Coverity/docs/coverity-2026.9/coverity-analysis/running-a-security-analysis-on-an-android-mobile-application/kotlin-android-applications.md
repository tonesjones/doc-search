---
title: "Kotlin Android applications"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/kotlin-android-applications.html"
content_id: "Pr7Z~m75DA734xArtXfziw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:24.545332+00:00"
---

# Kotlin Android applications

Coverity can perform a security analysis of Android applications written in Kotlin.

Coverity conducts a Kotlin analysis by invoking the Sigma analysis engine. To access that
engine, you must invoke the analysis using the `cov-analyze` command, the
CLI `coverity analyze` command, or the CLI `coverity scan`
command. You must be running Coverity on a platform that supports Sigma, and the Sigma
engine must not have been disabled by command-line options.

**Note:** The `cov-analyze` command does not require any additional
command-line options to enable Kotlin security analyses. Kotlin security checkers are
enabled by default.

**Attention:** The Coverity CLI has a known issue when reading the Coverity Connect
password in the Cygwin shell using the `coverity setup` or
`coverity scan` commands. To work around this issue, run
`coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.

The security analysis workflow follows the typical Coverity analyses workflow. (See The capture: Examples)
