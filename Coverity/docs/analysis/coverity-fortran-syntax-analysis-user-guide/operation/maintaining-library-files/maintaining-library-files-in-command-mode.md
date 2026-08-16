---
title: "Maintaining library files in command mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/maintaining-library-files-in-command-mode.html"
content_id: "oI8Fd39rNMoCzJMXG4EsAA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:22.444183+00:00"
---

# Maintaining library files in command mode

`fcklib` is an unsupported utility that can be used to maintain Coverity
Fortran Syntax Analysis library files. This utility can be found in the
forcheck/bin/ directory relative to the root of your Coverity
Analysis installation. With `fcklib`, you can list and remove program
units and compress the library.

`fcklib` is run by typing the `fcklib` command, with
options and library filename. The `fcklib` command line has the following
form:

```
fcklib options libraryfile
```

In interactive mode, you can enter the options and library filename as a respond to the
system prompt:

```
option(s) and library file?
```

When you specify the `-rm` option without any program unit names,
`fcklib` prompts for the names of the program units to be
removed:

```
program unit(s)?
```

You can enter a list of program units, separated by commas or blanks.

The default suffix of Coverity Fortran Syntax Analysis library filenames is
`.flb`. The following options are implemented:

`-batch`
:   Exit if error during command processing. Default: `-nbatch`.

`-help`
:   Present brief help. Default: `-nhelp`.

`-remove` *s*
:   Remove one or more program units from the library. The program unit names
    must be separated by a ”`,`”. Default:
    `-nremove`.

`-file remove` *f*
:   Remove all program units contained in the source file specified from the library. The filenames
    must be separated by a ”`,`”. Default: `-nfile
    remove`.

`-compress`
:   Compress the library. Default: `-ncompress`.

    Note: When `fcklib` compresses a library file, it creates a temporary file
    `.#fcklib.tmp`, which is deleted after successful
    compression. If, however, `fcklib` ends abnormally, the user
    will find this file on its current directory.

`-l`
:   List the program units contained in the library. Default:
    `-nl`.

If more options have been specified in the same command the `-rm` option
is carried out first. Then the library will be compressed, if asked for. Finally, if a
listing of library program units is requested, the program units will be shown.
