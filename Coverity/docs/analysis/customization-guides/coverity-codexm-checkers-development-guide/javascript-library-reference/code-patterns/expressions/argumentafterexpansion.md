---
title: "argumentAfterExpansion"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/argumentafterexpansion.html"
content_id: "57FvLGW5TSP8OcssrvjxSQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:24.385833+00:00"
---

# argumentAfterExpansion

Matches boxed arguments after the list expansion argument.

This pattern only matches nodes of type `expression`.

## Properties

`argumentAfterExpansion` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `argumentExpression` | `expression` | The argument |

**Inherits properties from:**

- astnode
- expression

## Example

In the following JavaScript function call, `f(...l, 3)`, the `argumentAfterExpansion` pattern matches the
literal `3` argument :

[image: JavaScript code follows]

```
    function f(x, y, z) {
        return x + y + z;
    }

    var l = [1, 2];
    (...l, 3);
```

The `.argumentExpression` property is the expression `"3"`.

## See also

listExpansionArgument
