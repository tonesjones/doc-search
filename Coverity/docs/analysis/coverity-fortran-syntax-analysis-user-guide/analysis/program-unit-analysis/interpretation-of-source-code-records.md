---
title: "Interpretation of source code records"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/interpretation-of-source-code-records.html"
content_id: "k1FeLRuhU~fu395wVhexvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:34.789122+00:00"
---

# Interpretation of source code records

If you specify the `-ff` option Coverity Fortran Syntax Analysis reads the
source input in free source form, as supported by the compiler emulation chosen. If you
specify the `-standard`, `-f90`, `-f95`,
`-f03`, or `-f08` option as well, Coverity Fortran
Syntax Analysis reads the source input according to the Fortran 90 and up free source
form standard.

Tabs are expanded to blanks before the statement is processed. In fixed source form,
source lines are extended with blanks or truncated in the following way: If a source
line — after expansion of tabs — consists of less than 72 characters, it will be
extended with blanks to 72 characters. This is significant for character and Hollerith
constants. Any characters beyond column 72 are ignored, unless the `-allc` option is in effect.

Lower case characters are converted to upper case before interpretation, except within
character and Hollerith constants. If your compiler (as configured) does not accept
lower case characters, tabs or form feeds, one message only will be given for each
subprogram to inform you that you used lower case characters, tabs, or form feeds
respectively. Also if you use include files and this feature is not supported by the
configured compiler, only one warning for each subprogram will be presented.
