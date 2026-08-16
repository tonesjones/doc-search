---
title: "Changes to Swift code analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changes-to-swift-code-analysis.html"
content_id: "8AU18IMaE4XNuM51MVu94w"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:25.593121+00:00"
---

# Changes to Swift code analysis

With the release of Coverity 2021.9.0, the Sigma analysis engine is integrated into
Coverity Analysis. With this integration, Swift code analysis is performed with Sigma
(SIGMA.*) Swift checkers rather than the legacy Coverity Analysis Swift checkers,
resulting in the following changes and suggested actions for you to take:

- Analysis of Swift 5.5 (and above) code is now supported.
- To capture Swift 5.5 code, you must use the `coverity capture`
  command on Swift source files, instead of using the `cov-build`
  command.
- To capture Swift 5.4 code, you can still use `cov-build` or use the
  `coverity capture` command on Swift source files.
- Support is dropped for Swift user models (this applies to all Swift versions).

  Note: To those who currently analyze Swift 5.4 code and employ user models:

  After upgrading to Coverity Analysis 2021.9.0, you can still analyze
  Swift 5.4 code, but without the functionality of user
  models.
- To those with existing Swift issues in Coverity streams:

  If you want to retain
  existing issues that might not be covered by the new Sigma Swift checkers, then
  you should create new streams for subsequent Coverity scans of your Swift code.

  Note: Create the new streams after upgrading to the Coverity 2021.9 release
  but before running new analysis scans.

  By following this process, you
  will retain Swift issues that are not carried over by the Sigma analysis
  engine.
- If your Swift code analysis requires any of the removed Swift checkers, then you
  should continue using Coverity Analysis 2021.6 to analyze that code.
