---
title: "Verification of procedure references"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/verification-of-procedure-references.html"
content_id: "rRXktlFf0TMURYOt8YVIxw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:35.662466+00:00"
---

# Verification of procedure references

Coverity Fortran Syntax Analysis verifies the type of all references, the type, the type
length, the rank and shape of referenced functions. Conflicts of user procedure names
with intrinsic procedures are detected. When the `-ancmpl` has been
enabled, unreferenced procedures will be listed.
