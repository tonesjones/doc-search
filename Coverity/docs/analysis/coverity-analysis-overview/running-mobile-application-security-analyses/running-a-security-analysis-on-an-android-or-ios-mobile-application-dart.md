---
title: "Running a security analysis on an Android or iOS mobile application (Dart)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-a-security-analysis-on-an-android-or-ios-mobile-application-dart-.html"
content_id: "WKXQyOxp0UB9JzJEVby0Tg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:10.434465+00:00"
---

# Running a security analysis on an Android or iOS mobile application (Dart)

Coverity can perform a security analysis of either Android or iOS applications written in Dart™.

Coverity conducts a Dart analysis by invoking the Sigma analysis engine.
To access that engine, you must invoke the analysis
using the `cov-analyze` command, the CLI `coverity analyze` command,
or the CLI `coverity scan` command.
You must be running Coverity on a platform that supports Sigma,
and the Sigma engine must not have been disabled by command-line options.

Note:
The `cov-analyze` command does not require any
additional command-line options to enable Dart security analyses.
Dart security checkers are enabled by default.

Attention: The Coverity CLI has a known issue when
reading the Coverity Connect password in the Cygwin shell using the `coverity
setup` or `coverity scan` commands. To work around this
issue, run `coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.

The security analysis workflow follows the typical Coverity analyses workflow.
(See The capture: Examples.).
