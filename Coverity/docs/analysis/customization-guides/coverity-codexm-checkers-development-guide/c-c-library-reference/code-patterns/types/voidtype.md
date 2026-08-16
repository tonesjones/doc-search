---
title: "voidType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/voidtype.html"
content_id: "zmacX3draf198SLaYy24LQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:24.895941+00:00"
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
