---
title: "boolLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/boolliteral.html"
content_id: "_86WRfOB4C4~JxMlIOb51g"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:35.747078+00:00"
---

# boolLiteral

Matches Boolean literals: that is, either `true` or `false`.

This pattern only matches nodes of type `expression`.

## Properties

`boolLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `enum` | `` `true` `` or `` `false` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all literal `true` Boolean values:

  
 [image: CXM code follows]   

```
    pattern trueBooleanLiteral {
        boolLiteral {
            .value == `true'
        }
    };
```
