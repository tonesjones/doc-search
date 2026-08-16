---
title: "ForLoopKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopkind.html"
content_id: "128TRYeA2i6RJA_QU~TIdg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:54.170031+00:00"
---

# ForLoopKind

Represents either a simple or an enhanced for loop.

A simple for loop is of the form:

  
 [image: Go code follows]   

```
    for (int i; i < 10; i++) {
        // ...
    }
```

An enhanced for loop is of the form:

  
 [image: Go code follows]   

```
    for (i := mySet) {
        // ...
    };
```

The following values are defined:

| Name | Description |
| --- | --- |
| `` `enhanced` `` | An enhanced `for` loop |
| `` `simple` `` | A simple `for` loop |

## See also

forLoop,
forLoopSimple
