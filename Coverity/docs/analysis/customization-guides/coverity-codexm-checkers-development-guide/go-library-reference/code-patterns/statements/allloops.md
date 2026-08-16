---
title: "allLoops"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/allloops.html"
content_id: "NI6oXYq~aPry6USweW4gyg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:05.003213+00:00"
---

# allLoops

Matches all loop kinds.

The pattern matches both simple and enhanced `for` loops.

This pattern only matches nodes of type `statement`.

## Properties

`allLoops` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern uses `allLoops` to determine whether the `simpleStatement` is a loop:

  
 [image: CXM code follows]   

```
    pattern simpleStatementLoop {
        simpleStatement {
            .expression == allLoops
        }
    };
```

## See also

forLoop,
forLoopSimple
