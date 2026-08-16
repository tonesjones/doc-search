---
title: "Using modules"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-modules.html"
content_id: "8pwa9MYEauRpffD1PFnEBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:53.071649+00:00"
---

# Using modules

When importing modules with the USE statement, Coverity Fortran Syntax Analysis has to
import the public items of the module to analyze the code. Thus, the imported module has
to be analyzed before analyzing the code that imports it.

Coverity Fortran Syntax Analysis stores the public module information in a temporary
library file for later reference. If the modules are located in front of the importing
program unit or if they are in separate files and you analyze all files in one run, this
works fine without further intervention.

Coverity Fortran Syntax Analysis computes a module-dependency graph and analyses the
files in reverse-dependency order as required. In other cases you must analyze the
referenced modules first and store the result in a Coverity Fortran Syntax Analysis
library.

When analyzing the source code which references these modules you specify this library
file as a reference library.
