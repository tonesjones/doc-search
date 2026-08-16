---
title: "Creating a Compiler Integration Toolkit (CIT) configuration for a new compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-compiler-integration-toolkit-cit-configuration-for-a-new-compiler.html"
content_id: "0D0QG0AtkQ3Rl90zjAzvHA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:17.708197+00:00"
---

# Creating a Compiler Integration Toolkit (CIT) configuration for a new compiler

Before you attempt to configure a new, unsupported compiler, there are a number of
templates available upon which you can base your configuration (if your compiler is
based on an existing compiler type). For example, some compilers are GNU compilers with
extensions and modifications that are specific to a particular industry. A number of
supported compiler configurations are located in the following directory:

<install_dir>/config/templates

If you do not have a compiler that can "share" configuration from one of the templates,
then you can start by using the /generic template directory.
