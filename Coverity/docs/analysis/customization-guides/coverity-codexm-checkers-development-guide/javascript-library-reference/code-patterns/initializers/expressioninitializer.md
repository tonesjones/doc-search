---
title: "expressionInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressioninitializer.html"
content_id: "Y5rQelFk1HjjKDa2BKm17g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:02.254227+00:00"
---

# expressionInitializer

Matches expression initializers.

This pattern only matches nodes of type `initializer`.

## Properties

`expressionInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression that evaluates to the value used to initialize the object |

**Inherits properties from:**

- astnode
- initializer

## Example

Matches the initializer for the variable `a` in the following code:

[image: JavaScript code follows]

```
    var a = 0;
```

In this instance, the `.expression` property is the literal `0`.
