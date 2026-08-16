---
title: "Type verification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/type-verification.html"
content_id: "VANvaY0wXYVoib_wx7m~bA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:36.747927+00:00"
---

# Type verification

As part of the syntax analysis Coverity Fortran Syntax Analysis detects type conflicts.
In general the typing rules are applied more strictly than most compilers do. Type
checking is relaxed for typeless data and if the `-relax` option has been
enabled. Coverity Fortran Syntax Analysis signals implicit type conversions if they can
result in a loss of precision. Specifically, an error is reported when:

- A character datum is converted to a shorter type, or an integer is converted to a
  shorter integer.
- A real or complex expression is converted to a type with lower precision.
- A complex expression is converted to a real.
- A real expression is converted to a complex.
- A literal constant is specified in a type with lower precision than that of the
  target. This check is relaxed for the value zero.

If you specify the `-rigorous` option, any implicit type conversion will
be flagged. More­over, padding of character variables with blanks will be flagged unless
the right hand side of the assignment statement is a character constant with zero length
or consists of blanks only.
