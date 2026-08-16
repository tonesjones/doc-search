---
title: "Compiler emulation and include files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-emulation-and-include-files.html"
content_id: "KYjKJMg_jwzijgLi5qwwyA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:24.387427+00:00"
---

# Compiler emulation and include files

When you analyze a Fortran source program on a host computer the `INCLUDE` lines
must be processed by Coverity Fortran Syntax Analysis so the include files must be
opened and read on the host system. Therefore Coverity Fortran Syntax Analysis will not
verify the syntax of the filename specified in the `INCLUDE` line for
conformance to the syntax of the emulated compiler, but allows for the various syntaxes.
So, for example, the VAX Fortran syntax `INCLUDE ’(INCL1)/NOLIST’` and
`INCLUDE ’MODEL:INC1’` will be accepted on all systems. However, you
cannot use the syntax `INCLUDE ’[USER.PROJ]INCLIB(INCL1)’` on non-VMS
systems because on non-VMS systems Coverity Fortran Syntax Analysis cannot open a member
of an include library file. The VMS symbolic path (like MODEL: in the ex­ample) is
stripped by Coverity Fortran Syntax Analysis to allow the file to be found on non VMS
systems.

Bear in mind that when emulating a certain compiler, the default file name extension
(suffix) of include files is taken from the configuration file used so it adapts to the
defaults of the system and compiler chosen. See also The usage of language extensions.
