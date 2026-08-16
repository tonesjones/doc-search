---
title: "closedVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/closedvariablesymbol.html"
content_id: "HQaBAMi24TXGJpWXnBjBug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:04.296529+00:00"
---

# closedVariableSymbol

Matches captured outer variables.

This pattern only matches nodes of type `symbol`.

## Properties

`closedVariableSymbol` does not expose any new properties.

**Inherits properties from:**

- symbol

## Example

In the following JavaScript example:

[image: JavaScript code follows]

```
    function myClosure() {
        var counter = 0;
        return function () {return counter += 1;}
    };
```

... the symbol representing `counter` in the returned lambda
matches `closedVariableSymbol`.

## See also

closedVariableReference
