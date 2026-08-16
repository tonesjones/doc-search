---
title: "Compiler integration overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-integration-overview.html"
content_id: "rLVO9n8VCYt2tHpkn5ta9A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:43.983982+00:00"
---

# Compiler integration overview

Coverity provides support for many native compilers. There are instances, however, when
the native compiler accepts non-standard code or has an option that the Coverity
compiler misinterprets or does not understand. Additionally, there are native compilers
for which Coverity does not provide support. The compiler integration for the Analysis
build system is highly configurable and can be customized to accommodate many different
compilers and code bases. This document describes many of the compiler integration
options and how to use the options to configure native compilers.

This document assumes that as a user of the Coverity Analysis build system, you are
familiar with `cov-configure` and the
coverity_config.xml configuration file. This configuration
describes information about a specific installation of a compiler, such as where the
configuration should search for system header files, what macros it defines, information
about the dialect of C/C++ it accepts, and so forth. This configuration tells the
Coverity Analysis build system how it should try to emulate the native compiler. The
Coverity Analysis build system can then intercept the calls of the native compiler to
facilitate the capture and understanding of the code base that is going to be
analyzed.

The Compiler Integration Toolkit (CIT) provides a mechanism for describing the general
behavior of a native compiler. A Compiler Integration Toolkit (CIT) configuration is
essentially a meta-configuration; its primary function is to tell the
`cov-configure` command how to generate a
coverity_config.xml file for a specific compiler installation.
The coverity_config.xml and the Compiler Integration Toolkit (CIT)
configuration XML use the same DTD and have much in common. Some of the other Compiler
Integration Toolkit (CIT) configuration files are passed through verbatim and will used
by the `cov-translate` command in addition to the
coverity_config.xml file.

Most compilers that are supported by Coverity have that support implemented as a Compiler
Integration Toolkit (CIT) configuration. These integrations have the most options for
customization and bug fixing. Some of Coverity's earliest compiler integrations are not
implemented using the Compiler Integration Toolkit (CIT) and are hard-coded into the
product. The customization of these implementations is limited and is achieved by
manipulating the coverity_config.xml file using the
`cov-configure --xml-option` option, or by editing the
coverity_config.xml file directly after
`cov-configure` runs.

The Coverity Analysis build system and the Compiler Integration Toolkit (CIT) provide the
flexibility to support many native compilers and code bases. For a list of native
compilers with successful integrations, see the Coverity 2026.6.0 Installation and Upgrade Guide.
