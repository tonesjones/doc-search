---
title: "Coverity Analysis deployment considerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-deployment-considerations.html"
content_id: "_Vrh5o6fsll7MyFjKIVn5Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:56.058779+00:00"
---

# Coverity Analysis deployment considerations

Software organizations often produce several products, each of which typically consists
of a number of related code branches and targets for supported platforms, product
versions, trunks, and development branches. The Coverity Analysis deployment needs to
analyze each code base on a regular basis so that the issues that developers see in
Coverity Connect reflect their changes to the code bases.

**To plan for your deployment:**

1. **Determine which types of analyses to run:**
   - Code base analyses
   - Incremental analyses, parallel analyses, or some other type of analysis
     process

     For details about these topics, see Analyzing source code interactively.

   As part of this process, you also need to perform the following tasks:

   1. **Determine which checkers to run.**

      By default, Coverity Analysis enables a set of checkers that are covered
      by your Coverity Analysis license. You can work with development team
      leads and power users to determine whether to enable additional checkers
      or disable other checkers (see Enabling/disabling checkers), and, if necessary, to create
      custom checkers (see Coverity
      CodeXM Checkers Development Guide).
   2. **Consider whether to model any functions or methods.**

      Modeling functions in third-party libraries, for example, can improve
      analysis results. For more information, see Using custom models of functions and/or methods.
2. **Plan Coverity Connect projects and streams for your analysis results:**

   To allow developers to view and manage their issues, administrators use Coverity
   Connect to define streams and group them
   into projects. For example, a technical
   lead might define a project that is composed of all the streams for a single
   software product. Such a project might include Linux, MacOS, and Windows target
   builds, along with multiple versions of each. A manager might need to see a
   project that consists of all the code streams in a given department.

   For
   additional information about this topic, see Prerequisites.
3. **Consider whether to push third-party issues to Coverity Connect so that
   developers and team leads can view and manage them along with their Coverity
   Analysis analysis issues.**

   For more information, see Using Coverity Analysis to commit third-party issues to the Coverity
   Connect database.
4. **Consider whether to use Coverity Desktop in conjunction with Coverity Analysis:**

   For details, see Coverity 2026.6.0 for Eclipse, Wind River Workbench, and QNX Momentics: User Guide and Coverity Desktop 2026.6.0 for Microsoft Visual Studio: User Guide.
5. **Think about how to integrate Coverity Analysis into your build system:**

   See Integrating Coverity Analysis into a build system.

   As
   part of this process, you also need to complete the following tasks:

   1. **Check Coverity Analysis platform and compiler support:**

      Refer to "Supported
      platforms" in the Coverity 2026.6.0 Installation and Upgrade Guide. If
      you are using a C/C++ compiler that is not supported, it is possible to
      extend the compatibility of compilers with Coverity Analysis. For
      details, see Using the Compiler Integration Toolkit (CIT).

      Note: For performance reasons, the following directories should
      not reside on a network drive:
      - The Coverity Analysis installation directory.
      - The intermediate
        directory. Instead, to maximize the performance of
        the analysis, this directory should reside on the build
        host.
      - The analyzed code.

      It is possible to run the analysis on a machine that is
      different from the one used for the build, even one with a different
      operating system or architecture, so long as the same version of
      Coverity Analysis is installed on both systems. This setup supports
      the specialization of machines, distributed builds, and the AIX
      platform, which does not have the `cov-analyze`
      command. To run an analysis on a different machine, you need to copy
      the self-contained intermediate directory to a local disk on the
      chosen host.

      **Reminder:** C# security analyses should run
      on Windows. Analyzing C# web applications on Linux is not supported.
   2. **Determine memory requirements for the analyses you intend to perform:**

      For details, see "Hardware and network recommendations and
      requirements" in the Coverity 2026.6.0 Installation and Upgrade Guide.
   3. **Determine the analysis interval:**

      Because developers continually modify the code base, regularly scheduled
      Coverity Analysis analyses are necessary to provide information about
      the introduction of new issues and the elimination of existing ones. For
      example, you might run the analysis on a nightly basis.
