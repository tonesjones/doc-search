---
title: "Configuration selection options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuration-selection-options.html"
content_id: "pOkfjFI4aGzHMTi~POaNsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:02.036199+00:00"
---

# Configuration selection options

Configuration files contain detailed compiler emulation information, including type
sizes, enabled language extensions, additional intrinsic procedures, checker enablement
and reported impact. The configuration files contain metadata which supports selection
among them using these criteria:

platform
:   The target hardware/OS for the compiler.

vendor
:   The organization that created or maintains the compiler.

version
:   The compiler version.

level
:   The language level (standard) supported by the compiler.

A configuration is selected using the corresponding `--platform`,
`--vendor`, `--version` and `--level`
options. If multiple configurations match the specified criteria, the first one in the
list is used but a warning is issued. If no configurations match the specified criteria,
an error is issued and `cov-run-fortran` halts.

A table of available configurations can be printed using the
`--list-configs` option. The `--configuration` option
can be used instead of the above four options to select a configuration file by name.
The `--config-path` option can be used to specify an alternate directory
to search for configuration files. By default, they are located in the
forcheck/share/ directory relative to the root of your Coverity
Analysis installation.
