---
title: "Analyzing your whole program with cov-run-desktop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyzing-your-whole-program-with-cov-run-desktop.html"
content_id: "oJ4w_OyogKKPl8o5kqUP0w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:00.303121+00:00"
---

# Analyzing your whole program with cov-run-desktop

If you emit your entire project and analyze it using `cov-run-desktop` and the
`--whole-program` option, you can run some checkers that are
otherwise not enabled for Desktop Analysis. Furthermore, other checkers, such as some
Java/.NET security checkers, are more effective if they can analyze your whole project
at once.

Before you run `cov-run-desktop` with the `--whole-program`
option, be sure that you have emitted all the source files in your project. The
`--whole-program` option tells `cov-run-desktop`
that you'd like to do a deeper (but slower) analysis. It also tells
`cov-run-desktop` that you've emitted your entire project, so that
it is reasonable to enable checkers that need to examine the entire project. (A
`--whole-program` analysis can yield poor results if it selects only
a subset of files from the project.)

Note: If you are using the Coverity Desktop plug-in for Eclipse to perform Desktop Analysis, this
behavior can be configured through the Analysis Configurations
dialog. See the Coverity 2026.6.0 for Eclipse, Wind River Workbench, and QNX Momentics: User Guide for more information.

If you are
using the Coverity Desktop plug-in for Visual Studio to perform Desktop Analysis,
this behavior can be configured through the Analysis
Configurations dialog. See the Coverity Desktop 2026.6.0 for Microsoft Visual Studio: User Guide for
more information.

If you are using the Coverity Desktop plug-in for IntelliJ
IDEA and Android Studio to perform Desktop Analysis, this behavior can be configured
through the Analysis Configurations dialog. See the Coverity Desktop 2026.6.0 for IntelliJ IDEA and Android Studio: User Guide for more information.
