---
title: "Coverity Fortran Syntax Analysis library files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-fortran-syntax-analysis-library-files.html"
content_id: "_Emf3HlIweDydfNspYjNUQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:20.070072+00:00"
---

# Coverity Fortran Syntax Analysis library files

Coverity Fortran Syntax Analysis stores the global information of all program units in a
Coverity Fortran Syntax Analysis library file. You can save this file for later
reference. The first time you specify a library file it has to be created using the
`-create` option. If global program analysis is in effect (this is
the default) all information from the library file is included in the global
analysis.

New or modified program units can then be analyzed and their global information stored or
replaced in the library. To update the library, you specify the library file with the
`-update` option. If global program analysis is in effect, all
information from the library will again be included in the global analysis.

When the global information of the program units of a program has been stored in one or
more libraries in this way, you can analyze the program units in the context of the
entire program by referring to these libraries. Now all implicit interfaces are known to
Coverity Fortran Syntax Analysis and all references of subprograms can be verified.
Coverity Fortran Syntax Analysis scans the libraries in the specified order and includes
all referenced pro­gram units found in the global analysis. Each individual library is
searched recursively until no references are resolved any more.

You can force Coverity Fortran Syntax Analysis to include all or only specific program
units from a library in the analysis.

When you specify only library files as input, Coverity Fortran Syntax Analysis will
per­form a global program analysis, and presents the reference structure and program
cross references if requested. All information contained in the first library file will
be included in the analysis by default. The other libraries are searched for referenced
program units as previously explained.

When you want to create a library file you specify the `-create` option.
The library file will be created and the global information of the analyzed program
units will be stored in this library file. For example:

```
cov-run-fortran --dir idir -- test.f -create testlib.flb
```

will analyze the source file test.f and place the global information
in the newly created library file testlib.flb.

New or modified program units can then be analyzed and their global information stored or
replaced in this library file by specifying the library file with the
`-update` option. For example:

```
cov-run-fortran --dir idir -- test.f -update testlib.flb
```

will analyze the source file `test.f` and replace the global information
in the library file `testlib.flb`.

Now you can analyze new or changed program units in the context of the entire program by
referring to previously created libraries. When libraries are specified using the
`-library` option, Coverity Fortran Syntax Analysis merely references
the specified libraries. It uses the library information to resolve global references,
but does not analyze or update the specified libraries. For example:

```
cov-run-fortran --dir idir -- test1.f -library testlib.flb
```

will analyze the source file `test1.f` and verify the procedure
references, common blocks etc. of all references which reside in the library file
`testlib.flb`.

By specifying the `-include` option you can force Coverity Fortran Syntax
Analysis to include all or specific program units from a library in the analysis. For
example:

```
cov-run-fortran --dir idir -- test1.f -library -include sub1,sub2 testlib.flb
```

will analyze the source file `test1.f` and verify the procedure references
of the program

units SUB1 and SUB2 which reside in the library file `testlib.flb`.

In the next two examples we analyze library files only:

```
cov-run-fortran --dir idir -- -library projectlib.flb -lib plotlib.flb
```

will analyze the program consisting of all program units contained in the library file
`projectlib.flb` and all references found in the library file
`plotlib.flb`.

```
cov-run-fortran --dir idir -- -library projectlib.flb -incl plotlib.flb
```

will analyze the program consisting of all program units contained in the library files
`projectlib.flb` and `plotlib.flb`.

You can delete, compress and list the information of program units in the library file
using the unsupported utility `fcklib`. See Maintaining library files for further information.
