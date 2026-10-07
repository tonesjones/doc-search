---
title: "Backwards compatibility"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/backwards-compatibility.html"
content_id: "XDwE9oGf~~T~8NS9g1kyfw"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:09.144284+00:00"
---

# Backwards compatibility

For newly added features in coverity.conf that need to be used with older
versions of `cov-run-desktop`, the ext4 form may be used for
compatibility with older releases:

- The string `or` is equivalent to `:` (colon).
- The string `else` is equivalent to `=`
  (equals).
- The syntax `$(ext4_var_or_NAME)` is equivalent
  to `$(var:NAME)`.
- The `variables` property may be placed within
  an `ext4` property.
- Any other new attribute, property or condition, may be placed in an
  `ext4` element or property. This will include things like:
  - The configurations condition
  - The checkers and extend_checkers properties in the
    `CovRunDesktopSettings` object.
