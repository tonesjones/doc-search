---
title: "integerLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integerliteral.html"
content_id: "yKENSb2tb7KjyusRJkMX_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:44.877089+00:00"
---

# integerLiteral

Matches integer literals; that is, all possible literal integer values.

This pattern only matches nodes of type `expression`.

## Properties

`integerLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `base` | `enum` | One of `` `binary` ``, `` `decimal` ``, `` `octal` ``, or `` `hexadecimal` ``. |
| `intKind` | `enum` | The kind of the integer type: See intKind. |
| `value` | `int` | The value of the integer literal |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only `long` integer literals:

  
 [image: CXM code follows]   

```
    pattern longIntegerLiteral {
        integerLiteral {
            .kind == `long`
        }
    };
```
