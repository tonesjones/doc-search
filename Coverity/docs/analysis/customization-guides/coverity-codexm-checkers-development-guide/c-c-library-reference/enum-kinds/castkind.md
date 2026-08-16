---
title: "castKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castkind.html"
content_id: "PNBioNQfp3FB1g9tkVsQfQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:36.186896+00:00"
---

# castKind

Represents the various kinds of casts that C and C++ support.

## Details

The following values are defined:

| Name | Description |
| --- | --- |
| `` `explicit` `` | An explicit cast; for example, `(int)` a |
| `` `implicit` `` | An implicit cast |
| `` `static` `` | A C++ static cast |
| `` `dynamic` `` | A C++ dynamic cast |
| `` `reinterpret` `` | A C++ reinterpret cast |
| `` `const` `` | A C++ constant cast |

## See also

castOperator,
castOperatorConstCast,
castOperatorDynamicCast,
castOperatorExplicit,
castOperatorImplicit,
castOperatorReinterpretCast,
castOperatorStaticCast
