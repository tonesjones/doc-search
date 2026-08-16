---
title: "Creating a compiler from an existing Compiler Integration Toolkit (CIT) implementation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-compiler-from-an-existing-compiler-integration-toolkit-cit-implementation.html"
content_id: "jjg~pTdX20OfsfpfgPoduQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:18.352983+00:00"
---

# Creating a compiler from an existing Compiler Integration Toolkit (CIT) implementation

You can create a new Compiler Integration Toolkit (CIT) compiler by deriving from an existing
Compiler Integration Toolkit (CIT) implementation. With this feature, you do not have to
compile new code to add a new compiler. All that is required is creating a new directory
for the compiler under the Compiler Integration Toolkit (CIT)
`<install_dir>/config/templates` directory AND a properly
formatted derived compiler configuration file within it. Optionally, a switch file as
well as additional `compiler-compat` files can be specified. This
functionality is only intended for compilers that are extremely similar to compilers
that already have Compiler Integration Toolkit (CIT) implementations.

The `pre_translate` function that gets used is the one that is specified
in the configuration file of the compiler from which it is being derived. Similarly to
how regular configuration files are structured, this can be overwritten through the use
of the existing `extern_trans` functionality.

In this section:

- Configuration format for derived compilers
- Derived switch files and compat header files
