---
title: "listExpansionArgument"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/listexpansionargument.html"
content_id: "2Y075a_nzGUS2RfGaJ_Gkw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:33.550771+00:00"
---

# listExpansionArgument

Matches instances of spread syntax in JavaScript function calls.

Spread syntax allows an iterable to be used as an argument.

This pattern only matches nodes of type `expression`.

## Properties

`listExpansionArgument` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `listExpression` | `expression` | The list to be expanded |

**Inherits properties from:**

- astnode
- expression

## Example

The `listExpansionArgument` pattern matches the argument in the following
function call `f(...l)`:

[image: JavaScript code follows]

```
    function f(x, y, z) {
        return x + y + z;
    }

    var l = [1, 1, 1];
    f(...l);
```

The `.operandExpression` property is the expression `l`.

## See also

argumentAfterExpansion,
spreadOperator (which uses syntax similar to that used for an array literal)
