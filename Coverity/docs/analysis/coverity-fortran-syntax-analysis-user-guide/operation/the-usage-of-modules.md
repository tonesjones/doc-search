---
title: "The usage of modules"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-usage-of-modules.html"
content_id: "r96~Z6JPG3Yp6oUt9C2OcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:21.144708+00:00"
---

# The usage of modules

When Coverity Fortran Syntax Analysis encounters a USE statement it must have the public
information of the module at hand. So Coverity Fortran Syntax Analysis needs to analyze
the referenced modules before the reference is encountered. Therefore Coverity Fortran
Syntax Analysis analyzes the input files first for ”USE dependencies” and determines the
order to analyze the input files.

The public information of analyzed modules is stored in the specified create or update
library. If no create or update library has been specified this information is stored in
a temporary library file. See Coverity Fortran Syntax Analysis library files for information on how
to use library files.

You could also analyze modules first and store the public information in one or more
libraries. When analyzing the referencing program units you must specify these
libraries.
