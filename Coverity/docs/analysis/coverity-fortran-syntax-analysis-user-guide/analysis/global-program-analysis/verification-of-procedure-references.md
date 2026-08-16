---
title: "Verification of procedure references"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verification-of-procedure-references.html"
content_id: "rRXktlFf0TMURYOt8YVIxw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:46.512962+00:00"
---

# Verification of procedure references

Coverity Fortran Syntax Analysis verifies the type of all references, the type, the type
length, the rank and shape of referenced functions. Conflicts of user procedure names
with intrinsic procedures are detected. When the `-ancmpl` has been
enabled, unreferenced procedures will be listed.
