---
title: "allLoops"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/allloops.html"
content_id: "dZrc8DCQfcVYtRey~oEg4g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:50.419123+00:00"
---

# allLoops

Matches all loop kinds.

The pattern matches `for` (simple/enhanced), `while` and `do ... while` loop statements.
For specific patterns, with more details about each kind of loop,
refer to forLoopSimple,
forLoopEnhanced,
whileLoop,
and doWhileLoop.

## Properties

`allLoops` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The following pattern uses `allLoops` to determine whether the `simpleStatement` is a loop:

  
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
whileLoop,
