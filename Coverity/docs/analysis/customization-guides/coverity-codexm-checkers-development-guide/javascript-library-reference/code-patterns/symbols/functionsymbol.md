---
title: "functionSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionsymbol.html"
content_id: "yWnZV4XotH306aPA5mzruQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:05.059632+00:00"
---

# functionSymbol

Matches function symbols.

This pattern only matches nodes of type `symbol`.

## Properties

`functionSymbol` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `functionType` | `type` | The type description of the function |

**Inherits properties from:**

- symbol

## Example

In the following JavaScript example:

[image: JavaScript code follows]

```
    function f() {
        // ...
    };
```

... `functionSymbol` matches the symbol representing `f()`.
