---
title: "Advanced: Build"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-build.html"
content_id: "7J25jiHRYZA~NXugegocTA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:55.560491+00:00"
---

# Advanced: Build

Figure 1. Advanced: Build tab
[image: image]

If Using native builder settings is selected for
Strategy, the following options are available:

Additional cov-emit-java options
:   Specifies any additional options to be passed to
    `cov-emit-java`, during the java emit portion of the
    build.

Gradle Configuration
:   Specifies the Gradle configuration which will be built during local
    analysis.

    This field is only present if using Gradle.

    Note: Gradle users also need to configure the Coverity Desktop
    Gradle Plugin. See Local analysis with Gradle for
    details.

If Using custom settings is selected for
Strategy, the following options are available:

Command settings
:   This section contains the options for configuring custom build settings.

    Configure the following settings:

    - Clean command - Command line to clean
      (delete) artifacts produced by the build, so that the next build
      command will recompile all of the source code. For example,
      `make clean`.
    - Build command - Command line to compile the
      source code. For example, `make` (for C/C++) or
      `ant` (for Java).
    - Working directory - The clean and build
      command will be run from this directory.
    - Build incrementally - When enabled, selecting
      the Capture and Analyze button in the
      Uncaptured Source Files dialog will execute the build command and
      attempt to capture the uncaptured files. The custom Clean command is
      not executed.

      When running Capture build of Entire Scope,
      this setting is ignored and the custom Clean command is executed.

Build capture settings
:   - Use --record-with-source - When enabled, the
      build will also capture header file dependencies, which increases
      the breadth of your analysis, but may also slow down the process
      considerably.

Additional options
:   - Additional cov-run-desktop --build options -
      Additional options to pass to `cov-run-desktop`
      during the build. These will be appended to the list above. If there
      is a conflict, values defined here will be used.

    See the Coverity 2026.6.0 Command Reference for information on available
    `cov-run-desktop --build` options.
