---
title: "Checker options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checker-options.html"
content_id: "Gq4kZaNwk5u5fqq1baRerg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:10.696706+00:00"
---

# Checker options

Numerous checker options let you adjust the checker's behavior. The most common
reason for using these options is to reduce the number of false positives or false
negatives.

**Use case:** Set the CSRF checker's `filter` option to detect
Java servlet and ASP.NET MVC filters.

For example, in analyses of Java source, the CSRF checker has been returning false
positives because it fails to detect filters that validate cross-site request tokens. By
explicitly naming the filters that do so, the `filter` option eliminates
these kinds of false positives.

**Use case:** Turn off the BAD_FREE checker's `allow_first_field`
option so the checker will report the freeing of a C/C++ structure's first
field.

Freeing the address of the first field of a C/C++ structure causes no harm, as the pointer is
equivalent to a pointer to the entire structure. However, it might indicate an error in logic.
Turning off `allow_first_field` enables reporting such an occurrence as a defect, so
developers can double check these situations.

**Learn more:** The chapter "Coverity Analysis checkers"
in the Coverity 2026.6.0 Checker Reference describes each built-in checker and the options
that the checker can use. For more information about tainted data options,
see Tainted data overview.
