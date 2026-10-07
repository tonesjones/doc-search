---
title: "multiSubscriptReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/multisubscriptreference.html"
content_id: "KzGDEKtA2r~fm5k~0TlW1A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.036865+00:00"
---

# multiSubscriptReference

Matches expressions that use a multi-subscript operator on a multidimensional array.

This pattern only matches nodes of type `expression`.

## Properties

`multiSubscriptReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arrayExpression` | `expression` | The array the subscript is being used on |
| `indices` | `list<expression>` | The values inside the brackets ( `[ ]` ). |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all two-dimensional arrays:

  
 [image: CXM code follows]   

```
    pattern variableArrayLookup {
        multiSubscript as mss where mss.indicies.length == 2
    };
```
