---
title: "Advanced: Build"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-build.html"
content_id: "S5jszfVGPH8z5Ul9MkTRww"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:44.785607+00:00"
---

# Advanced: Build

Figure 1. Advanced: Build tab
[image: image]

Build
:   Select whether to build your workspace using the built-in MSBuild engine, or
    specify your own build/clean commands.

Solution build configuration
:   This option depends on your selection of the Build
    option.

    If you choose to use the built-in build engine, you will have the option to
    choose the specific build engine from a drop-down menu.

    If you choose to use custom build settings, you will need to specify your own
    clean and build command, as well as your project's working directory.

Build capture settings
:   This field allows you to use the
    --record-with-source option with your
    build process. This causes the build to also capture header file
    dependencies, which increases the breadth of your analysis, but may also
    slows down the build process considerably.

Additional options
:   This field allows you to specify additional options to pass to the build
    command. See the Coverity 2026.6.0 Command Reference for information on
    available `cov-build` options.
