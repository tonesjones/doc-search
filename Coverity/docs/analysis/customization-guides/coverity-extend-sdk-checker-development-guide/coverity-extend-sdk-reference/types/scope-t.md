---
title: "scope_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scope_t.html"
content_id: "g07iia91wsneCKT6VIpSZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:53.354353+00:00"
---

# scope_t

This class represents a named scope in the program being analyzed.

- `string name` — Name of the scope mangled as defined by the
  IA64 C++ ABI.
- `string unmangled_name` — Un-mangled name of the scope.
- `scope_t parent` — Parent scope, or `NULL`.
