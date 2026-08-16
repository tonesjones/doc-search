---
title: "Patterns for C# and Java checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/patterns-for-c-and-java-checkers.html"
content_id: "~M7kRQIeZ8G4Z6_EfZ~RLw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:18.104086+00:00"
---

# Patterns for C# and Java checkers

The Coverity Extend SDK was originally used only to analyze C/C++ source code.
Now that the Coverity Extend SDK also supports the creation of checkers that
analyze C# and Java source code, you should note the following conventions when writing
such checkers:

- To match the use of a C# struct or class or Java class, use the pattern
  `StructType`. See TypePattern Superclass.
- The terms *function* and *method* are sometimes used interchangeably in
  the Coverity Extend SDK header files and documentation. To match a C#
  or Java method call, use the pattern `CallSite`. See Function call site expression patterns.
- To match the use of a C# or Java static field, use the pattern
  `StaticVar`. See Variable reference expression patterns.
- To match the use of a C# or Java instance field, use the pattern
  `Component`. Keep in mind that matching a non-static class
  instance field involves an implicit dereference. In other words, the code
  `obj.field` involves a dereference of the object reference
  `obj`. For a code example, see
  <install_directory>/sdk/samples/java_match_field.
  For more information, see Basic expression patterns.
- To match C# or Java references in an Coverity Extend SDK checker, you
  must use the `Pointer` pattern. The `Reference`
  pattern is only used for analyzing C/C++ code. Using the
  `Reference` pattern to analyze C# or Java code will not
  result in a match. See Type-filtered expression patterns.
