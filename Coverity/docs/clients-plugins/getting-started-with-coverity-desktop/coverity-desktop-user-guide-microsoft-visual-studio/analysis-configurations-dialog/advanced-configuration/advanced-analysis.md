---
title: "Advanced: Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-analysis.html"
content_id: "YoTDbWIMETuvC34L~aU64A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:45.709495+00:00"
---

# Advanced: Analysis

Figure 1. Advanced: Analysis tab
[image: image]

Select checker settings
:   Your checker settings will be automatically selected by default, but you may
    choose to customize the list of configured checkers for analysis.

    - Coverity SDK checkers

      If you or your organization use customized checkers that were
      developed using the Coverity Software Development Kit, you can
      specify the location of the checkers. When you specify these
      checkers, they will appear in the list of checkers that you can
      enable through the Configure Checkers dialog.
    - Configure Checkers...

      This allows you to enable specific checkers for local analysis, and
      see detailed information on each one. Some checkers have additional
      options available, which you can configure by clicking
      Checker Options...

Cov-run-desktop options
:   Options passed to `cov-run-desktop` for local analysis.
    These are inherited from the coverity.conf file. See
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide for more information on
    coverity.conf.

Additional cov-run-desktop options
:   Specifies any additional options to be passed to
    `cov-run-desktop` during local analysis.

    These options will be added to those listed under the
    Cov-run-desktop options field. If there is a
    conflict, the options specified here take precedent.

Enable coding standard analysis
:   This is a general option that you can enable coding standards checkers for
    security and quality checkers of the selected coding standard configuration
    file(s). You can either use one of our provided configurations (found in
    <install_dir>/config/coding-standards) or you
    can choose to specify your own custom configuration file.

Import Microsoft® Code Analysis results (C# only)
:   Imports Microsoft Visual Studio Code Analysis (MSVSCA, also known as FxCop)
    results so that they can be viewed and triaged in Coverity Desktop. In order
    to import MSVSCA results, the MSVSCA analysis must be completed before you
    run the Coverity Desktop analysis. MSVSCA results are displayed similarly to
    other Coverity Desktop issues, but the checker name has a prefix of
    MS.*.

    You can enable Microsoft Code Analysis as part of the build process under the
    Code Analysis page of the C# Project
    Properties editor in Visual Studio. To ensure that Coverity
    Desktop imports the most recent results, this flag should be checked.

    Note: To avoid negatively impacting local analysis run time, you can make an
    alternate Analysis Configuration (named MS_AC for
    example) with Microsoft Code Analysis enabled. Then, when you need to see
    your Microsoft Code Analysis results, set your active Analysis Configuration
    to MS_AC and run your analysis as usual.

Select File Exclusions...
:   This will take you to the File Exclusions tab.

Use N processor cores
:   Specifies the number of cores to use for parallel analysis. The default is
    the smaller of the number of cores on the machine and the number allowed by
    the license file.
