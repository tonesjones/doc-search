---
title: "cv_wrapper_type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cv_wrapper_type_t.html"
content_id: "bqDayt1OQ4n_vY4hsfpgyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:51.334525+00:00"
---

# cv_wrapper_type_t

This class represents a variant of an underlying type but with `const` or
`volatile` (or both) applied.

- `type_t target` — The type that is being wrapped with
  cv-qualifiers. Cannot be `cv_wrapper_type_t`.
- `v_flag_t flags` — Bitmap of cv-qualifiers being applied. Never
  0.
