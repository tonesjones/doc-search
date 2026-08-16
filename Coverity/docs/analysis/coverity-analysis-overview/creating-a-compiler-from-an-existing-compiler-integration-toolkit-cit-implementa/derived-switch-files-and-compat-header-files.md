---
title: "Derived switch files and compat header files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/derived-switch-files-and-compat-header-files.html"
content_id: "yUdOjoy2hyab25LohDg~~w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:19.659553+00:00"
---

# Derived switch files and compat header files

A new switch file and compiler-compat header files can be created within the directory of the
new compiler. These files must abide by the current naming format. For example, if a new
derived compiler implementation is created in the directory
<install_dir>/config/templates/newcompiler, the switch file
must be named newcompiler_switches.dat, and compiler compat files
must use the existing naming formats unless the file is manually specified within the
configuration file as an extra compat file.

The derived compiler will use the compiler-compat headers and the switch files of the
compiler being derived from. Any additional files created in the new compiler directory
are added to those when creating the compiler-compat files during configuration. For the
switch files, additional switches can be added but existing switches cannot be
overridden.

Unless an `extern_trans` is specified, the usefulness of the
additional switch file is limited to those options that can be fully handled with
`oa_map`, or those options that just need to
be ignored. If additional functionality is required, such as manual handling in a
`pre_translate` function, then either a
regular, non-derived Compiler Integration Toolkit (CIT) implementation must be created
for the compiler requiring it, or an `extern_trans`
must be used in the derived compiler configuration.
