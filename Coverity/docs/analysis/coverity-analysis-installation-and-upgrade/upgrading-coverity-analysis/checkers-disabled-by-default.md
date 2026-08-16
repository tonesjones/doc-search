---
title: "Checkers disabled by default"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkers-disabled-by-default.html"
content_id: "Bph5wH7MUAcbvE3c3tm7cg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:19.890191+00:00"
---

# Checkers disabled by default

The following checkers are *disabled* by default: if no language is specified in the list
below, the checker is disabled for all languages; if a language is specified, it is only
disabled for that language.

- `ATOMICITY` (Java)
- `COM.ADDROF_LEAK`
- `COM.BSTR.ALLOC`
- `COM.BSTR.BAD_COMPARE`
- `COM.BSTR.NE_NON_BSTR`
- `INTEGER_OVERFLOW`
- `LOCK_INVERSION` (C#)
- `MIXED_ENUMS`
- `RISKY_CRYPTO` (C/C++/Objective-C/Objective-C++ only)
- `USE_AFTER_FREE` (Java)

To enable a checker, use the `–en` option on the
`cov-analyze` command line as follows:

`-en <CHECKER_NAME>`
