---
title: "class_type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/class_type_t.html"
content_id: "DgbXyvGjbB8DfmdxV0Ufcg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:59.107428+00:00"
---

# class_type_t

This class represents a class or struct type.

- `bool m_is_struct` — True if this object represents a struct,
  false if it represents a class.
- `int size` — The size in bytes of this class.
- `parent_t parents[]` — The sequence of base classes.
