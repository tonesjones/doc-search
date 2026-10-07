---
title: "DEC PDP-11 Fortran-77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/dec-pdp-11-fortran-77-extensions.html"
content_id: "kVRpR21N~IQ1F5mog9GGoQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:36.634708+00:00"
---

# DEC PDP-11 Fortran-77 extensions

- DEC PDP-11 Fortran-77 does not support the full language, but an extended
  subset. Coverity Fortran Syntax Analysis does not signal the usage of
  unsupported full language Fortran 77 features, but optionally signals extensions
  to the full standard.
- The keyword VIRTUAL is supported but the limitations in usage will not be
  checked.
- DEC FORTRAN 4+ synonyms for Fortran 77 keywords in OPEN and CLOSE are supported,
  and are flagged.
