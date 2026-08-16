---
title: "scalar_type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scalar_type_t.html"
content_id: "jC0inynFqptxbDZ7mnzU7Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:48.039933+00:00"
---

# scalar_type_t

This class represents a fundamental type such as int. It has the
following fields and methods.

- `string name` — Name of the type. Possible values are:

  - `void`
  - `bool`
  - `char`
  - `signed char`
  - `unsigned char`
  - `short`
  - `unsigned short`
  - `int`
  - `unsigned int`
  - `long`
  - `unsigned long`
  - `long long`
  - `unsigned long long`
  - `float`
  - `double`
  - `long double`
- `int size` — Size in bytes of objects of this type.
- `bool m_is_float` — True if this type is a floating-point type
  (one of `float`, `double` or `long
  double`).
- `bool m_is_signed` — True if this type is any of the
  floating-point types, or one of the signed integer types.
