---
title: "Standard conformance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/standard-conformance.html"
content_id: "RDh6PfQpnBCl9u0BvlIYTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:54.984901+00:00"
---

# Standard conformance

For optimal portability the program should be standard conforming. Coverity Fortran
Syntax Analysis verifies standard conformance very precisely when you specify the
`-standard` option. When this option is applied, Coverity Fortran
Syntax Analysis validates the syntax for conformance to the Fortran standard of the
level that is in effect (as determined by the compiler emulation chosen). All
nonstandard syntax will be flagged.
