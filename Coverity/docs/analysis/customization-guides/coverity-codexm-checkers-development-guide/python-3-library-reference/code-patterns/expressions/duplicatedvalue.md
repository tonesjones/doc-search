---
title: "duplicatedValue"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/duplicatedvalue.html"
content_id: "os0kdL7E1z~crKbdp29Bsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:40.088505+00:00"
---

# duplicatedValue

Matches expressions that describe other expressions already referenced in the abstract syntax tree (AST).

Note:
Python itself does not generate this pattern: It is a product of the Coverity AST.

This pattern only matches nodes of type `expression`.

## Properties

`duplicatedValue` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `reusedExpression` | `expression` | The reused expression |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches a reused integer literal expression:

[image: CXM code follows]

```
    pattern reusedInteger {
        duplicatedValue {
            .reusedExpression == integerLiteral
        }
    };
```
