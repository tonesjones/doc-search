---
title: "The Compiler Integration Toolkit (CIT) compiler configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-compiler-integration-toolkit-cit-compiler-configuration-file.html"
content_id: "lDyWXB948pDmBTfQAcKTyA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:10.377335+00:00"
---

# The Compiler Integration Toolkit (CIT) compiler configuration file

Coverity Analysis detects Compiler Integration Toolkit (CIT) implementations
in the <compiler>_config.xml file. The name of the compiler in
the configuration does not have to match the name of the file, but it must match the
name of the template directory, as it is what cov-configure looks
for when it searches for a compiler type. For example,
config/templates/qnx must have the configuration and switch
table named qnx_config.xml and
qnx_switches.dat, respectively. The compiler compatibility
headers must match the `comptype` specified in the configuration file;
one per `comptype` and must be named
compiler-compat-<comptype>.h.

The configuration file basically describes the following:

1. A high level description of the compiler, for example, compiler type, text description, and
   whether it is C or C++. It also describes the next configuration if multiple
   configurations are generated for a single binary.
2. Provides information to cov-configure that is useful for generating the
   configuration. For example, should the compiler attempt to dynamically determine
   what the correct sizes are for types? Or, what macros are actually defined so that
   you need not worry about adding a macro that is not present? You can also specify
   macros that you do not want `cov-configure` to detect.
3. Provides information about the options that the compiler uses, the switches used for
   compiling and preprocessing, and where the pre-process output is saved.

   The rest
   of the options section is copied verbatim into the generated compiler
   configuration and consists of a series of actions
   `cov-translate` is to take during the translation process.
   For more information, see Tags for phases of command-line transformations.

In this section:

- <cit_version> tag
- <compiler> and <variant> tags
- <options> tags specific to the Compiler Integration Toolkit (CIT)
- <config_generic_info> tags
