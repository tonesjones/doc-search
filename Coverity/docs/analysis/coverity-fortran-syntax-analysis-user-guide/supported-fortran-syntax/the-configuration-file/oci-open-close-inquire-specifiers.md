---
title: "OCI (OPEN/CLOSE/INQUIRE) specifiers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/oci-open/close/inquire-specifiers.html"
content_id: "RxBS25y4zC~yvhApUkPauw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:15.836609+00:00"
---

# OCI (OPEN/CLOSE/INQUIRE) specifiers

Coverity Fortran Syntax Analysis recognizes all standard Fortran specifiers. Moreover,
the additional specifiers as specified in the configuration file will be recognized. You
can modify the configuration file and remove, add, or change the nonstandard specifiers
to be recognized.

Coverity Fortran Syntax Analysis can accept added specifiers which are standardized in a
higher Fortran standard level than the Fortran conformance level as specified in this
configuration file without reporting. You can group the added specifiers for each
language level. Each group must have one of the following headers:

```
!Fortran 90 additions
!Fortran 95 additions
!Fortran 2003 additions
!Fortran 2008 additions
!Fortran 2015 additions
```

The nonstandard compiler specific additions must be in a group with the following
header:

```
!Nonstandard additions
```

If you specify e.g. `-f03` only the specifiers which are not in the
Fortran 2003 standard are reported.

In the next paragraphs we describe the way specifiers can be specified in the
configuration file.

Each `OPEN`, `CLOSE` or `INQUIRE` keyword or
combination of keyword and value must be specified on a single record of the
configuration file. The list is delimited by a record with a zero. Each record has the
following format:

1. Keyword, string.

   If a keyword starts with the characters of another keyword, the longest
   keyword has to be specified first, or the ”`=`” must be included
   in the name of the shortest keyword. Specify a blank before the
   ”`=`” to allow non-significant blanks between the keyword and
   the ”`=`”. If a keyword may be split up in more than one part,
   separated by blanks (Fortran 90 free form input), include a blank in the
   specification at these positions.

   0.
   `OPEN`/`CLOSE`/`INQUIRE`
   indicator, character.

   ’`O`’ can be used in
   `OPEN` statement

   ’`C`’ can be used in
   `CLOSE` statement

   ’`I`’ can be used in
   `INQUIRE` statement

   Specify additional records with
   the same keyword for each statement type in which the keyword can be specified.
2. Value or value type, string.

   This field can either denote a value keyword (character
   constant), or the type of a variable value.

   If a value can be a value
   keyword, specify a value keyword in the value type field. Each keyword and value
   combination must be specified in a separate record. A value keyword cannot be
   shorter than two characters. If it has a length of two characters, it cannot end
   with an ’`R`’ or an ’`A`’. If a value keyword
   starts with the characters of another value keyword, this value keyword has to
   be specified first. If a value key­word may be split up in more than one part,
   separated by blanks, include a blank in the specification at these positions. A
   specific value keyword can be specified for two different open keywords and one
   close keyword.

   If the value can be a variable, the first character of the
   value type field denotes the type of the value.

   ’N’ no value expected

   ’ ’ any type allowed

   ’E’ external expected

   ’I’ integer
   datum expected

   ’K’ key description expected

   ’L’ label or logical
   expected

   ’C’ character

   ’U’ unit specifier expected

   ’V’
   scalar-default-char-variable expected

   The second character of the value
   type field denotes reference or assignment.

   ’R’ reference

   ’A’
   assignment

   For `OPEN` and `CLOSE` ’R’ is
   the default, for `INQUIRE` ’A’ is the default. Note that the
   value type and reference/assignment character are to be specified in a single
   string field, for example ’`IA`’ to denote an integer assignment.
3. Synonym keyword, string.

   Here you can specify for which keyword the keyword is a synonym.
   If the keyword is no synonym specify a blank string. If non-blank the value type
   field is not relevant. Synonyms will be flagged as nonstandard.
4. Standard Fortran specifier, logical.

   `T` The keyword is a standard Fortran
   specifier

   `F` The keyword is no standard Fortran
   specifier
