---
title: "HP-UX FORTRAN/9000 and HP Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/hp-ux-fortran/9000-and-hp-fortran-77-extensions.html"
content_id: "jsFEkP1kq741B4GtmpAqnQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:04.761713+00:00"
---

# HP-UX FORTRAN/9000 and HP Fortran 77 extensions

There are minor differences between the HP-UX FORTRAN/9000 compiler of the HP 9000/300
and 9000/700 series and the HP Fortran 77 compiler of the HP 9000/800 series.

- Though the HP Fortran compilers accept names up to 255 significant characters,
  Coverity Fortran Syntax Analysis considers only the first 64 characters as
  significant.
- HP compilers interpret a `!` as end of line comment when in column 1
  or in column 7 to 72. Coverity Fortran Syntax Analysis interprets a
  `!` in all columns but column 6 as end of line comment (as in
  Fortran 90). In Coverity Fortran Syntax Analysis the `ˆL` character
  is always processed as a formfeed. In HP-UX FORTRAN/9000, `ˆL` is
  only accepted when found in column 1 of an input record.
- The `INCLUDE` line and the `$include` compiler
  directive are both supported.

- All compiler directives are accepted. Some of them are processed and have the
  expected effect, such as `$LIST`, `$PAGE`,
  `$ANSI`. Others have no effect on the Coverity Fortran Syntax
  Analysis analysis, such as `$ALIAS`, `$INLINE`
  etc.
- cpp preprocessing is supported.
