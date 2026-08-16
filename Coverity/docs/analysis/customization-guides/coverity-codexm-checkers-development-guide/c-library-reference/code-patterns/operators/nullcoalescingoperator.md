---
title: "nullCoalescingOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullcoalescingoperator.html"
content_id: "GNuwkHEbSyIoEgiaktTvzg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:12.426959+00:00"
---

# nullCoalescingOperator

Matches the C# null-coalescing operator `??`.

This pattern only matches nodes of type `expression`.

## Properties

`nullCoalescingOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `nonNullExpression` | `expression` | The value to be coalesced. |
| `nullExpression` | `expression` | The value to use if the nullable value is actually `null` |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only null-coalescing of Boolean values:

  
 [image: CXM code follows]   

```
    pattern boolNullCoalescing {
        nullCoalescingOperator {
            .nullExpression == expression {
                .type = booleanType
            }
        }
    };
```
