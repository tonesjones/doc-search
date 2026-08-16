---
title: "function_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/function_t.html"
content_id: "Z8VLR8HiJJKU4UeYzMeW0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:59.835183+00:00"
---

# function_t

This class represents a function.

- `type_t *get_return_type` — Get the return type of this
  function.
- `function_type_t *get_ftype` — Get the function type.
- `bool is_virtual` — Determine if the method is virtual.
- `bool is_pure` — Determine if the method is pure virtual.
- `bool is_nonstatic_method` — Determine if the method is
  non-static.
- `bool is_static_method` — Determine if the method is
  static.
- `bool is_ctor` — Determine if the method is a constructor.
- `bool is_dtor` — Determine if the method is a destructor.
