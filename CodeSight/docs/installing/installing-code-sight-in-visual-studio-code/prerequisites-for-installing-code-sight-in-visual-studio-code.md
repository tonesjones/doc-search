---
title: "Prerequisites for installing Code Sight in Visual Studio Code"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/prerequisites-for-installing-code-sight-in-visual-studio-code.html"
content_id: "7ZQJqE8tfhB24mVJXIAPxg"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.755028+00:00"
---

# Prerequisites for installing Code Sight in Visual Studio Code

Before you install the Black Duck Code Sight extension, you should make sure your system
is ready for it.

You should already have installed the following software:

- A supported version of Visual Studio Code

  You can download VS Code from
  <https://code.visualstudio.com/download>.

  CAUTION:

  These steps *do not apply* to Microsoft Visual Studio.
- A code project to work with

  For languages that Code Sight supports in Visual Studio Code, please see the
  Code Sight Support Matrix.

Important:
If you want to analyze source code written in a compiled language such as C, C++, C#, Java, and so on, then you need to
provide information about creating a build to the configuration file that you use.
See the following section, How do I enable Coverity (SAST) scans within Visual Studio Code?, for instructions on how to do so.

Important:
If you want to analyze Kotlin source code, then you also need to
provide Kotlin-specific information to the configuration file that you use.
See Set up Kotlin analysis for Eclipse, IntelliJ, or Visual Studio Code for instructions on how to do so.

For information about managing which scan engines have been installed and authenticated, please see
Authenticating and installing: Products and Licenses panel and the two procedure pages that follow it.
