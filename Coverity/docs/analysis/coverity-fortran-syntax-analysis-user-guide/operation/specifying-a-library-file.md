---
title: "Specifying a library file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-a-library-file.html"
content_id: "LfzmJblW4soyNEdLKIpqGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:00.749890+00:00"
---

# Specifying a library file

Files with a name with a `.flb` suffix or filenames preceded by one of the
library options are considered to be Coverity Fortran Syntax Analysis library files.
They must be specified after the source input files, if any. When a library file is not
specified, Coverity Fortran Syntax Analysis will store all global program-unit
information in a scratch file, which will be deleted when Coverity Fortran Syntax
Analysis has completed. You can, however, save this global program-unit information by
specifying a Coverity Fortran Syntax Analysis library file. In subsequent Coverity
Fortran Syntax Analysis runs you can reference and update this library file. For
detailed information, see the section on the usage of library files.
