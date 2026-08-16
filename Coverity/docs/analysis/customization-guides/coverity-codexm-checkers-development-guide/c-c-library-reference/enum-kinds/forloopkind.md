---
title: "forLoopKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopkind.html"
content_id: "Z2vwez8SXTawquKp9xxVIg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:38.909469+00:00"
---

# forLoopKind

Represents either simple or range `for` loops.

## Details

A simple `for` loop is of the form:

  
 [image: C/C++ code follows]   

```
    for (int i; i < 10; i++) {
        // ...
    }
```

A range `for` loop is of the form:

  
 [image: C++ code follows]   

```
    foreach (int element : fibNumbers) {
        // ...
    };
```

The following values are defined:

| Name | Description |
| --- | --- |
| `` `range` `` | (C++) A `for` loop that uses the range expression introduced in C++11 |
| `` `simple` `` | A simple C or C++ `for` loop |

## See also

forLoop,
forLoopRange,
forLoopSimple
