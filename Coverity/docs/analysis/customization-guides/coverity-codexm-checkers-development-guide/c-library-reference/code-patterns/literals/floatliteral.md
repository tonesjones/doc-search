---
title: "floatLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floatliteral.html"
content_id: "e7URgTZ8Pylr82KCOPy6UQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:58.483123+00:00"
---

# floatLiteral

Matches floating-point literals.

This pattern only matches nodes of type `expression`.

## Properties

`floatLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isHexFloat` | `bool` | `true` if this float is represented using hexadecimal numerals |
| `suffix` | `enum?` | The suffix of the literal: either `` `f` `` or `null`. |
| `valueString` | `string` | The value of the `float`, represented as a string |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern:

  
 [image: CXM code follows]   

```
    f matches floatLiteral { .valueString == "2.5" };
```

... matches this target-code expression:

  
 [image: C# code follows]   

```
    float f = 2.5;
```
