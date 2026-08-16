---
title: "Installing Coverity Analysis components"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-analysis-components.html"
content_id: "X0q5ILGMh8aIQohvsu3EWg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:50.225165+00:00"
---

# Installing Coverity Analysis components

This part of the guide is for administrators who install Coverity®
Analysis.

Coverity Analysis provides tools that you use to analyze your code bases and programs.
This document guides you through the steps of running the Coverity Analysis
installer.

Some of the analysis components that you can install include:

- Coverity Analysis – for analysis of compiled and interpreted code bases,
  including code used for Web applications.
- Coverity Extend SDK
- Coverity Desktop Analysis
- .NET Core SDKs
- Documentation:
  - English version
  - Japanese version
  - Korean version
  - Chinese version

Note: If you are upgrading an existing version of Coverity Analysis, see the Coverity 2026.6.0 Installation and Upgrade Guide.

Note that certain Coverity Analysis components are only available for certain platforms.
So, depending on the platform on to which you are installing, you might only be able to
access a subset of the analysis tools. For details, see Supported platforms for Coverity Analysis.

Coverity Analysis also uses Rapid Scan Static (the Sigma engine) on certain platforms
(see Supported platforms for Coverity Analysis). For the list of Sigma
checkers disabled by default when running Coverity Analysis, see "Checkers
disabled in Sigma when running Coverity Analysis" in the Coverity 2026.6.0 Checker Reference.

In this section:

- Downloading the Coverity Analysis installer from the Black Duck repository
- Installing Coverity Analysis
- Coverity Analysis installer modes
- Coverity Analysis license options
- Using an archive file to install Coverity Analysis
