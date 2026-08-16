---
title: "forLoopOf"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopof.html"
content_id: "LgMaaKg7G7novf~TlyIdag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:07.362350+00:00"
---

# forLoopOf

Matches simple `for of` loops.

This pattern only matches nodes of type `statement`.

## Properties

`forLoopOf` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently, this is a blockStatement. |
| `iterableExpression` | `expression` | The iterable object |
| kind | `enum` | Always `` `of` `` |

**Inherits properties from:**

- astnode
- statement

## Example

The `forLoopOf` pattern matches the `for` loop in the following code:

[image: JavaScript code follows]

```
    function* l() {
        yield 1;
        yield 2;
    }
    for (var x of l()) {
        // ...
    };
```

## See also

forLoopIn,
forLoopSimple
