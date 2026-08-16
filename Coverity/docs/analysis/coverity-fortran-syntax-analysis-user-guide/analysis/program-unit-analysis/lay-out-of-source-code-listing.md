---
title: "Lay-out of source code listing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/lay-out-of-source-code-listing.html"
content_id: "nA0Wtf~Bgl14f9mcNZ4IGg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:35.445234+00:00"
---

# Lay-out of source code listing

A source code listing is generated if a listing file has been requested and both the
`-shsub` and the `-shsrc` options are in effect. To
make clear which part of fixed source records is being ignored, the source record past
column 72 of non-comment records is printed at column 83 and higher. Comment records,
however, are printed verbatim. If the `-allc` or the `-ff`
option is enabled, all records are printed verbatim.

Source input lines or statements are numbered as described in Line or statement numbering. If the `-shinc` option is
specified, input records which are read from an include file are presented with
hierarchical line numbers.

The pages on the listing file are numbered. When you use Coverity Fortran Syntax
Analysis’s library facility, a hierarchical page numbering system is provided. In that
case Coverity Fortran Syntax Analysis maintains a library version number which is
updated each time you insert or replace program units in the library. The page numbers
printed on the listing present the library version number and the page sequence number
as ”version.page”.
