---
title: "Silicon Graphics MIPSpro Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/silicon-graphics-mipspro-fortran-77-extensions.html"
content_id: "kzxLUjoXd586NtsyBoZiiQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:11.265541+00:00"
---

# Silicon Graphics MIPSpro Fortran 77 extensions

- cpp preprocessing is supported.
- By default the SGI Fortran 77 compiler supports C-string backslash editing. This
  can be disabled using the compiler option `-backslash`. Coverity
  Fortran Syntax Analysis supports backslash editing if extension 42 has been
  enabled in the configuration file, which is the default for the SGI compiler
  emulation.
- SGI Fortran 77 supports recursive subprogram references when the
  `-automatic` compiler option is specified during compilation.
  In Coverity Fortran Syntax Analysis extension 229 is enabled in the compiler
  emulation file to allow for recursion.
