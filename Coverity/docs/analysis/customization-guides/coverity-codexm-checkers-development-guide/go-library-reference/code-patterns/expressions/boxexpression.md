---
title: "boxExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/boxexpression.html"
content_id: "ivuytzO6Zv7e_XnkF0CrLQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:33.303149+00:00"
---

# boxExpression

Matches box expressions: both boxing a value and unboxing a reference.

This pattern only matches nodes of type `expression`.

## Properties

`boxExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being boxed or unboxed |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all unboxing expressions:

  
 [image: CXM code follows]   

```
    pattern unboxingExpression {
        unboxExpression {
            .unboxMethod == NonNull
        }
    }
```
