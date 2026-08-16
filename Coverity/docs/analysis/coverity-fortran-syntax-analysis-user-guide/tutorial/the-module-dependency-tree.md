---
title: "The module dependency tree"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-module-dependency-tree.html"
content_id: "_ePij_doLhrLIYQpbVn2Ag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:51.744216+00:00"
---

# The module dependency tree

Coverity Fortran Syntax Analysis can present the dependencies of modules as a tree. You
can also specify specific modules for which you want to see the dependencies.

-shmoddep
:   Show the dependency tree of all modules.

-shmoddep *root list*
:   Show the dependency tree for the modules specified. The specified modules must
    be separated by a ”;”.
