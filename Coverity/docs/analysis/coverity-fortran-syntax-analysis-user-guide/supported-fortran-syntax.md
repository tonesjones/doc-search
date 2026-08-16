---
title: "Supported Fortran syntax"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/supported-fortran-syntax.html"
content_id: "JIHjleLXcUWkVHBysNt0AQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:55.611007+00:00"
---

# Supported Fortran syntax

Coverity Fortran Syntax Analysis supports the full Fortran 2015 syntax, which includes
Fortran 2008, Fortran 2003, Fortran 95, Fortran 90 and Fortran 77. Moreover, Coverity
Fortran Syntax Analysis supports many of the Fortran 2015 features and language
extensions of various compilers. Not all the vendor specific Fortran language extensions
which Coverity Fortran Syntax Analysis can support are enabled for a compiler being
emulated. The reason is that some of the language extensions are only provided to be
compatible with earlier versions of that compiler or now have standard Fortran
equivalents which you can use preferably. Moreover some of the extensions make a program
less secure, for example less strict type checking, so enabling these extensions will
weaken the possibilities of Coverity Fortran Syntax Analysis to detect programming
flaws. Coverity Fortran Syntax Analysis has, by default, enabled only those Fortran
language extensions which:

- Are generally accepted and have no standard Fortran equivalent, or are present in a
  more recent Fortran standard,
- Impose no risk and can be easily converted to standard Fortran,
- Improve the readability or the maintainability.

In the table in
Section A.3 on page
73–81 the language extensions, relative to Fortran 77, which are
supported by Coverity Fortran Syntax Analysis are listed. In the table in
Section A.4 on page
83–93 the language extensions, relative to Fortran 90 and Fortran 95,
which are supported by Coverity Fortran Syntax Analysis are listed.

In the tables you can see which extensions are supported by Coverity Fortran Syntax
Analysis and the various compilers. A ”+” denotes an extension which is by default
enabled by Coverity Fortran Syntax Analysis if the compiler emulation concerned has been
chosen. A ”o” denotes an extension which is by default not enabled. A ”@” means the
support of that particular extension is explained in the text.

You can enable or disable each of the listed extensions by editing the appropriate
configuration file. For Fortran 90, Fortran 95, Fortran 2003, Fortran 2008 or Fortran
2015 compilers you can use the respective default configuration file as a template. See
the section ”Changing
the configuration file”.
