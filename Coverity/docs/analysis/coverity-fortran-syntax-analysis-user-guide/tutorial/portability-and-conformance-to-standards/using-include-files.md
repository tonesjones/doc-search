---
title: "Using include files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-include-files.html"
content_id: "ahTafmKeoHY9GDFC2_eq2Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:57.559898+00:00"
---

# Using include files

The syntax for the INCLUDE line or include preprocessor directive can vary with the
platform for which the program has been developed. Coverity Fortran Syntax Analysis can
handle most dialects. However, if you analyze the source on e.g. a Windows platform and
the target platform is Linux, it could be difficult to place the include files in the
correct directories. Using the `-I` you can specify where Coverity
Fortran Syntax Analysis must search for include files.
