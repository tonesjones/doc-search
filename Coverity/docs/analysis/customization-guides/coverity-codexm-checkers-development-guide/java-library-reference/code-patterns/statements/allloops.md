---
title: "allLoops"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/allloops.html"
content_id: "w5afBrCVLCbVMxKTn9PQtw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:33.545718+00:00"
---

# allLoops

Matches all loop kinds.

The pattern matches `for` (simple or enhanced), `while`, and `do ... while` loop.

For specific patterns, with more details about each loop, refer to forLoopSimple,
forLoopEnhanced,
whileLoop, and
doWhileLoop.

## Properties

`allLoops` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern uses `allLoops` to determine if a `simpleStatement` contains a while loop expression:

  
 [image: CXM code follows]   

```
    pattern simpleStatementLoop {
        simpleStatement {
            .expression == allLoops
        }
    };
```

## See also

doWhileLoop,
forLoop,
forLoopEnhanced,
forLoopSimple,
whileLoop
