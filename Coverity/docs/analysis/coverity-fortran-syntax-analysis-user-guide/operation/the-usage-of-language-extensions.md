---
title: "The usage of language extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-usage-of-language-extensions.html"
content_id: "494pEaL6YOe88VhHdduP7A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:23.731977+00:00"
---

# The usage of language extensions

Coverity Fortran Syntax Analysis can analyze programs written in FORTRAN 66, FORTRAN 77,
Fortran 90, Fortran 95, Fortran 2003, Fortran 2008, and Fortran 2015. Moreover, Coverity
Fortran Syntax Analysis supports many language extensions of the various compilers. When
using language extensions a program can become less portable. Coverity Fortran Syntax
Analysis can be used to verify portability and to assist in converting Fortran programs
from one platform to another.

When specifying the `-standard` option, Coverity Fortran Syntax Analysis
flags all deviations from the Fortran standard of the level that is in effect, e.g.
Fortran 95 when a Fortran 95 compiler emulation has been chosen. If the program is
standard conforming, you will have minimal problems converting the program to platforms
which support the same or higher level of the Fortran standard. The `-obsolescent` option can be used to flag syntax which is marked as obsolescent in the Fortran
standard of the level in effect. The `-rigorous` option additionally
flags less portable code and indicates possible unintentional usage.

The Fortran language level, the types and language extensions of a compiler to be emulated are
specified in a configuration file. The configuration is selected from among the built-in
configuration files by using the `--platform`, `--vendor`,
`--version` and `--level` options. A specific
configuration file — including a custom configuration — can be selected using the
`--configuration` option.

The supported compilers are listed in Compilers supported. For each of the
supported compilers, a configuration file is supplied. These files can be found in the
`forcheck/share/` directory relative to your Coverity Analysis
installation root.

When operating in command line mode the default file name extensions (suffixes) of source and
include files are specified in the configuration file which can be adapted by the user.
See the tables with supported language extensions in Fortran 77 language extensions table and Fortran 90/95/2003/2008/2015 language extensions table.

When you want to enable different language extensions than the default you have to make a copy
of the appropriate configuration file and delete or add lines for the specific language
extensions. You can find the numbers of these extensions in Fortran 77 language extensions table and Fortran 90/95/2003/2008/2015 language extensions table and in the file
`fxdf.txt`.

You also can verify if the Fortran syntax extensions of the emulated compiler are accepted by a
higher Fortran level. E.g. when specifying the `-f03` option Coverity
Fortran Syntax Analysis flags all deviations from the Fortran 2003 standard.
