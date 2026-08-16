---
title: "ForLoopKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopkind.html"
content_id: "NjyWVAZwbg~Jp5NhXrbBKQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:23.088942+00:00"
---

# ForLoopKind

Represents either simple or enhanced `for` loops.

A simple `for` loop has the following form:

  
 [image: Java code follows]   

```
    for (int i; i < 10; i++) {
        // ...
    };
```

An enhanced `for` loop has the following form:

  
 [image: Java code follows]   

```
    for (int i : mySet) {
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
forLoopEnhanced,
forLoopSimple
