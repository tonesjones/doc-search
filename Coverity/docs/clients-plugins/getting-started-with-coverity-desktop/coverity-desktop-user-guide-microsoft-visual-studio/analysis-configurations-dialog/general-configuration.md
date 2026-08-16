---
title: "General configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/general-configuration.html"
content_id: "SMFFsUwBwl4Ap~Mc6sNLKA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:40.871993+00:00"
---

# General configuration

The General tab, as shown in the figure below,
specifies the disk locations of your Coverity Analysis tools, including
license files, as well as your code base directory.

This information is required for running local analyses and
creating authentication key files for connecting to Coverity Connect (see
Coverity Connect for details).

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
