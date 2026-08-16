---
title: "General configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/general-configuration.html"
content_id: "tdcD6lNf6_aR0RyfOOoyEA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:08.486899+00:00"
---

# General configuration

The General tab, as shown in the figure below,
specifies the disk locations of your Coverity Analysis tools, including
license files, as well as your code base directory.

This information is required for running local analysis and loading
shared settings from a coverity.conf file.

Figure 1. General tab
[image: image]

Static Analysis tools
:   The full path to your Coverity Analysis installation
    directory. This is required for local analysis.

License file
:   The location of your license.dat file, which contains your
    existing Coverity Analysis license. The default location is
    <install_dir>/bin.

Code base directory
:   The plug-in will store additional Coverity configuration information in the
    specified directory, as well as look for a
    coverity.conf file here. The
    coverity.conf file may be created by your Coverity Connect or analysis administrator, and used to
    specify configuration information common to all developers. See the Coverity
    Desktop Analysis
    2026.6.0 User Guide for additional details.

Use custom compilers configuration
:   This option allows you to specify a custom set of compilers for building the
    files in the current Analysis Configuration. If enabled, click
    Edit compiler configurations to open the
    Compiler Configuration dialog, and
    specify your project's compilers.

    If this option is left unselected, Coverity Desktop will
    use the default compilers, which are configured automatically. These
    include:

    - GNU C/C++ compiler (gcc)
    - Microsoft Visual C/C++ compiler (cl) - for Microsoft Windows
      only
    - Sun/Oracle compiler (javac)
    - Microsoft C# compiler (csc) - for Microsoft Windows only
    - Clang compiler (clangcc)
