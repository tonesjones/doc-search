---
title: "integralLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integralliteral.html"
content_id: "vD~8Pw_7_PXmqYlyNIUQJA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:59.212221+00:00"
---

# integralLiteral

Matches integer literals; that is, all literals of the type `int`, `short`, `long`, or `byte`.

This pattern only matches nodes of type `expression`.

## Properties

`integralLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `base` | `enum` | One of `` `binary` ``, `` `decimal` ``, `` `octal` ``, or `` `hexadecimal` ``. |
| `kind` | Subset of `enum intKind` | One of `` `short` ``, `` `byte` ``, `` `int` ``, or `` `long` ``; see also intKind |
| `value` | `int` | The value of the integer literal |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only `long` integer literals:

[image: CXM code follows]

```
    pattern longIntegerLiteral {
        integralLiteral {
            .kind == `long`
        }
    };
```
