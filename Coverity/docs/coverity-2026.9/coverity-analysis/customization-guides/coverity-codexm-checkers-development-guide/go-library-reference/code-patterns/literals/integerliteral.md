---
title: "integerLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/integerliteral.html"
content_id: "yKENSb2tb7KjyusRJkMX_A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:35.931965+00:00"
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
