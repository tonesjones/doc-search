---
title: "General language extensions supported"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/general-language-extensions-supported.html"
content_id: "fD9bVuvgFyXfDl7zCEmQAA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:57.011397+00:00"
---

# General language extensions supported

- Tab formatting is supported when fixed form source is enabled. If the first column
  of a fixed form input record consists of a tab succeeded by a digit as continuation
  character, then the continuation character will be located at column 6 and the next
  characters from column 7 on. If this tab is not followed by a digit the next
  characters are placed from column 7 on. Subsequent tabs, or tabs in columns past the
  continuation field are expanded to blanks to columns 9, 17, 25, etc., before
  processing the statement.

  This is different from the way some compilers will treat
  tabs. Some compilers consider tabs after column 6 as one blank character or
  discard tabs at these positions. Because of this difference Coverity Fortran
  Syntax Analysis may locate characters past column 72, discarding them, while the
  compiler will not.

  This way has been chosen because an expansion of tabs
  will generally be used when source code is transformed to standard Fortran 77,
  or when sending your program to a different computer system. Moreover, the
  compiler will probably expand tabs in the source listing. In the Coverity
  Fortran Syntax Analysis way you can see which characters will be interpreted by
  any compiler and which may not.

- Though some compilers accept longer source records (e.g. in free form), the maximum
  record size Coverity Fortran Syntax Analysis can read is 512 characters, after
  expansion of tabs and of cpp macros.
- Though some compilers support an unlimited number of continuation lines Coverity
  Fortran Syntax Analysis can read up to 999 continuation lines.
- `LOGICAL*1` data are treated as logicals. `BYTE` data
  as integers.
- The nonstandard form of the `PARAMETER` statement (without
  parentheses) is not equivalent to the standard Fortran `PARAMETER`
  statement. In the nonstandard form the type of the named constant takes the type of
  the literal constant, which may be different from that of the implicit or specified
  type of the name using the Fortran 77 syntax.
- Though a specific compiler may support longer names, Coverity Fortran Syntax
  Analysis supports names of up to 64 characters only.
- Some compilers support directives which are identified by a key in the first columns
  followed by a keyword. These compiler directive strings can be specified in the
  con­figuration file. Some of these directives will not only be accepted, but also
  interpreted by Coverity Fortran Syntax Analysis: see the notes on each specific
  compiler emulation.
- Some compilers support directives using keywords in column 7-72. Detection of these
  keywords can be enabled if the keyword is present in the tables of Fortran language
  extensions.
- Coverity Fortran Syntax Analysis can handle cpp preprocessor directives. cpp
  pre­processing is enabled by enabling extension 7 in the configuration file. You can
  also enable or disable cpp preprocessing using the enable cpp command line option or
  by setting this option in the IDE. Parametrized macro expansion is supported with
  some limitations. The macro must be on a single line and variadic macros are not
  supported. Macro expansion must be used with great care because it can cause
  significant characters be placed beyond character position 72 in fixed source format
  and change character constants. If a file includes another file with the Fortran
  IN­CLUDE statement, the included file is not preprocessed. Files included using the
  cpp directive #include are preprocessed.

The usage of language extensions will be flagged when the `-standard`, the
`-f77`, the `-f90`, the `-f95`, the
`-f03`, the `-f08` or the `-f15` option
has been specified. By specifying the `-obsolescent` option all language
features which are marked as obsolescent in the Fortran standard which is in effect will
be flagged.
