---
title: "booleanLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booleanliteral.html"
content_id: "XFWmBy17xi9DogrCcrOzMw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:09.154730+00:00"
---

# booleanLiteral

Matches Boolean literals; that is, both `true` and `false`.

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

The following CodeXM pattern matches all `true` values:

  
 [image: CXM code follows]   

```
    pattern trueBooleanLiteral {
        booleanLiteral {
            .value == true
        }
    };
```
