---
title: "Local verification of argument lists"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/local-verification-of-argument-lists.html"
content_id: "QsBon_Bfax7tdB5TBBcW8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:37.400946+00:00"
---

# Local verification of argument lists

Within a program unit the argument list of each procedure invocation is compared with the
declared interface if the interface is explicit. If the interface is implicit, Coverity
Fortran Syntax Analysis tries to locate the interface in the temporary and specified
library files. If the interface is not found, the argument list is compared with that of
the first invocation.

The number of arguments, data types and data-type kind and length must correspond. When
an argument is a scalar in one invocation, the argument cannot be an array name in a
different invocation. In that case the message ”array versus scalar conflict” will be
presented.

An array element as an actual argument is compatible with both an array name and a
scalar. In that case the first occurrence, other than an array element, determines the
expected argument rank of the referenced procedure. If array shapes differ and the
`-rigorous` option is in effect, an error will be presented.

For argument lists of dummy functions and subroutines, all these checks are relaxed and
only informative messages will be presented.

Only the explicit interface specified or the first argument list of an implicit interface
of each invocation — augmented with type information as described — will be stored to be
used in the global program analysis.
