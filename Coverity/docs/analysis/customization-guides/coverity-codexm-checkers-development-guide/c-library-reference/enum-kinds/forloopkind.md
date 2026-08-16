---
title: "ForLoopKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopkind.html"
content_id: "Y_lD5LNZ0eduSDIfejS~aw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:39.961976+00:00"
---

# ForLoopKind

Represents either simple or enhanced `for` loops.

A simple `for` loop is of the form:

[image: C# code follows]

```
    for ( int i; i < 10; i++ ) {
        // ...
    }
```

An enhanced `for` loop is of the form:

[image: C# code follows]

```
    foreach ( int element in fibNumbers ) {
        // ...
    };
```

## Details

The following values are defined:

| Name | Description |
| --- | --- |
| `` `enhanced` `` | An enhanced `for` loop |
| `` `simple` `` | A simple `for` loop |

## See also

forLoop,
forLoopEnhanced,
forLoopSimple
