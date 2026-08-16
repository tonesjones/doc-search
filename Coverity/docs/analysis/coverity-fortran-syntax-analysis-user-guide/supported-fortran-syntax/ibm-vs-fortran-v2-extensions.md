---
title: "IBM VS Fortran V2 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ibm-vs-fortran-v2-extensions.html"
content_id: "4T9Y2J_~PvT6hSt36L6i7Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:06.066580+00:00"
---

# IBM VS Fortran V2 extensions

- In Coverity Fortran Syntax Analysis the maximum length for type character is set by
  default to 32767 for the VS Fortran emulation. The default for the VS Fortran
  compiler, however, is 500. A larger length for type character for the VS Fortran
  compiler is allowed when specifying the `CHARLEN(len)` compiler
  option. You also can adapt the Coverity Fortran Syntax Analysis configuration file
  used to have Coverity Fortran Syntax Analysis flag the usage of character lengths
  larger than 500.
- The free form source syntax is not fully supported. A continuation character in
  front of the on-line comment character (`!`) is not always
  detected.

- The `PROCESS` directive will be accepted, but the compiler options
  specified have no effect.
- The `INCLUDE` line is supported, but not conditional.
- `DEBUG` packets are supported, but with restrictions. Within debug
  packets all variables are supposed to have the implicit type, and no array-element
  references are allowed. Moreover, invalid transfer of control from and into debug
  packets will not be signaled.
- Asynchronous I/O and double byte characters are not supported.
