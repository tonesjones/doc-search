---
title: "booleanLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/booleanliteral.html"
content_id: "2Xzi4bz2vSHt4QvlXfw9Rg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.900603+00:00"
---

# booleanLiteral

Matches Boolean literals: that is, either `true` or `false`.

This pattern only matches nodes of type `expression`.

## Properties

`booleanLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `enum` | `` `true` `` or `` `false` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all literal Boolean values:

  
 [image: CXM code follows]   

```
    pattern trueBooleanLiteral {
        booleanLiteral {
            .value == true
        }
    };
```
