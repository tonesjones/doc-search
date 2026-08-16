---
title: "Running a security analysis on an iOS mobile application (Swift)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-a-security-analysis-on-an-ios-mobile-application-swift-.html"
content_id: "93p1qQk6u_A6k6qwRHUT2g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:09.787930+00:00"
---

# Running a security analysis on an iOS mobile application (Swift)

Coverity can perform a security analysis of iOS applications written in Swift.

Coverity conducts a Swift analysis by invoking the Sigma analysis engine.
To access that engine, you must invoke the analysis
using the `cov-analyze` command, the CLI `coverity
analyze` command, or the CLI `coverity scan` command.
You must be running Coverity on a platform that supports Sigma,
and the Sigma engine must not have been disabled by command-line options.

Note:
The `cov-analyze` command does not require any
additional command-line options to enable Swift security analyses. Swift iOS security
checkers are enabled by default.

Attention: The Coverity CLI has a known issue when
reading the Coverity Connect password in the Cygwin shell using the `coverity
setup` or `coverity scan` commands. To work around this
issue, run `coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.

Since the 2021.12.0 release of Coverity, Swift is now captured without a build command, and you must use
the Coverity CLI capture subcommand (`coverity capture`) to capture
Swift code. There is no support to capture Swift source code using
`cov-build`. All versions of
Swift code are supported. The Coverity CLI also captures other files that might be
relevant to the analysis including configuration files. For more information, see the
description of the `coverity capture`
command in Coverity 2026.6.0 Command Reference.

The security analysis workflow follows the typical Coverity analyses workflow.
(See The capture: Examples.).
