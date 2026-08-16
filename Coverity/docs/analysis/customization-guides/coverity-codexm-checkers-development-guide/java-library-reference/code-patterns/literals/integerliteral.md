---
title: "integerLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integerliteral.html"
content_id: "ckl3A9ssxnwK3CY96BAFWg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:12.640611+00:00"
---

# integerLiteral

Matches all integer literals. That is, all integer literals of the kind `` `short` ``, `` `byte` ``, `` `int` ``, and `` `long` ``.

## Properties

`integerLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `base` | `enum` | One of `` `binary` ``, `` `decimal` ``, `` `octal` ``, or `` `hexadecimal` `` |
| `kind` | `enum intKind` | One of `` `short` ``, `` `byte` ``, `` `int` ``, or `` `long` ``; see intKind |
| `value` | `int` | The value of the integer literal |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only `long` integer literals:

  
 [image: CXM code follows]   

```
    pattern longIntegerLiteral {
        integerIteral {
            .kind == `long`
        }
    };
```
