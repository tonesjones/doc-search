---
title: "Advanced: Build"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-build.html"
content_id: "yCeTeAUFtBdYO_tYFHWO3A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:13.500881+00:00"
---

# Advanced: Build

Figure 1. Advanced: Build tab
[image: image]

Strategy
:   Select whether to build your workspace using the Eclipse Java/CDT project
    builder, or specify your own build/clean commands. If you choose to build
    using custom settings, the Command settings section
    will be displayed, where you can specify your build commands and working
    directory. You can also enable incremental builds, which allows you to
    capture previously uncaptured source files for local analysis, without
    having to complete a full build of your entire project/workspace.

    For C/C++ projects in Eclipse, the Eclipse CDT (C/C++ Development Tools)
    provides Build Configurations. Build
    Configurations specify build processes to create different
    variants of a project. To create new configurations or specify the default
    configuration, access the Manage Configurations
    dialog from the Project Properties of a C/C++
    project.

Command settings
:   This section contains the options for configuring custom build settings. It
    is displayed only if you have chosen the Strategy
    option Using custom settings.

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
    - Detect JRE class shadowing - When enabled,
      the plug-in will attempt to prepend custom JRE classpaths to the
      value passed to `--bootclasspath` when running
      `cov-emit-java`. This will use custom classes
      instead of JRE classes of the same name. This option is available
      only if you have chosen the Using Eclipse Java/CDT
      project builder settings option.

Additional options
:   - Additional cov-emit-java options - Additional
      options to pass to `cov-emit-java` during the emit
      portion of the build. This option is available only if you have
      chosen the Using Eclipse Java/CDT project builder
      settings option.
    - Cov-run-desktop --build options - Options to
      pass to `cov-run-desktop` during the build. These
      are inherited from the coverity.conf file.
    - Additional cov-run-desktop --build options -
      Additional options to pass to `cov-run-desktop`
      during the build. These will be appended to the list above. If there
      is a conflict, values defined here will be used.

    See the Coverity 2026.6.0 Command Reference for information on available
    `cov-run-desktop --build` options.
