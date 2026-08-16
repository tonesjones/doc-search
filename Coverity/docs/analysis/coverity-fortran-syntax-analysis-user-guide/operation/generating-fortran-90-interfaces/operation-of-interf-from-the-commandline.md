---
title: "Operation of interf from the commandline"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-of-interf-from-the-commandline.html"
content_id: "TnPnk7m_ZDx8KeGR6pCxaw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:25.669269+00:00"
---

# Operation of interf from the commandline

This utility can be found in the forcheck/bin/ directory relative to
the root of your Coverity Analysis installation. The command line has the following
form:

```
interf [options] libraryfile outputfile
```

where `libraryfile` is the name of the Coverity Fortran Syntax Analysis library
file in which the information of the program units is stored. The default suffix of
Coverity Fortran Syntax Analysis library filenames is .flb.
`Outputfile` is the name of the file in which the generated module
with the interfaces will be stored. The default suffix is .f. The
following options are implemented:

-batch
:   Exit if errors occur during command processing. Default:
    `-nbatch`.

-help
:   Present help information on screen. Default: `-nhelp`.
