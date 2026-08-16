---
title: "The usage of include files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-usage-of-include-files.html"
content_id: "880evhaCnko7AwF86oTPvg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:19.433652+00:00"
---

# The usage of include files

When Coverity Fortran Syntax Analysis encounters an INCLUDE line, or an include
preprocessor directive, it tries to open the include file specified. When an absolute
filename has been specified, as for example in
/usr/project/incfil.h, or ~/incfil.h it
opens that file.

When a relative filename has been specified, the search strategy differs among the
various platforms. Coverity Fortran Syntax Analysis conforms to this search strategy. On
most platforms the search strategy is as follows:

Coverity Fortran Syntax Analysis first tries to find the include file relative to the
directory of the current source file. Then Coverity Fortran Syntax Analysis tries to
find the include file relative to the current directory. Then it uses the directories as
specified by the `-I` dir option. If Coverity Fortran Syntax Analysis
cannot find the include file on the directories specified it tries to locate it on the
default include directory /usr/include.

On some platforms the strategy is different and is as listed in the next paragraphs.

**For HP/UX:**

When a relative filename has been specified Coverity Fortran Syntax Analysis first tries
to find the file on the directory of the source file in which the include directive has
been specified. Then it uses the directories as specified by the `-I`
option. If Coverity Fortran Syntax Analysis cannot find the include file on the
directories specified, it tries to locate it on the current directory and then on the
default include directory /usr/include.

**For IBM/AIX:**

When a relative filename has been specified Coverity Fortran Syntax Analysis uses the
directories as specified by the `-I` option. If Coverity Fortran Syntax
Analysis cannot find the include file on the directories specified it tries to locate it
on the current directory, after that it searches the directory of the source file and
then the default include directory /usr/include.

When you want to specify more than one include directory with the `-I` dir
option you must use a ”;”, a ”:”, or a ”,” as separator.

On IBM/AIX Coverity Fortran Syntax Analysis converts an IBM/MVS type filename”(xxx)” to
lowercase characters.

The default suffix for include files depends on the compiler emulation chosen. See the
sections on compiler emulations and supported Fortran syntax for more information.
