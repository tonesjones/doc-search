---
title: "localVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/localvariablesymbol.html"
content_id: "O2POKJLNMj2llVImcPZXrQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:48.628537+00:00"
---

# localVariableSymbol

Matches locally defined variables.

This pattern only matches nodes of type `symbol`.

## Properties

`localVariableSymbol` does not expose any new properties.

**Inherits properties from:**

- symbol

## Example

In the following JavaScript source:

[image: JavaScript code follows]

```
    function f() {
        val a = "hello";
    };
```

... `localVariableSymbol` matches the symbol representing `a` in the function body.
