---
title: "generatorReturnStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generatorreturnstatement.html"
content_id: "d9Y~Pte9dXxM9sh9YEki~w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:09.220903+00:00"
---

# generatorReturnStatement

Matches `return` statements in the body of generator functions.

This pattern only matches nodes of type `statement`.

## Properties

`generatoreReturnStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The `generatorReturnStatement` pattern matches the following two cases:

[image: JavaScript code follows]

```
    function* genX(x) {
        yield 1;
        return x;     // Case 1
    }
    function* gen() {
        yield 1;
        return;       // Case 2
    };
```

Note:
The generatorReturnValue pattern does
*not* match the second case.
