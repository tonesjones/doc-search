---
title: "arrayLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayliteral.html"
content_id: "sRb0GWrJqsEsNy2HV5FDlw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:43.172137+00:00"
---

# arrayLiteral

Matches array literals.

An *arrayLiteral* (as specified in ECMAScript 2015, 12.2.5) is an expression that describes the initialization of an array object.

This pattern only matches nodes of type `expression`.

## Properties

`arrayLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `elementList` | `list<expression>` | The array elements |

**Inherits properties from:**

- astnode
- expression

## Example

The `arrayLiteral` pattern matches the initializer of `arr`:

[image: JavaScript code follows]

```
    var arr = ["a", "b", "c"];
```

The `.elementList` property is a list of three string literal expressions,
representing `"a"`, `"b"`, and `"c"`.

## See also

arrayElision,
spreadOperator

Both these patterns match special array elements.
