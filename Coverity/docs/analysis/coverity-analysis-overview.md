---
title: "Coverity Analysis overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-overview.html"
content_id: "Nu4MDY7vVqmdC2afvB7z8A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:21.817826+00:00"
---

# Coverity Analysis overview

Coverity Analysis is built on top of a set of foundational technologies
that support the use of Coverity
checkers to detect quality issues (also called
quality defects) and security issues (potential security vulnerabilities). Issues found
by Coverity Analysis can cause data corruption, unpredictable behavior,
application failure, and other problems. Coverity Analysis analyzes
code bases to help minimize the number of software issues before your applications reach
the customer.

There are several possible approaches to running Coverity Analysis:

- You can run Coverity Analysis from the command line.

  Typically
  this is a first step to see whether Coverity Analysis is
  returning useful results. Once you are satisfied with the results of scans, you
  can integrate the analysis into your build pipeline.

  After an analysis scan has been run, you can view and manage the issues it has
  found by using Coverity Connect
  .
- Another way to run Coverity is to run it within the code editor you
  prefer by using the Code Sight plug-in/extension. This is a
  convenient way to run an analysis scan locally.
- Still another, older solution is to run local analyses of source code using the
  Coverity Desktop set of products.

This guide provides an overview of how to run and manage analysis scans.

Scope
:   This guide covers tasks for setting up and running static quality and security
    analyses in a centralized (server-based) build system.

    This guide also
    provides details on extending the set of compilers that are available to Coverity Analysis (see Using the Compiler Integration Toolkit (CIT)) and on using Coverity Analysis to commit third-party bugs and issues to
    Coverity Connect (see Using the Third Party Integration Toolkit).

Audience
:   The audience for this guide is administrators (including build engineers and
    tools specialists) and power users who set up and run the Coverity analyses in an integrated build environment. For details, see Roles and responsibilities.

To see how Coverity products work together, see Coverity Help Center.

In this section:

- Roles and responsibilities
- Use cases
- Capture models you can use
- Security considerations for running Coverity scans

## Additional reference material

For further information about the products mentioned in this section, see the
following resources:

Coverity Analysis
:   For installation instructions and supported platform details, see Coverity 2026.6.0 Installation and Upgrade Guide. Coverity Analysis
    component accessibility varies by license.

    Coverity 2026.6.0 Command Reference

    Coverity 2026.6.0 Checker Reference

Coverity Connect
:   Coverity Platform 2026.6.0 User and Administrator Guide

Polaris
:   [Black Duck
    Polaris Platform: Product overview](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-product-overview.html)

Code Sight
:   [Welcome to Code Sight](https://docs.blackduck.com/r/codesight/latest/code-sight-documentation/welcome-to-code-sight.html)

Coverity Desktop
:   Coverity Platform 2026.6.0 User and Administrator Guide

    Coverity 2026.6.0 for Eclipse, Wind River Workbench, and QNX Momentics: User Guide

    Coverity Desktop 2026.6.0 for IntelliJ IDEA and Android Studio: User Guide

    Coverity Desktop 2026.6.0 for Microsoft Visual Studio: User Guide
