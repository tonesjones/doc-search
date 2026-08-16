---
title: "floatLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floatliteral.html"
content_id: "AGgjEAI9b2dExAyjFqBVdA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:11.903652+00:00"
---

# floatLiteral

Matches `float` literals.

This pattern only matches nodes of type `expression`.

## Properties

`floatLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isHexFloat` | `bool` | `true` if this `float` is represented using hexadecimal |
| `suffix` | `enum>` | The suffix of the literal: either `` `f` `` or `null` |
| `valueString` | `string` | The value of the `float`, represented as a string |

**Inherits properties from:**

- astnode
- expression

## Example

The following Java expression:

  
 [image: Java code follows]   

```
float f = 2.5;
```

... could be matched using this CodeXM pattern:

  
 [image: CXM code follows]   

```
    f matches floatLiteral { .valueString == "2.5" };
```
