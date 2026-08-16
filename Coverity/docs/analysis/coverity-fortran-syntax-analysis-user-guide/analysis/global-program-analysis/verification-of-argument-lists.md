---
title: "Verification of argument lists"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verification-of-argument-lists.html"
content_id: "F9Sa7QBxA3K5yQcwdDiA9Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:47.143457+00:00"
---

# Verification of argument lists

The argument lists of each procedure reference is compared with the dummy (formal)
argument list of the analyzed procedure. When the referenced procedure has not been
analyzed, the argument lists will be compared with that of the interface definition
provided, or with that of the first reference. Verification is done as specified in
Program unit analysis.

Arguments are compared for type, and type parameters. If the `-rigorous`
option has been enabled and the rank or shape of array arguments differ, you are
informed. If a dummy array argument is longer than the actual an error is presented.

If an actual argument is a constant, expression, active DO variable, an active FORALL
index or if a variable is specified more than once in an actual argument list, then it
is invalid to modified the dummy argument in the procedure. In that case the message
”invalid modification” will be given with the reason. This check will only be performed
one reference level deep.

If the assigned dummy argument appears in more than one argument list of the entries of a
procedure, this verification is only carried out, as long as the entries are
disjoint.

If a dummy argument is not defined, or referenced before defined, the corresponding
actual argument must be defined before each reference. Because Coverity Fortran Syntax
Analysis’s limited path-flow analysis, referenced-before-defined of dummy arguments will
only be flagged as long as statements are guaranteed to be executed sequentially, or if
the `-rigorous` option is in effect.

When the actual argument is a literal constant without a kind parameter or a constant
expression of primaries without a kind parameter the type length is supposed to be the
default type length of the type of the constant or constant expression.
