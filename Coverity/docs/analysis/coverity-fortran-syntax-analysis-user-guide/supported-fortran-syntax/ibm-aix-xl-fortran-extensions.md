---
title: "IBM AIX XL FORTRAN extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ibm-aix-xl-fortran-extensions.html"
content_id: "6MVoKcmM5h030HMPzyJdDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:05.412071+00:00"
---

# IBM AIX XL FORTRAN extensions

- The XL Fortran compiler has no limit on the length of source records in
  free-form mode, Coverity Fortran Syntax Analysis only reads a maximum of 512
  characters.
- Though the XL compiler accepts tabs, a tab before a continuation character is
  not supported. Coverity Fortran Syntax Analysis accepts a tab before a
  continuation character.
- The XL Fortran compiler accepts names up to 250 significant characters, Coverity
  Fortran Syntax Analysis considers only the first 64 characters as
  significant.
- By default in Coverity Fortran Syntax Analysis the maximum length for type
  character is set to 32767 for the XL compiler emulation. The default for the XL
  Fortran compiler, however, is 500. A larger length for type character for the XL
  Fortran compiler is allowed by specifying the `CHARLEN(len)`
  compiler option or the `qcharlen=num` command line flag. You also
  can adapt the Coverity Fortran Syntax Analysis configuration file used to have
  Coverity Fortran Syntax Analysis flag the usage of character lengths larger than
  500.
- The free form source syntax is not fully supported. A continuation character in
  front of the on-line comment character (`!`) is not always
  detected.
- cpp preprocessing is supported.
- The `PROCESS` directive will be accepted, but the compiler
  options specified have no effect.
- The `INCLUDE` line is supported, but not conditional.
