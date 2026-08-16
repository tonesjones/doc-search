---
title: "Running Desktop Analysis from an editor or IDE"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-desktop-analysis-from-an-editor-or-ide.html"
content_id: "7SiGJagPUnVR9I0OhopN6A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:46.972266+00:00"
---

# Running Desktop Analysis from an editor or IDE

It is possible to run Desktop Analysis from your editor or integrated development environment
(IDE). Usage and configuration options are provided for some of the most common
platforms in the following sections. Some basic configuration is needed prior to running
local analysis from your editor, such as creating a coverity.conf
configuration file, setting up your PATH, and running the `--setup`
command. Be sure to complete these steps, as described in Desktop Analysis in an IDE, prior to running Desktop Analysis from your
editor or IDE.

Note: It is highly encouraged that one person (like an admin or team lead) create the
coverity.conf configuration file and check it into your Source
Code Management (SCM) repository, usually in the root directory. This will allow all
users to benefit from preconfigured settings.

If you are an Eclipse, Visual Studio®, IntelliJ, or Android Studio user,
it is recommended that you use the Coverity Desktop plug-in for use with Desktop
Analysis. More information on the plug-ins can be found in their respective usage
guides.

- For Eclipse, Wind River, or QNX, see the Coverity 2026.6.0 for Eclipse, Wind River Workbench, and QNX Momentics: User Guide.
- For Visual Studio, see the Coverity Desktop 2026.6.0 for Microsoft Visual Studio: User Guide.
- For IntelliJ or Android Studio, see the Coverity Desktop 2026.6.0 for IntelliJ IDEA and Android Studio: User Guide.
