---
title: "function_type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/function_type_t.html"
content_id: "MluZnrp7~sMkB3TEbGVFaQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:52.051304+00:00"
---

# function_type_t

This class represents a function type.

- `type_t args[]` — The sequence of argument types. For
  non-static methods, the receiver object (`this`) type is the
  first argument.
- `type_t return_type` — The return type of the function.
- `bool has_varargs` — If true, the function accepts a variable
  number of arguments. The `args` sequence has the required
  parameter types (those that precede `"..."`).
