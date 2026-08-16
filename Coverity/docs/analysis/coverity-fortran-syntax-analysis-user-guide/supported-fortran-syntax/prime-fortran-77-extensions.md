---
title: "Prime Fortran-77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/prime-fortran-77-extensions.html"
content_id: "kY1XRjChNjGwBNTpvppm9w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:09.945635+00:00"
---

# Prime Fortran-77 extensions

- In-line comment between /* and */ is not supported anymore.
- The maximum number of continuation lines allowed depends for Prime Fortran on
  how many language elements each line contains. Coverity Fortran Syntax Analysis
  allows 19 continuation lines by default.
- Both the `INCLUDE` line and the `$INSERT` directive are supported.
- The B-field edit descriptor is not supported.
- The `SHORTCALL` statement is not supported.
- The `FULL LIST` compiler directive is not supported.
