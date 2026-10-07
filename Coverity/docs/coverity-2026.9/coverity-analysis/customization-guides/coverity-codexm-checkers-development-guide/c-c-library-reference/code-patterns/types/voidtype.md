---
title: "voidType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/voidtype.html"
content_id: "zmacX3draf198SLaYy24LQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:19.269825+00:00"
---

# voidType

Matches the `void` type.

## Properties

`voidType` does not expose any new properties.

## Example

In the following target source code, the return type of the function `test()`
is matched by `voidType`:

  
 [image: C/C++ code follows]   

```
void test() { /* ... */ };
```
