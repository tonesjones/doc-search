---
title: "forward_declarable_type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/forward_declarable_type_t.html"
content_id: "BaIOcr7R9JC5LQ_7mS9ttg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:58.908743+00:00"
---

# forward_declarable_type_t

This class is a superclass of the types that can be forward-declared: class/union or enum
only.

- `bool is_defined` — Indicates that the object is an
  internal_defined_class_type_t or
  internal_defined_enum_type_t, and the
  `as_defined` function can be called.
- `bool is_forward_declared` — Indicates that the type was
  forward-declared and the definition is not contained in the
  forward_declarable_type_t object itself.
  `is_forward_declared` is the negation of
  `is_defined`. To find out if a definition is available,
  use the `has_definition` function.
- `bool is_unnamed` — Indicates if the type was originally
  unnamed. The `get_name` function returns a generated
  name.
- `bool has_definition` — Indicates if there is a definition for
  this type.
