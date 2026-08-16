---
title: "parameterSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parametersymbol.html"
content_id: "KFyswgEU2UCBalvQmvqgYQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:06.531403+00:00"
---

# parameterSymbol

Matches variables defined as parameters to functions.

This pattern only matches nodes of type `symbol`.

## Properties

`parameterSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isThis` | `bool` | Whether or not the symbol represents the implicit parameter `this` |
| `position` | `int` | The numerical position in the parameter list |

**Inherits properties from:**

- symbol

## Example

In the following example,

[image: JavaScript code follows]

```
    function f(a) {
        return a;
    };
```

... `parameterSymbol` matches the symbol representing `a` in the function body.
