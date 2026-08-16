---
title: "System messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/system-messages.html"
content_id: "qcQeiktYXV84CsrOIB_WrQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:28.924930+00:00"
---

# System messages

When a problem arises in Coverity Fortran Syntax Analysis itself (like overflow of a
buffer), a system message in capitals between parentheses will show, for example:

`** [ 5 O] (TOO MANY PROGRAM UNITS, REMAINDER NOT PROCESSED).`

A system message is flagged with an `O` (overflow) or an `E` (error).
Analysis will proceed after an overflow message, the analysis,
however, is no longer complete. A system error is usually fatal.

System messages are sent to the report file and to the listing file if specified, or to
your screen or log file otherwise.
