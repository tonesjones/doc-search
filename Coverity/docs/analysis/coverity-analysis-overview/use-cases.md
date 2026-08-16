---
title: "Use cases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/use-cases.html"
content_id: "FiZ42YVe7Uxr7LNnNdpvZw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:23.745069+00:00"
---

# Use cases

Coverity Analysis supports a number of use cases:

Running analyses with Coverity Analysis
:   Each analysis uses a set of commands that vary by
    programming language and analysis type.
    To get started with Coverity Analysis, you can run analyses from the command line.

    Once you are familiar with the basics of Coverity Analysis and are satisfied with
    the results of your scans, you can create a server-based script
    that integrates Coverity Analysis into your build pipeline and regularly runs the commands needed to analyze your code base.

    For more information about common analysis tasks, see Analysis with Coverity Checkers.

    For more information about pipeline integration, see Setting up Coverity Analysis for a production environment.

Enabling or disabling checkers
:   Coverity Analysis uses checkers to
    analyze your code base for specific types of issues. By default, Coverity Analysis enables a certain set of checkers.

    To control the depth and nature of the analysis, you can work with Coverity Analysis power users
    (see Roles and responsibilities) to determine whether to change the
    set of checkers that are enabled.
    For details, see Enabling or disabling checkers.

    Note:
    It is possible to extend the set of checkers that is available to Coverity Analysis.
    See Coverity
    CodeXM Checkers Development Guide.

Using custom models of functions and/or methods
:   A *model* summarizes the behavior of a function or method.
    Coverity Analysis allows you to integrate custom models into the analysis.
    For details, see Using custom models to improve analysis results.

Extending C/C++ compiler compatibility
:   Coverity Analysis supports a number of C/C++ compilers
    (see "C/C++ compilers" in the
    Coverity 2026.6.0 Installation and Upgrade Guide).

    To extend the set of C/C++ compilers
    that are compatible with Coverity Analysis,
    see Using the Compiler Integration Toolkit (CIT).

Using Coverity Analysis to commit third-party issues to the Coverity Connect database
:   In addition to supporting the management of software issues found by Coverity Analysis, Coverity Connect
    supports issues found by third-party tools.

    The Third Party Integration Toolkit relies on Coverity Analysis to commit third-party defects to
    the Coverity Connect database.
    See Using the Third Party Integration Toolkit.
