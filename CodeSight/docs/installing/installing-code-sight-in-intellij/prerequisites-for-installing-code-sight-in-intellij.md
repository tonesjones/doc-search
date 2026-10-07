---
title: "Prerequisites for installing Code Sight in IntelliJ"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/prerequisites-for-installing-code-sight-in-intellij.html"
content_id: "iiXQdqObaXI2iTNphiq89w"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.060927+00:00"
---

# Prerequisites for installing Code Sight in IntelliJ

Before you install the Black Duck Code Sight plug-in, you should make sure your system is ready for it.

You should already have installed the following software:

- A supported version of a JetBrains environment

  You can download these IDEs from the JetBrains pages at
  <https://www.jetbrains.com/>.

  Note:
  The Community edition of IntelliJ IDEA supports Java but does not officially support scripting languages.
  However, in most cases Code Sight will find and report issues in the source for these languages as well.
- A code project to work with

  For languages that Code Sight supports in these IDEs, please see the
  Code Sight Support Matrix.

Important:
If you want to analyze Kotlin source code, then you need to
provide information about creating a build to the configuration file that you use.
See Set up Kotlin analysis for Eclipse, IntelliJ, or Visual Studio Code for instructions on how to do so.

For information about managing which scan engines have been installed and authenticated, please see
Authenticating and installing: Products and Licenses panel and the two procedure pages that follow it.
