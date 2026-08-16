---
title: "I see a header file error: expected a ';'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/i-see-a-header-file-error-expected-a-.html"
content_id: "PpjulIyHcHi4xk7xNBn_yw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:22.653537+00:00"
---

# I see a header file error: expected a ';'

**Error:**

```
"/workarea09/wa_s30/desyin/removeFrag/sb8/swtools/all_platforms/tasking/c166v86r3/include/stdio.h", line 136: error:
      expected a ";"
extern   _USMLIB int    fscanf   ( FILE *, const char *, ... );
```

**Solution:**

This is due to the `_USMLIB` macro not being understood. There are three
possible solutions:

- A macro_candidate tag is needed to probe the compiler for this value during
  `cov-configure`.
- Another, totally independent macro needs to be defined so that this macro definition gets
  created.
- The macro must be defined on the command line every time the compiler is invoked (least
  likely)

It is possible that the native compiler will recognise this and convert it to another text
string during the compilation. In this case, you will need to work out what the new text
string means. If it has no effect on our analysis, then you can remove the original
macro by doing a `#define` of it (to nothing) in the
coverity-compat-compiler.h file in the
/template directory.
